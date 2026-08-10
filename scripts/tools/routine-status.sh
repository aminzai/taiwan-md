#!/usr/bin/env bash
# routine-status.sh — 過去 24hr cron routine 跑況 (cross-session continuity signal)
#
# Phase A2 (per reports/become-boot-mode-design-2026-05-13.md §5.3)
# 取代 BECOME §Step 3 ROUTINE.md 全檔 (649 行) 載入需求
#
# 用途：BECOME §Step 6 L4 always-load query 接這個 script
# 輸出：~3-5 行 markdown summary (過去 24h 跑了哪些 routine + 時間)
#
# 設計原則 (per D7 boundary rule):
# ✅ Cron 替我做了什麼 (cross-session continuity)
# ❌ 不含 work artifact inspection (PR/issue list → MAINTAINER Stage 1)
#
# v2 (2026-08-10 mouhouse-audit)：飛輪遷居 mouhouse 後，本機 checkout 的 memory/
# 不 pull 就看不到營運機的 routine 痕跡——v1 在這種情況下把「本機 stale」讀成
# 「飛輪停擺」（指揮部產線期間每次甦醒都誤報）。v2 補 origin/main ls-tree 視角
# （用已 fetch 的 ref，不強制連網），本機與 origin 兩個集合取聯集。
# 同時修掉 v1 的殼層 bug：當天尚無 memory 檔時 ls 空 glob 非零退出，
# 撞 set -euo pipefail 讓整支腳本 rc=1 且一行都不印（fail-loud 變 fail-silent）。

set -euo pipefail

MEMORY_DIR="${MEMORY_DIR:-docs/semiont/memory}"

if [[ ! -d "$MEMORY_DIR" ]]; then
  echo "⚠️ routine-status: $MEMORY_DIR 不存在"
  exit 0
fi

TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d 'yesterday' +%Y-%m-%d)

# 過去 24hr 內的 routine memory files (filename schema: YYYY-MM-DD-HHMMSS-{handle}.md)
# 本機 checkout 視角：空 glob 用 [[ -e ]] guard，不讓 ls 的非零退出炸掉 set -e
list_local() {
  local f
  for f in "$MEMORY_DIR/$TODAY"-*.md "$MEMORY_DIR/$YESTERDAY"-*.md; do
    [[ -e "$f" ]] && basename "$f"
  done
  return 0
}

# origin/main 視角：飛輪跑在別台機器（mouhouse）時，本機不 pull 也看得到。
# 讀已 fetch 的 ref，不在甦醒路徑上強制連網；ref 齡由呼叫端輸出行判讀。
list_origin() {
  git ls-tree --name-only origin/main "$MEMORY_DIR/" 2>/dev/null \
    | awk -F'/' '{print $NF}' \
    | grep -E "^(${TODAY}|${YESTERDAY})-" || true
}

ROUTINE_FIRES=$(
  { list_local; list_origin; } \
    | sort -u \
    | awk -F'-' '
      {
        date = $1"-"$2"-"$3
        time = substr($4, 1, 2)":"substr($4, 3, 2)
        handle = ""
        for (i=5; i<=NF; i++) handle = handle (i>5?"-":"") $i
        sub(/\.md$/, "", handle)
        # 只取 routine-fire 類 (排除 manual / interactive session)
        if (handle ~ /^(twmd-|spore-|prebuild-)/) {
          print date" "time"  "handle
        }
      }
    '
)

ORIGIN_AGE=$(git log -1 --format='%cr' origin/main 2>/dev/null || echo "unknown")

if [[ -z "$ROUTINE_FIRES" ]]; then
  echo "📋 routine | 過去 24hr 無 cron fire（本機 + origin/main 雙視角皆空；origin/main 最新 commit ${ORIGIN_AGE}）"
  echo "   ↳ 檢查營運機 mouhouse 的排程器是否運作（ROUTINE.md §宿主機）"
  exit 0
fi

echo "📋 routine | 過去 24hr cron fires（本機 ∪ origin/main，origin 最新 commit ${ORIGIN_AGE}）:"
echo "$ROUTINE_FIRES" | tail -10 | sed 's/^/  /'
