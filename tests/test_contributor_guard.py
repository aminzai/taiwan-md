"""OBSERVER-QUEUE #67（2026-10-10 哲宇拍板 B）：babel 不覆蓋投稿者翻好的譯文。

三種形狀：
  (a) 目標檔被開著的投稿 PR 碰到 → 跳過
  (b) 現行譯文是人翻的、zh 更新判 stale → 跳過、記提議檔
  (c) 現行譯文是機器翻的 stale → 照常進佇列
再加：gh 失敗不弄垮產線、BABEL_CONTRIBUTOR_GUARD=0 整個關掉。
"""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

LANG_SYNC = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, LANG_SYNC / filename)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = mod   # @dataclass 解析 annotation 時要在 sys.modules 找得到
    spec.loader.exec_module(mod)
    return mod


cg = _load("contributor_guard", "contributor_guard.py")


# ───────────────────────────── fixtures ─────────────────────────────

def _git(repo: Path, *args, author=None):
    env = None
    if author:
        name, email = author
        env = {"GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email,
               "GIT_COMMITTER_NAME": name, "GIT_COMMITTER_EMAIL": email,
               "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": str(repo)}
    r = subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, env=env)
    assert r.returncode == 0, r.stderr
    return r.stdout


def _write_translation(repo: Path, rel: str, translated_at: str, body: str):
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        f"---\ntitle: 'x'\ntranslatedFrom: 'People/X.md'\ntranslatedAt: '{translated_at}'\n---\n\n{body}\n",
        encoding="utf-8",
    )


HUMAN = ("aminzai", "lagunawang@gmail.com")
BOT = ("Taiwan.md Semiont", "309092923+taiwanmd-semiont[bot]@users.noreply.github.com")
OWNER = ("Che-Yu Wu", "cheyu.wu@monoame.com")


@pytest.fixture
def repo(tmp_path):
    """一個小 git repo：de 譯文是投稿者翻的、ar 譯文是 babel 翻的，之後各被一個
    routine heal 碰過 frontmatter（確認看的是 translatedAt 的 commit，不是最後一個 commit）。"""
    _git(tmp_path, "init", "-q", "-b", "main")
    _git(tmp_path, "config", "user.email", "t@t")
    _git(tmp_path, "config", "user.name", "t")
    _write_translation(tmp_path, "knowledge/de/People/x.md", "2026-09-01T10:00:00+08:00", "Mensch")
    _git(tmp_path, "add", "knowledge/de/People/x.md")
    _git(tmp_path, "commit", "-q", "-m", "translate(de): X → x", author=HUMAN)
    _write_translation(tmp_path, "knowledge/ar/People/x.md", "2026-09-02T10:00:00+08:00", "آلة")
    _git(tmp_path, "add", "knowledge/ar/People/x.md")
    _git(tmp_path, "commit", "-q", "-m", "🧬 [semiont] babel: ar 批次 1 篇", author=BOT)
    # 兩檔都被一個 heal 碰 body（不碰 translatedAt）——最後一個 commit 是機器
    for rel in ("knowledge/de/People/x.md", "knowledge/ar/People/x.md"):
        p = tmp_path / rel
        p.write_text(p.read_text(encoding="utf-8") + "\n<!-- heal -->\n", encoding="utf-8")
    _git(tmp_path, "add", "knowledge")
    _git(tmp_path, "commit", "-q", "-m", "🧬 [routine] heal: 分類值改名", author=BOT)
    return tmp_path


def _guard(repo, pr_files=None, gh_fails=False, log=None, enabled=True):
    def runner():
        if gh_fails:
            raise RuntimeError("gh: not logged in")
        import json
        return json.dumps([{"number": n, "files": [{"path": p} for p in paths]}
                           for n, paths in (pr_files or {}).items()])
    msgs = log if log is not None else []
    idx = cg.OpenPRIndex(log=msgs.append, runner=runner)
    return cg.ContributorGuard(repo=repo, log=msgs.append, open_prs=idx,
                               proposals_tsv=repo / "reports" / "babel" / "human-translation-stale.tsv",
                               enabled=enabled), msgs


# ───────────────────────────── 作者判定 ─────────────────────────────

def test_authorship_reads_translated_at_commit_not_last_commit(repo):
    a = cg.translation_authorship(repo, "knowledge/de/People/x.md", {})
    assert a is not None and a.via == "translatedAt"
    assert a.name == "aminzai" and not a.machine
    b = cg.translation_authorship(repo, "knowledge/ar/People/x.md", {})
    assert b is not None and b.via == "translatedAt" and b.machine


@pytest.mark.parametrize("name,email,subject,machine", [
    ("Taiwan.md Semiont", "309092923+taiwanmd-semiont[bot]@users.noreply.github.com", "anything", True),
    ("github-actions[bot]", "41898282+github-actions[bot]@users.noreply.github.com", "x", True),
    ("Taiwan.md Semiont", "cheyu.wu@monoame.com", "🧬 [routine] heal: x", True),
    ("Wu Che Yu", "frank890417@gmail.com", "🧬 [造橋鋪路] 巴別塔 owl/Hy3 cascade", True),
    ("Che-Yu Wu", "cheyu.wu@monoame.com", "🧬 [semiont] heal: 分類", True),
    ("aminzai", "lagunawang@gmail.com", "translate(de): X", False),
    ("Kevin Huang", "kevin86568656@gmail.com", "translate(de): 陳士駿", False),
    # 投稿者也會寫 🧬 [semiont] 前綴——🧬 本身不是機器證據
    ("HHQ", "101655495+rhosiqs@users.noreply.github.com", "🧬 [semiont] translation: polish English prose", False),
    ("Che-Yu Wu", "cheyu.wu@monoame.com", "fix typo", False),
])
def test_is_machine_author(name, email, subject, machine):
    assert cg.is_machine_author(name, email, subject) is machine


