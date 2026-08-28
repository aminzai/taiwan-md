#!/usr/bin/env python3
"""footnote-card-adoption.py — 腳註來源卡的採用漏斗，一個指令問完

為什麼存在：2026-08-28 腳註來源卡上線時，收官只留了一句「D+3 回頭看數字」的
handoff。那是自律不是閘門——`承諾的物理位置決定是否會被實現`（MEMORY §神經迴路
2026-04-17 δ）。這支工具把那個問題變成任何人任何時候一行就能問完的東西。

它回答四件事，全部是可證偽的：

  1. 有多少人在用          activeUsers on footnote_card_open
  2. 用哪種手勢            trigger = hover / click / focus 的比例
  3. 展開之後有沒有點出去  outbound_click(section=footnote_card) ÷ footnote_card_open
  4. 跟舊行為的對照        section_view(section=footnotes)＝還是只有滑到文末的人

第 3 條是這個功能存在的理由。上線前站上 17,113 條來源連結一個埋點都沒有，
所以「來源點擊率」歷史值是 0 筆資料不是 0 次點擊；這條線從 2026-08-28 起才有底。

事件去重規則（讀數字前要知道）：`footnote_card_open` 同一頁同一條腳註只送一次，
所以 eventCount = 讀者展開過幾條不同的來源，不是展開動作的次數。

用法:
  footnote-card-adoption.py                    # 近 7 天
  footnote-card-adoption.py --start 28daysAgo  # 自訂窗口
  footnote-card-adoption.py --json             # 給下游吃

退出碼: 0 有資料 / 1 窗口內零事件（上線初期正常，但連續多輪為零要當訊號查）

誕生：2026-08-28 footnote-cards session，reports/design-footnote-source-cards-2026-08-28.md
"""
import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib.sense_client import reexec_in_venv  # noqa: E402

reexec_in_venv()
from lib.sense_client import ga_run  # noqa: E402

OPEN_EVENT = "footnote_card_open"
CARD_SECTION = "footnote_card"
MARKER_SECTION = "footnote_marker"


def _rows(dims, metrics, start, end, dim_filter):
    try:
        return ga_run(dims, metrics, start, end, dim_filter=dim_filter)
    except Exception as e:  # noqa: BLE001 — 缺 creds / API 掛掉都不該讓呼叫端崩
        print(f"⚠️  GA4 查詢失敗：{type(e).__name__}: {e}", file=sys.stderr)
        return []


def _sum(rows, idx=0):
    total = 0
    for r in rows:
        try:
            total += int(r["mets"][idx])
        except (ValueError, IndexError, KeyError):
            pass
    return total


def collect(start, end):
    # 1. 展開卡片：總量 + 不重複使用者
    opened = _rows([], ["eventCount", "activeUsers"], start, end,
                   [("eventName", "exact", OPEN_EVENT)])
    open_count = int(opened[0]["mets"][0]) if opened else 0
    open_users = int(opened[0]["mets"][1]) if opened else 0

    # 2. 手勢拆解
    by_trigger = _rows(["customEvent:trigger"], ["eventCount"], start, end,
                       [("eventName", "exact", OPEN_EVENT)])
    triggers = {(r["dims"][0] or "(not set)"): int(r["mets"][0]) for r in by_trigger}

    # 3. 點出去：卡片上的來源連結
    out = _rows(["customEvent:section"], ["eventCount", "activeUsers"], start, end,
                [("eventName", "exact", "outbound_click")])
    card_out = next((r for r in out if r["dims"][0] == CARD_SECTION), None)
    out_count = int(card_out["mets"][0]) if card_out else 0
    out_users = int(card_out["mets"][1]) if card_out else 0

    # 4. 主動點記號（相對於滑過去的）
    clicks = _rows(["customEvent:section"], ["eventCount"], start, end,
                   [("eventName", "exact", "content_click")])
    marker_clicks = next(
        (int(r["mets"][0]) for r in clicks if r["dims"][0] == MARKER_SECTION), 0)

    # 5. 舊行為對照：滑到文末腳註區的人
    views = _rows(["customEvent:section"], ["eventCount"], start, end,
                  [("eventName", "exact", "section_view")])
    fn_section_view = next(
        (int(r["mets"][0]) for r in views if r["dims"][0] == "footnotes"), 0)

    pv = _rows([], ["screenPageViews"], start, end, None)
    pageviews = _sum(pv)

    return {
        "window": {"start": start, "end": end},
        "opened": {"events": open_count, "users": open_users},
        "triggers": triggers,
        "source_clicks": {"events": out_count, "users": out_users},
        "marker_clicks": marker_clicks,
        "footnotes_section_view": fn_section_view,
        "pageviews": pageviews,
    }


def _pct(n, d):
    return f"{n / d * 100:.1f}%" if d else "—"


def render(d):
    o, s = d["opened"], d["source_clicks"]
    print(f"🧬 腳註來源卡採用漏斗　{d['window']['start']} → {d['window']['end']}")
    print()
    print(f"  頁面瀏覽                      {d['pageviews']:>8,}")
    print(f"  滑到文末腳註區（舊路徑）      {d['footnotes_section_view']:>8,}"
          f"   {_pct(d['footnotes_section_view'], d['pageviews'])} of PV")
    print(f"  展開來源卡（新路徑）          {o['events']:>8,}"
          f"   {o['users']:,} 人")
    print(f"  ├─ 主動點記號                {d['marker_clicks']:>8,}")
    if d["triggers"]:
        total = sum(d["triggers"].values()) or 1
        for k, v in sorted(d["triggers"].items(), key=lambda x: -x[1]):
            print(f"  ├─ {k:<24}{v:>8,}   {_pct(v, total)}")
    print(f"  └─ 點開來源（新分頁）        {s['events']:>8,}"
          f"   {_pct(s['events'], o['events'])} 的展開有轉成點擊，{s['users']:,} 人")
    print()
    if o["events"] == 0:
        print("  ⚠️  窗口內零展開。上線初期正常；連續多輪為零要查埋點是不是斷了")
        print("     （先用 --realtime 確認 gtag 有載，再看 instrumentation-audit.py）")
    elif s["events"] == 0:
        print("  ⚠️  有人展開但零點擊。卡片被當成 tooltip 讀完就走，")
        print("     這是「讀者要的是內容不是來源」的訊號，不是 bug")
    else:
        print(f"  📌 這個比例是本功能唯一的可證偽點：{_pct(s['events'], o['events'])}")
        print("     上線前站上 17,113 條來源連結零埋點，所以沒有更早的基準可比")
    return 0 if o["events"] else 1


def main():
    ap = argparse.ArgumentParser(description="腳註來源卡採用漏斗")
    ap.add_argument("--start", default="7daysAgo")
    ap.add_argument("--end", default="today")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    d = collect(a.start, a.end)
    if a.json:
        print(json.dumps(d, ensure_ascii=False, indent=1))
        return 0 if d["opened"]["events"] else 1
    return render(d)


if __name__ == "__main__":
    sys.exit(main())
