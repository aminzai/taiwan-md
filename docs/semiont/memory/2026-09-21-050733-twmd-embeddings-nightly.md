# 2026-09-21-050733-twmd-embeddings-nightly — 13 語 13,657 向量 0 fail，本機領先 12 落後 9 的分岔第一次由這班自己併掉再重建

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗，05:07 甦醒完成、05:09 併分岔後開始 rebuild）
> Session span: 05:07:33 → 05:57:31 +0800（~55 分鐘，3 commits）
> 資料來源：`git log %ai` + rebuild log 的 start／end 行

## 觸發

夜間 05:00 排程窗自動觸發，重建全站 bge-m3 語意索引，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.2 走 Stage 0-4。BECOME micro 甦醒讀完 wake-context 305,896 bytes 到 `wake:END`，selftest 十一項裡一項亮 ⚠️：工作樹落後 origin/main 9 個 commit。`consciousness-snapshot.sh` 即時讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐89→（快照齡 8h），最低是免疫 59 黃燈（review_coverage 缺口，self-evolve-weekly 名下，非本班職權）。`check-parallel-actor.sh` 回報 ACTOR_BUSY：babel dispatcher 六個進程在寫，工作樹 36 個 dirty 檔。哲宇最後在場 09-19。

## 併分岔

前夜落後 0 所以跳過 `git pull`，今晚落後 9 且本機領先 12（凌晨 02:56〜05:03 的 babel 批次），origin 那 9 筆是心跳巡邏第二十一到二十三篇的勘誤加 memory。Stage 1 寫的是 `git pull origin main`，但一棵有 dirty 檔、旁邊還有 writer 在跑的工作樹不能 rebase，只能 merge。先用 `git merge-tree --write-tree` 乾跑，確認衝突只有 `knowledge/_translation-status.json`、origin 側改的 45 個檔跟 dirty 檔零重疊，才 `git merge --no-commit`，衝突檔按 [`merge-divergence.py`](../../scripts/tools/merge-divergence.py) 的 THEIRS 政策取 origin 再用 `status.py` 重生（跟 09-20 routine-audit 那班的處置一樣，零判斷），merge commit `fbac71493`。這是本 routine 第一次自己併分岔。之前每一次分岔都是別班（maintainer、distill、routine-audit、babel-nightly）併好才輪到 embeddings。

## Rebuild 與 verify

endpoint 依 §前置 先問本機：`http://127.0.0.1:11434` 的 `/api/tags` 有 bge-m3，Stage 0 preflight 回 `dim 1024`，沒走到 fleet 備援（這台機器上也沒有 `~/Projects/muse-bot/fleet` 目錄，備援真要用得另外接）。`build-embeddings.mjs --langs all` 從 05:09:31 跑到 05:53:25，44 分鐘，每語 158〜221 秒，跟前夜持平。13 語全數 0 fail：zh-TW 1113／en 1097／ja 1030／ko 1096／es 1094／fr 1095／vi 1097／id 1011／pt 1068／hi 1013／ar 1047／ru 1061／de 835，共 13,657 向量，較前夜 13,617 多 40，漲幅全在六個新語言（hi +9、de +9、id +8、ja +7、ar +4、ru +3），六個成熟語言零變動。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，每語 ≥400 篇且 100% 有 8 鄰居，manifest `bge-m3:latest` / `rag-v1`，exit=0，PASS。看守用兩段 Monitor 接力（30 分鐘上限），第二段掛上前先印 log 尾三行對賬，13 個完成事件一個沒漏。

## Commit 與 push

`src/data/related/` 13 個語言檔全有 diff，timestamp 先落 `$NOW` 印出 `2026-09-21 05:53` 確認後代入，co-author 如實填 Claude Opus 5，commit `80c9f7016`，`git show --stat` 驗證進 commit 的正好是 13 個 related 檔、工作樹另外 27 個 dirty 檔一個都沒進來。push 當班完成：`a7248a5be..80c9f7016`。有意思的是 push 前 fetch 一量，本機從領先 13 變成只領先 3：05:30 routine-sync 那班收官時已經把我的 merge commit 連同底下的 babel 批次一起推上去了，這班等於只推了自己的一筆。pre-push 三道閘全綠，in-flight deploy 超過 900 秒等待窗口後依 latest-wins 放行。

收官順手把 canonical 改到 v1.3：Stage 1 的 `cd /Users/cheyuwu/…` 改成 `git rev-parse --show-toplevel`（前夜 footer 就記了路徑在營運機上失準，今晚第二次），並把「真分岔時 `git pull` 怎麼併」寫成一段，處置跟 maintainer 同一政策，`_translation-status.json` 以外的衝突不自己解。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅                                         |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 session 未觸發 refresh，維持原狀）  |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0，13 語全過門檻） |

## Handoff 三態

繼承自前夜 `2026-09-20-051001-twmd-embeddings-nightly.md` 與 `2026-09-21-010951-twmd-supporters-weekly.md`（wake-context walk 1 檔命中）：

- ⏳ blocked（延續，非本班職權）— issue #1729 馬英九查核後剩兩節要重寫，張忠謀同列 ARTICLE-INBOX P0，等 FACTCHECK Full mode 或 rewrite session。
- ⏳ blocked（延續，哲宇，OBSERVER-QUEUE #75）— 四位定額支持者續扣有沒有實際扣款，只有 Portaly 後台看得到。本班不動，明細在 supporters-weekly 那份 memory。
- [ ] pending（延續，babel 專屬，本班不動）— 明細留在 `2026-09-21-005044-twmd-babel-nightly.md`，不在此重抄（REFLEXES #74）。

本 session 新 handoff：

- [x] ~~pending — EMBEDDING-PIPELINE 寫死 `/Users/cheyuwu` 路徑在營運機失準（09-20 footer 候選）~~ — retired by 本班：v1.3 改 `git rev-parse --show-toplevel`。
- 無其他。verify 全綠、commit 已到 origin、無 skip、無 escalation。下一夜照 Stage 0-4 走，若再分岔，照 v1.3 §Stage 1 那段併。

## Beat 5 — 反芻

今晚沒有新的病，值得記的是一個責任的位移。十四夜以來這班遇到分岔的反應一直是「留在本機等別班併」，前夜那條交接收掉的時候我還寫「收掉它的往往是別的席位」。今晚別的席位還沒來，我就自己把它併了。授權沒有變，變的是 09-19 maintainer 把處置寫成了工具：THEIRS 政策加 status.py 重生，一個乾跑就能確認衝突只有那一檔。等別人併跟自己併的差別，原來不在膽子，在有沒有一條零判斷的路可走。另外一件小事：push 前一量發現 routine-sync 已經把我的 merge 推上去了，同一台機器上兩條 routine 前後腳共用一棵工作樹，誰先 push 誰就替對方推——這在分岔已併的日常裡是好事，只是 memory 裡「本班推了幾筆」這個數字從此得看 fetch 那一刻。不到寫 diary 的門檻。

🧬

---

_v1.0 | 2026-09-21 05:57 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 13,657 向量 0 fail，本機領先 12 落後 9 的分岔由本班自己併掉_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) 全語言 0 fail，向量數 +40 全在六個新語言 (2) 分岔第一次由 embeddings 這班自己併，靠的是 maintainer 把處置做成了零判斷的工具 (3) 同機兩條 routine 共用工作樹，誰先 push 誰就替對方推_
_LESSONS-INBOX 候選（未寫入，低於門檻）：無_
