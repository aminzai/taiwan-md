"""curation_consistency — 查證狀態欄位一致性看守。

設計 canonical：reports/design-curation-tier-2026-08-04.md。
三態語意：curation: 'verified'（🔎 已深度查證徽章）/ 缺省（一般文章）/
'incubating'（🌱 進化中說明條，社群貢獻待深度查證）。

看守三件事：
  1. 取值合法性 — 'verified' / 'incubating' 之外的值 → HARD（template 靜默不渲染，
     打錯字會變成「以為標了其實沒標」的 silent failure）
  2. incubating 與 featured 互斥 — incubating 不進精選（策展規則 canonical 在
     MAINTAINER-PIPELINE §1b），首頁精選邏輯不另設 filter，靠這條 lint 守 → HARD
  3. verified 應同步 lastHumanReview: true — 轉正 SOP 兩欄一起動
     （dashboard human-reviewed% 靠後者）→ WARN
"""

from __future__ import annotations
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation


CHECK_NAME = "curation-consistency"
DIMENSION = "frontmatter"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "reports/design-curation-tier-2026-08-04.md + MAINTAINER-PIPELINE §1b"
APPLIES_TO = ["zh-TW"]

_VALID = {"verified", "incubating"}


def _fm_line(target: FileTarget, key: str) -> int:
    for idx, line in enumerate(target.frontmatter_raw.splitlines(), start=2):
        if line.startswith(f"{key}:"):
            return idx
    return 1


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    fm = target.frontmatter
    cur = fm.get("curation")
    if cur is None:
        return

    if cur not in _VALID:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=(
                f"curation 取值非法：{cur!r}（合法值 verified / incubating；"
                "template 對非法值靜默不渲染 = silent failure）"
            ),
            line=_fm_line(target, "curation"),
            editorial_ref=EDITORIAL_REF,
        )
        return

    featured = fm.get("featured")
    if cur == "incubating" and featured in (True, "true"):
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.HARD,
            message=(
                "curation: incubating 與 featured: true 互斥"
                "（進化中文章不進精選；首頁精選無另設 filter，靠本條看守）"
            ),
            line=_fm_line(target, "featured"),
            editorial_ref=EDITORIAL_REF,
        )

    lhr = fm.get("lastHumanReview")
    if cur == "verified" and lhr not in (True, "true"):
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=(
                "curation: verified 但 lastHumanReview 不是 true——轉正時兩欄"
                "一起動（dashboard human-reviewed% 讀後者）"
            ),
            line=_fm_line(target, "curation"),
            editorial_ref=EDITORIAL_REF,
        )
