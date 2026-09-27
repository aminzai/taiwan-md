#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# ci-main-health.sh — main 上每一條 workflow 最後一次跑成什麼樣
# ─────────────────────────────────────────────────────────────────
#
# `pr-ci-armed.sh` 的 main 側姊妹。那支問「這個 PR 的 CI 有沒有被允許跑」，
# 這支問「main 上有沒有東西正紅著而沒人看到」。
#
#   bash scripts/tools/ci-main-health.sh            # 報告，永遠 exit 0
#   bash scripts/tools/ci-main-health.sh --strict   # 有 RED 就 exit 1
#
# 每行輸出：
#   <state>  <age>  <workflow 名稱>  <檔名>
#
# state：
#   GREEN            main 上最後一次跑成功
#   RED              main 上最後一次失敗／被取消／逾時 → 本班第一個 polish item
#   RUNNING          正在跑或排隊中
#   OFF-BRANCH       從沒在這個分支上跑過，而它的觸發條件本來就跑不到這裡
#                    （只掛 pull_request，或 push 只綁 tag）→ 預期內，不是缺口
#   BLOCKED          最後一次是 action_required／stale：沒跑成，不是跑壞了
#   UNKNOWN(x)       GitHub 回了本工具不認得的 conclusion → 不假裝知道
#   NEVER-ON-MAIN ⚠️ 從沒在 main 上跑過，但它宣告了 push／schedule／
#                    workflow_dispatch 這類 main 跑得到的觸發 → 接線可能斷了
#
# ── 為什麼要有這支工具（2026-09-27 twmd-maintainer-am）────────────────
#
# MAINTAINER-PIPELINE Step 1.5 原本把這件事寫成一段可貼的指令：
#
#   gh api "repos/OWNER/REPO/actions/runs?branch=main&per_page=100" --jq \
#     '[.workflow_runs[]] | group_by(.name)[] | (sort_by(.created_at)|last) | ...'
#
# 那段 group-by 是 2026-09-03 的修補，解掉的是「點名式健檢只看得到造它的人
# 當時想得到的那幾條」（`Python tests` 在 main 上紅了四天沒人看到）。方向對，
# 但它換來另一種盲：**group-by 只能看到那 100 筆裡出現過的 workflow**。
# 本 repo 的 babel 產線整點 commit，deploy 跟著跑——2026-09-27 實測那 100 筆
# 只涵蓋 **8.3 小時**（15:19Z → 23:35Z）。一條掛 paths filter 的 workflow
# 紅完之後不再被觸發，就會滑出這個窗，於是「最後一次跑成什麼樣」這個問題
# 被悄悄換成「最近八小時跑過的那幾條長怎樣」。這正是 `pr-ci-armed.sh` 檔頭
# 記的同一個病（REFLEXES #82 存在代理有效／#15 可貼的 snippet 會腐爛）。
#
# 修法：不掃 repo-wide run 列表，改成**先列出 workflow，再逐條問它自己的
# runs endpoint**（`/actions/workflows/<id>/runs?branch=main&per_page=1`）。
# 每條各問一次，窗口大小與 main 的 commit 量脫鉤，工作流再冷門也看得到。
#
# 刻意不設「幾天沒跑就算 stale」的門檻：掛 paths filter 的 workflow 冷幾天
# 是正常的，憑感覺設一個數字只會生出假陽性（REFLEXES #66 門檻要用真實產出
# 校準）。這裡只印齡，讓讀的人自己判斷，硬旗只給 RED 與 NEVER-ON-MAIN。
#
# Requires: gh (已登入), jq, python3
# Exit: 0（預設）；--strict 且有 RED 時 1
# ─────────────────────────────────────────────────────────────────

set -uo pipefail

REPO="${TWMD_REPO:-frank890417/taiwan-md}"
BRANCH="${TWMD_CI_BRANCH:-main}"
STRICT=0
[ "${1:-}" = "--strict" ] && STRICT=1

if ! command -v gh >/dev/null 2>&1; then
  echo "❌ 需要 gh CLI" >&2
  exit 0
fi

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

# workflow 是否宣告了「會在 main 這個分支上跑」的觸發。
# YAML 的 `on:` 會被解析成布林 True 當 key，所以兩種 key 都要看。
#
# ⚠️ `push` 不等於「會在 main 上跑」：`push: {tags: [cli-v*]}` 是 tag 推送，
# 分支永遠對不上。第一版把它算成 main-eligible，於是把 npm-publish-cli 誤報成
# NEVER-ON-MAIN（2026-09-27 首跑抽驗時抓到，REFLEXES #99 尺先驗再用）。
main_eligible() {
  local path="$1"
  local full="$REPO_ROOT/$path"
  [ -f "$full" ] || { echo "unknown"; return; }
  python3 - "$full" <<'PY'
import sys
try:
    import yaml
except ImportError:
    print("unknown"); sys.exit(0)
try:
    doc = yaml.safe_load(open(sys.argv[1], encoding="utf-8")) or {}
except Exception:
    print("unknown"); sys.exit(0)
trig = doc.get("on", doc.get(True))
if trig is None:
    print("unknown"); sys.exit(0)
if isinstance(trig, str):
    trig = {trig: None}
elif isinstance(trig, list):
    trig = {k: None for k in trig}
elif not isinstance(trig, dict):
    print("unknown"); sys.exit(0)

if {"schedule", "workflow_dispatch", "repository_dispatch"} & set(trig):
    print("yes"); sys.exit(0)

if "push" in trig:
    spec = trig["push"]
    # `push:` 無細則 → 所有分支都跑；有 branches → 看得到分支；
    # 只有 tags（可再帶 paths）→ tag 推送，不會在分支上跑。
    if not isinstance(spec, dict):
        print("yes"); sys.exit(0)
    if "branches" in spec or "branches-ignore" in spec:
        print("yes"); sys.exit(0)
    if "tags" in spec or "tags-ignore" in spec:
        print("no"); sys.exit(0)
    print("yes"); sys.exit(0)

print("no")
PY
}

