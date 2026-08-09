#!/usr/bin/env python3
"""restore-footnote-urls.py — 把譯文腳註裡被模型改動的來源網址還原成中文原稿的版本。

## 為什麼有這支

腳註的來源網址是「不可翻譯內容」，但模型常常動它。實際看到的形狀有三種：
截成根網址（`https://sec.nycu.edu.tw/sec/ch/app/...?id=38552&serno=...`
變成 `https://sec.nycu.edu.tw/`）、把查詢字串丟掉、把 percent-encoding 改一碼。
這類改動不會讓譯文讀起來有問題——它讓來源失去可追溯性，而
`verify-translation.py` 的 URL multiset 閘門會擋下整篇，於是一篇字字正確的
譯文因為兩個網址被退回重翻，等於為 0.1% 的瑕疵燒掉 100% 的算力。

既有工具都不做這件事：`footnote-format-fix.py` 修的是格式（缺描述、多餘括號），
不碰網址內容；`heal-passthrough-fields.py` 管的是 frontmatter。

## 為什麼只動腳註定義行，而且只在編號對得起來時動

腳註定義是譯文裡唯一能跟中文原稿「一對一」對齊的結構：`[^5]` 就是 `[^5]`，
不需要理解語意就能配對。正文裡的網址沒有這種錨，硬對會配錯。所以這支刻意
只處理 `[^N]:` 開頭的行，其餘一律回報不動——保守到寧可少修，因為修錯一個
來源網址比留著一個壞網址更糟：前者讀者點進去看到的是別人的內容，後者至少
會被閘門擋下來。

同理，同一個腳註裡中文有 k 個網址、譯文不是 k 個時也不動：數量不同代表模型
增刪了連結，位置對應已經不可靠，那需要判斷力不是機械替換。

用法：
    python3 restore-footnote-urls.py <zh_path> <translation_path>            # 預覽
    python3 restore-footnote-urls.py <zh_path> <translation_path> --apply    # 寫回

Exit code: 0 = 沒有需要還原的 / 已還原；1 = 有無法安全處理的差異（需人看）。
"""
import argparse
import re
import sys
from pathlib import Path

FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$")
# markdown target `](URL)` 與 angle-wrapped `](<URL>)` 兩種都收。
# angle 形式優先整段吃下，否則含括號的維基網址會在第一個 `)` 被截斷
# （BABEL-VORTEX-LOOP v1.19-v1.20 修過同一個 regex 病，這裡沿用它的結論）。
URL_IN_LINK = re.compile(r"\]\(\s*(?:<([^>]+)>|([^)\s]+))")


def footnote_urls(line: str) -> list[str]:
    return [m.group(1) or m.group(2) for m in URL_IN_LINK.finditer(line)]


def collect(text: str) -> dict[str, tuple[int, str]]:
    """footnote id → (行號, 整行)"""
    out = {}
    for i, line in enumerate(text.splitlines()):
        m = FOOTNOTE_DEF.match(line)
        if m:
            out[m.group(1)] = (i, line)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zh_path")
    ap.add_argument("translation_path")
    ap.add_argument("--apply", action="store_true", help="寫回檔案（預設只預覽）")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    zh_text = Path(args.zh_path).read_text(encoding="utf-8")
    tr_path = Path(args.translation_path)
    tr_lines = tr_path.read_text(encoding="utf-8").splitlines(keepends=True)

    zh_fn = collect(zh_text)
    tr_fn = collect("".join(tr_lines))

    restored, skipped = [], []
    for fid, (idx, tr_line) in tr_fn.items():
        if fid not in zh_fn:
            skipped.append((fid, "中文原稿沒有這個編號"))
            continue
        zh_urls = footnote_urls(zh_fn[fid][1])
        tr_urls = footnote_urls(tr_line)
        if not zh_urls or zh_urls == tr_urls:
            continue
        if len(zh_urls) != len(tr_urls):
            skipped.append((fid, f"連結數不同 zh={len(zh_urls)} 譯文={len(tr_urls)}，位置對應不可靠"))
            continue
        # 位置替換：第 n 個連結換成中文原稿的第 n 個。
        it = iter(zh_urls)
        new_line = URL_IN_LINK.sub(lambda m: f"]({next(it)}", tr_line)
        for a, b in zip(tr_urls, zh_urls):
            if a != b:
                restored.append((fid, a, b))
        tr_lines[idx] = new_line + ("\n" if not new_line.endswith("\n") else "")

    if not args.quiet:
        for fid, old, new in restored:
            print(f"  [^{fid}] {old}\n      → {new}")
        for fid, why in skipped:
            print(f"  ⚠️ [^{fid}] 不動：{why}")
        verb = "已還原" if args.apply else "可還原（預覽，加 --apply 寫回）"
        print(f"{verb} {len(restored)} 個網址；需人看 {len(skipped)} 個")

    if args.apply and restored:
        tr_path.write_text("".join(tr_lines), encoding="utf-8")

    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main())
