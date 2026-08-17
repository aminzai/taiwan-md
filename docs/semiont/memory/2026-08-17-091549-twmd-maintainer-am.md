---
session_id: '2026-08-17-091549-twmd-maintainer-am'
session_span: '08:35 → 09:20 +0800'
trigger: 'cron routine twmd-maintainer-daily (am 08:30)'
observer: 'none (cron)'
beat_coverage: 'Stage 1-4 (MAINTAINER-PIPELINE)'
---

✅ BECOME ack: mode=review→**強制升 full**（High-stake #1：PR triage 71 ≥ 5）/ 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# 2026-08-17-091549-twmd-maintainer-am — 七十一個 PR 裡有五十九個沒在等我，而擋住其餘的東西有一半是我們自己種的

> session twmd-maintainer-am — cron maintainer 巡邏
> Session span: 08:35 → 09:20 +0800（約 45 分鐘，4 commits）

## 觸發

Cron 08:30 開跑。Stage 1 掃到 **71 個 open PR**（67 個來自 idlccp1984），命中 High-stake #1 強制升 Full mode。昨天的 maintainer 記的是「九個 PR 連三天敗在同一道閘門」，今天這個數字變成 65/67。

## 兩個把問題放大的計數錯誤，都是我自己的

**一、59 個 PR 是 draft，我一開始把它們當佇列。**

`gh pr list` 的 71 是「開著的 PR」，不是「在等審的 PR」。實際 non-draft 只有 **12** 個，其中 idlccp1984 佔 8 個。59 個 draft 在流程上代表投稿者自己說「還在寫」，不該被計進 backlog，更不該被讀成「維護積壓」。昨天那句「九個 PR 連三天敗在同一道閘門」很可能也含了 draft。

這是 REFLEXES #82 的變體：**量 open PR 數不等於量待審量**，而前者是儀表板上最容易拿到的那個數字。

**二、我用 grep 數 hard 違規，漏掉沒有行號的那些。**

批次盤點時我數 `^\s+hard L`，而「全形分號超硬門檻」這條違規的 line 是 None，印出來是 `hard LNone`，被我的計數漏掉。於是 #1376 被算進「可以 merge」那一疊，我 merge 了它，main 變紅，幾分鐘後我把內容收回（`e7dfe182a`）。

改用 JSON 的 severity 欄位重數之後，真實狀況是：**8 個 non-draft PR 沒有一個通過部署閘門**，即使跑完完整 heal 鏈。製造數字的人最容易被自己的數字騙（REFLEXES #59）——這次騙到的是我自己的 merge 決策。

## 追上游：擋住這批的東西，有一半是我們自己的工具寫進去的

65 個 PR 敗在 frontmatter-gate。逐層拆下去，最大宗的 blocker 是「缺 `subcategory`」（26 件）。而 `assign-subcategory.cjs` 這支能自動補的工具**從以前就在 `scripts/tools/` 裡，從來沒有被 `contributor-pr-heal.py` 那條 heal 鏈叫過**。工具造出來了，沒有接到需要它的路上（REFLEXES #91）。

接上去之後只解掉 11/29，剩下 18 個 NO MATCH。追進去發現更難看的三層：

1. **解析 `SUBCATEGORY.md` 的 regex 用 `\s*$` 收尾**，於是 `### 👥 People（人物）— 已大致完成` 這行整節認不出來。People 從來沒被解析過，它底下 13 個子分類全被歸進上一個 current（Nature）。
2. **`_KEYWORD_BOOSTS` 有 8 個標籤是 SSOT 裡不存在的名字**（People 的「政治人物」「企業家」、Nature 的「生態保育」「地質地形」等），而 auto-heal 會把它們**寫進投稿者的 frontmatter**。
3. **`allowed_subcategories()` 又把那些標籤 union 進「合法清單」**——工具自己製造漂移、工具自己認可，外面沒有任何東西在對賬。

所以「投稿者亂填 subcategory」這個表面，有一部分根本是我們自己填的。

三個都修了，補 5 條測試（`8ba8c6726`）。

## 新增 subcategory-valid 檢查，以及為什麼它只能是 WARN

`curation` 欄位有驗舉值（非法值 → HARD），隔壁的 `subcategory` 只驗欄位在不在、不驗值存不存在。同一份 frontmatter 兩把尺（REFLEXES #83）。補了 `subcategory-valid`。

上線前先拿全庫 914 篇 dogfood（REFLEXES #66），結果 **211 篇 / 135 個相異取值** 會命中。看清單就知道方向反了：`Geography 縣市` 22 篇、`People 音樂` 13 篇、`People 流行人物` 11 篇——這是 **SSOT 自己漏收了實際在用的子分類**，不是那 211 篇寫錯。設 HARD 等於拿分類體系的缺口去擋文章，而且會當場讓 main 變紅。

所以定 WARN：讓原本完全不可見的漂移看得見，至於 135 個取值哪些收進 SSOT、哪些改掉，動到 211 檔，命中 §自主權邊界，留哲宇。

**這是今天唯一一次閘門校準沒有出錯的地方**，而它之所以沒出錯，是因為我在定嚴重度之前先跑了真實產出。前面兩個計數錯誤都是沒先驗就下結論。

## 實際動到的東西

