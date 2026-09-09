#!/usr/bin/env python3
"""currency-identity-check.py — 台灣的錢被寫成中國的錢。

2026-09-10 出生：id 的環境正義篇把「新台幣 2 兆元」寫成 `2 triliun yuan`、
「每噸數十元」寫成 `puluhan yuan`。在印尼文／西班牙文／俄文裡，沒有限定詞的
yuan / юань / يوان 就是人民幣。同一個下午已經是第三次撞到這一族——先前還有一次
是反過來的災難：為了修這種錯做字串取代，`يوان` 是 `تايوان`（台灣）的子字串，
把「莊智淵代表台灣」改成了「莊智-美元」。

判準：譯文裡「數字（可帶量級詞）緊接幣別詞」，而前後 45 字內沒有任何限定詞
（Taiwan / NT$ / TWD / Тайвань / تايوان / baru …），且 **zh 來源通篇沒有「人民幣」**。
最後這一條很重要——講中國公司或中國市場的文章（大宇雙劍賣 IP 給中手游、
動畫投資 1 億元人民幣）裡的 yuan 是對的。

三輪校準才收斂（REFLEXES #66）：
  第一版只找幣別詞 → 12,899 處，其中絕大多數是「Legislative Yuan／Executive Yuan」
    （立法院／行政院），根本不是貨幣。
  第二版加數字錨定 → 1,288 處，但 `[0-9,]*` 吃掉逗號讓「2024, Yuan Goang-Ming」
    （袁廣鳴）穿過。
  第三版排除幣別詞後接大寫字的情形（Yuan Ze University、Yuan Goang-Ming）→ 1,180 處。

用法：
    python3 currency-identity-check.py <譯文...>   # exit 1 = 有命中
    python3 currency-identity-check.py --all
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]

MAG = (r"(?:ribu|juta|miliar|triliun|mil|millones|millón|milliards?|millions?|"
       r"thousand|million|billion|тысяч\w*|миллион\w*|миллиард\w*|"
       r"ألف|آلاف|مليون|مليار|हज़ार|लाख|करोड़|अरब|nghìn|triệu|tỷ|"
       r"Tausend|Millionen|Milliarden)")

CURRENCY = {
    "id": r"yuan", "es": r"yuan(?:es)?", "fr": r"yuans?", "pt": r"yuan(?:es)?",
    "en": r"yuan", "de": r"Yuan", "ru": r"юан\w*", "ar": r"يوان",
    "hi": r"युआन", "vi": r"nhân dân tệ",
}

# 有這些限定詞在附近就不是「裸幣別」
QUALIFIER = re.compile(
    r"(Taiwan|Tai[wv]an|TWD|NT\$|Тайв|تايوان|ताइवान|Đài Loan|baru|Baru)", re.I)
# 幣別詞後面接大寫開頭的字＝專有名詞（Yuan Ze University、Yuan Goang-Ming）
PROPER_NOUN = re.compile(r"^\s*[A-ZА-Я][a-zа-я-]")

SUGGEST = {
    "id": "NT$ / dolar Taiwan", "es": "NT$ / dólares taiwaneses", "fr": "NT$ / dollars taïwanais",
    "pt": "NT$ / dólares taiwaneses", "en": "NT$ / New Taiwan dollars", "de": "NT$ / Neue Taiwan-Dollar",
    "ru": "NT$ / новых тайваньских долларов", "ar": "NT$ / دولار تايواني جديد",
    "hi": "NT$ / नए ताइवानी डॉलर", "vi": "NT$ / Đài tệ",
}


def lang_of(path: Path) -> str | None:
    try:
        parts = path.resolve().relative_to(REPO / "knowledge").parts
    except ValueError:
        return None
    return parts[0] if len(parts) >= 2 and re.fullmatch(r"[a-z]{2}", parts[0]) else None


def zh_source(text: str) -> Path | None:
    m = re.search(r"^translatedFrom:\s*['\"]?([^'\"\n]+)", text, re.M)
    return (REPO / "knowledge" / m.group(1).strip()) if m else None


def scan(path: Path) -> list[str]:
    lang = lang_of(path)
    if lang not in CURRENCY:
        return []
    text = path.read_text(encoding="utf-8")
    zh = zh_source(text)
    if zh is None or not zh.exists():
        return []
    # 文章本身就在講人民幣（中國公司、中國市場）→ 那裡的 yuan 是對的
    if "人民幣" in zh.read_text(encoding="utf-8"):
        return []
    pat = re.compile(rf"[0-9][0-9.,]*[0-9]?\s?(?:{MAG}\s)?{CURRENCY[lang]}\b", re.I)
    hits = []
    for m in pat.finditer(text):
        if PROPER_NOUN.match(text[m.end():m.end() + 12]):
            continue
        window = text[max(0, m.start() - 45):m.end() + 45]
        if QUALIFIER.search(window):
            continue
        hits.append(f"{m.group()}   …{window.strip()[:80]}…".replace("\n", " "))
    return hits


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    files = (sorted(p for p in (REPO / "knowledge").rglob("*.md") if lang_of(p) in CURRENCY)
             if args[0] == "--all" else [Path(a) for a in args])

    total = flagged = 0
    for f in files:
        hits = scan(f)
        if not hits:
            continue
        flagged += 1
        total += len(hits)
        lang = lang_of(f)
        print(f"❌ {f.resolve().relative_to(REPO)} — {len(hits)} 處裸幣別（該用 {SUGGEST[lang]}）")
        for h in hits[:5]:
            print(f"     {h}")
        if len(hits) > 5:
            print(f"     …另外 {len(hits) - 5} 處")
    if flagged:
        print(f"\n════ {flagged} 檔，合計 {total} 處 ════")
        print("台灣的錢不是中國的錢。沒有限定詞的 yuan／юань／يوان 讀者會讀成人民幣。")
        print("⚠️ 修的時候不要做裸字串取代——`يوان` 是 `تايوان`（台灣）的子字串，"
              "2026-09-09 有人因此把「莊智淵代表台灣」改成了「莊智-美元」。用數字錨定。")
        return 1
    print(f"✅ {len(files)} 檔，沒有把台幣寫成人民幣")
    return 0


if __name__ == "__main__":
    sys.exit(main())
