"""Tests for body_internal_links plugin.

Trigger: 哲宇 2026-09-05 拍板 OBSERVER-QUEUE #39 選 A「先量起來＋補高流量前
50 篇」。這個 plugin 只做「量」——INFO 級，測試重點是「正文 vs 延伸閱讀／
參考資料／腳註定義行」的切分是否正確，而不是 gate 行為（本 check 沒有 HARD/
WARN 分支）。
"""

from pathlib import Path

import pytest

from lib.article_health.checks import body_internal_links as bil
from lib.article_health.loader import load_target
from lib.article_health.types import Severity


def _write_tmp(tmp_path: Path, body: str, frontmatter: str = "") -> Path:
    content = f"---\n{frontmatter}---\n{body}" if frontmatter else body
    f = tmp_path / "test.md"
    f.write_text(content, encoding="utf-8")
    return f


def _check(tmp_path: Path, body: str, frontmatter: str = ""):
    f = _write_tmp(tmp_path, body, frontmatter)
    target = load_target(f)
    violations = list(bil.check(target, {}))
    assert len(violations) == 1  # 永遠只有一條 INFO 摘要（同 word-count 慣例）
    return violations[0]


@pytest.fixture
def fake_knowledge(tmp_path, monkeypatch):
    """Stand up a tiny `knowledge/` tree so md-link category lookup works."""
    root = tmp_path / "knowledge"
    (root / "History").mkdir(parents=True)
    (root / "History" / "清朝.md").write_text("---\ntitle: x\n---\n")
    (root / "Music").mkdir()
    (root / "Music" / "五月天.md").write_text("---\ntitle: x\n---\n")
    monkeypatch.setattr(bil, "_KNOWLEDGE_ROOT", root)
    bil._reset_cache()
    yield root
    bil._reset_cache()


def _parse_snippet(v) -> dict:
    """snippet 格式：`count=N density=D zero=True/False`。"""
    parts = dict(kv.split("=", 1) for kv in v.snippet.split())
    return parts


# ─── Case 1: 完全沒有連結 → zero=True ────────────────────────────────────


def test_no_links_is_zero(tmp_path, fake_knowledge):
    body = "這是一段沒有任何連結的正文。" * 20
    v = _check(tmp_path, body)
    assert v.severity == Severity.INFO
    parts = _parse_snippet(v)
    assert parts["count"] == "0"
    assert parts["zero"] == "True"
    assert "零連結" in v.message


# ─── Case 2: wikilink 算數 ────────────────────────────────────────────────


def test_wikilink_counted(tmp_path, fake_knowledge):
    body = "正文提到 [[五月天]] 這個樂團。" + "填字。" * 20
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "1"
    assert parts["zero"] == "False"
    assert "wikilink 1" in v.message


# ─── Case 3: 指向已知分類的 markdown 連結算數；未知分類不算 ──────────────


def test_md_link_to_known_category_counted(tmp_path, fake_knowledge):
    body = (
        "正文提到 [清朝](/history/清朝/) 這段歷史。"
        + "填字。" * 20
    )
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "1"
    assert "md-link 1" in v.message


def test_md_link_to_unknown_route_not_counted(tmp_path, fake_knowledge):
    body = (
        "參考 [儀表板](/dashboard/) 跟 [某篇部落格](/blog/some-post/)。"
        + "填字。" * 20
    )
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    # /dashboard/ 只有一段（不符 /category/slug/ 形狀）；/blog/some-post/
    # 有兩段但 blog 不是 knowledge/ 底下的真實分類——兩者都不算站內文章連結。
    assert parts["count"] == "0"
    assert parts["zero"] == "True"


# ─── Case 4: 延伸閱讀之後的連結不算正文 ──────────────────────────────────


def test_further_reading_links_excluded(tmp_path, fake_knowledge):
    body = (
        "正文完全沒有連結。" * 20
        + "\n\n## 延伸閱讀\n\n"
        + "- [五月天](/music/五月天/) — 相關樂團\n"
        + "- [[清朝]]\n"
    )
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "0"
    assert parts["zero"] == "True"


def test_references_section_links_excluded(tmp_path, fake_knowledge):
    body = (
        "正文完全沒有連結，但用了腳註[^1]。" * 10
        + "\n\n## 參考資料\n\n"
        + "[^1]: 見 [清朝](/history/清朝/) 條目。\n"
    )
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "0"
    assert parts["zero"] == "True"


# ─── Case 5: 正文自己的腳註定義行不算（即使還沒到延伸閱讀）───────────────


def test_footnote_def_line_excluded_before_cutoff(tmp_path, fake_knowledge):
    body = (
        "正文提到某件事[^1]，本身沒有連結。" * 10
        + "\n[^1]: 出處見 [五月天](/music/五月天/)。\n"
        + "後面繼續寫正文。" * 10
    )
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "0"
    assert parts["zero"] == "True"


# ─── Case 6: density 計算（每千字）────────────────────────────────────────


def test_density_per_thousand_chars(tmp_path, fake_knowledge):
    # 1000 CJK chars, 1 wikilink → density 應為 1.0
    body = "[[五月天]]" + "字" * 1000
    v = _check(tmp_path, body)
    parts = _parse_snippet(v)
    assert parts["count"] == "1"
    assert float(parts["density"]) == pytest.approx(1.0, abs=0.01)
