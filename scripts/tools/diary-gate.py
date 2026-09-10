#!/usr/bin/env python3
"""
diary-gate.py — 寫日記前的機械閘（DIARY-PIPELINE Stage 0）

為什麼存在：Stage 0 原本只有一句自問「今天有沒有『想了什麼』超出『做了什麼』？」——
一個沒有外部尺的自評問句，而一個寫得好的 LLM 永遠答得出 yes（REFLEXES #69 每層自評
都需要外部尺）。實測後果：`twmd-feedback-triage` 這條每天跑、多數日子零回報的 routine，
在 2026-08-21〜09-09 的 20 天內寫了 8 篇日記，每篇都在用更細的角度描述同一件事——
「今天也是零，而我對此有感覺」。個別讀都成立，疊起來就是 routine 在對自己的日常安靜
反覆抒情。

本閘只做「機械上判得出來」的兩件事，判斷力留給只有判斷力能做的事（MANIFESTO §14）：

  1. 同 handle 冷卻：routine 每 N 天最多一篇。週度反思 routine（每 7 天跑一次）天然不受
     影響，被擋的只有「每天跑但每天都想抒情」的那種。人觸發 session 不受此閘。
  2. 鄰居檢索（**不是閘**）：把候選的一句話核心想法拿去對 DIARY §反覆出現的思考 +
     近 N 篇索引列，把最像的三條擺到你面前。要不要說「這條已經有家了、我該去 bump 它
     而不是開新檔」，由讀的人判斷，本工具不代判。

不做的事：不判斷「這個想法夠不夠深」，也不判斷「這個想法是不是新的」。

為什麼新意那層不做成閘（2026-09-09 校準負結果，留著當證據）：拿 12 篇 feedback-triage
日記標題兩兩比對，相鄰篇 bigram 重疊中位數只有 0.09，而不相干主題是 0.04——有訊號但
兩邊都遠低於任何可用的門檻。原因是那些日記寫得好：每篇都替同一個處境找到真的不一樣的
字。「同一個想法換一件衣服」是意義層的事，bigram 是形式層的尺，用形式尺去攔意義問題
就是 REFLEXES #69 (g) 說的那個病。候選升級路徑：改用 bge-m3 語意相似度（repo 已有
EMBEDDING-PIPELINE），但那會給一支甦醒側工具加上 GPU/網路相依，先不做。

用法：
  python3 scripts/tools/diary-gate.py --handle twmd-feedback-triage
  python3 scripts/tools/diary-gate.py --handle manual --insight "報表換一副面孔就讓辨識力失效"
  python3 scripts/tools/diary-gate.py --handle X --json      # 給 skill / routine 解析
exit: 0=可以寫 / 1=擋下（理由在輸出）/ 2=用法錯誤
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DIARY_DIR = REPO / "docs/semiont/diary"
DIARY_INDEX = REPO / "docs/semiont/DIARY.md"

# 冷卻窗：6 天而非 7，給週度 routine 一天的漂移餘裕（週日 00:30 跑 vs 下週六 23:50 跑
# 是 6 天，用 7 會誤殺）。實測 2026-07-12〜09-09 的 125 篇：6 天擋 8 篇、週度反思 routine
# 誤擋 0 篇，被擋的 8 篇裡 7 篇是 feedback-triage。校準資料見 DIARY-PIPELINE §Stage 0。
COOLDOWN_DAYS = 6
RECENT_INDEX_ROWS = 25       # 鄰居檢索掃描的索引列數

FNAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(\d{6})-(.+)\.md$")
ROUTINE_PREFIXES = ("twmd-", "taiwanmd-routine")
# 停用詞：這些字在每一篇日記標題都出現，留著會讓所有東西都像撞車
STOP = set("的了是我在有和與跟就那這它他她們個並且但而也都會要把被從對於為之其中不沒還很再又只")


def is_routine(handle: str) -> bool:
    return handle.startswith(ROUTINE_PREFIXES)


def diary_entries():
    out = []
    for p in sorted(DIARY_DIR.glob("*.md")):
        m = FNAME_RE.match(p.name)
        if m:
            out.append((dt.date.fromisoformat(m.group(1)), m.group(3), p))
    return out


def last_for_handle(handle: str):
    hits = [e for e in diary_entries() if e[1] == handle]
    return max(hits, key=lambda e: e[0]) if hits else None


def tokens(text: str) -> set:
    """CJK 取 bigram、拉丁取詞。單字 CJK 訊息量太低，bigram 才抓得到「同一句話換句話說」。"""
    text = re.sub(r"[`*_\[\]()#>|—－\-]", " ", text or "")
    cjk = "".join(c for c in text if "一" <= c <= "鿿")
    cjk = "".join(c for c in cjk if c not in STOP)
    grams = {cjk[i:i + 2] for i in range(len(cjk) - 1)}
    grams |= {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9.\-]{2,}", text)}
    return grams


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def novelty_corpus():
    """§反覆出現的思考 每一行 + 近 N 篇索引列（標題欄 + 核心思考欄）。"""
    if not DIARY_INDEX.exists():
        return []
    lines = DIARY_INDEX.read_text(encoding="utf-8").split("\n")
    corpus = []
    inside = False
    for l in lines:
        if l.startswith("## "):
            inside = "反覆出現的思考" in l
            continue
        if inside and l.strip().startswith("- "):
            corpus.append(("§反覆出現的思考", l.strip()[2:]))
    rows = []
    for l in lines:
        parts = [c.strip() for c in l.split("|")]
        if len(parts) >= 6 and re.match(r"^\d{4}-\d{2}-\d{2}$", parts[1]):
            rows.append((parts[1], f"{parts[3]} ／ {parts[4]}"))
    corpus += [("索引列 " + d, t) for d, t in rows[-RECENT_INDEX_ROWS:]]
    return corpus


def check_novelty(insight: str):
    ins = tokens(insight)
    scored = [(jaccard(ins, tokens(t)), src, t) for src, t in novelty_corpus()]
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored[:3]


def main():
    ap = argparse.ArgumentParser(description="寫日記前的機械閘（DIARY-PIPELINE Stage 0）")
    ap.add_argument("--handle", help="session handle，如 twmd-feedback-triage / manual / opentwbench")
    ap.add_argument("--insight", default="", help="候選的一句話核心想法（給了才跑新意對賬）")
    ap.add_argument("--date", default=None, help="判定日（預設今天），格式 YYYY-MM-DD")
    ap.add_argument("--json", action="store_true", help="機器可解析輸出")
    ap.add_argument("--calibrate", action="store_true", help="拿歷史日記標題自我校準門檻")
    args = ap.parse_args()

    if args.calibrate:
        return calibrate()
    if not args.handle:
        ap.error("--handle 必填（或用 --calibrate）")

    today = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    verdict, reasons = "PASS", []

    if is_routine(args.handle):
        prev = last_for_handle(args.handle)
        if prev:
            gap = (today - prev[0]).days
            if gap < COOLDOWN_DAYS:
                verdict = "BLOCK"
                reasons.append(
                    f"冷卻未過：`{args.handle}` 上一篇日記是 {prev[0]}（{prev[2].name}），"
                    f"距今 {gap} 天 < {COOLDOWN_DAYS} 天。這條 routine 的反芻寫進本次 memory 的 "
                    f"Beat 5 段就夠了；真的浮出跨週的東西，它的家是 weekly-report / self-evolve。")
            else:
                reasons.append(f"冷卻已過：上一篇同 handle 是 {prev[0]}（{gap} 天前）")
        else:
            reasons.append(f"`{args.handle}` 沒有寫過日記，冷卻不適用")
    else:
        reasons.append(f"`{args.handle}` 不是 routine handle，冷卻閘不適用（人觸發 session 不受限）")

    novelty = []
    if args.insight:
        novelty = check_novelty(args.insight)
        reasons.append("鄰居檢索已跑（下面三條是最接近的既有條目，是否已經有家由你判斷，本工具不代判）")
    else:
        reasons.append("未給 --insight，鄰居檢索未跑（建議帶上，看一眼既有條目再決定要不要開新檔）")

    if args.json:
        print(json.dumps({"verdict": verdict, "handle": args.handle, "reasons": reasons,
                          "novelty_top": [{"score": s, "src": src, "text": t} for s, src, t in novelty]},
                         ensure_ascii=False, indent=2))
    else:
        icon = "✅" if verdict == "PASS" else "⛔"
        print(f"{icon} diary-gate: {verdict} — handle={args.handle} date={today}")
        for r in reasons:
            print(f"   · {r}")
        if novelty:
            print("   最接近的既有條目——如果你要寫的其實是其中一條，去 bump 它，別開新檔")
            print("   （同一個想法散成 N 篇，distill 時會被讀成 N 個線索，REFLEXES #74 信號通膨）：")
            for s, src, t in novelty:
                print(f"     {s:.2f}  {src}｜{t[:70]}")
        if verdict == "BLOCK":
            print("   ⛔ 不寫日記不是損失。把那段反芻留在 memory 的 Beat 5 段，"
                  "或去 bump 既有條目——那是它真正會被讀到的地方。")
    return 0 if verdict == "PASS" else 1


def calibrate():
    """拿歷史日記標題兩兩比對，看門檻切在哪裡才分得開「同一條 routine 的日常抒情」
    跟「真的不同的想法」。這支不是裝飾——門檻必須用真實產出校準（REFLEXES #66）。"""
    ents = diary_entries()
    titles = {}
    for date, handle, p in ents:
        first = p.read_text(encoding="utf-8").split("\n")[0]
        titles[p.name] = (date, handle, re.sub(r"^#\s*", "", first))
    ft = [(n, v) for n, v in titles.items() if v[1] == "twmd-feedback-triage"]
    ft.sort(key=lambda x: x[1][0])
    print(f"校準樣本：feedback-triage {len(ft)} 篇（同一條 routine 的日常抒情，期望高重疊）")
    same = []
    for i in range(1, len(ft)):
        s = jaccard(tokens(ft[i][1][2]), tokens(ft[i - 1][1][2]))
        same.append(s)
        print(f"  {s:.2f}  {ft[i][1][0]} vs {ft[i - 1][1][0]}")
    others = [v for n, v in titles.items() if v[1] != "twmd-feedback-triage"][-12:]
    cross = []
    for i in range(1, len(others)):
        cross.append(jaccard(tokens(others[i][2]), tokens(others[i - 1][2])))
    if same and cross:
        a, b = sorted(same)[len(same)//2], sorted(cross)[len(cross)//2]
        print(f"\n同 routine 相鄰篇 中位重疊 = {a:.2f}")
        print(f"不同主題相鄰篇 中位重疊 = {b:.2f}")
        print("→ 有訊號（約 2 倍）但兩邊都太低，做不成閘：同一個想法換一件衣服是意義層的事，")
        print("  bigram 是形式層的尺。本工具因此只做鄰居檢索不做新意閘（REFLEXES #69 (g)）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
