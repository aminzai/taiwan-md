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
    for name, zh_re, forms in _COMPILED:
        form = forms.get(lang)
        if form is None or zh_re.search(zh_text):
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
