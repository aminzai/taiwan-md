#!/usr/bin/env python3
"""numeral-conversion-check.py — 抓「量級換算錯了」的譯文（數字串變了，但變錯了）。

跟 `numeral-magnitude-check.py` 是同一個病的另一半，兩支合起來才蓋住整族：

  · magnitude 那支抓「**沒換算**」——量級詞換了、數字串原封不動
    （`23.3萬` → `23.3 लाख`，指紋是「同一個數字串出現在量級詞旁」）
  · 本支抓「**換算錯**」——數字串確實變了，所以 magnitude 那支的指紋對不上，
    但變出來的值跟原文差了一個 10 的次方
    （`16.5億` = 1.65e9 → `165 Millionen` = 1.65e8，差十倍）

magnitude 那支的 docstring 自己寫了這個缺口，並說補償手段是「主 session 逐篇把
zh 的量級詞列出來算一次再對照」。2026-09-10 早班就是那個手段在作用：審德文投稿時
順手對照 `knowledge/de/People/steve-chen-youtube-cofounder.md`，抓到 YouTube 賣價
六處全寫成十分之一（投稿者九月一日交的版本是對的，九月八日 babel 重譯時弄錯）。
那次是人讀出來的，本支把它變成機器讀得出來的。

判準（保守，沿用 magnitude 那支用真實產出校準出來的四道濾網）：
  同一組**有效數字**出現在兩邊的量級詞旁，但算出來的值差一個 10 的整數次方。
  `16.5億` 的有效數字是 `165`；`165 Millionen` 的有效數字也是 `165`。
  有效數字相同而量級不同 = 譯者搬動了小數點但搬錯格。

  四道濾網（每一道都是 magnitude 那支踩過才有的，不重新踩一次）：
  1. 辨識度門檻 —— 有效數字至少三位，或原文帶小數點／千分位。
     「1」「2」「10」在任何長文裡都會巧合命中。
  2. 左邊界 —— `(?<![0-9.,])`。沒有它，`3.3 लाख` 裡的子字串 `3 लाख` 會命中，
     報出一個不存在的錯（2026-09-09 改壞 41 個檔的那個子字串陷阱）。
  3. 複合量級詞 —— `nghìn tỷ`（千個 tỷ = 10¹²）、`mil millones`（十億）後面
     還接著量級詞時，真正的量級是兩者相乘，單一詞比對判不了，跳過。
  4. 倍率必須是 10 的整數次方且 |exp| ≤ 3 —— 換算錯的倍率必然如此；
     倍率離譜的是兩個不相干的數字剛好共用有效數字。

  ⚠️ 本支**只抓「有效數字相同但量級錯」**。譯者把數字整個打錯（`16.5億` 寫成
  `1,8 Milliarden`）有效數字就不同了，本支看不到，那需要逐段對齊配對，是第三支
  工具的工作。兩支加起來不是這一族的全集。

  ⚠️ ja/ko 原生使用万／億，量級與中文同構，不適用（直接回 0，不是錯誤）。

用法：
  python3 scripts/tools/lang-sync/numeral-conversion-check.py <zh 原文> <譯文>
  python3 scripts/tools/lang-sync/numeral-conversion-check.py --lang de   # 掃整個語言
  python3 scripts/tools/lang-sync/numeral-conversion-check.py --all       # 掃全部語言
exit 1 = 有可疑的換算。**這支是線索產生器不是裁決者**：命中要人看一眼再改，
且改的時候絕對不要做裸字串取代（`165` 是 `1165` 的子字串），要帶量級詞一起換。

═══════════════════════════════════════════════════════════════════════════
⚠️  狀態：**未校準完成，不可當量測依據，不可接任何 gate**（2026-09-10）
═══════════════════════════════════════════════════════════════════════════

誕生：2026-09-10 twmd-maintainer-am，為了把 magnitude 那支自述的「換算錯」缺口
從人讀變成機器讀。三輪校準後全庫跑出 1,938 處 / 1,026 檔，**但 20 筆分層抽驗
只有 4 筆能確認是真的**，另外至少四個假陽性家族還沒修。**所以那個數字不算數，
沒有寫進任何報告或佇列**——一支抓「數字錯了」的工具，自己先不能報錯的數字。

已修的三個家族（每一個都是全庫 dogfood 才現形，見各處 inline 註解）：
  1. 逗號小數語言的小數點被當千分位（de `1,65 Milliarden` 報成差 100 倍）
  2. `mil` 是 `millones`／`milhões` 的前綴（es/pt 共 761 檔幾乎整批假陽性）
  3. 歐陸千分位點的歧義（es `60.000 millones` 是正確的）

**還沒修的四個家族**（抽驗揭露，下一個接手的人從這裡開始）：
  4. **frontmatter 沒排除** —— `rationale`／`design_rationale` 這類欄位存的是
     中文設計論證，本支把它當正文掃。`en/Economy/acer-pc-industry-pioneer.md`
     命中的那處，出處正是 zh rationale 裡「US$1.5 億非 15 億」那句話本身。
  5. **外語量級詞洩漏破壞最長匹配** —— 最長匹配只認該語言自己的量級詞表。
     `es/Society/za-share.md` 的 description 整段是英文，`mil` 就match進英文的
     `million` 裡。（順帶：那個 description 是英文本身是另一個病，屬
     `target-language-check` 的守備範圍，本支不處理。）
  6. **空白當千分位** —— 法文寫 `1 580 milliards`，左邊界擋不住空白，
     `580 milliard` 被切出來當成一個獨立的數。
  7. **有效數字巧合碰撞** —— 同一篇裡 zh 的某個數跟譯文另一個不相干的數剛好
     共用有效數字。`vi/Economy/evergreen-marine.md` 把 zh「100億」對上譯文講
     蘇伊士運河管理局損失的「100 triệu USD」（那句本身完全正確）。
     這一族是本支架構上的極限：它比對的是兩份文件裡的數字集合，不是同一句話裡
     的同一個量。要根治需要逐段對齊再配對——正是 magnitude 那支 docstring 說的
     「第三支工具的工作」。倍率濾網只能壓低發生率，消不掉。

接手建議：4/5/6 是機械的（排除 frontmatter、量級詞表補各語言常見外語形、
左邊界加空白），修完再抽驗一次；7 要先決定架構（要不要做段落對齊），
不決定就不要把這支接上任何 gate——否則它會變成第十四個假陽性家族。
"""
import argparse
import json
import math
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"

