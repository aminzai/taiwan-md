"""footnote-url 要量得到參考資料區的普通清單網址。

2026-10-08 心跳：〈台灣官方網站資源〉的參考資料是 `- [標題](網址)` 清單、沒有 [^N] 腳註，
其中一條 404，本檢查回報 hard=0 warn=0。網路呼叫一律換成假的，測試不打外網。
"""

from pathlib import Path

from lib.article_health.checks import footnote_url
from lib.article_health.loader import load_target

DEAD = "https://dead.example.org/history"
ALIVE = "https://alive.example.org/"


def _fake_check(url, timeout=5.0):
    if url.startswith("https://dead."):
        return (False, 404, "")
    return (True, 200, "")


def _target(tmp_path: Path, body: str):
    path = tmp_path / "sample.md"
    path.write_text("---\ntitle: 'x'\n---\n\n" + body, encoding="utf-8")
    return load_target(path)


def _run(target, monkeypatch):
    monkeypatch.setattr(footnote_url, "_check_url", _fake_check)
    return list(footnote_url.check(target, {"network": True}))


def test_plain_reference_list_urls_are_checked(tmp_path, monkeypatch):
    target = _target(
        tmp_path,
        "正文。\n\n## 參考資料\n\n"
        f"- [活的來源]({ALIVE})\n"
        f"- [死的來源]({DEAD})\n",
    )
    vs = _run(target, monkeypatch)
    assert len(vs) == 1
    assert vs[0].snippet == DEAD
    assert vs[0].message.startswith("參考資料 URL")


def test_list_urls_outside_references_section_are_not_checked(tmp_path, monkeypatch):
    # 文末資源清單、延伸閱讀不在這把尺的範圍：只量參考資料區
    target = _target(
        tmp_path,
        f"## 完整資源清單\n\n- [死的入口]({DEAD})\n\n"
        f"## 參考資料\n\n- [活的來源]({ALIVE})\n\n"
        f"## 延伸閱讀\n\n- [另一個死的]({DEAD}/x)\n",
    )
    assert _run(target, monkeypatch) == []


def test_footnote_definitions_still_checked_and_deduped(tmp_path, monkeypatch):
    target = _target(
        tmp_path,
        "正文[^1]。\n\n## 參考資料\n\n"
        f"[^1]: [死的腳註]({DEAD}) — 描述。\n"
        f"- [同一個死網址]({DEAD})\n",
    )
    vs = _run(target, monkeypatch)
    assert len(vs) == 1
    assert vs[0].message.startswith("腳註 URL")


def test_disabled_without_network_flag(tmp_path, monkeypatch):
    monkeypatch.delenv("ARTICLE_HEALTH_NETWORK", raising=False)
    target = _target(tmp_path, f"## 參考資料\n\n- [死的來源]({DEAD})\n")
    monkeypatch.setattr(footnote_url, "_check_url", _fake_check)
    assert list(footnote_url.check(target, {})) == []
