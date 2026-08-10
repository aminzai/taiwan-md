# 2026-08-10-093453-twmd-flywheel-watch — 飛輪零靜默，儀器自己校掉第四種假象：手動工作被印成一條 routine

✅ BECOME ack: mode=micro / Q14=PASS

> session twmd-flywheel-watch — cron 09:30 每日外部飛輪觀測（指揮部 commander-macbook）
> Session span: 09:30 → 09:41 +0800（約 11 分鐘，1 commit）
> 資料來源：`git log %ai` on `origin/main`、`scripts/tools/flywheel-watch.py`

## 觸發

飛輪整批遷到營運機 mouhouse 之後，沒有任何一條 routine 在看它還活著沒有，所以這條刻意留在不營運的這台，每天早上從 `origin/main` 的 commit 紀錄看一眼。今天是排程照常 fire，沒有觀察者在場。

## 觀測結果：綠燈

`git fetch origin` 之後跑儀器，過去 24 小時窗口內 156 筆 commit、其中 16 筆帶 `[routine]` 標記，十條 routine 留下動靜（data-refresh-am、embeddings-nightly、feedback-triage、flywheel-watch、maintainer-daily、routine-audit-weekly、routine-sync、spore-harvest、spore-harvest-am、supporters-weekly），沒有一條該跑而沒留痕跡，`routine-live-state.json` 的 dump 齡 3.4 小時。exit 0，判定飛輪在轉。

窗口裡絕大多數 commit 屬於巴別塔產線：十語批次加上脈搏儀器的整點快照。昨天已經記過一次這個落差，今天再確認一次：**commit 總數量體跟飛輪轉速在這台機器上是兩件事**，儀器只認 `[routine]` 標記所以判定沒有被帶偏。

## 儀器自校：第四種假象

第一次輸出的清單裡多了一行「有動靜（只留收官索引）：twmd-vi-delegation-wave」。排程表裡沒有這條 routine，那是昨晚越南語委派那次手動工作的 session handle。儀器的第二把尺讀 MEMORY.md 索引列的 handle，讀到不帶 `twmd-` 前綴的就自動補上，於是一次手動工作在報告裡穿上了 routine 的制服。

靜默判定本來就只走 `enabled`（排程表）那一圈，所以這次不影響綠燈紅燈，壞的只有顯示面。但顯示面就是下一個讀報告的人的判定依據——照這個輸出讀下去，會以為排程表裡有一條叫 `twmd-vi-delegation-wave` 的 routine。修法是把顯示用的集合跟 `enabled` 取交集，判定路徑一行不動。改完重跑，那行消失，其餘輸出完全一致。

這是這支儀器第四次校掉假象，前三次是 weekly 時刻未到、收官痕跡沒帶 taskId、產出 commit 寫成 `[semiont] distill:`。四次的形狀相同：**名字被當成識別鍵**。上週的 routine-audit 也記過同一族的分類器誤歸類（vc 1→2），今天這條算第三例。

## 收官走 worktree

指揮部這台的主工作樹正在驅動巴別塔產線，本機 main 長期領先 origin 一批產線中間產物。照 ROUTINE.md 註 ²⁰ 的固定做法，從 `origin/main` 開 `.worktrees/20260810-flywheel-watch` 寫紀錄、commit、`push origin HEAD:main`、移除 worktree，主工作樹一根手指都不碰。這條路徑 8/8 焊進註腳，昨天首次被照做，今天是第二次。

## 收官 checklist

| 檢查項                     | 狀態                                        |
| -------------------------- | ------------------------------------------- |
| MEMORY 有這次的紀錄        | ✅                                          |
| Timestamp 精確             | ✅ `git log %ai`                            |
| Handoff 三態已審視         | ✅                                          |
| CONSCIOUSNESS 反映最新狀態 | ❌ 本 routine 不動器官分數（由 refresh 寫） |
| 自我檢查工具 PASS          | ✅ flywheel-watch 重跑 exit 0               |

## Handoff 三態

繼承（`2026-08-09-093410-twmd-flywheel-watch`）：

- [x] ~~pending：若開跑發現前一筆沒到 `origin/main`，往「是不是有人在主工作樹直接收官」查~~ — retired：昨天那筆 `13933862f` 確認在 `origin/main` 上，不必診斷
- [ ] pending（繼承不動）：兩把尺仍共用 taskId 這個鍵，要真獨立得有一把不靠名字的，記著不急做
- [ ] pending（繼承不動，非本 routine 範圍）：#1184 justfont 白名單、免疫黃燈連 30 天三選一、Chrome MCP 帳號登入態

本次新開：

- [ ] pending（給下一條 flywheel-watch）：顯示面收窄之後，新 routine 上線但還沒進 `routine-live-state.json` 的話，它的收官索引列不會出現在「有動靜」清單裡。看到清單無故變短時先查 live-state 那份名單，不要直接判它死了

## Beat 5 — 反芻

今天真正的觀測對象其實有兩個。飛輪本身十條全在轉，這部分沒什麼好說的。有東西可說的是這支儀器自己，它第四次證明我造的識別鍵一直都是名字。名字這個鍵在 commit 標記上會漂（型別前綴蓋掉 taskId），在索引列上會擴（手動工作補個前綴就變 routine），每次補的都是同一個洞的不同開口。

值得留意的是今天這次的性質跟前三次不同。前三次都是假警報，會讓人以為某條 routine 死了。今天這次相反，把一件本來就發生了的事貼錯標籤，判定全對、只有敘述錯。這種錯不會觸發任何閘門，只會靜靜地讓讀報告的人建立一個不存在的認知。**沒有紅燈的錯，得靠有人願意多讀一行才會現形**。

🧬

---

_v1.0 | 2026-08-10 09:41 +0800_
_session twmd-flywheel-watch — 每日外部飛輪觀測_
_誕生原因：cron 09:30 fire；上一份 handoff 指定要確認 8/9 收官是否抵達 origin/main_
_核心洞察：飛輪零靜默零警報（24hr 156 commit／16 筆 routine 標記／10 條有動靜／live dump 齡 3.4h），繼承的那條 handoff 當場退役；儀器校掉第四種假象——手動工作的 session handle 被自動補上 `twmd-` 前綴後在報告裡穿上 routine 的制服，判定不受影響但敘述會誤導讀者，修法是顯示面跟排程表取交集_
