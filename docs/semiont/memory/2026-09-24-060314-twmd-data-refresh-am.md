# 2026-09-24-060314-twmd-data-refresh-am — 第十九夜讓場 14 步全綠零 stale；排程快照提前落檔，routine 面板第一次拿到當天的資料

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01:28 → 06:16 +0800（2 commits：`f4c4c19ab` refresh + 本篇收官）
> 資料來源：`git log %ai`、排程器 `lastRunAt`

## 觸發

排程 06:00 觸發。任務三段：跑 14 步資料刷新、把排程器的即時狀態落檔、處理 Step 11 新鮮度閘門可能抓到的過期檔。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 落檔 260,659 bytes，Read 分頁讀到 `wake:END`，11 項體檢全綠。器官 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐90，最低仍是免疫 59（`review_coverage` 19，黃燈自 07-05）。Q14：過去 48 小時幾乎全是統一調度器的十二語批次，00:30 那班把旗艦文十二語收齊、修了五道閘門誤判；embeddings 05:00 那班確認前夜殼層修補已送達本機，交接段只剩「明晚第一次用正確的殼啟動」。觀察者 09-19 最後在場。

## 讓場與提前落檔

`ACTOR_BUSY`：dispatcher 98122 已連跑三天，帶四個翻譯進程在寫工作樹。`git fetch` 量到本機與 origin 同為 0/0，Step 1 拉不到東西，stash 卻會把 worker 手上的檔案抽走，於是照前十八夜切掉 Step 1，只跑 2–14。runner 用 header 加第 116 行之後組成，`bash -n` 過，後段零引用 Step 1 的三個變數。

昨天交接的那條「Step 6.6 面板永遠拿昨天的 live-state」，今天換了一個順序：pipeline 丟背景後，趁 Step 2 還在抓資料就先呼叫 `list_scheduled_tasks` 並跑 `routine-live-normalize.py`，讓 `routine-live-state.json` 在 6.6 讀它之前就是今天的。結果 `stale_hours=0`，18 條裡 13 operational、4 disabled、1 degraded，degraded 的是本 routine 自己（它的尺是今天的 memory 檔，就是這一篇）。這次是當班手動排對順序，下一班不會自動這樣做，所以交接仍掛著。

## 14 步結果

三源全綠：CF 七天 4,381,553 requests、404 率 1.1%、AI crawler 220,248 次跨 18 家（前夜 213,667）；GA4 與 SC 各 20 筆。`_translations.json` 12,938 筆零孤兒（前夜 12,801）。spore 166 篇 unchanged、0 warnings；免疫維持 59，`external_rulers` 3.5；fork-census 零新子代。llms.txt zh 1122／en 1107／ja 1063／ko 1107／es 1108／fr 1109；GitHub ⭐1187 🍴187 👥75。build 1,963 秒、ms/page **148**（前夜 158，七夜來第一次回落；但趨勢檔只覆蓋 1.9 天，「7d 平均」其實只有一個樣本）。Step 11：14 個 dashboard JSON 全是今日 mtime，analytics 內容日 2026-09-23（UTC），**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors，Step 13 no-op，Step 14 INDEX 722 行。

404 監測（09-22 全日 5,537 筆）：unknown 2,084 佔 37.6%，已低於昨天交接設的「過半才動判準」門檻，本班不動掃描器。重複語言前綴（`/frfr/…`）在只取前 300 條的 `top_paths` 裡今天只剩一條 3 筆，截斷的視野量不出昨天那 81 條路徑的全貌，所以沒有拿它去登記決策。

## 收官時撞到的索引殘影

`f4c4c19ab` 用 `git commit -- <37 paths>` 收官（昨天驗證過能避開 babel 同時段的 commit），commit 後其中 14 檔呈 `MM`。追查：HEAD 與工作樹都是 prettier 格式化後的版本，索引留著格式化前的 README 表格與 JSON，是 lint-staged 在 pathspec commit 的暫存索引上改完、回頭沒清掉原索引。embeddings 05:59 收官的 memory 檔也是同一個狀態，一個早上兩班。兩者都先驗 `git diff --quiet HEAD` 再 `git reset -q -- <paths>` 清掉，工作樹沒動。這在 LESSONS-INBOX 已有條目（`formatter-vs-generator-quote-churn-fakes-scope-alarm`，08-10），本班補兩個 instance，vc 1 → 3，並補上新的風險面：dispatcher 若 commit 整個索引，會把舊 blob 帶走，把 README 格式還原並記在翻譯批次名下。

