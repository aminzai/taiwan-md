---
title: 'Design: 共編規則——對外貢獻規則與對內進化 gate 分流'
description: 'EVOLVE Mode 4 設計報告：解 OBSERVER-QUEUE #16 進化分數對 SEO 型候選的結構性偏誤，並把今天三條投稿判例寫成對貢獻者友善的共編規則。方案發散、定案理由、CONTRIBUTING.md 與 EVOLVE-PIPELINE.md 兩層條文草案、實作清單、驗收與風險。'
type: 'design-report'
status: 'implemented'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-154128-fortnight-review'
related:
  - '../CONTRIBUTING.md'
  - '../docs/pipelines/EVOLVE-PIPELINE.md'
  - '../docs/pipelines/MAINTAINER-PIPELINE.md'
  - '../docs/semiont/OBSERVER-QUEUE.md'
  - '../docs/pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md'
  - '../docs/editorial/EDITORIAL.md'
  - '../docs/semiont/ARTICLE-INBOX.md'
  - '../reports/design-curation-tier-2026-08-04.md'
  - '../reports/domain-expert-cocreation-574-2026-06-30.md'
  - '../reports/fortnight-deep-review-2026-09-05.md'
  - '../docs/semiont/MANIFESTO.md'
---

# 設計報告：共編規則——對外貢獻規則與對內進化 gate 分流

