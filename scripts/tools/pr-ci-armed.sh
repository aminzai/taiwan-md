#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# pr-ci-armed.sh — 每個 open PR 的 CI 到底有沒有真的跑過
# ─────────────────────────────────────────────────────────────────
#
# 回答一個 `gh pr checks` 答不出來的問題：**這個 PR 的 workflow 有沒有被
# 允許執行**。GitHub 對第一次投稿的 fork 貢獻者預設不自動跑 CI，run 會停在
# `action_required` 等維護者按核准——而停在那裡的 run **不會在 commit 上留下
# check-run**。所以 `gh pr checks` 回的是「no checks reported」，讀起來像
# 中性資訊，不像「這個 PR 從頭到尾零檢查」。
#
#   bash scripts/tools/pr-ci-armed.sh              # 掃所有 open PR
#   bash scripts/tools/pr-ci-armed.sh 1365 1430    # 只看指定 PR
#
# 每行輸出：
#   #N  <state>  checks=<在 head sha 上的 check-run 數>  pending=<待核准 run 數>  <author> <title>
#
# state：
#   ARMED       head sha 上有 check-run，CI 真的跑過 → 綠紅可信
#   UNARMED     head sha 上零 check-run，且有 run 卡在 action_required
#               → **一條都沒跑**，不要把「沒有紅燈」讀成「綠燈」
#   NO-WORKFLOW head sha 上零 check-run 且零待核准 → 這個 PR 的改動路徑
#               不匹配任何 workflow 的 paths filter（也是一種零檢查，
#               但成因不同：不是被擋，是根本沒被觸發）
#
# 為什麼要有這支工具（2026-08-19 maintainer-am）：
# MAINTAINER-PIPELINE Step 1.5b 原本把這件事寫成一段內嵌 snippet，用
# `gh api repos/OWNER/REPO/actions/runs` **不帶 branch 參數**再用 jq 過濾
# head_branch。那個 endpoint 預設只回最新 30 筆 run——在這個 repo（babel
# 整點 commit、deploy 頻繁）只涵蓋約 6 小時。PR #1365 有 84 筆 run 卡在
# action_required 三天，snippet 照著跑回報 `待批准=0`，判準表的
# 「checks=0 且 待批准>0」因此永遠不會成立。偵測器自己是盲的。
# 修法是 server-side `?branch=` 過濾 + per_page=100，並把取數邏輯放進
# 儀器而不是留在文件裡的可貼指令（REFLEXES #15 / #82）。
#
# Requires: gh (已登入), jq
# Exit: 0 always（這是報告工具，不是 gate）

set -uo pipefail

REPO="${TWMD_REPO:-frank890417/taiwan-md}"

if ! command -v gh >/dev/null 2>&1; then
  echo "❌ 需要 gh CLI" >&2
  exit 0
fi

if [ $# -gt 0 ]; then
  PRS="$*"
else
  PRS=$(gh pr list -R "$REPO" --state open --limit 100 --json number -q '.[].number')
fi

printf '%s\n' "════════ PR CI armed 狀態 — $REPO ════════"

unarmed=0
noworkflow=0
total=0

for n in $PRS; do
  meta=$(gh pr view "$n" -R "$REPO" --json headRefOid,headRefName,author,isDraft,title 2>/dev/null) || continue
  sha=$(printf '%s' "$meta" | jq -r .headRefOid)
  branch=$(printf '%s' "$meta" | jq -r .headRefName)
  author=$(printf '%s' "$meta" | jq -r .author.login)
  draft=$(printf '%s' "$meta" | jq -r 'if .isDraft then "draft" else "ready" end')
  title=$(printf '%s' "$meta" | jq -r .title | cut -c1-52)

  checks=$(gh api "repos/$REPO/commits/$sha/check-runs" --jq .total_count 2>/dev/null || echo 0)

  # server-side branch filter：不帶它就只看得到最新 30 筆 repo-wide run
  pending=$(gh api "repos/$REPO/actions/runs?branch=$branch&per_page=100" \
    --jq "[.workflow_runs[] | select(.head_sha==\"$sha\" and .conclusion==\"action_required\")] | length" \
    2>/dev/null || echo 0)

  total=$((total + 1))
  if [ "${checks:-0}" -gt 0 ]; then
    state="ARMED      "
  elif [ "${pending:-0}" -gt 0 ]; then
    state="UNARMED ⚠️ "
    unarmed=$((unarmed + 1))
  else
    state="NO-WORKFLOW"
    noworkflow=$((noworkflow + 1))
  fi

  printf '  #%-5s %s checks=%-3s pending=%-3s [%s/%s] %s\n' \
    "$n" "$state" "${checks:-0}" "${pending:-0}" "$draft" "$author" "$title"
done

echo "────────────────────────────────────────────────────────"
printf '  掃了 %s 個 open PR：UNARMED %s / NO-WORKFLOW %s\n' "$total" "$unarmed" "$noworkflow"
if [ "$unarmed" -gt 0 ]; then
  cat <<'EOF'
  ⚠️ UNARMED 的 PR 一條 CI 都沒跑過。確認改動無害後核准：
     gh api "repos/OWNER/REPO/actions/runs?branch=<branch>&per_page=100" \
       --jq '.workflow_runs[] | select(.head_sha=="<sha>" and .conclusion=="action_required") | .id' \
       | while read id; do gh api -X POST "repos/OWNER/REPO/actions/runs/$id/approve"; done
     只核准 head sha 上那批，不要把整條分支的歷史 run 全放出去。
EOF
fi
