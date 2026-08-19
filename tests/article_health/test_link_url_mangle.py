"""Regression tests for the link-URL corruption healer.

Two families: Prettier italic-caption mangling, and stray whitespace left
inside link destinations by generation tools (2026-08-15 contributor batch).
"""

from pathlib import Path

from lib.article_health.checks import link_url_mangle
from lib.article_health.loader import load_target


def _target(tmp_path: Path, line: str):
    path = tmp_path / "sample.md"
    path.write_text(line + "\n", encoding="utf-8")
    return path, load_target(path)


def test_fix_restores_mangled_commons_url_and_moves_link(tmp_path):
    path, target = _target(
        tmp_path,
        "_Photo: [CC BY](https://commons.wikimedia.org/wiki/File:%E8%9B%8B*2025-12-02.jpg).\\_",
    )

    assert len(list(link_url_mangle.check(target, {}))) == 1
    assert link_url_mangle.fix(target, {}) == 1

    healed = path.read_text(encoding="utf-8")
    assert "_Photo: CC BY._" in healed
    assert (
        "[CC BY](https://commons.wikimedia.org/wiki/"
        "File:%E8%9B%8B_2025-12-02.jpg)"
    ) in healed
    assert len(list(link_url_mangle.check(load_target(path), {}))) == 0


def test_fix_moves_at_risk_url_before_prettier_can_mangle(tmp_path):
    path, target = _target(
        tmp_path,
        "_Photo: [Commons](https://commons.wikimedia.org/wiki/File:%E8%9B%8B_05.jpg)._",
    )

    assert len(list(link_url_mangle.check(target, {}))) == 1
    assert link_url_mangle.fix(target, {}) == 1
    assert len(list(link_url_mangle.check(load_target(path), {}))) == 0


def test_fix_ignores_legitimate_non_wiki_star_url(tmp_path):
    path, target = _target(
        tmp_path,
        "_Source: [query](https://example.com/search?q=50000*)._",
    )

    assert link_url_mangle.fix(target, {}) == 0
    assert "50000*" in path.read_text(encoding="utf-8")


def test_fix_restores_mangled_wiki_url_outside_caption(tmp_path):
    path, target = _target(
        tmp_path,
        "[Jack Edwards](https://en.wikipedia.org/wiki/Jack*Edwards*(British_Army_soldier))",
    )

    assert link_url_mangle.fix(target, {}) == 1
    assert (
        "https://en.wikipedia.org/wiki/Jack_Edwards_(British_Army_soldier)"
        in path.read_text(encoding="utf-8")
    )


def test_fix_supports_legacy_star_wrapped_caption(tmp_path):
    path, target = _target(
        tmp_path,
        "*Image: [Commons](https://commons.wikimedia.org/wiki/File:%E5%8F%B0*Taiwan*01.jpg)*",
    )

    assert link_url_mangle.fix(target, {}) == 1
    healed = path.read_text(encoding="utf-8")
    assert "*Image: Commons*" in healed
    assert "File:%E5%8F%B0_Taiwan_01.jpg" in healed


def test_fix_preserves_balanced_parentheses_in_url(tmp_path):
    path, target = _target(
        tmp_path,
        "_Photo: [Commons](https://commons.wikimedia.org/wiki/File:Hinton_(3x4*cropped).jpg).*",
    )

    assert link_url_mangle.fix(target, {}) == 1
    healed = path.read_text(encoding="utf-8")
    assert (
        "[Commons](https://commons.wikimedia.org/wiki/File:Hinton_(3x4_cropped).jpg)"
        in healed
    )
    assert len(list(link_url_mangle.check(load_target(path), {}))) == 0


def test_fix_dry_run_does_not_write(tmp_path):
    path, target = _target(
        tmp_path,
        "_Photo: [Commons](https://commons.wikimedia.org/wiki/File:%E8%9B%8B_13.jpg)._",
    )
    before = path.read_text(encoding="utf-8")

    assert link_url_mangle.fix(target, {"dry_run": True}) == 1
    assert path.read_text(encoding="utf-8") == before


# ── whitespace inside link destinations (2026-08-15) ──────────────────────────
# One space before `)` per link, produced by whatever generated the article.
# The link still resolves, so nothing renders wrong — but footnote-format then
# reports every affected footnote as its own "格式不合規範", turning a single
# upstream defect into hundreds of unrelated-looking errors.


def test_flags_and_fixes_trailing_space_in_footnote_url(tmp_path):
    path, target = _target(
        tmp_path,
        "[^1]: [原民會：噶瑪蘭族](https://www.cip.gov.tw/zh-tw/tribe/info.html?cumid ) — 政府官方族群介紹。",
    )

    assert len(list(link_url_mangle.check(target, {}))) == 1
    assert link_url_mangle.fix(target, {}) == 1

    healed = path.read_text(encoding="utf-8")
    assert "info.html?cumid) — 政府官方族群介紹。" in healed
    assert len(list(link_url_mangle.check(load_target(path), {}))) == 0


def test_fixes_trailing_space_in_image_url(tmp_path):
    path, target = _target(
        tmp_path,
        "![蘭陽平原遺址分布。](https://www.lym.gov.tw/images/20200928-e-kj-122-08.jpg )",
    )

    assert link_url_mangle.fix(target, {}) == 1
    assert "122-08.jpg)" in path.read_text(encoding="utf-8")


def test_counts_every_whitespace_link_on_one_line(tmp_path):
    path, target = _target(
        tmp_path,
        "See [a](https://a.example/x ) and [b](https://b.example/y ).",
    )

    # Reported once per line, but every link is repaired.
    assert len(list(link_url_mangle.check(target, {}))) == 1
    assert link_url_mangle.fix(target, {}) == 2

    healed = path.read_text(encoding="utf-8")
    assert "[a](https://a.example/x)" in healed
    assert "[b](https://b.example/y)" in healed


def test_leaves_clean_urls_untouched(tmp_path):
    path, target = _target(
        tmp_path,
        "[^1]: [乾淨的來源](https://example.com/a?b=c) — 沒有多餘空白。",
    )

    assert len(list(link_url_mangle.check(target, {}))) == 0
    assert link_url_mangle.fix(target, {}) == 0


def test_respects_angle_bracket_destination(tmp_path):
    """`<…>` is CommonMark's sanctioned way to carry a literal space — leave it."""
    path, target = _target(
        tmp_path,
        "[spec](<https://example.com/a b>)",
    )

    assert len(list(link_url_mangle.check(target, {}))) == 0
    assert link_url_mangle.fix(target, {}) == 0
    assert "<https://example.com/a b>" in path.read_text(encoding="utf-8")
