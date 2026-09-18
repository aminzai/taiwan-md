#!/usr/bin/env python3
"""babel-weak-lanes.py — 從近兩日 dispatcher 實績算出弱適配的 backend×語言，
印成 babel-dispatch.py 的 `--worker-skip-langs label=lang,lang` 旗標。

用法（wrapper 內）：
    SKIP="$(python3 scripts/tools/lang-sync/babel-weak-lanes.py $FLEET_WORKERS \
              --worker nemo=openrouter:... --worker lagunas=openrouter:...)"
    python3 scripts/tools/lang-sync/babel-dispatch.py ... $SKIP

為什麼按 backend 不按 label 聚合：fleet 對同一台 ollama 核發 macm4max1/2/3
三個 label，同一個模型的實績被拆成三格，preflight 只在其中一格 n≥8 且 <15%
時警示（09-19 實例：macm4max3 × ar 6% n=31 被報，macm4max1 × ar 同模型沒被報）。
切軌的單位是模型，不是 label。

門檻沿用 babel-preflight.py：n ≥ 8 且通過率 < 15%，視窗 2 天。
starvation guard 由 babel-dispatch.py 做（某語言不能被全部 worker 跳過）；
本工具只負責出證據，不做最後裁決。

--explain 印出每個弱格的數字到 stderr（收官 memory 用）。
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta

MIN_N = 8
MAX_PASS = 0.15


def parse_workers(raw_list: list[str]) -> dict[str, str]:
    """label=spec[@host] → {label: spec}（@host 剝掉，跟 dispatcher 同規則）。"""
    out = {}
    for raw in raw_list:
        if "=" not in raw:
            continue
        label, _, rest = raw.partition("=")
        spec, _, _host = rest.partition("@")
        out[label.strip()] = spec.strip()
    return out


def backend_lang_grid(days: int) -> dict[tuple[str, str], list[int]]:
    cut = (datetime.now().astimezone() - timedelta(days=days)).isoformat()
    grid: dict[tuple[str, str], list[int]] = defaultdict(lambda: [0, 0])
    for rp in glob.glob("/tmp/babel-unified-2*/report.jsonl"):
        try:
            with open(rp, encoding="utf-8") as fh:
                for line in fh:
                    try:
                        r = json.loads(line)
                    except Exception:
                        continue
                    if r.get("ts", "") < cut or "backend" not in r or "lang" not in r:
                        continue
                    if r.get("event"):  # cascade_exhausted / cap_reached 等事件列不是嘗試
                        continue
                    grid[(r["backend"], r["lang"])][0 if r.get("ok") else 1] += 1
        except Exception:
            continue
    return grid


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--worker", action="append", dest="workers", default=[], metavar="label=spec[@host]")
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--explain", action="store_true", help="print the weak cells to stderr")
    args = ap.parse_args()

    workers = parse_workers(args.workers)
    grid = backend_lang_grid(args.days)
    weak: dict[str, set[str]] = defaultdict(set)  # backend -> langs
    for (backend, lang), (ok, fail) in sorted(grid.items()):
        n = ok + fail
        if n >= MIN_N and ok / n < MAX_PASS:
            weak[backend].add(lang)
            if args.explain:
                print(f"weak  {backend} × {lang}: {ok}/{n} = {ok / n * 100:.0f}%", file=sys.stderr)

    flags = []
    for label, spec in workers.items():
        langs = weak.get(spec)
        if langs:
            flags.append(f"--worker-skip-langs {label}={','.join(sorted(langs))}")
    print(" ".join(flags))


if __name__ == "__main__":
    main()
