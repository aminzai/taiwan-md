#!/usr/bin/env python3
"""routine-stall-check.py — 飛輪停轉告警，跑在第三處（GitHub Actions）。

## 為什麼存在

`flywheel-watch.py` 跑在指揮部這台、`routine-liveness-check.py` 跑在週日反思鏈裡，
兩者都依附飛輪自己的其中一台機器。2026-08-23 09:19 → 08-28 05:35，排程器停轉
4 天 20 小時，零告警——因為所有監看儀器都跟著飛輪一起睡著了（REFLEXES #82「儀器
只看見存在，看不見缺席」）。這支腳本設計成跑在兩台 mac 之外的第三處，只讀
GitHub Actions checkout 下來的 git 歷史與 repo 檔案，不依賴 scheduled-tasks MCP、
不依賴任何一台機器活著。完整診斷見
`reports/fortnight-deep-review-2026-09-05.md` §2.4、§4.2 D；
方向已寫在 `docs/semiont/ROUTINE.md` 註 ²⁵（alert-only：綠燈靜默，只在異常時推播）。

## 兩把尺

**尺一（全飛輪停轉）**：`git log` 裡最近一筆 subject 含 `[routine]` 的 commit 距今
超過 30 小時 → CRITICAL。只認 `[routine]`——`[semiont] memory: …` 是收官/手動
session 的標記，不是 routine 痕跡（flywheel-watch 首跑就校過這個假陽性）。

**尺二（週排程 miss）**：`docs/semiont/ROUTINE.md` 排程表裡「非 ⏸️ 且 cron 帶
day-of-week 欄位」的每條 routine（如 `0 2 * * 0`），機械算出它上一次應該 fire 的
時刻；那個時刻已經過了 30 小時，且 `docs/semiont/memory/` 找不到日期 ≥ 應 fire
日、檔名 handle 對得上（含 `TASKID_ALIASES` 別名）的檔 → WARN「錯過一趟」。
是否要檢查一條 routine，優先讀 `docs/semiont/routine-live-state.json` 的
`enabled`；那份檔讀不到才退回 ROUTINE.md 本身的 ⏸️ 標記（此時候選名單已經是
非 ⏸️ 的子集，等於直接照 SSOT 走）。

只判斷「有 day-of-week 欄位」的 cron（第 5 欄不是 `*`）。月排程（如
`30 10 5 * *`，第 3 欄日號、第 5 欄 `*`）不在尺二範圍內——沿用 flywheel-watch
「算不出來的不裝作知道」同一種誠實：混進日號展開需要另一套判準，這裡不假裝。

## Fail-loud

讀不到 `ROUTINE.md`、讀不到 `docs/semiont/memory/` 目錄、或 `git log` 本身失敗
→ exit 3，印原因到 stderr。**「讀不到」不是綠燈**（REFLEXES #85「不知道需要自己
的符號」）——工具本身壞掉跟「飛輪健康」是兩種不同的沉默，不能互相偽裝。

`routine-live-state.json` 讀不到則是另一種情況：規格明文把它列為「有退回路徑」
的輸入（退回 ROUTINE.md ⏸️），所以那不算 fail-loud，只在輸出附一行說明。

## 用法

    python3 scripts/tools/routine-stall-check.py
    python3 scripts/tools/routine-stall-check.py --json
    python3 scripts/tools/routine-stall-check.py --now 2026-08-26T12:00:00+08:00 --since-days 30

Exit code：0 綠燈；1 有 WARN；2 有 CRITICAL；3 工具本身壞掉（讀不到必要輸入）。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ROUTINE_SSOT = "docs/semiont/ROUTINE.md"
MEMORY_DIR = "docs/semiont/memory"
LIVE_STATE = "docs/semiont/routine-live-state.json"

TAIPEI = timezone(timedelta(hours=8))  # ROUTINE.md 排程表明寫「Cron (local +0800)」

RULE1_THRESHOLD_HOURS = 30
RULE2_THRESHOLD_HOURS = 30

# 重用 flywheel-watch.py 的別名表（同一份 SSOT 事實：taskId 跟 routine 實際簽名用的
# 語意名不總是同一個字）。只收 SSOT 自己寫明是同一條的別名，不做泛化。
TASKID_ALIASES = {
    "twmd-maintainer-am": "twmd-maintainer-daily",
}

TASKID_CELL_RE = re.compile(r"`(twmd-[a-z0-9-]+)`")
CRON_CELL_RE = re.compile(r"^`([-\d*/, ]+)`$")
MEMORY_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-\d{6}-(.+)\.md$")


def fail_loud(message: str) -> None:
    """讀不到必要輸入時的統一出口：印到 stderr、exit 3。不算綠燈。"""
    print(f"routine-stall-check: {message}（工具本身壞掉，不是綠燈）", file=sys.stderr)
    sys.exit(3)


def canonical_task_id(name: str) -> str:
    return TASKID_ALIASES.get(name, name)


def parse_now(raw: str | None) -> datetime:
    if raw is None:
        return datetime.now(timezone.utc)
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError as exc:
        fail_loud(f"--now 無法解析為 ISO8601：{raw!r}（{exc}）")
        raise  # 不會執行到，滿足型別檢查
    if dt.tzinfo is None:
        # 沒帶時區的輸入視為 Taipei 本地時間（ROUTINE.md 的 cron 本來就是這個時區）
        dt = dt.replace(tzinfo=TAIPEI)
    return dt


# ---------------------------------------------------------------------------
# 尺一：全飛輪停轉（commit 齡）
# ---------------------------------------------------------------------------


def check_rule1(now: datetime, since_days: int) -> dict:
    since_dt = now - timedelta(days=since_days)
    r = subprocess.run(
        [
            "git",
            "log",
            f"--since={since_dt.isoformat()}",
            f"--until={now.isoformat()}",
            "--format=%H|%ai|%s",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if r.returncode != 0:
        fail_loud(f"git log 失敗：{r.stderr.strip() or '未知錯誤'}")

    lines = [l for l in r.stdout.splitlines() if l.strip()]
    # maxsplit=2：subject 本身可能含 `|`（不太可能但別假設不會），只切前兩個
    routine_lines = [l for l in lines if "[routine]" in l.split("|", 2)[-1]]

    if not routine_lines:
        return {
            "status": "critical",
            "last_commit": None,
            "age_hours": None,
            "threshold_hours": RULE1_THRESHOLD_HOURS,
            "note": (
                f"過去 {since_days} 天內找不到任何 subject 含 [routine] 的 commit"
                "（下限未知，一定超過門檻——建議加大 --since-days 確認，但已視同全飛輪停轉）"
            ),
        }

    # git log 預設新到舊，第一筆就是（--until 邊界內）最近一筆
    commit_hash, commit_ai, subject = routine_lines[0].split("|", 2)
    commit_dt = datetime.strptime(commit_ai, "%Y-%m-%d %H:%M:%S %z")
    age_hours = (now - commit_dt).total_seconds() / 3600
    status = "critical" if age_hours > RULE1_THRESHOLD_HOURS else "ok"
    return {
        "status": status,
        "last_commit": {"hash": commit_hash, "at": commit_ai, "subject": subject},
        "age_hours": round(age_hours, 1),
        "threshold_hours": RULE1_THRESHOLD_HOURS,
    }


# ---------------------------------------------------------------------------
# 尺二：週排程 miss
# ---------------------------------------------------------------------------


def parse_weekly_candidates(routine_md_text: str) -> list[dict]:
    """機械解析 ROUTINE.md 排程表：非 ⏸️ 且 cron 帶 day-of-week 欄位的 routine。

    只吃「## 核心 routine 排程表」章節底下**第一個**連續的 `|` 表格區塊——章節裡
    後面還有一個「🪦 已退休」表格，裡面的 taskId（如 `twmd-maintainer-pm`）長得
    一模一樣但早就不該被檢查；用「第一個表格結束就停」把它擋在外面，不用再對
    退休表格另寫一套排除規則。
    """
    lines = routine_md_text.splitlines()
    heading_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("## 核心 routine 排程表"):
            heading_idx = i
            break
    if heading_idx is None:
        fail_loud(f"{ROUTINE_SSOT} 找不到「## 核心 routine 排程表」章節")

    rows, in_table = [], False
    for line in lines[heading_idx + 1 :]:
        stripped = line.strip()
        if stripped.startswith("|"):
            in_table = True
            rows.append(stripped)
            continue
        if in_table:
            break  # 第一個表格結束，不繼續吃後面的「🪦 已退休」表

    candidates = []
    for row in rows:
        cells = [c.strip() for c in row.strip("|").split("|")]
        if not cells:
            continue
        if set(cells[0]) <= {"-", " ", ":"}:
            continue  # markdown 表格分隔列
        m = TASKID_CELL_RE.search(cells[0])
        if not m:
            continue
        task_id = m.group(1)

        cron = None
        for c in cells:
            cm = CRON_CELL_RE.match(c)
            if cm and len(cm.group(1).split()) == 5:
                cron = cm.group(1).strip()
                break
        if not cron:
            continue

        dow = cron.split()[4]
        if dow == "*":
            continue  # 尺二只管 day-of-week 排程，月排程不在範圍內

        if "⏸️" in row:
            continue  # 非 ⏸️ 才是候選

        candidates.append({"task_id": task_id, "cron": cron})
    return candidates


def weekly_last_due(cron: str, now_local: datetime) -> datetime | None:
    """這條 day-of-week cron 上一次「應該」fire 的時刻（Taipei 本地時間）。

    邏輯照搬 flywheel-watch.py `last_due` 的 weekly 分支——算不出來回 None，
    不假裝知道（同一份誠實：cron 語意的 OR/範圍展開不在這支工具的野心裡）。
    """
    parts = cron.split()
    if len(parts) != 5:
        return None
    minute_s, hour_s, dom, _month, dow = parts
    if dow == "*" or dom != "*":
        return None
    try:
        minute, hour = int(minute_s), int(hour_s)
    except ValueError:
        return None
    try:
        wanted = {int(x) % 7 for x in re.split(r"[,\-]", dow) if x.strip().lstrip("-").isdigit()}
    except ValueError:
        return None
    if not wanted:
        return None
    for back in range(0, 8):
        d = now_local - timedelta(days=back)
        if d.isoweekday() % 7 in wanted:
            cand = d.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if cand <= now_local:
                return cand
    return None


def read_live_state() -> dict[str, bool] | None:
    """回傳 {taskId: enabled}；讀不到或壞掉回 None（呼叫端退回 ROUTINE.md ⏸️）。"""
    path = REPO_ROOT / LIVE_STATE
    try:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError):
        return None
    out = {}
    for t in data.get("tasks", []):
        tid = t.get("taskId")
        if tid:
            out[tid] = bool(t.get("enabled", True))
    return out


def memory_covers(
    task_id: str, due_date: date, now_date: date, memory_files: list[str]
) -> str | None:
    """`memory/` 裡有沒有 due_date ≤ 日期 ≤ now_date、handle 對得上（含別名）的檔。

    上界 `now_date` 是必要的：`--now` 回溯測試時，磁碟上的 `memory/` 是「現在」的
    完整內容，含有模擬時刻之後才寫的檔。只設下界（`file_date >= due_date`）會讓
    後續某次正常班（例如下週同一條 routine 準時 fire）被誤讀成「這次 miss 已經補上」——
    在正式生產環境（`--now` 用真實現在）這個上界是 no-op，只在回溯測試時生效。
    """
    aliases = {task_id, canonical_task_id(task_id)}
    aliases |= {alias for alias, canon in TASKID_ALIASES.items() if canon == task_id}
    for fname in memory_files:
        m = MEMORY_FILE_RE.match(fname)
        if not m:
            continue
        date_s, handle = m.groups()
        try:
            file_date = datetime.strptime(date_s, "%Y-%m-%d").date()
        except ValueError:
            continue
        if file_date < due_date or file_date > now_date:
            continue
        if handle in aliases or canonical_task_id(handle) in aliases:
            return fname
    return None


def check_rule2(
    candidates: list[dict],
    live_state: dict[str, bool] | None,
    memory_files: list[str],
    now_local: datetime,
) -> dict:
    checked, skipped = [], []
    for cand in candidates:
        task_id, cron = cand["task_id"], cand["cron"]

        if live_state is not None and live_state.get(task_id) is False:
            skipped.append({"task_id": task_id, "reason": "live-state disabled"})
            continue

        due = weekly_last_due(cron, now_local)
        if due is None:
            checked.append(
                {"task_id": task_id, "cron": cron, "status": "unknown-cron", "due_at": None}
            )
            continue

        hours_since_due = (now_local - due).total_seconds() / 3600
        entry = {
            "task_id": task_id,
            "cron": cron,
            "due_at": due.isoformat(),
            "hours_since_due": round(hours_since_due, 1),
        }
        if hours_since_due <= RULE2_THRESHOLD_HOURS:
            entry["status"] = "grace"
            checked.append(entry)
            continue

        covered_by = memory_covers(task_id, due.date(), now_local.date(), memory_files)
        entry["status"] = "ok" if covered_by else "warn"
        entry["covered_by"] = covered_by
        checked.append(entry)

    return {
        "threshold_hours": RULE2_THRESHOLD_HOURS,
        "checked": checked,
        "skipped": skipped,
        "live_state_fallback": live_state is None,
    }


# ---------------------------------------------------------------------------
# 組裝 + 輸出
# ---------------------------------------------------------------------------


def build_result(now: datetime, since_days: int) -> dict:
    routine_md_path = REPO_ROOT / ROUTINE_SSOT
    if not routine_md_path.is_file():
        fail_loud(f"讀不到 {ROUTINE_SSOT}")
    try:
        routine_md_text = routine_md_path.read_text(encoding="utf-8")
    except OSError as exc:
        fail_loud(f"{ROUTINE_SSOT} 讀取失敗：{exc}")

    memory_dir_path = REPO_ROOT / MEMORY_DIR
    if not memory_dir_path.is_dir():
        fail_loud(f"讀不到 {MEMORY_DIR}")
    try:
        memory_files = [p.name for p in memory_dir_path.iterdir() if p.suffix == ".md"]
    except OSError as exc:
        fail_loud(f"{MEMORY_DIR} 列目錄失敗：{exc}")

    rule1 = check_rule1(now, since_days)

    now_local = now.astimezone(TAIPEI)
    candidates = parse_weekly_candidates(routine_md_text)
    live_state = read_live_state()
    rule2 = check_rule2(candidates, live_state, memory_files, now_local)

    severity = "ok"
    if rule1["status"] == "critical":
        severity = "critical"
    if severity != "critical" and any(c["status"] == "warn" for c in rule2["checked"]):
        severity = "warn"

    return {
        "severity": severity,
        "checked_at": now.isoformat(),
        "since_days": since_days,
        "rule1_flywheel_commit_age": rule1,
        "rule2_weekly_schedule_miss": rule2,
    }


def human_report(result: dict) -> str:
    icon = {"ok": "✅", "warn": "⚠️ ", "critical": "🚨"}[result["severity"]]
    lines = [
        f"{icon} routine-stall-check — 尺一 commit 齡 + 尺二週排程 miss（閾值皆 {RULE1_THRESHOLD_HOURS}h）",
        f"檢查時刻：{result['checked_at']}",
        "",
    ]

    r1 = result["rule1_flywheel_commit_age"]
    lines.append("尺一（全飛輪停轉）")
    if r1["last_commit"]:
        flag = " 🚨 超過門檻" if r1["status"] == "critical" else ""
        lines.append(f"  最近一筆 [routine] commit：{r1['age_hours']}h 前（{r1['last_commit']['at']}）{flag}")
        lines.append(f"  {r1['last_commit']['subject']}")
    else:
        lines.append(f"  🚨 {r1['note']}")
    lines.append("")

    r2 = result["rule2_weekly_schedule_miss"]
    lines.append(
        f"尺二（週排程 miss，{len(r2['checked'])} 條檢查 / {len(r2['skipped'])} 條 skipped）"
    )
    if r2["live_state_fallback"]:
        lines.append(f"  ⚠️  {LIVE_STATE} 讀不到，enabled 判斷退回 ROUTINE.md 的 ⏸️ 標記")
    for c in r2["checked"]:
        if c["status"] == "warn":
            lines.append(
                f"  ⚠️  {c['task_id']} 錯過一趟 — 應 fire {c['due_at']}"
                f"（{c['hours_since_due']}h 前），memory/ 無對應檔"
            )
        elif c["status"] == "ok":
            lines.append(f"  ✅ {c['task_id']} 有對應 memory 檔（{c['covered_by']}）")
        elif c["status"] == "grace":
            lines.append(f"  🕐 {c['task_id']} 距上次應 fire {c['hours_since_due']}h，未過 {RULE2_THRESHOLD_HOURS}h 門檻")
        else:
            lines.append(f"  ？ {c['task_id']} cron `{c['cron']}` 算不出上次應 fire 時刻，未判定")
    for s in r2["skipped"]:
        lines.append(f"  ⏸️  {s['task_id']} skipped（{s['reason']}）")

    lines.append("")
    if result["severity"] == "ok":
        lines.append("✅ 綠燈")
    elif result["severity"] == "warn":
        lines.append("⚠️  有 WARN，需要人看一眼週排程是不是空場")
    else:
        lines.append("🚨 CRITICAL — 全飛輪可能停轉，先查營運機 Claude app 活著沒、額度有沒有到頂")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description="飛輪停轉告警：commit 齡 + 週排程 miss 雙尺")
    ap.add_argument("--json", action="store_true", help="輸出 JSON 而非人讀摘要")
    ap.add_argument(
        "--now",
        type=str,
        default=None,
        help="ISO8601（如 2026-08-26T12:00:00+08:00）；預設現在時刻。給測試與回溯用",
    )
    ap.add_argument(
        "--since-days",
        type=int,
        default=14,
        help="git log 掃描窗口天數（只限制尺一；尺二讀 memory/ 全目錄）",
    )
    args = ap.parse_args()

    now = parse_now(args.now)
    result = build_result(now, args.since_days)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(human_report(result))

    sys.exit({"ok": 0, "warn": 1, "critical": 2}[result["severity"]])


if __name__ == "__main__":
    main()
