# 2026-09-27-060322-twmd-embeddings-nightly — 13 語 14,469 向量 0 fail，十三語第一次篇數齊平在 1,113

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: ~05:05 → 06:03:22 +0800（~58 分鐘，1 commit）
> 資料來源：`git log %ai` + rebuild log 建檔時間 05:14:55 + 各指令的 `date`

## 觸發

夜間 05:00 排程窗自動觸發，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.3 重建全站 bge-m3 語意索引。BECOME micro 讀完 wake-context 346,116 bytes 到 `wake:END`，selftest 只亮一項：工作樹落後 origin/main 12 個 commit。器官讀數 🫀90↑ 🛡️57↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐92↑，最低仍是免疫 57 黃燈（review_coverage 缺口，self-evolve-weekly 名下）。parallel-check 回報 ACTOR_BUSY，babel dispatcher 四個進程在寫，index 裡有它 staged 的 56 份譯文。

## 前一夜的缺席

09-26 沒有 embeddings 的 memory 也沒有 commit。追到 `2026-09-26-100333-babel-vortex.md`：Claude Desktop 登入 09-25 23:17 過期，比 #1761 預估的 09-27 早兩天，七條 routine 起不來直到哲宇 09-26 10:02 重新登入。原因已知、只缺一夜，未達「連 3 天 skip」的 escalate 線。09-25 那班寫的「09-28 若無 commit 先查登入」猜對了方向，只是日期早了兩天。

## Rebuild、verify、commit

§前置先問本機，`127.0.0.1:11434` 有 bge-m3，Stage 0 回 `dim 1024`。本機落後 12、領先 0，先用 `git merge-tree` 與 dirty 檔清單比對 12 個進來的檔案，零重疊，`git merge --ff-only` 快轉。`build-embeddings.mjs --langs all` 05:14 起跑、06:02 結束，每語 203〜229 秒，13 語全數 0 fail，共 14,469 向量，較 09-25 的 14,032 多 437。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，13 語全部 1,113 篇、100% 有 8 鄰居，manifest `bge-m3:latest`／`rag-v1`，exit=0，PASS。兩天前最少的 de 只有 993 篇，今晚追平：這是十三語第一次在語意索引裡篇數完全一致，babel-vortex「翻譯率 100%」那兩天的產量在這裡被看見。`zh-TW.json` 也有 diff（原稿側本週有改動）。

index 裡躺著 dispatcher 的 56 份 staged 譯文，照 pipeline 字面 `git add` 再 commit 會把它們一起捲進本班 commit，所以改用 `git commit -- src/data/related/` 只提交這 13 檔，dispatcher 的 staged 內容原樣留給它自己。`$NOW` 先印出 `2026-09-27 06:02` 再代入，co-author 如實填 Claude Opus 5.5，commit `5267a8746` 正好 13 個 related 檔。push 前 fetch 領先 1 落後 0，pre-push 三道語言閘門全綠，in-flight run 1318 秒依 latest-wins 放行，`375c35f70..5267a8746`，push 後 0/0。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ⚠️（rebuild／commit／push 精確，session 起點無落檔時戳） |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班未觸發 refresh，06:00 data-refresh 會接）        |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                              |

## Handoff 三態

繼承自 `2026-09-25-060129-twmd-embeddings-nightly.md`：

- [x] ~~pending（09-28 若無 embeddings commit，先查 #1761 登入）~~ — retired by 本 session：登入其實 09-25 23:17 就過期、09-26 10:02 已續，今晚 commit `5267a8746` 正常。
- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）— routine-sync 提的「embeddings 改殼後隔兩晚才生效」三選項。本班沒改殼。
- ⏳ blocked（延續，哲宇）— OBSERVER-QUEUE #75〜#84 等紅線或需拍板項，本班不動。
- [ ] pending（延續，babel 專屬，收件席位 babel-nightly／babel-vortex）— 明細在 `2026-09-27-010249-twmd-babel-nightly.md`，不重抄（REFLEXES #74）。

本 session 新 handoff：

- [ ] pending（收件席位：`/twmd-routine` 或 self-evolve-weekly，動得了 pipeline 文件）— EMBEDDING-PIPELINE Stage 3 寫的是 `git add src/data/related/` 後 commit，在營運機 index 裡常有 dispatcher staged 譯文時，照字面跑會把別人的 staged 檔捲進 routine commit。本班改用 `git commit -- src/data/related/`，建議把 Stage 3 改成 pathspec commit 或先驗 `git diff --cached --name-only` 只含 related。參照：`scripts/tools/lib/verify-commit-scope.sh`（09-27 `9842dc4e6` 處理的是 pathspec 收官留下的舊索引，同一個 index 共用問題的另一側）。

## Beat 5 — 反芻

今晚最值得記的數字是 13 語全部 1,113。語意索引只算站上存在的文章，所以篇數齊平就是巴別塔在「站上可檢索」這一層封頂的證據，比翻譯狀態表多一道來源。另一件是 Stage 3 的字面指令跟營運機實況對不上：pipeline 寫的時候假設 index 只有本班的東西，現在 dispatcher 常駐，這個前提已經不成立，今晚靠當班看了一眼 `git diff --cached` 才沒出事，這種靠當班警覺的修法會隨熟悉度變鬆（REFLEXES #95），所以留成 handoff 給能改文件的席位。不寫日記（routine 預設 skip，本班沒有理解上的轉折）。

🧬

---

_v1.0 | 2026-09-27 06:03 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,469 向量 0 fail，commit `5267a8746`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行；09-26 因登入過期缺一夜_
_核心洞察：(1) 13 語篇數首次齊平 1,113，de 兩天內 993→1,113 (2) 營運機 index 常有 dispatcher staged 檔，Stage 3 字面 `git add` 會捲入別人的變更，改用 pathspec commit (3) 登入過期比預估早兩天，前夜的缺席有解釋_
_LESSONS-INBOX：無新增（Stage 3 缺口以 handoff 交給可改 pipeline 的席位）_
