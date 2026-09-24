"""隔離區檔名 `{lang}--{slug}.md` 要被認成該語言，不能退回 zh-TW（2026-09-25）。"""
from pathlib import Path

from lib.article_health.loader import _derive_meta_from_path


def test_quarantine_basename_carries_language():
    lang, _, slug = _derive_meta_from_path(Path("/tmp/run/quarantine/pt--ma-ying-jeou-meme.md"))
    assert (lang, slug) == ("pt", "ma-ying-jeou-meme")


def test_unknown_prefix_still_defaults_to_zh():
    lang, _, _ = _derive_meta_from_path(Path("/tmp/xx--notes.md"))
    assert lang == "zh-TW"


def test_knowledge_paths_unchanged():
    assert _derive_meta_from_path(Path("knowledge/id/Economy/x.md"))[0] == "id"
    assert _derive_meta_from_path(Path("knowledge/Economy/發票.md"))[0] == "zh-TW"
