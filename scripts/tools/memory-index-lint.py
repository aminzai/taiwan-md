#!/usr/bin/env python3
"""
memory-index-lint.py — MEMORY.md §心跳日誌 index row 150 字 hard gate 檢查

MEMORY-PIPELINE §Index row 寫法 規定「摘要欄 + 教訓欄合計 ≤ 150 字」，但 husky
pre-commit 只驗 frontmatter、不驗 index row 長度。2026-06-19 distill 收官時手寫的
index row 估三次長度都超標（138→189→286 字），是臨時加的 len() check 抓到、不是
husky——這把尺缺自動化。本工具補上（REFLEXES #69：self-report 的長度估算也需要外部尺）。

只 hard-fail「最新一列」（剛寫的才 enforce）；歷史層超標只 warn 不回頭改
（per MANIFESTO §時間是結構修補協議）。

用途：memory 收官 commit 前跑 `memory-index-lint.py`；`--diary` 驗 DIARY.md 最新列
（標題欄 ≤60 + 核心思考欄 ≤150，per DIARY-PIPELINE §Index row。2026-07-05 dna-audit
S5 殼核不對稱修補：memory 有尺 diary 沒有，是 DIARY.md 274KB 的根因）。
已 wire 進 husky pre-commit（staged 含 MEMORY.md / DIARY.md 時觸發）。
exit 1 = 最新列超標。對應 MEMORY-PIPELINE §Index row 寫法。
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT = REPO / "docs/semiont/MEMORY.md"
DIARY = REPO / "docs/semiont/DIARY.md"
GATE = 150
TITLE_GATE = 60
DATE_RE = re.compile(r"^\s*20\d\d-\d\d-\d\d\s*$")


def index_rows(lines, diary=False):
    """回傳 index rows。row 格式：| date | session/handle | 摘要/標題 | 教訓/核心思考 | [→](link) |
    memory 模式：(line_no, session, 摘要+教訓字數)。diary 模式：(line_no, handle, 標題字數, 核心思考字數)。"""
    rows = []
    for i, l in enumerate(lines):
        parts = l.split("|")
        # 前後空 cell → ['', date, session, summary, lesson, link, ''] = 7 parts
        if len(parts) < 7 or not DATE_RE.match(parts[1]):
            continue
        session = parts[2].strip()
        if diary:
            rows.append((i + 1, session, len(parts[3].strip()), len(parts[4].strip())))
        else:
            n = len(parts[3].strip()) + len(parts[4].strip())
            rows.append((i + 1, session, n))
    return rows


def lint_diary():
    lines = DIARY.read_text(encoding="utf-8").split("\n")
    rows = index_rows(lines, diary=True)
    if not rows:
        print("（DIARY.md 找不到 index row — 檔案結構異常？）", file=sys.stderr)
        return 0
    ln, handle, tlen, clen = rows[-1]
    hist_over = sum(1 for _, _, t, c in rows[:-1] if t > TITLE_GATE or c > GATE)
    if tlen <= TITLE_GATE and clen <= GATE:
        note = f"（歷史層 {hist_over} 列超標 = gate 儀器化前舊風格，不回頭改）" if hist_over else ""
        print(f"✅ DIARY 最新 index row L{ln} 標題 {tlen}≤{TITLE_GATE} / 核心思考 {clen}≤{GATE}{note}")
        return 0
    print(f"❌ DIARY 最新 index row L{ln}「{handle[:20]}」超標：標題 {tlen}（gate {TITLE_GATE}）/ 核心思考 {clen}（gate {GATE}）")
    print("   索引是 navigation aid，細節留 diary file。重寫後再 commit。")
    if hist_over:
        print(f"   （另有 {hist_over} 歷史層超標列，非最新，不回頭改）")
    return 1


def main():
    argv = sys.argv[1:]
    if "--diary" in argv:
        return lint_diary()
    path = argv[0] if argv else str(DEFAULT)
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    rows = index_rows(lines)
    if not rows:
        print("（找不到 index row — 檔案結構異常？）", file=sys.stderr)
        return 0

    over = [(ln, s, n) for ln, s, n in rows if n > GATE]
    newest_ln = rows[-1][0]
    newest_over = next((r for r in over if r[0] == newest_ln), None)

    hist_over = len(over) - (1 if newest_over else 0)
    if not newest_over:
        # pass path：只 enforce 最新列，歷史超標一行帶過（不回頭改）
        note = f"（歷史層 {hist_over} 列超標 = 2026-05-12 gate 前舊風格，不回頭改）" if hist_over else ""
        print(f"✅ 最新 index row L{newest_ln} ≤ {GATE} 字{note}")
        return 0

    print(f"❌ 最新 index row L{newest_ln}「{rows[-1][1][:28]}」超標 {newest_over[2]} 字（gate {GATE}）")
    print(f"   摘要 ≤100 / 教訓 ≤50，細節留 memory file。重寫後再 commit。")
    if hist_over:
        print(f"   （另有 {hist_over} 歷史層超標列，非最新，不回頭改）")
    return 1


if __name__ == "__main__":
    sys.exit(main())
