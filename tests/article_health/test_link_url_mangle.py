"""Regression tests for the Prettier italic-caption URL mangle healer."""

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


def test_fix_dry_run_does_not_write(tmp_path):
    path, target = _target(
        tmp_path,
        "_Photo: [Commons](https://commons.wikimedia.org/wiki/File:%E8%9B%8B_13.jpg)._",
    )
    before = path.read_text(encoding="utf-8")

    assert link_url_mangle.fix(target, {"dry_run": True}) == 1
    assert path.read_text(encoding="utf-8") == before
