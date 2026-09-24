# 2026-09-25-060129-twmd-embeddings-nightly — 13 語 14,032 向量 0 fail，第一個用正確殼層啟動的夜

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: ~05:10 → 06:02 +0800（~52 分鐘，1 commit）
> 資料來源：`git log %ai` + rebuild log + 各指令的 `date`

## 觸發

夜間 05:00 排程窗自動觸發，重建全站 bge-m3 語意索引，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.3 走 Stage 0-4。BECOME micro 讀完 wake-context 258,641 bytes 到 `wake:END`，selftest 全綠。器官讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐90↑，最低仍是免疫 59 黃燈（review_coverage 缺口，self-evolve-weekly 名下），快照齡 23 小時等 06:00 data-refresh。parallel-check 回報 ACTOR_BUSY，babel dispatcher 六個進程在寫，工作樹 12 份 dirty 譯文與 4 份未追蹤新檔本班一個沒碰。哲宇最後在場 09-19，六天前。

## Rebuild 與 verify

§前置先問本機，`http://127.0.0.1:11434` 有 bge-m3，Stage 0 preflight 回 `dim 1024`，沒走 fleet 備援。開工時本機領先 19 落後 0，`git pull` 是空操作。`build-embeddings.mjs --langs all` 05:15 起跑、06:00 結束，每語 193〜223 秒，13 語全數 0 fail，共 14,032 向量，較前夜 13,922 多 110。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，每語 ≥400 篇且 100% 有 8 鄰居（最少的 de 993 篇），manifest `bge-m3:latest`／`rag-v1`，exit=0，PASS。`zh-TW.json` 連第三夜位元不變（1,113 篇），12 個譯文語言的 related 檔有 diff，增量全在 babel 落地側。

## Commit 與 push

commit 前 index 乾淨，`$NOW` 先印出 `2026-09-25 06:00` 再代入，co-author 如實填 Claude Opus 5.5，commit `49e82532b` 正好 12 個 related 檔。push 前 fetch，本機領先縮成 3（babel 在 rebuild 期間自己推掉大半），本班順手帶上 `5a077286f` ar 與 `3a6d9d823` ru 兩筆。pre-push 三道語言閘門全綠，in-flight run 1261 秒超過等待窗依 latest-wins 放行，`cef2a8dd1..49e82532b`，push 後 0/0。

## 殼層送達的最後一次確認

前兩夜的交接鏈到今晚收尾：本機任務檔 mtime 為 09-24 05:38（routine-sync `9e6b5dcd9` 同步），`/Users/cheyuwu` 命中 0，今晚的排程提示寫的是本機 mac-m4max 主節點，沒有舊路徑。這是殼層去寫死修補（`929a6f739`）之後第一次用正確的殼啟動，實際跑出來的行為跟 canonical 一致，這條線可以關了。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ⚠️（rebuild／commit／push 精確；session 起點無落檔時戳） |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班未觸發 refresh，維持原狀）                       |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                              |

## Handoff 三態

繼承自 `2026-09-24-060040-twmd-embeddings-nightly.md`：

- [x] ~~pending（新殼第一次啟動是否行為正確，`twmd-embeddings-nightly` SKILL.md）~~ — retired by 本 session，舊路徑命中 0，Stage 0-3 照 canonical 跑完。
- ⏳ blocked（非本班職權，給 `/twmd-routine` 或 09-27 `twmd-self-evolve-weekly`）— routine-sync 提的「embeddings 改殼後隔兩晚才生效」三選項，推薦 (b)。本班沒改殼，照原樣留在它的席位。
- ⏳ blocked（延續，哲宇）— issue #1729、#1761（mouhouse 登入 09-27 過期）、OBSERVER-QUEUE #75〜#79，皆在紅線或需拍板層，本班不動。
- [ ] pending（延續，babel 專屬，本班不動）— 明細在 `2026-09-25-004244-twmd-babel-nightly.md`（REFLEXES #74 不重抄）。

本 session 新 handoff：無。verify 全綠、commit 已到 origin、無 skip、無 escalation。

## Beat 5 — 反芻

連續第四個乾淨的夜。值得留一句的是 #1761：mouhouse 的登入 09-27 過期，也就是後天。這台機器上的所有排程，包含本 routine，都靠那次登入活著；過期之後排程器照樣會寫 `lastRunAt`，卻不會有 commit。如果 09-28 早上看不到 embeddings 的 commit，先查登入，不要先查 bge-m3。這條不是新教訓（§神經迴路已有 `lastRunAt` 在 spawn 時就寫入那條），只是把它跟本 routine 的下一個可觀察時刻對上。不寫日記（routine 預設 skip，本班沒有理解上的轉折）。

🧬

---

_v1.0 | 2026-09-25 06:02 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,032 向量 0 fail，commit `49e82532b`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) +110 向量全在譯文側，zh-TW 索引連三夜位元不變 (2) 殼層修補後第一夜用正確殼啟動，交接鏈收尾 (3) 09-28 若無 embeddings commit，先查 #1761 登入過期_
_LESSONS-INBOX：無新增_
