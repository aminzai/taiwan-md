# 2026-08-21-181117-twmd-maintainer-am — 投稿者自己把模板修好了，於是我終於有時間去讀那個沒人回報的 bug

> ✅ BECOME ack: mode=review→**強制升 Full**（48 ready PR ≥ 5，BECOME §Step 0 High-stake #1）/ 8 organ 最低=免疫 59（漂移，自 2026-07-05，即時 consciousness-snapshot.sh）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS
> session twmd-maintainer-am — cron routine（排程 08:30，實際 18:11 才 fire）
> Session span: 18:11:17 → 18:39 +0800
> 資料來源：`git log %ai` / `gh pr list` / `zh.wikipedia.org` API

## 觸發與晨鏈延遲

排程 08:30，實際 18:11 開工。整條晨鏈今天都睡過頭：routine-sync 與 feedback-triage 的 memory 時間戳是 18:08，跟我差三分鐘。data-refresh-am 沒跑，所以甦醒時 groundtruth 讀到的 dashboard 齡 35 小時。

**這件事 feedback-triage 那條已經診斷完並escalate 了**（推測機器睡著、排程在喚醒後一起 fire），照 REFLEXES #74 / #80 我不重複開單，只在這裡記一筆座標。開工時另外兩條 routine 還在同一個工作樹上寫檔，所以本 session 全程在 worktree 裡跑（`.worktrees/20260821-…-maintainer-am-batch`），commit 範圍只碰自己的檔。

## Stage 1 SCAN

| 項目              | 讀數                                                                                                           |
| ----------------- | -------------------------------------------------------------------------------------------------------------- |
| open PR           | 55（ready 48 / draft 7）→ 收工 17                                                                              |
| open issue        | 5（fresh 1：#1496）                                                                                            |
| 過去 24hr commits | 0（8/21 開工前一筆都沒有）                                                                                     |
| 過去 48hr commits | 128（全部落在 8/20）                                                                                           |
| build             | ⚠️ 本機 `npm run build` 紅 — `marked-cjk-friendly` 在 package.json 但不在 node_modules（環境缺件，非本次改動） |
| CI armed          | 55 掃過：UNARMED 1（#1365，第三次）/ NO-WORKFLOW 0                                                             |
| 免疫器官          | 59 yellow，漂移中，自 2026-07-05                                                                               |

## 這批投稿跟前幾批不一樣

41 篇 idlccp1984 新投稿，機械稽核跑完**31 篇 hard=0**。`author` 沒有一篇偽造、`featured` 沒有一篇自設 true、全形分號大多是 0。前幾批要一篇篇補的三個欄位，這次從 #1500 之後他自己填對了——缺欄位的只有最早那三篇（#1497/#1498/#1499，02:0x–02:3x 送出），看得起來是他中途把模板修好了。

昨天那支紅旗 healer（`c920ebe91`）今天一次都沒被觸發。這不是工具沒用，是它要防的東西這批沒出現。

**merge 38 篇**：30 篇直接過閘門，6 篇 P1 推 heal 進對方分支後合併（#1497 補 subcategory 文學＋分號 22 處／#1498 補教育＋15 處／#1499 補戰後與威權＋21 處／#1501 半形冒號／#1506「下載量」改「下載次數」／#1509 移除三張授權不明熱連結圖），另 #1503（aminzai 日文翻譯，ratio 1.51、段落腳註 URL 21→21 / 22→22 全保）與 #1517 一併 merged。

**#1517 與 #1519 是同一篇 `美援.md`，逐位元組相同**。合併 #1519、#1517 也標 MERGED 保住譜系，沒有 close——close 是拒絕不是收割（§1b）。

## 查維基的方法本身改了一次，結果推翻我兩個方向的預設

七篇 People 條目要過 §人物知名度門檻。我第一版用的方法是數腳註網域裡有沒有 `wikipedia`——**那是代理訊號**（REFLEXES #82）：`commons.wikimedia.org` 的圖片檔會被算成「有維基條目」，而真的有條目但文章沒引維基的會被算成沒有。

改成直接打 `zh.wikipedia.org` API 查，兩個方向都被推翻：**六指淵與尼克星我原本判不過，實際都有條目**；而張忠仁那篇「wiki refs: 3」全部是 commons 圖片檔。

結果：理科太太（中央社 ×3／Taipei Times／央廣）、六指淵（親子天下／SETN／udn）、尼克星（民視／ETtoday）、廖添丁（國史館台灣文獻館／NMTH 館藏）、鍾肇政（國立臺灣文學館／客委會）、張忠仁與張忠義（報導者／光華／台大醫院）——六篇照門檻收。

**#1525 三度C 沒收**：維基查無條目，八個腳註四個指向 `m9535453m.com`，那是傳主自己的製作公司作品頁。這是 OBSERVER-QUEUE #30 的第五例（前四：#1365 KENJI／#1395 黑貓老師／#1401 Cheap／#1471 蔡黑皮），已補登並把「維基條目用 API 查、不用腳註推」寫進那則的建議裡。

**#1524 尼克星是我今天最靠近邊界的一次收**。文章有一段寫他在跨境直播被中國網友要求「回歸中國」時的回應，引了民視。收它的理由是主體是創作者的內容實作、政治只佔十五個 H2 裡的一個，而且那段自己寫了「不能把尼克星的表態擴大解釋成完整政治論述」；跟 #1484 蔣經國、#1491 館長那種「主體就是那個人的立場軌跡」不同型（那兩篇留給哲宇）。這個判斷寫在這裡是為了讓它便宜地被推翻。

