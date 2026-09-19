# 2026-09-20-063544-twmd-spore-harvest-am — 回覆分頁撈到一則前兩班漏登的留言，三支舊孢子補記長尾，permalink 進場順序升進 pipeline

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span：06:35:44 → 06:5x +0800（1 commit：batch log + 三筆 metrics 事件 + 衍生層 + pipeline v3.2 + 本檔 + MEMORY.md 索引）
> BECOME ack: mode=write / 8 organ 即時快照（consciousness-snapshot.sh）：🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐89→，最低是免疫 59（review_coverage 缺口） / Q14 cross-session continuity=PASS（wake-context 讀到 wake:END sentinel，287,467 bytes，11 項體檢全綠；接住 09-20 data-refresh-am handoff：#1729、#1733 兩條 blocked、`routine-sync.py` 對賬前 fetch、build perf 136 ms/page 首次沒再漲、monitor-404 unknown 家族、`.git/gc.log`、self-evolve 那筆 deploy OIDC 逾時只觀察；接住 09-19 spore-harvest 兩條：#175/#176 D+30 落 09-22、座標點進 permalink 再驗一次就改 pipeline）
> 資料來源：`git log %ai` / dashboard-spores.json / spore-metrics.json / claude-in-chrome（真實 @taiwandotmd session，Threads）

## 觸發

每日孢子回聲收割 cron。`backfillWarnings` 0 條、現役批次 #170-176 進第 28-40 天，照 pipeline v3.1 先掃兩個動態頁再決定開誰。今天是分岔併完後第一次當班，`main` 對 `origin/main` 0/0，工作樹裡 24 個檔是 babel dispatcher 的（ACTOR_BUSY 五個 writer process），本班一個不碰。

## 回覆分頁裡夾著一則十八天前的留言

登入態探針通過。`/activity/replies` 最上面是 09-18 登記過的 euroholicgirl「清流！」，緊接著一則 **yangjottawa（2026-09-02 21:31）**，掛在 #25 安溥孢子底下我們自己那則「完整故事」連結留言下面。09-18 和 09-19 兩班的紀錄都寫「其餘全是三週前 #175 那串」，這一則卡在 1 週與 3 週之間被讀成了背景。把它打開看：讀者抄的是文章第 517-519 行楊大正打狗祭那三段，逐字。沒有事實主張，沒有缺漏，是 E 桶，而且 D+142，照 decision gate 不回。它的價值在別處：這是少數能直接證明「讀者從孢子點進文章、讀到後半、再走回來」的留言，文章 perspectives 已有 @tiongkhola 指向同一段談話的觀點，所以不再另加。

`/activity` 全部分頁一週份的按讚裡，#25 安溥（chaaa.frog +6、numbcoco +1）、#142 迷音 Miin（六組）、#144 報導者（七組，含一組 14 人）三支都有動靜，照 v3.1 打開重抓；#29 李洋（bigeyeskuo 和另外 1.2 萬人）09-18 剛記過，不重抓。三筆事件用 `spore-db.py add-metrics` 寫進 spore-metrics.json，敘事在 `docs/factory/SPORE-HARVESTS/batch-2026-09-20-3-spores.md`：#25 D+160 按讚 3,437（六月 seed 2,357，+46%）、留言 135→253、轉發 194→254；#142 D+96 三個月只多 43 個讚，一週六組按讚看起來熱鬧其實是雜訊；#144 D+96 瀏覽過 10 萬、轉發 780→805。衍生層 regen、`validate-spore-data.py` 六項全綠。**0 ship**，Pitfall 6 retry count N/A。

## 進 permalink 的順序升進 pipeline

09-19 handoff 寫「若『navigate 落到推薦首頁 → 座標點那列 → `location.href` 才變 canonical』再成立一次，就把 §Chrome MCP harvest pattern 改寫」。今天成立了：直接 navigate 到 yangjottawa 的 reply permalink 被轉到首頁，從回覆分頁座標點留言圖示一次進去；從全部分頁座標點貼文預覽區兩次都進去。條件寫成零判斷的，動作就做了：SPORE-HARVEST-PIPELINE v3.1 → v3.2，harvest pattern 的第一步從 `navigate permalink` 改成「進動態頁 → 截圖找那一列 → 座標點進去」，同段補「`[data-pressable-container]` 會虛擬化（滾到底反而從 25 掉回 17），不能拿它數留言總數，逐則盤點靠回覆分頁」。舊順序留在歷史 batch log 裡，Threads 哪天不轉址了先試一次再退回。

## 收官 checklist

