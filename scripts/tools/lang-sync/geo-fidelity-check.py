#!/usr/bin/env python3
"""geo-fidelity-check.py — 譯文地理主權保真度檢查（幻覺式地點遷移偵測）。

2026-07-18 出生戰役 heal agent 揭露：vi 譯文把「台北圓環」（二二八事件引爆點）
譯成「Bắc Kinh」（北京）——把台灣的定義性歷史創傷遷到中國首都。這是 CJK 殘留
檢查結構上抓不到的語意錯誤，且是 sovereignty red line（MANIFESTO §10 幻覺鐵律
＋主權的巴別塔：譯文不該把台灣的事搬到中國）。

機制：對每個 (zh source, translation) 對，數中國地名標記在譯文 vs zh 源的出現數。
若譯文提到北京/上海/中國大陸而 zh 源完全沒有對應原詞 → 幻覺式遷移，flag 人審。
保守設計：只抓「譯文有、源頭零」的強訊號，避免正常提及中國的文章誤報。

用法：
    python3 geo-fidelity-check.py --lang vi           # 掃 knowledge/vi/ 全部
    python3 geo-fidelity-check.py --files a.md b.md
Exit 1 = 有可疑遷移。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
KNOWLEDGE = REPO / "knowledge"

# 中國地名/主權標記在各語言的形式。key = zh 源要對照的原詞（zh 源有這詞才算合法）。
# 每個 marker：譯文形式的 regex（各語言）＋ zh 源對照詞（source 有任一即豁免該行）。
MARKERS = [
    {
        "name": "Beijing 北京",
        # 只有 zh 源真的含「北京」才整檔豁免。京劇/天安門 不放檔級豁免——否則一篇
        # 同時有合法天安門對照段＋台北→北京 幻覺的文章（如 taiwan-democratization）
        # 會被整檔跳過，真錯藏住（2026-07-18 首版踩過）。Beijing opera 走行級豁免。
        "zh_terms": ["北京"],
        "target": re.compile(r"\bBắc Kinh\b|\bBeijing\b|\bPequim\b|बीजिंग|北京", re.I),
        # 譯文行本身是 Beijing/Peking opera（京劇）語境 → 該行合法（Tiananmen「Thiên An
        # Môn」等本就不被 target 命中，不需豁免）
        "line_exempt": re.compile(
            r"opera|ópera|ôpêra|kinh kịch|ओपेरा|京剧|京劇|京戲", re.I
        ),
    },
    {
        "name": "Shanghai 上海",
        "zh_terms": ["上海"],
        "target": re.compile(r"\bThượng Hải\b|\bShanghai\b|\bXangai\b|शंघाई|上海", re.I),
    },
    {
        "name": "China-mainland 中國大陸",
        # 加 外省/眷村（1949 mainlander 移民史是台灣史正題，譯文說 mainland 合法）
        "zh_terms": ["中國大陸", "中国大陆", "大陸", "大陆", "外省", "眷村"],
        # 只抓明確「中國大陸」複合詞，不抓單獨 China（正常提及中國太多）
        "target": re.compile(
            r"Trung Quốc đại lục|Tiongkok daratan|China continental|"
            r"चीन की मुख्य भूमि|中國大陸|中国大陆",
            re.I,
        ),
    },
]


def strip_frontmatter(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[m.end():] if m else text


def find_zh_source(trans_path: Path) -> Path | None:
    """從 translatedFrom frontmatter 找 zh 源。"""
    text = trans_path.read_text(encoding="utf-8")
    m = re.search(r"^translatedFrom:\s*['\"]?([^'\"\n]+)['\"]?", text, re.M)
    if not m:
        return None
    zh_rel = m.group(1).strip()
    p = KNOWLEDGE / zh_rel
    return p if p.exists() else None


def check_file(trans_path: Path):
    zh_path = find_zh_source(trans_path)
    if zh_path is None:
        return [("NO_ZH_SOURCE", 0, "translatedFrom 指向不存在的 zh 源")]
    zh_body = strip_frontmatter(zh_path.read_text(encoding="utf-8"))
    trans_text = trans_path.read_text(encoding="utf-8")
    trans_body = strip_frontmatter(trans_text)
    offset = trans_text[: len(trans_text) - len(trans_body)].count("\n")

    hits = []
    for marker in MARKERS:
        # zh 源有對應原詞 → 該 marker 整篇合法，跳過
        if any(t in zh_body for t in marker["zh_terms"]):
            continue
        # zh 源零對應，但譯文出現 → 逐行 flag（該行本身若是合法語境如 Beijing opera 則跳過）
        line_exempt = marker.get("line_exempt")
        for i, line in enumerate(trans_body.splitlines(), start=offset + 1):
            if marker["target"].search(line):
                if line_exempt and line_exempt.search(line):
                    continue
                hits.append((marker["name"], i, line.strip()[:90]))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang")
    ap.add_argument("--files", nargs="*")
    args = ap.parse_args()

    if args.files:
        files = [Path(f) for f in args.files]
    elif args.lang:
        files = sorted((KNOWLEDGE / args.lang).rglob("*.md"))
    else:
        ap.error("--lang or --files required")

    total = 0
    for f in files:
        hits = check_file(f)
        if hits:
            total += len(hits)
            rel = f.relative_to(REPO) if f.is_absolute() else f
            print(f"⚠️  {rel}")
            for name, line_no, ctx in hits[:6]:
                print(f"    [{name}] L{line_no}: {ctx}")
    if total:
        print(f"\n❌ {total} 處可疑地理遷移（譯文提中國地點但 zh 源無對應原詞）— 需人審")
        sys.exit(1)
    print(f"✅ {len(files)} 檔無可疑地理遷移")


if __name__ == "__main__":
    main()
