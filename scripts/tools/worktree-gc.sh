#!/usr/bin/env bash
# worktree-gc.sh — worktree 安全回收（胼胝體鐵律：用完要刪，但刪前先儀器化檢查有沒有丟工作）
#
# 哲宇 reminder 2026-06-14：「worktree 用完要記得刪掉（可以儀器化檢查是否有丟再刪），
# 不要一直累積一堆滯留檔案」。本工具刪前對每個 worktree 驗三道：
#   (1) locked？（可能是 live background agent）→ 跳過，除非 --force-locked
#   (2) 有未 commit 變更？→ 保留（會丟工作）
#   (3) 有未進 origin/main 的 commit？→ 保留（會丟工作）
# 三道全過才算「乾淨」可刪。判斷不確定時一律偏向「保留」。
#
# 用法:
#   bash scripts/tools/worktree-gc.sh                       # dry-run：列可刪 / 保留 + 原因
#   bash scripts/tools/worktree-gc.sh --apply               # 真的 remove 乾淨且 unlocked 的
#   bash scripts/tools/worktree-gc.sh --apply --force-locked # 連 locked 的乾淨 worktree 也刪（自負風險）
set -uo pipefail
cd "$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR not-a-git-repo"; exit 2; }
MAIN="$(git rev-parse --show-toplevel)"
APPLY=0; FORCE_LOCKED=0
for a in "$@"; do
  [ "$a" = "--apply" ] && APPLY=1
  [ "$a" = "--force-locked" ] && FORCE_LOCKED=1
done

git fetch origin -q 2>/dev/null || true
removable=0; kept=0; pruned=0

cur_wt=""; cur_locked=0
flush() {
  [ -z "$cur_wt" ] && return
  if [ "$cur_wt" = "$MAIN" ]; then cur_wt=""; cur_locked=0; return; fi   # 永不動主 worktree

  if [ ! -d "$cur_wt" ]; then
    echo "  prune  $cur_wt（目錄已不存在）"; pruned=$((pruned+1))
    [ "$APPLY" = 1 ] && git worktree prune 2>/dev/null
    cur_wt=""; cur_locked=0; return
  fi

  local br reason="" safe=1
  br="$(git -C "$cur_wt" rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"

  # (1) locked
  if [ "$cur_locked" = "1" ] && [ "$FORCE_LOCKED" = "0" ]; then reason="LOCKED（可能 live agent）"; safe=0; fi
  # (2) 未 commit 變更
  # 排除 node_modules：semiont-worktree.sh 開 worktree 時把它做成指向主工作樹的
  # 符號連結，而 .gitignore 的 `node_modules/` 只匹配目錄，符號連結在 git 眼中是
  # 檔案，於是每個用官方工具開的 worktree 都固定帶一筆未 commit 變更。這不是使用者
  # 的工作，是我們自己鋪的鷹架——不排掉的話這支回收器對它自家開的 worktree 永遠
  # 判「保留」，一次都不會開火（2026-08-09 發現時已積 10 個，最老的兩個多月，
  # 而 .gitignore 修好也救不了既有的：worktree 讀的是自己檢出那個 commit 的版本）。
  local dirty; dirty="$(git -C "$cur_wt" status --porcelain 2>/dev/null | grep -vE '^\?\? node_modules/?$' | grep -c . || true)"; dirty="${dirty:-0}"
  if [ "$dirty" -gt 0 ]; then reason="${reason:+$reason; }${dirty} 個未 commit 變更"; safe=0; fi
  # (3) 未進 origin/main 的 commit
  local unpushed; unpushed="$(git -C "$cur_wt" log --oneline origin/main..HEAD 2>/dev/null | grep -c . || true)"; unpushed="${unpushed:-0}"
  if [ "$unpushed" -gt 0 ]; then reason="${reason:+$reason; }${unpushed} 個未進 origin/main 的 commit"; safe=0; fi

  if [ "$safe" = "1" ]; then
    echo "  REMOVE $cur_wt [$br]（乾淨：0 dirty / 0 unpushed）"; removable=$((removable+1))
    if [ "$APPLY" = 1 ]; then
      # 先拆掉自己鋪的鷹架：semiont-worktree.sh 留下的 node_modules 符號連結會讓
      # `git worktree remove` 回「contains modified or untracked files」而拒絕，
      # 於是判定為乾淨的 worktree 照樣刪不掉（跟 (2) 的 dirty 判定同一個根因，
      # 只是低一層）。拆的是連結本身，指向的主工作樹 node_modules 不受影響。
      # 刻意不改用 `--force`：那會連真正的未存工作一起吃掉，而擋住刪除正是我們
      # 要保留的保護。
      [ -L "$cur_wt/node_modules" ] && rm -f "$cur_wt/node_modules"
      local fflag=""; [ "$cur_locked" = "1" ] && fflag="--force"
      git worktree remove $fflag "$cur_wt" 2>&1 | sed 's/^/    /'
    fi
  else
    echo "  KEEP   $cur_wt [$br] — $reason"; kept=$((kept+1))
  fi
  cur_wt=""; cur_locked=0
}

while IFS= read -r line; do
  case "$line" in
    "worktree "*) flush; cur_wt="${line#worktree }" ;;
    "locked"*)    cur_locked=1 ;;
    "") ;;
  esac
done < <(git worktree list --porcelain)
flush

echo "---"
echo "可刪（乾淨）: ${removable}  /  保留（有未存工作或 locked）: ${kept}  /  prune（目錄消失）: ${pruned}"
[ "$APPLY" = 0 ] && echo "（dry-run — 加 --apply 真的 remove；locked 的乾淨 worktree 需 --apply --force-locked）"
exit 0
