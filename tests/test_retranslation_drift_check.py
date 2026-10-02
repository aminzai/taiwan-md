import importlib.util
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts" / "tools" / "lang-sync" / "retranslation-drift-check.py"
)
SPEC = importlib.util.spec_from_file_location("retranslation_drift_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

FM = "---\ntitle: 't'\ntranslatedFrom: 'Society/x.md'\nsourceCommitSha: 'abc1234'\n---\n"
ZH_OLD = "前言社區組織。\n\n## 一\n\n社區組織的事。\n\n## 二\n\n社區組織活動。\n\n## 三\n\n社區組織大學。\n\n## 四\n\n鄰長沒有補助。\n"
ZH_NEW = ZH_OLD.replace("鄰長沒有補助。", "鄰長每月有 2,500 元。")
JA_OLD = FM + "前言コミュニティ組織。\n\n## 一\n\nコミュニティ組織の事。\n\n## 二\n\nコミュニティ組織の活動。\n\n## 三\n\nコミュニティ組織の大学。\n\n## 四\n\n隣長は補助なし。\n"


def run(monkeypatch, new_text):
    blobs = {("abc1234", "knowledge/Society/x.md"): ZH_OLD,
             ("BASE", "knowledge/ja/Society/x.md"): JA_OLD,
             ("NEW", "knowledge/ja/Society/x.md"): new_text,
             ("NEW", "knowledge/Society/x.md"): ZH_NEW}
    monkeypatch.setattr(MODULE, "git_show", lambda rev, path: blobs.get((rev, path)))
    return MODULE.check("knowledge/ja/Society/x.md", "BASE", "NEW")


def test_whole_article_term_swap_in_unchanged_chapters_is_flagged(monkeypatch):
    """2026-10-03 正控制組：10-02 日文社區篇把「社區」整篇寫成「社協」（日文是社會福祉
    協議會），中文那幾章根本沒改。只改了第四章的重譯不該動到前三章的主詞。"""
    bad = JA_OLD.replace("コミュニティ組織", "社協組織").replace("隣長は補助なし。", "隣長は毎月2,500元。")
    kind, notes = run(monkeypatch, bad)
    assert kind == "drift"
    assert "整篇換詞" in notes[0] and "社協組織" in notes[0]


def test_faithful_patch_of_changed_chapter_only_is_clean(monkeypatch):
    """負控制組：只補中文改過的那一章、沒改的章原樣保留，應該完全不報。"""
    good = JA_OLD.replace("隣長は補助なし。", "隣長は毎月2,500元。")
    kind, notes = run(monkeypatch, good)
    assert kind == "ok", notes