## Issue #1496：回報的是看不完，底下是一個在說謊的數字

讀者說搜「台北101」看到「…還有 18 篇」但沒有入口。追進 `Layout.astro` 之後發現那個 **18 本身是錯的**。

`_doSearch()` 先撈 200 筆、用相關度 cutoff 過濾、**`.slice(0, 30)` 硬砍**，再回傳。渲染端取前 12 筆，然後拿 `matches.length - 12` 當「還有 N 篇」——`matches` 已經砍過，所以那個數字**永遠不會超過 18**。八十篇相關的查詢，畫面告訴你三十篇。**它量的是搜尋器自己的上限，不是語料庫**（REFLEXES #82 在使用者介面層的一個新面孔）。GA4 的 `search_query` 結果數吃同一個變數，所以搜尋分析數據也被同一個上限壓平了。

修了兩件（`98291fd89`）：命中總數改在 cutoff 之後、slice 之前算；面板從 12 筆改成把手上 30 筆全渲染——`.search-results` 本來就有 `max-height: 400px; overflow-y: auto`，捲軸一直在，只是被 12 筆上限餓著。

**沒做**：讀者要的 `/search?q=…` 獨立頁（排序／時間篩選／URL 狀態／分頁）。理由寫進 issue 了——13 條語言路由、三種時間排序需要索引帶進發布日與更新日兩個目前沒有的欄位，那是功能專案不是 heal。issue 保持開著當規格書，排程留哲宇，我沒有承諾時程（§外向留言分層）。

## 驗證這次是跛的，值得記

pipeline 說 UI 改動要「真的開瀏覽器看一眼」（§1c／REFLEXES #69）。**routine session 結構上做不到**：`preview_start` 對無人值守的 session 直接拒絕。退一步想跑 build gate，本機 `npm run build` 又因為 `marked-cjk-friendly` 沒裝而紅——**pipeline 指名的兩條驗證路徑，今天對這台機器上的 cron session 都關著**。

實際用的替代：把改動前後的計數邏輯抽出來在 node 跑（80 筆語料下舊版報 30、新版報 80），加上把 inline script 抽出來 `node --check`。這比看畫面弱，因為它驗的是我寫的邏輯照我想的跑，不是讀者真的看到對的東西——同一顆腦的尺（REFLEXES #65 (f)）。已寫 LESSONS。

## Stage 4 Quality gate

| Gate                                   | 結果                                                |
| -------------------------------------- | --------------------------------------------------- |
| open issues 都有 status label/assignee | ✅ #1496 補 enhancement                             |
| open PRs ≤ 5d age 都有 review comment  | ✅ 批次一則（burst 紀律）＋ issue 一則              |
| broken-link ratio < 7%                 | ⏭️ 本 cycle 未跑（時間排擠，非結構性 backlog）      |
| build green                            | ❌ 本機紅（環境缺件，非本次改動）；CI 端 38 PR 全綠 |
| BECOME ACK 一行記憶體頂                | ✅                                                  |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | n/a — 本 cycle 48 ready PR，vc 歸零                 |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ #1496 修兩項，commit `98291fd89`                 |

## Handoff 三態

繼承上一 session（`2026-08-20-084151-twmd-maintainer-am`）：

- [x] ~~#1466 鐵牛破折號等投稿者三天~~ — 仍 open 未回應，但已過三天觀察窗，下輪判斷要不要代改（我不再重複計時）
- [ ] pending（原樣傳遞）：`b78ee4f5` 檢舉信 — 今天 feedback-triage 已第八次攔下，不屬本 routine
- [ ] pending（原樣傳遞）：OBSERVER-QUEUE #28 偵測器與回覆決定仍等哲宇
- [ ] pending：#1452 / #1451 兩個 draft 仍無新 commit，繼續照 v2.8 尊重「還在寫」
- [ ] pending：`punct-cleanup --fix` 全站 legacy 清償仍等哲宇排優先序（>50 檔命中 §自主權邊界）
- [ ] pending：#1453 學測模板孤兒 template 等投稿者回覆協作切法

本 session 新 handoff：

- [ ] pending：**本機 `npm run build` 紅** — `marked-cjk-friendly` 在 package.json 但 node_modules 沒有。我沒跑 `npm i`（平行 session 共用 node_modules，不在別人跑的時候動共享環境）。下一個獨佔 session 補裝，補完順手確認 routine 還跑不跑得動 build gate
- [ ] pending：**#1365 第三次 UNARMED**，本輪已核准 head sha 那兩批 run。8/16、8/19、8/21 三次同型 = 「核准非永久」已 vc=3，`pr-ci-armed.sh` 仍掛在 maintainer 手跑、UNARMED 不會主動叫（LESSONS 2026-08-19 §待補 原樣未動）
- [ ] pending：#1496 的 `/search` 頁是功能專案，issue 開著當規格書，等哲宇排程
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #30（人物門檻，**今天累積到第五例** #1525）／#34（#1484 蔣經國、#1491 館長）／#33（#1450、#1483 覆寫查證文）／#32（#1407、#1411 About 自述）／#29（#1325、#1430 德文兩批 59 檔）

---

_session: 2026-08-21-181117-twmd-maintainer-am | 2026-08-21 18:39 +0800_
