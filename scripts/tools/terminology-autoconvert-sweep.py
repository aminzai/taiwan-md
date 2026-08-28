#!/usr/bin/env python3
"""terminology-autoconvert-sweep.py — 用我們自己寫的台灣中文，找出會被誤轉的詞條

誕生 2026-08-28（twmd-maintainer-am）：讀者回報用語轉換器把社群文章裡的
「粉絲」轉成「冬粉」（issue #1613）。詞庫裡 `粉絲.yaml` 寫 china: 粉絲 →
taiwan: 冬粉 —— 那是食物那個義項，在「藝人的粉絲」這個義項裡台灣本來就講粉絲。

轉換器早在 2026-08-22 就有 `auto_convert: false` 這個開關（為了「挺胸 → 蠻胸」
而生），機制不缺。缺的是**有沒有東西在系統性地找出哪些詞條該掛這個旗子** ——
在此之前每一個都要等讀者先撞到一次。這支就是那個東西。

判準：拿轉換器真正會用的那份規則，去掃 knowledge/ 的中文 SSOT。
knowledge/*.md 是台灣人用台灣話寫的、過了編輯閘門的正文 —— 如果一條規則
會去改我們自己寫的東西，那條規則八成在某個義項上是錯的。

這是 dogfood 不是猜測：命中數就是「這條規則上線後會改壞幾處我們自己的字」。

用法：
    python3 scripts/tools/terminology-autoconvert-sweep.py              # 報告
    python3 scripts/tools/terminology-autoconvert-sweep.py --min-hits 20
    python3 scripts/tools/terminology-autoconvert-sweep.py --json out.json

輸出是**候選清單不是判決**：命中高也可能是真的該轉（那個詞在台灣本來就少用），
逐條要人看。詞庫的策展門檻在 OBSERVER-QUEUE #11，屬哲宇。
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 pyyaml：pip install pyyaml")

REPO = Path(__file__).resolve().parents[2]
TERM_DIR = REPO / "data" / "terminology"
KNOWLEDGE = REPO / "knowledge"

# 中文語系的目錄名（其餘是譯文，不能拿來當「台灣人怎麼寫」的證據）
LANG_DIRS_TO_SKIP = {
    "en", "ja", "ko", "es", "fr", "ar", "hi", "id", "ru", "pt", "vi", "de",
}


def clean_china_source(raw: str) -> str:
    """逐行對齊 converter.astro 的 cleanChinaSource。

    順序很重要，不能自己重寫一個「意思差不多」的版本：`N/A（概念差異）`
    要先被 startswith('N/A') 擋掉，如果先去括號再切斜線，它會變成單一個
    字母 `N`，然後這支就會報告「有一條規則要把全站的 N 換成已讀」。
    第一版真的這樣報了 7,661 次命中 —— 稽核工具跟被稽核的對象用不同的尺，
    量出來的是尺的差異不是對象的問題（REFLEXES #83）。
    """
    if not raw:
        return ""
    s = str(raw)
    if s.startswith("N/A") or s.startswith("（無"):
        return s
    s = re.sub(r"（[^）]*）", "", s)
    s = re.sub(r"\([^)]*\)", "", s)
    if "/" in s:
        s = s.split("/")[0]
    return s.strip()


def load_rules():
    """讀出轉換器實際會套用的那份規則（已經 opt out 的不算）。"""
    rules = []
    skipped_opt_out = 0
    for f in sorted(TERM_DIR.glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        try:
            d = yaml.safe_load(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        if d.get("auto_convert") is False:
            skipped_opt_out += 1
            continue
        disp = d.get("display") or {}
        china = disp.get("china") or d.get("china")
        taiwan = disp.get("taiwan") or d.get("taiwan")
        if not china or not taiwan or china == taiwan:
            continue
        cleaned = clean_china_source(china)
        if not cleaned or cleaned == taiwan:
            continue
        if cleaned.startswith("N/A") or cleaned.startswith("（無"):
            continue
        # 單字規則本來就危險，但那是另一條路的問題；這裡照收，交給命中數說話
        rules.append({
            "file": f.name,
            "id": d.get("id") or f.stem,
            "china": cleaned,
            "taiwan": taiwan,
            "subcategory": d.get("subcategory") or "",
            "sources": d.get("sources") or [],
        })
    return rules, skipped_opt_out


def zh_corpus_files():
    """只收中文 SSOT。譯文目錄跳過。"""
    for p in KNOWLEDGE.rglob("*.md"):
        rel = p.relative_to(KNOWLEDGE)
        if rel.parts and rel.parts[0] in LANG_DIRS_TO_SKIP:
            continue
        yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-hits", type=int, default=10,
                    help="命中幾次以上才列出來（預設 10）")
    ap.add_argument("--top", type=int, default=40, help="最多列幾條")
    ap.add_argument("--json", help="把完整結果寫成 JSON")
    args = ap.parse_args()

    rules, opted_out = load_rules()
    files = list(zh_corpus_files())
    corpus = []
    for p in files:
        try:
            corpus.append(p.read_text(encoding="utf-8"))
        except Exception:
            continue
    blob = "\n".join(corpus)

    hits = []
    for r in rules:
        n = blob.count(r["china"])
        if n:
            hits.append({**r, "hits": n})
    hits.sort(key=lambda x: -x["hits"])

    print(f"\n════════ 會改到我們自己中文的轉換規則 ════════")
    print(f"  中文 SSOT：{len(files)} 篇 / 轉換規則：{len(rules)} 條"
          f"（已 opt out：{opted_out} 條）")
    print(f"  會命中自家正文的規則：{len(hits)} 條\n")

    shown = [h for h in hits if h["hits"] >= args.min_hits][: args.top]
    if not shown:
        print(f"  沒有規則命中自家正文 ≥ {args.min_hits} 次。\n")
    else:
        print(f"  {'命中':>5}  {'中國詞':<10} → {'台灣詞':<12}  詞條")
        print("  " + "─" * 62)
        for h in shown:
            print(f"  {h['hits']:>5}  {h['china']:<10} → {h['taiwan']:<12}  {h['file']}")
        print(f"""
  命中數 = 這條規則上線後會改動我們自己寫的台灣中文幾處。
  高命中通常代表那個詞在台灣本來就通用，只是在另一個義項上跟中國用法撞名
  —— 那種要在詞條加 `auto_convert: false`（詞條頁照樣解釋語感差異，
  只是不進find-and-replace）。

  但這是候選不是判決：也有可能那個詞真的該轉，而我們自己的文章正好寫錯了。
  逐條要人看。詞庫的策展門檻屬哲宇（OBSERVER-QUEUE #11）。
""")

    if args.json:
        Path(args.json).write_text(
            json.dumps({"corpus_files": len(files), "rules": len(rules),
                        "opted_out": opted_out, "hits": hits},
                       ensure_ascii=False, indent=2),
            encoding="utf-8")
        print(f"  完整結果 → {args.json}\n")


if __name__ == "__main__":
    main()
