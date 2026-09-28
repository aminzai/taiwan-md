#!/usr/bin/env python3
"""name-substitution-check.py — 譯文裡出現 zh 原稿根本沒提到的名人或首都。

模型遇到陌生的台灣人名或地名，會拿它最熟的那一個頂上去：2026-09-28 盤點，
越南文把台北寫成 Hà Nội（河內）45 篇、把台灣人寫成蔡英文 25 篇；es／pt／hi
〈蔡健雅〉整篇的主角是「Tsai Ing-wen」、hi〈賴聲川〉是「Lai Ching-te」、pt
寫「蔣介石宣布解嚴」、en 把中山高寫成「Chiang Kai-shek Expressway」。這些譯文
網址、腳註、結構全對，verify-translation 每一道都過。

判斷很窄：名人（或首都）在譯文出現，而 zh 原稿（含 frontmatter 與腳註）連一個
別名都沒有。zh 有提到就不算——解說性補充與同一人的不同稱呼都放過。

    python3 name-substitution-check.py knowledge/es/People/tanya-chua-singer.md ...
    python3 name-substitution-check.py --all            # 全部譯文，列出命中
    python3 name-substitution-check.py --all --json     # 給 babel-pulse 用

有命中時 exit 1。zh 原稿由譯文 frontmatter 的 translatedFrom 找。

跟 name-absence-check.py 的分工：那支拿名字表（拉丁拼寫、全部人物頁）報告候選，誤報三族要人逐筆核，
存量在 OBSERVER-QUEUE #84。這支只收模型最常拿來頂替的幾個名人與首都，各語言用自己的文字寫
（越南文漢越音、韓文、天城文、西里爾），所以看得到那支看不到的越南文 86 篇；判準窄到可以當驗收閘。
存量處置見 #91。
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
KNOWLEDGE = ROOT / "knowledge"
LANGS = ("en", "ja", "ko", "es", "fr", "de", "pt", "vi", "id", "ru", "hi", "ar")
LATIN = ("en", "es", "fr", "de", "pt", "id")

# (名稱, zh 別名, {語言: 譯文寫法})——zh 任一別名出現就視為原稿有提到這個人／地方
ENTITIES = [
    ("蔡英文", r"蔡英文|小英|蔡總統|蔡政府|蔡前總統|英德配|蔡賴",
     {**{l: r"\bTsai Ing-?wen\b" for l in LATIN}, "ja": r"蔡英文", "ko": r"차이잉원",
      "ru": r"Цай Ин-?вэнь", "hi": r"(?:त्)?साई इंग[- ]?वेन", "ar": r"تساي (?:إنغ|إينغ)[- ]?(?:ون|وين)",
      "vi": r"Thái Anh Văn"}),
    ("賴清德", r"賴清德|賴總統|賴政府|賴副總統|賴神|英德配|蔡賴",
     {**{l: r"\bLai Ching-?te\b|\bWilliam Lai\b" for l in LATIN}, "ja": r"頼清徳|賴清德", "ko": r"라이칭더",
      "ru": r"Лай Цин-?дэ", "hi": r"लाई चिंग[- ]?ते", "ar": r"لاي تشينغ[- ]?تي", "vi": r"Lại Thanh Đức"}),
    ("蔣介石", r"蔣介石|蔣中正|中正|蔣公|老蔣|介石|蔣總統|兩蔣|蔣氏|去蔣",
     {**{l: r"\bChiang Kai-?shek\b" for l in LATIN}, "ja": r"蒋介石|蔣介石", "ko": r"장제스",
      "ru": r"Чан Кайши", "hi": r"च(?:ि)?यांग काई-?शेक", "ar": r"تشيانغ كاي", "vi": r"Tưởng Giới Thạch"}),
    # 第三十二輪擴表（主動結構掃描：同一個機制換一個名人）。實例：de 把捐款給黑熊學院的曹興誠寫成
    # Morris Chang、es／pt／id 把 1985 年的政務委員李國鼎寫成 Lee Teng-hui、成功大學被換成中山大學
    # （Sun Yat-sen）、蔣宋美齡寫成「蔣經國的妻子」。柯文哲、鄭成功沒收：抽樣裡譯者的補充語境
    # （「柯條款」「國姓爺之子鄭經」）占了一半，當驗收閘會擋到對的譯文。
    ("蔣經國", r"蔣經國|經國|小蔣|兩蔣|蔣氏|蔣總統|蔣家",
     {**{l: r"\bChiang Ching-?kuo\b" for l in LATIN}, "ja": r"蒋経国|蔣經國", "ko": r"장징궈",
      "ru": r"Цзян Цзинго", "vi": r"Tưởng Kinh Quốc"}),
    ("孫中山", r"孫中山|孫文|國父|中山|逸仙",
     {**{l: r"\bSun Yat-?sen\b" for l in LATIN}, "ja": r"孫文|孫中山", "ko": r"쑨원|쑨중산",
      "ru": r"Сунь Ятсен", "vi": r"Tôn Trung Sơn|Tôn Dật Tiên"}),
    ("李登輝", r"李登輝|李總統|李前總統",
     {**{l: r"\bLee Teng-?hui\b" for l in LATIN}, "ja": r"李登輝", "ko": r"리덩후이",
      "ru": r"Ли Дэнхуэй", "vi": r"Lý Đăng Huy"}),
    ("馬英九", r"馬英九|馬總統|馬政府|小馬哥|馬前總統",
     {**{l: r"\bMa Ying-?jeou\b" for l in LATIN}, "ja": r"馬英九", "ko": r"마잉주",
      "ru": r"Ма Инцзю", "vi": r"Mã Anh Cửu"}),
    ("陳水扁", r"陳水扁|阿扁|扁政府",
     {**{l: r"\bChen Shui-?bian\b" for l in LATIN}, "ja": r"陳水扁", "ko": r"천수이볜",
      "ru": r"Чэнь Шуйбянь", "vi": r"Trần Thủy Biển"}),
    ("張忠謀", r"張忠謀",
     {**{l: r"\bMorris Chang\b" for l in LATIN}, "ja": r"張忠謀|モリス・チャン", "ko": r"장중머우|모리스 창",
      "ru": r"Моррис Чан", "vi": r"Morris Chang|Trương Trung Mưu"}),
    ("郭台銘", r"郭台銘",
     {**{l: r"\bTerry Gou\b" for l in LATIN}, "ja": r"郭台銘|テリー・ゴウ", "ko": r"궈타이밍|테리 궈",
      "ru": r"Терри Гоу", "vi": r"Terry Gou|Quách Đài Minh"}),
    ("黃仁勳", r"黃仁勳",
     {**{l: r"\bJensen Huang\b" for l in LATIN}, "ja": r"ジェンスン・フアン|黄仁勲|黃仁勳", "ko": r"젠슨 황",
      "ru": r"Дженсен Хуанг", "vi": r"Jensen Huang|Hoàng Nhân Huân"}),
    ("唐鳳", r"唐鳳",
     {**{l: r"\bAudrey Tang\b" for l in LATIN}, "ja": r"オードリー・タン|唐鳳", "ko": r"오드리 탕",
      "ru": r"Одри Тан", "vi": r"Audrey Tang|Đường Phượng"}),
    ("鄧麗君", r"鄧麗君",
     {**{l: r"\bTeresa Teng\b" for l in LATIN}, "ja": r"テレサ・テン|鄧麗君", "ko": r"덩리쥔",
      "ru": r"Тереза Тенг|Дэн Лицзюнь", "vi": r"Đặng Lệ Quân"}),
    ("周杰倫", r"周杰倫|周董",
     {**{l: r"\bJay Chou\b" for l in LATIN}, "ja": r"ジェイ・チョウ|周杰倫", "ko": r"저우제룬|주걸륜",
      "ru": r"Джей Чоу|Чжоу Цзелунь", "vi": r"Châu Kiệt Luân|Jay Chou"}),
    ("蔡依林", r"蔡依林|Jolin",
     {**{l: r"\bJolin Tsai\b" for l in LATIN}, "ja": r"ジョリン・ツァイ|蔡依林", "ko": r"차이이린",
      "ru": r"Джолин Цай|Цай Илинь", "vi": r"Thái Y Lâm|Jolin Tsai"}),
    # 首都頂替：譯文語言所在國的首都，zh 連那個國家都沒提到
    ("河內", r"河內|河内|越南", {"vi": r"Hà Nội"}),
    ("胡志明市", r"胡志明|西貢|越南", {"vi": r"Hồ Chí Minh"}),
    ("雅加達", r"雅加達|印尼|印度尼西亞", {"id": r"\bJakarta\b"}),
    ("首爾", r"首爾|漢城|韓國|南韓|朝鮮", {"ko": r"서울"}),
    ("德里", r"德里|印度", {"hi": r"दिल्ली"}),
    ("莫斯科", r"莫斯科|俄羅斯|俄國|蘇聯|蘇俄", {"ru": r"\bМоскв"}),
]
_COMPILED = [(name, re.compile(zh), {l: re.compile(p) for l, p in forms.items()})
             for name, zh, forms in ENTITIES]


def check(lang, zh_text, tr_text):
    """回傳 [(名稱, 譯文命中次數)]：譯文提到、zh 原稿一個別名都沒有的名人／首都。"""
    hits = []
    # zh 原稿自己也會寫拉丁字：英文來源標題、Wikimedia 圖檔名（底線當空白）。那裡已經有這個名字，就不算頂替
    zh_latin = zh_text.replace("_", " ")
    for name, zh_re, forms in _COMPILED:
        form = forms.get(lang)
        if form is None or zh_re.search(zh_text) or form.search(zh_latin):
            continue
        n = len(form.findall(tr_text))
        if n:
            hits.append((name, n))
    return hits


def source_of(tr_path):
    head = tr_path.read_text(encoding="utf-8")[:3000]
    m = re.search(r"(?m)^translatedFrom:\s*['\"]?([^'\"\n]+?)['\"]?\s*$", head)
    return KNOWLEDGE / m.group(1) if m else None


def check_file(tr_path):
    rel = tr_path.resolve().relative_to(KNOWLEDGE.resolve())
    lang = rel.parts[0]
    if lang not in LANGS:
        return []
    zh_path = source_of(tr_path)
    if zh_path is None or not zh_path.is_file():
        return []
    return check(lang, zh_path.read_text(encoding="utf-8"), tr_path.read_text(encoding="utf-8"))


def all_translations():
    for lang in LANGS:
        yield from sorted((KNOWLEDGE / lang).rglob("*.md"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true", help="檢查全部譯文")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    paths = list(all_translations()) if args.all else [Path(f) for f in args.files]
    found = {}
    for p in paths:
        if p.name.startswith("_"):
            continue
        hits = check_file(p)
        if hits:
            found[p.resolve().relative_to(KNOWLEDGE.resolve()).as_posix()] = hits
    if args.json:
        print(json.dumps({"count": len(found), "files": {k: dict(v) for k, v in found.items()}},
                         ensure_ascii=False, indent=1))
    elif found:
        for rel, hits in found.items():
            print(f"{rel}: " + "、".join(f"{name}×{n}" for name, n in hits) + "（zh 原稿沒有提到）")
        print(f"\n{len(found)} 篇譯文出現 zh 原稿沒有的名人或首都")
    else:
        print("沒有名人頂替")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
