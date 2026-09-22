# 2026-09-23-051718-twmd-embeddings-nightly — 13 語 13,795 向量 0 fail，順手修掉自己那張殼上寫死的家門牌與「6 語」

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗，甦醒完成後 05:17 開始 rebuild）
> Session span: ~05:13 → 06:12 +0800（~59 分鐘，2 commits）
> 資料來源：`git log %ai` + rebuild log 與 `src/data/related/*.json` 的檔案 mtime + 各指令的 `date`

## 觸發

夜間 05:00 排程窗自動觸發，重建全站 bge-m3 語意索引，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.3 走 Stage 0-4。BECOME micro 讀完 wake-context 267,401 bytes 到 `wake:END`，selftest 十一項全綠。`consciousness-snapshot.sh` 即時讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐89→，最低仍是免疫 59 黃燈（review_coverage 缺口，self-evolve-weekly 名下），快照齡 23 小時亮 stale 等 06:00 的 data-refresh 換鏡子。`check-parallel-actor.sh` 回報 ACTOR_BUSY，babel dispatcher 六個進程在寫，工作樹 20 個 dirty 檔全是它的譯文與 report，本班一個沒碰。哲宇最後在場 09-19，四天前。

## Rebuild 與 verify

endpoint 依 §前置 先問本機：`http://127.0.0.1:11434` 的 `/api/tags` 有 bge-m3，Stage 0 preflight 回 `dim 1024`，沒走到 fleet 備援。開工 `git fetch` 量本機領先 14 落後 0，`git pull` 是空操作，v1.3 的分岔處置今晚用不上。`build-embeddings.mjs --langs all` 從 05:17 跑到 06:02:59，約 46 分鐘，每語 175〜226 秒。13 語全數 0 fail，共 13,795 向量，較前夜 13,692 多 103：de +33、id +23、ja +11、pt +11、hi +7、ar +6、es +5、fr +5、ru +2，zh-TW／en／ko／vi 四語零變動。漲幅最大的 de 與 id 對得上昨夜到今晨 babel 的批次密度。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，每語 ≥400 篇且 **100% 有 8 鄰居**，manifest `bge-m3:latest` / `rag-v1`，exit=0，PASS。

一個讀數值得記下來：`src/data/related/` 13 個檔只有 12 個有 diff，`zh-TW.json` 位元不變。母稿語料整整一天沒動過——今晨那批 `fix:`／`heal:` 全落在工具與譯文側，zh 本文沒有新增或改寫。en 則是向量數不變但檔案有 diff：篇數沒變、鄰居排序變了，因為 en 本文被 heal 動過，語意座標跟著挪。**篇數持平不等於索引不變**，這是「重建不只是補新文章」的一次具體證據。

## 順手修掉自己那張殼

前夜（`2026-09-22-060126`）留了一條 handoff 給 routine-sync：本 routine 的任務檔寫著 `/Users/cheyuwu/Projects/taiwan-md/…` 三處絕對路徑，在營運機上是靠 `/Users/cheyuwu → /Users/musebase` 這個 symlink 剛好存在才沒斷。`routine-sync` 今天 05:42 跑過（`2026-09-23-054243`），沒接這條，連往下傳都沒有——它的 commit 範圍鎖三路徑，這條在結構上不在它的席位裡。交給一個拿不到權限的席位，跟沒交一樣。

所以本班自己做掉，改 git SSOT 的 `docs/semiont/routine-prompts/twmd-embeddings-nightly.md` 一個檔（`929a6f739`），routine-sync 明早會把它同步到各機任務檔。四處改動是同一個病的四個長相：兩處絕對路徑改成 repo 相對與 `$(git rev-parse --show-toplevel)`。pipeline 版本號 `（v1.1）` 拔掉改指該檔 frontmatter（canonical 早已 v1.3）。self-test 題數從寫死的「7 題」改成指向 BECOME §Step 9 表。

第四處最值得記：鐵律那行寫「memory 必含 6 語向量數」。站上早就 13 語，而 canonical 的 Stage 2 verify 2026-07-28 才因為同一個寫死的「6 語」連兩夜漏測六個新語言、被 REFLEXES #15 vc=2 逼著修掉。**canonical 修好了，殼層那份同源的寫死留了將近兩個月**，而它管的正好是本班每晚要交什麼。ROUTINE-PROMPT-CONTRACT 講「殼是 pointer，不是第二份 SOP」，這四處全是殼把 canonical 的事實抄了一份然後各自腐爛——同一句話就寫在被我改的那一行旁邊。

## Commit 與 push

索引 commit 前先驗 index 乾淨（前夜 babel-nightly 與今晨 routine-sync 都記過 staged 檔被並行 commit 掃走）。timestamp 先落 `$NOW` 印出 `2026-09-23 06:03` 肉眼確認後代入，co-author 如實填 Claude Opus 5 (1M context)，commit `e53834589`，`git show --stat` 驗進 commit 的正好是 12 個 related 檔，沒有夾帶。push 前再 fetch，本機從領先 14 變領先 2：babel 在 rebuild 期間自己推了一批，本班替它推最後 1 筆 pt 批次（`b497a9780`），跟前兩夜同一個形狀。pre-push 模板層語言閘門全綠，in-flight run 已跑 1139 秒超過 900 秒等待窗、依 latest-wins 放行，`5dcc2fe75..e53834589`。push 後 0/0。殼層修補走第二個 commit 分開落地，不跟索引產物混在一起。

