"""footnote_density — citation density grading (A-F).

Migrated from `scripts/tools/footnote-scan.sh` grade calculation.

Grade rules (matches shell):
  A: ≥3 footnotes AND density ≤300 (1 fn per ≤300 words)
  B: ≥1 footnote (lower density / count)
  C: ≥3 URLs (no formal footnotes but has external sources)
  D: ≥1 URL  (minimal sourcing)
  F: zero footnotes, zero URLs (citation desert)

Severity: WARN (informational health metric, not block-grade).
For PR-level enforcement use prose_health's citation-desert check.

2026-09-20 (semiont-heartbeat 巡邏第十六、十七篇): a "參考資料" list whose
definitions are never referenced from the body used to grade A/B — the
grade counted definitions, not citations (REFLEXES #82 proxy signal:
existence ≠ effect). Two Geography drafts carried 6-7 defs with zero
inline `[^N]` and graded B. Now: zero body references → WARN and the grade
is downgraded to C; ≥3 defined-but-unreferenced → INFO with the ids.
Calibration on 2026-09-20 zh corpus: 968 articles with defs, 7 with zero
body refs (6 of them `lastHumanReview: false`), 260 partially unreferenced.
"""

from __future__ import annotations
import re
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation


CHECK_NAME = "footnote-density"
DIMENSION = "citation"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "EDITORIAL.md §引用密度 A-F grading"
APPLIES_TO = ["*"]

_RE_DEF = re.compile(r"^\[\^[0-9a-zA-Z_-]+\]:", re.MULTILINE)
_RE_DEF_ID = re.compile(r"^\[\^([0-9a-zA-Z_-]+)\]:", re.MULTILINE)
_RE_REF_ID = re.compile(r"\[\^([0-9a-zA-Z_-]+)\](?!:)")


def _unreferenced(body: str) -> tuple[list[str], int]:
    """Return (defined-but-never-referenced ids, number of referenced defs)."""
    defs = _RE_DEF_ID.findall(body)
    if not defs:
        return [], 0
    prose = "\n".join(l for l in body.split("\n") if not _RE_DEF_ID.match(l))
    refs = set(_RE_REF_ID.findall(prose))
    unref = [d for d in defs if d not in refs]
    return unref, len(defs) - len(unref)


def _word_count(body: str) -> int:
    return len(body.split())


def _grade(fn_count: int, url_count: int, density: int | None) -> str:
    if fn_count >= 3 and density is not None and density <= 300:
        return "A"
    if fn_count >= 1:
        return "B"
    if url_count >= 3:
        return "C"
    if url_count >= 1:
        return "D"
    return "F"


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    body = target.body
    fn_count = len(_RE_DEF.findall(body))
    url_count = body.count("http")
    words = _word_count(body)
    density = words // fn_count if fn_count > 0 else None
    grade = _grade(fn_count, url_count, density)

    unref, referenced = _unreferenced(body)
    if fn_count > 0 and referenced == 0:
        # A reference list nobody points at is not citation. Grade honestly.
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.WARN,
            message=(
                f"腳註 {fn_count} 條定義但正文零 `[^N]` 引用——這是參考清單不是引用，"
                f"等級 {grade}→C（把每條腳註掛回它支撐的那一句）"
            ),
            editorial_ref=EDITORIAL_REF,
            fix_suggestion="C",
        )
        return
    if len(unref) >= 3:
        yield Violation(
            check=CHECK_NAME,
            severity=Severity.INFO,
            message=(
                f"腳註 {len(unref)}/{fn_count} 條定義但正文沒引用：[^{']、[^'.join(unref[:6])}]"
                f"{'…' if len(unref) > 6 else ''}"
            ),
            editorial_ref=EDITORIAL_REF,
        )

    if grade in ("A", "B"):
        return  # healthy — no violation

    if grade == "C":
        msg = f"腳註等級 C：無正式腳註但有 {url_count} 個 inline URL"
    elif grade == "D":
        msg = f"腳註等級 D：僅 {url_count} 個 URL，無正式腳註"
    else:  # F
        msg = "腳註等級 F：引用荒漠（零腳註、零 URL）"

    yield Violation(
        check=CHECK_NAME,
        severity=DEFAULT_SEVERITY,
        message=msg,
        editorial_ref=EDITORIAL_REF,
        fix_suggestion=grade,  # surfaces grade letter for dashboard JSON
    )
