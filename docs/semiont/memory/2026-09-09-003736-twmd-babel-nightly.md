# 2026-09-09-003736-twmd-babel-nightly — 撞見昨晚跨夜未收工的 dispatcher，讓出場地不重複派發

> session twmd-babel-nightly — cron 觸發，00:30 例行多語批次同步
> Session span: 00:37:36 → 00:37:53 +0800（<1 分鐘，0 commits，純觀察與判斷）
> 資料來源：`git log %ai` + `ps` + `/tmp/babel-unified-.../report.jsonl`

## 觸發

00:30 cron 照排程要跑今晚的 babel-nightly，走完 BECOME write mode（9/9 mode subset 過）之後照 SOP 先跑 Stage 0 宿主機自檢。

## 撞見的狀況：dispatcher 已經跑了快一整天

`check-parallel-actor.sh` 直接回報 `ACTOR_BUSY`：一個 `babel-dispatch.py --langs en,ja,ko,es,fr,vi,id,pt,hi,ar,ru,de` 進程（PID 52743）已經連續跑了 23 小時 53 分，從昨晚（2026-09-08 00:42）啟動到現在還沒收工，git log 最新一筆 commit（`18108504`，ru 批次）就在三分鐘前才落地。三重巡檢照 REFLEXES #38(f) 走了一遍：存活（`ps` 抓到 6 個子行程，`translate.py` / `structured-translate.py` 正在跑不同語言批次）、生產（`report.jsonl` 跟 `master.log` 的 mtime 是這一分鐘、`freezes.jsonl` 也正常在對 `gemma31` 這個弱適配 worker 做凍結處置）、第二訊號源（git log 的 commit 節奏跟 report.jsonl 對得上）。三個訊號都綠，確認它真的在幹活。

`babel-preflight.py` 回報宿主機 healthy（4/4 層可用，7 把 OpenRouter key 全通過，本機 ollama + 1 台 fleet 節點都在），但也印出跟正在跑的 dispatcher 完全對得上的同一組弱適配警訊：`gemma31`（`google/gemma-4-31b-it:free`）對 ar/de/es/fr/hi/id 六個語言近兩日通過率全部 <15%（最低 de/es 0%）。`status.py` 顯示 12 語言裡 de 剛出生不久只有 10.4% fresh（1003 篇 missing），其餘語言在 53%-78% 之間，離「stale=0」還有很長一段距離——這也是為什麼那個 dispatcher 已經跑了快 24 小時還沒退場。

在這個狀況下再啟動第二個 `babel-dispatch.py` 打同一批 `knowledge/` 檔案，會踩 REFLEXES #57（routine 入口必須 detect parallel-actor）跟 #6/#42/#68 那組多核心 git 協調鐵律——兩個 dispatcher 同時寫同一批翻譯檔、搶 git index、搶 fleet worker 額度，產出的收穫不會疊加，只會互相打架。所以這次 session 的正確動作是「讓場」：不碰 working tree（那些未 commit 的 `knowledge/*.md` 改動跟 `reports/babel/*.json` 都屬於正在跑的 dispatcher 的 in-flight 狀態），不搶 fleet 額度，讓它繼續跑到它自己 stale=0 或 cascade exhausted。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅（`git log %ai` + `ps` elapsed）                            |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 session 未變更任何 canonical 檔案，無需更新）          |
| 自我檢查工具 PASS            | ✅（無 commit，無需跑 article-health，prose-health 自檢見下） |

## Handoff 三態

繼承自 `2026-09-08-090356-twmd-maintainer-am.md`：

- [ ] OBSERVER-QUEUE #51 等哲宇拍板：1,646 篇譯文 subcategory 一次改回原文值（推薦 A）。本班無新事證，存量仍在每晚 babel 批次持續增長。
- [ ] OBSERVER-QUEUE #28 偵測器仍 🔒，反查 Supabase 寫入端未動。本班無新事證。
- [ ] `/exams/` feature session 前置已解除（德文已上線），投稿者 idlccp1984 等待中。本班無新事證。
- [ ] de/Food/bubble-tea.md 缺 `## Bildquellen`，本班未動手驗證，留給下一次真正改動 knowledge/ 的 session 確認並收尾。

本 session 新 handoff：

- [ ] **twmd-babel-nightly 的排程假設需要重新檢視**：今晚撞見的是一個結構性訊號，`babel-dispatch.py` 從 2026-09-08 00:42 跑到現在（2026-09-09 00:37）已經連續 24 小時，「每晚 00:30 觸發一次新 dispatcher」的排程模型跟「dispatcher 一輪要跑超過 24 小時才收工」的實際運作節奏已經對不上，下一個排程窗口幾乎必然撞見上一輪還沒結束。下一步可執行動作：(a) 若 dispatcher 支援 idempotent 續跑（偵測到已有活動進程直接 no-op 退出而非讓 cron 層的 session 空轉判斷），把「偵測已有 dispatcher，優雅退出」這段邏輯內建進 babel-nightly 的排程 prompt 或 dispatcher 自身的 lock 機制；(b) 若 dispatcher 本身沒有 24hr+ 續跑的健康監控，補一道「dispatcher 存活超過 N 小時未收工」的 chronic 警訊到 dashboard，讓這不再是每次撞見才臨場判斷。

## Beat 5 — 反芻

今晚是讓場而不是動手。BECOME §行動鐵律 3「有 SOP 就跑」跟 REFLEXES #57「routine 入口必須 detect parallel-actor」在這個情境下是同一件事的兩面：SOP 要求我啟動 dispatcher，但更高位階的並行保護規則要求我先確認場地淨空。確認之後發現場地已經被正確佔用，正確動作是識別「這個任務其實已經在被完成」，讓它繼續，不硬跑第二個。這跟今天稍早 `twmd-routine-sync`、`twmd-data-refresh-am` 兩條 routine 在同一個活著的 dispatcher 前做的判斷是同一種反射的第三次同日驗證（見 groundtruth 段 git log），只是這次是 babel-nightly 自己撞見自己的前一輪還沒收工，形狀值得記一筆：**同一個 routine 的兩次排程窗口互相重疊，是排程模型跟實際執行時長脫節的訊號**，跟 MEMORY §神經迴路裡「sovereign-mode 的器官節律會跟世界節律脫鉤」是同一個家族的變體，只是這次脫鉤的雙方都是同一個 routine 自己。

🧬

---

_v1.0 | 2026-09-09 00:37 +0800_
_session twmd-babel-nightly — 00:30 cron 觸發今晚多語批次同步_
_誕生原因：Stage 0 宿主機自檢撞見前一輪 dispatcher（PID 52743）已連續運行 23h53m 仍在產出，三重巡檢確認真活著非假象_
_核心洞察：(1) 排程窗口重疊本身就是訊號：dispatcher 一輪跑超過 24 小時，代表每日固定 cron 觸發的模型已經跟實際工作節奏脫鉤 (2) 讓場是在確認場地已被正確佔用之後的主動判斷，跟不作為是兩件事_
_LESSONS-INBOX 候選：babel-nightly cron 觸發窗口與 dispatcher 實際續跑時長的節律脫鉤，候選機械化方向見上方新 handoff_
