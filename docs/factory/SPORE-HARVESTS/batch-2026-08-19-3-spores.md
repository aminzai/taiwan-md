---
spores: '#172, #173, #174'
harvest_date: '2026-08-19 06:45'
harvest_window_day: 'D+1'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am'
triggered_by: 'cron'
reply_count: '8 visible (Threads 7 distinct + 1 dup / X 4 未讀 login wall / Facebook 1 作者自留言非讀者回覆)'
---

# 2026-08-19 D+1 harvest — budget-總預算十年 三平台首輪

三則孢子（#172 Threads / #173 X / #174 Facebook）皆為 8/18 發佈的「總預算十年」特別企劃，本輪為發佈後首次 harvest（D+1）。

## #172 Threads

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Metrics: views 4,074 / likes 266 / comments 9 / reposts 57 / shares 49
- Login-state probe：PASS（追蹤中／發佈按鈕可見，帳號已登入）

### 留言逐字 + 分桶

| Author        | 留言原文                                                             | Bucket                    | 處置                             |
| ------------- | -------------------------------------------------------------------- | ------------------------- | -------------------------------- |
| chipher       | 這個讚耶！把難懂的總預算數據，用圖表變得讓人容易看懂                 | E                         | log only（時間預算內未逐一回覆） |
| alden.0202    | 預算編列跟養魚一樣，錢流去哪要先算清楚，文化跟國防差這麼多有點意外。 | F                         | log only                         |
| locadia641231 | 體育部呢？                                                           | B                         | **已驗證 + 已回覆**（見下）      |
| liyangyang411 | 推推資訊整理得很詳細                                                 | E                         | log only                         |
| zannaex       | 留己看                                                               | F（bookmark，非互動內容） | skip                             |
| hyhct943      | 擴一個                                                               | E（低信號）               | log only                         |
| rosie_forosie | 推整理                                                               | E                         | log only                         |

**alden.0202 在 DOM 讀到兩次完全相同文字**（同一則留言重複渲染 or 巢狀鏡像），計入 harvest 但不重複回覆。9 則計數 vs 7 distinct + 1 dup = 8 個 pressable container，缺口 1 則未定位（可能是巢狀回覆，per [REFLEXES #91 前身 diary 2026-08-10 教訓](../../semiont/MEMORY.md)——本輪未逐則點開 permalink 深掃，留痕跡在此不追）。

### Bucket B 處置：locadia641231「體育部呢？」

跨源驗證（非外部 WebSearch，直接查站內資料 SSOT `src/data/ly-budget.json`）：**運動部**（原教育部體育署）115 年度確實是獨立追蹤的機關，預算 66.4 億，但 `budget.template.astro` 的機關排行榜只取前 22 大（`rankRows.slice(0, 22)`），運動部實際排名第 24（0-index 23），沒有落在頁面可見範圍內。讀者的疑問完全成立——資料庫裡有，頁面沒露出。

回覆（已透過 Chrome MCP execCommand insertText 發佈，post-ship verify 用 pressable-container count diff 確認新增 1 則、無重複）：

> 有喔，115 年新設運動部（原教育部體育署），66.4 億，但排名 24，沒進頁面前 22 大機關榜，之後找地方補上。

**EVOLVE candidate**（累積到 1 條，未達 Round 2 觸發門檻 3 條，先記錄）：`/budget` 頁機關排行榜目前硬性只顯示前 22 大，讀者已證實會主動問榜外機關（運動部）。候選修法：排行榜加「顯示更多」或搜尋欄，或至少在文字段落點名幾個榜外但話題性高的機關（運動部、原能會等）。

## #173 X

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views 5,918 / replies 4 / reposts 125 / likes 361 / bookmarks 56
- **X 登入牆連續命中**（per 8/17 memory 已連續第六天以上同狀態，本輪第 N+1 次驗證，不重複升 LESSONS，沿用既有 handoff）：瀏覽器未登入 X，"See all the replies" 蓋版擋住留言內容，4 則 reply 內容本輪無法讀取。Metrics（views/replies/reposts/likes/bookmarks 五個數字）在登入牆之前的 header 區塊可讀，已照常入帳。

## #174 Facebook

- URL: https://www.facebook.com/61576525376323/posts/pfbid02iQux9KoUcNtxZHLVdFQ9R2oFXTH8X3EQmauC8XJ3CoUacveZVPKFXoqphTxwbzYwl
- Metrics: likes 1 / comments 1 / shares 1（FB 公開頁面未登入可讀讚數/留言數/分享數，views 不對外公開不可讀）
- 唯一一則留言是作者本人置頂補連結（「完整《十年預算》頁面👉 https://taiwan.md/budget/?utm_source=facebook...」），非讀者留言，0 條讀者互動需分桶。

## 本輪摘要

- 3 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏）：1 條，已驗證 + 已回覆 + EVOLVE candidate 登記
- Bucket D（立場質疑）：0 條
- Bucket E（正面互動）：5 條，log only（時間預算內選擇性回覆，非全數回覆——Bucket B 的即時性優先於 E 的禮貌性回覆）
- Bucket F/G：2 條，log only / skip
- Reply shipped：1（Threads Bucket B）
- Factual fix：0（無事實錯誤需修文章）
