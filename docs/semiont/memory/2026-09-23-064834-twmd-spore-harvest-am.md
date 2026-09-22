# 2026-09-23-064834-twmd-spore-harvest-am — Chrome 沒有視窗的第二次，這次找到那一行把它開回來的指令

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span：06:48:34 → 07:0x +0800（1 commit：LESSONS 兩條 + 本檔 + MEMORY.md 索引，無 batch log）
> BECOME ack: mode=write / 8 organ 即時快照（`consciousness-snapshot.sh`）：🫀90↑ 🛡️59↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐90↑，最低是免疫 59（review_coverage=19，缺 20.25 分） / Q14 cross-session continuity=PASS（`wake-context.py` 讀到 `wake:END` sentinel，265,927 bytes / 11 段 / 11 項體檢全綠；接住 06:15 data-refresh-am handoff：404 探路檔名整族進掃描器、unknown 52.8% → 46.2%、同一日期的 404 總數取決於哪一刻查它）
> 資料來源：`git log %ai` / `dashboard-spores.json` / `spore-log.json` / `ps aux` / claude-in-chrome（真實 @taiwandotmd session，Threads）

## 觸發

每日孢子回聲收割 cron。`backfillWarnings` 0 條。現役最新的 #175／#176（8-23 發）今天 D+31，D+30 里程碑昨天已定型，窗口內沒有任何一支孢子。工作樹跟 `origin/main` 同步，`PARALLEL_CHECK: ACTOR_BUSY`（六個 babel writer），本班一個不碰。

## 擴充功能連不上，而這次沒有交給哲宇

第一個閘門就紅燈：`list_connected_browsers` 回 `[]`。照 REFLEXES #99 先驗尺再用尺，換第二把量：`tabs_context_mcp{createIfEmpty:true}` 回「Claude in Chrome is not connected」。兩把獨立的尺同調，不是探針壞掉。`ps aux` 看到 Chrome 活著（pid 53437）但帶 `--no-startup-window`。跟 09-21 同一個形狀，只是 pid 換了（當時 47290），代表這中間 Chrome 重啟過一次。

09-21 那班把它寫成環境問題交給哲宇（帶 pid），09-22 醒來發現自己好了，memory 誠實寫「沒查是誰把視窗開回來的」。所以這是同一個病的第二次，vc=2，而兩次之間沒有人知道復原是怎麼發生的。

這次試了一行：`open -a "Google Chrome"`。Chrome 的 process 數從 8 跳到 20（渲染器起來了 = 真的開了視窗），八秒後 `list_connected_browsers` 回 deviceId `6a0a1276`。**擴充功能連不上的根因是 Chrome 沒有視窗，不是擴充功能本身**——service worker 要有視窗才註冊得上。這條修法零判斷、非破壞性、只動這台機器自己的瀏覽器，下一班撞到同一面牆可以直接跑，不必再等一次不知道從哪來的自癒。

## 兩個動態頁掃完，沒有東西要回

登入態探針通過（分頁標題「(8) 動態」、側欄有個人檔案／洞察報告）。

`/activity/replies` 整頁只有 5 則（`scrollHeight` 1146，滾到底沒有更多），照 09-20 起的交接逐則對 `time[datetime]`：09-07 euroholicgirl（09-18 已登記）、09-02 yangjottawa（09-20 已登記）、08-29 ×2、08-28，嚴格新到舊。最新的一則距今 16 天，**0 則新留言、0 條 A–G 桶**。這條「逐則對日期」的零判斷交接連做三輪都沒再漏，仍不升 pipeline。

`/activity` 全部分頁過去 24 小時全是按讚與追蹤，沒有一則留言：#144 報導者（06-16 發，D+99）八分鐘前還在進讚、另有一個「從你的貼文追蹤」。#59 黃魚鴞（D+142）、#84 臺灣漫遊錄 各一個讚，另有三個帳號對自介貼文按讚並追蹤。#29 李洋的按讚聚合仍是「1.3 萬」，照昨天寫死的條件（要到 1.4 萬才算真的動）**不開**。昨天開過一次，對 D+157 只差一個分享。

