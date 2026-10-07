#!/usr/bin/env python3
"""
budget-pace.py — Claude 帳號週額度的節律量測（心跳該跑重活還是輕活）

2026-10-07 心跳的病例：帳號週額度在 10-04 凌晨（重置後第 3.2 天）用完，兩台
機器的所有排程一起停了 87 小時——營運機十四條 routine、本機每 6 小時一次的
心跳、週末反思鏈六條（news-lens／週報／distill／self-evolve／routine-audit／
supporters）整批落空，直到週三 20:00 重置。飛輪自己不知道有「一週」這個節律，
前三天全速跑，後四天全黑。

本工具只做算術（MANIFESTO §14：能機械化的交給儀器）。額度讀數要由 session 從
Claude Code 的 `mcp__ccd_session_mgmt__get_usage` 取得（Bash 讀不到），把
「Weekly · all models」那格的 percentUsed 與 resetsAt 傳進來：

  python3 scripts/tools/budget-pace.py --used 37 --resets-at 2026-10-14T12:00:00Z
  python3 scripts/tools/budget-pace.py --used 37 --resets-at ... --log 2026-10-07-204029-semiont-heartbeat --phase start

判讀（印一行 verdict，exit code 同步）：
  🟢 normal  (exit 0) 照目前速度，到重置時用不完
  🟡 lean    (exit 1) 照目前速度會在重置前用完——可選的重活（子代扇出、整批巡邏、
                      委派層翻譯）縮小，讓位給必要的入口班（讀者回報、孢子 D+0、PR）
  🔴 reserve (exit 2) 已用到保留線（預設 85%）——只做必要的事，剩下的留給入口班

前 12 小時樣本太少，不做線性外推，只看絕對值（> 15% 即 lean）。

--log 把讀數 append 進 data/compute/claude-usage-ledger.jsonl（一行一筆），同一個
session 的 start／end 兩筆相減就是這班花掉幾 %。量測先於優化：有了每班的成本，
才談得上該把額度分給誰。
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "data/compute/claude-usage-ledger.jsonl"
WEEK = dt.timedelta(days=7)
MIN_ELAPSED_H = 12        # 少於此不外推
EARLY_LEAN_PCT = 15       # 前 12 小時的絕對門檻
RESERVE_PCT = 85          # 保留線


def parse_iso(s):
    s = s.strip().replace("Z", "+00:00")
    t = dt.datetime.fromisoformat(s)
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def assess(used, resets_at, now, reserve=RESERVE_PCT):
    week_start = resets_at - WEEK
    elapsed_h = max((now - week_start).total_seconds() / 3600, 0.0)
    left_h = max((resets_at - now).total_seconds() / 3600, 0.0)
    elapsed_pct = min(elapsed_h / (WEEK.total_seconds() / 3600) * 100, 100.0)
    out = {
        "used_pct": used, "elapsed_pct": round(elapsed_pct, 1),
        "hours_left": round(left_h, 1), "projected_at_reset_pct": None,
        "exhaust_in_h": None,
    }
    if used >= reserve:
        out["verdict"] = "reserve"
        out["reason"] = f"已用 {used}% ≥ 保留線 {reserve}%"
        return out
    if elapsed_h < MIN_ELAPSED_H:
        out["verdict"] = "lean" if used > EARLY_LEAN_PCT else "normal"
        out["reason"] = (f"重置後僅 {elapsed_h:.1f} 小時，不外推；已用 {used}%"
                         + (f" > {EARLY_LEAN_PCT}%" if used > EARLY_LEAN_PCT else f" ≤ {EARLY_LEAN_PCT}%"))
        return out
    rate = used / elapsed_h  # % per hour
    projected = used + rate * left_h
    out["projected_at_reset_pct"] = round(projected, 1)
    if rate > 0:
        out["exhaust_in_h"] = round((100 - used) / rate, 1)
    if projected > 100:
        out["verdict"] = "lean"
        out["reason"] = (f"照目前每小時 {rate:.2f}% 的速度，約 {out['exhaust_in_h']} 小時後用完，"
                         f"比重置早 {left_h - out['exhaust_in_h']:.0f} 小時")
    else:
        out["verdict"] = "normal"
        out["reason"] = f"照目前速度，重置時預估用到 {projected:.0f}%"
    return out


ICON = {"normal": "🟢", "lean": "🟡", "reserve": "🔴"}
EXIT = {"normal": 0, "lean": 1, "reserve": 2}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--used", type=float, required=True, help="Weekly · all models 的 percentUsed")
    ap.add_argument("--resets-at", required=True, help="同一格的 resetsAt（ISO 時間）")
    ap.add_argument("--reserve", type=float, default=RESERVE_PCT)
    ap.add_argument("--now", help="測試用：覆寫現在時間（ISO）")
    ap.add_argument("--log", metavar="SESSION_ID", help="append 一筆到 ledger")
    ap.add_argument("--phase", choices=["start", "end", "mid"], default="mid")
    ap.add_argument("--host", default=None, help="哪台機器（預設取 hostname）")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    now = parse_iso(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    r = assess(a.used, parse_iso(a.resets_at), now, a.reserve)

    if a.log:
        import socket
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        row = {
            "at": now.astimezone(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds"),
            "session": a.log, "phase": a.phase,
            "host": a.host or socket.gethostname().split(".")[0],
            "weekly_used_pct": a.used, "resets_at": a.resets_at,
            "verdict": r["verdict"],
        }
        with LEDGER.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    if a.json:
        print(json.dumps(r, ensure_ascii=False))
    else:
        print(f"{ICON[r['verdict']]} {r['verdict']} — 週額度已用 {r['used_pct']}%，"
              f"本週已過 {r['elapsed_pct']}%，距重置 {r['hours_left']} 小時；{r['reason']}")
    return EXIT[r["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