| 動作          | 對象                                                                                      | 結果                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| merge         | #1408 rhosiqs 英文散文潤稿                                                                | ✅ MERGED，hard=0 warn=0；17.2KB→14.1KB 但 sections 10→10 / footnotes 5→5 / URLs 5→5，ratio OK |
| merge → 收回  | #1376 排隊                                                                                | ⚠️ merge 後發現 hard=1（全形分號 70 > 12），內容收回，PR 留 MERGED 狀態，原因寫在留言          |
| 工具修復      | taxonomy_subcat 三缺陷 + heal 鏈接上 assign-subcategory + 新增 subcategory-valid + 5 測試 | ✅ `8ba8c6726`                                                                                 |
| 累積式回覆    | idlccp1984 整批 8 個 non-draft                                                            | ✅ 一則，含逐 PR 阻塞數字表、draft 狀況說明、#1376 收回致歉                                    |
| 回覆 + 排佇列 | issue #1440 選單「數據」                                                                  | ✅ 已回覆 + `needs-observer-review` + OBSERVER-QUEUE #31                                       |

## 給 idlccp1984 的那則為什麼寫成一則

pipeline §Step 3.7 burst 期規則：同 contributor 48hr 內 ≥3 PR 不逐 PR 發建議。他兩天投 67 個，逐 PR 貼等於一次送 8 份通知。改成一則講清楚三件事：draft 狀況（59 個沒進佇列，可能是他不知道）、兩個共同 blocker 的逐 PR 數字表、以及我 merge 又收回 #1376 是我算錯不是他的內容有問題。

**內容本身沒有被退。**這批取材是好的——排隊、藍白拖、台北橋機車瀑布正是站上缺的那種「日常但沒人好好寫過」的題目。卡住的兩件事（圖片熱連結、全形分號密度）都是機械項目，而昨天的 maintainer 已經把它們補進 CONTRIBUTING 了（第 395/397 行）。所以文件缺口是關的，**還開著的是送達**：frontmatter-gate 對 fork PR 的留言步驟因唯讀 token 必定失敗，說明只落在 job summary 裡，投稿者多半不會去點。這是 LESSONS `gate-explains-into-a-dead-channel`（8/13 記的）四天後仍然成立。

我沒有替他改那 58 個分號。那等於大幅改寫投稿者的散文去滿足一個計數器，是 `vi-delegation-wave` 那條教訓講的「用弄壞內容的方式讓閘門閉嘴」。

## 順帶記一個閘門設計問題

全形分號硬門檻是**絕對值 12，不隨篇幅正規化**。49KB 的長文跟 10KB 的短文吃同一個數字，長文結構性吃虧（#1376 是 70，但它也是這批裡最長的一篇）。沒有當場改閾值——那是 §自主權邊界。記在這裡等 distill 判要不要升 LESSONS。

## Quality gate

| Gate                                                       | 狀態                                                                                                              |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee                     | ✅ 4 個全有 label，全部有維護者回覆                                                                               |
| open PRs ≤ 5d age 都有 review comment                      | ✅ non-draft 12 個：idlccp1984 8 個走累積式一則、#1408 已 merge+致謝、#1325/#1430/#1365 在 OBSERVER-QUEUE #29/#30 |
| broken-link ratio < THRESHOLD_PERCENT                      | ⏭️ 本 cycle 未跑（PR 追上游佔滿預算）                                                                             |
| build green                                                | ✅ pre-push 全站 ci-deploy mirror 全綠；收回 #1376 後 main 恢復                                                   |
| BECOME ACK 一行記憶體頂                                    | ✅                                                                                                                |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                        | n/a — 本 cycle 有真實 backlog，vc 歸零                                                                            |
| 有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修 | ✅ 修了 taxonomy 三缺陷 + heal 鏈 + 新檢查；#1440 明確寫出為什麼進佇列不當場改                                    |

## Handoff 三態

繼承上一 session（`2026-08-17-071012-twmd-feedback-triage`）：

- [x] ~~pending（給 `twmd-maintainer-am`）— #1440 選單「數據」→「資料」用詞建議~~ retired by 本 session：對照 TERMINOLOGY.md 確認我方 SSOT 站在讀者這邊（第 42 行 tier B），但區段命名跨 13 語系屬品牌識別 → OBSERVER-QUEUE #31 + 已回覆讀者
- ⏳ blocked（給哲宇）— OBSERVER-QUEUE #28 第三人指控信，兩件待決原封不動。原樣延續
- [ ] pending（給哲宇）— OBSERVER-QUEUE #29 德文（#1325/#1430 兩個 PR 等這個）、#30 KENJI 人物門檻（#1365）、SPORE-INBOX pending 45 三選一、#1264 seo-meta 門檻、#1184 justfont 白名單。原樣延續
- [ ] pending（給下次 review session）— REFLEXES #86-91 六條新編號尚未經第二個獨立 session 驗證使用。原樣延續

本 session 新 handoff：

- [ ] **pending（給哲宇，新）— OBSERVER-QUEUE #31**：選單「數據」→「資料」，以及要不要讓 `src/i18n/**` 進 terminology 檢查。後半是純工具改動，若只拍板那半，任何 session 可執行
- [ ] **pending（給下次 maintainer）— idlccp1984 那 8 個 non-draft PR 的圖片熱連結**：共約 46 張外部圖需走 `image-ingest.mjs` 收進 `public/article-images/`。這件事**投稿者做或我們做都可以**，但每張要填 credit / license / source-url，是逐張的授權工作不是批次替換。若投稿者沒動作，下次 cycle 可考慮挑 1-2 篇示範一次給他看
- [ ] **pending（給 distill）— 全形分號硬門檻不隨篇幅正規化**：絕對值 12 對長文結構性不利。本 cycle 觀察到 vc=1，看之後會不會再撞
- [ ] **pending（給下次 maintainer / routine-audit）— `gh pr list` 的計數要排除 draft**：本 cycle 與昨天的 cycle 都把 draft 算進 backlog，導致 alarm 放大。這是 REFLEXES #82 變體，可能值得在 MAINTAINER Stage 1.3 加一句「先分 draft / ready 再報數」

🧬

---

_v1.0 | 2026-08-17 09:20 +0800_
_session twmd-maintainer-am_