## 收官 checklist

| 檢查項                       | 狀態                                                                    |
| ---------------------------- | ----------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                      |
| Timestamp 精確               | ⚠️（rebuild／commit／push 精確到秒。session 起點無落檔時戳，見 Beat 5） |
| Handoff 三態已審視           | ✅                                                                      |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 session 未觸發 refresh，維持原狀）                               |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0，13 語全過門檻）                              |

## Handoff 三態

繼承自 `2026-09-23-013029-twmd-babel-nightly.md`（wake-context walk 第 1 檔）與今晨 `2026-09-23-054243-twmd-routine-sync.md`：

- [x] ~~pending（本班自己留給 routine-sync 的任務檔寫死路徑）~~ — retired by 本 session，改 git SSOT 殼層 `929a6f739`，連帶收掉同檔另三處寫死。
- ⏳ blocked（延續，非本班職權）— issue #1729 馬英九腳註已擴散 12 語，等 Write session 帶哲宇 review。
- ⏳ blocked（延續，哲宇，OBSERVER-QUEUE #75 / #76 / #77 / #78）— 四位定額支持者續扣、用語庫 blanket claim、日記巴別塔七語預設、babel 入池門檻白名單，四條都在紅線或需拍板層，本班不動。
- [ ] pending（延續，babel 專屬，本班不動）— 明細留在 `2026-09-23-013029-twmd-babel-nightly.md`（`no output written by translate.py` 家族、phase-F／N 的 240 秒 timeout 44 次、旗艦文十一語委派、圖表來源列 1,124 列存量回填），不在此重抄（REFLEXES #74）。
- [ ] pending（延續，`routine-sync.py`，席位已釘 09-27 `twmd-self-evolve-weekly`）— 對賬前 `git fetch` 與鏡像新鮮度印一行，本班不碰。

本 session 新 handoff：

- [ ] pending（給明晚本班，`docs/semiont/routine-prompts/twmd-embeddings-nightly.md`）— 明早 routine-sync 跑完後驗一次本機任務檔是否真的收到今晚的殼層改動（`grep -c '/Users/cheyuwu' ~/.claude/scheduled-tasks/twmd-embeddings-nightly/SKILL.md` 應為 0）。改了 git SSOT 不等於各機吃到，這一步是本次修補唯一還沒驗到的一環。
- 無其他。verify 全綠、兩個 commit 已到 origin、無 skip、無 escalation。

## Beat 5 — 反芻

今晚的技術面比前夜更乾淨：零分岔、零 fail、13 語全數 100% 有 8 鄰居。真正有內容的是那張殼。

前夜我把殼層的寫死路徑寫成 handoff 交給 routine-sync，語氣是「不急，今晚零影響」。今天它跑了、沒接、也沒往下傳，而我一查才看懂為什麼：它的 commit 範圍鎖在三個路徑，那個檔不在裡面。我當時讀成優先序問題，實際上那個席位結構上就拿不到那個檔。這比「handoff 傳得動資訊、傳不動急迫性」更前面一步——交接連能不能被執行都沒驗過，對方認真讀了也只能原樣往下傳。那條紀律要的是一個決定，這條要的是先看一眼收件人有沒有手。

第二件事是那個「6 語」。同一個寫死的語言數，canonical 兩個月前被逼著修掉並在 pipeline 裡留了註解說明它怎麼讓 verify 連兩夜漏測，而殼層那份同源的抄本安安靜靜活到今晚。它甚至不是躲在角落——它就寫在「本殼不複寫任何 step 細節」那句話的下面幾行。殼層每晚都被完整讀一次，被我讀了幾十次，而我每次都照它的字面去交「6 語向量數」然後實際交 13 語，於是那個數字錯了也沒有任何摩擦感。**寫死的事實在被反覆讀取的地方最安全**，因為讀它的人會自動用現實去補正，補正完就不覺得需要回頭改它。這是 #91（建造與登記是兩個不同步的代謝）在殼層的形狀：修補登記在 canonical，殼層那份沒人對賬。

不到寫 diary 的門檻——這兩件都是「做了 X 順帶注意到 Y」，反芻留在這裡就夠。

🧬

---

_v1.0 | 2026-09-23 06:12 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 13,795 向量 0 fail，順手修掉本 routine 殼層四處寫死_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) 全語言 0 fail，+103 向量集中在 de／id，zh-TW 索引位元不變而 en 篇數不變但鄰居挪動——篇數持平不等於索引不變 (2) 前夜交給 routine-sync 的殼層修補被結構性退回：交接前沒驗收件席位有沒有權限 (3) canonical 兩個月前修掉的寫死「6 語」，在殼層那份抄本活到今晚，而讀它的人每次都自動補正所以沒有摩擦感_
_LESSONS-INBOX 候選（未寫入，待 vc 累積）：交接對象的權限邊界應在寫 handoff 時驗一次（本例 vc=1，與「handoff 傳得動資訊傳不動急迫性」同族但更上游）_
