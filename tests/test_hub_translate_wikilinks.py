"""hub-translate.py 的 wikilink_targets 修復回歸測試（2026-09-05）。

病根：`hub-translate.py` 從誕生起 `wikilink_targets` 一律傳 `{}`，`armor_pre()`
因此永遠組不出 wikilink 指引段，模型對 Hub 檔裡的 `[[X]]` 沒有任何目標可查
（de Culture Hub 30 個、People Hub 113 個 hard wikilink-target-not-found）。
修復後 `hub-translate.py` 比照 `prepare-batch.py` 現場組 zh→{lang} 索引 +
`lookup_wikilink_target()`，本檔驗證：

(a) `build_wikilink_targets()` 對「已有譯文」與「沒有譯文」的 wikilink 組出
    正確的 target_map（前者是 `/lang/...` 路徑、後者是 prepare-batch 同款
    zh-only 提示字串——不是 None，也不是被省略的 key）。
(b) 組出的 `wikilink_targets` 傳進 `armor_pre()` 後，回傳的 system prompt
    真的含有 wikilink 指引段（`armor_pre()` 沒有另外回傳 wikilink_note，
    只斷言它出現在組好的 system 字串裡）。
"""
import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LANG_SYNC_DIR = REPO / "scripts" / "tools" / "lang-sync"

# translate.py 的 `backends` / `structured-translate` 是相對於 lang-sync 目錄的
# local import，只有該目錄進了 sys.path 才 import 得到（同源 test_cjk_leak_check.py
# 的既有做法）。
sys.path.insert(0, str(LANG_SYNC_DIR))


def _load(name: str, fname: str):
    spec = importlib.util.spec_from_file_location(name, LANG_SYNC_DIR / fname)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


HUB_TRANSLATE = _load("hub_translate_under_test", "hub-translate.py")
PREPARE_BATCH = HUB_TRANSLATE.pb  # 同一個 prepare-batch 模組實例，供 monkeypatch KNOWLEDGE
TRANSLATE = HUB_TRANSLATE.tr


def test_build_wikilink_targets_resolves_known_and_marks_zh_only(tmp_path, monkeypatch):
    """假 Hub 內容含一個「有 vi 譯文」跟一個「沒有 vi 譯文」的 wikilink，
    `build_wikilink_targets()` 要能各自組出對的值——不能像修復前那樣一律 {}。"""
    fake_knowledge = tmp_path / "knowledge"
    (fake_knowledge / "Culture").mkdir(parents=True)
    zh_path = "Culture/_Culture Hub.md"
    (fake_knowledge / zh_path).write_text(
        "---\n"
        "title: 假 Culture Hub\n"
        "description: 測試用\n"
        "---\n\n"
        "本文提到 [[已有 vi 譯文的條目]] 跟 [[沒有譯文的條目]] 兩個連結。\n",
        encoding="utf-8",
    )

    # extract_wikilinks()/lookup_wikilink_target() 都是 prepare-batch.py 既有函式，
    # 只是它們的檔案 I/O 走模組層級的 KNOWLEDGE 常數——monkeypatch 成暫存目錄，
    # 讓測試不必碰真正的 knowledge/。
    monkeypatch.setattr(PREPARE_BATCH, "KNOWLEDGE", fake_knowledge)

    zh_to_lang_idx = {
        "已有 vi 譯文的條目.md": "vi/Culture/da-cheng-yi-you-yi-wen.md",
    }

    target_map = HUB_TRANSLATE.build_wikilink_targets(zh_path, zh_to_lang_idx)

    assert target_map["已有 vi 譯文的條目"] == "/vi/Culture/da-cheng-yi-you-yi-wen/"
    # prepare-batch.py 的既有慣例：沒解析到的 target 不是 None、也不是被省略的
    # key，是明確的 zh-only 提示字串，讓 armor_pre() 用 `startswith("/")` 判斷。
    assert target_map["沒有譯文的條目"] == "(zh only — convert to plain text + Chinese parenthesis)"


def test_wikilink_targets_reach_armor_pre_prompt():
    """組好的 wikilink_targets 傳進 armor_pre() 後，system prompt 裡要出現
    wikilink 指引段——修復前傳空 dict，armor_pre() 完全不會組這段。"""
    zh_content = (
        "---\n"
        "title: 假 Hub\n"
        "description: 測試用\n"
        "---\n\n"
        "本文提到 [[已有 vi 譯文的條目]] 跟 [[沒有譯文的條目]] 兩個連結。\n"
    )
    wikilink_targets = {
        "已有 vi 譯文的條目": "/vi/Culture/da-cheng-yi-you-yi-wen/",
        "沒有譯文的條目": "(zh only — convert to plain text + Chinese parenthesis)",
    }
    article = {
        "zh_path": "Culture/_Culture Hub.md",
        "status": "missing",
        "en_path": "knowledge/vi/Culture/_Culture Hub.md",
        "slug": "_Culture Hub",
        "wikilink_targets": wikilink_targets,
    }

    system, _user, _ctx = TRANSLATE.armor_pre(article, zh_content, "vi")

    assert "WIKILINK TARGETS" in system
    assert "已有 vi 譯文的條目 → /vi/Culture/da-cheng-yi-you-yi-wen/" in system
    assert "沒有譯文的條目 → (zh only" in system
