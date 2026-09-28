"""select_top_paths 的家族保障 — 全域榜排「最吵的」，重導要的是「修得掉的」。

誕生 2026-09-28 twmd-maintainer-am：`top_paths` 原本是純全域 top-300，而下游
`generate-redirects.mjs` 只吃 slug-variant / cross-lang-slug / renamed-or-truncated
三族。一支被改名文章的舊網址典型只有 1-2 次命中，於是永遠擠不進全域榜。
當天實測 latest.json：切線落在 2 hits，slug-variant 全家 84 hits 只有 5 hits／2 條
進榜，renamed-or-truncated（12 hits）與 cross-lang-slug（1 hit）整族缺席。
"""

import importlib.util
import pathlib

import pytest

REPO = pathlib.Path(__file__).resolve().parents[1]


def _load_module():
    """monitor-404.py 檔名帶連字號，不能 import，用 spec 載入。"""
    path = REPO / "scripts/tools/monitor-404.py"
    spec = importlib.util.spec_from_file_location("monitor_404", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def mod():
    return _load_module()


def _agg(hits, family, suggest=""):
    return {"hits": hits, "family": family, "suggest": suggest, "ua_counts": {"ua": hits}}


def _build_realistic(mod):
    """複製 2026-09-28 的病理分佈：兩個吵家族淹掉全域榜，三個可修家族全在尾巴。"""
    path_agg = {}
    # 吵：足以自己填滿整個全域 top-N
    for i in range(mod.TOP_PATHS_LIMIT + 200):
        path_agg[f"/scanner/{i}"] = _agg(50, "scanner")
    for i in range(300):
        path_agg[f"/unknown/{i}"] = _agg(30, "unknown")
    # 可修但安靜：每條只有 1 次命中，純全域榜一條都留不下
    for i in range(84):
        path_agg[f"/slug-variant/{i}"] = _agg(1, "slug-variant", suggest=f"/fixed/{i}")
    for i in range(12):
        path_agg[f"/renamed/{i}"] = _agg(1, "renamed-or-truncated", suggest=f"/new/{i}")
    path_agg["/cross-lang/0"] = _agg(1, "cross-lang-slug", suggest="/ja/ok")
    return path_agg


def test_quiet_fixable_families_survive(mod):
    """三個可修家族必須進榜，且各自拿到 min(家族條數, PER_FAMILY_LIMIT)。"""
    out = mod.select_top_paths(_build_realistic(mod))
    counts = {}
    for e in out:
        counts[e["family"]] = counts.get(e["family"], 0) + 1

    assert counts.get("slug-variant") == mod.PER_FAMILY_LIMIT  # 84 條 → 取前 50
    assert counts.get("renamed-or-truncated") == 12  # 少於上限 → 全收
    assert counts.get("cross-lang-slug") == 1


def test_regression_pure_global_ranking_would_drop_them(mod):
    """反證：同一份資料在純全域 top-N 下，三個可修家族一條都不會留下。"""
    path_agg = _build_realistic(mod)
    ranked = sorted(path_agg.items(), key=lambda kv: kv[1]["hits"], reverse=True)
    global_only = {a["family"] for _, a in ranked[: mod.TOP_PATHS_LIMIT]}
    for fam in ("slug-variant", "renamed-or-truncated", "cross-lang-slug"):
        assert fam not in global_only, f"fixture 沒有重現病理：{fam} 本來就進得去全域榜"


def test_global_top_n_still_fully_present(mod):
    """家族保障是「加進來」，不能排擠既有全域榜的任何一條。"""
    path_agg = _build_realistic(mod)
    ranked = sorted(path_agg.items(), key=lambda kv: kv[1]["hits"], reverse=True)
    expected = {p for p, _ in ranked[: mod.TOP_PATHS_LIMIT]}
    got = {e["path"] for e in mod.select_top_paths(path_agg)}
    assert expected <= got


def test_output_sorted_desc_and_unique(mod):
    """下游與報表都依賴 hits 遞減排序；聯集不得產生重複路徑。"""
    out = mod.select_top_paths(_build_realistic(mod))
    hits = [e["hits"] for e in out]
    assert hits == sorted(hits, reverse=True)
    paths = [e["path"] for e in out]
    assert len(paths) == len(set(paths))


def test_empty_input(mod):
    assert mod.select_top_paths({}) == []


def test_missing_ua_counts_does_not_crash(mod):
    """ua_counts 缺席或空白時取空字串，不要炸掉整天的處理。"""
    out = mod.select_top_paths(
        {
            "/a": {"hits": 3, "family": "unknown", "suggest": ""},
            "/b": {"hits": 2, "family": "unknown", "suggest": "", "ua_counts": {}},
        }
    )
    assert [e["ua"] for e in out] == ["", ""]
