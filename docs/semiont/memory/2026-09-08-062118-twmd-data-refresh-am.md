# 2026-09-08-062118-twmd-data-refresh-am — 撞上跑了 5 小時的 babel dispatcher，Step 1 繞開改手動跑 2-14 步

> session twmd-data-refresh-am — cron 排程觸發（06:00 daytime dashboard 14-step sync）
> Session span: 約 06:09 → 06:30 +0800（含 BECOME 甦醒 + pipeline 執行）
> 資料來源：`git log %ai` + `check-parallel-actor.sh` + `ps`

## 觸發

排程 `twmd-data-refresh-am` 06:00 daytime 定時觸發，走 STRICT BECOME GATE micro mode 後執行 DATA-REFRESH-PIPELINE。

## Step 1 git sync：現查後跳過，不是照腳本跑

啟動時 `check-parallel-actor.sh` 回報 `ACTOR_BUSY`：`babel-dispatch.py --rounds 200` 已跑 5 小時 29 分（`/tmp/babel-unified-20260908-004220-52743`），底下 6 支 `structured-translate.py` / `translate.py` worker 仍在寫 `knowledge/{lang}/...`，每 10 篇自己 commit 一次。`refresh-data.sh` Step 1 的做法是 `git stash push --include-untracked` 把整棵工作樹（含 dispatcher 尚未 commit 的產出）先搬走再 `git pull --rebase` 再搬回來——這對一個正在寫檔、正在自己 commit 的平行 process 是真實風險（git index lock 碰撞 / stash 期間磁碟上檔案暫時消失）。

先查 `git rev-list --left-right --count HEAD...origin/main`：ahead 3 / behind 0，代表這次 pull 本來就沒有東西可拉，stash+pull+pop 整套動作在此刻是「零收益、有風險」。於是不跑 `refresh-data.sh` 整支腳本，改成手動依序執行 Step 2-14（跳過 Step 1），行為上等同「pull 沒事做，正常跳過」，只是省了一次不必要的 stash round-trip。這是今天沿用昨天 `twmd-routine-sync`（05:38 那輪）撞見同一個 dispatcher 時「現查後繞開」的同一套判斷，把它套用到 data-refresh 這個真的需要碰 git sync 的 routine 上。

## npm run prebuild 意外撞見環境問題

Step 7 第一次跑 `npm run prebuild` 直接炸：`node_modules` 缺 `typescript` 套件（`ERR_MODULE_NOT_FOUND`），`npm ls typescript` 回空。`npm install typescript --no-save --no-audit --no-fund` 補回 214 個套件（同時 removed 12 / changed 95，代表整個 `node_modules` 對 `package-lock.json` 已經漂移一段時間，不只缺一個套件），`package.json` / `package-lock.json` 都沒被動到（git status 乾淨）。裝完重跑 `npm run prebuild` 正常過。這是這台機器（`musebase`，非平常跑 routine 的機器路徑）第一次跑這條 pipeline 疑似留下的環境落差，跟本次 routine 邏輯無關，純粹環境缺口。

## Step 11 freshness gate：mtime 全綠，content 欄位撞到時區假警報

14 個 `public/api/dashboard-*.json` 逐一核對 mtime，全部是今天（`2026-09-08`），真正的訊號乾淨、零 stale。但 `dashboard-analytics.json` 內容欄位 `lastUpdated` 用 `datetime.now(timezone.utc)` 寫入 UTC 時間，這台機器系統時區是 `Asia/Taipei`（CST，UTC+8）。06:19 CST 執行時 UTC 還停在前一天 22:19，`ANALYTICS_DATE`（UTC 日期）跟 `TODAY`（CST 本地日期）比對就會判定「stale」，即使內容其實是幾秒鐘前才重新生成的。這是「兩把尺量不同時區」的結構性假警報，只在本地時間落在 UTC 前一天的窗口（CST 00:00-07:59）才會出現——剛好完全覆蓋 `twmd-data-refresh-am` 06:00 這個排程時段。**沒有當 cycle wire fix**：這不是 catch-同一個 stale JSON 兩次連續 cycle 那種「generator 沒接」的情況（per DATA-REFRESH-PIPELINE catch≠fix 鐵律），而是 checker 本身比較邏輯的時區假設在這台機器不成立，屬於另一類問題（REFLEXES #38 混維度 / #65 checker 兩把尺），值得下一個真的要動 `refresh-data.sh` Step 11 或 `generate-dashboard-analytics.py` 的 session 順手把比較改成同一時區或改用「N 小時內」而非「日期字串相等」。

