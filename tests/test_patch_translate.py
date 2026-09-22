import importlib.util
import re
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts" / "tools" / "lang-sync" / "patch-translate.py"
)
SPEC = importlib.util.spec_from_file_location("patch_translate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_chapter_urls_are_armored_and_restored(tmp_path):
    """章節級 patch 跟分段式引擎共用 st._validate_chunk()，也就共用「正文連結
    網址對不上」這個失敗家族；2026-09-23 兩條引擎同時改走 @@LINKn@@ 裝甲，
    原始網址不再進 prompt（成因結構一樣就一起修，不等它在這邊也長出統計）。"""
    seen = []

    class Backend:
        name = "stub"

        def translate(self, _system, user, **_kwargs):
            seen.append(user)
            return re.sub(r"[一-鿿，。]+", "translated prose ", user)

    zh_chapter = (
        "## 章節\n\n這是[台灣的頁面](/society/%E5%8F%B0%E7%81%A3)與"
        "[參考來源](https://example.org/a_(b))的說明文字，長度要夠過比值下限。" * 3
    )

    out, issues = MODULE.translate_regular_chapter(
        zh_chapter, "en", Backend(), [], None, None, {}, tmp_path)

    assert "@@LINK0@@" in seen[0]
    assert "/society/%E5%8F%B0%E7%81%A3" not in seen[0], "原始 URL 不該進 prompt"
    assert "/society/%E5%8F%B0%E7%81%A3" in out
    assert "https://example.org/a_(b)" in out
    assert issues == []
