#!/usr/bin/env python3
"""
cjk-leak-check.py — detect partial zh leakage into ja/ko translations.

verify-translation.py's CJK checks only catch a whole field being byte-
identical to the zh source (the "whole tags array left in Chinese" class of
bug). They can't see a PARTIAL leak — a few zh words or even a whole sentence
left untranslated in the middle of an otherwise-genuine ja/ko paragraph —
because ja/ko legitimately contain Han characters (kanji/hanja) throughout, so
raw CJK-presence isn't a signal for these targets.

Found 2026-07-24 in the ko P1 batch: knowledge/ko/Art/taiwanese-cinema.md had
掐死/淘汰/烂死/这一次/悄悄 scattered through the body (Chinese-only figurative
verbs the model apparently gave up translating) plus one entire closing
paragraph left 100% in zh. None of that shows up as "field identical to
source" — it's word-level and sentence-level leakage inside otherwise-real
prose.

Approach: zh-only grammatical particles / function words that have NO
legitimate standalone usage in ja or ko body text (unlike content nouns,
which do legitimately share Han characters across zh/ja/ko). A hit is a
strong, low-noise signal — these words don't occur in genuine ja/ko prose.

Usage:
  python3 cjk-leak-check.py knowledge/ko/Art/taiwanese-cinema.md [more files...]
  python3 cjk-leak-check.py --glob 'knowledge/ko/**/*.md'
  python3 cjk-leak-check.py --since-git <ref>  # files changed since a git ref
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]

# Only markers that are unambiguous: zh function words / zh-only figurative
# verbs, never legitimate ja/ko vocabulary on their own. Content nouns
# (e.g. 電影, 政治, 歷史) are deliberately excluded — those DO legitimately
# appear in ja/ko (shared kanji/hanja), so they're not leak signals.
ZH_ONLY_MARKERS = [
    "的", "了", "這個", "这个", "那個", "那个", "你", "我們", "我们",
    "沒有", "没有", "就是", "都是", "還是", "还是", "因為", "因为",
    "所以", "如果", "這樣", "这样", "這裡", "这里", "這次", "这次",
    "一個", "一个", "而且", "但是", "可是", "掐死", "淘汰", "烂死",
    "爛死", "淹死", "悄悄", "這一次", "这一次", "被宣告",
]

# ja legitimately uses 的 in a few loanword contexts (rare) and legitimately
# uses some of these markers never — keep the list target-agnostic for now,
# false positive rate is low enough to review by hand.


def scan_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"READ_ERROR: {e}"]
    hits = []
    for marker in ZH_ONLY_MARKERS:
        c = text.count(marker)
        if c:
            # show one example context for the first occurrence
            idx = text.find(marker)
            ctx = text[max(0, idx - 20):idx + 20].replace("\n", " ")
            hits.append(f"{marker!r} x{c} (e.g. …{ctx}…)")
    return hits


def files_from_git_range(rng):
    out = subprocess.run(
        ["git", "diff", "--name-only", rng],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout
    return [REPO / p for p in out.splitlines() if p.startswith("knowledge/") and p.endswith(".md")
            and ("/ja/" in p or "/ko/" in p)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--glob")
    ap.add_argument("--since-git")
    args = ap.parse_args()

    if args.since_git:
        paths = files_from_git_range(args.since_git)
    elif args.glob:
        paths = list(REPO.glob(args.glob))
    elif args.files:
        paths = [(REPO / f) if not Path(f).is_absolute() else Path(f) for f in args.files]
    else:
        print("need files, --glob, or --since-git", file=sys.stderr)
        sys.exit(1)

    flagged = 0
    for p in paths:
        if not p.exists():
            continue
        hits = scan_file(p)
        if hits:
            flagged += 1
            print(f"\n❌ {p.relative_to(REPO)}")
            for h in hits:
                print(f"   - {h}")

    print(f"\n{flagged}/{len(paths)} files flagged for zh leakage")
    sys.exit(1 if flagged else 0)


if __name__ == "__main__":
    main()
