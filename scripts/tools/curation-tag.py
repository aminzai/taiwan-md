#!/usr/bin/env python3
"""curation-tag.py — 查證狀態欄位批次/單檔設定工具。

設計 canonical：reports/design-curation-tier-2026-08-04.md
用法：
  python3 scripts/tools/curation-tag.py --set incubating --files list.txt          # dry-run
  python3 scripts/tools/curation-tag.py --set incubating --files list.txt --apply
  python3 scripts/tools/curation-tag.py --set verified knowledge/People/某人.md --apply

行為：
  - frontmatter 無 curation 欄位 → 在 closing --- 前插入
  - 已有 curation → 更新值
  - --set incubating 時，featured: true 一併改 false（incubating 不進精選，互斥由
    article-health curation-consistency check 看守）
  - 文字級編輯，不重排 YAML；檔案不存在或無 frontmatter 一律 fail-loud 列出
"""

import argparse
import re
import sys
from pathlib import Path

VALID = {'verified', 'incubating'}


def process(path: Path, value: str, apply: bool) -> str:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return 'NO_FRONTMATTER'
    end = text.find('\n---', 3)
    if end == -1:
        return 'BROKEN_FRONTMATTER'
    fm = text[: end + 1]  # 含 opening --- 到 closing 前一行
    body = text[end + 1 :]  # 從 closing --- 行開始

    actions = []
    if re.search(r'^curation:', fm, flags=re.M):
        new_fm, n = re.subn(r"^curation:.*$", f"curation: {value}", fm, flags=re.M)
        if new_fm != fm:
            actions.append(f'update curation → {value}')
        fm = new_fm
    else:
        fm = fm.rstrip('\n') + f'\ncuration: {value}\n'
        actions.append(f'insert curation: {value}')

    if value == 'incubating' and re.search(r"^featured:\s*true\s*$", fm, flags=re.M):
        fm = re.sub(r"^featured:\s*true\s*$", 'featured: false', fm, flags=re.M)
        actions.append('featured true → false')

    if not actions:
        return 'NOOP'
    if apply:
        path.write_text(fm + body, encoding='utf-8')
    return ' / '.join(actions)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set', dest='value', required=True, choices=sorted(VALID))
    ap.add_argument('--files', help='名單檔（每行一個 repo-relative 路徑）')
    ap.add_argument('paths', nargs='*', help='直接給檔案路徑')
    ap.add_argument('--apply', action='store_true', help='實際寫入（缺省 dry-run）')
    ap.add_argument('--limit', type=int, help='只處理前 N 檔（dry-run 抽檢用）')
    args = ap.parse_args()

    targets = list(args.paths)
    if args.files:
        targets += [
            ln.strip()
            for ln in Path(args.files).read_text(encoding='utf-8').splitlines()
            if ln.strip() and not ln.strip().startswith('#')
        ]
    if args.limit:
        targets = targets[: args.limit]
    if not targets:
        sys.exit('no targets')

    mode = 'APPLY' if args.apply else 'DRY-RUN'
    ok = missing = 0
    for t in targets:
        p = Path(t)
        if not p.is_file():
            print(f'❌ MISSING  {t}')
            missing += 1
            continue
        result = process(p, args.value, args.apply)
        if result in ('NO_FRONTMATTER', 'BROKEN_FRONTMATTER'):
            print(f'❌ {result}  {t}')
            missing += 1
            continue
        ok += 1
        print(f'✅ {result}  {t}')
    print(f'\n[{mode}] ok={ok} problems={missing} total={len(targets)}')
    sys.exit(1 if missing else 0)


if __name__ == '__main__':
    main()