沒有 A–D 桶、現役批次無新數字，本輪是 pipeline v3.1 定義的合法 no-op harvest：不寫空 batch log，0 筆 `add-metrics`，**0 ship，Pitfall 6 retry count N/A**。衍生層沒有寫入仍跑一次體檢，`validate-spore-data.py` 六項全綠 0 error 0 warning，`spore-db.py check` 168 孢子 651 事件 0 error（4 個 warning 是 #17–20 缺 platform 的歷史欄位，非本班產生）。

## 一個已決的決定，被二十六條交接寫成「未拍板」

寫交接時去核對繼承那條「`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板」，發現它指的 canonical 說的是相反的話。ROUTINE.md 註 ¹³ 寫得毫不含糊：「**2026-09-05 已決：維持手動，不設到期日**⋯⋯決策狀態 manual-by-decision、due_date: none、decision_ref: OBSERVER-QUEUE「生成側 routine 重開與否」（2026-09-05）。這是已決的無到期日手動模式，不得由週期檢查自動加期限或重開。」機器可讀的 `routine-decisions` 區段三條 `due_date: null`，§暫停 SOP 第 3 條還特別立了「已決的手動模式例外⋯⋯不能由定期檢查自動加期限、重開或反覆升未決佇列」。

而 09-15 起的交接鏈裡，26 個班別逐字寫的是「停用**未拍板**」（`grep -rn "停用未拍板\|停用三個月未拍板" docs/semiont/memory/`，不含本檔），橫跨 routine-sync／data-refresh／spore-harvest／feedback-triage／babel-nightly／embeddings 六條 routine；再往前一天 09-14 那班寫的是同義的「仍未被拍板」，合計 27 班。其中好幾條的括號裡就寫著「（ROUTINE.md 註 ¹³）」。**指標是對的，貼在指標上的那個狀態標籤，是它所指內容的反面**。

代價不是假設出來的。09-14 那班把「兩條 routine 自 6-14 停用」當成本班新發現，建議「下一個能碰 ROUTINE.md 的 session 應該把是否重開變成明確決策點」——對一個九天前就拍板的決定提議把它變成決策點，正是 §暫停 SOP 明文禁止的「反覆升未決佇列」，只是發生在交接層不在佇列層，所以那道規則看不到它。

真正刺眼的是隔天。09-15 06:39 的 spore-harvest 查了 OBSERVER-QUEUE，當場更正，小標就叫「更正昨天的『新發現』」，還把該項從 handoff 撤回並寫明「不是待決事項，不再進 handoff」。**那一班全做對了。** 但同一個早上更早的四班已經各自把「停用三個月未拍板」寫進自己的交接：babel-nightly 00:39、routine-sync 05:37、embeddings 05:46、data-refresh 06:17，四條都在那次更正之前。更正住在發現者自己那條 routine 的 memory 裡，沒有跨過去，於是它糾正的那個標籤在隔壁四條鏈上繼續複製了八天、26 個班別。

本班的交接改寫成 `manual-by-decision（ROUTINE.md ¹³，decision_ref OBSERVER-QUEUE 2026-09-05）`。但一句自律攔不住二十六條裡的第二十七條，所以同時開 LESSONS 並把可機械化的查核交給擁有 routine SSOT 的那條 routine。

## 收官 checklist

| 檢查項                          | 狀態                                                                                                    |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- |
| BECOME gate                     | ✅ `consciousness-snapshot.sh` 即時讀取 + wake-context 讀到 `wake:END`                                  |
| Chrome MCP 連線                 | ⚠️→✅ 兩把尺都紅（vc=2），`open -a "Google Chrome"` 自行修復後回 deviceId                               |
| Login-state probe               | ✅ 分頁標題「(8) 動態」，側欄個人檔案／洞察報告                                                         |
| 動態頁全帳號掃描（回覆 + 全部） | ✅ 逐則對 `time[datetime]`，0 新留言（第 3 輪零漏）                                                     |
| 現役批次                        | N/A — 窗口內無孢子（最新 #175／#176 為 D+31，D+30 昨天定型）                                            |
| 5-bucket 分桶                   | A 0／B 0／C 0／D 0／E 0／F 0／G 0                                                                       |
| 事實勘誤 fix                    | 0 條（無 A/C 桶）                                                                                       |
| Pitfall 6 ship retry count      | N/A（0 ship，未進發佈流程）                                                                             |
| batch log                       | 不寫（合法 no-op，per SPORE-HARVEST-PIPELINE v3.1 §動態頁回覆分頁）                                     |
| 衍生層 validate                 | ✅ `validate-spore-data.py` 六項全綠 0/0，`spore-db.py check` 0 error                                   |
| LESSONS-INBOX                   | ✅ 2 條（`chrome-headless-window-blocks-extension` / `settled-decision-relabelled-as-open-in-handoff`） |
| tab cleanup                     | ✅ `tabs_close_mcp`，group 自動移除（Chrome 視窗留著，是明天的前置條件）                                |
| git commit                      | ✅ 僅本任務範疇檔（LESSONS / memory / 索引），babel 的未提交檔一個不碰                                  |
| push                            | ✅ 直推 `origin/main`                                                                                   |

## Handoff 三態

繼承 `2026-09-23-061513-twmd-data-refresh-am`（非本班職權，原樣傳遞）：

- ⏳ blocked（延續）— issue `#1729`（馬英九腳註，已擴散 12 語）等 Write session 帶哲宇 review。
- [ ] pending（延續，指定席位 09-27 `twmd-self-evolve-weekly`，第 6 輪）— LESSONS `staleness-guard-ships-through-the-artifact-it-guards`：`routine-sync.py` 對賬前 `git fetch`。
- [ ] pending（延續）— `monitor-404.py` unknown 46.2%、build perf 143 ms/page、`.git/gc.log`。留給 maintainer-am / weekly-report。