> session：2026-09-05-154128-fortnight-review
> 觸發：哲宇對 [OBSERVER-QUEUE #16](../docs/semiont/OBSERVER-QUEUE.md) 的回答「完整制定更完整的共編規則，讓未來大家好依循」，追問後選 C「兩層都要，一對外一對內互指」。
> 流程：EVOLVE-PIPELINE Mode 4（THINK → DIVERGE → REPORT → IMPLEMENT）。本報告是 REPORT 相產物，實作停在本報告等哲宇拍板。

---

## 一、目標與為什麼是現在

一句話：把「貢獻者怎麼參與既有文章」與「Taiwan.md 自己的候選怎麼選、怎麼分流過 gate」寫成兩份可依循、互相指向的規則，對外的一份進 CONTRIBUTING.md，對內的一份進 EVOLVE-PIPELINE.md。

為什麼是現在。今天同一個 fortnight-review session 裡，維護判斷連續三次撞到同一種缺口。人物條目要不要收自媒體時代的表演者，KENJI、黑貓老師、Cheap、蔡黑皮、三度C 五案同判 close（PR #1365 #1395 #1401 #1471 #1525）。投稿者整篇覆寫已查證成品該怎麼收，陳士駿、台灣便利商店文化、台灣高鐵三案（PR #1630 #1450 #1483）拍板改走 EVOLVE 接住加 Co-authored。投稿者用 Taiwan.md 第一人稱寫自述文該不該進 About/，兩案（PR #1407 #1411）拍板不收。三條判例當場寫進了 MAINTAINER-PIPELINE，但那是一份給維護流程看的內部文件，投稿前不會有人先讀完它。

同一時期投稿量體正在變大：兩週 94 個 PR 合併，中文文章淨增 128 篇，貢獻者從 74 個增加到 75 個。同型案例會反覆出現，沒有寫成對外文字的規則，下一個 idlccp1984、下一個像聲景投稿者 nistoreyo 那樣的領域專家，只能重新從零撞一次同一道牆。

同一天，OBSERVER-QUEUE #16 也被正式回覆：進化分數 v2.0 算 BIM 英文版 metadata 58.2 分，低於 60 分 gate，但它 100% 命中 EVOLVE 行動表裡 🟠 SEO 優化型「高曝光＋低 CTR＋品質 OK」的觸發條件，ROI 最高的行動（5 分鐘一篇）被一把為另一種行動類型設計的尺擋住。哲宇的回答把這兩件事接在一起，同時把貢獻者怎麼參與跟 Taiwan.md 自己怎麼進化，定案成兩份互相看得見對方的規則。

---

## 二、現況盤點

### 2.1 CONTRIBUTING.md：對外清單逐項對照

CONTRIBUTING.md 最後一行寫著「最後更新：2024-03-17」，這份文件本身已經兩年多沒被實質改動，同一段時間站上文章從幾十篇長到 1,118 篇。逐項核對哲宇列的九個對外項目：

| 項目                    | CONTRIBUTING.md 現況                              | 缺口                                         |
| ----------------------- | ------------------------------------------------- | -------------------------------------------- |
| 補充 vs 覆寫判準        | 未提及，只有「歡迎貢獻更多內容」的籠統鼓勵        | 全缺，今天三案判例只落在 MAINTAINER-PIPELINE |
| Co-authored-by 掛法     | 未提及                                            | 全缺                                         |
| 人物條目知名度門檻      | 未提及，§內容審查只講事實查核與文化敏感性         | 全缺，五案判例同樣只在 MAINTAINER-PIPELINE   |
| About/ 只收第一人稱     | 未提及                                            | 全缺                                         |
| SEO metadata 修改怎麼提 | 未提及，EDITORIAL.md 有品質標準但兩份文件互不連結 | 缺                                           |
| curation 三態           | 已有（§🌱 你的文章 merge 之後），是唯一覆蓋的項目 | 講了進化中怎麼來，沒講怎麼升級到已查證       |
| 新條目 frontmatter 必填 | 有文章結構範本，必填規則散在後面 §3 品質檢查      | 部分覆蓋，位置分散                           |
| 圖片授權規則            | 有（§🛠️ 工具與資源），但只在推薦工具段落順帶一句  | 部分覆蓋，位置不顯著                         |
| 用語 TERMINOLOGY tier   | 未提及                                            | 全缺                                         |

九項裡完整覆蓋的只有一項，部分覆蓋兩項，六項全缺。

### 2.2 EVOLVE 行動表與分數 gate：怎麼互動、哪裡矛盾

EVOLVE-PIPELINE.md Phase 2 目前只有一個 hard gate，「進化分數 ≥ 60 才算 candidate」，套用在全部四種行動類型。同一份文件緊接著的行動表，寫的觸發條件其實是各自的定性描述，不是分數：🔴 Rewrite 看高曝光加品質差，🟠 SEO 優化看高曝光加低 CTR 加品質 OK，🟡 翻譯看有曝光但無對應語言版本，🟢 新建看有需求但確認無文章。一份文件裡，gate 講分數，行動表講條件，兩者從來沒有真正對齊過。

矛盾的根源在分數公式本身。七個維度裡，品質缺陷（20%）、文章年齡（10%）、圖譜密度（10%），合計四成權重，計算前提都是「有一篇既有文章可以打分」。這剛好符合 🔴 Rewrite 型的定義，既有文章品質差、過期。但對其餘三型要嘛不成立要嘛方向相反。🟠 SEO 優化的定義特徵正是品質 OK，卻被品質缺陷維度往下扣。🟢 新建的定義特徵是還沒有文章，文章年齡與圖譜密度兩個維度找不到打分的對象。🟡 翻譯看的是另一語言的曝光缺口，跟既有中文文章的品質無關。BIM 案例的 58.2 分，扣分完全來自「品質缺陷 20%×20」與「文章年齡 10%×15」，這兩個維度分數低的原因正是文章寫得好、又是新文章。

實務上這個矛盾目前靠 OBSERVER-QUEUE #16 選項 (c)「維持現狀，SEO 型 candidate 一律靠人工判斷 append 並揭露 gate 分數」繞過。這不是設計出來的分流，是每次撞到都要手動寫一段「gate 分數如實揭露」但仍照樣 append 的臨時解法（見 `docs/semiont/ARTICLE-INBOX.md` BIM 條目）。

### 2.3 cross-ref：改動會被誰引用

`.github/ISSUE_TEMPLATE/article-proposal.yml`、`.github/workflows/pr-frontmatter-gate.yml`、README.md、`docs/community/REVIEWERS.md`、`docs/pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md` 都連到 CONTRIBUTING.md，但全部是整份文件層級的超連結，issue 模板一句話指過去、README 列成 front door、REVIEWERS.md 引「見 CONTRIBUTING.md」，沒有任何檔案依賴它內部的章節錨點或既有段落格式。新增一個 H2 章節不會斷任何 cross-ref。

EVOLVE-PIPELINE.md 這邊，sister_docs 已含 REWRITE、MAINTAINER、PEER-INGESTION、FACTCHECK，ROUTINE.md 的 `twmd-news-lens-weekly` 依賴 Phase 2 的輸出介面「append ARTICLE-INBOX candidate」。本次修法只改 gate 的內部判準，不改這個對外介面，呼叫方無感。

---

## 三、方案發散

**方案一：CONTRIBUTING 加一章＋EVOLVE 改 gate 分流（最小改動）**。CONTRIBUTING.md 新增「共編規則」章節，把九項對外清單寫成給貢獻者看的白話文字，判例細節 pointer 到 MAINTAINER-PIPELINE 不重寫。EVOLVE-PIPELINE.md Phase 2 新增「gate 適用範圍」段落，讓 60 分 gate 只管 🔴 Rewrite，其餘三型改用行動表既有的定性條件。兩份文件在段落開頭互相指向對方。

**方案二：獨立 `docs/community/CO-EDITING.md` 當單一 canonical，CONTRIBUTING 與 EVOLVE 各放 pointer**。好處是判例與 gate 邏輯只有一處要維護。壞處是多了第三個檔案，README、ANATOMY 的資源地圖都要重新掛一次索引，貢獻者要多跳一次連結才看得到規則，CONTRIBUTING 本來就是 front door，把重要的參與規則移出去等於把門後退一步。更關鍵的是它把「貢獻者該遵守什麼」跟「routine 怎麼選候選」這兩種服務完全不同讀者的內容塞進同一份文件，即使內部分兩節，仍是同一個 canonical 檔案在混兩種維度。

**方案三：判例全部只住 MAINTAINER-PIPELINE，CONTRIBUTING 只放連結**。改動量最小，今天三條判例已經寫完，不用重抄。但 MAINTAINER-PIPELINE 是 1500 多行的內部維運 SOP，語氣是寫給 routine 和 maintainer 看的操作手冊，貢獻者不會也不該去讀它。這個方案也不解決 #16，MAINTAINER-PIPELINE 管的是怎麼收 PR，不是候選怎麼選、分數怎麼算。

| 判準                                       | 方案一                                                                                               | 方案二                                                                        | 方案三                                                        |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------- |
| SSOT 唯一性                                | 判例正文唯一在 MAINTAINER-PIPELINE，CONTRIBUTING 只放摘要加 pointer，gate 邏輯唯一在 EVOLVE-PIPELINE | 判例與 gate 邏輯集中一檔，唯一性形式上最高                                    | 判例唯一在 MAINTAINER-PIPELINE，但 gate 矛盾沒有 canonical 家 |
| 貢獻者可讀性                               | 高，新章節就在貢獻者本來會讀的 front door                                                            | 中，多一次點擊，新檔案要重新掛進索引才會被看到                                | 低，貢獻者得去讀內部維運手冊才知道規則                        |
| 維護成本                                   | 中，兩份文件要記得互相同步，但各自範圍清楚                                                           | 低（單點維護），但多一個檔案的生命週期要顧                                    | 最低，但漏了 EVOLVE 那半，問題沒解完                          |
| REFLEXES #17 指標 over 複寫                | 符合，判例正文只在一處，CONTRIBUTING 是摘要不是複寫                                                  | 符合（移到新檔案）                                                            | 符合，但問題範圍不完整                                        |
| REFLEXES #38 混維度                        | 符合，對外規則跟對內 gate 是兩個不同讀者、不同動作，分別放兩份文件                                   | 違反，同一檔案同時服務貢獻者要不要這樣做，跟 routine 要不要選這個候選兩種動作 | 部分符合，但對外層等於沒內容，不成一層                        |
| 對齊哲宇裁示「兩層都要，一對外一對內互指」 | 完全對齊                                                                                             | 不對齊，變成三層                                                              | 不對齊，對外層是空的                                          |

---

## 四、定案與理由

採方案一。

哲宇追問後選的是「C：兩層都要，一對外一對內互指」，這句話本身已經框定答案是兩份文件，不是三份，也不是對外層空著。方案二和方案三分別踩到這句話的兩端。

方案一同時通過 REFLEXES #38 的混維度檢查：CONTRIBUTING 服務的是要提交東西的人，他讀這份文件時要決定的是我能不能這樣做、怎麼做才會被收下。EVOLVE-PIPELINE 服務的是 routine 與 session，讀這份文件時要決定的是這個候選要不要進 INBOX、算哪一種行動。兩種讀者、兩種決策時刻，理應各自成篇。

判例正文已經在今天寫進 MAINTAINER-PIPELINE，依 REFLEXES #17 同一事實只能一個 canonical，CONTRIBUTING 的新章節只做貢獻者視角的摘要，規則加為什麼加案例，附 pointer 回 MAINTAINER-PIPELINE 看完整判準與案例出處，不重寫判例全文。這樣同時保住 SSOT，也解決了貢獻者不會去讀 MAINTAINER-PIPELINE 的可讀性問題。

互指的具體做法：CONTRIBUTING 新章節每條規則附案例出處，EVOLVE-PIPELINE 的 gate 分流段落開頭附一句「貢獻者對這幾條規則的理解見 CONTRIBUTING.md §共編規則」。兩處都看得到對方，往後任一邊修改判例都會被提醒去檢查另一邊是否同步。

---

## 五、對外層條文草案（可直接貼進 CONTRIBUTING.md）

> 建議插入位置：現有「🎯 貢獻原則」章節之後、「📝 內容撰寫指南」之前，作為獨立 H2 章節。既有「🌱 你的文章 merge 之後」段落保留不動，本章第 5 條只補「怎麼升級」，不重寫三態定義。

```markdown
## 🤝 共編規則：怎麼跟既有內容互動

Taiwan.md 現在有 1,100 多篇文章，同一種投稿情境會一直重複出現。下面九條規則是這幾個月真實案例定案下來的，讀完你會比較清楚怎麼提交最容易被收下，遇到狀況時我們會怎麼處理。

### 1. 補充既有文章，不要整篇覆寫

如果你想改善的文章 frontmatter 已經有 `lastHumanReview: true`，或掛著 `researchReport`，或已經有 `sporeLinks`，代表這篇走過我們的深度查證流程。這種情況請不要刪掉大量既有段落、整批換掉腳註，改成「補充段落」提交：留住已核對過的內容，把你的新角度或更好的來源加進去。

**為什麼**：查證是這個站最貴的成本，整篇覆寫會把已經核對過的引語、年份、來源一起沖掉，即使你補上的內容品質更好，讀者信任也要重新累積一次。

**你會怎麼被列名**：我們會把你的角度織回原文，PR 說明與 commit 都會附上 `Co-authored-by: 你的名字 <你的 GitHub noreply 信箱>`（GitHub 設定 → Emails → 勾選 Keep my email addresses private 後顯示的那組）。

**案例**：陳士駿（PR #1630）、台灣便利商店文化（PR #1450）、台灣高鐵（PR #1483）都是這樣處理的。如果文章沒有上述三個欄位任一個（多數 `curation: incubating` 的文章屬於這種），代表還在查證排隊中，直接大幅修改沒問題，走一般流程即可。

### 2. 人物條目的收錄門檻

核心問題：一個不認識台灣的外國人，有沒有可能透過主流管道知道這個人？至少要滿足兩項之一：查得到維基百科本人條目，或有兩則以上互相獨立的第三方媒體報導。

**不算報導**：Spotify、KKBOX 這類平台收錄頁；你自己經營的 YouTube／IG／FB／Threads 頻道；單純以表演者身分上節目通告。

**為什麼**：這條門檻是我們對讀者承諾的查證能力有極限，沒有第三方報導，我們沒辦法核對這個人說過的話、做過的事。

**案例**：KENJI（PR #1365）、黑貓老師與 Cheap（PR #1395／#1401）、蔡黑皮（PR #1471）、三度C（PR #1525）都因兩項皆無而婉拒獨立成篇，其中可查證的部分歡迎併入相關產業或表演藝術條目。

### 3. About/ 只收 Taiwan.md 自己的第一人稱

`knowledge/About/` 只放 Taiwan.md（或哲宇本人）用第一人稱講「我是什麼」的自述。你對這個專案的觀察、期許、想像，即使內容正確、方向也符合我們的理念，執筆的人仍然是你，這類稿件請改用具名身分發表成一篇貢獻者觀點文章。

**案例**：〈Taiwan.md 不是什麼〉（PR #1407）、〈Taiwan-md 的未來〉（PR #1411）都是這個情況，內容我們很珍惜，只是換一個位置發表。

### 4. SEO metadata（title / description）修改另外開 PR

只想調整某篇文章的 `title` 或 `description`（不動正文）時，請單獨提交，並附上你觀察到的問題，例如 Search Console 顯示曝光高但點擊率低，或標題不符合下方的格式規範。完整規格見 [EDITORIAL.md](./docs/editorial/EDITORIAL.md) 的「Title 與 Description 的品質」章節：標題走冒號三明治格式，描述壓在 120-160 字。分開提交能讓我們更快處理，也不會把兩種完全不同的審核標準，事實查證與文字品質，混在同一個 PR 裡。

### 5. 你的文章上站後：curation 三態代表什麼、怎麼升級

見上方「🌱 你的文章 merge 之後」，新文章預設 🌱 進化中，一般文章無標示，🔎 已深度查證代表走完內部深度研究與逐項事實查證。從進化中升級不需要你做任何額外動作，這是維護流程逐篇處理的節奏。想加速，最有效的方式是自己補上可查證的一手來源，或參考下方第 9 條的素材共創模式。

### 6. 新條目 frontmatter 必填欄位

| 欄位                                    | 規則                                                                          |
| --------------------------------------- | ----------------------------------------------------------------------------- |
| `title` / `description`                 | 見上方第 4 條引用的 EDITORIAL 規格                                            |
| `category` / `subcategory`              | About 以外的中文文章必填，見 [SUBCATEGORY.md](./docs/taxonomy/SUBCATEGORY.md) |
| `author` / `difficulty` / `readingTime` | 必填，難度分級供讀者判斷閱讀時間                                              |
| `featured`                              | 一律填 `false`，由維護者統一管理                                              |
| `curation`                              | 不用手填，由維護流程在合併後加上                                              |

跑 `python3 scripts/tools/article-health.py <你的檔案> --profile=ci-deploy` 會告訴你缺了什麼。

### 7. 圖片授權

只能用你自己拍的照片，或 Creative Commons／Wikimedia Commons 這類明確授權的圖片，並在圖片下方標注來源與授權條款。不要用外部網域的圖片熱連結，請先下載存進 `public/article-images/`。AI 生成的圖片如果附了「File:...」這種來源連結，連結不一定正確，提交前請自己點開確認。

### 8. 用語：避免把中國用語直接寫進正文

我們的用語詞庫（見 [TERMINOLOGY.md](./docs/editorial/TERMINOLOGY.md)）標了一批兩岸用法有分歧的詞（tier B），例如「數據」對「資料」、「視頻」對「影片」。寫文章時盡量用台灣慣用說法，不確定可以查一下站上的用語詞庫頁。這不是逐字校對的門檻，維護流程會抓明顯的用字，你只需要盡量注意。

### 9. 不確定怎麼開始？試試「素材共創模式」

如果你是某個題目的領域專家，手上有第一手材料，論文、田野資料、專業知識，但不確定怎麼寫成 Taiwan.md 的文體，不用先寫完一篇稿子。你出材料，我們走站上的寫作流程織成文章，你甚至不需要碰 GitHub，在 issue 或 email 對話就可以。完整說明見 [CONTRIBUTOR-SYSTEM-PIPELINE.md §3](./docs/pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md)。
```

---

## 六、對內層條文草案（可直接貼進 EVOLVE-PIPELINE.md）

> 建議插入位置：Phase 2「進化分數 v2.0」小節之後、「產出：四種行動」表格之前，新增一個獨立小節。

```markdown
### 進化分數 gate 的適用範圍（v2.1，解 OBSERVER-QUEUE #16）

> 貢獻者對「補充 vs 覆寫」「人物門檻」等共編規則的理解見 [CONTRIBUTING.md §共編規則](../../CONTRIBUTING.md)，本節只處理 Taiwan.md 自己選候選時的 gate 邏輯，兩者是不同的讀者與決策時刻。

**為什麼要分流**：進化分數七個維度裡，品質缺陷（20%）、文章年齡（10%）、圖譜密度（10%）三項的計算前提是「有一篇既有文章可以打分」，這是 🔴 Rewrite 型的定義特徵，但對其餘三型不成立甚至方向相反。🟠 SEO 優化的定義特徵正是品質 OK，卻被品質缺陷維度扣分；🟢 新建的定義特徵是還沒有文章，文章年齡與圖譜密度沒有對象可算；🟡 翻譯看的是另一語言的曝光缺口，跟中文本體品質無關。一個分數同時服務四種本質不同的行動類型，是 REFLEXES #38「混維度＝silent killer」的具體案例（誕生：2026-07-17 BIM 英文版 metadata 案，SC 7 天 623 曝光排全站第 7、CTR 趨近 0，GA4 7 天 57 次瀏覽排全站第 5，文章本體 53 條腳註、2026-05-22 新文，算出 58.2 分卡在 60 分 gate 之外）。

**Gate 適用範圍**：

| 行動型      | 60 分 gate                | 改用判準                                                                                                                                       |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔴 Rewrite  | 適用，< 60 不算 candidate | 不變                                                                                                                                           |
| 🟠 SEO 優化 | 不適用                    | 沿用本檔既有「高曝光＋低 CTR（< 5%）＋品質 OK」定性條件（Phase 1B），不新增量化門檻                                                            |
| 🟡 翻譯     | 不適用                    | 沿用 v2.0 §Bump-vs-translate decision matrix：`missing` 或 `stale`（真 body drift）才算 candidate，`metadata-stale` 走零成本 bump，不進本 gate |
| 🟢 新建     | 不適用                    | 沿用本檔既有「曝光 ≥ 500 + 無對應文章」判準（§Top 5 最常忘的 step 第 3 條），並過 Phase 4 CHECK 確認 ARTICLE-INBOX 也無重複                    |

這次修法沒有引入新的量化數字，只是把本檔既有的行動表條件、Bump-vs-translate 矩陣、Top 5 步驟第 3 條，正確接回各自的行動型別當作 gate，取代原本全部套用一個為 Rewrite 型設計的分數。其餘既有 hard gate（三源全綠、不重複 INBOX、candidate 含對比理由、GA+SC 雙源 pointer）四型照樣適用，這裡只鬆綁進化分數這一項判準，不是整組 gate 鬆綁。

**🟠 SEO 優化型的 5 分鐘操作**：

1. 讀 `public/api/dashboard-analytics.json` 的 `searchConsole7d.opportunities` 或跑 `fetch-search-console.py`，篩出 CTR < 5% 的項目，按曝光量由高到低排序。
2. 對候選文章核對「品質 OK」：無 article-health hard violation，且非 `curation: incubating` 的半成品（是的話先歸 🔴 或標記需要先補充，不算 SEO 型 candidate）。
3. 通過即改該篇 `title` / `description`，套 EDITORIAL.md「Title 與 Description 的品質」四原則與七條文字感，正文不動。更新 frontmatter 屬 MANIFESTO §自主權邊界「AI 自主可做」清單內的動作。
4. Append 或更新 ARTICLE-INBOX candidate 時，reasoning 仍要附 SC 與 GA 雙源 pointer 的實際數字，這是既有 Hard Gate，不因為換了判準而跳過。

**跟進化分數 v2.0 的關係**：進化分數保留，角色收窄為 🔴 Rewrite 型內部的優先序排序，不再是四型共用的入場門檻。入場後的排序，🟠 SEO 優化型按 CTR 差距（預期 CTR 減實際 CTR）由大到小、🟢 新建型按曝光量由高到低、🟡 翻譯型按 status.py 的嚴重度排序，body drift 優先於 metadata-stale。
```

需同步更新本檔既有「🚦 Hard Gate Inventory」表的「進化分數 ≥ 60」列，備註欄補一句：僅適用 🔴 Rewrite 型，v2.1。

---

## 七、實作清單

1. CONTRIBUTING.md 貼入 §五全文，插入位置見上方標註（**自主權內**：九條規則的判準本身今天已由哲宇拍板，這裡只是把既有決策寫成對外文字，不新增任何判斷）
2. EVOLVE-PIPELINE.md 貼入 §六全文並同步修 Hard Gate Inventory 表一行（**需哲宇**：OBSERVER-QUEUE #16 標記命中 BECOME High-stake #3 quality gate 調整，本報告是拍板前的 blueprint，即使沒有引入新數字，改的仍是 gate 的判準結構）
3. EVOLVE-PIPELINE.md sister_docs 加一行指向 CONTRIBUTING.md，CONTRIBUTING.md 對應索引處視情況加一行指向新章節（**自主權內**，純索引補齊）
4. OBSERVER-QUEUE #16 移入「已決」，處置寫「哲宇拍板方案 (a) 變體：gate 分流至各行動型既有判準」（**待第 2 項拍板後執行**）
5. ARTICLE-INBOX.md BIM 條目的 gate 揭露註記改標「已依 v2.1 gate 分流正常入場」（**待第 2 項拍板後執行**，跟第 4 項同批）

依賴順序：第 1、3 項可以立刻做，第 2 項需要哲宇先看過本報告點頭，第 4、5 項是第 2 項落地後的收尾動作。

---

## 八、驗收

**Dogfood 一：BIM 案例走新 SEO 型觸發**。沿用 ARTICLE-INBOX.md 已記錄的真實數字，不重新臆測。SC 7 天「bim residential housing construction taiwan case study」623 曝光、CTR 趨近 0，落在 CTR < 5% 的定性條件內。文章本體 53 條腳註、2026-05-22 新文、無 article-health hard violation、非 incubating，品質 OK 成立。三項判準全部滿足，不需要 58.2 分這個數字，直接判定為 🟠 SEO 優化型 candidate。跟現況唯一的差別：不用再寫「gate 分數如實揭露」這句話，因為分數從一開始就不是判準的一部分。

**Dogfood 二：今天五個 PR 對照對外規則**。人物門檻對應到的 KENJI（#1365）、黑貓老師（#1395）、Cheap（#1401）、蔡黑皮（#1471）、三度C（#1525）五案，對上 §五第 2 條「人物條目的收錄門檻」，判準與案例編號逐一吻合。補充既有文章對應到的陳士駿（#1630）、台灣便利商店文化（#1450）、台灣高鐵（#1483），對上第 1 條。About 第一人稱對應到的〈Taiwan.md 不是什麼〉（#1407）、〈Taiwan-md 的未來〉（#1411），對上第 3 條。今天拍板的判例，每一條都在對外草案裡找得到對應規則與出處。

---

## 九、風險與反措施

**規則寫太細變成門檻牆**：九條規則加上案例編號，容易讓第一次來的貢獻者覺得規矩好多。反措施：草案已經把核心的判準（人物門檻、覆寫判準）放在條文本身，案例只當佐證，不逐條展開判斷過程。CONTRIBUTING.md 開頭「🧬 最簡單的貢獻方式」的對話式入口保留不動，願意跟 Taiwan.md 聊的貢獻者不需要自己讀完整章。

**兩層互指漂移**：CONTRIBUTING 的摘要與 MAINTAINER-PIPELINE 的判準未來各自修改，可能對不上。反措施：暫不新增獨立的 counts-drift 守門，成本高於現有漂移風險，先靠 §四已寫入的互指機制，任一邊修改判例時文件裡的互指句會提醒維護者去檢查另一邊。如果未來這類漂移實際發生兩次以上，再考慮升級成儀器化檢查。

---

## 十、後記

哲宇拍板方案一後，§七實作清單五項全部落地。以下記實作過程中的三個摩擦。

**CONTRIBUTING.md 插入點跟草案標註的位置不同**：§五原本建議插在「🎯 貢獻原則」章節之後、「📝 內容撰寫指南」之前，實際落地時就是這個位置（「🌱 你的文章 merge 之後」段落結束、`---` 分隔線之後），跟草案一致，沒有摩擦——這裡記一筆是因為原本擔心 CONTRIBUTING.md 大量使用全形標點，字串替換容易因為半形/全形標點誤判而找不到錨點，改用行號定位插入，避免了這個問題。

**EVOLVE-PIPELINE.md 的 ASCII spine 是等寬字元畫的框，改一個字要重算全部留白**：Hard Gate Inventory 表格加「（🔴 型）」限定只是普通 Markdown 表格，改了就好；但 ASCII spine 那行 `↳ Hard gate: 進化分數 ≥ 60 才算 candidate` 是用空格手動對齊等寬框線的視覺寬度（CJK 字元佔 2 格、ASCII 佔 1 格），直接在字尾加註解會撐破右邊界。用視覺寬度換算重新排版這一行，其餘框線不動。

**🟠 SEO 型觸發條件沒有照原始任務描述的「SC 28 天曝光 ≥ 500 且 CTR < 全站非品牌均值一半」寫**：這組數字在本報告全文與現行 EVOLVE-PIPELINE.md 都找不到出處，§六定案的版本是「沿用本檔既有『高曝光＋低 CTR（< 5%）＋品質 OK』定性條件（Phase 1B），不新增量化門檻」——最終照本報告落地，沒有採用那組沒有 canonical 來源的數字，避免犯下報告自己在 §九／實作反例點名的「發明新門檻數字」。

**Dogfood 一驗證結果**：BIM 英文版 metadata（`knowledge/en/Technology/taiwan-bim-construction-tech.md`）三項判準逐一核對——SC 7 天「bim residential housing construction taiwan case study」623 曝光、CTR ~0，落在 Phase 1B「高曝光＋低 CTR（< 5%）」定性條件內；`article-health.py --profile=ci-deploy` 跑出 `hard=0`；frontmatter 沒有 `curation` 欄位（非 `incubating`）。三項全過，判定為 🟠 SEO 優化型 candidate，不需要 58.2 分這個數字。

**Dogfood 二驗證結果**：今天五個 PR 判例全部在 CONTRIBUTING.md §🤝 共編規則找得到對應條文——#1365（KENJI）對第 2 條人物條目收錄門檻、#1630（陳士駿）對第 1 條補充既有文章不整篇覆寫、#1450（台灣便利商店文化）對第 1 條、#1407 與 #1411（〈Taiwan.md 不是什麼〉／〈Taiwan-md 的未來〉）對第 3 條 About/ 只收第一人稱。

---

_v1.0 | 2026-09-05 fortnight-review session（EVOLVE Mode 4 REPORT 相）。實作等哲宇看過本報告後拍板 §七標「需哲宇」的項目。_
_v1.1 | 2026-09-05 fortnight-review session — 哲宇拍板方案一，§七實作清單五項落地：CONTRIBUTING.md 新增 §🤝 共編規則（9 條）、EVOLVE-PIPELINE.md 新增 §進化分數 gate 的適用範圍（v2.1）+ ASCII spine／Hard Gate Inventory 補「（🔴 型）」限定 + sister_docs 互指、status 轉 `implemented`。§十後記補三則實作摩擦 + 兩項 dogfood 實跑結果。_
