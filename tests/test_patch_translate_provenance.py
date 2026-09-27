import importlib.util
import sys
from pathlib import Path

LANG_SYNC = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"
sys.path.insert(0, str(LANG_SYNC))
SPEC = importlib.util.spec_from_file_location("patch_translate", LANG_SYNC / "patch-translate.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_replace_provenance_strips_by_key_not_by_count(monkeypatch):
    # structured-translate 現在尾端寫 5 行 provenance（含 sourceBodyHash）；舊的 [:-4] 切片會留下一行
    monkeypatch.setattr(MODULE, "provenance_lines", lambda zh_path, zh: [
        "translatedFrom: 'About/x.md'", "sourceCommitSha: 'abc1234'",
        "sourceContentHash: 'sha256:1'", "sourceBodyHash: 'sha256:2'", "translatedAt: 'now'"])
    block = "\n".join(["title: 'T'", "tags: ['a']",
                       "translatedFrom: 'About/x.md'", "sourceCommitSha: 'old'",
                       "sourceContentHash: 'sha256:0'", "sourceBodyHash: 'sha256:0'", "translatedAt: 'then'"])
    out = MODULE.replace_provenance(block, "About/x.md", "")
    keys = [l.split(":")[0] for l in out.split("\n")]
    assert keys.count("translatedFrom") == 1
    assert keys.count("sourceBodyHash") == 1
    assert out.startswith("title: 'T'\ntags: ['a']\n")
