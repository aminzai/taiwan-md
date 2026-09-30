# 2026-10-01-055635-twmd-embeddings-nightly — 13 語 14,482 向量 0 fail，verify PASS，`033916420`，兩個改回真 slug 的條目在索引裡也換了名

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗）
> Session span: ~05:05 → 05:58 +0800（~53 分鐘，2 commits：索引 `033916420` 05:55:58＋本 memory）
> 資料來源：rebuild 起跑 `date`（05:15:02）＋結束 `date`（05:55:46）＋ `git log %ai`；session 起點無落檔時戳

## 觸發

夜間 05:00 排程窗自動觸發，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.4 重建全站 bge-m3 語意索引。BECOME micro 讀完 wake-context 237,894 bytes 到 `wake:END`，selftest 全綠，工作樹與 origin/main 同步。器官讀數 🫀70↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐92↑，最低仍是免疫 59（review_coverage 缺口，self-evolve-weekly 名下），snapshot 齡 23 小時。parallel-check 報 ACTOR_BUSY（babel writer 51717、93350），工作樹只有它的 `_translation-status.json` 與 babel 報表，index 空。

## Rebuild 與 verify

§前置先問本機，`127.0.0.1:11434` 有 bge-m3，Stage 0 回 `dim 1024`，EMBED_HOST 解析為本機，fleet 備援沒動到。本機與 origin 0/0，不需 pull。`build-embeddings.mjs --langs all` 05:15 起跑、05:55 結束，每語 176〜196 秒，13 語全數 0 fail，共 14,482 向量（每語 1,114，比昨天多 1）。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，全部 1,114 篇、100% 有 8 鄰居，manifest `bge-m3:latest`／`rag-v1`，exit=0，PASS。

## 這次的 diff 從哪來

昨天零 diff 時記了一筆：索引變不變，要跟 `knowledge/` 有沒有改動對得上才算健康。今天兩邊都在動，而且對得上。昨晨重建之後 `knowledge/` 進了三件事：素人投稿 #1781〈309本里長帳簿〉與十二語譯文、babel 夜班把十語 `309.md` 改回 `village-chief-campaign-ledgers`（`28ac08c38`）、上線七週的 `society/2026` 十二語改回 `2026-advanced-subjects-test-controversy`（`94070476c`）。

量了三件事確認索引跟上：十二個譯文語言的索引裡 `309`、`2026` 兩個舊鍵都是 0，新 slug 都在，鄰居清單裡指向舊 slug 的參照是 0。`309` 從沒進過索引（它 09-30 上午才出生、今晨 00:45 就改名，中間沒有重建），`society/2026` 則在索引裡當了七週的正式鍵，今天才退場。鄰居變動量每語 4〜13 條，合計約 95 條，量級對得上「一篇新文章加一次改名」。

`src/data/related/` 13 檔改動，照 v1.4 用路徑式 commit `033916420`，commit 前 index 空、commit 後驗證只含 `src/data/related/`，push 時 origin 已先有 routine-sync 的 `ad5837968`，fast-forward 推上。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ⚠️（rebuild 起訖與 commit 精確，session 起點無落檔時戳） |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（本班未觸發 refresh，06:00 data-refresh 會接）        |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0）                              |

## Handoff 三態

繼承自 `2026-09-30-055548-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）— routine-sync 提的「embeddings 改殼後隔兩晚才生效」三選項，本班沒改殼。
- ⏳ blocked（延續，哲宇）— OBSERVER-QUEUE #75〜#91（待決），本班不動。
- [ ] pending（延續，babel 專屬，收件席位 babel-nightly）— 明細在 `2026-10-01-010545-twmd-babel-nightly.md`（ru〈309本里長帳簿〉cascade exhausted、LESSONS `gate-rejects-what-the-prompt-never-taught`、84 檔帶空白站內網址待拍板），不重抄（REFLEXES #74）。

本 session 新 handoff：無。

## Beat 5 — 反芻

昨天那句「索引零變動要有 `knowledge/` 零改動作旁證」，今天得到它的正面版本：`knowledge/` 有三件事進來，索引就該剛好反映這三件，舊鍵退場、新鍵出現、沒有鄰居還指著舊名字。改名對這條 routine 來說是一次「刪一個鍵、加一個鍵」，所以夜班修 slug 的效果要到隔天清晨索引重建後才完整落到「你可能也想讀」。這次對上了，不另開 LESSONS。不寫日記（routine 預設 skip），evolve 跳過（沒 ship 內容）。

🧬

---

_v1.0 | 2026-10-01 05:58 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 14,482 向量 0 fail，verify PASS，`033916420`_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：索引 diff 對得上 knowledge/ 的三件改動（新文章、309 與 2026 兩次改名），舊 slug 在索引裡零殘留_
_LESSONS-INBOX：無新增_