push 撞上 pre-push 等 in-flight deploy 120 秒，放行後推上，本機與 origin 0/0。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅                                                    |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                         |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary`（見下） |

## Handoff 三態

繼承 `2026-09-23-061513-twmd-data-refresh-am`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註，已擴散 12 語）仍 OPEN，等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 維持停用，本輪 live-state 與排程器一致。
- [ ] pending（延續，席位 09-27 `twmd-self-evolve-weekly`）— `routine-sync.py` 對賬前 `git fetch`，有差印一行並 exit 非 0（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，同席位 09-27）— `routine-sync.py` 的 `load_live()` 應印鏡像 mtime、超過 24 小時標 ⚠️（REFLEXES #82／#85）。
- [ ] pending（延續，本輪加一個數據點）— build perf ms/page 125→138→136→139→143→158→**148**。第一次回落，但趨勢檔覆蓋僅 1.9 天，不能讀成改善。可執行動作不變：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion` 拉 CI 歷史找起跳點（REFLEXES #41），建議 Review／Full session 認領。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 讓自動 gc 停擺；平行 writer 期間不動（REFLEXES #35）。
- [ ] pending（1-file，routine prompt，REFLEXES #43 變體）— Step 6.6 面板讀 live-state 的順序問題。本班手動把 Stage 1.5 提到 pipeline 背景執行期間做，`stale_hours` 0；要讓下一班自動這樣做，routine prompt 的 Stage 1.5 應寫成「pipeline 丟背景後立刻跑，不等它結束」，或末尾補一行 `node scripts/core/generate-dashboard-status.mjs`。prompt SSOT 的修改屬 routine 管理層，本班不改殼。
- [ ] pending（觀察，`monitor-404.py`）— unknown 37.6%，低於過半門檻；維持條件式：連兩夜回到過半且榜首是探路檔名才收判準。`/terminology/{中文詞}` 與 `/{lang}/{category}/{English Title}` 兩種形狀仍待先判來源。
- [ ] pending（需判斷）— 重複語言前綴 404 要不要補 301（昨天量到 81 條路徑 243 筆，全為瀏覽器 UA）。今天在前 300 條視野裡只剩 1 條；要判斷得先從 `state.json` 或 CF 全量撈，不能用截斷的 `top_paths`。量到仍有規模再登記 OBSERVER-QUEUE。

本 session 新 handoff：

- [ ] pending（LESSONS `formatter-vs-generator-quote-churn-fakes-scope-alarm`，vc=3）— pathspec 收官後固定清一次「工作樹等於 HEAD 的索引殘影」；refresh 與 embeddings 兩條 routine 都用 pathspec 收官，都會長。可做成小工具或寫進兩條 routine prompt 的收官步驟。

## Beat 5 — 反芻

今天把昨天那條交接做掉的方式，是在不改任何檔案的前提下調整自己動作的先後。面板遲一天的原因是「唯一能寫那個檔的步驟排在唯一會讀它的步驟後面」，而那兩個步驟一個在 bash、一個在 session，bash 的順序改不了，session 的順序每天由當班自己決定。所以今天綠了，明天會不會綠，取決於明天那一班有沒有讀到這一段。這正好是交接傳得動動作、傳不動習慣的樣子，真正的修法仍然是 prompt 那一行。

收官時那 14 個 `MM` 則是昨天的解法長出來的副作用。pathspec commit 是為了不讓 babel 把我的檔掃走，它做到了，代價是把格式化前的舊版留在索引，而那個索引正是 babel 會拿去 commit 的地方。昨天的交接把它記成「已驗證有效」並建議寫進 prompt；今天才看到它把風險換了一個方向：原本是我的檔被別人帶走，現在是我的舊檔可能被別人帶走。檢查一個解法有沒有效，要看它原本防的那件事，也要看它留下了什麼。

🧬

---

_v1.0 | 2026-09-24 06:16 +0800_
_session twmd-data-refresh-am — cron 06:00 每日 14 步資料刷新（第十九夜讓場）_
_誕生原因：排程 06:00 觸發，babel dispatcher 仍在寫工作樹_
_核心洞察：session 層的順序每班重新決定，手動排對一次不會留給下一班；pathspec 收官防住了被掃走，卻在共用索引留下格式化前的舊 blob。_
_LESSONS-INBOX：`formatter-vs-generator-quote-churn-fakes-scope-alarm` +2 instance（vc=3）_
