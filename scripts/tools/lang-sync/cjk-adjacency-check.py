#!/usr/bin/env python3
"""cjk-adjacency-check.py — 抓「漢字直接黏在拉丁字母上」的漏譯。

## 為什麼既有的 cjk-leak-check 抓不到

`cjk-leak-check.py` 對非漢字圈語言要求「連續 N 個以上漢字」才算洩漏，門檻是
為了不誤殺合法保留：譯文裡的 `Tên tiếng Việt (中文原名)` 是規範要求的寫法，
圖片授權的 `Photo: 化城再来人` 是不可改寫的攝影者本名。

但漏譯最常見的形狀恰好在門檻底下——**兩三個字的專有名詞被留在原地**：
`Giải Kim曲`（金曲獎翻一半）、`cây茄苳`、`đường敕使`、`bài演讲`（還是簡體）。
2026-08-09 委派批次實測：13 篇譯文裡 10 篇中招、合計 86 處，而這 13 篇全部
通過了 cjk-leak-check。

## 判準為什麼是「黏著」而不是「字數」

合法保留的漢字，前後一定有東西隔開：括號 `(中文名)`、引號、冒號後的空格。
漏譯的漢字則是直接長在拉丁文句子中間——`được拆除`、`Kim曲lần`——字母與漢字
之間沒有任何分隔。用相鄰關係當判準，比用長度當判準精準得多：實測抽樣 14 處
零誤報，而長度門檻在同一批漏掉全部 86 處。

這支刻意獨立於 `cjk-leak-check.py`：那支正在被線上產線呼叫，批次跑到一半改
它的判準會讓同一批的前後段用不同標準驗收（今天已經在別的閘門上踩過這個坑）。
等這批收完再考慮合併。

用法：
    python3 cjk-adjacency-check.py <檔案...>
    python3 cjk-adjacency-check.py --glob 'knowledge/vi/**/*.md'

Exit: 0 = 乾淨；1 = 有命中。
"""
from __future__ import annotations

import argparse
import glob as globmod
import re
import sys
from pathlib import Path

LATIN = r"A-Za-zÀ-ỹ"
CJK = r"一-鿿"
ADJACENT = re.compile(f"[{LATIN}][{CJK}]|[{CJK}][{LATIN}]")
CONTEXT = re.compile(f".{{0,24}}(?:[{LATIN}][{CJK}]|[{CJK}][{LATIN}]).{{0,24}}")


# 網址與行內程式碼裡的漢字是合法的：中文標題的維基網址、含中文 slug 的新聞
# 連結（`tw.news.yahoo.com/ai爬蟲再盜-…`）都是真實可用的路徑，改掉它就是把
# 連結改壞。這兩種先挖掉再掃——首版沒挖，第一次拿去驗收就把一條 Yahoo 新聞
# 網址報成漏譯。
MASK = re.compile(r"https?://\S+|`[^`]*`")

# 腳註定義行的連結標題是**逐字引用的來源名稱**，中文來源本來就常混拉丁字母
# （`(Yahoo奇摩新聞)`、`7-Eleven 台灣官網`），那是來源的真名不是漏譯。
#
# 不豁免的後果實測過，而且比漏譯嚴重：2026-08-09 一隻 agent 為了讓這道檢查
# 變綠，把 6 條中文來源標題翻成英文與越南文。讀者拿被改寫的標題去查證會找不到
# 原文——引用失去可追溯性，正是這整套閘門要保護的東西。閘門製造出「改內容換
# 綠燈」的誘因時，它造成的損害會大於它防的問題。
FN_LINK_LABEL = re.compile(r"^\[\^[^\]]+\]:\s*\[[^\]]*\]", re.M)

# 來源標題不一定住在 `[^N]:` 行——有些文章的參考資料是編號清單或項目清單
# （`- [這些動畫通通都是台灣做的！ - PTS公共電視](url)`），標題一樣是逐字引用的
# 中文原名。這是同一家族的第三次現形（前兩次：腳註定義行、括號內原名對照），
# 所以判準一般化到「任何連結標籤」，但只在標籤以漢字為主時豁免：正文裡的越南文
# 連結標籤混進一兩個漢字仍是漏譯，那種標籤是拉丁字為主，抓得到。
LINK_LABEL = re.compile(r"\[([^\]\[]{1,120})\]\(")

# 括號內的中文原名對照是規範要求的寫法（`Tên tiếng Việt (中文原名)`），而中文
# 原名本身可能含拉丁字——`(台灣海關報關制度與EZWAY)` 的「與EZWAY」就會觸發相鄰
# 判定。這是誤判，而誤判在這支上的代價已經驗證過：它會逼 agent 把原名改掉來
# 換綠燈，而原名正是讀者用來對照的錨。
# 判準用「括號內容以漢字為主」，不是「括號內容有漢字」——後者會把
# `(công益財團法人…)` 這種真的把首字翻掉的殘缺原名一起豁免，那是要抓的。
PAREN = re.compile(r"[（(]([^）)]{2,80})[）)]")


def _is_zh_gloss(inner: str) -> bool:
    """括號內容是不是「完好的中文原名對照」。

    只看漢字佔多數不夠——`(công益財團法人交流協會台北事務所)` 漢字壓倒性多數，
    但首字的「公」被翻成 `công` 了，那是損壞的原名，正是要抓的東西。

    真正的分界在拉丁字串的形態：中文原名裡合法出現的拉丁字是品牌與縮寫，
    寫法是全大寫或含數字（`EZWAY`、`7-ELEVEN`、`AI`）；而漏譯留下的是小寫的
    越南文單字直接黏在漢字上（`công益`、`人掏`）。所以要求括號內每一段拉丁
    字串都不是純小寫，才算完好的原名。
    """
    cjk = len(re.findall(f"[{CJK}]", inner))
    if cjk < 2:
        return False
    runs = re.findall(f"[{LATIN}]+", inner)
    return all(not r.islower() for r in runs)


def scan(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    # frontmatter 不掃：translatedFrom 指向中文原稿路徑是規範要求的，
    # imageCredit 的攝影者本名也不該被改寫。
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    # 用等長空白替換，讓前後文擷取的位置不跑掉。
    body = MASK.sub(lambda m: " " * len(m.group(0)), body)
    body = FN_LINK_LABEL.sub(lambda m: " " * len(m.group(0)), body)
    body = PAREN.sub(
        lambda m: " " * len(m.group(0)) if _is_zh_gloss(m.group(1)) else m.group(0),
        body,
    )
    body = LINK_LABEL.sub(
        lambda m: " " * len(m.group(0)) if _is_zh_gloss(m.group(1)) else m.group(0),
        body,
    )
    return [m.group(0).replace("\n", " ") for m in CONTEXT.finditer(body)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--glob")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    paths = [Path(p) for p in args.files]
    if args.glob:
        paths += [Path(p) for p in globmod.glob(args.glob, recursive=True)]

    total, flagged = 0, 0
    for p in paths:
        hits = scan(p)
        if not hits:
            continue
        flagged += 1
        total += len(hits)
        if not args.quiet:
            print(f"❌ {p} — {len(hits)} 處漢字黏著拉丁字母（多半是專有名詞漏譯）")
            for h in hits[:6]:
                print(f"     …{h}…")
            if len(hits) > 6:
                print(f"     …另外 {len(hits) - 6} 處")
    print(f"{flagged}/{len(paths)} 檔命中，合計 {total} 處")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
