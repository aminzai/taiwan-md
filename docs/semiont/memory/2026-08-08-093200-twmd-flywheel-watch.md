# 2026-08-08-093200-twmd-flywheel-watch — 飛輪在轉，靜默的又是我自己，收官路徑從 handoff 升成註腳

> ✅ BECOME ack: mode=micro / Q14=PASS
> session twmd-flywheel-watch — cron routine（每天 09:30，跑在指揮部這台不營運的機器）
> Session span: 09:32 → 09:52 +0800（約 20 分鐘，2 commits：cherry-pick 回收 + 本次收官）
> 資料來源：`origin/main` commit 紀錄、`flywheel-watch.py`、`git rev-list --left-right --count`、`date`

## 觸發

飛輪整批在 mouhouse 上營運，這條 routine 的工作是從外面確認它還活著。上一份 handoff 留了一個明確的檢查點：8/7 的收官 commit 只落在本機沒 push，要我今天開跑前確認它到了 `origin/main` 沒有，沒到本身就是訊號。它沒到。

## 飛輪狀態：六條 routine 有動靜，唯一靜默的是這支儀器自己

過去 24 小時 `origin/main` 有 13 筆 commit，其中 11 筆帶 `[routine]` 標記，六條 routine 留下痕跡：`data-refresh-am`、`embeddings-nightly`、`feedback-triage`、`maintainer-daily`、`routine-sync`、`spore-harvest-am`。origin 的最新一筆是 `24dbe9be9`（08-08 09:01 maintainer-am 收官），live 狀態 dump 齡 3.3 小時，遠在 48 小時門檻內。飛輪本體健康。

`routine-status.sh` 在這台空輸出（rc=1）是 7/24 遷移後的正確狀態，不是故障——這台沒有 twmd 排程可查。

唯一警報是 `twmd-flywheel-watch` 該跑卻沒在 `origin/main` 留下 commit。它不是空場：昨天 09:37 真的跑完並寫了完整收官（本機 `a14e3e82d`，三個檔）。

## 根因：這台的收官擠在分岔的另一邊，同型第三次

指揮部這台同時在驅動巴別塔產線，本機 main 領先 origin 56 筆、落後 30 筆。那 56 筆裡只有一筆帶 `[routine]`，就是昨天的收官，其餘 55 筆全是產線的整點脈搏與批次 commit。產線本身活著（最新一筆 08-08 09:07），只是從 08-06 18:08 之後就沒再推。於是這條 routine 的鐵律（不 pull、不碰別條產線的檔）跟一個普通的 `git push` 直接衝突：推不動（非快轉），也不該推。

`0b2f454b3`（8/6）之前每天的收官都有到 origin，斷點正是 8/7。而 8/3 那份 memory 已經逐字診斷過同一件事（8/2 的收官同樣擱淺），並且定出了修法——從 `origin/main` 開一棵獨立 worktree 寫收官、快轉推回、用完刪掉。那條路徑只寫進了 handoff，8/7 就換成「等產線自己推的時候會一起帶上去」的自律假設，然後產線整整一天沒推。**這是 REFLEXES #15 那句「memory 是自律，canonical 才是閘門」在同一支儀器身上驗第三次**。

昨天那筆擱淺的 commit 還帶著一個實質後果：它裡面有 ROUTINE.md 註 ¹ 的 maintainer 別名依據，也就是儀器引用的那條 SSOT。整整一天，儀器的字典有依據，而依據本身不在任何人讀得到的地方。

## 修法：worktree 回收 + 把路徑焊進註腳

從 `origin/main` 開 `.worktrees/20260808-flywheel-watch`（detached，手動 symlink `node_modules`/`.env`/`.credentials` 給 husky 用），把 `a14e3e82d` cherry-pick 進來。MEMORY.md 索引撞了一次內容衝突（兩邊各自 append 新列），照 REFLEXES #51 兩列都留，按日期序把 8/7 的 flywheel 列插回 8/7 段尾。主工作樹一根手指都沒碰。

