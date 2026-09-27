#!/usr/bin/env python3
"""numeric-event-check.py — 以數字命名的台灣事件，譯文有沒有一種認得出來的寫法（只報告，不修）。

為什麼要這支（2026-09-28 巴別塔渦流第二十六、二十七輪）：二二八、九二一、八八風災這類事件名本身就是數字或日期，
模型最常把它「翻成別的數字」——越南文把二二八寫成 Hai Ba Bát（2-3-8）、Tháng Tư 28（四月二十八），俄文寫成 22 февраля
與 22 августа，德文寫成 Zwei-Null-Acht-Vier（2084），印地文寫成 2-18。這些譯文 verify 與驗收全綠：閘門查結構、網址、
數量級，不查專有名詞的意思。第二十六輪用正則加兩隻唯讀審查找出 30 篇、全部修掉，第二十七輪同法查九二一與八八風災；
做到第二次就儀器化（BABEL-VORTEX-LOOP §儀器化第 2 條）。

判準：zh 正文（去掉 frontmatter、腳註定義行與網址——那些位置的中文是來源標題或路徑，不是正文）提到某事件，
譯文正文卻找不到任何一種「認得出來」的寫法 → 候選。認得出來的寫法有三種來源：
  1. 數字本身（228、921、88，與 2·28、9.21 這類分隔寫法）
  2. 各語言的日期寫法（28 février、21 de septiembre、8 августа⋯）
  3. 各語言的通行名稱（Chi-Chi、Morakot、Моракот⋯），以及第二十六輪審查確認過的另一種正確寫法
     （法文 le 28-Février、西文 Febrero 28、印地文 दो-दो-आठ、越南文 tháng Hai 28）
只報告不修：認不出來的不一定錯（可能是還沒收進表的正確寫法），要交人或唯讀審查分出真錯，確認的錯照各語言
語料最多的寫法手修。新的正確寫法審查確認後補進 FORMS，讓下一次的候選只剩真問題。

用法：
  python3 numeric-event-check.py                  # 全庫，三個事件
  python3 numeric-event-check.py --event 二二八    # 只查一個事件
  python3 numeric-event-check.py <譯文...>         # 指定檔案
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"
SRC = re.compile(r"^translatedFrom:\s*['\"]?([^'\"\n]+)", re.M)
FM = re.compile(r"^---\n.*?\n---\n", re.S)

# 每個事件：zh 正文怎麼認、數字本身、各語言的日期／通行名稱／已確認的其他正確寫法
EVENTS: dict[str, dict] = {
    "二二八": {
        "zh": r"二二八",
        "number": r"(?<!\d)228(?!\d)|2[·・./\-‑]2[·・./\-‑]?8",
        "forms": {
            "en": r"28 February|February 28", "fr": r"28 février|28-Février", "es": r"28 de febrero|Febrero 28",
            "pt": r"28 de fevereiro", "de": r"28\. Februar", "id": r"28 Februari",
            "vi": r"28 tháng 2|28/2|tháng Hai 28|Hai Hai Tám", "ru": r"28 февраля|28-го февраля",
            "ja": r"二・二八|二二八|2・28", "ko": r"2·28|2\.28", "hi": r"28 फ़रवरी|28 फरवरी|दो-दो-आठ", "ar": r"28 فبراير|٢٢٨",
        },
    },
    "九二一": {
        "zh": r"九二一",
        "number": r"(?<!\d)921(?!\d)|9[·・./\-‑]21",
        "forms": {
            "en": r"September 21|21 September|Chi-?Chi", "fr": r"21 septembre|Chi-?Chi", "es": r"21 de septiembre|Chi-?Chi",
            "pt": r"21 de setembro|Chi-?Chi", "de": r"21\. September|Chi-?Chi", "id": r"21 September|Chi-?Chi",
            "vi": r"21 tháng 9|Tập Tập|Chi-?Chi", "ru": r"21 сентября|Чичи|Цзицзи",
            "ja": r"九二一|9月21日|集集", "ko": r"9월 21일|지지", "hi": r"21 सितंबर|ची-ची|चीची", "ar": r"21 سبتمبر|تشي تشي",
        },
    },
    "八八風災": {
        "zh": r"八八風災|八八水災",
        "number": r"(?<!\d)88(?!\d)|8[·・./\-‑]8(?!\d)",
        "forms": {
            "en": r"Morakot|8 August|August 8", "fr": r"Morakot|8 août", "es": r"Morakot|8 de agosto", "pt": r"Morakot|8 de agosto",
            "de": r"Morakot|8\. August", "id": r"Morakot|8 Agustus", "vi": r"Morakot|8 tháng 8", "ru": r"Моракот|Morakot|8 августа",
            "ja": r"モーラコット|莫拉克|八八|8月8日|Morakot", "ko": r"모라꼿|모라콧|8월 8일|Morakot", "hi": r"मोराकोट|Morakot|8 अगस्त",
            "ar": r"موراكوت|Morakot|8 أغسطس",
        },
    },
}


def zh_prose(text: str) -> str:
    """zh 正文裡「讀者讀到的句子」：去掉 frontmatter、腳註定義行與網址。"""
    m = FM.match(text)
    body = text[m.end():] if m else text
    body = "\n".join(line for line in body.splitlines() if not line.startswith("[^"))
    return re.sub(r"https?://\S+", "", body)


# 法文排版在數字與月份之間用不斷行空白（U+00A0／U+202F），細空白 U+2009 也見過；
# 比對前一律換成一般空白，「28 février」才認得出來（第二十七輪：fr〈白先勇〉審查為正確、卻被報成候選）
_NBSP = str.maketrans({"\u00a0": " ", "\u202f": " ", "\u2009": " "})


def body_of(text: str) -> str:
    m = FM.match(text)
    return (text[m.end():] if m else text).translate(_NBSP)


def recognizable(event: str, lang: str, translation_body: str) -> bool:
    ev = EVENTS[event]
    pat = ev["number"] + ("|" + ev["forms"][lang] if lang in ev["forms"] else "")
    return re.search(pat, translation_body, re.I) is not None


def check(event: str, lang: str, zh_text: str, tr_text: str) -> int:
    """回傳 zh 正文提到的次數；譯文認得出來、或 zh 沒提到時回 0（不是候選）。"""
    n = len(re.findall(EVENTS[event]["zh"], zh_prose(zh_text)))
    if not n or recognizable(event, lang, body_of(tr_text)):
        return 0
    return n


def main() -> int:
    args = sys.argv[1:]
    events = list(EVENTS)
    if "--event" in args:
        i = args.index("--event")
        events = [args[i + 1]]
        args = args[:i] + args[i + 2:]
    files = ([Path(a) if Path(a).is_absolute() else REPO / a for a in args] if args else
             [p for L in ALL_TRANSLATION_LANGS for p in sorted((KNOWLEDGE / L).rglob("*.md"))
              if not p.name.startswith("_")])
    zh_cache: dict[Path, str] = {}
    found = {e: [] for e in events}
    for p in files:
        lang = p.relative_to(KNOWLEDGE).parts[0]
        t = p.read_text(encoding="utf-8")
        m = SRC.search(t)
        zp = KNOWLEDGE / m.group(1).strip() if m else None
        if not zp or not zp.exists():
            continue
        if zp not in zh_cache:
            zh_cache[zp] = zp.read_text(encoding="utf-8")
        for e in events:
            n = check(e, lang, zh_cache[zp], t)
            if n:
                found[e].append((p.relative_to(REPO).as_posix(), n))
    for e in events:
        print(f"{e}：{len(found[e])} 篇譯文找不到認得出來的寫法（zh 正文提到次數）")
        for rel, n in found[e]:
            print(f"  {rel}  ×{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
