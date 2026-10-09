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


def test_h3_heading_and_numbered_list_are_checked(tmp_path, monkeypatch):
    # 2026-10-09 晚間心跳：〈台灣全齡共融旅遊與生活文化〉寫成 `### 參考資料 / Sources`
    # 底下的 `1. [標題](網址)`，舊尺只認 `## 參考資料` 與 `-`／`*` 清單，十條一條都沒量
    target = _target(
        tmp_path,
        "正文。\n\n### 參考資料 / Sources\n\n"
        f"1. [活的來源]({ALIVE})\n"
        f"2. [死的來源]({DEAD})\n",
    )
    vs = _run(target, monkeypatch)
    assert [v.snippet for v in vs] == [DEAD]


def test_redirect_to_homepage_counts_as_unreachable():
    # 內政部、國健署把下架內頁轉回首頁，回 200
    assert footnote_url._redirected_home(
        "https://www.moi.gov.tw/News_Content.aspx?n=9&s=322560",
        "https://www.moi.gov.tw/default.aspx",
    )
    assert footnote_url._redirected_home(
        "https://www.hpa.gov.tw/Pages/List.aspx?nodeid=3869",
        "https://www.hpa.gov.tw/Home/Index.aspx",
    )


def test_ordinary_redirects_are_not_homepage():
    # http→https、首頁轉首頁、內頁轉另一個內頁都不算
    assert not footnote_url._redirected_home("http://www.goodtours.com.tw/", "https://www.goodtours.com.tw/")
    assert not footnote_url._redirected_home(
        "https://youtube.com/shorts/DedWMkt1zq4", "https://www.youtube.com/shorts/DedWMkt1zq4"
    )
    assert not footnote_url._redirected_home(
        "https://example.org/old/page", "https://example.org/index.php?id=12"
    )
