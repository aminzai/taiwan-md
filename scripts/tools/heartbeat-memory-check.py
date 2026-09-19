#!/usr/bin/env python3
"""
heartbeat-memory-check.py — 抓「有刷新 commit、沒有 memory 檔」的半途停機心跳

背景（2026-09-19 晚間 heartbeat 交接單）：
  14:30 那一輪心跳留下兩個 commit（dashboard 刷新 `33295b6ad`、索引 rollup `4bca24324`）
  之後就沒有了——沒有 memory 檔、沒有索引列。routine-liveness-check.py 的尺是
  「fire 後有沒有 commit」，這種「有 commit、沒收官」的形狀它量不到；memory-index-lint
  量的是「memory 檔有沒有進索引」，檔案根本沒寫它也看不見。兩把尺中間空出一格：
  心跳做了事、沒記，等於沒做（MANIFESTO §7），而且沒有任何東西會叫。

判準：
  每一個 `🧬 [semiont] heartbeat:` 刷新 commit（heartbeat 的第一動作）之後 WINDOW 小時內，
  應該出現一個 `🧬 [semiont] memory: semiont-heartbeat @` 收官 commit。
  距今 < GRACE 小時的刷新不判（session 可能還在跑）。

判定：
  ✅ closed     刷新後 WINDOW 內有收官 memory commit
  🕐 in-grace   刷新距今 < GRACE，不判
  🔴 orphan     刷新距今 ≥ GRACE 且 WINDOW 內零 memory commit

用法：
  python3 scripts/tools/heartbeat-memory-check.py            # 人讀表，預設看 7 天
  python3 scripts/tools/heartbeat-memory-check.py --days 14
  python3 scripts/tools/heartbeat-memory-check.py --json
  退出碼：0 全綠 / 2 有 orphan
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

REFRESH_TAG = "🧬 [semiont] heartbeat:"
MEMORY_TAG = "🧬 [semiont] memory: semiont-heartbeat"
GRACE_HOURS = 3.0
WINDOW_HOURS = 4.0


def _commits(days: int) -> list[tuple[str, datetime, str]]:
    out = subprocess.run(
        ["git", "log", f"--since={days} days ago", "--format=%h%x09%aI%x09%s", "--all"],
        capture_output=True, text=True, check=True,
    ).stdout
    rows = []
    for line in out.splitlines():
        h, iso, subj = line.split("\t", 2)
        rows.append((h, datetime.fromisoformat(iso), subj))
    return rows


def check(days: int, grace: float, window: float) -> list[dict]:
    rows = _commits(days)
    refreshes = [r for r in rows if r[2].startswith(REFRESH_TAG)]
    memories = [r for r in rows if r[2].startswith(MEMORY_TAG)]
    now = datetime.now(timezone.utc)
    result = []
    for h, t, subj in sorted(refreshes, key=lambda r: r[1]):
        age_h = (now - t).total_seconds() / 3600
        closer = next(
            (m for m in sorted(memories, key=lambda r: r[1])
             if t < m[1] <= t + timedelta(hours=window)),
            None,
        )
        if closer:
            status = "closed"
        elif age_h < grace:
            status = "in-grace"
        else:
            status = "orphan"
        result.append({
            "refresh": h, "at": t.isoformat(), "age_hours": round(age_h, 1),
            "status": status, "memory": closer[0] if closer else None,
            "subject": subj[len(REFRESH_TAG):].strip(),
        })
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--grace", type=float, default=GRACE_HOURS)
    ap.add_argument("--window", type=float, default=WINDOW_HOURS)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = check(a.days, a.grace, a.window)
    orphans = [r for r in rows if r["status"] == "orphan"]
    if a.json:
        print(json.dumps({"rows": rows, "orphans": len(orphans)}, ensure_ascii=False, indent=1))
    else:
        icon = {"closed": "✅", "in-grace": "🕐", "orphan": "🔴"}
        print(f"heartbeat 刷新 → 收官 memory 對賬（近 {a.days} 天，grace {a.grace}h / window {a.window}h）")
        for r in rows:
            when = r["at"][:16].replace("T", " ")
            mem = f"→ memory {r['memory']}" if r["memory"] else "→ 無收官 memory commit"
            print(f"  {icon[r['status']]} {when}  {r['refresh']}  {r['subject'][:22]}  {mem}")
        print(f"  刷新 {len(rows)} 次 / orphan {len(orphans)}")
    return 2 if orphans else 0


if __name__ == "__main__":
    sys.exit(main())
