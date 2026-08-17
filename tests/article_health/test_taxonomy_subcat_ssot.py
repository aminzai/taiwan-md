"""taxonomy_subcat 與 SUBCATEGORY.md 的對賬測試。

這三條測試都是 2026-08-17 maintainer-am 從真實故障回推出來的。當天 idlccp1984
一批 67 個投稿裡，多篇 frontmatter 帶著 SSOT 根本不存在的 subcategory 通過閘門，
追上游才發現源頭在我們自己的推論工具，而且沒有任何東西在對賬。

三個缺陷各對應下面一條測試：
  1. 標題 regex 用 `\\s*$` 收尾 → `### 👥 People（人物）— 已大致完成` 認不出來，
     People 整節沒被解析、13 個子分類全被歸進上一個分類（Nature）
  2. `_KEYWORD_BOOSTS` 用了 SSOT 沒有的標籤（政治人物 / 企業家 / 生態保育…），
     而 auto-heal 會把它寫進投稿者的 frontmatter
  3. `allowed_subcategories()` 把 boost 標籤 union 進「合法清單」，於是工具自己
     製造的漂移又被工具自己認可，形成閉環

對應 REFLEXES #91（建造與登記兩個不同步的代謝）與 #83（同族檢查兩把尺）。
"""

from __future__ import annotations

from lib.article_health.taxonomy_subcat import (
    _parse_taxonomy_file,
    allowed_subcategories,
    boost_label_drift,
)


def test_every_category_section_is_parsed():
    """標題後面接註解 / 破折號時，該節仍要被解析到。

    迴歸目標：People 那節標題是 `### 👥 People（人物）— 已大致完成`。
    """
    tax = _parse_taxonomy_file()
    for category in ("History", "Geography", "Culture", "Food", "Art",
                     "Music", "Technology", "Nature", "People", "Society",
                     "Economy", "Lifestyle"):
        assert tax.get(category), f"{category} 這節沒被解析到（標題 regex 又太嚴？）"


def test_people_subcategories_not_leaked_into_previous_section():
    """People 的子分類不可以出現在 Nature 的合法清單裡。

    迴歸目標：People 標題認不出來時，它的 rows 會被記到上一個 current。
    """
    nature = set(allowed_subcategories("Nature"))
    for people_only in ("體育", "音樂與表演", "歷史人物", "科技與企業"):
        assert people_only not in nature, (
            f"Nature 的合法清單混進了 People 的「{people_only}」"
            "——標題解析又漏掉某一節了"
        )


def test_keyword_boost_labels_all_exist_in_ssot():
    """推論表用的每個標籤都必須是 SSOT 裡真的有的子分類。

    這條壞掉代表 auto-heal 會把 SSOT 不存在的值寫進文章 frontmatter。
    """
    drift = boost_label_drift()
    assert drift == [], (
        "_KEYWORD_BOOSTS 用了 taxonomy 沒有的子分類名："
        + "、".join(f"{c}/{s}" for c, s in drift)
        + "（改 boost 標籤對齊 SUBCATEGORY.md，或把該子分類正式收進 SSOT）"
    )


def test_allowed_subcategories_is_ssot_only():
    """合法清單只能來自 SSOT，不能被推論表自己撐大。"""
    people = allowed_subcategories("People")
    assert "政治與民主" in people, "SSOT 的 People 子分類沒讀到"
    assert "政治人物" not in people, (
        "「政治人物」不是 SUBCATEGORY.md 裡的值，卻出現在合法清單——"
        "allowed_subcategories() 又把 boost 標籤 union 進來了"
    )


def test_unknown_category_returns_empty_not_boost_labels():
    """SSOT 沒收的分類回空清單，讓上游 warn 缺值，而不是補一個假的正典。"""
    assert allowed_subcategories("NoSuchCategory") == []
