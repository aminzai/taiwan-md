#!/usr/bin/env python3
"""從 GitHub Actions workflow 檔解析每一道 `npm audit` 跑在哪個目錄。

給 scripts/tools/npm-audit-sweep.sh 用。路徑從 workflow 解析而不寫死，
CI 多一道 audit 或改 working-directory 時掃描工具跟著變，不會長成第二把尺
（REFLEXES #83）。

輸出：一行一個路徑（去重，保留 workflow 裡的順序），沒有 working-directory
的那道印 "."。
"""

import re
import sys

STEP_START = re.compile(r"^\s*-\s+")
AUDIT_RUN = re.compile(r"^\s*-\s+run:.*\bnpm audit\b")
WORKDIR = re.compile(r"^\s*working-directory:\s*(\S+)\s*$")


def parse(text):
    lines = text.split("\n")
    paths = []
    for i, line in enumerate(lines):
        if not AUDIT_RUN.search(line):
            continue
        indent = len(line) - len(line.lstrip())
        workdir = "."
        # working-directory 是同一個 step 的 sibling key：縮排比這個 step 的
        # dash 深，且出現在下一個 "- " 之前。
        for nxt in lines[i + 1 :]:
            if not nxt.strip():
                continue
            cur = len(nxt) - len(nxt.lstrip())
            if cur <= indent and STEP_START.match(nxt):
                break
            if cur <= indent:
                break
            found = WORKDIR.match(nxt)
            if found:
                workdir = found.group(1).strip("\"'")
                break
        paths.append(workdir)

    seen = set()
    ordered = []
    for p in paths:
        if p not in seen:
            seen.add(p)
            ordered.append(p)
    return ordered


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <workflow.yml>", file=sys.stderr)
        return 2
    with open(sys.argv[1], encoding="utf-8") as handle:
        found = parse(handle.read())
    if not found:
        print("解析不到任何 npm audit step", file=sys.stderr)
        return 1
    for p in found:
        print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
