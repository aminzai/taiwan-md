"""body_internal_links — 正文（非延伸閱讀）站內連結密度，INFO 級量測.

Trigger: 哲宇 2026-09-05 拍板 OBSERVER-QUEUE #39 選 A「先量起來＋補高流量前 50
篇」。issue #615（idlccp1984 8/18）建議「文章中藍色連結連著另一個文章」；
OBSERVER-QUEUE #39 量出 1,132 篇裡 674 篇（59%）**正文**完全沒有任何站內連結
——互鏈幾乎都放在文末延伸閱讀，而 6/14 埋點證實讀者滑不到那裡（捲動深度 CTA）。

本 plugin 只做「先量起來」那一半（推薦選項 (b)：做成持續量測指標，讓現況不會
三個月後又漂回去）。**INFO 級，不 warn 不 hard**——哲宇拍板是「先量」不是「先擋」，
逐篇補鏈是下一輪工單（見 reports/internal-links-top50-2026-09-05.md）。

量法（只算「正文」，排除下面三種，避免把「文末湊出來的連結」算成「讀者真的會
點到的連結」）：
  1. frontmatter — loader 已排除（不在 target.body 內）
  2. `## 延伸閱讀` / `**延伸閱讀**：` 或 `## 參考資料` 之後的內容（兩者取先出現者）
  3. 腳註定義行 `[^N]: ...`（那是來源清單，不是讀者順著讀下去會點的內文連結）

計數對象：
  - `[[wikilink]]` / `[[wikilink|顯示文字]]`（不驗證目標是否存在——那是
    wikilink-target 的工作，這裡只算「有沒有連」）
  - 指向 `/{category}/{slug}/` 的站內 markdown 連結（category 需匹配
    knowledge/ 底下實際存在的分類目錄，排除 /api/、/dashboard/、/about/、
    /terminology/... 這類非文章路由）

輸出：單一 INFO violation，message 內含人讀得懂的摘要，snippet 內含機器可
解析的 `count=N density=D zero=True/False`（供 dashboard 生成腳本 / 分析
script grep，同 word-count / media-richness 既有慣例：INFO 數字放 message，
不新增 Violation dataclass 欄位）。

Canonical: docs/editorial/EDITORIAL.md §wikilink + §延伸閱讀 / REWRITE-PIPELINE
§交叉連結。OBSERVER-QUEUE #39（docs/semiont/OBSERVER-QUEUE.md）+
reports/fortnight-deep-review-2026-09-05.md §4.2 G。
"""

from __future__ import annotations
import re
from pathlib import Path
from typing import Any, Iterator

from ..langs import TRANSLATION_LANGS
from ..types import FileTarget, Severity, Violation


CHECK_NAME = "body-internal-links"
DIMENSION = "structure"
DEFAULT_SEVERITY = Severity.INFO
EDITORIAL_REF = (
    "EDITORIAL.md §wikilink + §延伸閱讀 — OBSERVER-QUEUE #39 "
    "(docs/semiont/OBSERVER-QUEUE.md) + "
    "reports/fortnight-deep-review-2026-09-05.md §4.2 G"
)
APPLIES_TO = ["zh-TW"]

# 延伸閱讀 / 參考資料 之後不算正文——沿用 format_structure.py 的判定式
# （同一份 canonical 規則，兩個 plugin 各自的用途不同：format_structure 管
# 「有沒有這個 section」，這裡管「這個 section 之前算不算正文」）。
_RE_FURTHER_READING = re.compile(
    r"^(?:##\s*延伸閱讀|\*\*延伸閱讀\*\*\s*[：:])", re.MULTILINE
)
_RE_REFERENCES_H2 = re.compile(r"^##\s*參考資料", re.MULTILINE)
# 腳註定義行（沿用 word_count.py 的判定式）
_RE_FOOTNOTE_DEF_LINE = re.compile(r"^\[\^[^\]]+\]:.*$", re.MULTILINE)

# wikilink（沿用 wikilink_target.py / cross_reference.py 的判定式，只算數量
# 不驗證目標是否存在）
_RE_WIKILINK = re.compile(r"\[\[([^\]|\n]+?)(?:\|[^\]\n]+)?\]\]")
# 站內 markdown 連結 `[text](/category/slug/)`——category 對照
# knowledge/ 實際分類目錄，排除 /api/ /dashboard/ /about/ /terminology/ 等
# 非文章路由（同 link_target.py 的 `_looks_like_article_path` 精神，這裡
# 只取 zh-TW 無語言前綴這一種形狀，因為本 check 只跑 zh-TW）。
_RE_MD_LINK_INTERNAL = re.compile(r"\]\(/([a-z0-9-]+)/([^)\s#?]+?)/?\)")

# CJK 字元計數（沿用 word_count.py 的判定式，density 分母用同一把尺）
_RE_CJK = re.compile(r"[一-鿿㐀-䶿]")

_LANG_DIRS_SKIP = set(TRANSLATION_LANGS)
_KNOWLEDGE_ROOT = Path("knowledge")


def _known_categories() -> set[str]:
    """knowledge/ 底下實際存在的分類目錄（小寫），快取一次。"""
    cached = getattr(_known_categories, "_cache", None)
    if cached is not None:
        return cached
    cats: set[str] = set()
    if _KNOWLEDGE_ROOT.exists():
        for entry in _KNOWLEDGE_ROOT.iterdir():
            if (
                entry.is_dir()
                and entry.name not in _LANG_DIRS_SKIP
                and not entry.name.startswith("_")
            ):
                cats.add(entry.name.lower())
    _known_categories._cache = cats  # type: ignore[attr-defined]
    return cats


def _reset_cache() -> None:
    """Test helper — invalidate the category cache."""
    if hasattr(_known_categories, "_cache"):
        delattr(_known_categories, "_cache")


def _body_main(body: str) -> str:
    """正文 = body 扣掉延伸閱讀／參考資料之後的內容，再扣掉腳註定義行。"""
    cutoffs = []
    m1 = _RE_FURTHER_READING.search(body)
    if m1:
        cutoffs.append(m1.start())
    m2 = _RE_REFERENCES_H2.search(body)
    if m2:
        cutoffs.append(m2.start())
    cutoff = min(cutoffs) if cutoffs else len(body)
    main = body[:cutoff]
    return _RE_FOOTNOTE_DEF_LINE.sub("", main)


def _count_links(body_main: str) -> tuple[int, int]:
    """回傳 (wikilink_count, md_link_count)。"""
    wiki_count = len(_RE_WIKILINK.findall(body_main))
    known_cats = _known_categories()
    md_count = 0
    for m in _RE_MD_LINK_INTERNAL.finditer(body_main):
        if m.group(1) in known_cats:
            md_count += 1
    return wiki_count, md_count


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    body_main = _body_main(target.body)
    wiki_count, md_count = _count_links(body_main)
    count = wiki_count + md_count
    cjk = len(_RE_CJK.findall(body_main))
    density = round(count / cjk * 1000, 2) if cjk > 0 else 0.0
    zero = count == 0

    yield Violation(
        check=CHECK_NAME,
        severity=Severity.INFO,
        message=(
            f"正文站內連結：{count} 個（wikilink {wiki_count} + "
            f"md-link {md_count}），密度 {density}/千字"
            + ("（零連結——讀者在正文裡點不到任何相關文章）" if zero else "")
        ),
        editorial_ref=EDITORIAL_REF,
        snippet=f"count={count} density={density} zero={zero}",
    )
