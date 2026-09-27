#!/usr/bin/env python3
"""name-absence-check.py — 譯文點名了一個 zh 原文裡根本沒有的人。

為什麼要這支（2026-09-26 巴別塔渦流第九輪）：一個晚上照出一整族張冠李戴，全部閘門都綠——
  · en〈台灣企業：宏碁〉把創辦人施振榮寫成 Shih Ming-de 63 處（那是施明德），接班的王振堂寫成 Terry Gou
  · en〈報導者〉把捐款人童子賢寫成 Barry Lam（林百里）
  · en〈拼板舟〉把夏曼・藍波安寫成 Hsiao Bi-khim（蕭美琴）；es〈閃靈〉把何韻詩寫成 Teresa Teng
  · en〈中壢事件〉description 自己寫著「note: source says Hsu Hsin-liang」，前面仍是 Hsiao Bi-khim
name-consistency-check 的規則 B 刻意只比人物頁標題（它的 docstring 記了全文比對第一版 277 處多半誤報），
所以正文裡的張冠李戴結構上看不到。這支換一個判準：譯文用了名字表裡某人的拼寫，而那個人的漢字
**根本不在 zh 原文裡**——原文沒提到的人，譯文不該點名。

為什麼只做報告不當閘門：判準有三族已知誤報，要人對 zh 逐筆核——
  1. 同一人不同稱呼：表的鍵是蔣中正，原文寫蔣介石或中正紀念堂（ALIAS 收了已知的幾組，收不完）
  2. 同音不同人：「Lin Chi-wei」在表上是林啟維，拿來寫林其蔚也拼成一樣
  3. 譯者補充語境：原文寫「總統」，譯文補上 Tsai Ing-wen——多半正確，但原文確實沒寫
校準（2026-09-26 全庫七個拉丁語系 7,943 篇）：原始判準 474 處／448 篇，蔣中正一族就佔 216；
加上連字號邊界（Lin Liang 不再吃進 Lin Liang-chun）與 ALIAS 之後 160 處／152 篇，抽樣裡真錯
佔多數。存量處置見 OBSERVER-QUEUE #84。

盲區（2026-09-27 維護班 session 提的正控制）：995ee366e 之前的 vi〈戴資穎〉整篇把她寫成
Đinh Trí Anh 46 處，這支 0 命中——那是憑空拼出來的名字，不是表上另一個人的拼寫，不在判準內。
反方向也試過：「zh 提到某人 ≥3 次、譯文卻沒有他任何已知拼寫」全庫 1,310 處／929 篇，越南文的
漢越音（李登輝 → Lý Đăng Huy）與鄭成功 → Koxinga 這類合法寫法淹沒訊號，正控制也沒命中，不採用。
發明出來的錯名只剩人物頁標題那一格（name-consistency 規則 A 的少數形）看得到。

掃描範圍（2026-09-27 起）：原本寫死七個拉丁語系，被 check-hardcoded-langs 點名（語言清單要從 langs.py 來）。
改成掃全部翻譯語言：非拉丁文字的譯文只在括號對照裡寫拉丁拼寫，那裡點名的人一樣該在 zh 裡；
全庫多出 6 處候選（ja 1、hi 2、ar 3），例如 hi 某篇括號寫 Tsai Ing-wen、zh 原文沒有蔡英文。

用法：
  python3 name-absence-check.py                 # 全庫盤點（langs.py 的全部翻譯語言）
  python3 name-absence-check.py <譯文...>        # 指定檔案
  python3 name-absence-check.py --json
輸出只列候選，exit 0；核對要回 zh 原文看那一句在講誰。
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"
TABLE = Path(__file__).with_name("name-variants.json")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402

# 表鍵 → 原文裡可能出現的其他稱呼。有任何一個在 zh 裡，就不算「原文沒提到」。
ALIAS = {
    "蔣中正": ["蔣介石", "中正"],
    "史溫侯": ["斯文豪", "郇和"],
    "莫那·魯道": ["莫那魯道", "莫那"],
    "館長陳之漢": ["陳之漢", "館長"],
    "蔡英文": ["小英", "蔡總統"],
    "柯文哲": ["柯P", "柯Ｐ"],
    "曾博恩": ["博恩"],
    # 「三金」＝金馬、金鐘、金曲，原文寫三金時譯文列出三座獎不算點名錯
    "金曲": ["三金"],
    "金馬": ["三金"],
    "金鐘": ["三金"],
}
# 張冠李戴也發生在獎項：台灣的「金」字獎各管一塊（金曲音樂、金馬電影、金鐘電視）。2026-09-27 渦流第十九輪
# 量到十二篇譯文點名了 zh 原文沒有的那一座：id〈金曲獎〉全篇 80 處寫成金馬，金韻、金韶、金音這些小獎最常被
# 譯成 Golden Melody。鍵用不帶「獎」的短名，zh 寫「金曲」或「金曲獎」都算提到。
AWARDS = {"金曲": ["Golden Melody"], "金馬": ["Golden Horse"], "金鐘": ["Golden Bell"]}
# 學校、政黨、電視台同一族（2026-09-27 渦流第二十輪）：大學換成另一所（台師大、交大、中正大學都被寫成台大）、
# 政黨換成另一個（時代力量寫成民眾黨），還有杜撰的「National Taiwan University of Literature」（國立台灣文學館）。
# 值是 (英文正式名, zh 可能的其他寫法)。國民黨不收：「Kuomintang government」多半是譯者替「國府」「政府」補的語境。
# 台藝大、台科大、臺灣體大要列：它們的英文名以 National Taiwan University 開頭，不列就會被當成台大。
INSTITUTIONS = {
    "民進黨": (["Democratic Progressive Party"], ["民主進步黨"]),
    "民眾黨": (["Taiwan People's Party", "Taiwan People’s Party"], []),
    "親民黨": (["People First Party"], []),
    "時代力量": (["New Power Party"], []),
    "台聯": (["Taiwan Solidarity Union"], ["台灣團結聯盟", "臺灣團結聯盟"]),
    "民視": (["Formosa Television"], []),
    "公視": (["Public Television Service"], ["公共電視"]),
    "華視": (["Chinese Television System"], []),
    "台大": (["National Taiwan University"], ["臺大", "台灣大學", "臺灣大學"]),
    "台藝大": (["National Taiwan University of Arts"], ["臺藝大", "台灣藝術大學", "臺灣藝術大學", "藝專"]),
    "台科大": (["National Taiwan University of Science and Technology"], ["臺科大", "台灣科技大學", "臺灣科技大學"]),
    "臺灣體大": (["National Taiwan University of Sport"], ["台灣體大", "體育運動大學"]),
    "師大": (["National Taiwan Normal University"], ["台灣師範大學", "臺灣師範大學", "師範學院"]),
    "政大": (["National Chengchi University"], ["政治大學"]),
    "成大": (["National Cheng Kung University"], ["成功大學"]),
    "清大": (["National Tsing Hua University"], ["清華"]),
    "交大": (["National Chiao Tung University", "National Yang Ming Chiao Tung University"],
             ["交通大學", "陽明交大", "陽明交通大學"]),
    "中興大學": (["National Chung Hsing University"], []),
    "中山大學": (["National Sun Yat-sen University"], []),
}
ALIAS.update({k: v[1] for k, v in INSTITUTIONS.items() if v[1]})
# 表鍵本身是日常用語或 slug 已知錯置，比對起來全是雜訊
SKIP = {"這群人", "簡立峰"}
SRC = re.compile(r"^translatedFrom:\s*['\"]?([^'\"\n]+)", re.M)


def _usable(form: str) -> bool:
    return len(form) >= 6 and len(form.split()) >= 2


def build_pattern():
    tbl = json.loads(TABLE.read_text(encoding="utf-8"))
    owners: dict[str, set[str]] = collections.defaultdict(set)
    for han, v in tbl.items():
        if han in SKIP:
            continue
        for f in list(v["forms"]) + ([v["zh_given"]] if v.get("zh_given") else []):
            if _usable(f):
                owners[f].add(han)
    for key, award_forms in AWARDS.items():
        for f in award_forms:
            owners[f].add(key)
    for key, (inst_forms, _) in INSTITUTIONS.items():
        for f in inst_forms:
            owners[f].add(key)
    # 同一個拼寫掛在兩個人名下的，無從判斷在講誰，不用
    forms = {f: next(iter(o)) for f, o in owners.items() if len(o) == 1}
    alt = "|".join(sorted(map(re.escape, forms), key=len, reverse=True))
    # 邊界連字號含 U+2011（不斷行連字號）：es 有一篇 Lin Liang‑jun 用的就是它
    return forms, re.compile(r"(?<![A-Za-z\-‑])(" + alt + r")(?![A-Za-z\-‑])")


def scan(path: Path, forms: dict, pat: re.Pattern) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    m = SRC.search(text)
    if not m:
        return []
    zh_path = KNOWLEDGE / m.group(1).strip()
    if not zh_path.exists():
        return []
    zh = zh_path.read_text(encoding="utf-8")
    out, seen = [], set()
    for mm in pat.finditer(text):
        form = mm.group(1)
        han = forms[form]
        if han in seen or han in zh or any(a in zh for a in ALIAS.get(han, [])):
            continue
        seen.add(han)
        out.append({
            "path": str(path.relative_to(REPO)),
            "line": text.count("\n", 0, mm.start()) + 1,
            "form": form,
            "person": han,
            "context": text[max(0, mm.start() - 60): mm.end() + 40].replace("\n", " "),
        })
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--json"]
    forms, pat = build_pattern()
    if args:
        files = [Path(a) if Path(a).is_absolute() else REPO / a for a in args]
    else:
        files = [p for L in ALL_TRANSLATION_LANGS for p in sorted((KNOWLEDGE / L).rglob("*.md"))]
    hits = [h for f in files if f.is_file() for h in scan(f, forms, pat)]
    if "--json" in sys.argv:
        print(json.dumps(hits, ensure_ascii=False, indent=1))
        return 0
    for h in hits:
        print(f"⚠️ {h['path']}:{h['line']} 「{h['form']}」是{h['person']}，zh 原文沒提到\n   …{h['context']}…")
    print(f"\n{len(hits)} 處／{len({h['path'] for h in hits})} 篇候選（報告不是閘門：回 zh 核那一句在講誰）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
