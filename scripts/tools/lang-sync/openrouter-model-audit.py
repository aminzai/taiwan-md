#!/usr/bin/env python3
"""openrouter-model-audit.py — 對賬程式碼裡寫死的 OpenRouter model slug 跟線上實況。

為什麼要這支：免費層的 model slug 會漂移，而**知道它漂移了的地方跟受它影響的地方
通常不是同一個檔案**。2026-07-24 有人在 `research-fleet.py` 的註解裡記下
「openai/gpt-oss-120b:free (lang-sync's own default) was retired by OpenRouter」，
自己換掉了自己的 DEFAULT_MODEL，然後那個事實在註解裡躺了六週——真正拿它當預設
cascade tier 2 的 `translate.py` 完全不知道，每次走預設路徑都白撞一次 404。

註解不會傳話，對賬會。這支就是把「現查 /api/v1/models」這個動作變成一行指令。

用法：
  python3 scripts/tools/lang-sync/openrouter-model-audit.py           # 人看
  python3 scripts/tools/lang-sync/openrouter-model-audit.py --json    # 給別的工具吃
exit 0 = 全部在架；exit 1 = 有 slug 下架了（cron 可以直接當閘）。
"""
import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
# 掃的範圍刻意含 lang-sync 以外的 scripts/tools：漂移的痛點正是「一支工具知道、
# 另一支不知道」，只掃自己那層就複製了原本的病。
SCAN = ["scripts/tools/lang-sync", "scripts/tools"]
# 射程刻意不限於 `:free`。第一版只掃免費 slug，結果漏掉 `openrouter/owl-alpha`——
# 它也下架了，而且就掛在 default backend chain 第一個 OpenRouter 位置上。閘門宣告
# 只蓋住一半的受災面，跟沒有閘門的差別只是它會給你綠燈（2026-09-08 maintainer 記
# 的 subcategory 閘門同病）。改成掃所有 `廠商/模型` 形狀，再用「廠商前綴出現在線上
# 清單裡」濾掉檔案路徑之類的假陽性。
SLUG = re.compile(r"['\"]([a-z0-9\-]+/[A-Za-z0-9._\-]+(?::[A-Za-z0-9._\-]+)?)['\"]")


def live_ids(timeout=20):
    with urllib.request.urlopen("https://openrouter.ai/api/v1/models", timeout=timeout) as r:
        return {m["id"]: m for m in json.load(r).get("data", [])}


def scan_repo(vendors):
    hits = {}
    seen = set()
    for root in SCAN:
        base = REPO / root
        if not base.exists():
            continue
        for f in sorted(base.rglob("*.py")) + sorted(base.rglob("*.sh")):
            if f in seen:
                continue
            seen.add(f)
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if "audit-ok:" in line:
                    continue  # 拒絕清單／墓碑條目：那一行本來就不打算呼叫它
                for slug in SLUG.findall(line):
                    if slug.split("/", 1)[0] not in vendors:
                        continue  # `scripts/tools` 之類的路徑，不是 model slug
                    hits.setdefault(slug, []).append(f"{f.relative_to(REPO)}:{i}")
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    try:
        live = live_ids()
    except Exception as e:
        print(f"❌ 查不到 OpenRouter 模型清單：{e}", file=sys.stderr)
        return 2
    hits = scan_repo({i.split("/", 1)[0] for i in live})

    dead = {s: locs for s, locs in hits.items() if s not in live}
    if args.json:
        print(json.dumps({
            "checked": len(hits), "dead": len(dead),
            "models": {s: {"live": s in live,
                           "context_length": live.get(s, {}).get("context_length"),
                           "refs": locs} for s, locs in sorted(hits.items())},
        }, ensure_ascii=False, indent=2))
        return 1 if dead else 0

    for slug, locs in sorted(hits.items()):
        ok = slug in live
        ctx = live.get(slug, {}).get("context_length", "-")
        print(f"{'✅' if ok else '❌'} {slug:52s} ctx={ctx}")
        if not ok:
            for loc in locs:
                print(f"      ↳ {loc}")
    print()
    if dead:
        # 付費版通常還在（下架的多半只有 :free 那格），順手指路省一次查詢
        for slug in sorted(dead):
            paid = slug.removesuffix(":free")
            if paid != slug and paid in live:
                print(f"   提示：`{paid}`（付費版）仍在架，ctx={live[paid].get('context_length')}")
        print(f"════ {len(hits)} 個 slug，{len(dead)} 個已下架——改掉引用處，別留在 cascade 裡白撞 ════")
        return 1
    print(f"════ {len(hits)} 個 slug 全部在架 ════")
    return 0


if __name__ == "__main__":
    sys.exit(main())
