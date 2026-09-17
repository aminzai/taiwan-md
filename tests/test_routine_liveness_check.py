"""tests/test_routine_liveness_check.py — routine-liveness-check.py 的 fire-vs-commit 對賬測試。

守的是 2026-09-17 maintainer-am 修的那個洞：本機 main 與 origin 真分岔期間，routine 在
origin/main worktree 上跑完、memory 只進 origin，本工具只掃本機 `git log` 便回報
「零 git 痕跡」→ 沉默死亡黃燈掛一整天（09-16 maintainer 真實案例，`a15603762` 只在 origin）。
每個測試建真的 git repo（同 test_routine_stall_check.py 的做法），不 mock subprocess，
因為「哪個 ref 被掃到」本身就是待測邏輯。
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

REPO_ROOT_REAL = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT_REAL / "scripts" / "tools" / "routine-liveness-check.py"
SPEC = importlib.util.spec_from_file_location("routine_liveness_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _run(cmd, cwd, env=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env, check=True)


def init_git_repo(path: Path) -> None:
    _run(["git", "init", "-q", "-b", "main"], cwd=path)
    _run(["git", "config", "user.email", "test@example.com"], cwd=path)
    _run(["git", "config", "user.name", "Test"], cwd=path)


def commit_at(path: Path, subject: str, when: datetime, memory_file: str | None = None) -> None:
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = when.isoformat()
    env["GIT_COMMITTER_DATE"] = when.isoformat()
    if memory_file:
        mem = path / "docs" / "semiont" / "memory"
        mem.mkdir(parents=True, exist_ok=True)
        (mem / memory_file).write_text("# fixture\n", encoding="utf-8")
        _run(["git", "add", "-A"], cwd=path)
        _run(["git", "commit", "-q", "-m", subject], cwd=path, env=env)
    else:
        _run(["git", "commit", "-q", "--allow-empty", "-m", subject], cwd=path, env=env)


def write_live_state(path: Path, task_id: str, fired_at: datetime) -> None:
    data = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "tasks": [{"taskId": task_id, "enabled": True, "lastRunAt": fired_at.isoformat().replace("+00:00", "Z")}],
    }
    (path / "docs" / "semiont").mkdir(parents=True, exist_ok=True)
    (path / "docs" / "semiont" / "routine-live-state.json").write_text(
        json.dumps(data, ensure_ascii=False), encoding="utf-8"
    )


@pytest.fixture
def repo(tmp_path, monkeypatch):
    init_git_repo(tmp_path)
    monkeypatch.setattr(MODULE, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(MODULE, "LIVE_STATE", tmp_path / "docs" / "semiont" / "routine-live-state.json")
    return tmp_path


def _status_for(task_id: str) -> str:
    report = MODULE.check(grace_hours=3, window_hours=6)
    row = next(r for r in report["results"] if r["taskId"] == task_id)
    return row["status"]


def test_trace_refs_only_head_without_origin(repo):
    commit_at(repo, "base", datetime.now(timezone.utc) - timedelta(days=2))
    assert MODULE._trace_refs() == ["HEAD"]


def test_trace_refs_includes_origin_main_when_ref_exists(repo):
    commit_at(repo, "base", datetime.now(timezone.utc) - timedelta(days=2))
    _run(["git", "update-ref", "refs/remotes/origin/main", "HEAD"], cwd=repo)
    assert MODULE._trace_refs() == ["HEAD", "origin/main"]


def test_trace_only_on_origin_main_is_still_traced(repo):
    """09-16 的真實形狀：本機 main 與 origin 分岔，routine 的 memory commit 只在 origin/main。"""
    base_time = datetime.now(timezone.utc) - timedelta(days=2)
    fire = datetime.now(timezone.utc) - timedelta(hours=5)
    commit_at(repo, "base", base_time)
    _run(["git", "checkout", "-q", "-b", "origin-side"], cwd=repo)
    commit_at(
        repo,
        "🧬 [routine] memory: twmd-maintainer-am @ 2026-09-16 — 收下的譯文裡有兩篇",
        fire + timedelta(minutes=30),
        memory_file="2026-09-16-090341-twmd-maintainer-am.md",
    )
    _run(["git", "update-ref", "refs/remotes/origin/main", "HEAD"], cwd=repo)
    # 本機 main 往另一邊長，收不到那個 commit
    _run(["git", "checkout", "-q", "main"], cwd=repo)
    commit_at(repo, "🧬 [semiont] babel: de 批次 6 篇", fire + timedelta(minutes=10))

    write_live_state(repo, "twmd-maintainer-daily", fire)
    assert _status_for("twmd-maintainer-daily") == "traced"


def test_no_trace_on_either_ref_is_silent_death(repo):
    fire = datetime.now(timezone.utc) - timedelta(hours=5)
    commit_at(repo, "base", fire - timedelta(days=1))
    _run(["git", "update-ref", "refs/remotes/origin/main", "HEAD"], cwd=repo)
    commit_at(repo, "🧬 [semiont] babel: de 批次 6 篇", fire + timedelta(minutes=10))
    write_live_state(repo, "twmd-maintainer-daily", fire)
    assert _status_for("twmd-maintainer-daily") == "silent-death"


def test_same_commit_on_both_refs_is_not_duplicated(repo):
    fire = datetime.now(timezone.utc) - timedelta(hours=5)
    commit_at(repo, "base", fire - timedelta(days=1))
    commit_at(
        repo,
        "🧬 [routine] memory: twmd-maintainer-am @ today",
        fire + timedelta(minutes=30),
        memory_file="2026-09-17-090000-twmd-maintainer-am.md",
    )
    _run(["git", "update-ref", "refs/remotes/origin/main", "HEAD"], cwd=repo)
    subjects = MODULE._git_subjects(fire, fire + timedelta(hours=6))
    assert len(subjects) == 1
    assert "twmd-maintainer-am" in subjects[0]