# 跟 numeral-magnitude-check.py 同一張表（刻意各自持有而非 import：那支是線上
# 產線呼叫中的工具，本支還在黃燈期，共用模組等於把黃燈期的改動風險接到產線上）。
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
ZH_MAG = {"萬": 4, "万": 4, "億": 8, "亿": 8, "兆": 12, "千": 3}
ZH_NUM = re.compile(r"([0-9][0-9,.]*)\s*([萬万億亿兆])")

# 小數點用逗號的語言。**這張表是本支的第一個 bug**：第一版對所有語言都做
# `replace(",", "")`，於是德文的 `1,65 Milliarden`（= 1.65e9，完全正確）被讀成
# 165 × 10⁹，倍率 100，報成錯——而那正是同一個早上我自己剛修好的那一行。
# 負控制抓到它，否則這支上線第一天就會對 de/es/fr/pt/ru/id/vi 的每個小數開火。
DECIMAL_COMMA = {"de", "es", "fr", "pt", "ru", "id", "vi"}


AMBIGUOUS = object()  # 分隔符意義判不了 → 整筆跳過，不猜


def parse_num(raw: str, lang: str):
    """依語言把數字串讀成值。判不出分隔符意義時回 AMBIGUOUS（跳過，不猜）。

    逗號與點在各語言意義相反，這一層是本支假陽性的主要來源。全庫 dogfood 的
    第二輪抽驗（20 筆分層樣本）揭露三個家族，全部出在這個函式：

      · 歐陸千分位點 —— es `60.000 millones` 是 60,000 millones（= 6e10，正確），
        第一版讀成 60.0 → 報成差 1000 倍。zh「600億」剛好等於它，所以這是
        **把正確的譯文報成錯的**，最惡性的一種假陽性。
      · 分隔符後剛好三位 —— id `2,606 juta` 可以是 2.606（小數，正確）也可以是
        2606（千分位）。第一版一律當千分位，把正確的報成差 1000 倍。
      · 同一個歧義在 es/pt/vi/ru/fr 都有。

    對策是**不猜**：分隔符後剛好三位數而無其他線索時回 AMBIGUOUS。這會少抓一些
    真錯（recall 降低），但線索產生器的假陽性成本遠高於漏抓——假陽性會讓人去
    「修」本來就對的數字（2026-09-09 裸字串取代改壞 41 檔正是這條路的終點）。
    """
    s = raw.strip().rstrip(".,")
    if not s or not re.fullmatch(r"[0-9][0-9.,]*", s):
        return None
    dec, tho = (",", ".") if lang in DECIMAL_COMMA else (".", ",")

    # 真正有歧義的只有一個組合：**逗號小數語言裡的點**。
    # 在 de/es/pt 等語言 `.` 是千分位（`60.000` = 六萬），但機器翻譯經常把
    # 來源的點小數原樣搬過來（`16.5` → `16.5`），兩讀都說得通。其餘組合沒有歧義：
    # zh/en/hi 的逗號永遠是千分位（`1,400` = 1400），de 的逗號永遠是小數點。
    # 第一版把歧義規則套在所有分隔符上，`1,400`(hi) 與 `1,000`(zh) 被判成判不出來，
    # 整批真錯跟著漏掉——濾網過寬跟過窄一樣會讓工具說不出真話。
    if tho == "." and "." in s and "," not in s:
        if re.fullmatch(r"[0-9]{1,3}(?:\.[0-9]{3})+", s):
            return AMBIGUOUS  # `60.000` 可讀成六萬（本地千分位）或 60.0（來源小數）
        return float(s)       # `16.5` 三位以外，只可能是搬過來的小數

    if dec not in s:
        if re.fullmatch(r"[0-9]{1,3}(?:" + re.escape(tho) + r"[0-9]{3})+", s):
            return float(s.replace(tho, ""))
        return AMBIGUOUS if tho in s else float(s)

    head, _, frac = s.rpartition(dec)
    if not head or not re.fullmatch(r"[0-9]*", frac):
        return AMBIGUOUS
    head = head.replace(tho, "")
    if not re.fullmatch(r"[0-9]+", head):
        return AMBIGUOUS
    try:
        return float(f"{head}.{frac}") if frac else float(head)
    except ValueError:
        return None


