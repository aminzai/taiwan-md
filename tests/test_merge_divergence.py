"""merge-divergence.py — 分岔合併工具的純函式：衝突分類、雙檔去重、檔名對齊。"""
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "merge-divergence.py"
SPEC = importlib.util.spec_from_file_location("merge_divergence", MODULE_PATH)
M = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(M)


def test_classify_routes_by_path():
    assert M.classify("knowledge/de/Food/x.md") == "theirs"
    assert M.classify("public/api/stats.json") == "theirs"
    assert M.classify("knowledge/_translations.json") == "theirs"
    assert M.classify("reports/babel/fail-memo.json") == "union-json"
    assert M.classify("docs/semiont/MEMORY.md") == "hand"
    assert M.classify("scripts/tools/lang-sync/babel-dispatch.py") == "hand"
    assert M.classify("knowledge/Food/母稿.md") == "hand"  # zh 母稿不是譯文，不自動取 origin


def test_dedupe_keeps_origin_copy(monkeypatch):
    fam = {"vi": {"Art/x.md": ["knowledge/vi/Art/a.md", "knowledge/vi/Art/b.md"]}}
    monkeypatch.setattr(M, "in_base", lambda base, rel: rel.endswith("/a.md"))
    drop, pre = M.dedupe_plan(fam, "base")
    assert drop == ["knowledge/vi/Art/b.md"] and pre == []


def test_dedupe_leaves_preexisting_origin_pairs(monkeypatch):
    fam = {"en": {"Art/x.md": ["knowledge/en/Art/a.md", "knowledge/en/Art/b.md"]}}
    monkeypatch.setattr(M, "in_base", lambda base, rel: True)
    drop, pre = M.dedupe_plan(fam, "base")
    assert drop == [] and len(pre) == 1


def test_align_renames_local_sibling_to_en(monkeypatch):
    fam = {"en": {"Art/x.md": ["knowledge/en/Art/canon.md"]},
           "de": {"Art/x.md": ["knowledge/de/Art/other.md"]}}
    monkeypatch.setattr(M, "in_base", lambda base, rel: rel.startswith("knowledge/en/"))
    renames, en_renames, skipped = M.align_plan(fam, "base")
    assert renames == [("knowledge/de/Art/other.md", "knowledge/de/Art/canon.md", False)]
    assert en_renames == [] and skipped == []


def test_align_moves_late_en_to_live_majority(monkeypatch):
    fam = {"en": {"Art/x.md": ["knowledge/en/Art/new-name.md"]},
           "de": {"Art/x.md": ["knowledge/de/Art/old-name.md"]},
           "fr": {"Art/x.md": ["knowledge/fr/Art/old-name.md"]}}
    monkeypatch.setattr(M, "in_base", lambda base, rel: not rel.startswith("knowledge/en/"))
    renames, en_renames, skipped = M.align_plan(fam, "base")
    assert renames == [] and skipped == []
    assert en_renames == [("knowledge/en/Art/new-name.md", "knowledge/en/Art/old-name.md")]
