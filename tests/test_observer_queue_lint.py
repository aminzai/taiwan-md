"""
test_observer_queue_lint.py — scripts/tools/observer-queue-lint.py 單元測試

覆蓋：§待決 段的止錨（只讀到下一個 H2）、欄數不足、預設選項／default-action 空欄、
跳脫管線 `\\|` 不當分隔、全綠案例。全部用假表格，不碰真實 OBSERVER-QUEUE.md。
"""
import importlib.util
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "observer-queue-lint.py"
)
SPEC = importlib.util.spec_from_file_location("observer_queue_lint", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

HEAD = """# OBSERVER-QUEUE

## 待決

| #   | 進佇列日   | 決策 | 預設選項 | 不決策的代價 | default-action |
| --- | ---------- | ---- | -------- | ------------ | -------------- |
"""

TAIL = """
## 已決

| 日期 | 決策 | 結果 |
| --- | --- | --- |
| 2026-09-17 | #50 這列不該被讀 | 只有三欄但住在已決 |
"""


def test_all_green():
    text = HEAD + "| 68  | 2026-09-17 | 分岔怎麼合 | **B** | 站上看不到 | 🔒紅線 |\n" + TAIL
    rows = MODULE.pending_rows(text)
    assert [MODULE.split_cells(l)[0] for _, l in rows] == ["68"]
    assert MODULE.lint_rows(rows) == []


def test_missing_columns_reported():
    text = HEAD + "| 60  | 2026-09-10 | 只有分析沒有選項 |\n" + TAIL
    problems = MODULE.lint_rows(MODULE.pending_rows(text))
    assert len(problems) == 1
    assert "#60" in problems[0] and "3 欄" in problems[0]


def test_empty_default_cells_reported():
    text = HEAD + "| 61  | 2026-09-10 | 決策 |  | 代價 |  |\n" + TAIL
    problems = MODULE.lint_rows(MODULE.pending_rows(text))
    assert any("預設選項欄是空的" in p for p in problems)
    assert any("default-action 欄是空的" in p for p in problems)


def test_escaped_pipe_not_a_separator():
    text = HEAD + "| 62  | 2026-09-10 | 用 `a \\| b` 舉例 | **A** | 代價 | 無 |\n" + TAIL
    rows = MODULE.pending_rows(text)
    assert len(MODULE.split_cells(rows[0][1])) == 6
    assert MODULE.lint_rows(rows) == []


def test_stops_at_next_h2():
    text = HEAD + "| 63  | 2026-09-10 | 決策 | **A** | 代價 | 無 |\n" + TAIL
    rows = MODULE.pending_rows(text)
    assert len(rows) == 1  # 已決那列（也是數字開頭的 2026-09-17）沒被算進來


def test_no_pending_section():
    assert MODULE.pending_rows("# 空檔案\n\n## 已決\n") == []
