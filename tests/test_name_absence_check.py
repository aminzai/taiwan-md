import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "name-absence-check.py"
SPEC = importlib.util.spec_from_file_location("name_absence_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _pair(tmp_path, monkeypatch, zh, tr):
    k = tmp_path / "knowledge"
    (k / "Society").mkdir(parents=True)
    (k / "en" / "Society").mkdir(parents=True)
    (k / "Society" / "x.md").write_text(zh, encoding="utf-8")
    p = k / "en" / "Society" / "x.md"
    p.write_text("---\ntranslatedFrom: 'Society/x.md'\n---\n" + tr, encoding="utf-8")
    monkeypatch.setattr(MODULE, "KNOWLEDGE", k)
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    return p


def test_person_absent_from_source_is_reported(tmp_path, monkeypatch):
    forms, pat = MODULE.build_pattern()
    p = _pair(tmp_path, monkeypatch, "童子賢個人捐了 500 萬元。", "Barry Lam donated NT$5 million.")
    forms["Barry Lam"] = "林百里"
    import re
    pat = re.compile(r"(?<![A-Za-z\-‑])(Barry Lam)(?![A-Za-z\-‑])")
    hits = MODULE.scan(p, forms, pat)
    assert [h["person"] for h in hits] == ["林百里"]


def test_alias_in_source_is_not_reported(tmp_path, monkeypatch):
    import re
    p = _pair(tmp_path, monkeypatch, "蔣介石來台。", "Chiang Kai-shek arrived.")
    forms = {"Chiang Kai-shek": "蔣中正"}
    pat = re.compile(r"(?<![A-Za-z\-‑])(Chiang Kai-shek)(?![A-Za-z\-‑])")
    assert MODULE.scan(p, forms, pat) == []


def test_hyphenated_given_name_is_not_a_prefix_match(tmp_path, monkeypatch):
    import re
    p = _pair(tmp_path, monkeypatch, "林亮君與林亭均。", "Lin Liang‑jun and Lin Ting‑jun.")
    forms = {"Lin Liang": "林良"}
    pat = re.compile(r"(?<![A-Za-z\-‑])(Lin Liang)(?![A-Za-z\-‑])")
    assert MODULE.scan(p, forms, pat) == []


def test_award_the_source_never_mentions_is_reported(tmp_path, monkeypatch):
    # 2026-09-27 實例：id〈金曲獎〉全篇把金曲獎寫成電影的金馬獎
    forms, pat = MODULE.build_pattern()
    p = _pair(tmp_path, monkeypatch, "金曲獎是台灣流行音樂的年度盛事。", "The Golden Horse Awards honor Taiwanese pop music.")
    assert [h["person"] for h in MODULE.scan(p, forms, pat)] == ["金馬"]


def test_award_named_in_source_or_covered_by_sanjin_is_not_reported(tmp_path, monkeypatch):
    forms, pat = MODULE.build_pattern()
    p = _pair(tmp_path, monkeypatch, "她拿過金曲獎。", "She won a Golden Melody Award.")
    assert MODULE.scan(p, forms, pat) == []
    p = _pair(tmp_path / "b", monkeypatch, "三金得主李欣芸。", "Winner of the Golden Horse, Golden Bell and Golden Melody.")
    assert MODULE.scan(p, forms, pat) == []


def test_university_swapped_for_another_is_reported(tmp_path, monkeypatch):
    # 2026-09-27 實例：en〈馬祖國際藝術島〉把台師大東亞系的江柏煒寫成台大
    forms, pat = MODULE.build_pattern()
    p = _pair(tmp_path, monkeypatch, "台師大東亞系教授江柏煒。", "Professor Jiang Bai-wei of National Taiwan University.")
    assert [h["person"] for h in MODULE.scan(p, forms, pat)] == ["台大"]


def test_longer_university_name_is_not_read_as_ntu(tmp_path, monkeypatch):
    forms, pat = MODULE.build_pattern()
    p = _pair(tmp_path, monkeypatch, "他畢業於台藝大。", "He graduated from the National Taiwan University of Arts.")
    assert MODULE.scan(p, forms, pat) == []
