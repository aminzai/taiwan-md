import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "heading-level-align.py"
SPEC = importlib.util.spec_from_file_location("heading_level_align", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

FM = "---\ntitle: t\n---\n"


def test_promoted_subheadings_go_back_to_the_zh_level():
    # 2026-09-28 實例：ja〈台灣維基百科〉zh 九個 ### 全被譯成 ##
    zh = FM + "## 一\n\n內容一\n\n### 甲\n\n內容甲\n\n### 乙\n\n內容乙\n"
    tr = FM + "## One\n\ntext one\n\n## A\n\ntext a\n\n## B\n\ntext b\n"
    new, note = MODULE.align(zh, tr)
    assert new == FM + "## One\n\ntext one\n\n### A\n\ntext a\n\n### B\n\ntext b\n"
    assert note == "2/3 headings realigned"


def test_different_heading_count_is_left_alone():
    zh = FM + "## 一\n\n內容\n\n### 甲\n\n內容\n"
    tr = FM + "## One\n\ntext\n"
    assert MODULE.align(zh, tr) == (None, "heading count differs (2 vs 1)")


def test_same_count_but_headings_in_different_places_is_left_alone():
    # 標題數碰巧一樣、位置卻對不上（譯文少一節又多一節）：不能照順序硬套層級
    zh = FM + "## 一\n\n### 甲\n\n" + "內容" * 200 + "\n"
    tr = FM + "text " * 200 + "\n\n## One\n\n## Two\n"
    new, note = MODULE.align(zh, tr)
    assert new is None and note.startswith("positions do not line up")


def test_hashes_inside_code_fences_are_not_headings():
    zh = FM + "## 一\n\n```\n## 不是標題\n```\n\n### 甲\n"
    tr = FM + "## One\n\n```\n## not a heading\n```\n\n## A\n"
    new, _ = MODULE.align(zh, tr)
    assert "## not a heading" in new and new.endswith("### A\n")
