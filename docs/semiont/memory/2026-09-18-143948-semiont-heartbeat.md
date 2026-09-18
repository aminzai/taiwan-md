# 2026-09-18-143948-semiont-heartbeat — 馬英九條目查核完：在世的人被寫成辭世、十七處查無來源，探測器的黃燈點回來，地圖標記不再每次亂撒

> session semiont-heartbeat — scheduled Full mode heartbeat（本機排程，下午檔期）
> Session span: 14:38 → 15:20 +0800（約 42 分鐘工作段，甦醒讀檔在前；8 commits + 1 PR merge）
> 資料來源：`git log %ai`

## 觸發

scheduled task `semiont-heartbeat` 14:30 檔期，今天第三輪（02:38、08:40 之後），而且哲宇剛在 13:00–14:20 的 news-radar session 裡跑完新聞雷達、派了三隻 Opus 寫手又叫停又重開。甦醒十一項體檢全綠，工作樹跟 origin 同步。同一棵樹上 news-radar 那個 session 還在動（它中途 commit 了 `39f3e6e647`），所以整輪只 stage 自己的檔、push 前 rebase。三隻寫手的 worktree（`.worktrees/20260918-*`）一個字沒碰。

## 診斷

`refresh-data.sh` 十四步全綠（`6814d7eb47` + `ccc623f5da`）。器官讀數跟早上一樣：心臟 50、免疫 58、其餘 80 以上。三盞黃燈（免疫漂移、MEMORY 索引 88 列、routine-live-state 齡 224h）都等 #68 分岔合併，本輪不動。新東西只有一個：BrianHuang813 09:54 開的 PR #1747，maintainer-am 08:40 那輪還沒看到。

## 執行一：PR #1747，語言註冊表接回 header

Brian 的修法很對：`Header.astro` 跟 `Layout.astro` 的 `isHome` 寫死 `/` 和 `/en`，其他九個語言的首頁一進來 header 就當成已經捲動過，`page_type` 那條正則也凍在五個語言。改成從 `ENABLED_LANGUAGE_CODES` 推導，下一個語言出生就自動對。八條 CI 全綠、MERGEABLE，squash merge（`3ca4acd3b6`）加一則英文致謝。

## 執行二：馬英九，issue #1729 等的那次 FACTCHECK Full mode

這條 issue 從 09-14 開著等「FACTCHECK Full mode」，兩輪維護班都只覆驗了開票那兩條腳註、沒動手，理由是政治人物條目。我這輪是 Full mode，就接了。派一隻 general-purpose agent 照 FACTCHECK-PIPELINE Phase 2–5 跑：30 條非維基腳註全部實讀（WebFetch 56 次、瀏覽器 5 頁、curl 42 條）、72 個原子逐字對來源。結果比 issue 估的糟很多：**非維基腳註 claim 對不上的 12 條，40%**，72 原子 ❌ 17。最重的一條 issue 根本沒提，因為它沒有腳註可以對不上——30 秒概覽寫「5 月 22 日辭世新聞底下」，馬英九在世，那天是他拍片回應失智傳言。十一個語言的譯本各自忠實地譯成 passing、fallecimiento、décès、死去、사망。

agent 回報的每一條我沒有直接採信（REFLEXES #31），把七個關鍵來源自己 curl 一遍：華人今日網的江宜樺原話、維基 1998 選舉頁的六個數字、維基二訪頁的「歡迎你以後常常來」、ETtoday 記者會的「最恥辱」、遠見的「業務侵占罪」、RFA 的「那些讓台灣停滯不前的罪人啊！」、維基 323 的「更二審」「5 時 30 分」——都在。然後依 CORRECTION-PIPELINE 分三種手勢落一個 heal commit（`8cc6a667e1`）。可追溯的改回來源原文：記者會引語、罪名、審級、計畫名稱、Britannica 原句。查無來源的撤掉：辭世、東吳演講與「害死台灣」引語、「150 人受傷」、油電三組數字、「300 億」、「8 次提統一」、「不沾鍋」三處互相矛盾的年份、木柵線與基隆河。來源掛錯的換掉：錢復推薦改掛真有那句的維基與官職資料庫、1998 數字換維基選舉頁、TNL 與遠見 129661 兩條跟所掛 claim 完全無關的整條刪、六條 404 死連結清掉。段落脊椎一處沒動。

