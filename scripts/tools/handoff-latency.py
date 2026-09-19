#!/usr/bin/env python3
"""handoff-latency.py — 量 memory §Handoff 的交接項目在幾班之間被原樣傳遞、幾天才被做掉。

用法：
  python3 scripts/tools/handoff-latency.py                 # 近 45 天，印開放項目排行＋分佈
  python3 scripts/tools/handoff-latency.py --days 90       # 換窗口
  python3 scripts/tools/handoff-latency.py --min-carry 5   # 只印被傳 ≥5 班的
  python3 scripts/tools/handoff-latency.py --json          # 機器可讀（給 dashboard / weekly-report-prep）

量的是什麼：
  一條 handoff 項目（`- [ ] pending（…）— 內容`）從第一次出現到最後一次出現，
  被多少個 session 的 §Handoff 原樣帶下去（carry），存活幾天（age），最後有沒有被
  收掉（[x] / ~~ / retired）。傳遞本身不是病，傳了 N 班沒人做才是。

為什麼存在：
  REFLEXES #15 #13（deferred-fix-lands-on-recurrence-not-on-reading）＋ DIARY 09-10 / 09-13 /
  09-19 / 09-20 四班獨立寫到「handoff 傳得動動作、傳不動決定」「決定被準確地交給下一個人」
  「登記不是進度」。同一句話浮現 ≥4 次，此前沒有任何儀器在數「一條交接要幾輪才被做掉」。
  wake-context 保證下一班讀得到 handoff；本工具量讀到之後有沒有人動。
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] if (Path(__file__).resolve().parents[1].name == "tools") else Path.cwd()
MEMORY_DIR = ROOT / "docs" / "semiont" / "memory"

FILE_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
HANDOFF_HEAD_RE = re.compile(r"^##+ .*(Handoff|handoff|交接)")
BULLET_RE = re.compile(r"^\s*[-*]\s+(.*)$")

REF_QUEUE_RE = re.compile(r"OBSERVER-QUEUE\s*#(\d{1,3})")
REF_QUEUE_CTX_RE = re.compile(r"OBSERVER-QUEUE\s*$")
REF_ISSUE_RE = re.compile(r"(?<![\w#])#(\d{3,5})\b")
REF_EXP_RE = re.compile(r"EXP-\d{4}-\d{2}-\d{2}-[\w]+")
REF_SLUG_RE = re.compile(r"`([a-z][a-z0-9]+(?:-[a-z0-9]+){2,})`")

RETIRED_MARKERS = ("[x]", "~~", "retired", "已解", "已做", "done")
BLOCKED_MARKERS = ("⏳", "blocked")


def parse_date(s: str) -> dt.date:
    return dt.datetime.strptime(s, "%Y-%m-%d").date()


def handoff_bullets(text: str) -> list[str]:
    lines = text.split("\n")
    s = next((i for i, l in enumerate(lines) if HANDOFF_HEAD_RE.match(l)), None)
    if s is None:
        return []
    e = next((j for j in range(s + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
    out = []
    for l in lines[s + 1:e]:
        m = BULLET_RE.match(l)
        if m:
            out.append(m.group(1).strip())
    return out


def classify(bullet: str) -> str:
    head = bullet[:40].lower()
    if any(k in head for k in RETIRED_MARKERS) or bullet.startswith("~~") or bullet.startswith("[x]"):
        return "retired"
    if any(k in head for k in BLOCKED_MARKERS):
        return "blocked"
    return "pending"


STRIP_RE = re.compile(r"^(\[[ x]\]|~~|⏳|✅|❌|🔒)+\s*")
LEAD_RE = re.compile(r"^(pending|blocked|retired|done)?\s*（[^）]*）\s*[—\-–:：]?\s*", re.I)
MD_RE = re.compile(r"[`*_~\[\]()（）【】「」『』<>]|https?://\S+")
PUNCT_RE = re.compile(r"[\s,.;:!?，。；：！？、／/|—–\-]+")


RETIRE_TAIL_RE = re.compile(r"(~~\s*[—\-–]|—\s*retired|retired by|—\s*本 ?session|—\s*本班|—\s*已 ?ship|✅).*$", re.I)


def normalize(bullet: str) -> str:
    b = STRIP_RE.sub("", bullet)
    b = LEAD_RE.sub("", b)
    b = RETIRE_TAIL_RE.sub("", b)
    b = b.replace("~~", "")
    b = MD_RE.sub("", b)
    b = PUNCT_RE.sub("", b)
    return b


def bigrams(s: str) -> set[str]:
    s = s.lower()
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) > 1 else {s}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=45)
    ap.add_argument("--min-carry", type=int, default=3, help="排行只印 carry ≥ N 的開放項")
    ap.add_argument("--threshold", type=float, default=0.5, help="同一項目的字元 2-gram Jaccard 門檻")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=15)
    args = ap.parse_args()

    if not MEMORY_DIR.exists():
        print(f"❌ 找不到 {MEMORY_DIR}", file=sys.stderr)
        return 2

    cutoff = dt.date.today() - dt.timedelta(days=args.days)
    files = sorted(
        p for p in MEMORY_DIR.glob("*.md")
        if FILE_DATE_RE.match(p.name) and p.name != "structure-log.md"
        and parse_date(FILE_DATE_RE.match(p.name).group(1)) >= cutoff
    )

    # clusters: list of dict(key_bigrams, sample, first, last, sessions:set, states:list[(date, state)])
    clusters: list[dict] = []
    total_bullets = 0
    sessions_with_handoff = 0
    for p in files:
        fdate = parse_date(FILE_DATE_RE.match(p.name).group(1))
        bullets = handoff_bullets(p.read_text(encoding="utf-8", errors="replace"))
        if not bullets:
            continue
        sessions_with_handoff += 1
        seen_in_file: set[int] = set()
        for b in bullets:
            norm = normalize(b)
            if len(norm) < 8:
                continue
            total_bullets += 1
            bg = bigrams(norm[:80])
            state = classify(b)
            best, best_i = 0.0, -1
            for i, c in enumerate(clusters):
                if i in seen_in_file:
                    continue
                j = jaccard(bg, c["bg"])
                if j > best:
                    best, best_i = j, i
            if best >= args.threshold:
                c = clusters[best_i]
                c["sessions"].add(p.name)
                c["last"] = max(c["last"], fdate)
                c["states"].append((fdate, state, p.name))
                c["days"].add(fdate)
                seen_in_file.add(best_i)
            else:
                clusters.append({
                    "bg": bg, "sample": b[:200], "first": fdate, "last": fdate,
                    "sessions": {p.name}, "days": {fdate}, "states": [(fdate, state, p.name)],
                })
                seen_in_file.add(len(clusters) - 1)

    today = dt.date.today()

    # 第二層：用穩定參照（issue/PR #N、OBSERVER-QUEUE #N、EXP-id、`slug-with-dashes`）追蹤，
    # 不受改寫影響——同一件事被三班各自換句話寫，2-gram 黏不住，但 #1729 黏得住。
    refs: dict[str, dict] = {}
    for p in files:
        fdate = parse_date(FILE_DATE_RE.match(p.name).group(1))
        for b in handoff_bullets(p.read_text(encoding="utf-8", errors="replace")):
            state = classify(b)
            keys = set()
            for m in REF_QUEUE_RE.finditer(b):
                keys.add(f"OBSERVER-QUEUE #{m.group(1)}")
            for m in REF_ISSUE_RE.finditer(b):
                if not REF_QUEUE_CTX_RE.search(b[max(0, m.start() - 20):m.start()]):
                    keys.add(f"#{m.group(1)}")
            for m in REF_EXP_RE.finditer(b):
                keys.add(m.group(0))
            for m in REF_SLUG_RE.finditer(b):
                slug = m.group(1)
                if slug.startswith("twmd-") or slug.endswith((".py", ".sh", ".mjs", ".json", ".md")):
                    continue  # routine 名與檔名不是交接項目的身分
                keys.add(slug)
            for k in keys:
                r = refs.setdefault(k, {"first": fdate, "last": fdate, "sessions": set(), "days": set(),
                                        "states": [], "sample": b[:160]})
                r["first"] = min(r["first"], fdate)
                r["last"] = max(r["last"], fdate)
                r["sessions"].add(p.name)
                r["days"].add(fdate)
                r["states"].append((fdate, state))
    ref_rows = []
    for k, r in refs.items():
        last_open = max((d for d, st in r["states"] if st != "retired"), default=None)
        last_ret = max((d for d, st in r["states"] if st == "retired"), default=None)
        final = "retired" if last_ret and (last_open is None or last_ret >= last_open) else \
            ("blocked" if all(st == "blocked" for d, st in r["states"] if d == r["last"]) else "pending")
        ref_rows.append({"ref": k, "first": r["first"].isoformat(), "last": r["last"].isoformat(),
                         "carry": len(r["sessions"]), "days": len(r["days"]),
                         "span_days": (r["last"] - r["first"]).days, "final": final,
                         "stale_days": (today - r["last"]).days, "sample": r["sample"]})
    ref_open = sorted([r for r in ref_rows if r["final"] != "retired" and r["days"] >= 2],
                      key=lambda r: (-r["span_days"], -r["days"]))
    ref_retired = [r for r in ref_rows if r["final"] == "retired"]

    rows = []
    for c in clusters:
        last_open = max((d for d, st, _ in c["states"] if st != "retired"), default=None)
        last_retired = max((d for d, st, _ in c["states"] if st == "retired"), default=None)
        if last_retired and (last_open is None or last_retired >= last_open):
            final_state = "retired"
        else:
            final_state = sorted(c["states"])[-1][1]
        carry = len(c["sessions"])
        age = (c["last"] - c["first"]).days
        rows.append({
            "sample": c["sample"], "first": c["first"].isoformat(), "last": c["last"].isoformat(),
            "carry": carry, "days": len(c["days"]), "age_days": age, "final": final_state,
            "stale_days": (today - c["last"]).days,
        })

    open_rows = [r for r in rows if r["final"] != "retired"]
    retired_rows = [r for r in rows if r["final"] == "retired"]
    multi = [r for r in rows if r["carry"] >= 2]

    def median(xs):
        xs = sorted(xs)
        return xs[len(xs) // 2] if xs else 0

    summary = {
        "window_days": args.days,
        "sessions_with_handoff": sessions_with_handoff,
        "bullets": total_bullets,
        "items": len(rows),
        "carried_items": len(multi),
        "retired_items": len(retired_rows),
        "open_items": len(open_rows),
        "median_carry_to_retire": median([r["carry"] for r in retired_rows]),
        "median_age_to_retire_days": median([r["age_days"] for r in retired_rows]),
        "open_carry_ge_min": len([r for r in open_rows if r["carry"] >= args.min_carry]),
        "max_open_carry": max([r["carry"] for r in open_rows], default=0),
        "ref_tracked": len(ref_rows),
        "ref_open_multi_day": len(ref_open),
        "ref_retired": len(ref_retired),
        "ref_median_span_to_retire_days": median([r["span_days"] for r in ref_retired]),
        "ref_median_days_to_retire": median([r["days"] for r in ref_retired]),
        "ref_open_span_ge_14": len([r for r in ref_open if r["span_days"] >= 14]),
    }
    ranked = sorted(open_rows, key=lambda r: (-r["days"], -r["carry"]))

    if args.json:
        print(json.dumps({"summary": summary, "open_top": ranked[:args.top], "ref_open_top": ref_open[:args.top]},
                         ensure_ascii=False, indent=2))
        return 0

    print(f"📨 handoff 交接延遲（近 {args.days} 天，{sessions_with_handoff} 班有 §Handoff，{total_bullets} 條交接行 → {len(rows)} 個項目）")
    print(f"   被傳 ≥2 班：{len(multi)}　已收掉：{len(retired_rows)}（收掉前中位 carry {summary['median_carry_to_retire']} 班／{summary['median_age_to_retire_days']} 天）　仍開放：{len(open_rows)}")
    print(f"   仍開放且 carry ≥{args.min_carry}：{summary['open_carry_ge_min']}　最長 carry：{summary['max_open_carry']} 班")
    print()
    print(f"最久沒人動的開放交接（carry ≥{args.min_carry}，依天次 / carry 排）：")
    shown = 0
    for r in ranked:
        if r["carry"] < args.min_carry:
            break
        shown += 1
        if shown > args.top:
            break
        tag = "⏳" if r["final"] == "blocked" else "📌"
        print(f"  {tag} carry {r['carry']:>2} 班／{r['days']:>2} 天次 · 跨 {r['age_days']:>3} 天 · {r['first']}→{r['last']} · {r['sample'][:100]}")
    if shown == 0:
        print("  （無）")
    print()
    print(f"依穩定參照追蹤（issue/PR #N、OBSERVER-QUEUE #N、EXP、`slug`；改寫也黏得住）：")
    print(f"   追到 {len(ref_rows)} 個參照　跨 ≥2 天仍開放：{len(ref_open)}（其中跨 ≥14 天：{summary['ref_open_span_ge_14']}）　已收掉：{len(ref_retired)}"
          f"（收掉前中位跨 {summary['ref_median_span_to_retire_days']} 天／{summary['ref_median_days_to_retire']} 天次）")
    for r in ref_open[:args.top]:
        tag = "⏳" if r["final"] == "blocked" else "📌"
        print(f"  {tag} {r['ref']:<22} 跨 {r['span_days']:>3} 天 · {r['days']:>2} 天次／{r['carry']:>2} 班 · {r['first']}→{r['last']}（距今 {r['stale_days']} 天）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
