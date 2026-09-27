import importlib.util
import json
from pathlib import Path


LANG_SYNC_DIR = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"
MODULE_PATH = LANG_SYNC_DIR / "babel-pulse.py"
SPEC = importlib.util.spec_from_file_location("babel_pulse", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_old_untracked_translation_outside_live_batch_is_orphan():
    # 2026-09-27 實例：前一晚 dispatcher 重啟後遺落的 de〈大龍峒〉，放了 21 小時沒人 commit
    items = MODULE.parse_porcelain("?? knowledge/de/Geography/dalongdong.md\0")
    r = MODULE.classify_uncommitted(items, set(), lambda p: 1260)
    assert r["pending"] == 0
    assert r["orphans"] == [{"path": "knowledge/de/Geography/dalongdong.md", "xy": "??", "age_min": 1260}]


def test_live_batch_and_just_written_files_are_pending(tmp_path, monkeypatch):
    run = tmp_path / "babel-unified-20260927-153924-74699"
    run.mkdir()
    (run / "report.jsonl").write_text(
        json.dumps({"trans": "knowledge/ar/Economy/a.md", "ok": True}) + "\n"
        + json.dumps({"trans": "knowledge/ar/Economy/b.md", "ok": False}) + "\n",
        encoding="utf-8")
    monkeypatch.setattr(MODULE, "RUN_BASE", tmp_path)
    pending = MODULE.live_run_outputs([{"kind": "unified", "pid": "74699"}])
    assert pending == {"knowledge/ar/Economy/a.md"}
    items = MODULE.parse_porcelain(
        "?? knowledge/ar/Economy/a.md\0?? knowledge/ar/Economy/b.md\0 M knowledge/ja/People/c.md\0")
    ages = {"knowledge/ar/Economy/a.md": 200, "knowledge/ar/Economy/b.md": 200,
            "knowledge/ja/People/c.md": 5}
    r = MODULE.classify_uncommitted(items, pending, ages.get)
    # a 在活產線的批次裡、c 剛寫好 → pending；b 沒通過驗證又放了 200 分鐘 → 孤兒
    assert r["pending"] == 2
    assert [o["path"] for o in r["orphans"]] == ["knowledge/ar/Economy/b.md"]


def test_dead_dispatcher_batch_does_not_count_as_pending(tmp_path, monkeypatch):
    # 重啟前那輪的 run dir 還在 /tmp，但它的 pid 已經不在產線清單裡：那批不再有人 commit
    run = tmp_path / "babel-unified-20260926-102234-52927"
    run.mkdir()
    (run / "report.jsonl").write_text(
        json.dumps({"trans": "knowledge/de/Geography/kaohsiung-city.md", "ok": True}) + "\n",
        encoding="utf-8")
    monkeypatch.setattr(MODULE, "RUN_BASE", tmp_path)
    assert MODULE.live_run_outputs([{"kind": "unified", "pid": "74699"}]) == set()


def test_rename_entry_skips_origin_path_and_non_markdown_is_ignored():
    z = "R  knowledge/en/People/new.md\0knowledge/en/People/old.md\0?? knowledge/en/People/x.metrics.json\0"
    items = MODULE.parse_porcelain(z)
    assert items == [("R ", "knowledge/en/People/new.md"), ("??", "knowledge/en/People/x.metrics.json")]
    r = MODULE.classify_uncommitted(items, set(), lambda p: 999)
    assert [o["path"] for o in r["orphans"]] == ["knowledge/en/People/new.md"]


def test_snapshot_paths_follow_the_months_that_exist(tmp_path):
    babel = tmp_path / "reports" / "babel"
    babel.mkdir(parents=True)
    for n in ("progress-2026-07.jsonl", "progress-2026-09.jsonl", "progress-log-2026-09.md", "fail-memo.json"):
        (babel / n).write_text("x", encoding="utf-8")
    paths = MODULE.snapshot_paths(tmp_path)
    assert "reports/babel/progress-2026-09.jsonl" in paths
    assert "reports/babel/progress-log-2026-09.md" in paths
    assert "reports/babel/fail-memo.json" not in paths


def _git(repo, *args):
    import subprocess
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


def test_staged_content_the_worktree_no_longer_backs_is_leftover(tmp_path, monkeypatch):
    repo = tmp_path / "r"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "t@example.com")
    _git(repo, "config", "user.name", "t")
    queue, draft = repo / "queue.md", repo / "draft.md"
    queue.write_text("| a |\n", encoding="utf-8")
    draft.write_text("x\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "init")
    # 2026-09-27 的形狀：有人暫存了表格重排版，工作樹又回到 HEAD
    queue.write_text("|  a  |\n", encoding="utf-8")
    _git(repo, "add", "queue.md")
    queue.write_text("| a |\n", encoding="utf-8")
    # 正常的部分暫存：工作樹還有自己的改動，是有人在編輯中，不算殘留
    draft.write_text("y\n", encoding="utf-8")
    _git(repo, "add", "draft.md")
    draft.write_text("z\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "REPO", repo)
    monkeypatch.setattr(MODULE, "GIT_LOCK", tmp_path / "lock")
    assert MODULE.leftover_staged() == ["queue.md"]
    (tmp_path / "lock").mkdir()
    assert MODULE.leftover_staged() == []  # 有人拿著共用鎖正在 add→commit
