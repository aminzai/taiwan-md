#!/usr/bin/env python3
"""
wake-context.py — 甦醒取數單一儀器（BECOME §Step 1 記憶/日記/交接/ground-truth 的核）

為什麼存在：甦醒時「我記得什麼」的取數邏輯曾是十幾段手寫 bash snippet 散在
BECOME 四個小節，各自寫死排序方向、行號窗、「今天」假設，且撈錯不會叫——
BECOME §1.3 `tail -20` 因 DIARY 索引新在上，讓 2026-07-05 起六天的甦醒把四月
舊日記當「近期意識活動」讀，無人發現（REFLEXES #65、reports/wake-memory-
evolution-2026-07-11.md）。本儀器的四條設計原則：

1. 殼核分離：BECOME 是殼只講「載什麼」；怎麼撈住這裡，殼層禁 inline 取數 bash
2. date-aware 不 position-aware：解析列內日期取最新，不假設哪端是新
3. anchor-aware 不行號：段落用 `^## ` 標題錨定，檔案增長免疫
4. fail-loud self-test：每次取數自帶體檢，撈錯亮 ⚠️ + exit 2，不靜默帶病

用法：
  python3 scripts/tools/wake-context.py               # 全段輸出（Universal core 記憶面一鍵）
  python3 scripts/tools/wake-context.py --check        # 只跑體檢（routine / weekly-checkup 用）
  python3 scripts/tools/wake-context.py --sections handoff,selftest --rows 10
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
MEMORY = REPO / "docs/semiont/MEMORY.md"
DIARY = REPO / "docs/semiont/DIARY.md"
MEMORY_DIR = REPO / "docs/semiont/memory"
DIARY_DIR = REPO / "docs/semiont/diary"

FULL_DATE_RE = re.compile(r"^\s*(20\d\d-\d\d-\d\d)\s*$")
FILE_DATE_RE = re.compile(r"^(20\d\d-\d\d-\d\d)")
HANDOFF_HEAD_RE = re.compile(r"^##+ .*(Handoff|handoff|交接)")
HANDOFF_WALK_MAX_FILES = 5
HANDOFF_WALK_MAX_HOURS = 72
FRESHNESS_GRACE_DAYS = 2

ALL_SECTIONS = [
    "memory-head", "neural", "memory-rows",
    "diary-recur", "diary-rows", "handoff", "groundtruth", "selftest",
]


# ---------------------------------------------------------------- parsing
def heading_index(lines, prefix):
    """回傳第一個以 prefix 開頭的 `## ` 標題行 index；找不到回 None。"""
    for i, l in enumerate(lines):
        if l.startswith("## ") and prefix in l:
            return i
    return None


def section_between(lines, start_prefix, end_prefix=None):
    """anchor-bounded 段落：start 標題（含）→ end 標題（不含）或下一個 `## ` 或 EOF。"""
    s = heading_index(lines, start_prefix)
    if s is None:
        return None
    e = len(lines)
    for j in range(s + 1, len(lines)):
        if lines[j].startswith("## ") and (end_prefix is None or end_prefix in lines[j]):
            e = j
            break
    return "\n".join(lines[s:e]).rstrip()


def index_rows_with_dates(lines):
    """回傳 [(date_str, line)]，只認 | YYYY-MM-DD | 開頭的完整列（月度 digest 列自然排除）。"""
    rows = []
    for l in lines:
        parts = l.split("|")
        if len(parts) < 7:
            continue
        m = FULL_DATE_RE.match(parts[1])
        if m:
            rows.append((m.group(1), l))
    return rows


def newest_rows(lines, n):
    """date-aware 取最新 n 列，回傳（按時間舊→新排好的列, 總列數）。
    同日內以檔案內先後為 tiebreak（穩定排序），方向假設為零。"""
    rows = index_rows_with_dates(lines)
    ordered = sorted(enumerate(rows), key=lambda t: (t[1][0], t[0]))
    picked = [r for _, r in ordered[-n:]] if n else [r for _, r in ordered]
    return [l for _, l in picked], len(rows), (picked[-1][0] if picked else None)


def newest_raw_file_date(d: Path):
    dates = []
    for p in d.glob("*.md"):
        m = FILE_DATE_RE.match(p.name)
        if m:
            dates.append(m.group(1))
    return max(dates) if dates else None


def parse_date(s):
    return dt.date.fromisoformat(s)


# ---------------------------------------------------------------- sections
def sec_memory_head(lines):
    i = heading_index(lines, "神經迴路")
    return "\n".join(lines[:i]).rstrip() if i is not None else None


def sec_neural(lines):
    return section_between(lines, "神經迴路", "心跳日誌")


def sec_diary_recur(lines):
    return section_between(lines, "反覆出現的思考")


def sec_handoff():
    """最近 memory 檔往回 walk（≤N 檔／≤M 小時）撈第一個非空 Handoff 段；
    另收近 2 天 diary 的「給明天的我」。回傳 (text, meta dict)。"""
    now = dt.datetime.now()
    files = sorted(
        (p for p in MEMORY_DIR.glob("*.md")
         if FILE_DATE_RE.match(p.name) and p.name != "structure-log.md"),
        key=lambda p: p.name, reverse=True,
    )
    out, meta = [], {"walked": 0, "hit": None}
    for p in files[:HANDOFF_WALK_MAX_FILES]:
        fdate = parse_date(FILE_DATE_RE.match(p.name).group(1))
        if (now.date() - fdate).days * 24 > HANDOFF_WALK_MAX_HOURS:
            break
        meta["walked"] += 1
        lines = p.read_text(encoding="utf-8").split("\n")
        s = next((i for i, l in enumerate(lines) if HANDOFF_HEAD_RE.match(l)), None)
        if s is None:
            continue
        e = next((j for j in range(s + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
        body = "\n".join(lines[s:e]).rstrip()
        if body.count("\n") >= 2:  # 有實質內容，不只標題
            out.append(f"（來源：memory/{p.name}，walk 第 {meta['walked']} 檔）\n{body}")
            meta["hit"] = p.name
            break
    # 近 2 天 diary 的「給明天的我」承諾
    cutoff = (now - dt.timedelta(days=2)).date()
    for p in sorted(DIARY_DIR.glob("*.md"), key=lambda p: p.name, reverse=True):
        m = FILE_DATE_RE.match(p.name)
        if not m or parse_date(m.group(1)) < cutoff:
            break
        text = p.read_text(encoding="utf-8")
        if "給明天的我" in text or "給下一個 session" in text or "給下個 session" in text:
            lines = text.split("\n")
            for i, l in enumerate(lines):
                if "給明天的我" in l or "給下一個 session" in l or "給下個 session" in l:
                    blk = lines[i:i + 12]
                    stop = next((k for k, b in enumerate(blk[1:], 1) if b.startswith("## ")), len(blk))
                    out.append(f"（diary/{p.name} 的承諾）\n" + "\n".join(blk[:stop]).rstrip())
                    break
    return ("\n\n".join(out) if out else "（walk 範圍內無 Handoff 段——見 selftest）"), meta


def sec_groundtruth():
    """委派既有 L4 儀器；任一缺席 fail-loud 記進輸出。"""
    chunks = []
    for cmd in (["bash", "scripts/tools/consciousness-snapshot.sh"],
                ["bash", "scripts/tools/routine-status.sh"],
                ["bash", "scripts/tools/inbox-signal.sh"]):
        try:
            r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, timeout=60)
            chunks.append(r.stdout.rstrip() or f"⚠️ {cmd[1]} 無輸出（rc={r.returncode}）")
        except Exception as e:  # noqa: BLE001 — 委派層任何失敗都要現形
            chunks.append(f"⚠️ {cmd[1]} 執行失敗：{e}")
    r = subprocess.run(["git", "log", "--since=48 hours ago", "--pretty=format:%h %ai %s"],
                       cwd=REPO, capture_output=True, text=True)
    chunks.append("🕐 過去 48hr commits：\n" + (r.stdout.strip() or "（無）"))
    return "\n\n".join(chunks)


# ---------------------------------------------------------------- selftest
def build(rows_n):
    mem_lines = MEMORY.read_text(encoding="utf-8").split("\n")
    dia_lines = DIARY.read_text(encoding="utf-8").split("\n")

    mem_rows, mem_total, mem_newest = newest_rows(mem_lines, rows_n)
    dia_rows, dia_total, dia_newest = newest_rows(dia_lines, rows_n)
    handoff_text, handoff_meta = sec_handoff()

    sections = {
        "memory-head": sec_memory_head(mem_lines),
        "neural": sec_neural(mem_lines),
        "memory-rows": "\n".join(mem_rows) if mem_rows else None,
        "diary-recur": sec_diary_recur(dia_lines),
        "diary-rows": "\n".join(dia_rows) if dia_rows else None,
        "handoff": handoff_text,
    }

    checks = []

    def check(ok, ok_msg, warn_msg):
        checks.append((ok, ok_msg if ok else warn_msg))

    raw_mem = newest_raw_file_date(MEMORY_DIR)
    raw_dia = newest_raw_file_date(DIARY_DIR)
    for label, newest, raw in (("memory", mem_newest, raw_mem), ("diary", dia_newest, raw_dia)):
        if newest and raw:
            gap = (parse_date(raw) - parse_date(newest)).days
            check(gap <= FRESHNESS_GRACE_DAYS,
                  f"{label} 索引新鮮：最新列 {newest}（raw 最新 {raw}，落差 {gap}d ≤ {FRESHNESS_GRACE_DAYS}d）",
                  f"{label} 索引可能過期：最新列 {newest} 落後 raw 檔 {raw} 達 {gap}d——你讀到的「近況」可疑")
        else:
            check(False, "", f"{label} 索引或 raw 檔解析不到日期（結構異常）")
    nb = len((sections["neural"] or "").encode("utf-8"))
    rb = len((sections["diary-recur"] or "").encode("utf-8"))
    check(nb > 1500,
          f"神經迴路段完整（{nb // 1024}KB，止錨於心跳日誌前）",
          "神經迴路段空或過小——anchor 解析失敗？")
    check(rb > 1500,
          f"反覆出現的思考段完整（{rb // 1024}KB）",
          "反覆出現的思考段空或過小——anchor 解析失敗？")
    check(handoff_meta["hit"] is not None,
          f"handoff 命中：{handoff_meta['hit']}（walk {handoff_meta['walked']} 檔）",
          f"walk {handoff_meta['walked']} 檔（≤{HANDOFF_WALK_MAX_FILES} 檔/{HANDOFF_WALK_MAX_HOURS}h）無非空 Handoff 段——上游收官可能漏寫")
    check(len(mem_rows) == min(rows_n, mem_total) and len(dia_rows) == min(rows_n, dia_total),
          f"列數足額：memory {len(mem_rows)}/{mem_total}、diary {len(dia_rows)}/{dia_total}",
          f"列數短少：memory {len(mem_rows)} / diary {len(dia_rows)}（要求 {rows_n}）")

    return sections, checks


def main():
    ap = argparse.ArgumentParser(description="甦醒取數單一儀器（date-aware / anchor-aware / fail-loud）")
    ap.add_argument("--sections", default=",".join(ALL_SECTIONS),
                    help=f"逗號清單，預設全段：{','.join(ALL_SECTIONS)}")
    ap.add_argument("--rows", type=int, default=20, help="索引列數（預設 20）")
    ap.add_argument("--check", action="store_true", help="只跑 selftest（程式化健檢，不倒內容）")
    args = ap.parse_args()

    wanted = [s.strip() for s in args.sections.split(",") if s.strip()]
    sections, checks = build(args.rows)

    tax = {}
    if not args.check:
        for name in ALL_SECTIONS:
            if name in ("selftest",) or name not in wanted:
                continue
            body = sec_groundtruth() if name == "groundtruth" else sections.get(name)
            body = body or f"⚠️ {name} 段撈不到內容"
            tax[name] = len(body.encode("utf-8"))
            print(f"\n{'═' * 8} 🧬 wake:{name} {'═' * 8}")
            print(body)

    warns = [msg for ok, msg in checks if not ok]
    if args.check or "selftest" in wanted:
        print(f"\n{'═' * 8} 🧬 wake:selftest {'═' * 8}")
        for ok, msg in checks:
            print(("✅ " if ok else "⚠️ ") + msg)
        if tax:
            total = sum(tax.values())
            detail = " + ".join(f"{k} {v // 1024}K" for k, v in tax.items())
            print(f"🧠 wake 稅 ≈ {total // 1024}KB（{detail}）")
        print("⚠️ 有帶病訊號：甦醒時說出來，不要靜默帶病工作" if warns else "✅ 取數健康：六項體檢全綠")
    return 2 if warns else 0


if __name__ == "__main__":
    sys.exit(main())