# ───────────────────────────── (a) open-PR 過濾 ─────────────────────────────

def test_open_pr_file_is_skipped_existing_and_missing(repo):
    guard, msgs = _guard(repo, pr_files={1798: ["knowledge/ar/People/x.md", "knowledge/hi/People/y.md"]})
    # stale 既有譯文被 PR 碰到
    d = guard.check("ar", "People/X.md", "stale", "knowledge/ar/People/x.md", zh_sha="abc1234")
    assert not d.ok and d.reason == "open-pr" and "#1798" in d.detail
    # 缺頁：還沒有路徑，用 slug 對 PR 檔名
    d2 = guard.check("hi", "People/Y.md", "missing", None, slug="y", zh_sha="abc1234")
    assert not d2.ok and d2.reason == "open-pr"
    # 沒被碰到的照常
    assert guard.check("hi", "People/Z.md", "missing", None, slug="z").ok
    assert any("開著的投稿 PR #1798" in m for m in msgs)
    # 沒有記成提議（open-pr 不是人翻 stale）
    assert not (repo / "reports/babel/human-translation-stale.tsv").exists()


def test_gh_failure_disables_filter_but_pipeline_continues(repo):
    guard, msgs = _guard(repo, gh_fails=True)
    d = guard.check("ar", "People/X.md", "stale", "knowledge/ar/People/x.md")
    assert d.ok
    assert guard.open_prs.available is False
    assert any("open-PR 過濾關閉" in m for m in msgs)


# ───────────────────────────── (b) 人翻的 stale ─────────────────────────────

def test_human_authored_stale_is_skipped_logged_and_proposed(repo):
    guard, msgs = _guard(repo)
    d = guard.check("de", "People/X.md", "stale", "knowledge/de/People/x.md", zh_sha="deadbee")
    assert not d.ok and d.reason == "human-authored" and "aminzai" in d.detail
    assert any("現行譯文是人寫的" in m and "aminzai" in m for m in msgs)
    tsv = repo / "reports/babel/human-translation-stale.tsv"
    lines = tsv.read_text(encoding="utf-8").splitlines()
    assert lines[0].startswith("# recorded_at\tlang\tpath\tzh_path\tzh_sha\tauthor\treason")
    cols = lines[1].split("\t")
    assert cols[1:5] == ["de", "knowledge/de/People/x.md", "People/X.md", "deadbee"]
    assert "aminzai" in cols[5]
    # 同一 (path, zh_sha) 再問一次：不重複記、不重複 log
    n_msgs = len(msgs)
    d2 = guard.check("de", "People/X.md", "stale", "knowledge/de/People/x.md", zh_sha="deadbee")
    assert not d2.ok
    assert len(tsv.read_text(encoding="utf-8").splitlines()) == 2
    assert len(msgs) == n_msgs
    assert guard.skipped == {"open-pr": 0, "human-authored": 1}


# ───────────────────────────── (c) 機器翻的 stale ─────────────────────────────

def test_machine_authored_stale_proceeds(repo):
    guard, msgs = _guard(repo)
    d = guard.check("ar", "People/X.md", "stale", "knowledge/ar/People/x.md", zh_sha="deadbee")
    assert d.ok and d.reason == ""
    assert not (repo / "reports/babel/human-translation-stale.tsv").exists()
    assert not any("skip" in m for m in msgs)


def test_env_switch_disables_everything(repo):
    guard, _ = _guard(repo, pr_files={1: ["knowledge/de/People/x.md"]}, enabled=False)
    assert guard.check("de", "People/X.md", "stale", "knowledge/de/People/x.md").ok


# ───────────────────────────── dispatcher 整合 ─────────────────────────────

def test_build_worklist_drops_guarded_targets(repo):
    bd = _load("babel_dispatch", "babel-dispatch.py")
    status_data = {"byArticle": {
        "People/X.md": {"zh": {"lastModified": "2026-10-01T00:00:00+08:00", "lastCommit": "aaa1111"},
                        "translations": {"de": {"status": "stale", "path": "de/People/x.md"},
                                         "ar": {"status": "stale", "path": "ar/People/x.md"}}},
        "People/Y.md": {"zh": {"lastModified": "2026-10-02T00:00:00+08:00", "lastCommit": "bbb2222"},
                        "translations": {"de": {"status": "missing"}, "ar": {"status": "missing"}}},
    }}
    guard, msgs = _guard(repo, pr_files={1798: ["knowledge/ar/People/y.md"]})
    slug_map = {"People/Y.md": "y"}
    de = bd.build_worklist(status_data, "de", "all", "forward", guard=guard, slug_map=slug_map)
    ar = bd.build_worklist(status_data, "ar", "all", "forward", guard=guard, slug_map=slug_map)
    assert de == ["People/Y.md"]                 # X：人翻的 stale 被擋；Y 缺頁照排
    assert ar == ["People/X.md"]                 # X：機器翻的 stale 照排；Y 缺頁被開著的 PR 擋
    # 沒 guard 時行為不變（舊路徑）
    assert bd.build_worklist(status_data, "de", "all", "forward") == ["People/Y.md", "People/X.md"]
