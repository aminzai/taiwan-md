#!/usr/bin/env python3
"""把 `npm audit --json` 的輸出收斂成 npm-audit-sweep.sh 讀得懂的幾行。

stdin 收 npm audit 的 JSON，stdout 第一行是
    OK <high 數> <critical 數> <只有 breaking change 修得掉的數>
之後每行一條 high 以上的公告：
    <severity>\t<套件>\t<fix>

fix 欄回答當班唯一要問的那一句「這條修補在不在小版本內」：
    minor               有非 semver-major 的修補 → 本班 npm audit fix 收得掉
    MAJOR(<pkg>@<ver>)  只有 breaking change 修得掉 → 是決定不是 heal
    none                上游還沒有修補（公告範圍涵蓋所有版本）→ 同上

解析失敗印 `PARSE_FAIL`，呼叫端必須把它跟「沒事」分開看
（REFLEXES #85：「不知道」要有自己的符號）。
"""

import json
import sys


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except Exception as exc:  # noqa: BLE001 — 任何解析問題都是「沒量到」
        print("PARSE_FAIL")
        print(f"error\t{type(exc).__name__}\t{exc}", file=sys.stderr)
        return 1

    vulns = data.get("vulnerabilities") or {}
    rows = []
    highs = crits = blocked = 0

    for name, meta in sorted(vulns.items()):
        severity = meta.get("severity")
        if severity not in ("high", "critical"):
            continue
        if severity == "high":
            highs += 1
        else:
            crits += 1

        fix_available = meta.get("fixAvailable")
        if fix_available is True:
            fix = "minor"
        elif isinstance(fix_available, dict):
            if fix_available.get("isSemVerMajor"):
                fix = f"MAJOR({fix_available.get('name')}@{fix_available.get('version')})"
                blocked += 1
            else:
                fix = "minor"
        else:
            fix = "none"
            blocked += 1

        rows.append(f"{severity}\t{name}\t{fix}")

    print(f"OK {highs} {crits} {blocked}")
    for row in rows:
        print(row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