printf '%s\n' "════════ $BRANCH CI 健康 — $REPO ════════"

red=0
never=0
blocked=0
unknown=0
total=0

while IFS=$'\t' read -r wid wname wpath; do
  [ -n "$wid" ] || continue
  total=$((total + 1))

  # ⚠️ `?branch=` 比對的是 head_branch，而 fork PR 的 head branch 常常就叫 main
  # ——所以不濾掉 pull_request 事件的話，別人從自己 main 送來的 PR 會被讀成
  # 「我們 main 上的一次執行」。第一版就是這樣把一則 2026-04-01 的投稿 PR 失敗
  # 報成「Translation PR Check 在 main 紅了 178 天」（2026-09-27 首跑抽驗時抓到，
  # REFLEXES #99 尺先驗再用／#24 工具在說謊）。掃描深度 50 筆，夠深到冷門
  # workflow 也撈得到，又不會退回 repo-wide 那種跟 commit 量綁在一起的窗。
  run=$(gh api "repos/$REPO/actions/workflows/$wid/runs?branch=$BRANCH&per_page=50" \
    --jq '[.workflow_runs[]
           | select(.event != "pull_request" and .event != "pull_request_target")]
          | sort_by(.created_at) | last
          | "\(.conclusion // .status)\t\(.created_at)\t\(.html_url)"' 2>/dev/null)

  if [ -z "$run" ] || [ "${run%%$'\t'*}" = "null" ]; then
    if [ "$(main_eligible "$wpath")" = "yes" ]; then
      state="NEVER-ON-MAIN ⚠️"
      never=$((never + 1))
    else
      state="OFF-BRANCH     "
    fi
    printf '  %s %-9s %-26s %s\n' "$state" "-" "$wname" "$wpath"
    continue
  fi

  concl="${run%%$'\t'*}"
  rest="${run#*$'\t'}"
  created="${rest%%$'\t'*}"
  url="${rest#*$'\t'}"

  age=$(python3 -c "
import datetime,sys
t=datetime.datetime.strptime(sys.argv[1],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=datetime.timezone.utc)
h=(datetime.datetime.now(datetime.timezone.utc)-t).total_seconds()/3600
print(f'{h:.0f}h' if h < 48 else f'{h/24:.1f}d')
" "$created" 2>/dev/null || echo '?')

  # 逐個 conclusion 明寫，不靠 `*)` catch-all 決定紅燈：GitHub 的 conclusion
  # 不只成功與失敗，`stale`／`action_required` 是「沒跑成」不是「跑壞了」，
  # 混進同一盞燈就是又一個混維度的 status（REFLEXES #38）。認不得的值也不
  # 假裝知道，給它自己的符號（REFLEXES #85）。
  case "$concl" in
    success) state="GREEN          " ;;
    in_progress | queued | waiting | requested | pending) state="RUNNING        " ;;
    skipped | neutral) state="SKIPPED        " ;;
    failure | cancelled | timed_out | startup_failure)
      state="RED            "
      red=$((red + 1))
      ;;
    action_required | stale)
      state="BLOCKED        "
      blocked=$((blocked + 1))
      ;;
    *)
      state="UNKNOWN($concl)"
      unknown=$((unknown + 1))
      ;;
  esac

  printf '  %s %-9s %-26s %s\n' "$state" "$age" "$wname" "$wpath"
  [ "$state" = "RED            " ] && printf '      ↳ %s (%s)\n' "$url" "$concl"
done < <(gh api "repos/$REPO/actions/workflows?per_page=100" \
  --jq '.workflows[] | select(.state=="active") | select(.path | startswith(".github/")) | "\(.id)\t\(.name)\t\(.path)"' 2>/dev/null)

echo "────────────────────────────────────────────────────────"
printf '  %s 條 active workflow：RED %s / BLOCKED %s / UNKNOWN %s / NEVER-ON-MAIN %s\n' \
  "$total" "$red" "$blocked" "$unknown" "$never"
if [ "$red" -gt 0 ]; then
  echo "  ⚠️ main 上有東西紅著。紅在 main 不會自己叫，它會等下一個路過的投稿 PR 替它背黑鍋"
  echo "     （2026-09-03 #1662 就是這樣中的）→ 本班 Stage 3.5 第一個 polish item。"
fi
if [ "$never" -gt 0 ]; then
  echo "  ⚠️ 有 workflow 宣告了 main 跑得到的觸發卻從沒在 main 上跑過 — 先查 paths filter 與分支條件。"
fi

if [ "$STRICT" = "1" ] && [ "$red" -gt 0 ]; then
  exit 1
fi
exit 0
