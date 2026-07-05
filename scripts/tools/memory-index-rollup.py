#!/usr/bin/env python3
"""
memory-index-rollup.py — MEMORY.md §心跳日誌 index 月度彙整（蒸餾債清償儀器）

背景：MEMORY.md index 曾累積 709 rows（觸發線 80，2026-04-14 蒸餾設計從未實作，
alert 每天黃燈無 routine 認領 — 2026-07-05 dna-audit S4）。本工具做最小可行蒸餾：

- inline 只保留最新 KEEP 列（預設 40，約 3 天 @13 fires/day），tail -25 甦醒讀取不受影響
- 較舊列 **verbatim 原文搬移**到 docs/semiont/memory/index-archive/{YYYY-MM}.md（append-only，
  raw 永不刪除 per REFLEXES #22；歸檔列可 grep、有 git 歷史）
- 每個被搬的月份在表內留一列月度摘要（digest row，date 欄用 YYYY-MM 不含日 →
  不會被 memory-index-lint / 本工具當一般列處理）
- 列守恆斷言（REFLEXES #38 檔案改寫 dry-run 變體）：kept + moved == 原列數，
  歸檔檔新增行數 == moved 對應數，任一不合 = abort 不寫入
- dry-run 是預設；--apply 才落地

擁有權（detection ≠ remediation，REFLEXES #58）：twmd-distill-weekly 每週跑一次
`--apply`，SOP 在 MEMORY-PIPELINE §索引蒸餾。
"""
import argparse
import re
import sys
from collections import OrderedDict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MEMORY = REPO / "docs/semiont/MEMORY.md"
ARCHIVE_DIR = REPO / "docs/semiont/memory/index-archive"
KEEP_DEFAULT = 40
FULL_DATE_RE = re.compile(r"^\s*(20\d\d)-(\d\d)-(\d\d)\s*$")

ARCHIVE_HEADER = """# MEMORY index archive — {month}

> 由 `scripts/tools/memory-index-rollup.py` 從 [MEMORY.md](../../MEMORY.md) §心跳日誌 verbatim 搬入。
> 列內容一字未改（raw 永不刪除，REFLEXES #22）；raw 檔在 `memory/`。append-only。

| 日期 | Session | 摘要 | 關鍵教訓 | 完整 |
| --- | --- | --- | --- | --- |
"""


def is_index_row(line: str):
    parts = line.split("|")
    if len(parts) < 7:
        return None
    m = FULL_DATE_RE.match(parts[1])
    return m.group(1) + "-" + m.group(2) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="真的寫入（預設 dry-run）")
    ap.add_argument("--keep", type=int, default=KEEP_DEFAULT)
    args = ap.parse_args()

    lines = MEMORY.read_text(encoding="utf-8").split("\n")
    rows = [(i, is_index_row(l)) for i, l in enumerate(lines)]
    row_idx = [(i, month) for i, month in rows if month]
    total = len(row_idx)
    if total <= args.keep:
        print(f"✅ inline rows {total} ≤ keep {args.keep}，無需 rollup")
        return 0

    to_move = row_idx[: total - args.keep]
    kept_months = {month for _, month in row_idx[total - args.keep :]}
    by_month = OrderedDict()
    for month in sorted({m for _, m in to_move}):
        # 歸檔內按（日期字串, 原行序）穩定排序 — 原表曾同時存在新在上與新在下兩段
        idxs = [i for i, m in to_move if m == month]
        idxs.sort(key=lambda i: (lines[i].split("|")[1].strip(), i))
        by_month[month] = idxs

    print(f"📦 rollup 計畫：inline {total} → keep {args.keep}，搬 {len(to_move)} 列：")
    for month, idxs in by_month.items():
        tag = "" if month not in kept_months else "（該月仍有 inline 列 → 不產 digest）"
        print(f"   {month}: {len(idxs)} 列 → memory/index-archive/{month}.md {tag}")

    if not args.apply:
        print("（dry-run。--apply 落地）")
        return 0

    # 寫歸檔（append；檔案不存在先給 header）
    moved_set = set()
    for month, idxs in by_month.items():
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        p = ARCHIVE_DIR / f"{month}.md"
        chunk = "\n".join(lines[i] for i in idxs) + "\n"
        before = p.read_text(encoding="utf-8").count("\n") if p.exists() else 0
        if not p.exists():
            p.write_text(ARCHIVE_HEADER.format(month=month) + chunk, encoding="utf-8")
        else:
            p.write_text(p.read_text(encoding="utf-8") + chunk, encoding="utf-8")
        after = p.read_text(encoding="utf-8").count("\n")
        gained = after - before
        # header 首建含 8 行固定結構
        expected = len(idxs) if before else len(idxs) + ARCHIVE_HEADER.format(month=month).count("\n")
        if gained != expected:
            print(f"❌ 守恆斷言失敗：{p.name} 增 {gained} 行 ≠ 預期 {expected}，abort（MEMORY.md 未動）")
            return 1
        moved_set.update(idxs)

    # 從 MEMORY.md 移除已搬列；在第一個被搬列的位置插入 digest rows（一次）。
    # 只有「inline 已清空的月份」才產 digest 列，避免同月既有彙整列又有散列的誤導。
    digest_lines = [
        f"| {month} | 月度彙整 | {len(idxs)} sessions，完整列已 verbatim 歸檔 | — | [→](memory/index-archive/{month}.md) |"
        for month, idxs in by_month.items()
        if month not in kept_months
    ]
    first_moved = min(moved_set)
    out = []
    inserted = False
    for i, l in enumerate(lines):
        if i in moved_set:
            if not inserted and i == first_moved:
                out.extend(digest_lines)
                inserted = True
            continue
        out.append(l)

    kept_rows = sum(1 for l in out if is_index_row(l))
    if kept_rows != args.keep:
        print(f"❌ 守恆斷言失敗：留下 {kept_rows} 列 ≠ keep {args.keep}，abort")
        return 1
    if len(out) != len(lines) - len(moved_set) + len(digest_lines):
        print("❌ 行數守恆斷言失敗，abort")
        return 1

    MEMORY.write_text("\n".join(out), encoding="utf-8")
    print(f"✅ rollup 完成：inline {total} → {kept_rows} 列 + {len(digest_lines)} digest；歸檔 {len(moved_set)} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
