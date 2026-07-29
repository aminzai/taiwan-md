import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_translation",
    ROOT / "scripts/tools/lang-sync/verify-translation.py",
)
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def test_detect_lang_repo_relative_paths():
    assert VERIFY.detect_lang("knowledge/ar/People/example.md") == "ar"
    assert VERIFY.detect_lang("ja/People/example.md") == "ja"


def test_detect_lang_absolute_path():
    assert (
        VERIFY.detect_lang("/Users/test/taiwan-md/knowledge/pt/Food/example.md")
        == "pt"
    )


def test_detect_lang_run_quarantine_path():
    assert (
        VERIFY.detect_lang("/private/tmp/babel-run/quarantine/ru--example.md")
        == "ru"
    )


def test_detect_lang_legacy_fallback():
    assert VERIFY.detect_lang("/tmp/unknown/example.md") == "en"
