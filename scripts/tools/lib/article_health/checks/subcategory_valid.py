"""subcategory_valid — subcategory 取值必須真的在 taxonomy SSOT 裡。

SSOT：docs/taxonomy/SUBCATEGORY.md。

為什麼需要這條（2026-08-17 maintainer-am 誕生）：
既有的 frontmatter 檢查只問「有沒有 subcategory 這個欄位」，不問「填的值是不是
真的存在」。同一份 frontmatter 裡的兄弟欄位 `curation` 是有驗舉值的
（curation_consistency：非法值 → HARD），`subcategory` 沒有——兩個相鄰欄位兩把
不同的尺（REFLEXES #83）。

實測後果：idlccp1984 8/15-8/16 那批投稿裡，20 篇抽樣有 9 篇的 subcategory 是
SSOT 沒有的值（People 的「政治人物」「醫療與公共溝通」「農業與育種」、Culture 的
「語言與社群」「信仰與民俗」、Technology 的「光電與顯示」…），而 frontmatter gate
全部放行。更麻煩的是其中一部分**是我們自己的 auto-heal 寫進去的**——
`taxonomy_subcat._KEYWORD_BOOSTS` 用了非正典標籤，而 `allowed_subcategories()`
又把那些標籤 union 進「合法清單」，於是工具自己製造了漂移、自己認可了漂移。
分類體系是靠 subcategory 分群做導覽與知識圖譜的，值一旦長歪，壞的是分群本身，
而且不會有任何畫面報錯——是 silent failure，跟 curation 打錯字同型。

看守兩件事：
  1. 取值在該 category 的 SSOT 清單內 → 否則 WARN（附該分類合法值，可直接改）
  2. category 本身不在 SSOT（About / Politics / Language 等尚未收編）→ 不判
     （不是文章的錯，是 taxonomy 還沒寫到那節；避免製造假陽性）

嚴重度為什麼是 WARN 不是 HARD（2026-08-17 上線前 dogfood 校準，REFLEXES #66）：
先拿全庫 914 篇跑過才定嚴重度，結果是 **211 篇 / 135 個相異取值** 會命中。看清單
就知道這不是「投稿者亂填」——`Geography 縣市` 22 篇、`People 音樂` 13 篇、
`People 流行人物` 11 篇這種規模，是 **SSOT 自己漏收了實際在用的子分類**，不是那
211 篇寫錯。這種情況設 HARD 等於拿分類體系的缺口去擋文章，而且會當場讓 main 變紅。
所以本條先以 WARN 上線：讓漂移**看得見**（原本完全不可見），至於 135 個取值哪些該
收進 SSOT、哪些該改掉，那是動 211 檔的分類體系決策，命中 §自主權邊界（>50 檔），
留哲宇拍板（OBSERVER-QUEUE）。等 taxonomy 補齊、漂移收斂到低位再談升 HARD。
"""

from __future__ import annotations

from typing import Any, Iterator

from ..taxonomy_subcat import allowed_subcategories
from ..types import FileTarget, Severity, Violation

CHECK_NAME = "subcategory-valid"
DIMENSION = "frontmatter"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "docs/taxonomy/SUBCATEGORY.md"
APPLIES_TO = ["zh-TW"]


def _fm_line(target: FileTarget, key: str) -> int:
    for idx, line in enumerate(target.frontmatter_raw.splitlines(), start=2):
        if line.startswith(f"{key}:"):
            return idx
    return 1


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    fm = target.frontmatter
    sub = fm.get("subcategory")
    category = fm.get("category")

    # 缺值本身由 frontmatter_format 管，本條只管「填了但填錯」
    if not sub or not category:
        return

    sub = str(sub).strip().strip("'\"")
    category = str(category).strip().strip("'\"")

    allowed = allowed_subcategories(category)
    if not allowed:
        # taxonomy 還沒收這個 category，不在本條射程內
        return

    if sub not in allowed:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=(
                f"subcategory 取值不在 taxonomy 裡：{sub!r}（category={category}）。"
                f"合法值：{'、'.join(allowed)}"
                "（SSOT: docs/taxonomy/SUBCATEGORY.md；分群 / 導覽靠這個欄位，"
                "填了不存在的值不會報錯但會靜默壞掉分類）"
            ),
            line=_fm_line(target, "subcategory"),
            editorial_ref=EDITORIAL_REF,
        )
