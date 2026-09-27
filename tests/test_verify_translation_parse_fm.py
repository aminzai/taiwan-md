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
