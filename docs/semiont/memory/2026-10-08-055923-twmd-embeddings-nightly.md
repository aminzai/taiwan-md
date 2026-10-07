# 2026-10-08-055923-twmd-embeddings-nightly — 停擺五天後第一次重建：13 語 14,482 向量 0 fail，verify PASS，`487e76883`

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: ~05:10 → 05:59:23 +0800（約 50 分鐘，2 commits：索引 `487e76883` 05:58:29＋本 memory）
> 資料來源：rebuild log 建立時間（05:14:24）＋ `git log %ai` ＋ `date`

## 觸發

05:00 排程窗觸發，照 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.4 重建全站 bge-m3 語意索引。上一次重建是 10-03 的 `3eb33efd6`，中間 10-04〜10-07 四夜沒有跑：原因是週額度用完，飛輪全黑 87 小時（`2026-10-07-204029-semiont-heartbeat`），不是 embed host 不可達，所以不算 graceful skip，也不累計「連 3 天 skip」的 escalation。

BECOME micro 跑完：wake-context 讀到 `wake:END`，selftest 全綠，工作樹與 origin 同步。器官讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐92↑，最低仍是免疫 59，但快照已經 119 小時沒更新，06:00 data-refresh 會補上。parallel-check 回報 ACTOR_BUSY：babel writer 8123、10306、51717 正在寫捷運史十二語與韓文台東縣的重譯，本班不碰這些 dirty 檔。觀察者缺席第 12 天，缺席協議已生效，本班不受影響。

## 重建與驗證

§前置先問本機：`127.0.0.1:11434` 有 bge-m3，Stage 0 回傳 `dim 1024`，EMBED_HOST 解析成本機，沒有動到 fleet 備援。本機領先 origin 9 個 commit（babel 夜班的批次）、落後 0，不需要 pull。`build-embeddings.mjs --langs all` 跑了大約 44 分鐘，每語 186〜227 秒，13 語全部 0 fail，一共 14,482 向量，每語 1,114 篇，篇數跟 10-03 一樣。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀出 13 語，每語 1,114 篇都有 8 個鄰居，manifest 是 `bge-m3:latest`／`rag-v1`，exit=0，PASS。

## 這次的 diff 從哪來

從 `3eb33efd6` 到現在 `knowledge/` 有 96 個 commit，zh 原文動了 16 篇，幾乎都是停擺前後幾輪心跳巡邏的修正：台達電、新住民美食、眷村、蔡明亮、賴清德、AI 發展、資安、輸入法、離島與海洋文化、同婚、台東縣、澎湖縣、捷運史等。抽四語跟 10-03 比對：zh-TW 50 篇鄰居變動、60 次替換；en、ja、de 各 106〜109 篇變動、122〜140 次替換。四語都沒有新增或刪除的鍵，也沒有鄰居指向不存在的鍵。譯文替換量約是 zh 的兩倍，跟 10-03 同一個形狀：中文小修，十二語整篇重譯。

照 v1.4 用路徑式 commit 收進 `src/data/related/` 13 檔，成為 `487e76883`。commit 前 index 是空的，commit 後只包含這 13 檔，push 線性接上 origin。

## 收官 checklist

| 檢查項                       | 狀態                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                            |
| Timestamp 精確               | ✅（起點取 rebuild log 建立時間，甦醒開始時間沒有落地，標約） |
| Handoff 三態已審視           | ✅                                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班沒有觸發 refresh，06:00 data-refresh 接手）           |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                                   |

## Handoff 三態

繼承自 `2026-10-03-055622-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）：routine-sync 提出的「embeddings 改殼後要隔兩晚才生效」三選項，本班沒有改殼。
- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE #75〜#93（待決）`，本班不動。
- [ ] pending（延續，babel 專屬，收件席位 `twmd-babel-nightly`）：〈台東縣〉〈台灣捷運發展史〉十二語跟上，明細在 `2026-10-08-023621-semiont-heartbeat.md`，這裡不重抄（REFLEXES #74）。本班量到 babel 正在寫這兩篇，下一次重建會把它們的新譯文收進索引。
- [ ] pending（延續，收件席位：能動排程的 Full mode 或 `/twmd-routine`；本班在 dispatcher 寫入中動不得）：`.git/gc.log` 與 `git prune`（issue #1729），本班 fetch／commit／push 時 git 照樣警告。

本 session 新 handoff：無。

## Beat 5 — 反芻

這一班是例行全綠，唯一跟平常不同的是中間隔了五天。停擺期間索引沒有壞，讀者那邊只是「你可能也想讀」停在 10-03 的版本，巡邏修正過的十六篇用的是舊文摘算出來的鄰居。五天的變動在一次重建裡全部收回，鍵零增減，這是這條 routine「把過期上限框在一天」設計的反面驗證：停幾天，過期就是幾天，重建一次就歸零，不累積別的債。這件事不需要新教訓，額度停擺本身已經登記在 `OBSERVER-QUEUE #93`。日記照 routine 預設略過，evolve 也略過，因為沒有 ship 內容。

🧬

---

_v1.0 | 2026-10-08 05:59 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,482 向量 0 fail，verify PASS，`487e76883`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行；週額度停擺後第一次_
_核心洞察：停擺五天的過期在一次重建裡歸零，十六篇 zh 巡邏修正與十二語重譯都對得上，鍵零增減、零懸空鄰居_
_LESSONS-INBOX：無新增_
