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


def test_frontmatter_debt_flags_tags_collapsed_into_one_string():
    # 2026-09-27：ar 438 篇、ja 14 篇的 tags 是一個字串包著整張清單（整篇引擎只切 ASCII 逗號）；
    # patch 碰到時要改走 LLM 重翻 frontmatter，不沿用那一格
    zh = {"tags": ["泰雅族", "紋面", "染織", "gaga", "文化復興"]}
    collapsed = {"tags": ["タイヤル族、紋面、染織、gaga、文化復興"]}
    assert MODULE.frontmatter_debt(zh, collapsed) == ["tags 擠成 1 個字串（zh 有 5 個）"]
    fine = {"tags": ["Atayal", "facial tattoo", "weaving", "gaga", "cultural revival"]}
    assert MODULE.frontmatter_debt(zh, fine) == []
    # zh 本來就只有一個標籤：譯文一個標籤是正常的
    assert MODULE.frontmatter_debt({"tags": ["泰雅族"]}, {"tags": ["タイヤル族"]}) == []
