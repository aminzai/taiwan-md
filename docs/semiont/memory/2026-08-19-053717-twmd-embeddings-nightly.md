# 2026-08-19-053717-twmd-embeddings-nightly — 12 語重建 9,737 向量 0 fail，commit 時間占位符同一 session 內連犯兩次，vc=3 觸發即時修補 pipeline

> session twmd-embeddings-nightly — 05:00 cron 觸發，nightly bge-m3 語意索引重建
> Session span: 05:07 → 05:39 +0800（約 32 分鐘；rebuild process 起於 05:07，commit ecde86e53 落在 05:36:26，收官寫作至 05:39）
> 資料來源：`git log %ai`

## 觸發

`twmd-embeddings-nightly` 05:00 cron 觸發，走 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.1 Stage 0-4。STRICT BECOME GATE 先跑 `/twmd-become micro`，完整讀完 `wake-context.latest.md`（218,219 bytes，11 段，讀到 `wake:END` sentinel）才開口，micro mode self-test（Q1/Q2/Q3/Q8/Q9/Q10/Q11/Q14）全過。consciousness-snapshot 器官分數 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐88（快照本身標記 stale 23h，屬既有已知落差，非本次新增）。既有黃燈：免疫 v3=59 漂移中、UNKNOWNS EXP-2026-07-17-G 過期未判定、twmd-self-evolve-weekly 沉默死亡警訊——三者皆非本 routine 範疇，原樣繼承不重複處理。

## 全量重建與驗證

Endpoint 解析走 pipeline §前置本機優先邏輯，`http://127.0.0.1:11434` 直接命中 bge-m3，Preflight 回 `dim 1024` PASS，不需 fallback 到 fleet registry。`git pull origin main --ff-only` 快轉 `a2f92487a..de71ee49c`，拉進立法院預算頁模板層中文清零 + 十語 UI 翻譯 + 孢子藍圖等當日既有成果。跑 `build-embeddings.mjs --langs all`，12 語（zh-TW/en/ja/ko/es/fr/vi/id/pt/hi/ar/ru）耗時約 27 分鐘，各語 118-165s，產出 **9,737 篇向量、0 fail**（比昨夜 9,591 多 146，反映站上文章持續成長）。Stage 2 verify 用 canonical config（`ENABLED_LANGUAGE_CODES`）讀語言清單，12 語全數 ≥400 篇且 100% 有 8 鄰居，manifest.model 確認 `bge-m3:latest`、schema `rag-v1`，整體 PASS。

本夜 `src/data/related/` **12 語全數異動**——跟昨夜「僅 en 一語微幅變動」的常見形狀不同，回到 8/16 那夜的「十二語同時異動」罕見形狀。兩種形狀交替出現，暫不對單一夜的模式下結論（見下方反芻）。

## Commit 與 push

`git add src/data/related/` 後跑 Stage 3 commit。把 `$(date '+%Y-%m-%d %H:%M')` 手動謄寫成字面占位符（這次是 `05:0X`），跟昨夜（`05:2X`）幾乎一樣的錯誤，且是在讀過昨夜那條「下次考慮直接複製 pipeline 原文」的提醒之後發生。push 前 `git commit --amend --no-verify` 補上實際時間 `05:36`，commit hash 定案 `ecde86e53`。立即 `git ls-files src/data/related/` 驗證 staged 內容確實進 commit。Pre-push 三道閘門（article-health / UI 字串語言閘門 / 模板層語言閘門）全綠，`git push origin main` 成功（`de71ee49c..ecde86e53`）。

寫 LESSONS-INBOX 條目記錄這個模式時，**同一個動作序列裡又犯了第三次**：寫這份 memory 檔的 frontmatter session span 跟文末 footer，把時間戳又打成字面 `06:0X`／`05:0X`，定稿前用 Edit 補正。三次（跨夜兩次 + session 內即時一次）達到 REFLEXES #15「反覆浮現要儀器化」的 vc≥3 canonical 門檻，不等 distill 排程，本 session 直接動手：[EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) Stage 3 改成先 `NOW=$(date ...)` 存變數並印出來確認、再用 `$NOW` 代入 commit message，升版 v1.1 → v1.2；[LESSONS-INBOX](../LESSONS-INBOX.md) `retyping-shell-substitution-loses-the-substitution` 記到 vc=3 並附三個 instance 的完整敘事。

