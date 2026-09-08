"""subcategory-translation-parity — 譯文的 subcategory 必須跟 zh 原文同一個值。

SSOT：譯文 frontmatter 的 `translatedFrom` 指到的那篇 zh 原文。

為什麼需要這條（2026-09-08 twmd-maintainer-am 誕生）：
分類頁的分群鍵**永遠是 zh-TW 的原始 frontmatter 值**，各語言的顯示文字是查
`src/data/subcategory-i18n.json` 這張對照表得到的，查不到就 fallback 回原始 key
（`category-hub.template.astro` 的註解白紙黑字寫著這個前提）。所以譯者「順手把
subcategory 也翻成目標語言」看起來很自然，實際上是把這篇文章從它該待的那一群
裡拿掉——`buildSubcategoryGroups()` 用完全比對分群，翻過的值自成一群；而該群
只有 1 篇時又會被併進 `__others__`。讀者看到的結果是這篇掉進「其他」。

姊妹條 `subcategory-valid` 問的是另一個問題（值在不在 taxonomy 清單裡），而且
`APPLIES_TO = ["zh-TW"]`——譯文完全不在它的射程內。這是那道閘門旁邊沒有人守的
另一半。

嚴重度為什麼是 WARN（上線前對全庫 dogfood，REFLEXES #66）：
誕生當下實測 13 個語言共 **1,634 篇** 的 subcategory 不是正典值，其中 **920 篇**
已經因此掉進所屬分類頁的「其他」組（vi/People 31 篇、ko/People 25 篇、vi/Culture
25 篇為前三）。這個規模動的是 >50 檔，命中 §自主權邊界，留哲宇拍板
（OBSERVER-QUEUE #51）。設 HARD 會當場讓 main 變紅，也會擋掉所有新譯文——所以
先以 WARN 上線讓漂移看得見，等 backlog 收斂再談升 HARD。這條的即時價值在
pre-commit 與 PR：新譯文一寫錯就看得到，存量不再增加。
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator

from ..loader import load_target
from ..types import FileTarget, Severity, Violation

CHECK_NAME = "subcategory-translation-parity"
DIMENSION = "frontmatter"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "docs/taxonomy/SUBCATEGORY.md + src/templates/category-hub.template.astro §groupLabel"
APPLIES_TO = ["*"]


def _knowledge_root(path: Path) -> Path | None:
    """從被檢查的檔往上找 `knowledge/`——不從 __file__ 推。

    譯文的 `translatedFrom` 是相對 knowledge/ 的 'Category/檔名.md'。用
    plugin 自己的 __file__ 去推 repo 根，在 worktree、tmp fixture、以及任何
    把 scripts/ 搬位置的情境都會靜默指到別棵樹（REFLEXES #82 的同型：拿
    「我住哪」當「被驗的東西住哪」的替身）。從 target 自己的路徑往上走，
    量的才是這篇文章實際所在的那棵樹。
    """
    for parent in path.resolve().parents:
        if parent.name == "knowledge":
            return parent
    return None


def _fm_line(target: FileTarget, key: str) -> int:
    for idx, line in enumerate(target.frontmatter_raw.splitlines(), start=2):
        if line.startswith(f"{key}:"):
            return idx
    return 1


def _clean(value: Any) -> str:
    return str(value or "").strip().strip("'\"")


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    # 只管譯文；zh-TW 原文由 subcategory-valid 管
    if not target.is_translation:
        return

    fm = target.frontmatter
    sub = _clean(fm.get("subcategory"))
    source_rel = _clean(fm.get("translatedFrom"))

    # 缺值分別由 frontmatter-format / orphan-translation-check 管，本條不重複報
    if not sub or not source_rel:
        return

    root = _knowledge_root(target.path)
    if root is None:
        return

    source_path = root / source_rel
    if not source_path.is_file():
        # 指到不存在的原文是孤兒問題，orphan-translation-check.sh 的射程
        return

    try:
        source = load_target(source_path)
    except Exception:
        return

    source_sub = _clean(source.frontmatter.get("subcategory"))
    if not source_sub or source_sub == sub:
        return

    yield Violation(
        check=CHECK_NAME,
        severity=Severity.WARN,
        message=(
            f"譯文 subcategory 跟 zh 原文對不上：這裡是 {sub!r}，"
            f"{source_rel} 是 {source_sub!r}。分類頁的分群鍵永遠用 zh 原始值"
            f"（顯示文字走 src/data/subcategory-i18n.json 對照表），"
            f"翻過的值會讓這篇自成一群、只有 1 篇時再被併進「其他」。"
            f"改回 {source_sub!r} 即可。"
        ),
        line=_fm_line(target, "subcategory"),
        editorial_ref=EDITORIAL_REF,
    )
