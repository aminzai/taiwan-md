#!/usr/bin/env python3
"""
sibling-slug-map.py — 從兄弟語言反查一篇文章已經在用的 slug，產出 prepare-batch 的 --slug-map。

為什麼需要這支：
  同一篇 zh 文章翻到第 N 個語言時，前面 N-1 個語言早就替它訂好一個 slug 了。
  讓 agent（或 prepare-batch 的 ASCII fallback）重新發明一個，會產生跨語言不一致的
  路徑——讀者在語言切換器按一下就落到 404，而且這種不一致沒有任何閘門在看。
  2026-08-09 vi 委派 200 篇是手工反查的（182/200 命中），SQUEEZE §委派層 SOP §一
  因此明寫「slug 一律先從兄弟語言反查」，但當時沒有留下工具，下一批又得重做一次。
  這支就是那次手工步驟的儀器化（VORTEX §儀器化第 2 條：同一件事做第二次就該儀器化）。

為什麼優先序是這個順序而不是隨便挑一個兄弟：
  en 排第一是因為它是最早、也最常被人工審過的一批，slug 品質最穩。之後排的是
  拉丁字母書寫系統的語言（它們的 slug 天生就是 ASCII，不經過轉寫）。ja/ko 排最後
  不是品質問題，是它們的 slug 更常出現「照日文漢字音讀轉寫」的形狀，跨語言辨識度較低。
  取到第一個就停——不做投票，因為多數決在只有兩三個兄弟時沒有意義，
  而且會讓結果隨著哪些語言先翻完而漂移。

用法：
  python3 scripts/tools/lang-sync/sibling-slug-map.py --lang de --out /tmp/de-slugs.json
  python3 scripts/tools/lang-sync/sibling-slug-map.py --lang de --input /tmp/paths.txt --out ...
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
STATUS = REPO / "knowledge" / "_translation-status.json"

# 見 docstring §為什麼優先序是這個順序
SIBLING_PRIORITY = ["en", "es", "fr", "pt", "id", "vi", "ru", "ar", "hi", "de", "ja", "ko"]


def load_status() -> dict:
    """`_translation-status.json` 的 byArticle 就是 slug 與 missing 兩件事的同一份 SSOT。
    刻意不另外讀 `_translations.json` 或掃目錄：兩個來源會在 quarantine／未 commit 的
    空窗期給出不同答案，而這支工具的輸出會直接變成檔案路徑，錯了就是永久的死鏈。"""
    return json.loads(STATUS.read_text(encoding="utf-8"))["byArticle"]


def target_paths(by_article: dict, lang: str) -> list[str]:
    """該語言目前 missing 的 zh_path：translations 裡沒有這個 lang，或它的 status 是 missing。"""
    out = []
    for zh_path, entry in by_article.items():
        t = entry.get("translations", {}).get(lang)
        if t is None or t.get("status") == "missing":
            out.append(zh_path)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True, help="要產 slug-map 的目標語言")
    ap.add_argument("--input", help="zh_path 清單檔（一行一個）；省略則取該語言全部 missing")
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, help="只取前 N 筆（配合 prepare-batch --top）")
    args = ap.parse_args()

    by_article = load_status()
    if args.input:
        paths = [l.strip() for l in Path(args.input).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        paths = target_paths(by_article, args.lang)
    if args.limit:
        paths = paths[: args.limit]

    slug_map: dict[str, str] = {}
    donors: Counter[str] = Counter()
    unresolved: list[str] = []
    for zh in paths:
        siblings = by_article.get(zh, {}).get("translations", {})
        for lang in SIBLING_PRIORITY:
            if lang == args.lang:
                continue
            sib = siblings.get(lang)
            # status=missing 的兄弟其實沒有檔案，它的 path 是推算值不是既成事實，不能當來源
            if sib and sib.get("status") != "missing" and sib.get("path"):
                slug_map[zh] = Path(sib["path"]).stem
                donors[lang] += 1
                break
        else:
            unresolved.append(zh)

    Path(args.out).write_text(json.dumps(slug_map, ensure_ascii=False, indent=1), encoding="utf-8")

    total = len(paths)
    hit = len(slug_map)
    print(f"🔤 兄弟語言 slug 反查 — {args.lang}")
    print(f"   命中 {hit}/{total}（{hit * 100 // max(total, 1)}%）→ {args.out}")
    if donors:
        print("   來源分布：" + "、".join(f"{l} {n}" for l, n in donors.most_common()))
    if unresolved:
        # 這批要嘛是全新文章（沒有任何語言翻過），要嘛是 zh 檔名剛改過。
        # 交給 prepare-batch 的 ASCII fallback 或人工命名，不在這裡猜。
        print(f"   ⚠️ {len(unresolved)} 篇沒有任何兄弟語言可反查（全新文章 / zh 檔名剛異動）：")
        for zh in unresolved[:8]:
            print(f"      {zh}")


if __name__ == "__main__":
    main()
