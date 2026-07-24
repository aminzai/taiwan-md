#!/usr/bin/env python3
"""progress-snapshot.py — 巴別塔同步率時間序列快照。

把 status.py 的九語 fresh/stale/missing 讀數 append 到
.taiwanmd/babel-progress.jsonl（本機、gitignored 目錄），給每小時
視覺化報告算 delta 與 throughput 用。跑一次 append 一列。

用法：
  python3 scripts/tools/lang-sync/progress-snapshot.py          # 快照 + append
  python3 scripts/tools/lang-sync/progress-snapshot.py --last 5 # 印最近 N 列
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / ".taiwanmd" / "babel-progress.jsonl"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from langs import ALL_TRANSLATION_LANGS  # noqa: E402


def snapshot() -> dict:
    subprocess.run(
        ["python3", "scripts/tools/lang-sync/status.py"],
        cwd=REPO, capture_output=True, text=True,
    )
    data = json.loads((REPO / "knowledge" / "_translation-status.json").read_text())
    summary = data["_meta"]["summary"]
    row = {"ts": datetime.now().astimezone().isoformat(timespec="seconds"),
           "total_zh": data["_meta"]["totalZh"], "langs": {}}
    for lang in ALL_TRANSLATION_LANGS:
        s = summary.get(lang, {})
        row["langs"][lang] = {
            "fresh": s.get("fresh", 0),
            "stale": s.get("stale", 0) + s.get("metadata_stale", s.get("metadataStale", 0)),
            "missing": s.get("missing", 0),
        }
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--last", type=int, default=0)
    args = ap.parse_args()
    if args.last:
        lines = OUT.read_text().splitlines() if OUT.exists() else []
        for ln in lines[-args.last:]:
            print(ln)
        return
    row = snapshot()
    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps(row, ensure_ascii=False))


if __name__ == "__main__":
    main()
