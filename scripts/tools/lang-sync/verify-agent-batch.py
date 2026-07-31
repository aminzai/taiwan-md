#!/usr/bin/env python3
"""verify-agent-batch.py — 驗收「sub-agent 批次翻譯」的產出，並跟 agent 自述對帳。

## 為什麼有這支

2026-07-31 用 Claude sub-agent 批次委派翻譯（Haiku 打頭陣、失敗升 Sonnet），
一批 50 篇。Agent 回報 48/49 通過，主 session 獨立複驗實際是 47——**差一篇**。
REFLEXES #31「sub-agent claim 是線索不是事實」再次成立，但當時的複驗是主
session 現寫的 python 迴圈貼在對話裡，跑一次丟一次：

- 跑第三次的時候我還在複製貼上同一段程式（§儀器化第 2 條：同一件事做第二次
  就該儀器化，判準是次數不是難度）
- 而且那個手寫迴圈只跑三道閘門，`verify-batch.py` 其實早就把八步串好了
  （§儀器化「動手前先查既有工具」——今晚正是因為沒查而重造過輪子）

所以這支**不自己實作檢查**，只做兩件既有工具做不到的事：
1. 把 agent 批次的任務清單（`[{zh, target, ...}]`）轉成 `verify-batch.py`
   吃的 manifest 形狀，讓批次驗收走既有那把尺
2. 跟 agent 自述的 pass/fail 對帳，把「宣稱通過但實際沒過」的差額印出來
   ——這一項是 agent 委派特有的風險，既有工具沒有對應概念

## 用法

  # 只驗收
  verify-agent-batch.py --tasks /tmp/batch1-args.json --lang vi

  # 驗收 + 跟 agent 自述對帳（claims 是 workflow 回傳的 details 陣列）
  verify-agent-batch.py --tasks tasks.json --lang vi --claims claims.json

claims JSON 形狀：`[{"target": "vi/...", "passed": true}, ...]`
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent.parent
KN = REPO / "knowledge"
HERE = Path(__file__).resolve().parent


def to_manifest(tasks: list[dict], lang: str) -> dict:
    """agent 任務清單 → verify-batch.py 的 manifest 形狀。

    verify-batch 的欄位名沿用它 en-only 時代的歷史（`en_path`），實際上是
    「譯文路徑」；這裡照它的期待填，不改它的 schema——改共用工具的介面會
    波及其他呼叫端，轉接成本應該由新來的這支承擔。
    """
    return {
        "lang": lang,
        "articles": [
            {"zh_path": f"knowledge/{t['zh']}", "en_path": f"knowledge/{t['target']}"}
            for t in tasks
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tasks", required=True, help="agent 批次任務 JSON")
    ap.add_argument("--lang", required=True)
    ap.add_argument("--claims", help="agent 自述結果 JSON（有就對帳）")
    args = ap.parse_args()

    tasks = json.loads(Path(args.tasks).read_text(encoding="utf-8"))
    if isinstance(tasks, str):          # Workflow args 可能以字串抵達
        tasks = json.loads(tasks)

    # 1) 缺檔先報（verify-batch 也會報，但這裡要先算進對帳基數）
    missing = [t["target"] for t in tasks if not (KN / t["target"]).exists()]

    # 2) 走既有那把尺
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     encoding="utf-8") as fh:
        json.dump(to_manifest(tasks, args.lang), fh, ensure_ascii=False)
        manifest_path = fh.name
    proc = subprocess.run(
        [sys.executable, str(HERE / "verify-batch.py"), manifest_path],
        cwd=REPO, capture_output=True, text=True,
    )
    print(proc.stdout[-6000:])
    if proc.returncode != 0 and proc.stderr.strip():
        print(proc.stderr[-1500:], file=sys.stderr)

    # 3) 逐檔三閘門（verify-batch 涵蓋批次層，這裡補逐檔 hard-gate 判定）
    passed, failed = [], []
    for t in tasks:
        p = f"knowledge/{t['target']}"
        if t["target"] in missing:
            failed.append((t["target"], "檔案不存在"))
            continue
        r1 = subprocess.run([sys.executable, str(HERE / "verify-translation.py"),
                             t["zh"], p, "--json"], cwd=REPO, capture_output=True, text=True)
        try:
            fails = json.loads(r1.stdout).get("fails", -1)
        except Exception:
            fails = -1
        r2 = subprocess.run([sys.executable, str(HERE / "cjk-leak-check.py"), p],
                            cwd=REPO, capture_output=True, text=True)
        leak = "0/1 files flagged" not in r2.stdout
        r3 = subprocess.run([sys.executable, str(REPO / "scripts/tools/article-health.py"),
                             p, "--profile=pre-commit", "--output=json"],
                            cwd=REPO, capture_output=True, text=True)
        try:
            health = bool(json.loads(r3.stdout)["reports"][0]["effective_passed"])
        except Exception:
            health = False
        if fails == 0 and not leak and health:
            passed.append(t["target"])
        else:
            failed.append((t["target"], f"verify_fails={fails} leak={leak} health={health}"))

    print(f"\n=== 逐檔硬閘門 ===\n✅ 通過 {len(passed)} / ❌ 未過 {len(failed)}")
    for tgt, why in failed:
        print(f"   {tgt} — {why}")

    # 4) 跟 agent 自述對帳（agent 委派特有風險，既有工具沒有這個概念）
    if args.claims:
        claims = json.loads(Path(args.claims).read_text(encoding="utf-8"))
        claimed = {c["target"].replace("knowledge/", ""): bool(c.get("passed"))
                   for c in claims}
        actual = {t: True for t in passed} | {t: False for t, _ in failed}
        overclaim = sorted(t for t, ok in actual.items()
                           if not ok and claimed.get(t) is True)
        underclaim = sorted(t for t, ok in actual.items()
                            if ok and claimed.get(t) is False)
        print(f"\n=== 與 agent 自述對帳 ===")
        print(f"agent 宣稱通過 {sum(1 for v in claimed.values() if v)} / 實際通過 {len(passed)}")
        if overclaim:
            print(f"⚠️  宣稱過但實際沒過 {len(overclaim)} 篇（REFLEXES #31）:")
            for t in overclaim:
                print(f"     {t}")
        if underclaim:
            print(f"ℹ️  宣稱沒過但實際過了 {len(underclaim)} 篇（agent 過度保守）:")
            for t in underclaim:
                print(f"     {t}")
        if not overclaim and not underclaim:
            print("✅ 自述與實測一致")

    Path(manifest_path).unlink(missing_ok=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
