#!/usr/bin/env bash
# git-prune-when-quiet.sh — 機會性回收：只在沒有 writer 的那一瞬間跑 prune
#
# 為什麼存在：`.git/gc.log` 的「too many unreachable loose objects; run 'git prune'」
# 從 2026-09-19 起在 51 份 memory 的交接裡傳了 21 天，每一班都讀到、沒有一班動手。
# 卡住它的不是判斷，是**沒有任何席位擁有一個沒有寫入者的空檔**（LESSONS
# `maintainer-seat-cannot-obtain-a-quiet-window-so-window-dependent-gates-never-run`
# 與 `suppressed-warning-recurs-because-its-fix-needs-a-window-no-routine-has`
# 講的是同一件事）。營運機上 babel-push-every --watch 與 dispatcher 幾乎全天在寫，
# 而 DNA #35 禁止在平行工作期間跑破壞性 git op——兩條都對，交集是空的。
#
# 修法不是去找那個空檔，是**讓它自己認出空檔**：這支可以被任何班次或 cron 無腦呼叫，
# 窗口不乾淨就原樣退場，乾淨就把 21 天的垃圾收掉。偵測沿用既有的
# `lib/check-parallel-actor.sh`（REFLEXES #57 那支），不自己再寫一份 pgrep 樣式——
# 兩份會漂（REFLEXES #92 twin-artifact）。
#
# 只有 ACTOR_BUSY 擋它：index.lock 或 babel/lang-sync writer 正在產生物件。
# REMOTE_AHEAD 與 DIRTY_BATCH 不擋——prune 不推不拉，未 commit 的檔案也不是物件。
#
# 用法:
#   bash scripts/tools/git-prune-when-quiet.sh            # 看窗口、不動手
#   bash scripts/tools/git-prune-when-quiet.sh --apply    # 窗口乾淨才動手
#
# exit: 0=已回收 / 10=窗口不乾淨，原樣退場（不是錯誤）/ 11=--apply 沒帶，只報告 / 2=error
set -uo pipefail

REPO="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "ERROR not-a-git-repo"; exit 2; }
cd "$REPO" || exit 2

APPLY=0
[ "${1:-}" = "--apply" ] && APPLY=1

GUARD="$REPO/scripts/tools/lib/check-parallel-actor.sh"
[ -f "$GUARD" ] || { echo "ERROR 找不到 $GUARD（偵測沿用它，不自己重寫）"; exit 2; }

counts() { git count-objects -v | awk '/^count:/{c=$2} /^size:/{s=$2} END{printf "%s 個 loose / %.0f MiB", c, s/1024}'; }

BEFORE="$(counts)"
# `--status` 在非 CLEAN 時 exit 1，所以不能用 `|| echo UNKNOWN` 當 fallback——
# 那會讓 STATUS 同時含狀態字與 UNKNOWN 兩行，等號比對整個失效、窗口判斷 fail-open。
# 這支第一次跑正控制就是這樣被抓到的：writer 全開而它說「窗口可用」。
STATUS="$(bash "$GUARD" --status 2>/dev/null | head -1 | tr -d '[:space:]')"
[ -n "$STATUS" ] || STATUS="UNKNOWN"

echo "════════ git-prune-when-quiet ════════"
echo "  現況     ${BEFORE}"
echo "  窗口     ${STATUS}"
if [ -s "$REPO/.git/gc.log" ]; then
  echo "  gc.log   $(tr '\n' ' ' < "$REPO/.git/gc.log" | cut -c1-110)"
else
  echo "  gc.log   （沒有，auto-gc 上次沒抱怨）"
fi

if [ "$STATUS" = "ACTOR_BUSY" ] || [ "$STATUS" = "UNKNOWN" ]; then
  if [ "$STATUS" = "UNKNOWN" ]; then
    echo "  → 原樣退場：問不出窗口狀態。量不到不等於乾淨（REFLEXES #85），一律當成不可動。"
  else
    echo "  → 原樣退場：有 writer 正在產生物件，DNA #35 禁止此刻跑破壞性 git op。"
  fi
  echo "    這不是失敗，是這支存在的理由。下一班照跑即可，窗口乾淨時它自己會動手。"
  bash "$GUARD" 2>/dev/null | sed 's/^/    /'
  exit 10
fi

if [ "$APPLY" -ne 1 ]; then
  echo "  → 窗口可用，但沒帶 --apply，只報告不動手。"
  exit 11
fi

echo "  → 窗口乾淨，開始回收（prune 與 gc 都用預設的兩週保護期，不碰新物件）"
git prune --expire=2.weeks.ago 2>&1 | sed 's/^/    /'
git gc --prune=2.weeks.ago --quiet 2>&1 | sed 's/^/    /'
rm -f "$REPO/.git/gc.log"
echo "  回收後   $(counts)"
echo "  ✅ 完成（gc.log 已清；auto-gc 下次不會再對每個 git 指令印那四行）"