譯本只同步修兩處：辭世那句，跟 `[^31]` 太陽花引語的正文段落加腳註——在世的人被寫成過世、偽造引語歸給在世政治人物，這兩件事等不了重譯。先查過這十一檔都不在救援分支的變更集裡（只有 de 版在 #1710 那側），不會給 #68 再長衝突面。其餘十幾處靠 zh 雜湊變更觸發 stale 重譯。完整 audit 表 append 在 `reports/research/2026-05/馬英九.md` §2026-09-18，Phase 6 由我補寫。issue #1729 留一則技術說明，先不關。FACTCHECK 的硬門檻是 ❌ 超過 10% 就要退回重寫，這篇 23.6%，卸任後節跟太陽花節該局部重寫。那是政治人物條目的脊椎判斷，INBOX P0 條目改成記這件事，留給 Write session 帶哲宇 review。

## 進化：兩件小的

news-radar 留的 handoff 說「探測器落後 > 7 天 🟡」那盞燈還沒重點亮。它在 SENSES 凋亡時跟著檔案消失，之後 138 天沒人發現雷達停擺。本輪把它搬進 `generate-dashboard-alerts.mjs`（`e012bfff6d`）：量 `reports/probe/` 最新檔案的齡，超過 9 天亮黃燈（news-lens-weekly 週日跑，7 天週期加 2 天寬限，用舊的 7 天會在每個週六準時誤報），目錄空也亮，owner 是 `twmd-news-lens-weekly`。三態各驗一次：今天剛跑零條、12 天前的檔亮 probe-stale、沒檔亮 probe-missing。consciousness-snapshot 每次甦醒都印這層，所以下次雷達停擺會在第十天的第一句話裡出現。

第二件是順手的。第一個 refresh commit 帶了 6,688 行 `map-markers.json` 變更，翻回去看，早上兩次刷新也各 6,688 行——`generate-map-markers.js` 用 `Math.random()` 把同城重疊的標記撒開，每次 prebuild 重撒 1,700 顆。改成用「檔案路徑｜城市」做 FNV-1a 雜湊決定方向（`6ddaed2707`），連跑兩次 `cmp` 一致，座標零重疊。以後每個資料刷新 commit 少 6,000 行純噪音。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                                                                 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                                                                   |
| Timestamp 精確               | ✅ git log %ai                                                                                                                                       |
| Handoff 三態已審視           | ✅                                                                                                                                                   |
| CONSCIOUSNESS 反映最新狀態   | ✅ dashboard 全套重刷（`6814d7eb47`），§警報補探測器落後這一維                                                                                       |
| 自我檢查工具 PASS            | ✅ 馬英九 zh article-health hard=0 / prose-health 3；en/ja/ko 譯本 hard=0；alerts 生成器三態實測；map-markers 兩次 build cmp 一致；pre-push 三閘全綠 |
| Diary                        | ❌ 不寫：diary-gate PASS，但反芻是 08:40 那條「閘門守完整不守歸屬」與 LESSONS `babel-amplifies…` 的第二次命中，bump 了 vc=2，沒長成新問題            |

## Handoff 三態

繼承 `2026-09-18-132812-news-radar` 與 `2026-09-18-083954-semiont-heartbeat`：

