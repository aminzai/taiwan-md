"""
test_fetch_cloudflare_crawler_status.py — scripts/tools/fetch-cloudflare.py 單元測試

覆蓋：reports/fortnight-deep-review-2026-09-05.md §2.5 / §4.2 E2「爬蟲成功率把
3xx 搬出失敗欄」。用假 GraphQL 回應（monkeypatch `_cf_graphql_soft`）驗算術，
不打真的 Cloudflare API——沒有憑證的環境也能跑。

驗證重點：
1. 既有欄位（requests / http200 / unsuccessfulRequests）一個字不動。
2. 新欄位 http3xx / http4xx / http5xx 依 edgeResponseStatus 正確分桶。
3. successRateExcl3xx = http200 / (requests - http3xx)，3xx 不計入分母。
4. 分母歸零（全部都是轉址）時 successRateExcl3xx 回 None，不假裝算得出比率。
"""
import importlib.util
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "tools" / "fetch-cloudflare.py"
)
SPEC = importlib.util.spec_from_file_location("fetch_cloudflare", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _row(ua, status, count):
    return {"dimensions": {"userAgent": ua, "edgeResponseStatus": status}, "count": count}


def test_crawler_status_buckets_and_success_rate_excl_3xx(monkeypatch):
    # Googlebot: 10 個 200、5 個 301（轉址，不是失敗）、2 個 404。
    # BingBot: 只有 3 個 301（分母全被轉址吃光 → successRateExcl3xx 該回 None）。
    fake_rows = [
        _row("Mozilla/5.0 (compatible; Googlebot/2.1)", 200, 10),
        _row("Mozilla/5.0 (compatible; Googlebot/2.1)", 301, 5),
        _row("Mozilla/5.0 (compatible; Googlebot/2.1)", 404, 2),
        _row("Mozilla/5.0 (compatible; bingbot/2.0)", 301, 3),
    ]

    def fake_graphql_soft(token, query, variables):
        return {"viewer": {"zones": [{"httpRequestsAdaptiveGroups": fake_rows}]}}, None

    monkeypatch.setattr(MODULE, "_cf_graphql_soft", fake_graphql_soft)

    result = MODULE.fetch_ai_crawlers("fake-token", "fake-zone", days=1)
    assert result is not None

    crawlers = {c["name"]: c for c in result["crawlers"]}

    google = crawlers["Googlebot"]
    # 既有欄位不動
    assert google["requests"] == 17
    assert google["http200"] == 10
    # 新欄位分桶正確
    assert google["http3xx"] == 5
    assert google["http4xx"] == 2
    assert google["http5xx"] == 0
    # successRateExcl3xx = 10 / (17 - 5) * 100 = 83.3
    assert google["successRateExcl3xx"] == 83.3

    bing = crawlers["BingBot"]
    assert bing["requests"] == 3
    assert bing["http200"] == 0
    assert bing["http3xx"] == 3
    # 分母 (3 - 3) = 0 → 不假裝算得出比率
    assert bing["successRateExcl3xx"] is None

    totals = result["totals"]
    # 既有欄位一個字不動：unsuccessfulRequests 仍是 requests - http200（含 3xx）
    assert totals["detectedRequests"] == 20
    assert totals["http200"] == 10
    assert totals["unsuccessfulRequests"] == 10
    # 新欄位：3xx/4xx/5xx 加總 + 排除 3xx 後的成功率
    assert totals["http3xx"] == 8
    assert totals["http4xx"] == 2
    assert totals["http5xx"] == 0
    # 10 / (20 - 8) * 100 = 83.3
    assert totals["successRateExcl3xx"] == 83.3
