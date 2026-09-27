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


FR = ("Cet article parle de l'histoire et de la culture de Taïwan pour les lecteurs qui veulent "
      "comprendre la société de cette île et ses habitants. ") * 12
EN = ("This article discusses the history and the culture of Taiwan for readers who want to "
      "understand the society of this island and its people. ") * 12


def _lang_repo(tmp_path, monkeypatch):
    en = tmp_path / "knowledge" / "en"
    en.mkdir(parents=True)
    (en / "a.md").write_text("---\ntitle: t\n---\n" + FR, encoding="utf-8")  # 在 en 目錄裡的法文
    (en / "b.md").write_text("---\ntitle: t\n---\n" + EN, encoding="utf-8")
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    monkeypatch.setattr(MODULE, "TLC_CACHE", tmp_path / ".taiwanmd" / "tlc-cache.json")
    return en


def test_fresh_translation_in_the_wrong_language_is_counted(tmp_path, monkeypatch):
    # 2026-09-27 實例：ja〈黃山料〉整篇英文，status 照算 fresh
    _lang_repo(tmp_path, monkeypatch)
    r = MODULE.language_mismatch()
    assert r["wrong_language"] == 1 and r["foreign_script"] == 0 and r["total"] == 1
    assert r["sample"] == [{"path": "knowledge/en/a.md", "kind": "wrong_language", "detected": "fr"}]


def test_unchanged_files_reuse_the_cache_and_changed_files_are_judged_again(tmp_path, monkeypatch):
    en = _lang_repo(tmp_path, monkeypatch)
    MODULE.language_mismatch()
    cache = json.loads(MODULE.TLC_CACHE.read_text(encoding="utf-8"))
    cache["knowledge/en/b.md"][1:3] = ["fail", "foreign_script"]  # 檔案沒動、判定被改：應該照快取
    MODULE.TLC_CACHE.write_text(json.dumps(cache), encoding="utf-8")
    assert MODULE.language_mismatch()["foreign_script"] == 1
    (en / "b.md").write_text("---\ntitle: t\n---\n" + EN + "More text. ", encoding="utf-8")
    assert MODULE.language_mismatch()["foreign_script"] == 0  # 檔案變了就重判


def test_translation_that_stops_after_the_first_sections_is_counted(tmp_path, monkeypatch):
    # 2026-09-27 實例：es〈長榮海運〉zh 八個章節只譯到第二個，版本標記照樣是新的
    zh_dir, en_dir = tmp_path / "knowledge" / "Economy", tmp_path / "knowledge" / "en" / "Economy"
    zh_dir.mkdir(parents=True)
    en_dir.mkdir(parents=True)
    zh_body = "".join(f"## 第{i}章\n\n" + "內容" * 200 + "\n\n" for i in range(8))
    (zh_dir / "x.md").write_text("---\ntitle: x\n---\n" + zh_body, encoding="utf-8")
    full = "".join(f"## Part {i}\n\n" + "text " * 240 + "\n\n" for i in range(8))
    head = "".join(f"## Part {i}\n\n" + "text " * 240 + "\n\n" for i in range(2))
    for n in range(4):
        (en_dir / f"ok{n}.md").write_text("---\ntranslatedFrom: 'Economy/x.md'\n---\n" + full, encoding="utf-8")
    (en_dir / "cut.md").write_text("---\ntranslatedFrom: 'Economy/x.md'\n---\n" + head, encoding="utf-8")
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    r = MODULE.truncated_translations()
    assert r["count"] == 1
    assert r["sample"][0]["path"] == "knowledge/en/Economy/cut.md" and r["sample"][0]["h2"] == "8→2"


def test_translation_that_dropped_every_source_is_counted(tmp_path, monkeypatch):
    # 2026-09-27 實例：fr〈台灣官方網站資源〉zh 引了 53 個網址，法文版一個都沒有
    zh_dir, en_dir = tmp_path / "knowledge" / "About", tmp_path / "knowledge" / "en" / "About"
    zh_dir.mkdir(parents=True)
    en_dir.mkdir(parents=True)
    links = "".join(f"- https://example.gov.tw/{i}\n" for i in range(6))
    (zh_dir / "x.md").write_text("---\ntitle: x\n---\n## 一\n\n內容\n\n## 參考資料\n\n" + links, encoding="utf-8")
    (en_dir / "kept.md").write_text("---\ntranslatedFrom: 'About/x.md'\n---\n## One\n\ntext\n\n## References\n\n" + links, encoding="utf-8")
    (en_dir / "dropped.md").write_text("---\ntranslatedFrom: 'About/x.md'\n---\n## One\n\ntext\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    r = MODULE.content_gaps()["no_sources"]
    assert r["count"] == 1 and r["sample"] == [{"path": "knowledge/en/About/dropped.md", "zh_urls": 6}]
