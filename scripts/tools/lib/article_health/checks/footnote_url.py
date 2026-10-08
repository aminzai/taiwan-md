"""footnote_url — verify footnote URL reachability via HEAD.

Migrated from `scripts/tools/check-footnote-urls.sh`.

**Network-bound — disabled by default.** Enable per-run via:
  python3 scripts/tools/article-health.py file.md --check=footnote-url
  ARTICLE_HEALTH_NETWORK=1 python3 ...  (env var)
  options.network=true (config)

Reason: blind HEAD on every commit slows pre-commit by 10-30s and
fails on flaky links. Best run as Stage 3.5 manual check or scheduled
cron sweep, not as gate.

Severity: WARN by default. 4xx/5xx surface as warnings (won't block PR).
"""

from __future__ import annotations
import os
import re
from typing import Any, Iterator

from ..types import FileTarget, Severity, Violation


CHECK_NAME = "footnote-url"
DIMENSION = "citation"
DEFAULT_SEVERITY = Severity.WARN
EDITORIAL_REF = "FACTCHECK-PIPELINE Phase 3 SOURCE AUTHORITY"
APPLIES_TO = ["*"]

_RE_FOOTNOTE_URL = re.compile(
    r"^\[\^[0-9a-zA-Z_-]+\]:\s*\[[^\]]+\]\((https?://[^)\s]+)\)",
    re.MULTILINE,
)

# 參考資料區寫成普通清單、沒有 [^N] 腳註的文章，上面那條正則一個網址都抓不到，
# 結果是「hard=0 warn=0」看起來像全部活著（2026-10-08 心跳：〈台灣官方網站資源〉
# 參考資料 5 條、1 條 404，本檢查回報全綠；當時全庫 116 篇 zh 文章、895 個網址在這個盲區）。
# 參考資料區的判定式沿用 format_structure / body_internal_links 的 `^##\s*參考資料`。
_RE_REFERENCES_H2 = re.compile(r"^##\s*參考資料", re.MULTILINE)
_RE_NEXT_H2 = re.compile(r"^##\s", re.MULTILINE)
_RE_LIST_URL = re.compile(
    r"^\s*[-*]\s*\[[^\]]+\]\((https?://[^)\s]+)\)",
    re.MULTILINE,
)


def _reference_list_urls(body: str) -> Iterator[tuple[int, str]]:
    """參考資料區裡清單項目的網址（腳註定義不在此列，交給 _RE_FOOTNOTE_URL）。"""
    m = _RE_REFERENCES_H2.search(body)
    if not m:
        return
    start = m.end()
    nxt = _RE_NEXT_H2.search(body, start)
    end = nxt.start() if nxt else len(body)
    for lm in _RE_LIST_URL.finditer(body, start, end):
        yield lm.start(1), lm.group(1)


def _network_enabled(config: dict[str, Any]) -> bool:
    if os.environ.get("ARTICLE_HEALTH_NETWORK") == "1":
        return True
    return bool(config.get("network", False))


# 不帶瀏覽器標頭時，iThome、中央社、數發部等站對 urllib 預設 User-Agent 一律回 403，
# 而同一批網址用瀏覽器開都是 200（2026-10-08 心跳實測 7/7）。擋爬蟲跟真的死掉混在同一個
# warn 裡，警告就沒人信了（REFLEXES #38）。仍然 403 的多半是 WAF，判讀前先用瀏覽器開一次。
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}


def _ssl_context():
    # Python 3.13 起預設 VERIFY_X509_STRICT，TWCA 簽的政府網站憑證（tasa／nstc／law.moj／
    # president）會被拒成「Missing Subject Key Identifier」，瀏覽器照常開得了。
    # 只放寬這一旗標，憑證鏈與主機名驗證照舊。
    import ssl

    ctx = ssl.create_default_context()
    if hasattr(ssl, "VERIFY_X509_STRICT"):
        ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT
    return ctx


def _encode(url: str) -> str:
    # 中文路徑（zh.wikipedia.org/wiki/台灣…）不編碼，urllib 直接拋 ascii codec 錯，
    # 被記成「無法存取」。已編碼的 % 保留，不會二次編碼。
    from urllib.parse import quote

    return quote(url, safe=":/?#[]@!$&'()*+,;=%~")


def _check_url(url: str, timeout: float = 5.0) -> tuple[bool, int | None, str]:
    """Returns (ok, status_code, message). ok = True if 2xx/3xx."""
    url = _encode(url)
    ctx = _ssl_context()
    try:
        import urllib.request
        import urllib.error

        req = urllib.request.Request(url, method="HEAD", headers=_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            status = resp.status
            return (200 <= status < 400, status, "")
    except urllib.error.HTTPError as e:
        # Some servers reject HEAD; retry GET with a small range
        try:
            req2 = urllib.request.Request(url, method="GET", headers=_HEADERS)
            req2.add_header("Range", "bytes=0-0")
            with urllib.request.urlopen(req2, timeout=timeout, context=ctx) as resp:
                status = resp.status
                return (200 <= status < 400, status, "")
        except Exception as e2:
            return (False, getattr(e, "code", None), f"{e}; retry: {e2}")
    except urllib.error.URLError as e:
        return (False, None, f"URLError: {e.reason}")
    except Exception as e:
        return (False, None, str(e))


def check(target: FileTarget, config: dict[str, Any]) -> Iterator[Violation]:
    if not _network_enabled(config):
        return

    body = target.body
    candidates = [("腳註", m.start(), m.group(1)) for m in _RE_FOOTNOTE_URL.finditer(body)]
    candidates += [("參考資料", pos, url) for pos, url in _reference_list_urls(body)]
    seen: set[str] = set()
    for kind, pos, raw in candidates:
        url = raw.rstrip(",;:.")  # trim common trailing punct
        if url in seen:
            continue
        seen.add(url)
        line = body.count("\n", 0, pos) + 1
        ok, status, msg = _check_url(url)
        if ok:
            continue
        status_str = f"HTTP {status}" if status else (msg or "no response")
        yield Violation(
            check=CHECK_NAME,
            severity=DEFAULT_SEVERITY,
            message=f"{kind} URL 無法存取 ({status_str}): {url[:80]}",
            line=line,
            snippet=url,
            editorial_ref=EDITORIAL_REF,
        )