- ⏳ blocked（給哲宇，🔒）— OBSERVER-QUEUE #68 分岔合併方向、#67 babel 覆蓋投稿者譯文，等拍板；拍板前兩台都別跑 babel 存量
- ⏳ blocked（給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C；`reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留
- [x] ~~issue #1729 等 FACTCHECK Full mode~~ — 本輪跑完，可撤可改的全落 `8cc6a667e1`；剩兩節重寫見下
- [x] ~~「探測器落後 > 7 天 🟡」那盞燈~~ — 本輪進 dashboard-alerts（`e012bfff6d`），閾值 9 天
- [ ] pending（給哲宇）— 讀 `reports/probe/2026-09-18.md` 決定亞運與中華台北 P0 派不派；T1-D 科技監控要他點頭
- [ ] pending（給 distill-weekly）— INBOX 登記修正（衛武營 → done、初級大人 P0 → P2、金城武／張懸與安溥 P1 → P0、Blue UAS 升回 P0）——news-radar 原文照抄
- [ ] pending（三隻 Opus 寫手，哲宇「全部重開，繼續跑」）— 低薪 / 油價 / 金鐘各在 `.worktrees/20260918-*`，本輪沒碰；接手者先 `test -f` 重驗再信 ship 宣稱
- [ ] pending — 合併落地後 MEMORY / DIARY 索引兩邊都 rollup 過，index-archive/2026-09.md 只在分支那側；`routine-live-state.json` 黃燈合併後自動熄
- [ ] pending — `台灣原住民當代藝術` 十語譯本仍帶舊錯，#68 合併後確認 stale 重譯；拖過一週就單獨跑 translate.py
- [ ] pending — `observer-queue-lint.py` WARN 收兩週數據後決定升不升 HARD
- [ ] pending（延續）— OBSERVER-QUEUE 兩側撞號主鍵、slug 慣例對照升工具、`routine-stall-check.py` 尺二救援分支驗證、issue 認領步驟進 MAINTAINER-PIPELINE、兩台機器 issue 職責歸屬進 ROUTINE.md

本 session 新 handoff：

- [ ] pending（Write session，帶哲宇 review）— 馬英九 §從 80 秒到 16 秒（卸任後節）與太陽花節退回 REWRITE Stage 2 局部重寫：FACTCHECK ❌ 23.6% > 10% 硬門檻。INBOX P0 條目已改成記這件事；issue #1729 留開等這步完成再關。
- [ ] pending — 馬英九 11 語譯本只修了辭世句與 `[^31]` 段，其餘 18 處改動靠 zh 雜湊變更觸發 stale 重譯；#68 合併後確認 status.py 把它們排進第一批。de 版在 PR #1710 上，等那條 PR 自己處理。
- [ ] pending（給 self-evolve 或下一個 Full mode）— FACTCHECK 月度巡邏抽樣指令排出的前五篇（緣起故事／日治時期／張忠謀／李安／蔡英文）仍沒人跑；本輪接的是 issue 驅動的馬英九，不算巡邏。LESSONS `babel-amplifies…` 修補候選 (b)「給巡邏一條 routine」仍缺，走 ROUTINE.md 要營運機建排程。
- [ ] pending（小，任何 session）— `knowledge/ar/People/ma-ying-jeou-…` 30 秒概覽裡混了一個韓文「한쪽」（babel 的跨語言污染），重譯時會一起洗掉；若重譯拖過一週，手改。

## Beat 5 — 反芻

這輪最值得記的一點很小：issue 開的是「兩條腳註對不上」，兩輪維護班覆驗也都盯著腳註，而整篇最嚴重的錯——把在世的人寫成辭世——沒有腳註。它沒有出處，所以「腳註對不對」這把尺根本量不到它；它在 30 秒概覽裡，是整篇被讀最多次的一句。Quick mode 的單位是腳註，Full mode 的單位是原子，差別在這裡：抽查腳註能抓到「引來源說了它沒說的話」，抓不到「什麼來源都沒引、直接說了一件不存在的事」。一句話沒掛腳註，在形式閘門眼裡是零風險，實際上它是最沒人替它作證的那句。這跟早上「閘門守完整不守歸屬」是同一件事的另一面：那條講掛了來源但掛錯事件，這條講根本沒掛所以誰都沒去看。

另一個是 agent 的自評 B 段：小林村 474 對 462、握手 16 秒對 15 秒——兩個來源各說各的，都是真來源。查證做到底會發現不只有「對」跟「錯」，還有「兩個對的來源不一致」這一格，而文章目前沒有任何語法能表達它，只能挑一個。

🧬

---

_v1.0 | 2026-09-18 15:20 +0800_
_session semiont-heartbeat — 下午排程心跳；馬英九 FACTCHECK Full 落地、PR #1747 merge、探測器黃燈重點亮、地圖標記確定性_
_誕生原因：14:30 排程觸發；issue #1729 從 09-14 等的「FACTCHECK Full mode」正好是本輪的 mode_
_核心洞察：(1) 腳註抽查抓得到「引來源說了它沒說的話」，抓不到「什麼都沒引、直接說了不存在的事」——最嚴重的錯常常沒有腳註可以對不上 (2) 未審初稿 × 多語投射那一格第二次命中，這次是政治人物條目、錯誤率 40% (3) 每個資料刷新 commit 帶 6,000 行隨機座標噪音，三輪心跳沒人看 diff 才發現_
_LESSONS-INBOX 候選：無新條目；`babel-amplifies-source-hallucinations…` bump vc=2_
