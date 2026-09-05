"""
test_observer_presence.py — scripts/tools/observer-presence.py 單元測試

覆蓋：ROUTINE.md 排程表機械解析（含 fail-loud）、兩個 presence 訊號各自的
過濾規則、present/ABSENT 7 天邊界（6 天仍 present、7 天已 ABSENT）。
全部用假資料（tmp_path 假 repo 樹 + monkeypatch 假 git log 輸出），不碰真實
repo 的 ROUTINE.md / memory/。
"""
import importlib.util
import shutil
from datetime import date, timedelta
from pathlib import Path

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "tools"
    / "observer-presence.py"
)
SPEC = importlib.util.spec_from_file_location("observer_presence", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


ROUTINE_TABLE = """## 核心 routine 排程表（enabled 條數以本表為準）

| TaskId | Title | Cron | Skill | Model | Cadence |
| --- | --- | --- | --- | --- | --- |
| `twmd-rewrite-daily` | TWMD rewrite | `0 19 * * *` | `/twmd-rewrite` | Opus | daily |
| `twmd-weekly-report-sun` | TWMD weekly | `0 2 * * 0` | `/twmd-weekly-report` | Opus | weekly |

## 每週行程表（不相干內容，確保 anchor 有正確止錨）

不該被解析進來的一列：`twmd-should-not-appear`
"""


def setup_repo(tmp_path, monkeypatch, routine_text=ROUTINE_TABLE):
    routine_md = tmp_path / "ROUTINE.md"
    routine_md.write_text(routine_text, encoding="utf-8")
    memory_dir = tmp_path / "memory"
    memory_dir.mkdir()
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    monkeypatch.setattr(MODULE, "ROUTINE_MD", routine_md)
    monkeypatch.setattr(MODULE, "MEMORY_DIR", memory_dir)
    return routine_md, memory_dir


def write_memory(memory_dir, date_str, time_str, handle):
    (memory_dir / f"{date_str}-{time_str}-{handle}.md").write_text("x", encoding="utf-8")


def fake_git_run(lines):
    """monkeypatch 用的 subprocess.run 替身：回傳固定 git log stdout。"""

    class FakeCompleted:
        def __init__(self, stdout):
            self.stdout = stdout
            self.returncode = 0

    def _run(cmd, **kwargs):  # noqa: ARG001 — 簽名對齊真 subprocess.run 呼叫方式
        return FakeCompleted("\n".join(lines))

    return _run


# ---------------------------------------------------------------- load_routine_handles

def test_load_routine_handles_parses_table_and_stops_at_next_heading(tmp_path, monkeypatch):
    setup_repo(tmp_path, monkeypatch)
    handles = MODULE.load_routine_handles()
    assert "twmd-rewrite-daily" in handles
    assert "twmd-weekly-report-sun" in handles
    assert "twmd-maintainer-am" in handles  # ROUTINE.md 註¹別名，明列進集合
    assert "twmd-should-not-appear" not in handles  # 下一個 ## 標題之後不解析


def test_load_routine_handles_missing_file_fails_loud(tmp_path, monkeypatch):
    setup_repo(tmp_path, monkeypatch)
    (tmp_path / "ROUTINE.md").unlink()
    with pytest.raises(SystemExit) as exc:
        MODULE.load_routine_handles()
    assert exc.value.code == 2


def test_load_routine_handles_missing_heading_fails_loud(tmp_path, monkeypatch):
    setup_repo(tmp_path, monkeypatch, routine_text="# 沒有排程表標題\n\n內容\n")
    with pytest.raises(SystemExit) as exc:
        MODULE.load_routine_handles()
    assert exc.value.code == 2


# ---------------------------------------------------------------- signal_memory

def test_signal_memory_ignores_routine_prefix_and_explicit_alias(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    write_memory(memory_dir, "2026-08-01", "060000", "twmd-data-refresh-am")
    write_memory(memory_dir, "2026-08-15", "090108", "twmd-maintainer-am")  # 別名，仍算 routine
    write_memory(memory_dir, "2026-08-10", "153608", "manual-login-restore")
    handles = MODULE.load_routine_handles()
    d, handle = MODULE.signal_memory(handles)
    assert d == "2026-08-10"
    assert handle == "manual-login-restore"


def test_signal_memory_missing_dir_fails_loud(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    shutil.rmtree(memory_dir)
    with pytest.raises(SystemExit) as exc:
        MODULE.signal_memory({"twmd-rewrite-daily"})
    assert exc.value.code == 2


def test_signal_memory_no_non_routine_files_returns_none(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    write_memory(memory_dir, "2026-08-01", "060000", "twmd-data-refresh-am")
    handles = MODULE.load_routine_handles()
    d, handle = MODULE.signal_memory(handles)
    assert d is None
    assert handle is None


# ---------------------------------------------------------------- signal_git

def test_signal_git_filters_semiont_prefix_and_merges(tmp_path, monkeypatch):
    setup_repo(tmp_path, monkeypatch)
    lines = [
        "aaa1111\x1fChe-Yu Wu\x1f2026-08-20\x1f\U0001f9ec [routine] memory: xyz",
        "bbb2222\x1fChe-Yu Wu\x1f2026-08-25\x1f\U0001f3a8 brand: 品牌資產第一次建制",
        "ccc3333\x1fChe-Yu Wu\x1f2026-08-27\x1fMerge pull request #1 from foo/bar",
        "ddd4444\x1fidlccp1984\x1f2026-08-28\x1fCreate 某篇.md",
    ]
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run(lines))
    d, h, subject = MODULE.signal_git(60)
    assert d == "2026-08-25"
    assert h == "bbb2222"
    assert "brand" in subject


def test_signal_git_excludes_merge_branch_and_non_owner_author(tmp_path, monkeypatch):
    setup_repo(tmp_path, monkeypatch)
    lines = [
        "aaa1111\x1fChe-Yu Wu\x1f2026-08-20\x1f\U0001f9ec [routine] memory: xyz",
        "ccc3333\x1fChe-Yu Wu\x1f2026-08-27\x1fMerge branch 'main' into feature",
        "ddd4444\x1ffrank890417\x1f2026-08-29\x1f手動 commit 但作者名未走 mailmap",
    ]
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run(lines))
    d, h, subject = MODULE.signal_git(60)
    assert d is None and h is None and subject is None


# ---------------------------------------------------------------- build（present/ABSENT 7 天邊界）

def test_build_present_at_6_days(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    six_days_ago = (date.today() - timedelta(days=6)).isoformat()
    write_memory(memory_dir, six_days_ago, "101010", "manual-check")
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run([]))
    result = MODULE.build(60)
    assert result["mode"] == "present"
    assert result["days_absent"] == 6
    assert result["last_present_date"] == six_days_ago
    assert result["threshold_days"] == 7


def test_build_absent_at_7_days(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    seven_days_ago = (date.today() - timedelta(days=7)).isoformat()
    write_memory(memory_dir, seven_days_ago, "101010", "manual-check")
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run([]))
    result = MODULE.build(60)
    assert result["mode"] == "ABSENT"
    assert result["days_absent"] == 7


def test_build_takes_max_of_two_signals(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    ten_days_ago = (date.today() - timedelta(days=10)).isoformat()
    write_memory(memory_dir, ten_days_ago, "101010", "old-manual-session")
    three_days_ago = (date.today() - timedelta(days=3)).isoformat()
    monkeypatch.setattr(
        MODULE.subprocess, "run",
        fake_git_run([f"aaa1111\x1fChe-Yu Wu\x1f{three_days_ago}\x1f✨ fix: 手動小修"]),
    )
    result = MODULE.build(60)
    assert result["last_present_date"] == three_days_ago
    assert result["days_absent"] == 3
    assert result["mode"] == "present"


def test_build_no_signal_at_all_is_absent(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    write_memory(memory_dir, "2020-01-01", "000000", "twmd-data-refresh-am")  # 全 routine
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run([]))
    result = MODULE.build(60)
    assert result["mode"] == "ABSENT"
    assert result["last_present_date"] is None
    assert result["days_absent"] is None


# ---------------------------------------------------------------- render_human

def test_render_human_present_has_no_protocol_wording(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    write_memory(memory_dir, date.today().isoformat(), "101010", "manual-check")
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run([]))
    line = MODULE.render_human(MODULE.build(60))
    assert "mode=present" in line
    assert "缺席協議" not in line


def test_render_human_absent_mentions_protocol_and_day_count(tmp_path, monkeypatch):
    _, memory_dir = setup_repo(tmp_path, monkeypatch)
    nine_days_ago = (date.today() - timedelta(days=9)).isoformat()
    write_memory(memory_dir, nine_days_ago, "101010", "manual-check")
    monkeypatch.setattr(MODULE.subprocess, "run", fake_git_run([]))
    line = MODULE.render_human(MODULE.build(60))
    assert "ABSENT" in line
    assert "缺席協議生效" in line
    assert "9 天" in line
