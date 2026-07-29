import importlib.util
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "lang-sync"
    / "structured-translate.py"
)
SPEC = importlib.util.spec_from_file_location("structured_translate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_bisect_uses_paragraph_boundary_and_preserves_content():
    source = "第一段很短。\n\n第二段比較長，應該靠近中點。\n\n第三段收尾。"

    parts = MODULE._bisect_at_paragraph_boundary(source)

    assert len(parts) == 2
    assert "\n\n".join(parts) == source
    assert all(part.strip() for part in parts)


def test_bisect_refuses_single_paragraph():
    assert MODULE._bisect_at_paragraph_boundary("只有一段，不能從句中硬切。") == []


def test_extract_footnote_preserves_second_source_as_armored_desc():
    body = (
        "[^4]: [來源一](https://one.example/a) + "
        "[來源二](https://two.example/b) — 兩個來源共同支持。"
    )

    defs = MODULE.extract_footnote_defs(body)

    assert defs[0]["title"] == "來源一"
    assert defs[0]["url"] == "https://one.example/a"
    assert defs[0]["desc"] == "[來源二](@@LINK0@@) — 兩個來源共同支持。"
    assert defs[0]["_link_restore"] == [("@@LINK0@@", "https://two.example/b")]


def test_extract_footnote_recovers_nested_empty_link_source():
    body = (
        "[^2]: [Threads. 火燒島。取自 "
        "[](https://threads.example/post/1)) — 詳見原始連結。"
    )

    defs = MODULE.extract_footnote_defs(body)

    assert defs[0]["title"] == "Threads. 火燒島。取自"
    assert defs[0]["url"] == "https://threads.example/post/1"
    assert defs[0]["desc"] == "詳見原始連結。"


def test_validate_footnotes_rejects_markdown_in_translated_title():
    defs = [{"n": "1"}]
    translated = {"1": {"title": "[Source](broken)", "desc": "Description"}}

    assert MODULE.validate_footnotes(defs, translated) == [
        "footnote 1: title contains markdown/newline"
    ]
