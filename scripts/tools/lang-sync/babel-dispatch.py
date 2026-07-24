#!/usr/bin/env python3
"""
babel-dispatch.py — Unified worker-pool translation batch dispatcher.

Replaces three hand-rolled bash dispatchers (dispatch-node-v3.sh /
run-p1-v3.sh / their predecessors) with one Python worker pool where each
worker is a *pinned backend endpoint* — an OpenRouter free model, a
local/remote Ollama node, or codex — driven through translate.py's cascade
orchestrator (`--cascade <spec>` with `--no-preflight`, single backend per
worker so there's no fallback ambiguity about which model actually did the
work).

Ported straight from the two legacy scripts (2026-07-24, still running
alongside this dispatcher — see --order below):
  - verify_group  (hard gate: verify-translation.py + cjk-leak-check.py +
    article-health.py --profile=pre-commit)
  - git_lock_commit (loud commit failure + article-health quarantine
    recovery + single retry, using the SAME lock dir the legacy dispatchers
    use: /tmp/taiwan-md-git.lock — mutual exclusion across all engines)

2026-07-24 orchestrator amendment (founder.md 教訓 "寧可 stale 也不要
missing" — legacy dispatchers' plain `unlink()` on gate-fail turned readable
P1/stale pages into 404s, measured en missing climbing 28→34 in one day):
a gate-fail (or a vanished/never-written output) on a path that exists in
git HEAD restores the HEAD version instead of deleting it — the article
just stays stale and gets retried next round. Only a path with NO HEAD
version (a genuine P0 attempt) gets truly unlinked. See
restore_head_or_quarantine(). This dispatcher does NOT duplicate
scripts/tools/lang-sync/salvage-quarantined.py (which does after-the-fact
git-log archaeology on today's deletions) — it just prevents new
degradations at the point of failure.

Usage:
  python3 scripts/tools/lang-sync/babel-dispatch.py \\
    --langs vi,id,pt,hi \\
    --worker "nemo=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \\
    --worker "gemma31=openrouter:google/gemma-4-31b-it:free" \\
    --worker "mac=ollama:qwen3.6:35b-a3b-coding-nvfp4@http://127.0.0.1:11434" \\
    --order reverse --rounds 50 --commit-every 10

Smoke test:
  python3 scripts/tools/lang-sync/babel-dispatch.py --langs vi \\
    --worker "nemo=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \\
    --order reverse --max-articles 2 --commit-every 2

Design doc: reports/ (this file was scaffolded per an orchestrator brief,
2026-07-24 — see git log for the commit that introduced it).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import threading
import time
from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime
from itertools import zip_longest
from pathlib import Path
from typing import Optional

REPO = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE = REPO / "knowledge"
STATUS_JSON = KNOWLEDGE / "_translation-status.json"
TRANSLATIONS_JSON = KNOWLEDGE / "_translations.json"
GIT_LOCK = Path("/tmp/taiwan-md-git.lock")  # SAME path the legacy bash dispatchers use

sys.path.insert(0, str(Path(__file__).resolve().parent))
from langs import ALL_TRANSLATION_LANGS, ENABLED_TRANSLATION_LANGS  # noqa: E402


# ────────────────────────── logging ──────────────────────────

class Logger:
    """tee-style: every line goes to stdout AND run_dir/master.log."""

    def __init__(self, path: Path):
        self.lock = threading.Lock()
        self.fp = open(path, "a", encoding="utf-8")

    def __call__(self, msg: object = "") -> None:
        text = str(msg)
        with self.lock:
            print(text)
            self.fp.write(text if text.endswith("\n") else text + "\n")
            self.fp.flush()


class JsonlWriter:
    def __init__(self, path: Path):
        self.lock = threading.Lock()
        self.fp = open(path, "a", encoding="utf-8")

    def write(self, obj: dict) -> None:
        with self.lock:
            self.fp.write(json.dumps(obj, ensure_ascii=False) + "\n")
            self.fp.flush()


# ────────────────────────── workers ──────────────────────────

@dataclass
class Worker:
    label: str
    cascade_spec: str            # verbatim --cascade value for translate.py
    host: Optional[str] = None   # OLLAMA_HOST override (only set for ollama+@host)
    model: Optional[str] = None  # OLLAMA_MODEL override (only set for ollama+@host)
    consecutive_failures: int = 0
    frozen_until: Optional[float] = None  # time.monotonic() deadline


def parse_worker_arg(raw: str) -> Worker:
    """label=backendspec[@host]

    backendspec is passed to translate.py --cascade verbatim (the @host
    suffix is always stripped first). If @host is present AND backendspec
    starts with `ollama`, OLLAMA_HOST/OLLAMA_MODEL env vars are set for that
    worker's subprocesses instead, and the cascade spec collapses to the
    bare `ollama` token (translate.py's build_cascade() falls back to
    os.environ["OLLAMA_MODEL"] in that case).
    """
    if "=" not in raw:
        raise SystemExit(f"--worker must be 'label=backendspec[@host]', got: {raw!r}")
    label, _, rest = raw.partition("=")
    spec, sep, host_raw = rest.partition("@")
    label = label.strip()
    spec = spec.strip()
    host_raw = host_raw.strip() if sep else ""
    if not label or not spec:
        raise SystemExit(f"--worker must be 'label=backendspec[@host]', got: {raw!r}")

    host = model = None
    cascade_spec = spec
    if host_raw and spec.startswith("ollama"):
        _, _, model_part = spec.partition(":")
        model = model_part or None
        host = host_raw
        cascade_spec = "ollama"

    return Worker(label=label, cascade_spec=cascade_spec, host=host, model=model)


def worker_env(worker: Worker) -> dict:
    """Per-subprocess env (never mutates os.environ — workers run concurrently
    and may point at different Ollama hosts)."""
    env = os.environ.copy()
    if worker.host:
        env["OLLAMA_HOST"] = worker.host
        if worker.model:
            env["OLLAMA_MODEL"] = worker.model
    return env


# ────────────────────────── git lock + commit (ported from dispatch-node-v3.sh) ──────────────────────────

def git_lock_commit(lang: str, worker_labels: set, files: list, log: Logger) -> bool:
    """mkdir-lock /tmp/taiwan-md-git.lock (120x1s retry, shared with the
    legacy bash dispatchers) → git add <the exact files THIS dispatcher
    verified ok> + the two derived JSONs → commit. Commit failure is LOUD
    (printed, not swallowed) + article-health quarantine recovery + single
    retry — ported from dispatch-node-v3.sh git_lock_commit(), with two
    amendments discovered during the 2026-07-24 smoke test:

    1. `git add knowledge/{lang}/` (the legacy directory-wide pattern) swept
       in the CONCURRENTLY-RUNNING legacy fleet dispatcher's not-yet-committed
       files (it targets the same knowledge/vi/ tree). When the pre-commit
       hook then rejected the batch, the recovery block deleted two files
       that belonged to that OTHER process, not this one — real data loss
       for a process this dispatcher has no authority over. Scoping `git add`
       to exactly the paths this run itself verified eliminates that cross-
       engine blast radius entirely.
    2. The recovery block's raw `unlink()` on a staged-but-failing file hits
       the same founder.md problem the per-article HEAD-restore amendment
       exists for: `.lintstagedrc` runs `prettier --write` on staged files
       BEFORE `article-health.py --staged` checks them, so a translation
       that passed the pre-staging single-file gate can still fail here post-
       reformat. Recovery now goes through restore_head_or_quarantine() too.
    """
    n_files = len(files)
    tries = 0
    while True:
        try:
            GIT_LOCK.mkdir()
            break
        except FileExistsError:
            tries += 1
            if tries > 120:
                log(f"🔴 git lock timeout, skipping commit this round ({lang})")
                return False
            time.sleep(1)

    try:
        subprocess.run(
            ["git", "add", *files,
             "knowledge/_translation-status.json", "knowledge/_translations.json"],
            cwd=REPO, capture_output=True, text=True,
        )
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO).returncode == 0:
            return True  # nothing staged, nothing to do

        workers_str = "+".join(sorted(worker_labels)) if worker_labels else "unknown"
        msg = f"🧬 [semiont] babel: {lang} 批次 {n_files} 篇（unified dispatcher, worker={workers_str}）"
        commit = subprocess.run(["git", "commit", "-m", msg], cwd=REPO, capture_output=True, text=True)
        if commit.returncode == 0:
            log(f"✅ committed {lang} ({n_files} files, worker={workers_str})")
            return True

        log(f"🔴 COMMIT FAILED for {lang} — pre-commit rejected staged batch, attempting recovery")
        log((commit.stdout + commit.stderr)[-4000:])

        staged = subprocess.run(
            ["git", "diff", "--cached", "--name-only"], cwd=REPO, capture_output=True, text=True
        ).stdout.splitlines()
        staged_md = [f for f in staged if f.startswith("knowledge/") and f.endswith(".md")]
        bad = []
        for f in staged_md:
            r = subprocess.run(
                ["python3", "scripts/tools/article-health.py", f, "--profile=pre-commit", "--quiet"],
                cwd=REPO, capture_output=True, text=True,
            )
            if "passed=False" in r.stdout:
                bad.append(f)
        log(f"recovery: {len(bad)}/{len(staged_md)} staged files fail article-health, quarantining")
        for f in bad:
            subprocess.run(["git", "restore", "--staged", f], cwd=REPO, capture_output=True, text=True)
            disposition = restore_head_or_quarantine(f, log)
            log(f"  {disposition}: {f}")

        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO).returncode != 0:
            msg2 = (f"🧬 [semiont] babel: {lang} 批次 {n_files} 篇"
                    f"（unified dispatcher, worker={workers_str}，post-quarantine retry）")
            commit2 = subprocess.run(["git", "commit", "-m", msg2], cwd=REPO, capture_output=True, text=True)
            if commit2.returncode == 0:
                log("✅ recovery commit succeeded")
            else:
                log("🔴 recovery commit STILL failed — needs manual intervention, leaving staged")
                log((commit2.stdout + commit2.stderr)[-4000:])
        return True
    finally:
        try:
            GIT_LOCK.rmdir()
        except OSError:
            pass


# ────────────────────────── verify trio + HEAD-restore (ported + amended) ──────────────────────────

def verify_one(zh_path: str, trans_path: str, log: Logger) -> tuple[bool, Optional[str]]:
    """The hard gate: verify-translation.py + cjk-leak-check.py +
    article-health.py --profile=pre-commit. Ported from dispatch-node-v3.sh
    verify_group() (per-article body), minus the unlink side effect — the
    caller decides disposition via restore_head_or_quarantine()."""
    r1 = subprocess.run(
        ["python3", "scripts/tools/lang-sync/verify-translation.py", zh_path, trans_path, "--json"],
        cwd=REPO, capture_output=True, text=True,
    )
    try:
        out1 = json.loads(r1.stdout)
    except Exception:
        out1 = {"fails": -1}
    r2 = subprocess.run(
        ["python3", "scripts/tools/lang-sync/cjk-leak-check.py", trans_path],
        cwd=REPO, capture_output=True, text=True,
    )
    leak_fail = r2.returncode != 0
    r3 = subprocess.run(
        ["python3", "scripts/tools/article-health.py", trans_path, "--profile=pre-commit", "--quiet"],
        cwd=REPO, capture_output=True, text=True,
    )
    health_fail = "passed=False" in r3.stdout
    ok = out1.get("fails", 1) == 0 and not leak_fail and not health_fail
    if ok:
        return True, None
    reason = "health" if health_fail else ("leak" if leak_fail else f"verify={out1.get('fails')}")
    log(f"❌ GATE FAIL {trans_path} ({reason})")
    return False, reason


def restore_head_or_quarantine(path_str: str, log: Logger) -> str:
    """2026-07-24 orchestrator amendment (founder.md 「寧可 stale 也不要
    missing」). Called whenever a translated file is in a bad state after a
    worker's attempt (gate-fail on a produced file, OR the file vanished /
    was never written — e.g. translate.py's own too-small-output unlink,
    which can destroy a just-overwritten stale HEAD version before our
    external verify even runs).

    - If `path_str` exists in git HEAD: restore that exact version. The
      working tree then byte-matches HEAD, so the later `git add` stages
      nothing for this path — the article silently stays stale and is
      retried next round.
    - Only if HEAD has no such path (a genuine P0 attempt that never had a
      committed translation) does this actually unlink → true quarantine,
      article returns to the missing list.

    Returns "restored" | "unlinked".
    """
    p = REPO / path_str
    check = subprocess.run(
        ["git", "cat-file", "-e", f"HEAD:{path_str}"], cwd=REPO, capture_output=True
    )
    if check.returncode == 0:
        show = subprocess.run(
            ["git", "show", f"HEAD:{path_str}"], cwd=REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if show.returncode == 0:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(show.stdout)
            log(f"♻️  restored {path_str} to HEAD version (寧可 stale 也不要 missing)")
            return "restored"
        log(f"⚠️  {path_str}: in HEAD but `git show` failed — unlinking as fallback")
    p.unlink(missing_ok=True)
    return "unlinked"


# ────────────────────────── round-state ──────────────────────────

class RunState:
    def __init__(self):
        self.lock = threading.Lock()
        self.pending_ok: dict = defaultdict(int)          # lang -> count since last commit
        self.pending_workers: dict = defaultdict(set)     # lang -> {worker labels} since last commit
        self.pending_files: dict = defaultdict(list)      # lang -> [trans_path] since last commit — the
                                                            # ONLY paths git_lock_commit is allowed to add
                                                            # (never a directory wildcard — see git_lock_commit
                                                            # docstring, 2026-07-24 cross-engine incident)
        self.last_worker: dict = {}                       # "lang:zh" -> worker label (soft retry-avoid)
        self.quarantine_log: dict = defaultdict(set)       # lang -> {zh_path} — audit trail only, NOT
                                                            # used to exclude future rounds: status.py's
                                                            # own re-scan (missing after unlink / unchanged
                                                            # after restore) already makes the article
                                                            # reappear next round, which is the explicitly
                                                            # desired "retried next round" behavior.
        self.in_flight: set = set()                        # "lang:zh" currently dispatched (claim protocol)


class TaskQueue:
    """Shared round queue. Tasks are (lang, group_path, zh_path). claim()
    applies a soft last-worker-avoidance preference (2026-07-24 amendment
    spec: quarantined articles "retried next round, preferably by a
    different worker")."""

    def __init__(self, tasks: list):
        self._dq = deque(tasks)
        self._lock = threading.Lock()

    def claim(self, worker_label: str, last_worker: dict):
        with self._lock:
            n = len(self._dq)
            for _ in range(n):
                task = self._dq.popleft()
                lang, _gpath, zh_path = task
                if last_worker.get(f"{lang}:{zh_path}") == worker_label and self._dq:
                    self._dq.append(task)  # try to give it to someone else first
                    continue
                return task
            return None

    def __len__(self):
        with self._lock:
            return len(self._dq)


# ────────────────────────── status / worklist ──────────────────────────

def refresh_status(log: Logger) -> dict:
    r = subprocess.run(
        ["python3", "scripts/tools/lang-sync/status.py"], cwd=REPO, capture_output=True, text=True
    )
    log(r.stdout.strip())
    if r.returncode != 0:
        log(f"⚠️  status.py refresh exit={r.returncode}\n{r.stderr[-1000:]}")
    return json.loads(STATUS_JSON.read_text(encoding="utf-8"))


def default_langs(status_data: dict) -> list:
    result = []
    for lang in ENABLED_TRANSLATION_LANGS:
        s = status_data["_meta"]["summary"].get(lang, {})
        if s.get("missing", 0) > 0 or s.get("stale", 0) > 0 or s.get("metadata_stale", 0) > 0:
            result.append(lang)
    return result


def build_worklist(status_data: dict, lang: str, priority: str, order: str) -> list:
    by_article = status_data["byArticle"]
    p0, p1 = [], []
    for zh, info in by_article.items():
        t = info.get("translations", {}).get(lang, {})
        st = t.get("status")
        if st == "missing":
            p0.append((zh, info["zh"]["lastModified"]))
        elif st in ("stale", "metadata-stale"):
            p1.append((zh, info["zh"]["lastModified"]))
    p0.sort(key=lambda x: x[1], reverse=True)  # newest zh edit first (matches prepare-batch.py --top order)
    p1.sort(key=lambda x: x[1], reverse=True)
    if order == "reverse":
        p0 = list(reversed(p0))
        p1 = list(reversed(p1))
    p0_paths = [z for z, _ in p0]
    p1_paths = [z for z, _ in p1]
    if priority == "p0":
        return p0_paths
    if priority == "p1":
        return p1_paths
    return p0_paths + p1_paths  # all: P0 first, then P1


def build_slug_map(run_dir: Path) -> Path:
    """From knowledge/_translations.json: for every zh_path that has an
    en/... entry, slug = basename of the en file without .md. Shared across
    all target langs (site convention: slug is the same file basename
    regardless of target language)."""
    trans = json.loads(TRANSLATIONS_JSON.read_text(encoding="utf-8"))
    slug_map = {}
    for en_key, zh_val in trans.items():
        if en_key.startswith("en/"):
            slug_map[zh_val] = Path(en_key).stem
    out = run_dir / "slug-map.json"
    out.write_text(json.dumps(slug_map, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


def run_prepare_batch(lang: str, zh_paths: list, slug_map_path: Path, round_dir: Path, log: Logger) -> None:
    round_dir.mkdir(parents=True, exist_ok=True)
    worklist_file = round_dir / "worklist.txt"
    worklist_file.write_text("\n".join(zh_paths) + "\n", encoding="utf-8")
    cmd = [
        "python3", "scripts/tools/lang-sync/prepare-batch.py",
        "--lang", lang, "--input", str(worklist_file),
        "--groups", str(len(zh_paths)),          # one group == one article: gives us per-article
        "--slug-map", str(slug_map_path),         # dispatch/timing/report granularity for free
        "--outdir", str(round_dir),
    ]
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    log(f"prepare-batch {lang}: exit={r.returncode}")
    log(r.stdout[-1500:])
    if r.returncode not in (0, 2):  # 2 = "some slugs fell back to ASCII placeholder", non-fatal
        log(f"⚠️  prepare-batch {lang} unexpected exit {r.returncode}\n{r.stderr[-1000:]}")


def collect_and_filter_groups(round_dir: Path, lang: str, seen_missing_slug: set, log: Logger) -> list:
    """Post-process prepare-batch.py's output: drop groups whose slug
    resolution failed (TBD-NEEDS-SLUG, logged once per zh_path for the whole
    run), plus cross-engine dedupe with concurrent dispatchers writing the
    same knowledge/{lang}/ tree.

    Dedupe rule is STATUS-AWARE (2026-07-24 v2 — v1 skipped on bare file
    existence, which is wrong for stale work: a stale article's target file
    exists BY DEFINITION, so the classic-langs run skipped its entire P1
    worklist, queueing 14 of ~600). Now:
      - status "missing": file exists >1KB → another engine just created it;
        skip, next round's status refresh reconciles.
      - stale flavors: file existing is the norm; skip only when its mtime is
        within the last 10 min (a concurrent engine just rewrote it)."""
    good = []
    now = time.time()
    for gf in sorted(round_dir.glob("_group-*.json")):
        data = json.loads(gf.read_text(encoding="utf-8"))
        arts = data.get("articles", [])
        if not arts:
            continue
        art = arts[0]
        zh_path, en_path = art["zh_path"], art["en_path"]
        status = art.get("status", "missing")
        if "TBD-NEEDS-SLUG" in en_path:
            key = f"{lang}:{zh_path}"
            if key not in seen_missing_slug:
                seen_missing_slug.add(key)
                log(f"⚠️  skip {zh_path} ({lang}): slug resolution failed (TBD-NEEDS-SLUG) — needs --slug-map entry")
            continue
        target = REPO / en_path
        if target.exists() and target.stat().st_size > 1024:
            if status == "missing":
                log(f"⏭️  skip {zh_path} ({lang}): {en_path} already exists (cross-engine dedupe, was missing)")
                continue
            if now - target.stat().st_mtime < 600:
                log(f"⏭️  skip {zh_path} ({lang}): {en_path} rewritten <10min ago (cross-engine dedupe)")
                continue
        good.append((lang, gf, zh_path))
    return good


def interleave_by_lang(per_lang_tasks: dict) -> list:
    """Round-robin across langs so no lang starves a slow one."""
    tasks = []
    iters = [iter(v) for v in per_lang_tasks.values()]
    for row in zip_longest(*iters, fillvalue=None):
        for item in row:
            if item is not None:
                tasks.append(item)
    return tasks


# ────────────────────────── dispatch ──────────────────────────

def do_commit(lang: str, state: RunState, no_commit: bool, log: Logger) -> None:
    with state.lock:
        n = state.pending_ok[lang]
        workers = set(state.pending_workers[lang])
        files = list(state.pending_files[lang])
        state.pending_ok[lang] = 0
        state.pending_workers[lang] = set()
        state.pending_files[lang] = []
    if n == 0:
        return
    if no_commit:
        log(f"⏭️  --no-commit: would commit {lang} batch of {n} (workers={sorted(workers)}) files={files}")
        return
    # Refresh derived JSONs FIRST, then take the lock and commit (matches
    # legacy invariant: status/translations caches never lag behind the
    # commit that introduces the files they describe).
    subprocess.run(["python3", "scripts/tools/sync-translations-json.py"], cwd=REPO, capture_output=True, text=True)
    subprocess.run(["python3", "scripts/tools/lang-sync/status.py"], cwd=REPO, capture_output=True, text=True)
    git_lock_commit(lang, workers, files, log)


def process_task(worker: Worker, lang: str, group_path: Path, zh_path: str,
                  state: RunState, report: JsonlWriter, freezes: JsonlWriter,
                  no_commit: bool, commit_every: int, log: Logger) -> None:
    data = json.loads(group_path.read_text(encoding="utf-8"))
    trans_path = data["articles"][0]["en_path"]

    t0 = time.monotonic()
    # --lang MUST be explicit: translate.py's --group mode defaults to
    # `lang = args.lang or group_path.parent.name`, and our run-dir layout is
    # tasks/{lang}/round{N}/_group-*.json — parent.name is "round01", not the
    # lang. Without this, LANG_NAMES.get(lang, lang) silently falls through to
    # the literal string "round01" as the target-language name in the
    # translation prompt (caught in the first smoke-test run — 2/2 verify
    # failures, both explained by this bug once inspected).
    cmd = ["python3", "-u", "scripts/tools/lang-sync/translate.py",
           "--group", str(group_path), "--lang", lang,
           "--cascade", worker.cascade_spec, "--no-preflight"]
    proc = subprocess.run(cmd, cwd=REPO, env=worker_env(worker), capture_output=True, text=True)
    elapsed = time.monotonic() - t0

    log(f"--- worker={worker.label} lang={lang} zh={zh_path} exit={proc.returncode} ({elapsed:.0f}s) ---")
    tail = (proc.stdout + ("\n" + proc.stderr if proc.returncode != 0 else ""))
    log(tail[-3000:])

    target = REPO / trans_path
    produced_by_backend = target.exists() and target.stat().st_size > 0  # BEFORE any restore — worker-health signal

    if not target.exists():
        disposition = restore_head_or_quarantine(trans_path, log)
        ok, fail_reason = False, f"no output written by translate.py (exit={proc.returncode})"
    else:
        # Normalize with prettier BEFORE the verify trio, so the gates measure
        # the same bytes the commit-time hook will see: .lintstagedrc runs
        # `prettier --write` on staged files BEFORE `article-health --staged`,
        # so un-normalized output can pass the single-file gate and still fail
        # at commit (2026-07-24 smoke test: 0 issues pre-stage → 11
        # footnote-format violations post-prettier on the same file).
        subprocess.run(["npx", "prettier", "--write", trans_path],
                       cwd=REPO, capture_output=True, text=True)
        ok, fail_reason = verify_one(zh_path, trans_path, log)
        disposition = "kept" if ok else restore_head_or_quarantine(trans_path, log)

    report.write({
        "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
        "lang": lang, "zh": zh_path, "trans": trans_path,
        "worker": worker.label, "ok": ok, "seconds": round(elapsed, 1),
        "fail_reason": fail_reason, "disposition": disposition,
    })

    with state.lock:
        state.last_worker[f"{lang}:{zh_path}"] = worker.label
        if not ok:
            state.quarantine_log[lang].add(zh_path)
        state.in_flight.discard(f"{lang}:{zh_path}")

    # Worker health: 3 consecutive hard failures (exit!=0 AND the backend
    # never even produced a file) → freeze 30min. A gate-fail on output the
    # backend DID produce is a quality issue, not a worker-availability
    # issue, so it does not count here.
    hard_fail = proc.returncode != 0 and not produced_by_backend
    if hard_fail:
        worker.consecutive_failures += 1
        if worker.consecutive_failures >= 3:
            worker.frozen_until = time.monotonic() + 30 * 60
            worker.consecutive_failures = 0
            freezes.write({
                "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
                "worker": worker.label, "reason": "3 consecutive hard failures (no output produced)",
                "frozen_for_s": 1800,
            })
            log(f"🥶 FREEZE worker={worker.label} for 30min — 3 consecutive hard failures")
    else:
        worker.consecutive_failures = 0

    if ok:
        with state.lock:
            state.pending_ok[lang] += 1
            state.pending_workers[lang].add(worker.label)
            state.pending_files[lang].append(trans_path)
            reached = state.pending_ok[lang] >= commit_every
        if reached:
            do_commit(lang, state, no_commit, log)


def wait_if_frozen(worker: Worker, workers: list, log: Logger) -> None:
    while True:
        now = time.monotonic()
        if not worker.frozen_until or now >= worker.frozen_until:
            return
        if all(w.frozen_until and w.frozen_until > now for w in workers):
            log("🥶 all workers frozen — sleeping 5min (work still queued)")
            time.sleep(300)
        else:
            time.sleep(10)


def worker_loop(worker: Worker, workers: list, queue: TaskQueue, state: RunState,
                 report: JsonlWriter, freezes: JsonlWriter, no_commit: bool,
                 commit_every: int, log: Logger) -> None:
    while True:
        wait_if_frozen(worker, workers, log)
        with state.lock:
            last_worker_snapshot = dict(state.last_worker)
        task = queue.claim(worker.label, last_worker_snapshot)
        if task is None:
            return
        lang, group_path, zh_path = task
        with state.lock:
            state.in_flight.add(f"{lang}:{zh_path}")
        process_task(worker, lang, group_path, zh_path, state, report, freezes, no_commit, commit_every, log)


# ────────────────────────── main ──────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Unified worker-pool translation batch dispatcher (replaces the hand-rolled "
                     "bash dispatchers dispatch-node-v3.sh / run-p1-v3.sh).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""example:
  python3 scripts/tools/lang-sync/babel-dispatch.py \\
    --langs vi,id,pt,hi \\
    --worker "nemo=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \\
    --worker "gemma31=openrouter:google/gemma-4-31b-it:free" \\
    --worker "laguna=openrouter:poolside/laguna-xs-2.1:free" \\
    --worker "mac=ollama:qwen3.6:35b-a3b-coding-nvfp4@http://127.0.0.1:11434" \\
    --order reverse --rounds 50 --commit-every 10
""",
    )
    ap.add_argument("--langs", default=None,
                     help="comma-separated target langs (default: ENABLED_TRANSLATION_LANGS "
                          "with any missing/stale)")
    ap.add_argument("--worker", action="append", dest="workers", default=[],
                     metavar="label=backendspec[@host]",
                     help="repeatable. backendspec passed to translate.py --cascade verbatim "
                          "(stripped of @host first). @host + ollama backend → OLLAMA_HOST/"
                          "OLLAMA_MODEL env for that worker's subprocesses.")
    ap.add_argument("--order", choices=["reverse", "forward"], default="reverse",
                     help="reverse (default) = process each priority's worklist from the tail "
                          "(anti-collision vs legacy dispatchers, which eat from the head)")
    ap.add_argument("--rounds", type=int, default=50)
    ap.add_argument("--commit-every", type=int, default=10,
                     help="commit after this many verified-ok files per lang (also flushed at "
                          "end of each round)")
    ap.add_argument("--max-articles", type=int, default=None, help="global cap across the whole run (smoke tests)")
    ap.add_argument("--no-commit", action="store_true", help="skip git commit (smoke tests)")
    ap.add_argument("--priority", choices=["p0", "p1", "all"], default="all",
                     help="p0=missing only, p1=stale+metadata-stale only, all=P0 first then P1 (default)")
    args = ap.parse_args()

    if not args.workers:
        ap.error("at least one --worker is required")
    workers = [parse_worker_arg(w) for w in args.workers]
    labels = [w.label for w in workers]
    if len(labels) != len(set(labels)):
        ap.error(f"--worker labels must be unique, got: {labels}")

    if args.langs:
        langs_requested = [x.strip() for x in args.langs.split(",") if x.strip()]
        for l in langs_requested:
            if l not in ALL_TRANSLATION_LANGS:
                ap.error(f"unknown lang {l!r} — not in langs.py ALL_TRANSLATION_LANGS {ALL_TRANSLATION_LANGS}")
    else:
        langs_requested = None  # resolved after first status refresh

    run_dir = Path(f"/tmp/babel-unified-{datetime.now().strftime('%Y%m%d-%H%M')}")
    run_dir.mkdir(parents=True, exist_ok=True)
    print(run_dir)  # run dir path — first thing printed, per spec

    log = Logger(run_dir / "master.log")
    report = JsonlWriter(run_dir / "report.jsonl")
    freezes = JsonlWriter(run_dir / "freezes.jsonl")

    log(f"START babel-dispatch.py {datetime.now().astimezone().isoformat(timespec='seconds')}")
    log(f"  run_dir={run_dir}")
    log(f"  workers={[(w.label, w.cascade_spec, w.host) for w in workers]}")
    log(f"  order={args.order} rounds={args.rounds} commit_every={args.commit_every} "
        f"priority={args.priority} max_articles={args.max_articles} no_commit={args.no_commit}")

    state = RunState()
    seen_missing_slug: set = set()
    total_enqueued = 0

    for round_num in range(1, args.rounds + 1):
        log(f"\n===== ROUND {round_num} {datetime.now().astimezone().isoformat(timespec='seconds')} =====")
        status_data = refresh_status(log)

        langs = langs_requested or default_langs(status_data)
        if not langs:
            log("No target langs (nothing missing/stale anywhere) — done.")
            break

        slug_map_path = build_slug_map(run_dir)

        remaining_budget = None
        if args.max_articles is not None:
            remaining_budget = args.max_articles - total_enqueued
            if remaining_budget <= 0:
                log(f"max-articles budget ({args.max_articles}) exhausted — stopping.")
                break

        per_lang_tasks: dict = {}
        for lang in langs:
            worklist = build_worklist(status_data, lang, args.priority, args.order)
            cap = 10 * len(workers)
            if remaining_budget is not None:
                cap = min(cap, remaining_budget - sum(len(v) for v in per_lang_tasks.values()))
            worklist = worklist[: max(cap, 0)]
            if not worklist:
                continue
            round_dir = run_dir / "tasks" / lang / f"round{round_num:02d}"
            run_prepare_batch(lang, worklist, slug_map_path, round_dir, log)
            groups = collect_and_filter_groups(round_dir, lang, seen_missing_slug, log)
            if groups:
                per_lang_tasks[lang] = groups

        if not per_lang_tasks:
            log("All target langs have empty worklists this round — done.")
            break

        tasks = interleave_by_lang(per_lang_tasks)
        total_enqueued += len(tasks)
        log(f"Round {round_num}: {len(tasks)} article(s) queued across {len(per_lang_tasks)} lang(s) "
            f"({', '.join(f'{l}={len(v)}' for l, v in per_lang_tasks.items())})")

        queue = TaskQueue(tasks)
        with ThreadPoolExecutor(max_workers=len(workers)) as pool:
            futures = [
                pool.submit(worker_loop, w, workers, queue, state, report, freezes,
                            args.no_commit, args.commit_every, log)
                for w in workers
            ]
            for f in futures:
                f.result()

        # End-of-round flush: commit whatever's pending even if under threshold.
        for lang in list(per_lang_tasks.keys()):
            do_commit(lang, state, args.no_commit, log)

        if args.max_articles is not None and total_enqueued >= args.max_articles:
            log(f"max-articles budget ({args.max_articles}) reached after round {round_num} — stopping.")
            break
    else:
        log(f"Reached --rounds limit ({args.rounds}) without exhausting the worklist.")

    log("\n===== FINAL STATUS =====")
    final = refresh_status(log)
    for lang in (langs_requested or default_langs(final)) or ENABLED_TRANSLATION_LANGS:
        s = final["_meta"]["summary"].get(lang)
        if s:
            log(f"  {lang}: fresh={s['fresh']} stale={s['stale']} missing={s['missing']} "
                f"metadata_stale={s.get('metadata_stale', 0)}")
    log(f"quarantine_log this run: {dict((k, sorted(v)) for k, v in state.quarantine_log.items())}")
    log("DONE")


if __name__ == "__main__":
    main()
