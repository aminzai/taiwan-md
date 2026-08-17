#!/usr/bin/env python3
"""check-budget-i18n.py — /budget 頁多語字串對賬：data/budget/i18n/{lang}.json 的 key 集合必須等於
src/i18n/budget.ts 的 en bundle；值不可空；非 CJK 語言不可含漢字（人名／機關括號原文除外，列出供人判）。
用法：python3 scripts/tools/check-budget-i18n.py [lang ...]（不給就檢查全部存在的檔）"""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
ts = (ROOT / 'src/i18n/budget.ts').read_text(encoding='utf-8')
en = ts.split("  en: {", 1)[1].split("  'zh-TW': {", 1)[0]
keys = re.findall(r"^\s*'(budget\.[^']+)':", en, re.M)
langs = sys.argv[1:] or [p.stem for p in (ROOT / 'data/budget/i18n').glob('*.json') if not p.stem.startswith('_')]
bad = 0
for lang in sorted(langs):
    p = ROOT / f'data/budget/i18n/{lang}.json'
    if not p.exists():
        print(f'❌ {lang}: 檔案不存在'); bad += 1; continue
    d = json.loads(p.read_text(encoding='utf-8'))
    missing = [k for k in keys if k not in d]; extra = [k for k in d if k not in keys]
    empty = [k for k, v in d.items() if not isinstance(v, str) or not v.strip()]
    cjk = [k for k, v in d.items() if lang not in ('ja', 'ko') and re.search(r'[一-鿿]', v)]
    ok = not (missing or extra or empty)
    bad += 0 if ok else 1
    print(f"{'✅' if ok else '❌'} {lang}: {len(d)} keys  missing={len(missing)} extra={len(extra)} empty={len(empty)} 含漢字={len(cjk)}")
    for k in (missing[:3] + extra[:3] + empty[:3]): print('     ', k)
    for k in cjk[:5]: print('      漢字:', k, '→', d[k][:60])
sys.exit(1 if bad else 0)
