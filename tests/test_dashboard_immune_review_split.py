"""
test_dashboard_immune_review_split.py — scripts/core/generate-dashboard-immune.py 單元測試

覆蓋：reports/fortnight-deep-review-2026-09-05.md §2.5 / §4.2 E3「review_coverage
拆兩格」。純算術測試（假 article dict，不碰真的 knowledge/ 或 git），確認：

1. stock（30 天前）／new30d（近 30 天）依 frontmatter `date` 正確分桶。
2. 沒有 frontmatter `date` 時退回 `_get_article_date` 的 git fallback
   （這裡用 monkeypatch 頂掉 `_git_first_commit_date`，不真的跑 git）。
3. `compute_review_coverage`（既有 tier-weighted 分數/breakdown）完全不受
   這支新函式影響——同一組 articles 餵下去，score 與 tierBreakdown 不變。
"""
import importlib.util
from datetime import datetime, timedelta
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "core"
    / "generate-dashboard-immune.py"
)
SPEC = importlib.util.spec_from_file_location("generate_dashboard_immune", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _article(path, category, date_str, reviewed):
    return {
        "path": path,
        "category": category,
        "slug": Path(path).stem,
        "lastHumanReview": reviewed,
        "frontmatter": {"date": date_str} if date_str else {},
    }


def test_stock_vs_new30d_split_by_frontmatter_date():
    now = datetime(2026, 9, 5)
    articles = [
        # 舊文（60 天前），一篇審過一篇沒審
        _article("knowledge/History/old-reviewed.md", "History", "2026-07-07", True),
        _article("knowledge/History/old-unreviewed.md", "History", "2026-07-07", False),
        # 近 30 天新增，兩篇都沒審
        _article("knowledge/Society/new-1.md", "Society", "2026-08-20", False),
        _article("knowledge/Society/new-2.md", "Society", "2026-09-01", False),
    ]

    split = MODULE.compute_review_coverage_split(articles, now=now)

    assert split["stock"] == {"total": 2, "reviewed": 1, "pct": 50.0}
    assert split["new30d"] == {"total": 2, "reviewed": 0, "pct": 0.0}


def test_missing_frontmatter_date_falls_back_to_git_first_commit(monkeypatch):
    now = datetime(2026, 9, 5)
    # 沒有 frontmatter date 的文章，git 首次 commit 落在 40 天前 → 算存量。
    monkeypatch.setattr(
        MODULE, "_git_first_commit_date", lambda rel_path: now - timedelta(days=40)
    )
    articles = [_article("knowledge/History/no-date.md", "History", None, True)]

    split = MODULE.compute_review_coverage_split(articles, now=now)

    assert split["stock"] == {"total": 1, "reviewed": 1, "pct": 100.0}
    assert split["new30d"] == {"total": 0, "reviewed": 0, "pct": 0}


def test_split_does_not_change_existing_tier_weighted_score_and_breakdown():
    articles = [
        _article("knowledge/Politics/a.md", "Politics", "2026-01-01", True),
        _article("knowledge/Food/b.md", "Food", "2026-01-01", False),
    ]

    # compute_review_coverage 是既有公式；跑兩次（split 呼叫前後）結果必須一致，
    # 證明 E3 沒有動到 review_score / tierBreakdown 半個字。
    score_before, breakdown_before = MODULE.compute_review_coverage(articles)
    MODULE.compute_review_coverage_split(articles, now=datetime(2026, 9, 5))
    score_after, breakdown_after = MODULE.compute_review_coverage(articles)

    assert score_before == score_after
    assert breakdown_before == breakdown_after
