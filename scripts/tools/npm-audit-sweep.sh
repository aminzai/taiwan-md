#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────
# npm-audit-sweep.sh — 一次掃完 CI 裡每一道 npm audit，不要一個個撞
# ─────────────────────────────────────────────────────────────────
#
#   bash scripts/tools/npm-audit-sweep.sh            # 報告，永遠 exit 0
#   bash scripts/tools/npm-audit-sweep.sh --strict   # 任一路徑有 high 以上就 exit 1
#
# 每個路徑印一行結論，後面接它沒收掉的每一條公告：
#
#   <state>  <路徑>  (<high 數> high / <critical 數> critical)
#     <severity>  <套件>  fix=<修法>
#
# fix 欄是這支工具存在的理由，它直接回答當班要問的那一句
# 「這條修補在不在小版本內」：
#
#   minor         有修好的版本，且不是 semver-major → 本班跑 npm audit fix
#                 --package-lock-only 就收得掉
#   MAJOR(<pkg>@<ver>)
#                 只有 breaking change 修得掉 → 這是一個決定，不是一次 heal，
#                 要帶 options + 成本進 OBSERVER-QUEUE
#   none          上游還沒有修好的版本（公告範圍涵蓋所有版本）→ 同上
#
# ── 為什麼要有這支工具（2026-10-08 twmd-maintainer-daily）─────────────
#
# LESSONS `external-advisory-reddens-a-gate-and-not-our-code-becomes-a-reason-
# not-to-act` 同一個結構在 09-30 / 10-02 / 10-08 命中三次（vc=3），它的
# 「候選機械化 (a)」逐字寫著：把 contracts job 的四個 npm audit 收斂成一個
# 會把四個路徑都掃完再一次報完的 step，讓「還有幾個同型閘門在後面」看得見，
# 而不是一個個撞。這支工具就是那條。
#
# 那個病的形狀：`npm audit` 吃的是倉庫外面的資料源，所以它會在倉庫一個字
# 都沒變的情況下由綠轉紅。CI 的 shell 是 `&&` 串起來的，第一道紅了後面三道
# 根本沒跑，於是當班看到的永遠只有第一個路徑——修好它，紅燈就移到下一格，
# 看起來像沒修好。10-02 那班已經踩過一次（修了 root，紅燈移到 harvest/ui）。
#
# 路徑清單**從 workflow 檔解析，不寫死**：CI 多一道 audit 或改 working-directory
# 時這支工具跟著變，不會變成另一把尺（REFLEXES #83 兩把尺 / #82 存在代理有效）。
#
# 仍然缺的那半：沒有東西在偵測「倉庫無變更但 gate 由綠轉紅」。本工具回答
# 「現在紅在哪、修法在不在小版本內」，不回答「這條紅是什麼時候、因為誰出現的」。
# ─────────────────────────────────────────────────────────────────
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
WORKFLOW="$REPO_ROOT/.github/workflows/engineering-checks.yml"
STRICT=0
[[ "${1:-}" == "--strict" ]] && STRICT=1

if [[ ! -f "$WORKFLOW" ]]; then
  echo "⚠️  找不到 $WORKFLOW — 路徑清單無從解析，不假裝掃過" >&2
  exit 2
fi

# 從 workflow 解析每一道 `npm audit` 跑在哪個 working-directory。
# 沒有 working-directory 的那道跑在 repo 根。
# 解析器住在獨立的 .py（不用 heredoc）：heredoc 塞進 process substitution 時，
# Python 裡的引號會被 bash 先拿去配對，整支腳本當場 syntax error。
PARSER="$REPO_ROOT/scripts/tools/lib/parse-audit-paths.py"
if [[ ! -f "$PARSER" ]]; then
  echo "⚠️  找不到 $PARSER — 不假裝掃過" >&2
  exit 2
fi
AUDIT_PATHS_RAW="$(python3 "$PARSER" "$WORKFLOW")" || {
  echo "⚠️  workflow 解析失敗 — 不假裝掃過" >&2
  exit 2
}
# 不用 mapfile：macOS 內建的是 bash 3.2，沒有這個 builtin，而這支工具最常
# 被跑的地方就是維護者的 mac（CI 的 ubuntu 是 bash 5）。
AUDIT_PATHS=()
while IFS= read -r _line; do
  [[ -n "$_line" ]] && AUDIT_PATHS+=("$_line")
done <<EOF
$AUDIT_PATHS_RAW
EOF

