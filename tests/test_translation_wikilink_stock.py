import importlib.util
import sys
from pathlib import Path

LANG_SYNC = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"
sys.path.insert(0, str(LANG_SYNC))
SPEC = importlib.util.spec_from_file_location("translation_wikilink_stock", LANG_SYNC / "translation-wikilink-stock.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)
X = MODULE.X


def _index(monkeypatch):
    # 江蕙有 es 譯文；蔡依林是 zh 條目但沒有 es 譯文（驗 A 類只收「有譯文」的）
    monkeypatch.setitem(X._STEM_CACHE, str(X.KNOWLEDGE), {"江蕙": "People/江蕙.md", "蔡依林": "People/蔡依林.md"})
    return X.LocalizerIndex(
        cat_map={"people": "People"},
        zh_to_lang_slug={"People/江蕙.md": {"es": "people/jody-chiang"}},
        lang_slug_set={"es": {"people/jody-chiang"}},
    )


def test_latin_label_with_a_translated_target_becomes_a_link(monkeypatch):
    body = "la aparición de [[江蕙|Jody Chiang]] trajo\n"
    new, counts, _ = MODULE.rewrite(body, "es", _index(monkeypatch))
    assert new == "la aparición de [Jody Chiang](/es/people/jody-chiang/) trajo\n"
    assert counts == {"A": 1}


def test_english_name_as_target_is_left_for_the_zh_alignment_tool(monkeypatch):
    # 2026-09-28 實例：es〈台語歌演化〉把 zh 的 [[江蕙]] 寫成 [[Jody Chiang]]
    body = "la aparición de [[Jody Chiang]] trajo\n"
    new, counts, _ = MODULE.rewrite(body, "es", _index(monkeypatch))
    assert new == body and counts == {"B": 1}


def test_chinese_label_is_left_alone_even_when_the_target_resolves(monkeypatch):
    # 改成連結的話錨字還是中文——讀者看到的問題沒解決，交給找名字的那一步
    body = "[[江蕙]] y [[蔡依林]]\n"
    new, counts, _ = MODULE.rewrite(body, "es", _index(monkeypatch))
    assert new == body and counts == {"C": 2}


def test_code_fences_are_not_touched(monkeypatch):
    body = "```\n[[江蕙|Jody Chiang]]\n```\n[[江蕙|Jody Chiang]]\n"
    new, counts, _ = MODULE.rewrite(body, "es", _index(monkeypatch))
    assert new == "```\n[[江蕙|Jody Chiang]]\n```\n[Jody Chiang](/es/people/jody-chiang/)\n"
    assert counts == {"A": 1}
