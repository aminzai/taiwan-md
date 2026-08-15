"""link-url-mangle — catch link URLs corrupted by whatever wrote them.

Three patterns. The first two are rooted in one prettier behaviour; the third
comes from the other end of the pipe (generation tools), but the failure shape
is the same: something wrote a link destination that is not what the author
meant, and the damage is invisible in the rendered page.

  HARD — whitespace inside a markdown link destination, e.g.
         `[原民會：噶瑪蘭族](https://www.cip.gov.tw/…?cumid )`. CommonMark
         tolerates it (the link still resolves), so nothing renders wrong and
         no build goes red — but `[^N]: [Title](URL) — desc` no longer matches
         the footnote-format gate, and every affected footnote reports as its
         own "格式不合規範" error. One stray byte per link, hundreds of
         errors, zero signal about the common cause. Normalising is lossless:
         a trailing/leading space is never part of a URL.

  HARD — a markdown link destination contains a literal `*` (e.g.
         `](https://commons.wikimedia.org/wiki/File:…立柱*2025-12-02.jpg)`).
         `*` is never valid in a real URL (it would be `%2A`); its presence
         means prettier rewrote an emphasis `_` into `*`. The link is broken
         (404). Restore the `_` AND de-link the caption (see WARN below).

  WARN — a markdown link to a percent-encoded (CJK) Wikimedia Commons URL whose
         filename ends in `_<digits>` (e.g. `_05.jpg`, `_2025-12-02.jpg`,
         `_13.jpg`) sits INSIDE an italic caption line (`_…_`). This has not
         mangled yet but WILL on the next `prettier --write`: prettier pairs
         the URL's trailing `_NN` with the caption's closing `_` italic
         delimiter and flips the span to `*`. Pure-ASCII Commons URLs are safe
         (CommonMark intraword-underscore rule); only percent-encoded CJK
         filenames trigger it. Mitigation: move the clickable link OUT of the
         `_…_` caption — keep plain-text attribution in the caption, put the
         `[link](url)` in the article's `## 圖片來源` section (not italic, so
         prettier leaves it alone). `<…>` angle-bracket wrapping does NOT help
         inside italic.

Trigger (whitespace): 2026-08-15 twmd-maintainer-am — 24 contributor PRs from
one batch all failed the PR gate. The reported surface was "腳註格式不合規範"
×353 across 16 files; the cause was a single generation artefact putting one
space before every `)`. Fixing it cleared every footnote-format hard failure in
those files without touching a word of prose. Recorded because the shape
recurs: a checker that reports per-instance turns one upstream defect into
hundreds of unrelated-looking errors, and nobody reads the 300th one.

Trigger (prettier): 2026-06-21 cicada-media EVOLVE — a hero caption's Commons URL
(`…翠池_汪大智_05.jpg`) got silently mangled to `*05.jpg` by pre-commit
prettier; a later audit found 13 already-broken files (科技園區發展 /
houtong-cat-village / 沈伯洋 across langs) plus ~49 at-risk. The breakage is
silent (build green, link 404 only on click). LESSONS-INBOX pattern
`prettier-cjk-url-italic-mangle`.
"""

from __future__ import annotations

import re
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation

CHECK_NAME = "link-url-mangle"
DIMENSION = "structure"
DEFAULT_SEVERITY = Severity.HARD
EDITORIAL_REF = "EDITORIAL §媒體編織（caption 不放 CJK-Commons-URL 連結，連結走 §圖片來源）+ REWRITE Step 4.3.6"
APPLIES_TO = ["*"]

# HARD: a markdown image link whose destination contains a literal `*` (mangled).
# `\S*\*\S*` lets the URL include balanced internal parens (houtong `(cropped*2022).jpg`).
_MANGLED = re.compile(r"\]\(<?(https?://\S*\*\S*?)>?\)")

