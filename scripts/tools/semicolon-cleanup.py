#!/usr/bin/env python3
"""semicolon-cleanup.py — 把可編輯正文裡當連接號用的全形分號換成句號。

為什麼有這支工具
────────────────
`punct-cleanup.py`（2026-07-19 legacy campaign）是清單產生器＋事實保真驗證器，
它負責「驗這次清理有沒有動到事實」，但**不會動手清**。當初那 144 篇 legacy 是外部
agent 一篇一篇讀著清的。

問題是這個門檻不只擋 legacy。2026-08-27 的維護 cycle 裡，同一天有九個投稿 PR 全部
卡在同一句「全形分號超硬門檻」，分號數 14 到 27 不等。這是投稿端 AI 寫繁中的固定
水印——繁體中文散文本來很少用「；」，它是論文與法律條文的標點。逐 PR 找人手清，
等於每次都用判斷力去做一件機械上可判定的事（MANIFESTO §14 高儀器化）。

修法邊界（比 gate 更保守，寧可少改也不要改到語意）
────────────────────────────────────────────────
1. **禁改區直接沿用 gate 自己的 predicate**（`prose_health._uneditable_punct_predicate`），
   不另寫一份。參考裝置段之後、blockquote、腳註定義行、圖片行、斜體圖說、書名號內，
   一律不動。兩邊共用同一個判準，就不會出現「清完了 gate 還是說超標」。
2. 只在「分號兩側都是中日韓文字」時才換。前後任一側是英數、標點、括號、URL 殘骸的，
   多半是列表分隔或授權行的形狀，不碰。
3. 換成「。」而不是「，」或「、」：分號在中文連接的是兩個能獨立成句的子句，換句號
   語意等價；換逗號會把兩句黏成流水句，換頓號會把子句誤讀成並列名詞。
4. 只清到剛好過門檻（預設 12），從檔案末尾往前清。留在前段的分號通常是作者真的在
   做並列對照的地方，最值得保留。`--all` 可全清。

用法
────
  python3 scripts/tools/semicolon-cleanup.py knowledge/Food/麥當樂.md            # 清到達標
  python3 scripts/tools/semicolon-cleanup.py --dry-run knowledge/...            # 只看會改哪幾處
  python3 scripts/tools/semicolon-cleanup.py --all knowledge/...                # 全清不留餘額
  python3 scripts/tools/semicolon-cleanup.py --limit 3 knowledge/...            # 自訂目標餘額

事實保真由 `punct-cleanup.py --verify` 把關（數字／引語／URL／腳註／frontmatter
multiset 不變）。本工具只換標點、不新增或刪除任何其他字元，所以那七道檢查應全過。

Exit codes: 0 = 已達標（或本來就達標）/ 1 = 清完仍超標（需人工）/ 2 = 參數或路徑錯誤
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.article_health.checks.prose_health import (  # noqa: E402
    _uneditable_punct_predicate as _uneditable,
)

# 跟 article-health.config.toml 的 pre-commit override 對齊（punct-cleanup.py 同源）
SEMICOLON_MAX = 12

_CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿]")
_FM = re.compile(r"^---\n.*?\n---\n", re.S)


def _split_frontmatter(text: str) -> tuple[str, str]:
    m = _FM.match(text)
    return (m.group(0), text[m.end():]) if m else ("", text)


def _candidates(body: str) -> list[int]:
    """回傳 body 裡可安全改寫的分號 offset（已排除 gate 禁改區與非子句連接用法）。"""
    uneditable = _uneditable(body)
    out = []
    for m in re.finditer("；", body):
        i = m.start()
        if uneditable(i):
            continue
        # 前後都必須是中日韓文字，才確定它連接的是兩個中文子句而不是列表項或授權行
        prev_ch = body[i - 1] if i > 0 else ""
        next_ch = body[i + 1] if i + 1 < len(body) else ""
        if not (_CJK.match(prev_ch or " ") and _CJK.match(next_ch or " ")):
            continue
        out.append(i)
    return out


def count_editable(text: str) -> int:
    """gate 口徑的可編輯正文分號數（含本工具不敢動的那些，所以用來對賬達標與否）。"""
    _, body = _split_frontmatter(text)
    uneditable = _uneditable(body)
    return sum(1 for m in re.finditer("；", body) if not uneditable(m.start()))


def clean(text: str, limit: int, clean_all: bool) -> tuple[str, int]:
    fm, body = _split_frontmatter(text)
    cands = _candidates(body)
    total = count_editable(text)
    if not clean_all:
        need = total - limit
        if need <= 0:
            return text, 0
        # 從後往前清：前段的分號比較可能是作者真的在做並列對照
        cands = cands[-need:] if need <= len(cands) else cands
    chars = list(body)
    for i in cands:
        chars[i] = "。"
    return fm + "".join(chars), len(cands)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="knowledge/*.md 路徑")
    ap.add_argument("--dry-run", action="store_true", help="只印會改哪幾處，不寫檔")
    ap.add_argument("--all", action="store_true", dest="clean_all", help="全清，不留門檻餘額")
    ap.add_argument("--limit", type=int, default=SEMICOLON_MAX, help=f"目標餘額（預設 {SEMICOLON_MAX}）")
    args = ap.parse_args()

    if not args.files:
        ap.print_help()
        return 2

    worst = 0
    for f in args.files:
        p = Path(f)
        if not p.exists():
            print(f"❌ 找不到 {f}", file=sys.stderr)
            worst = max(worst, 2)
            continue
        text = p.read_text(encoding="utf-8")
        before = count_editable(text)
        new, changed = clean(text, args.limit, args.clean_all)
        after = count_editable(new)

        if args.dry_run:
            fm, body = _split_frontmatter(text)
            for i in _candidates(body)[-max(0, before - args.limit):] if not args.clean_all else _candidates(body):
                a, b = body[max(0, i - 28):i], body[i + 1:i + 29]
                print(f"   …{a}《；→。》{b}…".replace("\n", "⏎"))
        elif changed:
            p.write_text(new, encoding="utf-8")

        mark = "✅" if after <= args.limit else "❌"
        verb = "會改" if args.dry_run else "改了"
        print(f"{mark} {f}: 可編輯正文分號 {before} → {after}（{verb} {changed} 處，門檻 {args.limit}）")
        if after > args.limit:
            print("   ↳ 剩下的分號前後不是純中文（多半在列表或授權行形狀裡），本工具不敢動，需人工看一眼")
            worst = max(worst, 1)
    return worst


if __name__ == "__main__":
    sys.exit(main())