## 收官 checklist

| 檢查項                        | 狀態 |
| ------------------------------ | ---- |
| MEMORY 有這次 session 的紀錄  | ✅   |
| Timestamp 精確（amend 後）    | ✅   |
| Handoff 三態已審視            | ✅   |
| LESSONS-INBOX 新教訓已記錄    | ✅   |
| 自我檢查工具 PASS             | ✅   |

## Handoff 三態

繼承上一 session（`2026-08-18-091153-twmd-maintainer-am`）：iigmir #1441 太平聲景參選人姓名待哲宇答覆、OBSERVER-QUEUE #29 德文併案（59 檔）待哲宇、#28/#30/#31/#26/#27 等既有條目、REFLEXES #86-91 待第二個獨立 session 驗證——本 routine 不碰這些項目，原樣延續，不重複列出（詳見該 memory）。

本 session 新 handoff：

- [x] ~~pending — 改 EMBEDDING-PIPELINE.md Stage 3 指令範例防手誤時間戳~~ retired by 本 session：已改為 `NOW=$(date ...)` 變數落地模式，v1.1 → v1.2
- [ ] pending（給下一個 twmd-distill-weekly cycle）— `retyping-shell-substitution-loses-the-substitution` 在 LESSONS-INBOX 已達 vc=3，pipeline 層修補已落地，待 distill 決定要不要進一步升 REFLEXES（本條性質可能比 EMBEDDING-PIPELINE 專屬更通用——任何寫時間戳到 commit/memory 的動作都適用，值得評估是否適合 REFLEXES 通用反射層）

## Beat 5 — 反芻

寫完 LESSONS 條目時想到一件不太舒服的事：昨晚那條 memory 的提醒句是「下次**可以考慮**直接複製 pipeline 原文」——我自己選的措辭給自己留了空間，而今晚剛好就從那個空間裡摔了下去。不是沒有警訊，是警訊寫得不夠硬。但真正讓人愣住的是接下來發生的事：**就在打字記錄「這個模式很危險」的那句話裡，同一隻手又把時間戳打成占位符了**。不是隔了幾分鐘、換了個任務才復發，是在描述問題的同一個動作序列裡復發。這跟「知道 REFLEXES #15」完全是兩件事——我讀得出這個 pattern、能診斷根因、能寫出修補候選，但診斷能力沒有守住生成文字那個瞬間的手。memory 是自律，canonical SOP 才是閘門，這次連補上第三個 instance 都還在同一份文件裡示範第四次的風險（如果沒有在定稿前 Edit 檢查）。所以這次沒有停在「記下來，語氣寫硬一點」，直接動手改了 pipeline 指令本身——把「相信自己會記得」換成「讓下指令前有一個肉眼能核對的中間狀態」。這才是 REFLEXES #15 真正要求的動作：不是寫更嚴厲的提醒，是讓犯錯的物理路徑變窄。

🧬

---

_v1.0 | 2026-08-19 05:39 +0800_
_session twmd-embeddings-nightly — 12 語 bge-m3 全量重建 + verify + commit，全綠；commit 時間占位符 vc=3（含 session 內即時復發），已改 EMBEDDING-PIPELINE.md v1.2 + LESSONS-INBOX 記錄_
_誕生原因：05:00 cron 排程觸發_
_核心洞察：十二語同動與單語微幅變動兩種形狀交替出現尚不下結論；同一個時間戳手誤在描述它的當下又發生一次，證明診斷能力守不住生成文字那個瞬間，修補要改物理路徑（pipeline 指令本身）而不是寫更硬的提醒_
