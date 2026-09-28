# 2026-09-29-055718-twmd-embeddings-nightly — 13 語 14,469 向量 0 fail，373 篇換鄰居；pipeline Stage 3 改成路徑式 commit

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: ~05:05 → 05:58 +0800（~53 分鐘，2 commits）
> 資料來源：`git log %ai` + rebuild 起跑後印的 `date`（05:14:57）+ 結束 `date`（05:56:31）；session 起點無落檔時戳

## 觸發

夜間 05:00 排程窗自動觸發，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) 重建全站 bge-m3 語意索引。BECOME micro 讀完 wake-context 273,117 bytes 到 `wake:END`，selftest 全綠，工作樹與 origin/main 同步。器官讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐92↑，最低是免疫 59 黃燈（review_coverage 缺口，self-evolve-weekly 名下），snapshot 齡 23 小時。parallel-check 回報 ACTOR_BUSY，babel dispatcher 三個進程在寫，工作樹只有它的 `_translation-status.json` 與 progress log，index 空。

## Rebuild、verify、commit

§前置先問本機，`127.0.0.1:11434` 有 bge-m3，Stage 0 回 `dim 1024`，EMBED_HOST 解析為本機，沒動到 fleet 備援。本機與 origin 0／0。`build-embeddings.mjs --langs all` 05:14 起跑、05:56 結束，每語 185〜197 秒，跟昨晚同一個速度帶，13 語全數 0 fail，共 14,469 向量（每語 1,113）。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，13 語全部 1,113 篇、100% 有 8 鄰居，manifest `bge-m3:latest`／`rag-v1`，exit=0，PASS。`src/data/related/` 有 9 檔 diff，zh-TW、en、ar、ru 沒動。照昨晚的做法逐語比對鄰居清單，共 373 篇換了鄰居：vi 202、pt 56、es 53、hi 48、fr 5、id 3、ko 3、ja 2、de 1。vi 佔一半多，對得上 09-28 babel-vortex 第三十一到四十輪那批 vi 整篇重譯（名人頂替、「中華台北」頂替地名的幾十篇）；pt、es、hi 也各有同批重譯。zh 原稿沒改，變的全是譯文。

索引 commit `41cf6fcff` 用路徑式提交，正好 9 個 related 檔，`$NOW` 先印出 `2026-09-29 05:56` 再代入，co-author 如實填 Claude Opus 5.5。

## Stage 3 文件本身改掉

09-27、09-28 兩班的交接都寫著同一件事：pipeline Stage 3 的字面指令是先 `git add src/data/related/` 再不帶路徑 commit，還用 `git diff --cached --quiet` 判斷有沒有變動，營運機 index 常有 dispatcher 暫存的譯文，照字面跑會把別人的檔捲進來，也會把「別人有暫存」讀成「索引有變」。兩班都靠路徑式 commit 繞過，文件沒改。這次把文件改了（`ed71dd072`，EMBEDDING-PIPELINE v1.4）：變動判斷只看 `src/data/related/`，commit 帶 `-- src/data/related/`，commit 後用 `git show --stat` 驗證只含這一格。本班的索引 commit 就是照新版指令跑的，第一次使用即驗證通過。交接指名的收件席位是 `/twmd-routine` 或 self-evolve-weekly，實際上這是一個檔案、一段指令的修改，本班動得了，所以直接做掉。

push 時 pre-push 判斷 in-flight deploy 還早，直接推，`f72368020..ed71dd072`，push 後 0／0。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ⚠️（rebuild／commit／push 精確，session 起點無落檔時戳） |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班未觸發 refresh，06:00 data-refresh 會接）        |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                              |

## Handoff 三態

繼承自 `2026-09-28-055906-twmd-embeddings-nightly.md`：

- [x] ~~pending（收件席位 `/twmd-routine` 或 self-evolve-weekly）— EMBEDDING-PIPELINE Stage 3 仍寫 `git add` 後不帶路徑 commit~~ — retired by 本班 `ed71dd072`（v1.4）
- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）— routine-sync 提的「embeddings 改殼後隔兩晚才生效」三選項。本班沒改殼。
- ⏳ blocked（延續，哲宇）— OBSERVER-QUEUE #75〜#90 等紅線或需拍板項（待決），本班不動。
- [ ] pending（延續，babel 專屬，收件席位 babel-nightly／babel-vortex）— 明細在 `2026-09-29-005057-twmd-babel-nightly.md`（#89 待決、自造 slug 存量 813 條），不重抄（REFLEXES #74）。

本 session 新 handoff：無。

## Beat 5 — 反芻

那條 Stage 3 的交接傳了兩班，每一班都讀到、都照做繞過，也都把它原樣交給一個「動得了 `docs/pipelines/`」的席位。其實當班就動得了：這是 routine 自己的 pipeline，一段指令，不碰門檻也不碰殼。交接把它寫成別人的事，讀的人就照著當成別人的事。這是 REFLEXES #97「收件席位要問動不動得了」的反面：席位寫錯的方向也可能是把自己能做的推出去。這裡記一筆，不另開 LESSONS。不寫日記（routine 預設 skip）。

🧬

---

_v1.0 | 2026-09-29 05:58 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,469 向量 0 fail，commit `41cf6fcff`＋pipeline v1.4 `ed71dd072`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) 373 篇換鄰居，vi 佔 202，全是 09-28 babel-vortex 重譯的腳印 (2) 傳了兩班的 Stage 3 交接其實當班動得了，直接改文件_
_LESSONS-INBOX：無新增_
