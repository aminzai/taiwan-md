import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "verify-translation.py"
SPEC = importlib.util.spec_from_file_location("verify_translation", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_unquoted_bracket_list_items_are_read():
    fm, _ = MODULE.parse_fm("---\ntitle: 'T'\ntags:\n  [\n    Alishan,\n    Waldbahn,\n    Japanische Kolonialzeit,\n  ]\nfeatured: false\n---\nbody")
    assert fm["tags"] == ["Alishan", "Waldbahn", "Japanische Kolonialzeit"]
    assert fm["featured"] == "false"


def test_quoted_bracket_list_items_still_read():
    fm, _ = MODULE.parse_fm("---\ntags:\n  [\n    'a',\n    'b',\n  ]\n---\n")
    assert fm["tags"] == ["a", "b"]


def _frontmatter_check(tmp_path, monkeypatch, capsys, zh_title, ja_title):
    import json
    import sys
    kn = tmp_path / "knowledge"
    kn.mkdir()
    (kn / "x.md").write_text(f"---\ntitle: '{zh_title}'\ndescription: '中文描述'\n---\n\n## 一\n\n內容。\n", encoding="utf-8")
    ja = tmp_path / "ja--x.md"  # dispatcher 隔離檔的命名，verify 從這裡推得目標語言
    ja.write_text(f"---\ntitle: '{ja_title}'\ndescription: '日本語の説明'\n---\n\n## 一\n\n内容。\n", encoding="utf-8")
    # zh 路徑一律相對 KN 解析（main 會剝掉開頭的斜線），所以把 KN 指到暫存目錄
    monkeypatch.setattr(MODULE, "KN", kn)
    monkeypatch.setattr(MODULE, "REPO", tmp_path)
    monkeypatch.setattr(sys, "argv", ["verify-translation.py", "x.md", str(ja), "--json"])
    MODULE.main()
    checks = json.loads(capsys.readouterr().out)["checks"]
    assert next(c for c in checks if c["name"] == "zh source exists")["level"] == "PASS"
    return next(c for c in checks if c["name"] == "frontmatter not untranslated")["level"]


def test_ja_title_that_is_the_same_kanji_name_passes(tmp_path, monkeypatch, capsys):
    # 2026-09-27：ja〈楊勇緯〉〈杜奕瑾〉的標題就是漢字人名，以前被判未翻，agent 只好替名字加拼音或編新標題
    assert _frontmatter_check(tmp_path, monkeypatch, capsys, "楊勇緯", "楊勇緯") == "PASS"


def test_ja_sentence_title_identical_to_zh_still_fails(tmp_path, monkeypatch, capsys):
    assert _frontmatter_check(tmp_path, monkeypatch, capsys, "台灣企業：長榮海運", "台灣企業：長榮海運") == "FAIL"
