# 2026-09-27-053928-twmd-routine-sync — 第 60 輪：babel-nightly 的新殼晚了一班才送達，因為 09-26 這班沒醒

> session twmd-routine-sync — cron 每日對賬（05:30 Asia/Taipei，實際 05:37 起跑）
> Session span: 05:37:53 → 05:45 +0800（約 8 分鐘，1 commit）
> 資料來源：`git log %ai`、scheduled-tasks `list_task_runs`
> ✅ BECOME ack: mode=micro / Q14=PASS（wake-context 讀到 `wake:END`，11 項體檢全綠；PARALLEL_CHECK=ACTOR_BUSY，babel writer 三個進程在跑）

## 觸發

每日排程。`git pull` 時本機與 origin/main 同步（0/0），對賬工具回報 18 條裡 1 條 prompt 漂移。

## babel-nightly 的 Stage 0.5 補送到機器

漂移的是 `twmd-babel-nightly`。方向不需要猜：git 版比機器版多出整段「Stage 0.5 先檢查、再續命，沒有才啟動」，其餘逐字相同，機器版是 git 版的嚴格子集。git 那段由哲宇在 `6007a0c6f`（09-25 14:51）加入，依據是 OBSERVER-QUEUE #70（已決，逾期預設 C）；機器檔最後寫入是 09-23 05:40。所以跑 `--apply --stamp 2026-09-27`，舊的機器版先存證到 `reports/routine-prompt-drift/2026-09-27-exhibitions-mac-mini-local-twmd-babel-nightly.md` 再覆蓋，重跑對賬 18/18 一致、exit 0。

照理 09-26 05:30 那一輪就該抓到這條。查 `list_task_runs`，routine-sync 的執行紀錄從 09-24T21:37Z（本地 09-25）直接跳到今天。`routine-liveness-check.py` 把它列為 silent-death（fire 09-25T21:45Z），是週報 `021339` 那六條之一，根因是 Claude Desktop 登入 09-25 23:17 過期，看門狗 `abc7f2978` 已裝上。今天這班準時醒，也替週報那條「09-27 早班若仍沒 memory 就是新病」交了第一份反證。結果是今晨 00:30 的 babel-nightly 讀的還是沒有 Stage 0.5 的舊殼。它實際上照新殼的語意在做事（產線已在跑、改做驗收，見 `010249`），所以這次漏送沒有造成錯誤行為，只是文件跟實際又錯開了一晚。

## cron／enabled 對 live 排程器

工具讀的 `routine-live-state.json` 是 05:14 的鏡像，比前幾輪新鮮。仍照前三輪的做法補驗：用 `list_scheduled_tasks` 拉 live，再用工具自己的 `parse_ssot_table()` 逐條比 cron 與 enabled，18 條對到 18 條零差。四條 enabled=false（rewrite-daily、founder-lens-weekly、spore-pick-daily、spore-publish-daily）跟 SSOT 一致，沒有動。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅                                        |
| Handoff 三態已審視           | ✅                                        |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無器官狀態變更）              |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile） |

## Handoff 三態

繼承自 09-25 第 59 輪（09-26 那輪沒醒，這四條原樣過了兩天）：

- ⏳ blocked：issue #1729（馬英九腳註）等 Write session 帶哲宇 review；`spore-pick-daily`／`spore-publish-daily` 是 manual-by-decision（ROUTINE.md 註 ¹³），本輪 enabled 一致，未打開。
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04；該席位改得動 `scripts/tools/`）：`routine-sync.py` 對賬前自己 `git fetch`，routine 層有差時非 0 exit。今晨 self-evolve 選了另外四件，這條第 7 輪往下傳。
- [ ] pending（同席位、同檔）：cron／enabled 對賬改讀 live，或至少印出 `routine-live-state.json` 的新鮮度。本輪是第四次手動補驗，比對邏輯就是上面那段 `parse_ssot_table()` 對 live JSON。
- [ ] pending（席位 `/twmd-routine` 或任何改得動 routine prompt 的 session）：第 6 步收官改成 `git commit -- <path>`，babel dispatcher 共用 index 時才不會把它 staged 的檔帶進來。本輪照做。
- [ ] pending（席位 `/twmd-routine`）：`twmd-embeddings-nightly` 跨過 05:30 收官，改殼要隔兩晚生效；推薦 (b) embeddings 收官改完殼順手跑 `routine-sync.py --apply`。

本 session 新 handoff：無。（本想交出「routine-sync 缺席沒人叫」，查證後 `routine-liveness-check.py` 早就涵蓋它，週報也已抓到，撤回。）

## Beat 5 — 反芻

今天修的那一條，本來昨天就該修。對賬工具本身沒有漏，漏的是它沒被叫起來，而沒跑的那一輪不會在自己的輸出裡留下「我沒跑」。我第一個反應是要替這件事開一條新交接，查了一下才發現外面那把尺（liveness 檢查）早就量到了、週報也已寫明根因。這次運氣好，晚一晚送到的是一段描述既有行為的文件，babel 夜班照舊做對了事；換成改變行為的殼層修補，漏送那一晚就是真實的錯誤執行。登入過期的代價，會沿著這種「對賬器缺席一天」的路徑多傳一站。

🧬

---

_v1.0 | 2026-09-27 05:45 +0800_
_session twmd-routine-sync — 第 60 輪 cron 對賬；prompt 17/18 → 18/18（babel-nightly git→機器），cron／enabled 對 live 零差_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發_
_核心洞察：09-26 這班因登入過期沒醒，讓 09-25 下午 ship 的殼層修補晚一晚才送達；開新交接前先查外部尺有沒有已經量到。_
