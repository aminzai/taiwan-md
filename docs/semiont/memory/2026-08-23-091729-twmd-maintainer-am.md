---
session_id: '2026-08-23-091729-twmd-maintainer-am'
session_span: '2026-08-23 08:30–09:17'
trigger: 'cron routine twmd-maintainer-daily'
observer: '無（cron context）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4'
---

# twmd-maintainer-am @ 2026-08-23 — 六篇卡在同一層，那一層的閘門自己缺了一半

✅ BECOME ack: mode=review→**強制升 Full**（PR triage ≥ 5，ready=20，命中 §Step 0 high-stake #1）/ 8 organ 最低=🛡️ 免疫 59↑（即時 consciousness-snapshot.sh，yellow「漂移 — 多維度退化中」自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

> 路徑註記：routine prompt 寫 `/Users/cheyuwu/Projects/taiwan-md`，本機實際在 `/Users/musebase/Projects/taiwan-md`（同一棵樹）。

---

## Stage 1: SCAN

| 項目               | 值                                                                        |
| ------------------ | ------------------------------------------------------------------------- |
| open PR（ready）   | 20                                                                        |
| open PR（draft）   | 7（另計，不進 backlog 與空場 vc）                                         |
| open issue         | 4（#1440 / #1389 / #1184 / #615）                                         |
| past 24hr commits  | 10 條 routine fire（feedback-triage ×2 / 週日反思鏈四條 / embeddings 等） |
| past 48hr commits  | 約 170 條（含 8/21-8/22 兩輪 maintainer 合併的 60+ 投稿）                 |
| build status       | 🟢 green（Deploy to GitHub Pages 最近三次 success）                       |
| i18n smoke         | 🟢 green（最近一次 8/20 success）                                         |
| immune organ score | 🛡️ 59↑（yellow，chronic 自 07-05）                                        |
| CI armed（27 PR）  | 26 ARMED / 1 UNARMED（#1365，第四次復發，屬 OQ #30 保留案）               |
| broken-link ratio  | 0.27% < 7% 門檻 ✅（all-langs 0.25%）                                     |

**Ready 20 篇的分流**：6 篇命中 OBSERVER-QUEUE 保留案（#1325/#1430 德文=OQ #29、#1365=OQ #30、#1453=OQ #36、#1484=OQ #34、#1491 館長陳之漢），其餘 14 篇為本 cycle 可動 backlog。

---

## Stage 2-3: TRIAGE + ACT

### 14 篇全部 MERGED

**乾淨直接 merge（5）**：aminzai 四篇日文譯本（#1566 三商 / #1567 網路社群遷徙史 / #1568 毒馬鈴薯 / #1578 外送專法）＋ iigmir #1579（英法西地名順序改成小地名在前，加一段台中大肚 7-11 錄音）。

**merge 後 heal（1）**：三篇日文譯本的 `author` 被改寫成 `Taiwan.md Translation Team`，全站 818 篇日文譯本只有這三篇這樣寫。最要緊的是〈台灣網路社群遷徙史〉原文作者是貢獻者 **p3nchan**，換成團隊名等於他的署名在日文版消失。三篇改回原文署名（`0dc2d0e32`）。

**P1 推對方分支後 merge（9，idlccp1984）**：`maintainerCanModify: true`，六篇的修補直接 push 進投稿者分支，CI 轉綠後 `gh pr merge`，九燈全 MERGED。

| PR    | 篇名     | blocker                              | 處置                                                                          |
| ----- | -------- | ------------------------------------ | ----------------------------------------------------------------------------- |
| #1569 | 台灣漆器 | 3 張路徑指向沒上傳的檔＋2 張熱連結   | 五張全收進庫（照他自己留的來源 URL 抓文化部 ×2、高史博 ×1；Wikimedia CC0 ×2） |
| #1570 | 鹽水蜂炮 | 全形分號 15 > 12                     | 拆句號                                                                        |
| #1571 | 全民健保 | 3 張 Unsplash 熱連結＋「數據庫」     | 移圖＋改「資料庫」                                                            |
| #1572 | 87 水災  | 2 張路徑不存在，且授權是 CC BY-NC    | 移除（NC 與站方 CC BY-SA 4.0 不相容）                                         |
| #1573 | 蔡培火   | 落在 `knowledge/` 根目錄＋分號 23 處 | `git mv` 進 People/＋拆句號                                                   |
| #1574 | 電鍋     | 3 張典藏網熱連結                     | 移除（來源頁查不到可再利用授權）                                              |
| #1575 | 台灣黑熊 | （PR 側綠，全站掃描才紅）            | 一張角括號包住的 Commons URL 收進庫                                           |
| #1576 | 貓眼石   | 6 張熱連結                           | 2 張 Wikimedia CC 收進庫、4 張館方圖移除（他自己註明「不宣稱 CC」）           |
| #1577 | 丹丹漢堡 | 無                                   | 直接 merge                                                                    |

九篇合併後補 `curation: incubating`（`998b8bdb1`）。

### 追上游：六個症狀，一個根因

修到第三篇才停下來問「這幾則是不是同一個地方破的」。答案是：**`image-health` 對內文圖片有熱連結硬門檻，但 frontmatter 的 hero 圖只驗本地路徑存不存在，外部網址整條分支根本不進去。**

所以文章中段的圖被擋下，而分享出去會被看到的那張卡片圖、OG 圖，沒有任何東西在守。

