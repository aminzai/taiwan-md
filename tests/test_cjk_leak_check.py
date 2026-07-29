import importlib.util
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "lang-sync"
    / "cjk-leak-check.py"
)
SPEC = importlib.util.spec_from_file_location("cjk_leak_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_ja_ignores_zh_markers_in_passthrough_frontmatter(tmp_path):
    path = tmp_path / "ja--example.md"
    path.write_text(
        "---\n"
        "title: '日本語の題名'\n"
        "rationale: '這個中文欄位是編輯資料'\n"
        "researchReport: 'reports/研究/那個人.md'\n"
        "---\n\n"
        "これは完全に日本語の本文です。\n",
        encoding="utf-8",
    )

    assert MODULE.scan_file(path, lang="ja") == []


def test_ja_still_flags_zh_marker_in_body(tmp_path):
    path = tmp_path / "ja--example.md"
    path.write_text(
        "---\n"
        "title: '日本語の題名'\n"
        "rationale: '這個中文欄位是編輯資料'\n"
        "---\n\n"
        "これは日本語ですが，那個段落は翻訳されていない。\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="ja")

    assert any("'那個'" in hit for hit in hits)
