#!/usr/bin/env python3
"""remap-inline-image-paths.py — 譯文正文內嵌 /article-images/ 路徑跟 zh 不一致但張數相同時，按順序對回 zh 的路徑。

誕生 2026-09-22 twmd-babel-nightly：zh 把 hualien-01/02 之類的佔位檔名改成有意義的檔名後，譯文 body 還停在舊名
（花蓮縣 id／pt、台東縣 pt／ru），舊名讓同一張圖在同篇出現兩次，pre-commit image-health hard 擋下任何後續
frontmatter heal。張數不同的不碰（body 真的 stale，留給重翻）。

    python3 scripts/tools/lang-sync/remap-inline-image-paths.py            # 全語 dry-run
    python3 scripts/tools/lang-sync/remap-inline-image-paths.py ja pt --apply
落地路徑清單寫到 /tmp/remap-inline-images.paths（精確路徑 stage 用）。
"""
import re, json, sys
from pathlib import Path
IMG = re.compile(r'(!\[[^\]]*\]\()(/article-images/[^)\s]+)(\))')
tr = json.load(open('knowledge/_translations.json', encoding='utf-8'))
apply = '--apply' in sys.argv
only = [a for a in sys.argv[1:] if not a.startswith('--')]
n_diff = n_fix = n_count_mismatch = 0; fixed = []
for tpath, zpath in tr.items():
    if only and tpath.split('/')[0] not in only: continue
    tp, zp = Path('knowledge', tpath), Path('knowledge', zpath)
    if not tp.exists() or not zp.exists(): continue
    zt, tt = zp.read_text(encoding='utf-8'), tp.read_text(encoding='utf-8')
    zi, ti = [m[1] for m in IMG.findall(zt)], [m[1] for m in IMG.findall(tt)]
    if zi == ti or not zi: continue
    n_diff += 1
    if len(zi) != len(ti): n_count_mismatch += 1; continue
    it = iter(zi)
    new = IMG.sub(lambda m: m.group(1) + next(it) + m.group(3), tt)
    n_fix += 1; fixed.append(tpath)
    if apply: tp.write_text(new, encoding='utf-8')
print(f'differ={n_diff} count-mismatch(skip)={n_count_mismatch} {"fixed" if apply else "would-fix"}={n_fix}')
Path('/tmp/remap-inline-images.paths').write_text('\n'.join('knowledge/' + p for p in fixed) + ('\n' if fixed else ''), encoding='utf-8')
