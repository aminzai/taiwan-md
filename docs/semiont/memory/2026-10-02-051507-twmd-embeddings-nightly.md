# 2026-10-02-051507-twmd-embeddings-nightly — 13 語 14,482 向量 0 fail，verify PASS，`5b779722a`，五篇搬回原分類的譯文在索引裡換了鍵

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: 05:15:07 → 06:04 +0800（約 49 分鐘，2 commits：索引 `5b779722a` 06:02:13＋本 memory）
> 資料來源：`session-id.sh` 時戳（05:15:07）＋ rebuild 起訖 `date`（05:15:20 → 06:01:53）＋ `git log %ai`

## 觸發

夜間 05:00 排程窗自動觸發，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.4 重建全站 bge-m3 語意索引。BECOME micro 讀完 wake-context 255,807 bytes 到 `wake:END`。selftest 只亮一盞：工作樹落後 origin/main 9 個 commit（凌晨 02:45〜03:05 的心跳巡邏 heal 在 origin 側）。器官讀數 🫀70↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐92↑，最低仍是免疫 59，snapshot 齡 23 小時。parallel-check 報 ACTOR_BUSY（babel writer 22091、51717），工作樹只有它的 `_translation-status.json` 與 babel 報表，index 空。

## 先跟上 origin，再重建

落後的 9 個 commit 碰的 51 個檔跟 dispatcher 正在寫的 dirty 檔零交集，本機領先 0，所以直接 `git pull --ff-only`，沒有走 Stage 1 那段分岔處置。這一步有實際意義：落後的那批正好是巡邏修過的三篇 zh 與五篇搬回原分類的譯文，不跟上就會拿舊文字算向量。

§前置先問本機，`127.0.0.1:11434` 有 bge-m3，Stage 0 回 `dim 1024`，EMBED_HOST 解析為本機，fleet 備援沒動到。`build-embeddings.mjs --langs all` 05:15 起跑、06:01 結束，每語 198〜224 秒（比昨天的 176〜196 秒慢一點，babel dispatcher 同機在跑），13 語全數 0 fail，共 14,482 向量，每語 1,114，跟昨天同數。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，全部 1,114 篇、100% 有 8 鄰居，manifest `bge-m3:latest`／`rag-v1`，exit=0，PASS。

## 這次的 diff 從哪來

篇數沒變，索引卻 13 檔都動，所以照昨天那條規矩去對 `knowledge/`。昨晨索引 `033916420` 之後 `knowledge/` 有 134 檔改動，三種來源：10-01 兩輪心跳巡邏 heal 的六篇 zh、babel 夜班把它們推到十二語的重譯、以及 `ddf3ef987` 把五篇譯文搬回跟 zh 原文同一個分類目錄。

量了四語：en 有 8 個鍵變動，剛好是四篇搬家各「刪舊鍵加新鍵」（`art→technology` 數位動畫、`culture→food` 茶文化、`culture→geography` 與 `society→geography` 兩篇城鄉），鄰居清單裡指向舊鍵的參照是 0。zh-TW 鍵不變、15 個鄰居替換分佈在 29 篇（巡邏改了內文，鄰居微調），ja 與 de 各 50 多個替換。量級對得上「六篇內文改寫加十二語重譯加四篇搬家」。

`src/data/related/` 13 檔照 v1.4 路徑式 commit `5b779722a`，commit 前 index 空、commit 後只含 `src/data/related/`。push 時 origin 已先有 routine-sync 的 `1f5cddc63`，fast-forward 推上。

## 收官 checklist

| 檢查項                       | 狀態                                              |
| ---------------------------- | ------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                |
| Timestamp 精確               | ✅                                                |
| Handoff 三態已審視           | ✅                                                |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班未觸發 refresh，06:00 data-refresh 會接） |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                       |

## Handoff 三態

繼承自 `2026-10-01-055635-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）— routine-sync 提的「embeddings 改殼後隔兩晚才生效」三選項，本班沒改殼。
- ⏳ blocked（延續，哲宇）— `OBSERVER-QUEUE #75〜#92（待決）`，本班不動。
- [ ] pending（延續，babel 專屬，收件席位 babel-nightly）— 明細在 `2026-10-02-014120-twmd-babel-nightly.md`（LESSONS `gate-rejects-what-the-prompt-never-taught` 第三夜觀察、`patch-eligibility-measures-chapter-size-not-change-size`、84 檔帶空白站內網址），不重抄（REFLEXES #74）。
- [ ] pending（延續，收件席位：能動排程的 Full mode 或 `/twmd-routine`）— `.git/gc.log` 與 `git prune`：本班 fetch／commit 時 git 照樣警告，dispatcher 全程在寫，本班沒動。

本 session 新 handoff：無。

## Beat 5 — 反芻

這一班的關鍵動作在重建之前：甦醒時那盞「落後 9 個 commit」的燈，如果略過，索引會用巡邏修正之前的文字算一次，然後在 commit 訊息上看起來跟平常一模一樣。跟上之後的 diff 能逐項對回 `knowledge/` 的三種改動，搬家的四篇舊鍵在索引裡零殘留，不另開 LESSONS。不寫日記（routine 預設 skip），evolve 跳過（沒 ship 內容）。

🧬

---

_v1.0 | 2026-10-02 06:04 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,482 向量 0 fail，verify PASS，`5b779722a`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：先 ff 跟上 origin 才重建，索引 diff 對得上巡邏 heal、十二語重譯與四篇搬家，舊鍵零殘留_
_LESSONS-INBOX：無新增_
