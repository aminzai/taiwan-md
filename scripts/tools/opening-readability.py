#!/usr/bin/env python3
"""opening-readability.py — 量文章開場「讀不讀得下去」的三個機械面向。

誕生：2026-09-19 哲宇讀 9/18 上線的三篇（誰算低薪／油價機制／金鐘獎）說「文謅謅、
沒有人味、讀到第一段就不想看」。三篇全過 article-health、prose-health、15 位冷讀者、
三輪 release 主編——每一道閘門量的都是「對不對」，沒有一道量「想不想讀」。這把尺
把其中能機械化的三個面向抓出來（MANIFESTO §14 高儀器化，判斷力留給冷讀者）：

  1. 前 N 段的數字密度（每百個中文字幾個數字）
  2. 前 N 段的平均句長（中文字／句）
  3. 口徑限定詞在前 N 段重複幾次（本國籍全時受僱員工／經常性薪資／稅前批售價 這類
     為了防冷讀者「哪個口徑」而長出來的詞）

口徑（2026-09-19 統一）：先剝掉 [^n] 腳註標記再數，年份也算數字。humanize brief 病灶表量到的
黃魚鴞 4.2 是連腳註數字一起算的舊口徑，本工具的 1.5 才是現行口徑。
基準線由範本定，不發明數字：哲宇點名喜歡的五篇在這把尺上——黃魚鴞 1.5／31 字、嚴長壽 0.4／27、
陳樹菊 1.4／19、居住正義 0.8／38、國宅與居住正義 3.6／28。WARN ＝ 範本上緣（數字 3.6／百字、句長 38），
HARD ＝ 範本上緣 × 1.3（4.7／49）。口徑限定詞 4 次 WARN、6 次 HARD。哲宇讀第一段仍是最終尺，儀器只擋明顯的。

用法：
  python3 scripts/tools/opening-readability.py knowledge/Society/誰算低薪.md [--paras 4] [--json]
  python3 scripts/tools/opening-readability.py a.md b.md c.md      # 多檔並列比較

Exit code：0 = 在基準內；1 = 任一面向超出 WARN；2 = 任一面向超出 HARD。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WARN_NUM_PER_100 = 3.6
HARD_NUM_PER_100 = 4.7
WARN_AVG_SENT = 38
HARD_AVG_SENT = 49
WARN_QUALIFIERS = 4
HARD_QUALIFIERS = 6

QUALIFIER_RE = re.compile(
    r"本國籍全時受僱員工|全時受僱|經常性薪資|非經常性薪資|口徑|稅前批售價|批售價|"
    r"獎勵要點|年度）|第 ?\d+ ?屆|分母|統計上|依定義|依法|所稱"
)
SKIP_PREFIX = ("#", ">", "```", "![", "_", "*", "|", "[^", "<")


def body_paragraphs(text: str) -> list[str]:
    parts = text.split("\n---\n", 1)
    body = parts[1] if len(parts) > 1 else text
    paras: list[str] = []
    in_fence = False
    for block in body.split("\n\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith("```"):
            in_fence = not in_fence if b.count("```") % 2 else in_fence
            continue
        if in_fence or b.startswith(SKIP_PREFIX):
            continue
        paras.append(b)
    return paras


def measure(path: Path, n_paras: int) -> dict:
    text = path.read_text(encoding="utf-8")
    paras = body_paragraphs(text)[:n_paras]
    joined = "".join(paras)
    joined_nofn = re.sub(r"\[\^\d+\]", "", joined)
    cjk = len(re.findall(r"[一-鿿]", joined_nofn))
    nums = len(re.findall(r"\d[\d,\.]*", joined_nofn))
    sents = [s for s in re.split(r"[。！？]", joined_nofn) if s.strip()]
    sent_lens = [len(re.findall(r"[一-鿿]", s)) for s in sents]
    avg_sent = sum(sent_lens) / len(sent_lens) if sent_lens else 0.0
    quals = len(QUALIFIER_RE.findall(joined_nofn))
    num_per_100 = nums / cjk * 100 if cjk else 0.0
    warns = []
    hards = []
    if num_per_100 > HARD_NUM_PER_100:
        hards.append(f"數字密度 {num_per_100:.1f}/百字 > {HARD_NUM_PER_100}")
    elif num_per_100 > WARN_NUM_PER_100:
        warns.append(f"數字密度 {num_per_100:.1f}/百字 > {WARN_NUM_PER_100}")
    if avg_sent > HARD_AVG_SENT:
        hards.append(f"平均句長 {avg_sent:.0f} 字 > {HARD_AVG_SENT}")
    elif avg_sent > WARN_AVG_SENT:
        warns.append(f"平均句長 {avg_sent:.0f} 字 > {WARN_AVG_SENT}")
    if quals >= HARD_QUALIFIERS:
        hards.append(f"口徑限定詞 {quals} 次 ≥ {HARD_QUALIFIERS}")
    elif quals >= WARN_QUALIFIERS:
        warns.append(f"口徑限定詞 {quals} 次 ≥ {WARN_QUALIFIERS}")
    return {
        "file": str(path),
        "paras": len(paras),
        "cjk": cjk,
        "numbers": nums,
        "num_per_100": round(num_per_100, 1),
        "avg_sentence": round(avg_sent, 0),
        "longest_sentence": max(sent_lens) if sent_lens else 0,
        "qualifiers": quals,
        "warns": warns,
        "hards": hards,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--paras", type=int, default=4, help="量前幾段（預設 4）")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    results = [measure(Path(f), args.paras) for f in args.files]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"{'檔案':<28} {'字':>5} {'數字/百字':>8} {'句長':>5} {'最長句':>6} {'口徑詞':>6}  判定")
        for r in results:
            name = Path(r["file"]).stem[:14]
            flag = ("❌ " + "；".join(r["hards"])) if r["hards"] else (("⚠️ " + "；".join(r["warns"])) if r["warns"] else "✅")
            print(
                f"{name:<28} {r['cjk']:>5} {r['num_per_100']:>8} {r['avg_sentence']:>5.0f} "
                f"{r['longest_sentence']:>6} {r['qualifiers']:>6}  {flag}"
            )
    if any(r["hards"] for r in results):
        return 2
    return 1 if any(r["warns"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