## Stage 1.5 — scheduler live-state dump

`mcp__scheduled-tasks__list_scheduled_tasks` 抓到 18 條任務（14 enabled + 4 disabled），跟昨天一致無變動。跑 `routine-live-normalize.py` 寫回 `docs/semiont/routine-live-state.json`。

## 收官 checklist

| 檢查項                       | 狀態                                                             |
| ---------------------------- | ---------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                               |
| Timestamp 精確               | ✅（git log %ai）                                                |
| Handoff 三態已審視           | ✅（見下）                                                       |
| commit 範圍紀律              | ✅（`verify-commit-scope.sh` 驗 35 檔，逐檔核對無 babel 檔混入） |
| 自我檢查工具 PASS            | ✅（pre-commit 兩次乾淨過）                                      |

## Handoff 三態

繼承 `2026-09-08-054309-twmd-embeddings-nightly`：連續第三個乾淨綠燈夜，無待接事項；譯文中文 wikilink 待翻譯映射修正 / Supabase 管理頁待登入 / 原住民歌手文章待補授權圖說等各自 owner 的舊項，跟本 routine 無關，原樣不重複。

本 session 新 handoff：

- [ ] pending（給下一個真的要動 Step 11 或 `generate-dashboard-analytics.py` 的 session）— `dashboard-analytics.json` 的 `lastUpdated` UTC 時間戳在 `Asia/Taipei` 本地時區的機器上，於本地 00:00-07:59 執行 refresh 時會被 Step 11 誤判 stale（實際內容是新的）。建議修法：freshness gate 比較改用同一時區（例如都轉 UTC 再比），或改成「距今 N 小時內」而非「日期字串相等」。非急件，目前只造成一次性 log 噪音，不影響實際資料新鮮度。
- [ ] pending（給下一個碰 `npm run prebuild` 或環境設定的 session）— 這台機器（musebase 路徑）的 `node_modules` 對 `package-lock.json` 有明顯漂移（一次 `npm install` 補了 214 個套件、移除 12、改了 95），值得確認是不是這台機器本來就沒跑過完整 `npm ci`，或者是不是該固定用 `npm ci` 而非 `npm install` 做環境還原。

## Beat 5 — 反芻

今天沒有照本宣科跑腳本，是先看了 `check-parallel-actor.sh` 的 `ACTOR_BUSY`、算了一下 ahead/behind、確認 stash 真的沒有必要之後，才決定跳過 Step 1。跟昨天 `twmd-routine-sync` 那輪「先現查再動作」的教訓一樣：工作樹很吵（56 個 dirty 檔）容易讓人反射性覺得「這是殘留，可以隨便碰」，但先問一句「這是不是有人正在做的事」，才分得出繞開跟清理的差別。今天多了一層：`refresh-data.sh` 的 Step 1 本身寫死了「dirty 就 stash」，沒有 parallel-actor 感知——這條腳本目前假設任何時候跑它的都是唯一 writer，但巡邏節律已經密到 babel-nightly 常態性跨過 06:00 的邊界。之前 §神經迴路已經記過「babel-nightly 4hr49min 撞 06:00 morning chain」，這次是同一個結構第二次被撞見，只是這次撞見的人剛好有工具可以現查、可以判斷「這次 pull 沒事做」而不必被迫二選一（等 5 小時 vs 冒險 stash）。加上 npm 環境缺口 + 時區假警報，這輪的三件事共同點是：儀器（parallel-actor 偵測 / freshness gate / node_modules 完整性）各自在正確的位置響了，接下來要做的是判斷「響了要不要當場修」還是「響了但這次沒事,留給對的人」。

🧬

---

_v1.0 | 2026-09-08 06:21 +0800_
_session twmd-data-refresh-am — cron daytime 14-step 資料刷新，撞上跑 5 小時的平行 babel dispatcher_
_誕生原因：排程 06:00 觸發 DATA-REFRESH-PIPELINE 例行執行_
\_核心洞察：(1) parallel-actor 感知目前只在旁支工具（check-parallel-actor.sh）裡，refresh-data.sh 本體的 Step 1 完全沒有這層意識，值得評估要不要把偵測 wire 進腳本本身而非靠呼叫端每次手動判斷 (2) UTC vs 本地時區的日期字串比較是一種會在特定時段固定發作的假警報，不是隨機噪音
