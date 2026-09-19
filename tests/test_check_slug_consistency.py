"""check-slug-consistency.py — 2026-09-19 補的兩把尺：多數決 fallback 與同語言撞號。

背景：maintainer-am 連五輪手動對照投稿譯文的檔名跟其他語言 sibling 是否一致，
每輪都命中（REFLEXES #15）；2026-09-14 LESSONS
`same-language-slug-collision-is-invisible-to-both-instruments`——既有兩把尺都只比 en，
看不見同一語言目錄裡已經有另一份同源檔。
"""
import importlib.util
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "tools" / "check-slug-consistency.py"
)
SPEC = importlib.util.spec_from_file_location("check_slug_consistency", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

SRC = "Art/某篇.md"


def _sib(**langs):
    return {SRC: {lang: names for lang, names in langs.items()}}


def test_en_canonical_wins_over_majority():
    pairs = [(Path("knowledge/de/Art/wrong.md"), SRC)]
    bad, bad_maj, coll = MODULE.check_pairs(pairs, {SRC: "right.md"}, _sib(ja=["other.md"], ko=["other.md"]))
    assert [(str(r), n) for r, n, _ in bad] == [("knowledge/de/Art/wrong.md", "right.md")]
    assert bad_maj == [] and coll == []


def test_majority_fallback_when_en_missing_needs_two_siblings():
    pairs = [(Path("knowledge/de/Art/wrong.md"), SRC)]
    # 只有一個 sibling → 不成慣例，不報
    bad, bad_maj, coll = MODULE.check_pairs(pairs, {}, _sib(ja=["right.md"]))
    assert bad == [] and bad_maj == [] and coll == []
    # 兩個 sibling 同名 → 報多數
    bad, bad_maj, coll = MODULE.check_pairs(pairs, {}, _sib(ja=["right.md"], ko=["right.md"]))
    assert bad == [] and coll == []
    assert [(str(r), n, c) for r, n, c, _ in bad_maj] == [("knowledge/de/Art/wrong.md", "right.md", 2)]


def test_same_language_collision_is_reported_even_when_name_is_canonical():
    pairs = [(Path("knowledge/de/Art/right.md"), SRC)]
    bad, bad_maj, coll = MODULE.check_pairs(
        pairs, {SRC: "right.md"}, _sib(de=["already-here.md"], ja=["right.md"]))
    assert bad == [] and bad_maj == []
    assert [(str(r), o) for r, o, _ in coll] == [("knowledge/de/Art/right.md", ["already-here.md"])]


def test_self_is_not_a_collision():
    pairs = [(Path("knowledge/de/Art/right.md"), SRC)]
    bad, bad_maj, coll = MODULE.check_pairs(pairs, {SRC: "right.md"}, _sib(de=["right.md"]))
    assert (bad, bad_maj, coll) == ([], [], [])


def test_translated_from_text_reads_frontmatter_only():
    text = "---\ntitle: 'x'\ntranslatedFrom: 'Art/某篇.md'\n---\n\ntranslatedFrom: 'body/should-not-count.md'\n"
    assert MODULE._translated_from_text(text) == "Art/某篇.md"


def test_en_file_skips_name_check_but_reports_collision():
    pairs = [(Path("knowledge/en/People/new-name.md"), SRC)]
    bad, bad_maj, coll = MODULE.check_pairs(
        pairs, {SRC: "old-name.md"}, _sib(en=["old-name.md"], ja=["old-name.md"]))
    assert bad == [] and bad_maj == []
    assert [(str(r), o) for r, o, _ in coll] == [("knowledge/en/People/new-name.md", ["old-name.md"])]