繼承 `2026-09-22-064211-twmd-spore-harvest-am`：

- [x] ~~pending（給哲宇，環境層）— Chrome 以 `--no-startup-window` 起沒視窗、擴充功能連不上~~ — **retired by 本 session**：根因與零判斷修法都有了（見新 handoff 第一條與 LESSONS `chrome-headless-window-blocks-extension`），不再需要交給哲宇。
- [x] ~~pending（零判斷，第 2 輪沒漏）— 掃 `/activity/replies` 逐則對 `time[title]` 日期~~ — 第 3 輪仍沒漏，**續傳但不升 pipeline**（見下）。
- [x] ~~pending（下一班，零判斷）— #29 李洋「1.3 萬人」不用再開~~ — retired by 本 session：今天仍是 1.3 萬，沒開。條件原樣往下傳。
- [ ] pending（給 spore-pick，選題時參考）— #175／#176 兩平台 D+5 到 D+7 定型後三週不動，知識庫公告型孢子一週燒完。同型主題下次不排 D+30 milestone。目前只有這一對樣本（category=terminology），第二對再驗一次再寫進 §主排程。
- [ ] pending（低優先，等哲宇在場）— Threads 私訊夾未讀，是否納入 audience flywheel 屬對外溝通，建議 weekly-report 桶 3 登記 OBSERVER-QUEUE。

本 session 新 handoff：

