#!/usr/bin/env python3
"""numeral-magnitude-check.py — 抓「量級詞換了、數字沒換」的譯文。

為什麼要這支：2026-09-09《夜市經濟學》的印地文版每一個數字都錯。譯者把中文的
「萬」「億」直接替換成印度的 लाख／अरब，但那不是一對一——萬是 10⁴ 而 लाख 是 10⁵，
億是 10⁸ 而 अरब 是 10⁹。「4000 億產值」寫成 `4 अरब`（差 100 倍）、「23.3 萬攤」
寫成 `23.3 लाख`（差 10 倍）。九道閘全綠，因為它們量的是結構、語言、連結，
**沒有一道在算術**。印尼文版同病兩處，而且同一篇裡對錯並存。

判準（單一、機械、保守）：
  中文原文出現 `N萬` 或 `N億` 時，正確的換算**一定會改變數字串**
  （23.3萬 → 2.33 लाख；4000億 → 400 अरब；93.9億 → 9.39 अरब）。
  所以「**同一個數字串 N 出現在譯文的量級詞旁邊**」就是這個錯的指紋。

  反過來不成立的情況已排除：
  · 年份、編號、百分比、頁碼 —— 它們不接量級詞，不會命中
  · 譯文用「原數字＋原單位」寫法（如保留「萬」字）—— 那是 cjk-leak 的守備範圍
  · 譯文把數字完全展開寫（233,000）—— 數字串不同，不命中

用法：
  python3 scripts/tools/lang-sync/numeral-magnitude-check.py <zh 原文> <譯文>
  python3 scripts/tools/lang-sync/numeral-magnitude-check.py --lang hi   # 掃整個語言
exit 1 = 有可疑的量級。這支是**線索產生器不是裁決者**：命中要人看一眼，
因為譯文可能刻意保留原數字做對照（那種寫法罕見但合法）。
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"

# 各語言的量級詞。值是 10 的次方，用來在報告裡算出正確數字。
MAGNITUDE = {
    "hi": {"हज़ार": 3, "हजार": 3, "लाख": 5, "करोड़": 7, "अरब": 9, "खरब": 11},
    "id": {"ribu": 3, "juta": 6, "miliar": 9, "triliun": 12},
    "ru": {"тысяч": 3, "миллион": 6, "миллиард": 9, "триллион": 12},
    "ar": {"ألف": 3, "آلاف": 3, "مليون": 6, "مليار": 9, "تريليون": 12},
    "es": {"mil": 3, "millón": 6, "millones": 6, "mil millones": 9},
    "pt": {"mil": 3, "milhão": 6, "milhões": 6, "bilhão": 9, "bilhões": 9},
    "fr": {"mille": 3, "million": 6, "milliard": 9},
    "de": {"tausend": 3, "million": 6, "milliarde": 9},
    "en": {"thousand": 3, "million": 6, "billion": 9, "trillion": 12},
    "vi": {"nghìn": 3, "ngàn": 3, "triệu": 6, "tỷ": 9},
}
ZH_MAG = {"萬": 4, "億": 8, "兆": 12, "千": 3}
ZH_NUM = re.compile(r"([0-9][0-9,.]*)\s*([萬億兆])")


def zh_figures(zh_text: str) -> list[tuple[str, float, str]]:
    """回傳 [(原數字串, 實際數值, 中文單位)]。"""
    out = []
    for m in ZH_NUM.finditer(zh_text):
        raw, unit = m.group(1).rstrip(".,"), m.group(2)
        # 辨識度門檻。第一版沒有它，抽驗五筆全是假陽性：中文某處有「1萬」、
        # 英文別處剛好有「1 million」講完全不同的事，就被判成沒換算。本支只驗
        # 「同一數字串出現在量級詞旁」，驗不了兩者指的是不是同一個量，所以數字
        # 本身必須夠獨特才能當指紋——帶小數點／千分位，或至少三位數。
        # 「1」「2」「10」這種在任何長文裡都會巧合命中（REFLEXES #66 用真實產出校準）。
        if not (("." in raw) or ("," in raw) or len(raw.replace(",", "")) >= 3):
            continue
        try:
            val = float(raw.replace(",", "")) * (10 ** ZH_MAG[unit])
        except ValueError:
            continue
        out.append((raw, val, unit))
    return out


def check(zh_path: Path, out_path: Path, lang: str) -> list[str]:
    mags = MAGNITUDE.get(lang)
    if not mags:
        return []
    zh_text = zh_path.read_text(encoding="utf-8", errors="ignore")
    out_text = out_path.read_text(encoding="utf-8", errors="ignore")
    hits, seen = [], set()
    for raw, val, unit in zh_figures(zh_text):
        if raw in seen:
            continue
        for word, power in mags.items():
            # 同一個數字串直接黏在目標語言的量級詞旁邊。
            # **左邊界不可省**：沒有它的話 `3.3 लाख` 裡的子字串 `3 लाख` 會命中，
            # 報出一個根本不存在的錯。這正是 2026-09-09 把檔案改壞的那個 bug——
            # 我第一版把它原封不動寫進了檢查器（同一天第七次子字串陷阱）。
            pat = r"(?<![0-9.,])" + re.escape(raw) + r"\s*" + re.escape(word)
            m2 = re.search(pat, out_text, re.I)
            if not m2:
                continue
            # 複合量級詞不算。越南文的「nghìn tỷ」是千個 tỷ ＝ 10¹²、西班牙文的
            # 「mil millones」是十億——量級詞後面接著另一個量級詞時，真正的量級是
            # 兩者相乘，本支的單一詞比對判不了。抽驗時 `1.70 nghìn tỷ`（1.7 兆，正確）
            # 被報成錯，就是這個家族。
            tail = out_text[m2.end():m2.end() + 24].lower()
            if any(re.match(r"\s*" + re.escape(w2.lower()), tail) for w2 in mags):
                continue
            written = float(raw.replace(",", "")) * (10 ** power)
            if abs(written - val) / max(val, 1) < 0.001:
                continue  # 剛好等值（例如中文「千」對上 thousand），不是錯
            # 倍率合理性。單位沒換算的錯，倍率必然是 10 的小次方（萬↔lakh 差 10、
            # 萬↔million 差 100、億↔billion 差 10）。倍率離譜的是巧合——中文某處的
            # 「100萬」跟譯文別處的「100 billion」講的是不同的事，差 10 萬倍。
            # 本支驗不了兩個數字指的是不是同一個量，只能用倍率把巧合濾掉。
            import math
            ratio = written / val
            exp = math.log10(ratio)
            if abs(exp) > 3.01 or abs(exp - round(exp)) > 0.01:
                continue
            correct = val / (10 ** power)
            hits.append(
                f"「{raw}{unit}」= {val:,.0f}，但譯文寫成「{raw} {word}」= {written:,.0f}"
                f"（差 {written / val:.0f} 倍）→ 應為「{correct:g} {word}」"
            )
            seen.add(raw)
            break
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zh", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--lang")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    pairs = []
    if a.zh and a.out:
        p = Path(a.out).resolve()
        # 語言代碼從路徑裡找，不假設呼叫端給的是相對於 knowledge/ 的絕對路徑
        # （倉庫外的校準樣本也要能驗）
        lang = next((seg for seg in p.parts if seg in MAGNITUDE), None)
        if not lang:
            print(f"❌ 路徑裡看不出語言：{a.out}", file=sys.stderr)
            return 2
        pairs.append((Path(a.zh), p, lang))
    elif a.lang:
        tj = KNOWLEDGE / "_translations.json"
        idx = json.loads(tj.read_text(encoding="utf-8")) if tj.exists() else {}
        for f in sorted((KNOWLEDGE / a.lang).rglob("*.md")):
            rel = str(f.relative_to(KNOWLEDGE))
            zh = idx.get(rel)
            if zh and (KNOWLEDGE / zh).exists():
                pairs.append((KNOWLEDGE / zh, f, a.lang))
    else:
        ap.error("要給 <zh> <譯文>，或 --lang")

    report, total = {}, 0
    for zh, out, lang in pairs:
        h = check(zh, out, lang)
        if h:
            try:
                key = str(out.relative_to(REPO))
            except ValueError:
                key = str(out)  # 倉庫外的校準樣本
            report[key] = h
            total += len(h)

    if a.json:
        print(json.dumps({"files": len(pairs), "hits": total, "detail": report},
                         ensure_ascii=False, indent=2))
        return 1 if total else 0
    for fn, hs in report.items():
        print(f"❌ {fn}")
        for x in hs:
            print(f"      {x}")
    if total:
        print(f"\n════ {len(pairs)} 檔，{total} 處量級可疑 ════")
        print("中文的萬(10⁴)／億(10⁸) 跟各語言的 thousand/million/billion 不是一對一。")
        print("換算正確的話數字串一定會變——數字串沒變就是沒換算。逐處人看，這支只給線索。")
        return 1
    print(f"✅ {len(pairs)} 檔，量級無可疑")
    return 0


if __name__ == "__main__":
    sys.exit(main())
