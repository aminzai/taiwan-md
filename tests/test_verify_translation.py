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


def test_extract_urls_ignores_markdown_backslash_escapes():
    zh = "[檔案頁](https://commons.wikimedia.org/wiki/File:Ruisui,_Hualien_County,_Taiwan.jpg)"
    tr = "[File](https://commons.wikimedia.org/wiki/File:Ruisui,\\_Hualien_County,\\_Taiwan.jpg)"
    assert VERIFY.extract_urls(zh) == VERIFY.extract_urls(tr)
    paren = "[獎](https://zh.wikipedia.org/zh-tw/最佳客語專輯獎_\\(金曲獎\\))"
    plain = "[award](https://zh.wikipedia.org/zh-tw/最佳客語專輯獎_(金曲獎))"
    assert VERIFY.extract_urls(paren) == VERIFY.extract_urls(plain)


def test_extract_urls_still_catches_real_url_changes():
    a = VERIFY.extract_urls("https://example.com/a_b/%E7%B8%BD")
    b = VERIFY.extract_urls("https://example.com/a_b/%E7%B8%BA")
    assert a != b
