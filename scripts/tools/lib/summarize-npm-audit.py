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

⚠️ `fixAvailable: true` 不等於「這條在小版本內修得掉」。npm 把
`isSemVerMajor` 的那包資訊放在**真正要動的那個祖先**上，傳遞依賴自己只拿到一個
裸的 `true`。`harvest/ui` 的 `fast-glob` 就是這樣：它自己回 `true`，而它的
`via` 指向 `micromatch`，後者回 `{tailwindcss@4.3.3, isSemVerMajor: true}`——
整條鏈只有升 tailwindcss 4 收得掉。照字面讀裸 `true` 會把它標成 minor、不算進
blocked，於是總結那行叫當班去跑一個什麼都不會動的 `npm audit fix`
（實測：非 --force 的 audit fix 對這五條零改動）。所以裸 `true` 要先沿 `via`
走一遍，找得到 major 祖先就繼承那個判定。

誕生：2026-10-09 twmd-maintainer-daily。這支工具 10-08 才 ship，13 個 pytest
與三個正控制全綠，但 fixture 全是合成的單層公告，沒有一個帶傳遞鏈——**正控制
只蓋到作者當時想得到的形狀**，而它上線後面對的第一個真紅就是這個形狀
（REFLEXES #99 尺先驗再用 / #24 工具在說謊 / #65 偵測器自己要對賬 ground truth）。

解析失敗印 `PARSE_FAIL`，呼叫端必須把它跟「沒事」分開看
（REFLEXES #85：「不知道」要有自己的符號）。
"""

import json
import sys


def _major_fix_via_chain(name, vulns):
    """沿 `via` 找出真正要動的那個 major 祖先；找不到回 None。

    npm 的 `via` 可能是字串（另一個套件名）或 dict（公告本體，常跟自己同名）。
    只追字串那種，並帶 visited 防自我參照（`braces` 的 via 就指著自己）。
    """
    seen = {name}
    frontier = [name]
    while frontier:
        current = frontier.pop()
        for item in (vulns.get(current) or {}).get("via") or []:
            if not isinstance(item, str) or item in seen:
                continue
            seen.add(item)
            candidate = vulns.get(item) or {}
            fix_available = candidate.get("fixAvailable")
            if isinstance(fix_available, dict) and fix_available.get("isSemVerMajor"):
                return fix_available
            frontier.append(item)
    return None


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
            # 裸 true：npm 沒點名要動誰，沿 via 找真正卡住的那個祖先（見檔頭）
            inherited = _major_fix_via_chain(name, vulns)
            if inherited:
                fix = f"MAJOR({inherited.get('name')}@{inherited.get('version')})"
                blocked += 1
            else:
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
