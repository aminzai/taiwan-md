#!/usr/bin/env python3
"""merge-divergence.py — 本機 main 與 origin/main 真分岔時，把合併裡機械的那幾步做掉。

誕生：2026-09-09〜09-19 營運機（musebase）跟 origin 分岔十天，合併時 843 個衝突檔，
哲宇 in-session 拍板 OBSERVER-QUEUE #68 選 B 並指示「分岔再發生由 maintainer routine
自行修復」。當天那次合併的每一步都是手寫 python 一次性跑掉的，本檔把可重複的部分
收成工具（REFLEXES #15），讓下一次能在 cron 裡由 maintainer 自己接住，不必等真人。

策略 B（origin 版優先）的分工：

  機械（本工具做）
    resolve     衝突檔按路徑分類：譯文與衍生檔取 origin（--theirs）；reports/babel 三個
                狀態 JSON 取聯集；認知層五檔與 scripts/ 留給人（列出來，不動）。
    dedupe      合併後同一語言、同一 translatedFrom 有兩個檔 → origin 有的那份留，
                本機那份 git rm；兩份都在 origin 的既有雙檔不動（另有 handoff）。
    align       本機帶進來的譯文檔名對不上 en canonical → git mv 到 en 檔名；en 檔本身
                是本機側新翻、其他語言早用另一個檔名上線的 → 反過來改 en 去配多數；
                上線過的檔改名時印出來，提醒補 config/redirects-manual.txt 301。
    verify      留下來的本機譯文跑 target-language-check（不是目標語言的 git rm）。
  判斷（人／session 做）
    docs/semiont 五檔的聯集（OBSERVER-QUEUE 要改編號）、scripts 的兩邊功能合成、
    最後的 commit 訊息與 push。完整 SOP：docs/pipelines/MAINTAINER-PIPELINE.md §Step 1.1b。

用法（在一個 `git merge --no-commit origin/main` 停住的 worktree 裡）：
    python3 scripts/tools/merge-divergence.py resolve [--base <origin-sha-before-merge>]
    python3 scripts/tools/merge-divergence.py dedupe --base <sha> [--apply]
    python3 scripts/tools/merge-divergence.py align  --base <sha> [--apply]
    python3 scripts/tools/merge-divergence.py verify --base <sha> [--apply]
    python3 scripts/tools/merge-divergence.py all    --base <sha> [--apply]
--base 是合併前 origin/main 的 commit（判斷「哪份是 origin 的」的唯一依據）。
不帶 --apply 一律 dry-run 只印計畫。
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "tools" / "lang-sync"))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

LANGS = set(ALL_TRANSLATION_LANGS)

# 衝突分類：路徑前綴 → 處置
THEIRS_PREFIXES = (
    "public/", "src/data/", "config/article-aliases.json", "config/redirects-generated.json",
    "knowledge/_slug-map.json", "knowledge/_translation-status.json", "knowledge/_translations.json",
    "reports/404-monitor/", "reports/fork-census/", "reports/newsroom/",
    "scripts/tools/.quality-baseline.json", "README.md", "public/llms.txt",
)
UNION_JSON = ("reports/babel/cascade-exhausted.json", "reports/babel/fail-memo.json",
              "reports/babel/fail-reasons.json")
HAND = ("docs/", "scripts/", ".gitignore", "reports/INDEX.md")


def sh(*args, check=True, cwd=ROOT):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=check).stdout


def classify(path: str) -> str:
    """一個衝突檔屬於哪一類：theirs / union-json / hand。"""
    if path in UNION_JSON:
        return "union-json"
    if re.match(r"^knowledge/[a-z-]+/.+\.md$", path) and path.split("/")[1] in LANGS:
        return "theirs"
    if path.startswith(THEIRS_PREFIXES):
        return "theirs"
    if path.startswith(HAND):
        return "hand"
    return "hand"


def _union_json(path: str):
    a = json.loads(sh("git", "show", f":2:{path}"))
    b = json.loads(sh("git", "show", f":3:{path}"))
    if all(isinstance(v, dict) for v in list(a.values())[:5] + list(b.values())[:5]):
        m = {k: dict(v) for k, v in b.items()}
        for k, v in a.items():
            d = m.setdefault(k, {})
            for r, c in v.items():
                d[r] = max(c, d.get(r, 0))
    else:
        m = dict(b)
        for k, v in a.items():
            m[k] = max(v, m.get(k, v)) if isinstance(v, (int, float, str)) else v
    (ROOT / path).write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n")


def cmd_resolve(apply: bool):
    conflicted = [p for p in sh("git", "diff", "--name-only", "--diff-filter=U").splitlines() if p]
    groups = defaultdict(list)
    for p in conflicted:
        groups[classify(p)].append(p)
    for k in ("theirs", "union-json", "hand"):
        print(f"{k:11s} {len(groups[k]):5d}")
    if not apply:
        for p in groups["hand"]:
            print("   hand:", p)
        return
    if groups["theirs"]:
        sh("git", "checkout", "--theirs", "--", *groups["theirs"])
        sh("git", "add", "--", *groups["theirs"])
    for p in groups["union-json"]:
        _union_json(p)
        sh("git", "add", "--", p)
    print(f"✅ theirs {len(groups['theirs'])} / union-json {len(groups['union-json'])} 已 stage；"
          f"留給人的 {len(groups['hand'])} 檔：")
    for p in groups["hand"]:
        print("   ", p)


def translated_from(p: Path):
    try:
        head = p.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return None
    m = re.search(r"^translatedFrom:\s*['\"]?([^'\"\n]+)", head, re.M)
    return m.group(1).strip() if m else None


def in_base(base: str, rel: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{base}:{rel}"], cwd=ROOT,
                          capture_output=True).returncode == 0


def families():
    """lang -> zh -> [rel paths]"""
    out = defaultdict(lambda: defaultdict(list))
    for lang in LANGS:
        for f in (ROOT / "knowledge" / lang).rglob("*.md"):
            if f.name.startswith("_"):
                continue
            src = translated_from(f)
            if src:
                out[lang][src].append(str(f.relative_to(ROOT)))
    return out


def dedupe_plan(fam, base: str):
    """同語言同源雙檔：origin 有的留、本機的丟；兩份都在 origin 的不動。"""
    drop, preexisting = [], []
    for lang, d in fam.items():
        for zh, files in d.items():
            if len(files) < 2:
                continue
            ino = [f for f in files if in_base(base, f)]
            loc = [f for f in files if f not in ino]
            if ino and loc:
                drop += loc
            elif len(ino) >= 2:
                preexisting.append((lang, zh, files))
            else:  # 全部本機：留跟 en 同名的，否則留排序第一個
                keep = sorted(files)[0]
                drop += [f for f in files if f != keep]
    return drop, preexisting


def cmd_dedupe(base: str, apply: bool):
    drop, pre = dedupe_plan(families(), base)
    print(f"同語言雙檔：本機該丟 {len(drop)} 檔；origin 既有雙檔 {len(pre)} 組（不動，另走 handoff）")
    for lang, zh, files in pre:
        print("   既有:", lang, zh, files)
    if apply and drop:
        for i in range(0, len(drop), 200):
            sh("git", "rm", "-q", "--", *drop[i:i + 200])
        print(f"✅ git rm {len(drop)} 檔")


def align_plan(fam, base: str):
    """檔名對 en canonical。回傳 (renames[(old,new,live)], en_renames[(old,new)], skipped)."""
    en_index = {zh: Path(fs[0]).name for zh, fs in fam.get("en", {}).items() if len(fs) == 1}
    renames, en_renames, skipped = [], [], []
    for lang, d in fam.items():
        if lang == "en":
            continue
        for zh, files in d.items():
            if len(files) != 1 or zh not in en_index:
                continue
            f = files[0]
            en_name = en_index[zh]
            if Path(f).name == en_name:
                continue
            en_path = fam["en"][zh][0]
            en_live = in_base(base, en_path)
            f_live = in_base(base, f)
            if not en_live and f_live:
                # en 是本機側新翻的，其他語言早用這個檔名上線 → 改 en 去配多數
                sib = [Path(x[0]).name for l2, d2 in fam.items() if l2 != "en" for z2, x in d2.items()
                       if z2 == zh and len(x) == 1]
                top = max(set(sib), key=sib.count)
                new_en = str(Path(en_path).with_name(top))
                if (en_path, new_en) not in en_renames:
                    en_renames.append((en_path, new_en))
                continue
            new = str(Path(f).with_name(en_name))
            if (ROOT / new).exists():
                skipped.append((f, new))
                continue
            renames.append((f, new, f_live))
    return renames, en_renames, skipped


def cmd_align(base: str, apply: bool):
    fam = families()
    renames, en_renames, skipped = align_plan(fam, base)
    live = [r for r in renames if r[2]]
    print(f"檔名對齊：sibling 改名 {len(renames)}（其中上線過 {len(live)} 要補 301）；"
          f"en 改配多數 {len(en_renames)}；目標已存在跳過 {len(skipped)}")
    for old, new, _ in live:
        print("   LIVE 301:", old, "->", new)
    for old, new in en_renames:
        print("   en:", old, "->", new)
    for old, new in skipped:
        print("   skip(目標已存在，先跑 dedupe):", old, "->", new)
    if apply:
        for old, new in en_renames:
            sh("git", "mv", old, new)
        for old, new, _ in renames:
            sh("git", "mv", old, new)
        print("✅ git mv 完成；接著跑 sync-translations-json.py 並補 301")


def cmd_verify(base: str, apply: bool):
    retained = [f for lang, d in families().items() for fs in d.values() for f in fs
                if not in_base(base, f)]
    if not retained:
        print("本機帶進來的譯文 0 篇")
        return
    out = json.loads(sh("python3", "scripts/tools/lang-sync/target-language-check.py", "--json", *retained,
                        check=False))
    bad = [r["path"] for r in out.get("results", []) if r.get("verdict") == "fail"]
    print(f"target-language-check：本機帶進 {len(retained)} 篇，不是目標語言 {len(bad)} 篇")
    for p in bad:
        print("   ❌", p)
    if apply and bad:
        sh("git", "rm", "-q", "--", *bad)
        print(f"✅ git rm {len(bad)} 篇")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["resolve", "dedupe", "align", "verify", "all"])
    ap.add_argument("--base", help="合併前 origin/main 的 commit（dedupe/align/verify 必填）")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.cmd != "resolve" and not a.base:
        ap.error("--base 必填")
    if a.cmd in ("resolve", "all"):
        cmd_resolve(a.apply)
    if a.cmd in ("dedupe", "all"):
        cmd_dedupe(a.base, a.apply)
    if a.cmd in ("verify", "all"):
        cmd_verify(a.base, a.apply)
    if a.cmd in ("align", "all"):
        cmd_align(a.base, a.apply)


if __name__ == "__main__":
    main()