修法把 hero 拉進內文那條規則裡（`f89314e27`）。**Wikimedia 白名單一個字沒動**——沒有調任何門檻，只是讓既有規則兩條路徑都適用，因此不落在 §自主權邊界 的閾值調整。

雙向 dogfood：塞一個 `https://example.com/fake.jpg` 進 hero → 如實紅；換成 `upload.wikimedia.org` → 照常綠。全站掃描命中 4 篇（黃土水／烏魚子／燒臘便當／阿美族年齡階級），四張卡片圖都是熱連結且來源頁無可再利用授權（燒臘便當那張是 YouTube 影片縮圖），同 commit 清掉，全站回到 0 hard。

**這個形狀 OBSERVER-QUEUE #31 已經記過一次**：文章層有 terminology 閘門、UI 字串層沒有，而導覽列是全站曝光最高的字，靠讀者 #1440 回報才發現。兩次的成因一樣：規則只掛在寫它的人當時在看的那條路徑上。

### Issue 處置

- **#1389**（豆漿與早餐店合併）：8/16 已完整判斷、8/20 已落 ARTICLE-INBOX P2 EVOLVE 並寫明邊界切法，投稿者無新 follow-up → Step 2.4 重複回應檢查 **SKIP**。本 cycle 不重複回覆是判斷，不是省略。
- **#1440 / #1184**：OQ #31 / #35 保留案，等哲宇。#1184 的修法在 justfont 後台，只有帳號持有人按得下去。
- **#615**：umbrella 追蹤 issue，無新進度。

### Draft 7 篇

#1407/#1411（OQ #32）、#1450（OQ #33）為保留案。#1395/#1401/#1451/#1452 四篇 PR 說明都還是未填模板，但三個 ground-truth 訊號未全中（#1401/#1451/#1452 建立後有 push），依 §1b「任一不中＝尊重還在寫」**不代轉 ready**。四篇零維護者留言，補一則說明 draft 狀態與分割鈕記憶行為。

### 回覆

- #1569 idlccp1984 九篇累積式一則（burst 紀律，不逐 PR 各發）：圖片入庫工具用法、授權可收/不可收的分界、Unsplash 那三張為何要撤（拍的不是台灣，圖說卻寫台灣）。
- #1578 aminzai 日文回覆（署名還原的理由）。
- #1579 iigmir 中文回覆。
- #1395 draft 說明。

---

## Stage 4: WRAP

### Quality gate

| Gate                                   | 結果                                                    |
| -------------------------------------- | ------------------------------------------------------- |
| open issues 都有 status label/assignee | ✅ 4 篇皆已分類（2 保留案 / 1 已落檔 / 1 umbrella）     |
| open PRs ≤ 5d age 都有 review comment  | ✅ 本輪 14 篇全 merge＋回覆；draft 四篇補說明           |
| broken-link ratio < 7%                 | ✅ 0.27%                                                |
| build green                            | ✅                                                      |
| BECOME ACK 一行記憶體頂                | ✅                                                      |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ n/a — 本輪 14 篇真 backlog，vc 歸零                  |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ 修掉閘門根因（`f89314e27`）＋ 4 篇既有文章卡片圖清理 |

### LESSONS-INBOX

新增兩條：`highest-exposure-slot-is-the-one-with-no-gate`（本 cycle 根因，同 REFLEXES #87 第二個獨立 instance）、`base-language-in-sibling-file-makes-every-translation-look-missing`（`check-ui-language.mjs` TABLE_DRIFT 對 `/search` 十二語切檔方式報 11 行假陽性，本 cycle 未修，理由寫在條目裡）。

### Handoff 三態

繼承上一 session（`2026-08-23-070907-twmd-feedback-triage`）：

- [ ] pending（不屬本 routine，原樣傳遞）：`b78ee4f5` 第十一次會再出現，照 HG13 讀完全文再 `--exclude`
- [ ] pending（不屬本 routine，原樣傳遞）：OBSERVER-QUEUE #28 那格繼續只推兩處數字
- [x] ~~#1466 鐵牛破折號、#1451／#1452 兩個 draft、#1453 學測模板~~ 本輪處置：#1466 已於 8/22 merged；#1451/#1452 draft 判定「尊重還在寫」不代轉，已留說明；#1453 屬 OQ #36 保留案
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #29／#30／#31／#32／#33／#34／#35／#36

本 session 新 handoff：

- [ ] pending：黃土水／烏魚子／燒臘便當／阿美族年齡階級 四篇的卡片圖已移除，待補授權清楚的替代圖（走 REWRITE 或 image-ingest，不是維護巡邏尺寸）
- [ ] pending：`check-ui-language.mjs` TABLE_DRIFT 對 `search.*` 的 11 行假陽性（zh-TW 在 `ui.ts`、11 語在 `search.ts`）——修法要動 i18n loader 合併順序，需要一個能驗證中文搜尋頁不掉字串的 session
- [ ] pending：#1365 第四次 UNARMED（每次新 push 都要重新核准，核准不是對投稿者永久生效）；本輪未核准，因該 PR 屬 OQ #30 保留案
- ⏳ blocked — 等哲宇：OQ #37 `/search` 完整結果頁**實際已於今晨 02:45 上線**（issue #1496 已 close），佇列那格的問句已過期，建議下一輪 feedback-triage 或哲宇 review 時就地更新狀態

---

_作者：Taiwan.md 🧬_
