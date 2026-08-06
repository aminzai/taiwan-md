#!/usr/bin/env python3
"""語言分支樹資料生成器（prebuild）。

SSOT 分工（reports/design-fork-graph-evolution-2026-08-04.md §3.2）：
- data/terminology/*.yaml         — 語言內容（display / fork_type / origin 敘事 / fork_point）
- data/terminology/_fork-graph-featured.yaml — 策展層（精選詞時間軸座標＋世代短文）
輸出 src/data/fork-graph.json（gitignored derived）。

fail-loud：featured id 不存在於詞庫 → exit 1。
fork_point parse 統計印 stdout；parse 失敗條目列出（不進資料、不擋 build）。
"""

import glob
import json
import os
import re
import sys

import yaml

# Windows cp950 console 強制 UTF-8（不影響 Linux/macOS）
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
TERM_DIR = os.path.join(ROOT, "data", "terminology")
FEATURED = os.path.join(TERM_DIR, "_fork-graph-featured.yaml")
OUT = os.path.join(ROOT, "src", "data", "fork-graph.json")

VALID_TYPES = {"A", "B", "C", "D", "E", "F"}
TYPE_MAP = {"semantic": "F", "orthographic": "F"}  # 舊值歸入最近類


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def first_variant(s):
    """display 欄常是「A / B / C」，圖上取第一個變體保持簡潔。"""
    return re.split(r"\s*/\s*", str(s or "").strip())[0].strip()


def parse_fork_year(raw):
    """~1950s / ~1974 / ~1895前 / ~1895（日治底層）/ ~1949… → 第一個四位數年份。"""
    m = re.search(r"(18\d\d|19\d\d|20\d\d)", str(raw or ""))
    return int(m.group(1)) if m else None


def main():
    curation = load_yaml(FEATURED)

    # ── 全庫掃描：密度層 + featured 內容源 ──
    lib = {}
    density_terms = []
    parse_fail = []
    for path in sorted(glob.glob(os.path.join(TERM_DIR, "*.yaml"))):
        if os.path.basename(path).startswith("_"):
            continue
        try:
            d = load_yaml(path)
        except Exception:
            continue
        if not d:
            continue
        fid = os.path.basename(path)[:-5]
        lib[fid] = d
        et = d.get("etymology") or {}
        fp = et.get("fork_point")
        if not fp:
            continue
        yr = parse_fork_year(fp)
        disp = d.get("display") or {}
        tw, cn = first_variant(disp.get("taiwan")), first_variant(disp.get("china"))
        if yr is None:
            parse_fail.append((fid, str(fp)))
            continue
        if not tw or not cn or tw == cn:
            continue  # neutralized / 同形條目不進密度層
        ftype = str(d.get("fork_type") or "")
        ftype = TYPE_MAP.get(ftype, ftype)
        if ftype not in VALID_TYPES:
            continue
        density_terms.append({"id": fid, "tw": tw, "cn": cn, "type": ftype, "year": yr})

    # ── 精選層：merge 詞庫內容 ──
    featured_out = []
    missing = []
    for item in curation["featured"]:
        fid = item["id"]
        d = lib.get(fid)
        if d is None:
            missing.append(fid)
            continue
        disp = d.get("display") or {}
        et = d.get("etymology") or {}
        ftype = item.get("type") or TYPE_MAP.get(str(d.get("fork_type")), str(d.get("fork_type")))
        origin_prose = str(et.get("origin") or "").strip()
        note = origin_prose if origin_prose else str(item.get("note") or "")
        if len(note) > 118:
            note = note[:115].rstrip("，。；、 ") + "⋯"
        featured_out.append(
            {
                "id": fid,
                "origin": item["origin"],
                "originYear": item["originYear"],
                "forkYear": item["forkYear"],
                "taiwan": str(item.get("twLabel") or first_variant(disp.get("taiwan"))),
                "china": str(item.get("cnLabel") or first_variant(disp.get("china"))),
                "type": ftype,
                "note": note,
                "curatorNote": str(item.get("note") or ""),
                "hasPage": first_variant(disp.get("taiwan")) != first_variant(disp.get("china")),
            }
        )
    if missing:
        print(f"❌ featured id 不存在於詞庫：{missing}", file=sys.stderr)
        sys.exit(1)

    density_ids = {t["id"] for t in density_terms}
    for f_item in featured_out:
        if f_item["id"] not in density_ids and f_item["taiwan"] != f_item["china"]:
            density_terms.append(
                {"id": f_item["id"], "tw": f_item["taiwan"], "cn": f_item["china"],
                 "type": f_item["type"], "year": f_item["forkYear"]}
            )

    featured_out.sort(key=lambda x: (x["forkYear"], x["originYear"]))

    # ── 密度層：per-decade × type ──
    decades = {}
    for t in density_terms:
        dec = (max(t["year"], 1890) // 10) * 10
        cell = decades.setdefault(dec, {"decade": dec, "total": 0, "byType": {}, "terms": []})
        cell["total"] += 1
        cell["byType"][t["type"]] = cell["byType"].get(t["type"], 0) + 1
        cell["terms"].append({"id": t["id"], "tw": t["tw"], "cn": t["cn"], "type": t["type"]})
    density = [decades[k] for k in sorted(decades)]
    for cell in density:
        cell["terms"].sort(key=lambda x: (x["type"], x["id"]))


    by_type_lib = {}
    for d in lib.values():
        ftype = TYPE_MAP.get(str(d.get("fork_type")), str(d.get("fork_type")))
        if ftype in VALID_TYPES:
            by_type_lib[ftype] = by_type_lib.get(ftype, 0) + 1

    out = {
        "featured": featured_out,
        "eraEssays": curation["era_essays"],
        "density": density,
        "counts": {
            "featured": len(featured_out),
            "densityTerms": len(density_terms),
            "libraryTotal": len(lib),
            "byTypeLibrary": by_type_lib,
            "yearSpan": [
                min(x["originYear"] for x in featured_out),
                max(max(x["forkYear"] for x in featured_out), max((t["year"] for t in density_terms), default=2026)),
            ],
        },
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    print(
        f"✅ fork-graph.json：精選 {len(featured_out)} 詞｜密度層 {len(density_terms)} 條"
        f"（fork_point parse 失敗 {len(parse_fail)}）｜詞庫 {len(lib)} 條"
    )
    if parse_fail:
        for fid, raw in parse_fail[:10]:
            print(f"   ⚠️ parse 失敗：{fid} fork_point={raw!r}", file=sys.stderr)


if __name__ == "__main__":
    main()