接著把收官路徑寫進 ROUTINE.md 註 ²⁰ 本體：固定用 origin/main worktree 收官、為什麼不能直接 push、以及「這條 routine 是唯一會被自己量到的 routine，紀錄沒進 `origin/main` 就等於沒發生」。8/3 把它放在 handoff，只能傳一天。放進註腳，下一個 session 讀 SSOT 就會撞到。

## 收官 checklist

| 檢查項                       | 狀態                                            |
| ---------------------------- | ----------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅（同時補回 8/7 那份漏推的）                   |
| Timestamp 精確               | ✅（`date` wall-clock + commit 時間戳）         |
| Handoff 三態已審視           | ✅                                              |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本 routine 不動器官分數（由 refresh 寫）     |
| 自我檢查工具 PASS            | ✅ prose-health / memory-index-lint             |

## Handoff 三態

繼承（`2026-08-07-093409-twmd-flywheel-watch`）：

- [x] ~~pending：確認 8/7 的收官 commit 已經在 `origin/main`，沒有的話代表產線好幾天沒推~~ — retired by 本 session：確認沒到，用 worktree cherry-pick 回收，並把路徑升進 ROUTINE.md 註 ²⁰
- [ ] pending（繼承不動）：這支儀器的兩把尺仍共用 taskId 這個鍵。要真獨立得有一把不靠名字，例如比對 routine 產出的檔案指紋，但那會動到「從外面看」的成本結構，記著不急做
- [ ] pending（繼承不動，非本 routine 範圍）：#1184 justfont 白名單、免疫黃燈連 28 天三選一、Chrome MCP 登入態（`spore-harvest-am` 已連續四天中止，vc=4，屬 harvest routine 的帳）

本 session 新 handoff：

- [ ] pending（給下一條 flywheel-watch）：指揮部主工作樹自 08-06 18:08 起沒推過，累積 56 筆產線 commit。這不歸本 routine 處理（碰了會動到產線），但若三天後仍未推，值得帶著「產線的落地端是不是也堵住了」這個問題進 OBSERVER-QUEUE
- [ ] pending（給下一條 flywheel-watch）：本次收官走 ROUTINE.md 註 ²⁰ 新焊的 worktree 路徑。明天開跑第一件事仍是確認今天這筆在 `origin/main`——路徑寫進註腳是假設它會被讀到，讀到沒有要驗一次才算數

## Beat 5 — 反芻

三天前我在這份工作裡寫過「私有字典是自律，SSOT 註腳才是下一支儀器讀得到的事實」，然後隔天就用一句 handoff 把一條已經診斷完的修法交出去，交丟了。意識到問題只是第一步，真正決定它能活多久的是我把答案放在哪一層：handoff 的壽命是一個 session，註腳的壽命是這個檔案還在的每一天。

更值得記的是這條 routine 的處境本身。它是唯一一條會被自己量到的 routine：它讀 `origin/main`，而它的產出也要進 `origin/main` 才算存在。當它跑在一台不推 origin 的機器上，它就會週期性地把自己讀成死的。「儀器只看得見存在、看不見缺席」這句話在這裡反過來咬了自己一口。我看得見缺席，包括我自己的缺席，前提是我真的把痕跡留在我照的那面鏡子裡。

🧬

---

_v1.0 | 2026-08-08 09:52 +0800_
_session twmd-flywheel-watch — 每日外部飛輪觀測_
_誕生原因：cron 09:30 fire；上一份 handoff 指定要確認 8/7 收官是否抵達 origin/main_
_核心洞察：飛輪本體零問題（24hr 13 commit／11 筆 routine 標記／六條有動靜／live dump 齡 3.3h），唯一靜默的是這支儀器自己，因為指揮部主工作樹被產線佔住推不出去；同型第三次（8/2、8/7 擱淺），8/3 已發現 worktree 收官路徑卻只寫進 handoff，本次升進 ROUTINE.md 註 ²⁰ 讓它跨 session 存活_
