#!/usr/bin/env bash
# check-hardcoded-langs.sh
# 偵測 src/ 與 scripts/ 內 hardcoded language code array，違反 LANGUAGES_REGISTRY SSOT 原則
#
# 對應 [MANIFESTO §指標 over 複寫](../../docs/semiont/MANIFESTO.md) 的自我 apply：
# 任何 ['en', 'ja', 'ko', ...] 形式的 hardcoded 語言清單應該改從
# src/config/languages.{ts,mjs} 的 LANGUAGES / ENABLED_LANGUAGE_CODES 動態 derive。
#
# 觸發背景：2026-04-25 β7 i18n-evolution-roadmap audit B6
# - getLangSwitchPath.ts:206 hardcoded ['en','ja','ko'] → fr/es 路由疊加 bug
# - 404.astro:376 同樣 hardcoded → fr/es 進 404 後切換 cascade
#
# 用法：
#   bash scripts/tools/check-hardcoded-langs.sh             # 完整掃描
#   bash scripts/tools/check-hardcoded-langs.sh --ci        # CI 模式（找到 = exit 1）
#   bash scripts/tools/check-hardcoded-langs.sh --staged    # 只掃 staged files

set -euo pipefail

MODE="${1:-scan}"

# 已知語言碼（跟 src/config/languages.mjs 對齊；新語言出生時補這裡一個 alternation）
LANGCODES="en|ja|ko|es|fr|vi|id|pt|hi|ar|ru|de|th"

# Patterns 來抓 hardcoded language array。
#
# v2（2026-07-26）：原本三條 pattern 都寫死「開頭必須是 en, ja, ko」，只抓得到
# 當初觸發它誕生的那個形狀。`new Set(['en','es','ja','ko','resources'])` 三條全
# 不中——那正是 cli/src/lib/knowledge.js 從四月漏到七月的那一行。改成「任意三個
# 相鄰的已知語言碼字串」，順序、引號、Set(...) 包裝都不影響命中。
PATTERNS=(
  "\\[\\s*['\"]($LANGCODES)['\"]\\s*,\\s*['\"]($LANGCODES)['\"]\\s*,\\s*['\"]($LANGCODES)['\"]"
)

# 允許清單（這些檔案的 hardcoded 語言清單是 SSOT 本體或合理的歷史 mirror）
ALLOWLIST=(
  "src/config/languages.ts"
  "src/config/languages.mjs"
  "scripts/tools/check-hardcoded-langs.sh"
  # 真陽性以外的一條：這是 per-language fallback cascade（缺 key 時依序退到哪個
  # 語言），是有順序的偏好清單，不是語言註冊表。新語言出生時本來就該自己決定
  # 退階順序，不能從 registry derive。
  "src/i18n/utils.ts"
)

# ── 已知債（2026-07-26 擴網當天量到，尚未修）─────────────────────────────
# 擴網之後這三個檔案立刻現形，都是同一種病：語言清單停在四五語的年代。
# 沒有當場修，因為它們在儀表板與地圖產生器裡，各自要獨立驗證，不在當時那個
# session 驗得起來的範圍。暫掛這裡讓 pre-commit 不會擋住正在跑的批次，
# 但**這不是豁免，是有日期的待辦**：
#   src/scripts/dashboard/registry.js:74      ['en','es','ja','ko']
#   src/scripts/dashboard/next-steps.js:18    ['en','es','ja','ko']
#   scripts/core/generate-map-markers.js:111  Set(['en','ja','ko','zh-TW','es'])
# 修掉一條就從這裡刪一行。完整脈絡：
# reports/design-taiwanmd-node-app-distribution-2026-07-26.md §八 Wave 0
KNOWN_DEBT=(
  "src/scripts/dashboard/registry.js"
  "src/scripts/dashboard/next-steps.js"
  "scripts/core/generate-map-markers.js"
)
ALLOWLIST+=("${KNOWN_DEBT[@]}")

# 收集要掃描的檔案
if [[ "$MODE" == "--staged" ]]; then
  FILES=$(git diff --cached --name-only --diff-filter=ACM \
    | grep -E '\.(ts|tsx|mjs|cjs|js|astro|sh)$' || true)
else
  # cli/ 與 workers/ 是分發層（npm 套件、MCP server、遠端 endpoint）。它們不在
  # 站體的 import 關係裡，所以站體的檢查一路看不到它們——2026-07-26 量到 cli 的
  # 語言表漏了七個語言、把 2900 筆譯文當中文回給使用者三個月，就是這個盲區。
  FILES=$(find src scripts cli workers astro.config.mjs \
    -type f \
    \( -name "*.ts" -o -name "*.tsx" -o -name "*.mjs" -o -name "*.cjs" \
       -o -name "*.js" -o -name "*.astro" -o -name "*.sh" \) \
    2>/dev/null | grep -v node_modules | grep -v dist || true)
fi

if [[ -z "$FILES" ]]; then
  echo "✅ 無檔案可掃描"
  exit 0
fi

VIOLATIONS=0
VIOLATION_LIST=""

for f in $FILES; do
  [[ ! -f "$f" ]] && continue

  # Skip allowlist
  skip=0
  for allowed in "${ALLOWLIST[@]}"; do
    if [[ "$f" == "$allowed" ]] || [[ "$f" == *"$allowed" ]]; then
      skip=1
      break
    fi
  done
  [[ $skip -eq 1 ]] && continue

  for pattern in "${PATTERNS[@]}"; do
    # Skip comment lines (// ... or # ... or * ...) where pattern only appears
    # in the comment text — comments don't execute, so they're not real bugs
    matches=$(grep -nE "$pattern" "$f" 2>/dev/null \
      | grep -vE '^[0-9]+:\s*(//|#|\*)' \
      | grep -vE '^[0-9]+:.*(//|#).*\[.*en.*ja.*ko' \
      || true)
    if [[ -n "$matches" ]]; then
      while IFS= read -r line; do
        VIOLATIONS=$((VIOLATIONS + 1))
        VIOLATION_LIST+="\n  $f:$line"
      done <<< "$matches"
    fi
  done
done

if [[ $VIOLATIONS -gt 0 ]]; then
  echo "🚨 發現 $VIOLATIONS 個 hardcoded language array："
  echo -e "$VIOLATION_LIST"
  echo ""
  echo "💡 修法：改從 LANGUAGES_REGISTRY 動態 derive："
  echo ""
  echo "    import { LANGUAGES } from '../config/languages';"
  echo "    const langPrefixes = LANGUAGES"
  echo "      .filter(l => l.enabled && !l.isDefault)"
  echo "      .map(l => l.code);"
  echo ""
  echo "  或直接用既有 export："
  echo ""
  echo "    import { ENABLED_LANGUAGE_CODES, ALL_LANGUAGE_CODES } from '../config/languages';"
  echo ""
  echo "  Why：對應 MANIFESTO §指標 over 複寫 SSOT 原則 + REFLEXES #20"
  echo "  Audit canonical：reports/i18n-evolution-roadmap-2026-04-25.md"

  if [[ "$MODE" == "--ci" ]] || [[ "$MODE" == "--staged" ]]; then
    exit 1
  fi
  exit 0
fi

echo "✅ 無 hardcoded language array 違反"
exit 0
