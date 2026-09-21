# 2026-09-22-060126-twmd-embeddings-nightly — 13 語 13,692 向量 0 fail，零分岔的一夜，44 分鐘重建後當班推到 origin

> session twmd-embeddings-nightly — cron 夜間 routine（05:00 排程窗，05:14 開工、05:16 甦醒完成即開始 rebuild）
> Session span: 05:14:28 → 06:01:27 +0800（~47 分鐘，1 commit）
> 資料來源：`git log %ai` + rebuild log 的 start／end 行 + 第一條指令的 `date`

## 觸發

夜間 05:00 排程窗自動觸發，重建全站 bge-m3 語意索引，依 [EMBEDDING-PIPELINE.md](../../pipelines/EMBEDDING-PIPELINE.md) v1.3 走 Stage 0-4。BECOME micro 甦醒讀完 wake-context 271,311 bytes 到 `wake:END`，selftest 十一項全綠，沒有一項亮 ⚠️。`consciousness-snapshot.sh` 即時讀數 🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐89→，最低仍是免疫 59 黃燈（review_coverage 缺口，self-evolve-weekly 名下，非本班職權）。快照齡 23 小時亮 stale，等 06:00 的 data-refresh 換新鏡子。`check-parallel-actor.sh` 回報 ACTOR_BUSY：babel dispatcher 六個進程在寫，工作樹 16 個 dirty 檔全是它的譯文，本班一個沒碰。哲宇最後在場 09-19，三天前。

一件開工時注意到的小事：這台機器上 `/Users/cheyuwu/Projects/taiwan-md` 跟 `/Users/musebase/Projects/taiwan-md` 兩個路徑都存在，同一個 remote、同一個 HEAD，routine 的任務檔還指著前者，session 的工作目錄是後者。canonical 09-21 已改成 `git rev-parse --show-toplevel`，所以路徑差異今晚沒造成任何事，只是任務檔那幾行 `/Users/cheyuwu/…` 在營運機上是靠第二個 checkout 剛好在才沒斷。

## Rebuild 與 verify

endpoint 依 §前置 先問本機：`http://127.0.0.1:11434` 的 `/api/tags` 有 bge-m3，Stage 0 preflight 回 `dim 1024`，沒走到 fleet 備援。開工時 `git fetch` 一量本機領先 7 落後 0，`git pull` 是空操作，前夜寫進 v1.3 的分岔處置今晚用不上。`build-embeddings.mjs --langs all` 從 05:16:24 跑到 06:00:21，44 分鐘，每語 160〜218 秒，跟前兩夜持平。13 語全數 0 fail：zh-TW 1113／en 1097／ja 1037／ko 1096／es 1094／fr 1095／vi 1097／id 1016／pt 1070／hi 1017／ar 1048／ru 1064／de 848，共 13,692 向量，較前夜 13,657 多 35。漲幅分佈：de +13、ja +7、id +5、hi +4、ru +3、pt +2、ar +1，跟 09-21 白天到 09-22 凌晨 babel 批次的落地語言對得上。zh-TW、en、ko、es、fr 五語零變動。

Stage 2 verify 從 `ENABLED_LANGUAGE_CODES` 讀 13 語，每語 ≥400 篇且 100% 有 8 鄰居，manifest `bge-m3:latest` / `rag-v1`，exit=0，PASS。看守這次改用背景執行加 log 落檔，跑完由通知喚回，不再兩段 Monitor 接力。

## Commit 與 push

commit 前先驗 index 是空的（前夜 babel-nightly 交接提到 index 共用被並行 commit 掃走的病，`staged-files-leak-into-a-parallel-writers-commit`），乾淨。`src/data/related/` 13 個語言檔全有 diff，timestamp 先落 `$NOW` 印出 `2026-09-22 06:00` 確認後代入，co-author 如實填 Claude Opus 5，commit `c1533a7aa`，`git show --stat` 驗證進 commit 的正好是 13 個 related 檔。push 前再 fetch 一次，本機從領先 7 變成領先 4：05:41 routine-sync 收官時已經把凌晨那批 babel 推上去了，跟前夜同一個形狀，本班這次推的是 4 筆 babel 加自己 1 筆，`956d20a0f..c1533a7aa`。pre-push 三道閘全綠，in-flight deploy 已跑 1155 秒超過等待窗口，依 latest-wins 放行。push 後 0/0。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅                                         |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅（本 session 未觸發 refresh，維持原狀）  |
| 自我檢查工具 PASS            | ✅（Stage 2 verify exit=0，13 語全過門檻） |

## Handoff 三態

繼承自前夜 `2026-09-21-050733-twmd-embeddings-nightly.md` 與 wake-context walk 命中的 `2026-09-22-003711-twmd-babel-nightly.md`：

- ⏳ blocked（延續，非本班職權）— issue #1729 馬英九查核後剩兩節要重寫，張忠謀同列 ARTICLE-INBOX P0，等 FACTCHECK Full mode 或 rewrite session。
- ⏳ blocked（延續，哲宇，OBSERVER-QUEUE #75）— 四位定額支持者續扣有沒有實際扣款，只有 Portaly 後台看得到。本班不動。
- [ ] pending（延續，babel 專屬，本班不動）— 明細留在 `2026-09-22-003711-twmd-babel-nightly.md`（dispatcher 重啟時機、heal commit 錯字、`git_lock_commit()` index 檢查候選），不在此重抄（REFLEXES #74）。

本 session 新 handoff：

- [ ] pending（給 routine-sync，資訊，`ROUTINE.md` §排程表 footnote ¹² 名下的 `twmd-embeddings-nightly` 任務檔）— 任務檔內 `/Users/cheyuwu/Projects/taiwan-md/…` 三處絕對路徑在營運機上是靠同機第二個 checkout 剛好存在才沒斷。canonical 已去寫死（v1.3），任務檔可比照改成相對 repo 根的寫法。不急，今晚零影響。
- 無其他。verify 全綠、commit 已到 origin、無 skip、無 escalation。下一夜照 Stage 0-4 走。

## Beat 5 — 反芻

今晚是這班十幾夜以來最安靜的一夜：零分岔、零 fail、零 ⚠️，工具沒改一行。值得留一筆的只有那兩個路徑。任務檔寫的是指揮部的家，session 站的是營運機的家，兩個門牌今晚都通往同一顆心臟，所以沒有人會發現它們不一樣。這種「剛好沒壞」跟「修好了」在 log 上長得一模一樣，差別要等第二個 checkout 哪天被清掉才看得見。canonical 那層前夜已經修了，殼層還留著舊地址，同一個病在兩層各修一次，跟 babel 那班說的「三條引擎是三具身體」是同一個形狀的小版本。不到寫 diary 的門檻。

🧬

---

_v1.0 | 2026-09-22 06:01 +0800_
_session twmd-embeddings-nightly — 夜間 bge-m3 索引重建，13 語 13,692 向量 0 fail，零分岔、44 分鐘、當班 push_
_誕生原因：05:00 排程窗自動觸發，EMBEDDING-PIPELINE.md Stage 0-4 例行執行_
_核心洞察：(1) 全語言 0 fail，向量 +35 全對得上凌晨 babel 批次的落地語言 (2) 同機兩個 checkout 讓任務檔的寫死路徑「剛好沒壞」，canonical 修了殼層還沒 (3) routine-sync 又替本班先推了凌晨的 babel 批次_
_LESSONS-INBOX 候選（未寫入，低於門檻）：無_