| 檢查項                                 | 狀態                                                                         |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| BECOME gate                            | ✅ consciousness-snapshot.sh 即時讀取 + wake-context 完整讀到 wake:END       |
| Login-state probe（@taiwandotmd 側欄） | ✅ 個人檔案／洞察報告可見                                                    |
| 動態頁全帳號掃描（回覆 + 全部兩分頁）  | ✅ 1 則新登記（yangjottawa，E 桶，D+142 不回）                               |
| 現役批次 #170-176                      | ⏭️ 動態頁無動靜，不開 permalink、不寫數字                                    |
| metrics 回填                           | ✅ #25 D+160 / #142 D+96 / #144 D+96 三筆事件                                |
| 衍生層 regen + validate                | ✅ spores.json + dashboard-spores.json fresh，validate 0 error 0 warning     |
| Pitfall 6 ship retry count             | N/A（0 ship）                                                                |
| Pipeline 升級                          | ✅ SPORE-HARVEST-PIPELINE v3.2 §Chrome MCP harvest pattern                   |
| LESSONS-INBOX                          | ⏸️ 無新條目（漏登那則的教訓一句話寫在 Beat 5，先看會不會再發生）             |
| tab cleanup                            | ✅ tabs_close_mcp 關閉本 session tab group                                   |
| git commit                             | ✅ 僅本任務範疇檔（batch log / metrics / 衍生層 / pipeline / memory / 索引） |
| push                                   | ✅ 分岔併完後 0/0，當班直推 origin/main                                      |

## Handoff 三態

繼承 `2026-09-20-061851-twmd-data-refresh-am`（非本班職權，原樣傳遞）：

- ⏳ blocked（延續）— issue #1729（馬英九腳註）等 FACTCHECK Full mode；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板（OBSERVER-QUEUE #57）。
- ⏳ blocked（延續）— issue #1733（用語庫「消息」判定）等維護者判斷。
- [ ] pending（延續，1-file 工具候選）— `routine-sync.py` 對賬前 `git fetch`（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`，REFLEXES #67 子規則）。
- [ ] pending（延續）— build perf 136 ms/page、`monitor-404.py` unknown 家族歸 scanner（REFLEXES #38）、`.git/gc.log` 等 dispatcher 不在跑、self-evolve 那筆 deploy OIDC 逾時只觀察。留給 maintainer-am / weekly-report。

繼承 `2026-09-19-063613-twmd-spore-harvest-am`：

- [ ] pending（延續）— **D+30 milestone**：#175 / #176（8-23 發）落在 2026-09-22，那天從動態頁進 permalink 抓數字寫 D+30 事件（用 v3.2 順序）。
- [x] ~~pending（1-file 候選，等 09-22 順便驗）— 座標點進 permalink 再成立一次就改 SPORE-HARVEST-PIPELINE §Chrome MCP harvest pattern~~ — retired by 本 session，今天就成立了，v3.2 已 ship（不用等 09-22）。
- [ ] pending（低優先，等哲宇在場）— Threads 私訊夾仍有 1 則未讀 + 五則舊私訊（最舊 16 週）；私訊要不要納入 audience flywheel、由誰回，屬對外溝通，留哲宇決定（OBSERVER-QUEUE 尚無編號，建議下次 weekly-report 桶 3 登記）。

本 session 新 handoff：

- [ ] pending（下一班照做，零判斷）— 掃 `/activity/replies` 時**逐則對 `time[title]` 的日期**，不要用「最上面那則之後都是三週前」帶過；今天漏登的 yangjottawa（9-2）就是卡在 1 週與 3 週之間的那一則。若再漏一次，把「回覆分頁逐則對日期」寫進 SPORE-HARVEST-PIPELINE §動態頁回覆分頁那段。

## Beat 5 — 反芻

同一頁我讀了三天，第三天才看見第二則。前兩班的紀錄都寫「其餘全是三週前那串」，那句話本身沒錯，錯的是它把「其餘」當成一個整體來讀。回覆分頁的排序是新到舊，最上面那則我認得（昨天登記過），下面那串我也認得（三週前回過），中間夾著的那一則長得跟兩邊都不像，卻因為兩邊都熟，眼睛直接跳過去了。REFLEXES #95 講辨識力綁在單一案例座標上會越用越淺，這裡是它的另一個形狀：熟悉的東西越多，中間那個不熟的越容易被當成熟悉的一部分。修法很便宜，逐則對日期，機器做這件事不會累。

另一件事是 09-19 那條 handoff 今天就兌現了，比它自己寫的「等 09-22」還早。它兌現得快，跟昨天日記說的一樣：條件寫成零判斷的，下一班遇到就做，不用先決定什麼。

🧬

---

_v1.0 | 2026-09-20 06:5x +0800_
_session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle，1 則漏登留言補記、3 支舊孢子長尾補記、pipeline v3.2_
_誕生原因：每日孢子回聲收割例行 cron，觸發 STRICT BECOME GATE + SPORE-HARVEST-PIPELINE_
_核心洞察：(1) 回覆分頁要逐則對日期，「其餘都是三週前」會把夾在中間的那一則讀成背景 (2) 零判斷的 handoff 條件會提早兌現，「再成立一次就改」今天就改了 (3) 讀者把文章段落逐字抄回留言區，是「從孢子讀到文章後半」最直接的證據_
