"""輪中補貨（topup_queue）：worker 在本輪佇列空手時向 backlog 補它接得了的語言。

2026-09-21 run 33830：三個切軌跳過 pt/ru 的地端 worker 22:30 吃完份額後直接退出，
三張 GPU 空等雲端 worker 磨 32 篇 pt/ru 尾巴 3–5 小時；每一輪的尾巴都長這樣。
"""
import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace


MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "babel-dispatch.py"
)
SPEC = importlib.util.spec_from_file_location("babel_dispatch", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules["babel_dispatch"] = MODULE   # @dataclass 解析 annotation 時要在 sys.modules 找得到
SPEC.loader.exec_module(MODULE)


def _stub_pipeline(monkeypatch, backlog: dict, tmp_path):
    """backlog: lang -> [zh_path, ...]（build_worklist 的回傳）。prepare-batch 與
    group 收集用假的：每篇一個 group 檔路徑。"""
    monkeypatch.setattr(MODULE, "refresh_status", lambda log: {})
    monkeypatch.setattr(
        MODULE, "build_worklist",
        lambda status_data, lang, priority, order, **kw: list(backlog.get(lang, [])),
    )
    calls = []

    def fake_prepare(lang, zh_paths, slug_map_path, round_dir, log):
        calls.append((lang, list(zh_paths), round_dir))

    monkeypatch.setattr(MODULE, "run_prepare_batch", fake_prepare)
    monkeypatch.setattr(
        MODULE, "collect_and_filter_groups",
        lambda round_dir, lang, seen, log: [
            (lang, round_dir / f"_group-{i}.json", zh)
            for i, zh in enumerate(next(z for l, z, rd in calls if rd == round_dir))
        ],
    )
    return calls


def _worker(label, skip=(), tier="normal"):
    return SimpleNamespace(label=label, skip_langs=frozenset(skip), tier=tier)


def _args():
    return SimpleNamespace(priority="all", order="forward", max_zh_bytes=None)


def test_topup_refills_only_eligible_langs_and_skips_round_seen(monkeypatch, tmp_path):
    backlog = {"ja": ["A.md", "B.md", "C.md"], "pt": ["P.md"], "ru": ["R.md"]}
    calls = _stub_pipeline(monkeypatch, backlog, tmp_path)
    state = MODULE.RunState()
    state.round_seen = {"ja:A.md"}          # 本輪已排過，不重排
    state.in_flight = {"ja:B.md"}           # 別的 worker 正在做，不重排
    queue = MODULE.TaskQueue([])
    logs = []
    w = _worker("gemma", skip=("pt", "ru"))

    ok = MODULE.topup_queue(w, queue, state, ["ja", "pt", "ru"], _args(), tmp_path, 1,
                            tmp_path / "slug.json", set(), logs.append)

    assert ok is True
    assert [c[0] for c in calls] == ["ja"]            # pt/ru 是它跳過的語言，不補
    assert calls[0][1] == ["C.md"]                    # A 已排過、B 在途，只剩 C
    assert len(queue) == 1
    assert "ja:C.md" in state.round_seen
    assert calls[0][2].name == "round01-topup01"
    assert any("top-up #1" in l for l in logs)


def test_topup_returns_false_when_backlog_has_nothing_for_this_worker(monkeypatch, tmp_path):
    calls = _stub_pipeline(monkeypatch, {"pt": ["P.md"]}, tmp_path)
    state = MODULE.RunState()
    queue = MODULE.TaskQueue([])
    logs = []
    w = _worker("gemma", skip=("pt", "ru"))

    ok = MODULE.topup_queue(w, queue, state, ["ja", "pt"], _args(), tmp_path, 3,
                            tmp_path / "slug.json", set(), logs.append)

    assert ok is False and len(queue) == 0 and calls == []
    assert any("退出等輪次結束" in l for l in logs)


def test_topup_skips_restricted_tier_workers(monkeypatch, tmp_path):
    _stub_pipeline(monkeypatch, {"ja": ["A.md"]}, tmp_path)
    state = MODULE.RunState()
    queue = MODULE.TaskQueue([])
    w = _worker("haiku", tier="tier6")

    assert MODULE.topup_queue(w, queue, state, ["ja"], _args(), tmp_path, 1,
                              tmp_path / "slug.json", set(), lambda m: None) is False
    assert len(queue) == 0


def test_taskqueue_extend_is_claimable():
    queue = MODULE.TaskQueue([])
    queue.extend([("ja", Path("g.json"), "A.md")])
    assert queue.claim("w", {}) == ("ja", Path("g.json"), "A.md")
    assert queue.claim("w", {}) is None
