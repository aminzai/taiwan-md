"""status.py classify()：截斷閘（2026-09-22）。provenance 三個 hash 全對但全檔 bytes 比例 < 0.5 的譯文
過去被判 fresh、從此沒有任何路徑再碰它（babel-health 量到 11 份 fresh 卻 CRITICAL）。"""
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync"))
MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "tools" / "lang-sync" / "status.py"
SPEC = importlib.util.spec_from_file_location("lang_sync_status", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _zh(**kw):
    base = {"lastCommit": "abc1234", "contentHash": "sha256:aa", "bodyHash": "sha256:bb", "footnoteDefs": 0, "bytes": 12000}
    base.update(kw)
    return base


def _tr(**kw):
    base = {"translatedFrom": "About/x.md", "sourceCommitSha": "abc1234", "sourceContentHash": "sha256:aa",
            "sourceBodyHash": "sha256:bb", "footnoteDefs": 0, "bytes": 12000}
    base.update(kw)
    return base


def test_truncated_translation_is_forced_stale_even_with_matching_provenance():
    r = MODULE.classify(_zh(), _tr(bytes=2000))
    assert r["status"] == "stale" and r["reason"].startswith("truncated")


def test_footnote_loss_gate_still_fires_first():
    r = MODULE.classify(_zh(footnoteDefs=5), _tr(bytes=2000, footnoteDefs=3))
    assert r["reason"].startswith("footnote-loss")


def test_missing_bytes_fields_do_not_trigger_gate(monkeypatch):
    # 舊 status cache 沒有 bytes 欄位時不誤判（0 不算）
    monkeypatch.setattr(MODULE, "git_commits_between", lambda *a, **k: 0)
    monkeypatch.setattr(MODULE.Path, "exists", lambda self: True)
    r = MODULE.classify(_zh(bytes=0), _tr(bytes=0))
    assert r["status"] == "fresh"


def test_armor_residue_is_forced_stale_even_with_matching_provenance():
    """裝甲殘留閘（2026-09-23）：三條引擎都把網址換成佔位符再換回來，換不回來時
    佔位符印給讀者看，而三個 hash 照樣對得上 → 永遠 fresh。判 stale 讓產線重翻，
    不在原地猜原始網址。"""
    r = MODULE.classify(_zh(), _tr(armorResidue=3))
    assert r["status"] == "stale" and r["reason"].startswith("armor-residue")


def test_armor_residue_regex_catches_both_engine_shapes():
    """整篇引擎是 ⟦U12⟧、分段與 patch 引擎是 @@LINK3@@——只認一種等於只擋一條引擎。
    而且只認**開括號**：第一版要求形狀完整（`⟦...⟧`），當天就被 vi 黃大煒篇打臉，
    那兩個 iframe 的 src 是 `⟦U1⟪`，模型把收尾括號換成別的符號就穿過去了。"""
    hits = MODULE.ARMOR_RESIDUE_RE.findall(
        "正文 ⟦U12⟧ 與 [text](@@LINK3@@) 還有 ⟦Un⟧、以及壞掉的 ⟦U1⟪")
    assert len(hits) == 4
    assert MODULE.ARMOR_RESIDUE_RE.findall("乾淨的譯文沒有任何佔位符") == []
