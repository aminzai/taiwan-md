"""tests/test_budget_pace.py — budget-pace.py 的判讀邊界。

回放 2026-09-30 那一週：重置在週三 20:00（UTC 12:00），10-04 01:00 左右撞到 100%，
相當於重置後第 77 小時用完。照線性燒法，工具應該從第 12 小時起就判 lean。
"""

from __future__ import annotations

import datetime as dt
import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("budget_pace", REPO / "scripts/tools/budget-pace.py")
M = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(M)

RESET = dt.datetime(2026, 10, 7, 12, tzinfo=dt.timezone.utc)
WEEK_START = RESET - dt.timedelta(days=7)


def at(hours):
    return WEEK_START + dt.timedelta(hours=hours)


def test_early_week_no_extrapolation():
    r = M.assess(1, RESET, at(0.5))
    assert r["verdict"] == "normal" and r["projected_at_reset_pct"] is None


def test_early_week_absolute_threshold():
    assert M.assess(20, RESET, at(6))["verdict"] == "lean"


def test_last_week_burn_flags_lean_from_hour_12():
    for h in (12, 24, 48, 60):
        used = round(100 * h / 77)
        assert M.assess(used, RESET, at(h))["verdict"] == "lean", h


def test_sustainable_pace_is_normal():
    r = M.assess(40, RESET, at(72))
    assert r["verdict"] == "normal" and r["projected_at_reset_pct"] < 100


def test_reserve_line():
    assert M.assess(85, RESET, at(150))["verdict"] == "reserve"
    assert M.assess(84, RESET, at(160))["verdict"] == "normal"


def test_cli_exit_codes(capsys):
    assert M.main(["--used", "1", "--resets-at", "2026-10-14T12:00:00Z", "--now", "2026-10-07T13:00:00Z"]) == 0
    assert M.main(["--used", "60", "--resets-at", "2026-10-14T12:00:00Z", "--now", "2026-10-09T12:00:00Z"]) == 1
    assert M.main(["--used", "90", "--resets-at", "2026-10-14T12:00:00Z", "--now", "2026-10-09T12:00:00Z"]) == 2
    assert "lean" in capsys.readouterr().out
