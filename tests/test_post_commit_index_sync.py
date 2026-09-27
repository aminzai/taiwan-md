import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lib" / "post-commit-index-sync.py"
# 模擬 lint-staged：把暫存檔改寫（這裡是轉大寫）再 add 回去
FORMATTER = ("#!/bin/sh\nfor f in $(git diff --cached --name-only); do "
             "tr 'a-z' 'A-Z' < \"$f\" > \"$f.tmp\" && mv \"$f.tmp\" \"$f\" && git add \"$f\"; done\n")


def _git(repo, *args):
    return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)


def _repo(tmp_path, with_post_commit: bool) -> Path:
    repo = tmp_path / "r"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "t@example.com")
    _git(repo, "config", "user.name", "t")
    (repo / "a.txt").write_text("a\n", encoding="utf-8")
    (repo / "other.txt").write_text("o\n", encoding="utf-8")
    _git(repo, "add", ".")
    _git(repo, "commit", "-q", "-m", "init")
    hooks = repo / ".git" / "hooks"
    (hooks / "pre-commit").write_text(FORMATTER, encoding="utf-8")
    (hooks / "pre-commit").chmod(0o755)
    if with_post_commit:
        (hooks / "post-commit").write_text(f"#!/bin/sh\n{sys.executable} {SCRIPT}\n", encoding="utf-8")
        (hooks / "post-commit").chmod(0o755)
    return repo


def _show(repo, spec: str) -> str:
    return _git(repo, "show", spec).stdout


def test_pathspec_commit_leaves_the_pre_hook_version_in_the_index(tmp_path):
    # 2026-09-27 一天三次的病：pre-commit 跑在暫時 index 上，真正的 index 留著改寫前的版本
    repo = _repo(tmp_path, with_post_commit=False)
    (repo / "a.txt").write_text("b\n", encoding="utf-8")
    _git(repo, "commit", "-q", "-m", "x", "--", "a.txt")
    assert _show(repo, "HEAD:a.txt") == "B\n"
    assert (repo / "a.txt").read_text(encoding="utf-8") == "B\n"
    assert _show(repo, ":a.txt") == "b\n"


def test_post_commit_aligns_the_index_and_leaves_other_staging_alone(tmp_path):
    repo = _repo(tmp_path, with_post_commit=True)
    (repo / "other.txt").write_text("p\n", encoding="utf-8")
    _git(repo, "add", "other.txt")  # 別人暫存中、這次沒 commit 的檔
    (repo / "a.txt").write_text("b\n", encoding="utf-8")
    _git(repo, "commit", "-q", "-m", "x", "--", "a.txt")
    assert _show(repo, "HEAD:a.txt") == "B\n"
    assert _show(repo, ":a.txt") == "B\n"
    assert _show(repo, ":other.txt") == "p\n"


def test_a_committed_path_that_is_being_edited_again_is_not_touched(tmp_path):
    repo = _repo(tmp_path, with_post_commit=False)
    (repo / "a.txt").write_text("b\n", encoding="utf-8")
    _git(repo, "commit", "-q", "-m", "x", "--", "a.txt")
    (repo / "a.txt").write_text("still editing\n", encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT)], cwd=repo, capture_output=True, text=True)
    assert r.returncode == 0
    assert _show(repo, ":a.txt") == "b\n"