if [[ ${#AUDIT_PATHS[@]} -eq 0 ]]; then
  echo "⚠️  workflow 裡解析不到任何 npm audit — 可能 CI 改了寫法，先確認再信這支工具" >&2
  exit 2
fi

echo "════════ CI 的 npm audit 全掃 — $(basename "$REPO_ROOT") ════════"
echo "  從 $(basename "$WORKFLOW") 解析到 ${#AUDIT_PATHS[@]} 道 audit（--audit-level=high）"
echo ""

SUMMARIZER="$REPO_ROOT/scripts/tools/lib/summarize-npm-audit.py"
if [[ ! -f "$SUMMARIZER" ]]; then
  echo "⚠️  找不到 $SUMMARIZER — 不假裝掃過" >&2
  exit 2
fi

TOTAL_HIGH=0
TOTAL_CRIT=0
BLOCKED_BY_MAJOR=0
MEASURED=0
UNMEASURED=0

for p in "${AUDIT_PATHS[@]}"; do
  dir="$REPO_ROOT/$p"
  label="$p"
  [[ "$p" == "." ]] && label="<repo 根>"

  if [[ ! -f "$dir/package.json" ]]; then
    printf '  %-13s %s\n' "UNKNOWN" "$label — 沒有 package.json，這道 audit 在 CI 跑得到而這裡量不到"
    UNMEASURED=$((UNMEASURED + 1))
    continue
  fi

  raw="$(cd "$dir" && npm audit --audit-level=high --json 2>/dev/null)"
  if [[ -z "$raw" ]]; then
    printf '  %-13s %s\n' "UNKNOWN" "$label — npm audit 沒回東西（離線？）"
    UNMEASURED=$((UNMEASURED + 1))
    continue
  fi

  summary="$(printf '%s' "$raw" | python3 "$SUMMARIZER" 2>/dev/null)"
  head_line="$(printf '%s' "$summary" | head -1)"
  set -- $head_line
  status="${1:-PARSE_FAIL}"
  nh="${2:-0}"
  nc="${3:-0}"
  nmajor="${4:-0}"

  if [[ "$status" != "OK" ]]; then
    printf '  %-13s %s\n' "UNKNOWN" "$label — audit JSON 解析失敗"
    UNMEASURED=$((UNMEASURED + 1))
    continue
  fi

  MEASURED=$((MEASURED + 1))
  TOTAL_HIGH=$((TOTAL_HIGH + nh))
  TOTAL_CRIT=$((TOTAL_CRIT + nc))
  BLOCKED_BY_MAJOR=$((BLOCKED_BY_MAJOR + nmajor))

  if [[ $((nh + nc)) -eq 0 ]]; then
    printf '  %-13s %s\n' "GREEN" "$label"
  else
    printf '  %-13s %s  (%s high / %s critical)\n' "RED" "$label" "$nh" "$nc"
    # printf '%s\n'（不是 '%s'）：少了結尾換行，`read` 在最後一行回 non-zero，
    # 迴圈不跑那一輪，於是每個路徑的最後一條公告被靜默丟掉。第一版就是這樣
    # 印了 4 行卻說 5 high——工具少報而沒有任何東西會叫。
    detail="$(printf '%s\n' "$summary" | tail -n +2)"
    shown=0
    while IFS="$(printf '\t')" read -r sev name fix; do
      [[ -z "$sev" ]] && continue
      printf '      %-9s %-22s fix=%s\n' "$sev" "$name" "$fix"
      shown=$((shown + 1))
    done <<EOF
$detail
EOF
    # 自己對賬：印出來的條數要等於表頭宣稱的條數（REFLEXES #65 — 偵測器
    # 自己的 parser 也要對 ground truth 數字交叉驗一次）。
    if [[ "$shown" -ne $((nh + nc)) ]]; then
      printf '      ⚠️  本工具少報：表頭 %s 條，實際印出 %s 條 — 解析有漏，別引用這段讀數\n' \
        "$((nh + nc))" "$shown"
    fi
  fi
done

echo "────────────────────────────────────────────────────────"

# 「量不到」不借用「沒事」那個符號（REFLEXES #85）。有任何一道沒量到，
# 這次掃描就不是一個可以引用的全綠讀數——全綠只在四道都真的量過時才成立。
if [[ $UNMEASURED -gt 0 ]]; then
  echo "  ⚠️  $UNMEASURED/${#AUDIT_PATHS[@]} 道 audit 這台機器量不到（上面標 UNKNOWN）"
  echo "     最常見的原因是那個子專案的 node_modules 沒裝；CI 每次都 npm ci 所以它量得到。"
  echo "     要在本機補量：cd <路徑> && npm ci --ignore-scripts"
fi

if [[ $((TOTAL_HIGH + TOTAL_CRIT)) -eq 0 ]]; then
  if [[ $UNMEASURED -gt 0 ]]; then
    echo "  🟡 量到的 $MEASURED 道全綠，但這不等於 CI 會綠（還有 $UNMEASURED 道沒量到）"
    [[ $STRICT -eq 1 ]] && exit 1
    exit 0
  fi
  echo "  ✅ ${#AUDIT_PATHS[@]} 道 audit 全綠"
  exit 0
fi

echo "  ⚠️  共 $TOTAL_HIGH high / $TOTAL_CRIT critical 分佈在上面的路徑裡"
if [[ $BLOCKED_BY_MAJOR -gt 0 ]]; then
  echo "     其中 $BLOCKED_BY_MAJOR 條只有 breaking change（或還沒有修補）收得掉 —"
  echo "     那是一個帶 options 與成本的決定，不是一次 heal，走 OBSERVER-QUEUE"
fi
if [[ $((TOTAL_HIGH + TOTAL_CRIT - BLOCKED_BY_MAJOR)) -gt 0 ]]; then
  echo "     剩下的在小版本內修得掉：在該路徑跑"
  echo "     npm audit fix --package-lock-only --audit-level=high"
  echo "     （--package-lock-only 不碰 node_modules，babel worker 可能正在用那棵樹）"
fi

[[ $STRICT -eq 1 ]] && exit 1
exit 0