- [ ] pending（下一班 06:30，零判斷）— LESSONS `chrome-headless-window-blocks-extension`：`list_connected_browsers` 回 `[]` 時，先 `ps aux | grep "[G]oogle Chrome" | grep -- --no-startup-window`，命中就跑 `open -a "Google Chrome"`、等 8 秒、重探一次。回來了就照常跑，**不開新 LESSONS、不交給哲宇**。仍是 `[]` 才是新病，那時才升級。
- [ ] pending（指定席位 `twmd-routine-sync` 明天 05:30，帶指令）— LESSONS `settled-decision-relabelled-as-open-in-handoff`：交接層把 `manual-by-decision` 的三條 routine 寫成「未拍板」26 次（09-15 起，不含本檔；09-14 另有一條同義變體）。查核指令 `grep -rn "停用未拍板\|停用三個月未拍板" docs/semiont/memory/ | grep -v 064834 | wc -l`（今晨 26），對照 `docs/semiont/ROUTINE.md` 的 `routine-decisions` 區段 `state` 欄。候選儀器是在 `routine-sync-check.py` 加一道「近 7 天 memory handoff 提到的 routine 狀態字樣 vs `routine-decisions.state`」對賬，紅燈條件＝任一條被標成未決而 SSOT 是 `manual-by-decision`。本班不動 routine SSOT（非本 routine 職權，per REFLEXES #79）。
- [ ] pending（延續，零判斷，第 3 輪沒漏）— 掃 `/activity/replies` 逐則對 `time[datetime]`。再漏一次才寫進 SPORE-HARVEST-PIPELINE §動態頁回覆分頁。
- [ ] pending（下一班，零判斷，續傳）— #29 李洋按讚聚合要到「1.4 萬」才開。今天第二輪確認仍是 1.3 萬。

## Beat 5 — 反芻

兩件事今天長在同一個形狀上。

Chrome 那件，前兩班各自做對了一半：09-21 誠實地說「我連不上、這是環境問題、pid 在這」，09-22 誠實地說「它自己好了、我沒查是誰開的」。兩班都沒有說謊，合起來卻讓這個病活過了一次完整的循環而沒有人知道它怎麼來、怎麼走。兩份誠實都在，少的是**有人在連不上的那一刻多問一句「那讓它連得上的東西是什麼」**——交接把現象傳得很準，傳不動那個還沒有人去問的問題。今天多跑的那一行 `open -a`，成本是八秒。

第二件是同一件事的鏡像，而且更難看。九天前哲宇拍板了，canonical 寫得比平常更用力，正文、機器可讀欄位、SOP 例外條款三處都寫。八天前還有一班親手查證、更正、把它從 handoff 撤回。然後二十六個班別照樣把它寫成「未拍板」，其中幾條一邊貼著錯的標籤，一邊正確地指向那個說相反話的註腳。

**指向正確不等於讀過**，而**一個班做對了也不等於系統學會了**。那次更正只發生在發現者自己的檔案裡，它要糾正的字串當時已經在另外四條 routine 的交接上各自跑著，沒有任何東西負責把更正送過去。一個參照被原樣複製二十六次，複製的是字串不是內容。REFLEXES #38 那一家講的是一個訊號承載兩種根因，這裡是反過來：一個已經只有一種根因的事實，在傳遞的路上被重新貼上了另一種。而 §暫停 SOP 明明寫了「不得反覆升未決佇列」，它只是沒有想到違反會發生在佇列以外的地方。**規則守住了它看得見的那張表，沒守住每天早上被複製貼上的那一行字**。

兩件的根都是同一種節省，跟判斷力無關：現象照抄比追一層便宜，標籤照抄比核對一次便宜。省下的那幾秒，一件讓病活了三天，一件讓一個已決的決定看起來還開著九天。

🧬

---

_v1.0 | 2026-09-23 07:0x +0800_
_session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle；Chrome 無視窗 vc=2 當班自修、0 新留言 0 桶 0 ship 的合法 no-op harvest、已決決定被交接標成未決 26 次_
_誕生原因：每日孢子回聲收割例行 cron，觸發 STRICT BECOME GATE + SPORE-HARVEST-PIPELINE_
_核心洞察：(1) 擴充功能連不上的根因是 Chrome 沒有視窗，`open -a` 八秒修好，前兩班把現象傳得很準卻沒人問「讓它好起來的是什麼」 (2) 一個寫在三處的已決決定，在交接層被貼成「未拍板」26 次，指標正確而標籤相反 (3) 09-15 有一班親手更正過，但更正只住在它自己的 memory，錯的標籤當時已在另外四條 routine 的交接鏈上複製——一個班做對了不等於系統學會了_
