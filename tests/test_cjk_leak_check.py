import importlib.util
import sys
from pathlib import Path


LANG_SYNC_DIR = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"
MODULE_PATH = LANG_SYNC_DIR / "cjk-leak-check.py"
SPEC = importlib.util.spec_from_file_location("cjk_leak_check", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

# translate.py 的 `backends` 是相對於 lang-sync 目錄的 local package，只有在
# 該目錄進了 sys.path 才 import 得到（正常執行 `python3 .../translate.py` 時
# Python 會自動把腳本所在目錄加進 sys.path[0]；用 spec_from_file_location 從
# tests/ 載入則不會，要手動補）。
sys.path.insert(0, str(LANG_SYNC_DIR))
TRANSLATE_MODULE_PATH = LANG_SYNC_DIR / "translate.py"
_TRANSLATE_SPEC = importlib.util.spec_from_file_location("translate", TRANSLATE_MODULE_PATH)
TRANSLATE_MODULE = importlib.util.module_from_spec(_TRANSLATE_SPEC)
assert _TRANSLATE_SPEC and _TRANSLATE_SPEC.loader
_TRANSLATE_SPEC.loader.exec_module(TRANSLATE_MODULE)


def test_ja_ignores_zh_markers_in_passthrough_frontmatter(tmp_path):
    path = tmp_path / "ja--example.md"
    path.write_text(
        "---\n"
        "title: '日本語の題名'\n"
        "rationale: '這個中文欄位是編輯資料'\n"
        "researchReport: 'reports/研究/那個人.md'\n"
        "---\n\n"
        "これは完全に日本語の本文です。\n",
        encoding="utf-8",
    )

    assert MODULE.scan_file(path, lang="ja") == []


def test_ja_still_flags_zh_marker_in_body(tmp_path):
    path = tmp_path / "ja--example.md"
    path.write_text(
        "---\n"
        "title: '日本語の題名'\n"
        "rationale: '這個中文欄位是編輯資料'\n"
        "---\n\n"
        "これは日本語ですが，那個段落は翻訳されていない。\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="ja")

    assert any("'那個'" in hit for hit in hits)


# ═══════════════ 書目區豁免（OBSERVER-QUEUE #23 選 A，2026-09-05）═══════════
#
# 背景：babel-nightly 620 筆裡 251 筆敗在同一處——參考資料區沒翻的中文來源
# 標題（`深度訪談`、`天下換日線`），其中含簡體來源（`维基百科`、
# `国家文化记忆库`）是另一回事。哲宇拍板選 A：書目區的正體來源標題放行，
# 簡體仍擋。以下 6 案例對應任務清單的最低要求（正文 leak 仍擋／腳註定義行
# 繁體標題放行／參考資料區繁體標題放行／參考資料區簡體擋／簡體出現在正文
# 擋／無 CJK 全綠），另加 2 案例驗證 translate.py 實際呼叫的生產閘門
# （detect_cjk_leak）跟 cjk-leak-check.py 的判準同步。


def test_body_leak_still_blocked_for_non_cjk_lang(tmp_path):
    """案例 1：正文中間夾雜未譯中文，跟書目無關——維持原本行為，仍擋。"""
    path = tmp_path / "en--example.md"
    path.write_text(
        "---\ntitle: 'Example'\n---\n\n"
        "TSMC built its fabs over decades, and 台灣半導體產業的發展歷程相當複雜"
        " remains untranslated in the middle of this sentence.\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="en")

    assert any("正文 CJK leak" in h for h in hits)


def test_footnote_def_line_traditional_title_allowed(tmp_path):
    """案例 2：單行腳註定義裡的正體來源標題（`[^n]: [標題](url) — 說明`）
    ——這是最常見的引用格式，本來就該放行（既有行為，非本次新增，但要跟新
    判準一起回歸測試，避免書目區重構把這條路弄壞）。"""
    path = tmp_path / "en--example.md"
    path.write_text(
        "---\ntitle: 'Example'\n---\n\n"
        "Little Tigers debuted in 1988[^1].\n\n"
        "## References\n\n"
        "[^1]: [小虎隊 - 維基百科](https://zh.wikipedia.org/zh-tw/小虎隊)"
        " — Wikipedia entry on the group's formation and breakup timeline.\n",
        encoding="utf-8",
    )

    assert MODULE.scan_file(path, lang="en") == []


def test_bibliography_section_traditional_title_allowed(tmp_path):
    """案例 3：參考資料區的正體來源標題放行——即使沒有走 `[^n]:` 腳註語法
    （舊式純文字條列），只要落在 References/參考資料 標題之後到檔尾，就算
    書目區。這是 #23 選 A 要解的最大宗失敗（620 筆裡 251 筆），修前會被
    CJK_RUN_RE 判成正文洩漏整篇擋下。"""
    path = tmp_path / "en--example.md"
    path.write_text(
        "---\ntitle: 'Example'\n---\n\n"
        "Overseas Taiwanese cannot vote by mail; they must return in person"
        " to cast a ballot[^1].\n\n"
        "## References\n\n"
        "- 台灣的不在籍投票爭議 — Crossing"
        " (https://crossing.cw.com.tw/article/12817):"
        " Current state of overseas voting rights.\n\n"
        "[^1]: 台灣的不在籍投票爭議 — Crossing"
        " (https://crossing.cw.com.tw/article/12817):"
        " Current state of overseas voting rights.\n",
        encoding="utf-8",
    )

    assert MODULE.scan_file(path, lang="en") == []


def test_bibliography_section_simplified_still_blocked(tmp_path):
    """案例 4：參考資料區出現簡體來源標題（`维基百科`）——即使落在書目區、
    即使整條腳註定義都在同一行（原本會被 strip_legit_zones 整行抹掉、完全
    偵測不到），仍要判 leak。這是修好「繁體放行」後最容易連帶放水的洞：
    書目區豁免只放寬正文/書目分區線，不放寬簡繁判準。"""
    path = tmp_path / "id--example.md"
    path.write_text(
        "---\ntitle: 'Example'\n---\n\n"
        "Larangan menyeberang ke Taiwan pernah diberlakukan secara ketat"
        " pada era kolonial[^1].\n\n"
        "## Referensi\n\n"
        "[^1]: [维基百科：台湾荷兰统治时期]"
        "(https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%8D%B7%E8%98%AD"
        "%E7%B5%B1%E6%B2%BB%E6%99%82%E6%9C%9F)"
        " — Entri Wikipedia tentang masa pemerintahan Belanda di Taiwan.\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="id")

    assert any("書目區簡體殘留" in h for h in hits)
    assert any("'维'" in h for h in hits)


def test_simplified_in_body_still_blocked(tmp_path):
    """案例 5：簡體字出現在正文（跟書目無關）——簡體字本身也是連續 4+ 漢字，
    既有的 CJK_RUN_RE 正文判準本來就會擋下，不需要靠 detect_simplified_residue
    (那支只管書目區)。這裡驗證書目區重構沒有意外把正文的判準也放寬。"""
    path = tmp_path / "en--example.md"
    path.write_text(
        "---\ntitle: 'Example'\n---\n\n"
        "The National Cultural Memory Bank documents this era, though"
        " 国家文化记忆库 remains untranslated here in the middle of the body.\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="en")

    assert any("正文 CJK leak" in h for h in hits)


def test_clean_file_no_cjk_passes(tmp_path):
    """案例 6：全文無 CJK、書目區也是正常單行正體腳註——全綠，沒有誤判。"""
    path = tmp_path / "ru--example.md"
    path.write_text(
        "---\ntitle: 'Golden Melody'\n---\n\n"
        "Golden Melody Award is Taiwan's most prestigious music award[^1].\n\n"
        "## Ссылки\n\n"
        "[^1]: [Golden Melody Award - Википедия]"
        "(https://zh.wikipedia.org/zh-tw/金曲獎)"
        " — Wikipedia entry on the award's history and structure.\n",
        encoding="utf-8",
    )

    assert MODULE.scan_file(path, lang="ru") == []


def test_bibliography_zone_ja_simplified_still_blocked(tmp_path):
    """加碼案例：ja/ko 分支用 marker 掃描正文，跟非 CJK 分支邏輯不同，但書目
    區簡體殘留檢查是兩分支共用的同一把尺——驗證 ja 也有這條保護。"""
    path = tmp_path / "ja--example.md"
    path.write_text(
        "---\ntitle: '例'\n---\n\n"
        "これは完全に日本語の本文です。\n\n"
        "## 参考資料\n\n"
        "[^1]: [维基百科：交工樂隊]"
        "(https://zh.wikipedia.org/zh-tw/交工樂隊) — 楽団の結成から解散までの記録。\n",
        encoding="utf-8",
    )

    hits = MODULE.scan_file(path, lang="ja")

    assert any("書目區簡體殘留" in h for h in hits)


def test_translate_detect_cjk_leak_matches_bibliography_policy(tmp_path):
    """驗證實際生產閘門 translate.py 的 detect_cjk_leak（babel-nightly 真正
    呼叫的那支）跟 cjk-leak-check.py 的書目區判準同步——不是兩套各自維護。"""
    text = (
        "---\ntitle: 'Example'\n---\n\n"
        "Overseas Taiwanese cannot vote by mail[^1].\n\n"
        "## References\n\n"
        "[^1]: 台灣的不在籍投票爭議 — Crossing"
        " (https://crossing.cw.com.tw/article/12817):"
        " Current state of overseas voting rights.\n"
    )

    assert TRANSLATE_MODULE.detect_cjk_leak(text, "en") is None


def test_translate_detect_cjk_leak_blocks_simplified_bibliography():
    text = (
        "---\ntitle: 'Example'\n---\n\n"
        "Larangan menyeberang ke Taiwan pernah diberlakukan secara ketat[^1].\n\n"
        "## Referensi\n\n"
        "[^1]: [维基百科：台湾荷兰统治时期]"
        "(https://zh.wikipedia.org/zh-tw/%E8%87%BA%E7%81%A3%E8%8D%B7%E8%98%AD"
        "%E7%B5%B1%E6%B2%BB%E6%99%82%E6%9C%9F)"
        " — Entri Wikipedia tentang masa pemerintahan Belanda di Taiwan.\n"
    )

    result = TRANSLATE_MODULE.detect_cjk_leak(text, "id")

    assert result is not None
    assert "書目區簡體殘留" in result