# Whole markdown link, used only after the line has been identified as an
# italic caption. Commons filenames in this failure family encode any literal
# parentheses as %28/%29, so a conservative "up to the next )" is sufficient
# and avoids trying to parse arbitrary Markdown here.
_CAPTION_LINK = re.compile(
    r"\[([^\]\n]+)\]\("
    r"(?:<(https?://[^>\n]+)>|(https?://(?:[^\s()]|\([^()\s]*\))+))"
    r"\)"
)

# HARD: whitespace inside a markdown link destination — `](https://… )` or
# `](  https://…)`. Angle-bracket destinations (`](<url with space>)`) are the
# CommonMark-sanctioned way to carry a literal space, so they are left alone.
# The URL body itself must not contain whitespace: a real space would have to
# be %20, so any bare space here is padding introduced by whatever wrote it.
_URL_WHITESPACE = re.compile(r"\]\((\s*https?://[^)<>]*?\s+)\)")

# WARN at-risk: percent-encoded Commons URL ending in `_<digits>` before the
# image extension, sitting in an italic caption line.
_ATRISK_URL = re.compile(
    r"\]\(<?https?://commons\.wikimedia\.org[^\s)]*%[0-9A-Fa-f]{2}"
    r"[^\s)]*_[0-9][0-9-]*\.(?:jpg|JPG|jpeg|png|webp)>?\)"
)


def _is_italic_caption(line: str) -> bool:
    s = line.strip()
    # Caption convention is usually `_…_`; older hub pages use `*…*`.
    return len(s) >= 2 and (
        (s.startswith("_") and (s.endswith("_") or s.endswith("*") or s.endswith("\\_")))
        or (s.startswith("*") and s.endswith("*"))
    )


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    text = target.text
    if not text:
        return

    for line_no, line in enumerate(text.split("\n"), start=1):
        # HARD — already mangled (`*` in a link URL).
        # Scope to the actual bug mechanism: a literal `*` in a link URL is a
        # prettier-mangle only when the link sits in an italic caption, OR the URL is a
        # wiki(m|p)edia URL (Commons filenames never contain a literal `*` — it'd be
        # %2A). A `*` in a non-wiki footnote query string (1111.com.tw `sa0=50000*`,
        # ly.gov.tw `NO%3DE01961*`) is legitimate — don't false-positive (2026-06-21).
        m = _MANGLED.search(line)
        if m and (
            _is_italic_caption(line)
            or "wikimedia.org" in m.group(1)
            or "wikipedia.org" in m.group(1)
        ):
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.HARD,
                message=(
                    "連結 URL 含 `*`（prettier 把斜體 caption 裡的 `_NN` 弄壞成 `*NN`，連結已 404）："
                    f"…{m.group(1)[-48:]}。修：URL 的 `*` 還原成 `_`，並把連結移出 `_斜體_` caption（連結走 §圖片來源）。"
                ),
                line=line_no,
                snippet=line.strip()[:90],
                editorial_ref=EDITORIAL_REF,
                fix_suggestion=(
                    "caption 留純文字 attribution（`Photo: X / Wikimedia Commons, CC BY-SA 4.0`），"
                    "可點連結放文末 `## 圖片來源`（非斜體，prettier 不動）。`<…>` 在斜體內無效。"
                ),
            )
            continue

        # HARD — stray whitespace inside a link destination. Reported once per
        # line with a count, not once per link: the whole point of this check is
        # that the per-instance view buried the single upstream cause.
        ws_hits = _URL_WHITESPACE.findall(line)
        if ws_hits:
            sample = ws_hits[0].strip()
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.HARD,
                message=(
                    f"連結網址內有多餘空白（本行 {len(ws_hits)} 處）：…{sample[-40:]}⎵)。"
                    "網址裡的空白一定是產生工具留下的，真正的空白會是 %20。"
                    "它不會讓連結壞掉，但會讓 footnote-format 逐條回報「格式不合規範」，"
                    "一個上游缺陷變成幾百個看起來無關的錯誤。修：`--fix` 可自動清掉。"
                ),
                line=line_no,
                snippet=line.strip()[:90],
                editorial_ref=EDITORIAL_REF,
                fix_suggestion=(
                    "跑 `python3 scripts/tools/article-health.py <檔> --fix`；"
                    "若空白是刻意的（極罕見），把網址包進 `<…>` 角括號。"
                ),
            )

        # WARN — at-risk: CJK Commons URL with trailing `_NN` inside an italic caption.
        if _is_italic_caption(line) and _ATRISK_URL.search(line):
            yield Violation(
                check=CHECK_NAME,
                severity=Severity.WARN,
                message=(
                    "斜體 caption 內含 percent-encoded CJK Commons URL 的 `_NN.jpg`，"
                    "下次 prettier 會弄壞成 `*NN`（連結 404）。建議現在就把連結移出 caption。"
                ),
                line=line_no,
                snippet=line.strip()[:90],
                editorial_ref=EDITORIAL_REF,
                fix_suggestion=(
                    "把 `[…](commons-url)` 移到 `## 圖片來源`，caption 只留純文字授權標示。"
                ),
            )


