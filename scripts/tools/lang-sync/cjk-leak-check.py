#!/usr/bin/env python3
"""
cjk-leak-check.py — detect partial zh leakage into any target-language body.

verify-translation.py's CJK checks only catch a whole field being byte-
identical to the zh source (the "whole tags array left in Chinese" class of
bug). They can't see a PARTIAL leak — a few zh words or even a whole sentence
left untranslated in the middle of an otherwise-genuine translation.

Two strategies depending on target script:
- ja/ko (CJK-script targets): raw CJK-presence isn't a signal — these
  languages legitimately contain Han characters (kanji/hanja) throughout.
  Instead: zh-only grammatical particles / function words with no legitimate
  standalone ja/ko usage (你/我們/因為/所以/一個/掐死/etc — deliberately
  excludes 的/了, false positives from legitimate ja suffix (先天的) and
  compound-word usage (終了)).
- en/es/fr/vi/id/pt/hi (non-CJK-script targets): the bar is much lower — ANY
  run of 4+ consecutive CJK Han characters in body prose (outside a
  parenthetical proper-noun gloss like "(李安)") is almost certainly a leak,
  since these languages have zero legitimate standalone Han vocabulary.

Found 2026-07-24 in the ko P1 batch: knowledge/ko/Art/taiwanese-cinema.md had
掐死/淘汰/烂死/这一次/悄悄 scattered through the body (Chinese-only figurative
verbs the model apparently gave up translating) plus one entire closing
paragraph left 100% in zh. None of that shows up as "field identical to
source" — it's word-level and sentence-level leakage inside otherwise-real
prose.

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
#
# 2026-07-24 修正：表曾含 的/了/一個/淘汰，跟本 docstring 直接矛盾——
# 日文 〜的 是最常見形容詞後綴（言語的/構造的）、了 在 完了/終了、
# 一個（いっこ）是量詞、淘汰（自然淘汰）是常用語。抽測 3/3 健康 ja 檔
# 被誤判（的 ×63/×42/×9），ja lane 在 gate 面前 100% 死路，是 2026-07-24
# ja/ko 大量好譯文被 quarantine 降級的主因之一（另一半是全形括號豁免）。
ZH_ONLY_MARKERS = [
    "這個", "这个", "那個", "那个", "你", "我們", "我们",
    "沒有", "没有", "就是", "都是", "還是", "还是", "因為", "因为",
    "所以", "如果", "這樣", "这样", "這裡", "这里", "這次", "这次",
    "而且", "但是", "可是", "掐死", "烂死",
    "爛死", "淹死", "悄悄", "這一次", "这一次", "被宣告",
]


# Non-CJK-script targets (en/es/fr/vi/id/pt/hi): unlike ja/ko, these languages
# have ZERO legitimate standalone Han-character vocabulary, so the bar is much
# lower — any run of 4+ consecutive CJK Han characters in the body (outside a
# parenthetical, where a short proper-noun citation like "(李安)" is normal)
# is almost certainly a leak, not a false positive.
CJK_RUN_RE = re.compile(r"[一-鿿]{4,}")
NON_CJK_SCRIPT_LANGS = {"en", "es", "fr", "vi", "id", "pt", "hi"}

# 括號 gloss 豁免 span：全形（）與半形 () 都認（2026-07-24 前只認半形——
# zh-TW 源文與模型鏡射的標準標點是全形，整批好譯文被誤判 leak 反覆重翻，
# nemotron 實測 ~85% "leak" gate-fail 多為此假陽性）。內容上限 30 字：
# 命名 gloss（人名／機構／書名＋對照拼音）在界內，整句洩漏不會躲在括號裡。
PAREN_GLOSS_RE = re.compile(r"[(（][^()（）]{0,30}[)）]")


def detect_lang(path: Path) -> str:
    parts = path.parts
    if "knowledge" in parts:
        idx = parts.index("knowledge")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return "unknown"


def scan_file(path: Path, lang: str = None):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"READ_ERROR: {e}"]
    lang = lang or detect_lang(path)
    hits = []

    if lang in NON_CJK_SCRIPT_LANGS:
        # Strip legitimate zh-bearing zones before scanning:
        #   frontmatter block (translatedFrom etc always references the zh filename)
        #   markdown links [text](url) — internal wikilinks use zh slugs, external
        #     citations legitimately keep the source's actual (Chinese) title
        #   footnote definitions `[^n]: ...` — same citation-title reasoning
        body = text
        if body.startswith("---"):
            end_fm = body.find("---", 3)
            if end_fm != -1:
                body = body[end_fm + 3:]
        body = re.sub(r"\[[^\]]*\]\([^)]*\)", "", body)          # [text](url)
        body = re.sub(r"^\[\^[^\]]+\]:.*$", "", body, flags=re.MULTILINE)  # [^n]: ...

        gloss_spans = [g.span() for g in PAREN_GLOSS_RE.finditer(body)]
        for m in CJK_RUN_RE.finditer(body):
            start, end = m.span()
            if any(s < start and end < e for s, e in gloss_spans):
                continue
            ctx = body[max(0, start - 20):end + 20].replace("\n", " ")
            hits.append(f"CJK run {m.group(0)!r} (e.g. …{ctx}…)")
        return hits

    # ja/ko marker 掃描前的合法區剝除（2026-07-24）：
    #   「…」『…』引述 span — 引用原文 zh 是編輯選擇（陳建仁原話等），非洩漏
    #   markdown 連結（容忍一層巢狀中括號）— 引用的 zh 標題合法
    scan = re.sub(r"「[^「」]*」|『[^『』]*』", "", text)
    scan = re.sub(r"\[[^\[\]]*(?:\[[^\]]*\][^\[\]]*)*\]\([^)]*\)", "", scan)
    for marker in ZH_ONLY_MARKERS:
        c = scan.count(marker)
        if c:
            # show one example context for the first occurrence
            idx = scan.find(marker)
            ctx = scan[max(0, idx - 20):idx + 20].replace("\n", " ")
            hits.append(f"{marker!r} x{c} (e.g. …{ctx}…)")
    return hits


def files_from_git_range(rng):
    out = subprocess.run(
        ["git", "diff", "--name-only", rng],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout
    return [REPO / p for p in out.splitlines() if p.startswith("knowledge/") and p.endswith(".md")
            and detect_lang(Path(p)) in (NON_CJK_SCRIPT_LANGS | {"ja", "ko"})]


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
