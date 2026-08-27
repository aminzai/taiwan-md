#!/usr/bin/env bash
# push-heal-to-pr.sh — 把本地 heal 過的檔案以一個 commit 推回投稿者的 PR head 分支
#
# MAINTAINER-PIPELINE §1b P1（v2.8）：格式債的 default 是「直接 push 修補到對方分支 → CI 綠
# → gh pr merge」，不等對方讀懂 gate 說明再自己修。8/18 手動做了七次（fetch / checkout /
# copy / commit / push），今天要做六十次——造橋。
#
# 全程 git plumbing，不 checkout 任何 PR 分支（REFLEXES #67 第三例：checkout 會把整套
# 檢查器換成投稿者 fork 那天的版本；且會動到共用 worktree）。步驟：
#   1. gh 取 PR head sha / fork owner / repo / branch，並確認 maintainerCanModify
#   2. git fetch origin pull/N/head → base commit
#   3. 把本地 heal 後的檔案 hash-object 成 blob，用暫時 index 從 base tree 換掉該 path
#   4. commit-tree（parent = base）→ push 到 fork 的 headRefName
#
# 用法：
#   bash scripts/tools/push-heal-to-pr.sh <PR號> <path/in/repo> [<path2> ...] [--delete <oldpath>] [-m "<commit message>"]
#   --delete <oldpath>：同一個 commit 裡從 PR tree 移除該路徑（用於路徑錯位：投稿檔落在 knowledge/ 根目錄，
#                       heal 後搬到 knowledge/<Cat>/，新路徑當一般 path 傳、舊路徑用 --delete）
#   環境變數 DRY_RUN=1 只印不推
#
# 前提：本地 <path> 已是 heal 後版本（contributor-pr-heal.py --from-pr N 跑過並手修完）。
# 退出碼：0 推成功／2 用法或前提錯／3 maintainerCanModify=false／4 push 失敗

set -euo pipefail

REPO_SLUG="${REPO_SLUG:-frank890417/taiwan-md}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

usage() { sed -n '2,22p' "$0" >&2; exit 2; }

[ $# -ge 2 ] || usage
PR="$1"; shift
MSG=""
PATHS=()
DELETES=()
while [ $# -gt 0 ]; do
  case "$1" in
    -m) MSG="$2"; shift 2 ;;
    --delete) DELETES+=("$2"); shift 2 ;;
    *) PATHS+=("$1"); shift ;;
  esac
done
[ ${#PATHS[@]} -ge 1 ] || usage

for p in "${PATHS[@]}"; do
  [ -f "$p" ] || { echo "❌ 本地檔不存在：$p" >&2; exit 2; }
done

meta="$(gh pr view "$PR" -R "$REPO_SLUG" --json headRefOid,headRefName,headRepository,headRepositoryOwner,maintainerCanModify,isDraft,state)"
state="$(jq -r .state <<<"$meta")"
[ "$state" = "OPEN" ] || { echo "❌ PR #$PR 不是 OPEN（$state）" >&2; exit 2; }
can="$(jq -r .maintainerCanModify <<<"$meta")"
[ "$can" = "true" ] || { echo "❌ PR #$PR maintainerCanModify=false，不能推到對方分支（改走 §1b P2 merge 後 main heal）" >&2; exit 3; }
head_sha="$(jq -r .headRefOid <<<"$meta")"
head_ref="$(jq -r .headRefName <<<"$meta")"
fork_owner="$(jq -r .headRepositoryOwner.login <<<"$meta")"
fork_repo="$(jq -r .headRepository.name <<<"$meta")"

# base 取法（2026-08-18 兩次修）：
# 1. 直接問 fork 分支的 sha（ls-remote，權威源）——origin 的 refs/pull/N/head 是 GitHub 側複製，
#    實測落後幾秒，commit-tree 的 parent 會變舊 head 而被 non-fast-forward 拒絕（Y2 兩次）。
# 2. 不讀 FETCH_HEAD——多個子代共用同一棵 worktree 時，別人的 `git fetch` 會在 fetch 與 rev-parse
#    之間把 FETCH_HEAD 蓋掉，base 變成別的 PR 的 commit（Y1 #1377 一次）。用 ls-remote 拿到的 sha
#    當 base，fetch 只負責把物件抓進來。
fork_url="https://github.com/$fork_owner/$fork_repo.git"
base="$(git ls-remote "$fork_url" "refs/heads/$head_ref" 2>/dev/null | awk '{print $1}')"
if [ -n "$base" ]; then
  git fetch -q "$fork_url" "refs/heads/$head_ref" 2>/dev/null || true
else
  base="$head_sha"
  git fetch -q origin "pull/$PR/head" 2>/dev/null || true
fi
git cat-file -e "$base^{commit}" 2>/dev/null || { echo "❌ 抓不到 base commit $base（fork 分支 fetch 失敗？）" >&2; exit 2; }
if [ "$base" != "$head_sha" ]; then
  echo "⚠️ fork 分支 head ($base) ≠ gh headRefOid ($head_sha)——PR 剛被推過新 commit？以 fork 分支為準" >&2
fi

# 暫時 index：從 base tree 出發，只換掉指定 path
tmp_index="$(mktemp)"
trap 'rm -f "$tmp_index"' EXIT
export GIT_INDEX_FILE="$tmp_index"
git read-tree "$base"
changed=0
for p in "${PATHS[@]}"; do
  blob="$(git hash-object -w "$p")"
  old="$(git ls-tree "$base" -- "$p" | awk '{print $3}')"
  if [ "$blob" = "$old" ]; then
    echo "· $p 跟 PR head 相同，略過"
    continue
  fi
  git update-index --add --cacheinfo "100644,$blob,$p"
  changed=$((changed+1))
done
for d in "${DELETES[@]:-}"; do
  [ -n "$d" ] || continue
  if git ls-tree "$base" -- "$d" | grep -q .; then
    git update-index --force-remove -- "$d"
    echo "· 移除 $d"
    changed=$((changed+1))
  else
    echo "· $d 不在 PR tree，略過"
  fi
done
if [ "$changed" -eq 0 ]; then
  echo "✅ 沒有差異可推（PR #$PR 已是 heal 後版本）"
  exit 0
fi
tree="$(git write-tree)"
unset GIT_INDEX_FILE

if [ -z "$MSG" ]; then
  MSG="🧬 [semiont] heal: 維護者代補格式（PR #$PR）

$(for p in "${PATHS[@]}"; do echo "- $p"; done)

MAINTAINER-PIPELINE §1b P1：格式債直接 push 到投稿者分支，CI 轉綠後 merge。
內容不動，只補 frontmatter／標點／圖片授權／腳註格式。"
fi
commit="$(git commit-tree "$tree" -p "$base" -m "$MSG")"
echo "commit $commit (parent $base, $changed 檔) → $fork_owner/$fork_repo:$head_ref"

if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "DRY_RUN=1，未 push。檢視：git show --stat $commit"
  exit 0
fi

if git push -q "https://github.com/$fork_owner/$fork_repo.git" "$commit:refs/heads/$head_ref"; then
  echo "✅ pushed → https://github.com/$REPO_SLUG/pull/$PR"
else
  echo "❌ push 失敗（token 對 fork 無寫入權？maintainerCanModify 需要 fork 允許維護者編輯）" >&2
  exit 4
fi