def fix(target: FileTarget, config: dict[str, Any]) -> int:
    """Safely move vulnerable Commons links out of italic captions.

    The transform is deliberately local and lossless:

    - an already mangled Wikimedia/Wikipedia URL gets its literal ``*`` bytes
      restored to ``_``;
    - the caption keeps the attribution as plain text;
    - the exact Markdown link is repeated on a separate, non-italic line
      immediately below it.

    Keeping the link nearby (instead of guessing translated ``圖片來源``
    headings) preserves the source/translation URL multiset and works across
    all eleven languages. The QA gates still run afterwards.
    """
    text = target.path.read_text(encoding="utf-8")
    lines = text.split("\n")
    changes = 0
    healed: list[str] = []

    for line in lines:
        # Strip padding whitespace out of link destinations first, so the
        # caption/mangle transforms below see canonical URLs. Lossless: a real
        # space inside a URL must be percent-encoded, and `<…>` destinations
        # are excluded by the pattern.
        def _tighten(match: re.Match[str]) -> str:
            nonlocal changes
            changes += 1
            return f"]({match.group(1).strip()})"

        line, _ = _URL_WHITESPACE.subn(_tighten, line)

        is_caption = _is_italic_caption(line)
        moved_links: list[str] = []

        def move(match: re.Match[str]) -> str:
            nonlocal changes
            label = match.group(1)
            url = match.group(2) or match.group(3)
            is_wiki = "wikimedia.org" in url or "wikipedia.org" in url
            restored = url.replace("*", "_") if is_wiki else url
            at_risk = bool(
                re.search(
                    r"commons\.wikimedia\.org[^\s)]*%[0-9A-Fa-f]{2}"
                    r"[^\s)]*_[0-9][0-9-]*\.(?:jpg|JPG|jpeg|png|webp)$",
                    restored,
                )
            )
            if not ((is_wiki and "*" in url) or at_risk):
                return match.group(0)
            changes += 1
            if is_caption:
                moved_links.append(f"[{label}]({restored})")
                return label
            # Outside a caption there is no Prettier emphasis ambiguity left:
            # restoring the impossible literal star is sufficient.
            return f"[{label}]({restored})"

        new_line = _CAPTION_LINK.sub(move, line)
        if moved_links:
            # Prettier's broken form leaves the closing delimiter escaped
            # (`.\_`) or flipped (`.*`). Restore the caption wrapper too.
            if not line.strip().startswith("*"):
                new_line = re.sub(r"(?:\\_|\*)\s*$", "_", new_line)
            healed.append(new_line)
            healed.append("")
            healed.extend(moved_links)
        else:
            healed.append(new_line)

    if changes and not config.get("dry_run", False):
        target.path.write_text("\n".join(healed), encoding="utf-8")
    return changes
