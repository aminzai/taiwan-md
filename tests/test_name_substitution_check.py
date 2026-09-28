import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "name-substitution-check.py"
SPEC = importlib.util.spec_from_file_location("name_substitution_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_famous_name_standing_in_for_an_unfamiliar_one_is_caught():
    # 2026-09-28 實例：es〈蔡健雅〉整篇主角寫成 Tsai Ing-wen
    zh = "---\ntitle: '蔡健雅'\n---\n蔡健雅四度拿下金曲獎最佳華語女歌手。\n"
    tr = "---\ntitle: 'Tsai Ing-wen'\n---\nTsai Ing-wen ganó cuatro veces el Golden Melody.\n"
    assert MODULE.check("es", zh, tr) == [("蔡英文", 2)]


def test_a_name_the_source_mentions_under_any_alias_is_left_alone():
    zh = "---\ntitle: t\n---\n小英政府上任後推動年金改革。\n"
    tr = "---\ntitle: t\n---\nAfter the Tsai Ing-wen administration took office...\n"
    assert MODULE.check("en", zh, tr) == []


def test_capital_of_the_translation_language_is_caught_only_when_zh_never_mentions_that_country():
    # 2026-09-28 實例：vi 把台北寫成 Hà Nội
    zh = "---\ntitle: t\n---\n他在台北車站看火車進站。\n"
    assert MODULE.check("vi", zh, "Anh đứng ở ga Hà Nội nhìn tàu vào ga.\n") == [("河內", 1)]
    zh_vn = "---\ntitle: t\n---\n她從越南嫁來台灣。\n"
    assert MODULE.check("vi", zh_vn, "Cô ấy từ Hà Nội đến Đài Loan.\n") == []


def test_de_chiang_ification_counts_as_the_source_mentioning_chiang():
    # 八田與一〈去蔣化〉：en「remove Chiang Kai-shek symbols」是正確翻譯
    zh = "---\ntitle: t\n---\n統派人士反制去蔣化運動。\n"
    tr = "Pro-unification figures countered the movement to remove Chiang Kai-shek symbols.\n"
    assert MODULE.check("en", zh, tr) == []


def test_a_name_inside_a_longer_word_does_not_count():
    zh = "---\ntitle: t\n---\n他在台北長大。\n"
    assert MODULE.check("en", zh, "the Tsai Ing-wenesque style\n") == []
    assert MODULE.check("id", zh, "Jakartanya\n") == []


def test_a_second_tier_attractor_is_caught_too():
    # 2026-09-28 實例：es〈台灣半導體產業〉把 1985 年的政務委員李國鼎寫成 Lee Teng-hui
    zh = "---\ntitle: t\n---\n1985 年的一個下午，政務委員李國鼎走進行政院。\n"
    tr = "En una tarde de 1985, el ministro sin cartera Lee Teng-hui fue al Yuan Ejecutivo.\n"
    assert MODULE.check("es", zh, tr) == [("李登輝", 1)]


def test_a_name_the_source_already_writes_in_latin_script_is_left_alone():
    # zh 圖說引用 Wikimedia 檔名 Chiang_Kai-shek_Memorial_Hall.jpg——譯文照寫 Chiang Kai-shek 不是頂替
    zh = "---\ntitle: t\n---\n![館舍](https://commons.wikimedia.org/wiki/File:Chiang_Kai-shek_Memorial_Hall.jpg)\n"
    tr = "![Hall](https://commons.wikimedia.org/wiki/File:Chiang_Kai-shek_Memorial_Hall.jpg) The Chiang Kai-shek Memorial Hall.\n"
    assert MODULE.check("en", zh, tr) == []


def test_mandarin_turned_into_cantonese_is_caught():
    # 2026-09-28 實例：ru〈台灣嘻哈〉把金曲「最佳華語男歌手」寫成「最佳粵語歌手」——金曲沒有粵語獎項
    zh = "---\ntitle: t\n---\n第 30 屆金曲獎，他拿下最佳華語男歌手。\n"
    assert MODULE.check("ru", zh, "получил приз «Лучший вокалист на кантонском языке»\n") == [("粵語", 1)]
    assert MODULE.check("ru", "---\ntitle: t\n---\n他在香港發片。\n", "на кантонском языке\n") == []


def test_chinese_taipei_standing_in_for_a_taiwanese_place_is_caught_but_not_in_sports():
    # 2026-09-28 實例：pt〈台中市〉標題寫成「Taipé Chinesa」；體育語境的 Chinese Taipei 是正式名稱
    zh = "---\ntitle: '台中市：1887 年差點當首都'\n---\n台中市位在台灣中部。\n"
    assert MODULE.check("pt", zh, "---\ntitle: 'Taipé Chinesa: Quase Capital'\n---\n") == [("中華台北", 1)]
    zh_sport = "---\ntitle: t\n---\n她在奧運為台灣拿下金牌。\n"
    assert MODULE.check("en", zh_sport, "She won gold for Chinese Taipei at the Olympics.\n") == []