def sig_digits(raw: str) -> str:
    """有效數字字串：去分隔符、去前導／尾隨零。16.5 → 165；1,65 → 165；0.85 → 85。"""
    d = re.sub(r"[.,]", "", raw).lstrip("0")
    return d.rstrip("0") or "0"


def distinct_enough(raw: str) -> bool:
    """濾網 1：辨識度門檻（同 magnitude 那支）。"""
    return ("." in raw) or ("," in raw) or len(raw.replace(",", "")) >= 3


def zh_figures(zh_text: str):
    out = []
    for m in ZH_NUM.finditer(zh_text):
        raw, unit = m.group(1).rstrip(".,"), m.group(2)
        if not distinct_enough(raw):
            continue
        n = parse_num(raw, "zh")
        if n is None or n is AMBIGUOUS:
            continue
        out.append((raw, n * (10 ** ZH_MAG[unit]), unit, sig_digits(raw)))
    return out


def check(zh_path: Path, out_path: Path, lang: str):
    mags = MAGNITUDE.get(lang)
    if not mags:
        return []
    zh_text = zh_path.read_text(encoding="utf-8", errors="ignore")
    out_text = out_path.read_text(encoding="utf-8", errors="ignore")

    # 譯文側：每個「數字 + 量級詞」的出現，連同它的有效數字與算出來的值。
    found = []
    for word, power in mags.items():
        # 濾網 2：左邊界不可省（見檔頭）。
        # 濾網 2b：**最長匹配**——本支的第二個 bug，由全庫 dogfood 抓到。
        # 西語的 `mil`(10³) 是 `millones`(10⁶) 的前綴，葡語的 `mil` 是 `milhões`
        # 的前綴。沒有這道濾網時，`30 millones` 被當成 `30 mil` 命中、報成差 1000 倍；
        # 第一次全庫跑出 4,164 處，其中 es 395 + pt 366 檔幾乎整批是這個家族——
        # **當時若把那個數字寫進報告，整份報告的主張就是錯的**。
        # 先試過的「加右側 \b 詞邊界」是錯的修法：量級詞會變格變複數
        # （Millionen／миллионов／milhões），硬詞邊界連正控制都擋掉了。
        # 對的規則是最長匹配：同一個位置若有更長的量級詞也成立，就讓那一輪去處理。
        pat = re.compile(r"(?<![0-9.,])([0-9][0-9,.]*)\s*" + re.escape(word), re.I)
        longer = [w for w in mags if len(w) > len(word)]
        for m in pat.finditer(out_text):
            at = out_text[m.start():m.start() + len(m.group(0)) + 24].lower()
            if any(re.match(
                r"(?<![0-9.,])[0-9][0-9,.]*\s*" + re.escape(w2.lower()), at
            ) for w2 in longer):
                continue
            raw = m.group(1).rstrip(".,")
            if not raw:
                continue
            # 濾網 3：後面還接量級詞 → 複合量級，單一詞比對判不了。
            tail = out_text[m.end():m.end() + 24].lower()
            if any(re.match(r"\s*" + re.escape(w2.lower()), tail) for w2 in mags):
                continue
            n = parse_num(raw, lang)
            if n is None or n is AMBIGUOUS:
                continue
            found.append((raw, n * (10 ** power), word, sig_digits(raw)))

    hits, seen = [], set()
    for zraw, zval, zunit, zsig in zh_figures(zh_text):
        if zsig in seen:
            continue
        for traw, tval, tword, tsig in found:
            if tsig != zsig:
                continue
            if abs(tval - zval) / max(zval, 1) < 0.001:
                continue  # 等值，換算對了
            # 濾網 4：倍率必須是 10 的整數次方、不離譜。
            ratio = tval / zval if zval else 0
            if ratio <= 0:
                continue
            exp = math.log10(ratio)
            if abs(exp) > 3.01 or abs(exp - round(exp)) > 0.01:
                continue
            correct = zval / (10 ** MAGNITUDE[lang][tword])
            hits.append(
                f"「{zraw}{zunit}」= {zval:,.0f}，譯文寫成「{traw} {tword}」"
                f"= {tval:,.0f}（差 {ratio:g} 倍）→ 應為「{correct:g} {tword}」"
            )
            seen.add(zsig)
            break
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zh", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--lang")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from langs import ALL_TRANSLATION_LANGS  # noqa: E402

    pairs = []
    if a.zh and a.out:
        p = Path(a.out).resolve()
        lang = next((s for s in p.parts if s in set(ALL_TRANSLATION_LANGS)), None)
        if lang and lang not in MAGNITUDE:
            print(f"✅ {lang} 原生使用万／億，量級與中文同構，不適用本檢查")
            return 0
        if not lang:
            print(f"❌ 路徑裡看不出語言：{a.out}", file=sys.stderr)
            return 2
        pairs.append((Path(a.zh), p, lang))
    else:
        langs = [a.lang] if a.lang else [
            l for l in ALL_TRANSLATION_LANGS if l in MAGNITUDE
        ]
        if not a.all and not a.lang:
            ap.error("要給 <zh> <譯文>，或 --lang，或 --all")
        tj = KNOWLEDGE / "_translations.json"
        idx = json.loads(tj.read_text(encoding="utf-8")) if tj.exists() else {}
        for lang in langs:
            if lang not in MAGNITUDE:
                continue
            for f in sorted((KNOWLEDGE / lang).rglob("*.md")):
                rel = str(f.relative_to(KNOWLEDGE))
                zh = idx.get(rel)
                if zh and (KNOWLEDGE / zh).exists():
                    pairs.append((KNOWLEDGE / zh, f, lang))

    report, total = {}, 0
    for zh, out, lang in pairs:
        h = check(zh, out, lang)
        if h:
            try:
                key = str(out.relative_to(KNOWLEDGE))
            except ValueError:
                key = str(out)
            report[key] = h
            total += len(h)

    if a.json:
        print(json.dumps({"files": len(report), "hits": total, "detail": report},
                         ensure_ascii=False, indent=2))
    else:
        for k in sorted(report):
            print(f"\n⚠️  {k}")
            for line in report[k]:
                print(f"    {line}")
        if report:
            print(f"\n❌ {total} 處換算可疑 / {len(report)} 檔（掃 {len(pairs)} 檔）")
            print("⚠️  線索不是裁決：逐處看一眼再改，且不要做裸字串取代")
        else:
            print(f"✅ {len(pairs)} 檔，量級換算無可疑")
    return 1 if report else 0


if __name__ == "__main__":
    sys.exit(main())
