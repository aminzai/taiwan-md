#!/usr/bin/env python3
"""
routine-liveness-check.py — fire-vs-commit 對賬：抓 routine 的沉默死亡

per weekly-deep-review 2026-07-10 §五 + evolution-roadmap P0-1：
scheduler 的 lastRunAt 只證明扳機被按下；routine 真正的完成證明是 git 痕跡。
機器睡眠或 cron 環境層病可以讓 session 在 fire 後無聲死亡——routine-status.sh
靠 memory 檔偵測 fire，所以「該來沒來的班」完全不可見；scheduler 又只記扳機。
兩個資料源各自誠實，交叉才見屍體（2026-07-10 morning chain 六連沉默死亡 vc=2，
前例 2026-07-04 rewrite-daily，LESSONS `routine-fire-vs-git-trace-silent-death`）。

資料源：
  - docs/semiont/routine-live-state.json（scheduler dump，data-refresh rider 每日更新）
  - git log（fire 之後 TRACE_WINDOW 小時內找該 routine 的 commit 痕跡）

判定（對最近一次 lastRunAt）：
  ✅ traced        fire 後 TRACE_WINDOW 內有對應 tag 的 commit
  🕐 in-grace      fire 距今 < GRACE_HOURS，session 可能還在跑，不判
  🔴 silent-death  fire 距今 ≥ GRACE_HOURS 且窗口內零 git 痕跡
  🟠 unregistered  taskId 不在 TAG_PATTERNS，本工具沒有它的 grep pattern → 看不見不等於沒跑
  ⏸️ disabled      live enabled=false，跳過
  ⚪ stale-dump    dump 本身超過 DUMP_STALE_HOURS，先跑 routine-live-normalize.py

用法：
  python3 scripts/tools/routine-liveness-check.py            # 人讀表
  python3 scripts/tools/routine-liveness-check.py --json     # 給 generate-dashboard-alerts.mjs
  python3 scripts/tools/routine-liveness-check.py --grace 2  # 覆寫 grace（小時）

下游消費者：
  - WEEKLY-REPORT-PIPELINE v4.0 Stage 2.5a（週體檢診斷面 a）
  - generate-dashboard-alerts.mjs（silent-death → yellow alert，owner=該 routine）
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LIVE_STATE = REPO_ROOT / "docs" / "semiont" / "routine-live-state.json"

GRACE_HOURS = 3        # fire 後多久內不判（session 可能還在跑）
TRACE_WINDOW_HOURS = 6  # fire 後多久內找 git 痕跡
DUMP_STALE_HOURS = 48   # dump 超齡警告（sync-check 同一條線）

# taskId → git log subject 的 grep pattern（跟 memory 檔 handle / commit 標記一致）
# 新 routine 誕生時必須同 commit 補這張表（REFLEXES #43 家族：新器官必須進 sensor 視野）
TAG_PATTERNS: dict[str, list[str]] = {
    "twmd-data-refresh-am": ["data-refresh-am", "twmd-data-refresh-am"],
    "twmd-data-refresh-pm": ["data-refresh-pm", "twmd-data-refresh-pm"],
    "twmd-babel-nightly": ["twmd-babel"],
    "twmd-embeddings-nightly": ["embeddings"],
    "twmd-maintainer-daily": [
        "twmd-maintainer-daily", "maintainer-daily",
        "twmd-maintainer-am", "maintainer-am", "twmd-maintainer:",
    ],
    "twmd-maintainer-pm": ["twmd-maintainer-pm", "maintainer-pm"],
    "twmd-spore-harvest-am": ["twmd-spore-harvest", "spore-harvest"],
    "taiwanmd-routine-twmd-feedback-triage": ["twmd-feedback-triage", "feedback-triage"],
    "twmd-rewrite-daily": ["twmd-rewrite-daily", "rewrite-daily", "[semiont] rewrite:", "[routine] rewrite:"],
    "twmd-news-lens-weekly": ["news-lens"],
    "twmd-weekly-report-sun": ["weekly-report", "twmd-weekly-report", "report: weekly"],
    "twmd-distill-weekly": ["distill"],
    "twmd-self-evolve-weekly": ["self-evolve"],
    "twmd-routine-audit-weekly": ["routine-audit"],
    "twmd-spore-pick-daily": ["spore-pick"],
    "twmd-spore-publish-daily": ["spore-publish"],
    "twmd-routine-sync": ["twmd-routine-sync"],
    "twmd-supporters-weekly": ["twmd-supporters-weekly", "supporters"],
    "twmd-music-media-audit-weekly": ["music-media-audit"],
    # 這兩條的 taskId 帶 cadence 後綴，commit 標記不帶（commit 寫 `twmd-terminology-trends:`）。
    # 沒登記時 fallback 拿 taskId 全字去 grep，永遠對不上，每月照報一次沉默死亡。
    "twmd-terminology-trends-monthly": ["twmd-terminology-trends", "terminology-trends"],
    "twmd-founder-lens-weekly": ["twmd-founder-lens", "founder-lens"],
}


def _git_subjects(since: datetime, until: datetime) -> list[str]:
    """每個 commit 一行：`<hash> <subject> | <改到的 memory 檔名>`。

    2026-08-18 補 memory 檔名（`--name-only` 只取 docs/semiont/memory/ 下的檔）：
    self-evolve-weekly 8/16 04:20 的兩個 commit 標題是 `[routine] evolve: …升 REFLEXES #91`
    與 `[routine] heal: 補上自身 commit hash`，memory 檔跟 evolve 同一個 commit、沒有獨立的
    `[routine] memory: twmd-self-evolve-weekly @ …`——只 grep subject 就得到「零 git 痕跡」，
    黃燈掛了兩天而 routine 明明跑完了。memory 檔名帶 handle 是 MEMORY-PIPELINE 的 canonical
    命名（`YYYY-MM-DD-HHMMSS-{handle}.md`），比 commit 標題可靠；subject 仍保留給
    沒寫 memory 只 ship 的 routine。同族：LESSONS `routine-audit-classifier-memory-commit-misattribution`。
    """
    out = subprocess.run(
        [
            "git", "log",
            f"--since={since.isoformat()}",
            f"--until={until.isoformat()}",
            "--pretty=format:@@%h %s",
            "--name-only",
        ],
        cwd=REPO_ROOT, capture_output=True, text=True, check=False,
    )
    lines: list[str] = []
    cur: str | None = None
    mem: list[str] = []

    def _flush() -> None:
        if cur is not None:
            lines.append(cur + (" | " + " ".join(mem) if mem else ""))

    for raw in out.stdout.splitlines():
        if raw.startswith("@@"):
            _flush()
            cur, mem = raw[2:], []
        elif raw.strip() and cur is not None and raw.startswith("docs/semiont/memory/"):
            mem.append(raw.rsplit("/", 1)[-1])
    _flush()
    return [l for l in lines if l.strip()]


def check(grace_hours: float, window_hours: float) -> dict:
    if not LIVE_STATE.exists():
        return {"error": f"{LIVE_STATE} 不存在 — 先跑 routine-live-normalize.py"}

    state = json.loads(LIVE_STATE.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    fetched = datetime.fromisoformat(state.get("fetched_at", "1970-01-01T00:00:00+00:00"))
    dump_age_h = (now - fetched).total_seconds() / 3600

    results = []
    for t in state.get("tasks", []):
        task_id = t.get("taskId", "?")
        if not t.get("enabled", False):
            results.append({"taskId": task_id, "status": "disabled"})
            continue
        last_run = t.get("lastRunAt")
        if not last_run:
            results.append({"taskId": task_id, "status": "never-ran"})
            continue

        fire = datetime.fromisoformat(last_run.replace("Z", "+00:00"))
        age_h = (now - fire).total_seconds() / 3600

        if age_h < grace_hours:
            results.append({"taskId": task_id, "status": "in-grace",
                            "firedAt": last_run, "ageHours": round(age_h, 1)})
            continue

        # 沒登記在 TAG_PATTERNS 的 routine，以前靜默 fallback 成拿 taskId 全字去 grep：
        # 對不上就報沉默死亡，跟真的死掉長得一模一樣（REFLEXES #85「不知道」不能借用「沒事」
        # 或「出事」的符號）。現在讓它自己說出「我沒有這條的 pattern」。
        registered = task_id in TAG_PATTERNS
        patterns = TAG_PATTERNS.get(task_id, [task_id])
        subjects = _git_subjects(fire, fire + timedelta(hours=window_hours))
        hits = [s for s in subjects
                if any(p.lower() in s.lower() for p in patterns)]

        if hits:
            status = "traced"
        elif not registered:
            status = "unregistered"
        else:
            status = "silent-death"

        results.append({
            "taskId": task_id,
            "status": status,
            "registered": registered,
            "firedAt": last_run,
            "ageHours": round(age_h, 1),
            "evidence": hits[0] if hits else None,
        })

    return {
        "checkedAt": now.isoformat(),
        "dumpFetchedAt": state.get("fetched_at"),
        "dumpAgeHours": round(dump_age_h, 1),
        "dumpStale": dump_age_h > DUMP_STALE_HOURS,
        "graceHours": grace_hours,
        "traceWindowHours": window_hours,
        "silentDeaths": sum(1 for r in results if r["status"] == "silent-death"),
        "unregistered": sum(1 for r in results if r["status"] == "unregistered"),
        "results": results,
    }


ICONS = {"traced": "✅", "in-grace": "🕐", "silent-death": "🔴",
         "disabled": "⏸️", "never-ran": "❓", "unregistered": "🟠"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--grace", type=float, default=GRACE_HOURS)
    ap.add_argument("--window", type=float, default=TRACE_WINDOW_HOURS)
    args = ap.parse_args()

    report = check(args.grace, args.window)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    if "error" in report:
        print(f"⚠️  {report['error']}")
        return 1

    print("🧬 routine-liveness-check — fire-vs-commit 對賬"
          f"（dump 齡 {report['dumpAgeHours']}h"
          f"{'，⚪ STALE 建議先 refresh dump' if report['dumpStale'] else ''}）\n")
    for r in report["results"]:
        icon = ICONS.get(r["status"], "?")
        line = f"  {icon} {r['taskId']:42s} {r['status']}"
        if r.get("firedAt"):
            line += f"  fire={r['firedAt'][:16]}"
        if r.get("evidence"):
            line += f"  → {r['evidence'][:60]}"
        print(line)
    print(f"\nSummary: silent-death={report['silentDeaths']} "
          f"unregistered={report['unregistered']} "
          f"(grace={report['graceHours']}h / window={report['traceWindowHours']}h)")
    if report["unregistered"]:
        print("  🟠 unregistered = 這條 routine 不在 TAG_PATTERNS，本工具看不見它的 commit 痕跡，"
              "不代表它沒跑。補進表裡再判。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
