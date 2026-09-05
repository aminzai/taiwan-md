---
title: 'mouhouse 四天空窗根因 2026-09-05'
description: '08-23 21:06 → 08-28 05:05 排程器零產出的根因：Claude Desktop OAuth refresh token 登入滿 30 天過期（session_stale_relogin），排程照 fire、lastRunAt 照更新、session 起不來；預測下一次過期 09-26～27'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-154128-fortnight-review'
related:
  - 'fortnight-deep-review-2026-09-05.md'
  - 'routine-audit-2026-08-30.md'
  - 'routine-migration-mouhouse-macmini-2026-07-24.md'
  - '../docs/semiont/OBSERVER-QUEUE.md'
---

# mouhouse 四天空窗根因 — 2026-09-05

> 兩週體檢（[fortnight-deep-review-2026-09-05.md](fortnight-deep-review-2026-09-05.md) §2.4）寫「根因至今未判」。哲宇拍板第 12 題選 B：他開 Tailscale，我 SSH 進 mouhouse 只讀 log。以下全部來自 `~/Library/Logs/Claude/main1.log`（涵蓋 08-18 → 09-01）、`pmset -g log`、`uptime`，沒有改任何設定。

## 一句話

排程器沒有停，機器沒有睡，是 **Claude Desktop 的登入 session 在滿 30 天那一刻過期**，之後每一條排程照時間 fire、照樣把 `lastRunAt` 往前推，但每個 session 都在啟動時被擋回「Sign in again to continue」。直到有人在 08-27 傍晚到 08-28 清晨之間重新登入，飛輪才在 08-28 05:05 的 embeddings 那一趟恢復。

## 證據鏈

| 時間（+0800）             | 事件                                                                                                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-07-24 17:37          | mouhouse 遷居當天 Google 登入（`[Auth] ASWebAuth completed success`），oauth token 首次交換                                                                                                                                    |
| 08-23 08:38               | `twmd-maintainer-daily` 最後一次 `Confirmed task run`，09:45 idle 暫停                                                                                                                                                         |
| **08-23 21:06:54**        | `OAuth token refresh failed: status=400 {"error":"invalid_grant","error_description":"Refresh token expired"}` → `session_stale_relogin`：「sessionKey is valid but too old for the requested scope expansion. Sign in again」 |
| 08-23 21:06:55            | `twmd-routine-audit-weekly` 的 session `Cannot start session`；八分鐘後 `Cleared stale pending dispatch`                                                                                                                       |
| 08-24 → 08-27             | 每一條排程（supporters／embeddings／routine-sync／data-refresh／spore-harvest／feedback-triage／maintainer）每天照 fire，全部同一個錯，共 27 次；`lastRunAt` 每次照更新                                                        |
| 08-26 05:17               | app 自動更新到 2.1.241 重啟，`Failed to warm session … session_stale_relogin`；08-26 10:28、08-27 09:39 再重啟兩次，同錯                                                                                                       |
| 08-27 09:39 → 08-28 05:05 | 期間有人重新登入（log 未記 ASWebAuth 行，推斷在此窗口）                                                                                                                                                                        |
| **08-28 05:05:33**        | `Confirmed task run for: twmd-embeddings-nightly`，飛輪恢復                                                                                                                                                                    |

排除項：`uptime` 14 天 23 小時（最後重開 08-21 18:04，在空窗之前）；`pmset -g log` 08-23 到 08-28 零 sleep／wake 事件，`sleep 0（sleep prevented by powerd）`、`autorestart 1`、`womp 1`，機器一直醒著；三次 app 重啟都不是修法，錯誤是帳號層的。

## 為什麼四天沒人知道

1. **失敗住在桌面 app 的 log 裡，沒有任何 routine 讀它。** routine 是 Claude session；session 起不來，等於所有跑在飛輪身上的儀器一起失明（REFLEXES #82「儀器只看見存在、看不見缺席」的最極端形態：連儀器本身都沒出生）。
2. **`lastRunAt` 是會說謊的代理訊號。** 排程器在 spawn 那一刻就更新它，不等 session 確認。任何拿 `lastRunAt` 當「有跑」的檢查（含 routine-live-state.json 的讀者）都會看到一台準時上工的機器。真正的尺是「fire 之後有沒有 commit」，也就是 08-30 週體檢 `routine-liveness-check.py` 與今天上線的 `routine-stall-check.py` 用的那把。
3. 08-10 停用的 flywheel-watch 是唯一跑在飛輪外面的眼睛（REFLEXES #82／ROUTINE 註 ²⁵）；停用後兩層被動替代都要有人甦醒才會看，而那四天恰好沒有人。

## 這會再發生

登入 07-24 17:37，過期 08-23 21:06，相隔 30 天 3.5 小時。每天都在用並沒有延長它（refresh token 是固定壽命，不是 sliding window）。重新登入的時間落在 08-27 晚到 08-28 早，**下一次過期預估 2026-09-26 到 09-27**。這是一個可以寫進日曆的日期。

## 修法（分三層，哲宇拍第一與第二層）

| 層       | 做什麼                                                                                                                                                                                                                                                         | 誰                                                                | 狀態                  |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------- |
| 結果偵測 | GitHub Actions `routine-stall-alert` 每 6 小時查 origin/main 最近一筆 routine commit 齡，>30h 開 issue（今天上線 425e0c0a9）；這次的形狀會在 08-24 15:19 左右第一次亮                                                                                          | 已落地                                                            | ✅                    |
| 原因偵測 | mouhouse 本機 launchd 看門狗：每小時 grep `main.log` 近一小時有無 `session_stale_relogin`／`Cannot start session`，命中就推播（Telegram 或 GitHub issue），並在 `~/.taiwanmd-auth-expiry` 記下登入日算倒數。它不依賴 Claude session，所以 session 死了它還活著 | 需哲宇同意在 mouhouse 裝 launchd（我有 SSH 可裝，是機器設定變更） | ⏳ OBSERVER-QUEUE #49 |
| 預防     | 每 25 天在 mouhouse 重新登入一次（下一次 2026-09-21 前）；哲宇的行事曆建一個每 25 天的提醒。Claude Desktop 目前沒有給 headless 機器延長 session 的設定                                                                                                         | 哲宇                                                              | ⏳ OBSERVER-QUEUE #49 |

一條給 LESSONS 的教訓已同日入庫：`scheduler-lastrunat-updates-even-when-session-never-starts`（REFLEXES #82 的新載體）。ROUTINE.md §宿主機 補一行「登入滿 30 天會過期」。

🧬

---

_v1.0 | 2026-09-05 17:30 +0800_
_session fortnight-review — 哲宇開 Tailscale 後 SSH 唯讀查 log_
_誕生原因：兩週體檢與 08-30 routine 自審都寫「根因未判」，三份 handoff 把判定交給一條已停用的 routine_
_核心洞察：(1) 不是機器也不是排程器，是帳號 session 的 30 天壽命 (2) lastRunAt 在 spawn 時就更新，session 起不來它也一樣往前走 (3) 所有跑在飛輪身上的儀器在這種失敗下一起失明，看門狗必須住在 Claude 之外_
