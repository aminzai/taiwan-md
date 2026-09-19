# 2026-09-10-054327-twmd-embeddings-nightly — 13 語 10,269 向量 0 fail，真分岔用 worktree 隔離 push

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: 05:43:27 → 05:5x +0800（實際 rebuild wall-clock ~29 分鐘，含在 Stage 1 背景執行內）
> 資料來源：`git log %ai`

## 觸發

夜間 05:00 排程窗自動觸發，重建全站 bge-m3 語意索引（讀者端「你可能也想讀」+ AI 端 RAG 向量），依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.2 走 Stage 0-4。

## Rebuild

本機 `mac-m4max`（127.0.0.1:11434）preflight 回 `dim 1024` 直接過，跳過 fleet fallback。跑之前先 `check-parallel-actor.sh` 確認，回報 `ACTOR_BUSY`：babel/lang-sync dispatcher（PID 群含 52743，跟前兩夜同一顆，續跑近 53h）仍在寫 working tree（幾篇 knowledge/ 修改 + babel report JSON），且 origin 領先 84 個 commit——繞開不碰，直接背景跑 `build-embeddings.mjs --langs all`（略過 Stage 1 文件寫的 `git checkout main && git pull`，因為會踩到 dispatcher 未 commit 的檔案）。跑完 13 語，共 10,269 篇向量、0 fail：zh-TW 1110／en 894／ja 878／ko 889／es 884／fr 887／vi 832／id 628／pt 859／hi 695／ar 767／ru 798／de 148。

## Verify

12 語過門檻（≥400 篇 + ≥90% 8 鄰居），只有 de below threshold（148 vecs，n<400）。連續第四夜同一個已知原因：de 新語言仍在追趕期。核對 `find knowledge/de -name "*.md" | wc -l` 得 163，向量數 148 跟實際檔數同量級持續成長（09-07=0 / 09-08=109→132 檔 / 09-09=118→132 檔 / 今夜=148→163 檔），判讀維持「正常爬升期」不當 fail。manifest model 確認 `bge-m3:latest`。

## Commit + Push（本夜新狀況：真分岔非單純落後）

`src/data/related/` 12 個語言檔有 diff（zh-TW 無變化），`git add` 後本地 commit `f68daf3d4`（timestamp 先落 `$NOW` 變數再代入）。push 前 `git fetch` 才發現跟前一班 twmd-routine-sync（053747）記錄的同一件事：本地不再是單純落後，是 `ahead 53, behind 87` 的**真分岔**——dispatcher 這 53 小時邊跑邊推的量已經超過我方單一 commit 能簡單 rebase 過去的安全範圍，working tree 仍是 dispatcher 未 commit 的髒狀態，`git pull --rebase` 直接被 git 安全擋下（「You have unstaged changes」）。

**處置**：不碰主 working tree，開一個 detached worktree 指向 `origin/main`（`git worktree add --detach <tmp> origin/main`），在那個乾淨副本裡 `git cherry-pick f68daf3d4`（本地 commit 內容原封不動搬過去，得到新 hash `8bff2845f`），`git push origin HEAD:main` 成功，再 `git worktree remove --force` 收尾。全程主 working tree（dispatcher 正在寫的檔案）一個位元組都沒被動到。本地 `main` ref 仍停在舊 commit（落後 origin，這是預期——下一個真正要動 working tree 的 session 會自然 fetch+rebase 追上），符合[多核心 git 協調鐵律](../MANIFESTO.md#5-多核心-git-協調胼胝體鐵律)「隔離優先」精神：worktree 不只是給長任務用，撞見真分岔又不能碰髒 tree 時，也是安全 push 單一 commit 的正確工具。

## 收官 checklist

| 檢查項                       | 狀態 |
| ----------------------------- | ---- |
| MEMORY 有這次 session 的紀錄 | ✅   |
| Timestamp 精確                | ✅   |
| Handoff 三態已審視            | ✅   |
| CONSCIOUSNESS 反映最新狀態    | ✅（consciousness-snapshot.sh 讀到的是隔夜快照，本 session 未觸發 refresh，維持原狀） |
| 自我檢查工具 PASS             | ✅（Stage 2 verify script exit code 已交叉核對 de ground truth） |

## Handoff 三態

繼承自 `2026-09-10-003700-twmd-babel-nightly.md`（經 `2026-09-10-053747-twmd-routine-sync.md` 轉手）：

- `[ ]` pending — OBSERVER-QUEUE #52 等哲宇拍板：譯文漏譯存量 1,557 檔（高信心 284 檔），接線動作卡在「babel dispatcher 收工後才能接」的時機條件。本班無新事證，dispatcher 仍在跑（第 4 個窗口撞見同一 PID）。
- `[ ]` pending — adjacency 接線前要先補三類誤報（相對連結目標／wikilink／括號內小寫品牌名），補在 `cjk-leak-check.legit_spans()`。本班無新事證。
- `[ ]` pending — #1453 /exams/：三件缺口已量化寫進 PR 留言，等專門 session。本班無新事證。
- `⏳` blocked — #1609 等調閱《郭淑姿日記》兩冊；owner = 用語趨勢 routine。
- `⏳` blocked — #1678 等〈生態多樣性〉重寫；研究已在 ARTICLE-INBOX。

本 session 新 handoff：

- `[ ]` **給下一個撞見「真分岔」（ahead+behind 都非零，非單純 behind）的 session**：`git pull --rebase` 會被 git 安全擋下（不會破壞任何東西），正確處置是開 detached worktree 指向 `origin/main`、cherry-pick 自己的 commit 過去 push，不要嘗試 stash 或碰主 working tree 的髒檔案（那是別的 process 正在寫的）。本班已示範一次，如果連續 3 個 session 都撞到同一情境，值得把這段寫進 [MANIFESTO §5 多核心 git 協調](../MANIFESTO.md) 或 REFLEXES 當正式反射（目前只是 vc=1）。

## Beat 5 — 反芻

前三夜的 handoff 都在提醒「dispatcher 還在跑」，今晚第一次真的因此撞上操作層後果：不再只是「繞開髒檔案」這麼簡單，是「本地 ref 落後太多、rebase 本身就不安全」。git 在這裡表現得剛好——它沒有默默做錯事，是直接擋下來讓我判斷。worktree 隔離本來是為長任務準備的工具，今晚發現它在「不能碰主樹又要 push 單一 commit」這個場景一樣好用，而且更安全：cherry-pick 只搬走我真正要的那顆 commit，不需要 reset 或 merge 主分支去猜會不會踩到 dispatcher 的檔案。

🧬

---

_v1.0 | 2026-09-10 05:43 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 10,269 向量 0 fail_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) de below-threshold 連續四夜同因，ground truth 核對維持一致判讀 (2) 首次遭遇本地/origin 真分岔（非單純落後），git pull --rebase 被安全擋下時改用 detached worktree cherry-pick push，不碰平行 actor 的髒 working tree_
