#!/usr/bin/env python3
"""untranslated-line-check.py — 譯文裡整行沒翻的正文行。

2026-09-10 出生：fr 的唐鳳篇有九句 `✦` 逐字引用整段照抄中文，ja 同篇十三處，
而 en/es 那九句早就翻好了。cjk-leak-check 只抓到十行裡的一行，cjk-adjacency-check
（OBSERVER-QUEUE #52 那把尺）判準是「漢字直接黏在拉丁字母上」——整行純中文
沒有拉丁字母可黏，那把尺結構上看不到這一族。全庫量到 178 行 / 86 檔。

判準：非 ja/ko 語系的正文行，去空白後長度 ≥25 且漢字佔比 ≥60%。

已知不適用：
  - ja/ko 本來就用漢字，漢字佔比對它們無意義 → exit 0 並說明（同 numeral-magnitude-check
    對 ja/ko 的處理）。這兩個語系的同族缺陷要換一把尺，屬 OBSERVER-QUEUE #57 的另案。
  - frontmatter（rationale 欄的 why_this_hook 全庫 716 檔都是中文，是 provenance 不是譯文）
  - 參考條目 `[^n]:`（中文來源的標題本來就該保留原文）
  - 表格列與延伸閱讀清單（`|` 開頭 / `- [` 開頭，多半是專有名詞原名對照）

用法：
    python3 untranslated-line-check.py <譯文...>          # exit 1 = 有命中
    python3 untranslated-line-check.py --all              # 掃全庫
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CJK = re.compile(r"[一-鿿]")
LANG_DIR = re.compile(r"^[a-z]{2}$")
# 漢字語系：這把尺對它們無效
KANJI_LANGS = {"ja", "ko"}

MIN_LEN = 25
MIN_RATIO = 0.60

# 參考／來源章節：底下的中文書目條目是真實來源的原名，保留是對的（同 [^n] 腳註）。
# 第一版沒排除，de/en 的編號書目全被誤報。
REF_HEADING = re.compile(
    r"^#{1,3}\s*("
    r"參考\w*|参考\w*|Referen\w*|Bibliograf\w*|Bibliograph\w*|"
    r"Quellen|Bildquellen|Источник\w*|참고|Fuentes|Sources?|"
    r"مراجع|مصادر|संदर्भ|Nguồn|Sumber"
    r")", re.I)
# 只由 wikilink 與分隔符組成的導覽列（Hub 檔的目錄），屬 hub 在地化另一族
NAV_ONLY = re.compile(r"^(\s*\[\[[^\]]+\]\]\s*[|、,·/]?\s*)+$")


def skip(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if s.startswith("<!--"):          # 內部編輯註記，不會 render
        return True
    if s.startswith(('title="', "title='")):
        # 內嵌影片的 title 屬性＝那支影片的真實標題，翻掉反而找不到
        return True
    if NAV_ONLY.match(s):             # Hub 檔的 wikilink 導覽列
        return True
    # frontmatter 欄位、參考條目、表格、延伸閱讀清單、YAML 陣列元素
    return s.startswith(
        ("---", "|", "[^", "- [", "'", '"', "rationale:", "translatedFrom:",
         "subcategory:", "tags:", "image", "title:", "description:", "date:",
         "readingTime:", "author", "category:")
    )


def scan(path: Path) -> list[tuple[int, str]]:
    hits = []
    lines = path.read_text(encoding="utf-8").splitlines()
    # frontmatter 只可能是「檔首第一行 --- 到下一個 ---」。不能用 toggle：正文裡的
    # 水平分隔線也是 ---，toggle 會從第一條分隔線之後把整篇當成 frontmatter 跳過。
    # 第一版就是這樣寫的，全庫數字從 169 縮到 63，而 en/About/founder.md 兩句
    # 整段中文的引用剛好落在分隔線後面，被靜靜吞掉。
    body_start = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                body_start = j + 1
                break
    for i, line in enumerate(lines[body_start:], body_start + 1):
        if REF_HEADING.match(line.strip()):
            break                     # 參考章節以下不看
        if skip(line):
            continue
        body = re.sub(r"\s", "", line)
        if len(body) < MIN_LEN:
            continue
        if len(CJK.findall(line)) / len(body) >= MIN_RATIO:
            hits.append((i, line.strip()))
    return hits


def lang_of(path: Path) -> str | None:
    try:
        parts = path.resolve().relative_to(REPO / "knowledge").parts
    except ValueError:
        return None
    return parts[0] if len(parts) >= 2 and LANG_DIR.fullmatch(parts[0]) else None


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--all":
        files = sorted(
            p for p in (REPO / "knowledge").rglob("*.md") if lang_of(p) not in (None, *KANJI_LANGS)
        )
    else:
        files = [Path(a) for a in args]

    total = flagged = 0
    skipped_kanji = []
    for f in files:
        lang = lang_of(f)
        if lang in KANJI_LANGS:
            skipped_kanji.append(f)
            continue
        if lang is None:
            continue
        if f.name.startswith("_"):
            continue                   # Hub／索引檔的導覽列屬 hub 在地化另一族
        hits = scan(f)
        if not hits:
            continue
        flagged += 1
        total += len(hits)
        rel = f.resolve().relative_to(REPO)
        print(f"❌ {rel} — {len(hits)} 行整行未翻")
        for n, text in hits[:6]:
            print(f"     {n}: {text[:110]}")
        if len(hits) > 6:
            print(f"     …另外 {len(hits) - 6} 行")

    if skipped_kanji:
        print(f"（{len(skipped_kanji)} 個 ja/ko 檔跳過：原生使用漢字，漢字佔比對它們無意義，"
              f"同族缺陷屬 OBSERVER-QUEUE #57 另案）")
    if flagged:
        print(f"\n════ {flagged} 檔，合計 {total} 行整行未翻 ════")
        print("整行純中文＝那段根本沒送進翻譯，不是保留原名。逐行翻掉，別扁平化。")
        return 1
    print(f"✅ {len(files) - len(skipped_kanji)} 檔，沒有整行未翻的正文")
    return 0


if __name__ == "__main__":
    sys.exit(main())
