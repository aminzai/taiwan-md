import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "numeric-event-check.py"
SPEC = importlib.util.spec_from_file_location("numeric_event_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

ZH = "---\ntitle: t\n---\n1947 年二二八事件爆發後，他四處奔走。\n"


def test_number_turned_into_another_number_is_a_candidate():
    # 2026-09-28 實例：vi〈呂捷〉把二二八寫成 Hai Ba Bát（2-3-8）
    tr = "---\ntitle: t\n---\nSau sự kiện Hai Ba Bát năm 1947, ông đi khắp nơi.\n"
    assert MODULE.check("二二八", "vi", ZH, tr) == 1


def test_house_style_and_reviewed_variants_are_recognized():
    for lang, body in [("vi", "Sau sự kiện 228 năm 1947"), ("fr", "après le 28-Février"),
                       ("hi", "दो-दो-आठ घटना के बाद"), ("es", "El Incidente de Febrero 28"), ("ko", "2·28 사건 이후")]:
        assert MODULE.check("二二八", lang, ZH, "---\ntitle: t\n---\n" + body + "\n") == 0, lang


def test_mentions_only_in_footnotes_frontmatter_or_urls_do_not_count():
    # 侯孝賢十一語：zh 的二二八只在 frontmatter；腳註定義與網址裡的中文是來源標題與路徑
    zh = ("---\ntitle: t\nnote: '二二八仍是禁忌'\n---\n他拍了悲情城市。[^1]\n\n"
          "[^1]: [二二八事件 — 維基百科](https://zh.wikipedia.org/wiki/二二八事件) — 條目\n")
    tr = "---\ntitle: t\n---\nHe made A City of Sadness.[^1]\n"
    assert MODULE.check("二二八", "en", zh, tr) == 0


def test_morakot_by_name_or_number_is_recognized_and_missing_is_not():
    zh = "---\ntitle: t\n---\n2009 年八八風災重創南台灣。\n"
    assert MODULE.check("八八風災", "de", zh, "---\ntitle: t\n---\nTaifun Morakot traf 2009 den Süden.\n") == 0
    assert MODULE.check("八八風災", "vi", zh, "---\ntitle: t\n---\nThảm họa 88 năm 2009.\n") == 0
    assert MODULE.check("八八風災", "de", zh, "---\ntitle: t\n---\nDie Katastrophe von 2009 traf den Süden.\n") == 1


def test_french_non_breaking_space_between_day_and_month_is_recognized():
    # 2026-09-28 實例：fr〈白先勇〉「parc de la paix du 28 février」審查為正確，數字與月份之間是 U+00A0
    tr = "---\ntitle: t\n---\nle parc de la paix du 28 février\n"
    assert MODULE.check("二二八", "fr", ZH, tr) == 0
