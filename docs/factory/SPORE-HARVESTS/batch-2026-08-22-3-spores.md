---
spores: '#172, #173, #174'
harvest_date: '2026-08-22 07:10'
harvest_window_day: 'D+4'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am（前一日 2026-08-21 無 cron 紀錄，本輪為跳過一天後的接續讀取）'
triggered_by: 'cron'
reply_count: '7 則留言可讀（Threads，5 已於前幾輪回覆＋1 本輪新回覆＋1 重複渲染同內容）/ X 5 則登入牆延續無法讀取 / Facebook 1 則作者自留言非讀者回覆'
---

# 2026-08-22 D+4 harvest — budget-總預算十年 三平台第三輪

三則孢子（#172 Threads / #173 X / #174 Facebook）皆為 8/18 發佈的「總預算十年」特別企劃。前一天（8/21）無 harvest 紀錄，本輪為接續 D+2（8/20）之後的讀取，跳過 D+3。

## #172 Threads

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Login-state probe：PASS（個人檔案／編輯個人檔案／洞察報告可見，帳號已登入）
- Metrics: views 4,799 / likes 303 / comments 14 / reposts 66 / shares 53

### 留言逐字 + 分桶

| Author        | 留言原文                                                             | Bucket                      | 處置                                                    |
| ------------- | -------------------------------------------------------------------- | --------------------------- | ------------------------------------------------------- |
| chipher       | 這個讚耶！把難懂的總預算數據，用圖表變得讓人容易看懂                 | E                           | D+2 已回覆，本輪確認仍在                                |
| locadia641231 | 體育部呢？                                                           | B                           | D+1 已驗證＋回覆（運動部 66.4 億排名 24），本輪確認仍在 |
| liyangyang411 | 推推資訊整理得很詳細                                                 | E                           | D+2 已回覆，本輪確認仍在                                |
| hyhct943      | 擴一個                                                               | E（低信號）                 | D+2 已回覆，本輪確認仍在                                |
| rosie_forosie | 推整理                                                               | E                           | D+2 已回覆，本輪確認仍在                                |
| zannaex       | 留己看                                                               | F（bookmark，非互動內容）   | skip（同前幾輪判斷）                                    |
| alden.0202    | 預算編列跟養魚一樣，錢流去哪要先算清楚，文化跟國防差這麼多有點意外。 | E（延伸比喻＋認同核心發現） | **本輪首次回覆**（見下）                                |

**alden.0202 留言狀態說明**：D+2（8/20）harvest 曾判斷此則「主串與各自 permalink 均查無此留言，判斷為已被平台或作者移除」。本輪重新讀取時該則留言**完整可見**，且 DOM 中同一則內容渲染出現兩次（`[data-pressable-container]` 抓到兩個內容完全相同、讚數與回覆數皆為 0 的節點）。研判為 D+2 那次的「查無蹤跡」屬 Threads 端渲染 / 虛擬化的間歇性抑制（同批次曾記錄「部分新增回覆無法顯示」平台訊息），並非留言真的被移除；兩個重複節點也是同源渲染問題，非讀者重複發文。本輪未再看到「部分新增回覆無法顯示」提示文字，comments=14 與可見留言數（含巢狀）對得上。

### Bucket E 回覆執行（本輪一則，Chrome MCP execCommand insertText via 留言自身 permalink 頁）

| Author     | 回覆內容                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| alden.0202 | 你這個養魚比喻很到位，錢流去哪真的要先算清楚。文化跟國防差二十倍是十一年資料攤開後我自己也意外的地方 🧬 |

Post-ship verify（per Pitfall 6 hard rule，`[data-pressable-container]` count diff）：before=2 → after=3，`after > before` 一次成功，0 重試。截圖確認回覆文字與 input 一致，無 ASCII/中文字元遺失。

- Metrics（harvest 時）: views 4,799 / likes 303 / comments 14 / reposts 66 / shares 53（回覆送出後尚未重新整理頁面確認 comments 是否即時 +1，數字取自送出前 snapshot）

## #173 X

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views ~10,000（header 顯示「1萬」K-rounded）/ replies 5 / reposts 201 / likes 599 / bookmarks 90
- **X 登入牆連續命中**（延續 8/17 起同狀態，本輪第 N+1 次驗證）：「See all the replies」蓋版擋住留言內容，5 則 reply 內容本輪仍無法讀取。Metrics 五個數字在登入牆之前的區塊可讀，已照常入帳。

## #174 Facebook

- URL: https://www.facebook.com/61576525376323/posts/pfbid02iQux9KoUcNtxZHLVdFQ9R2oFXTH8X3EQmauC8XJ3CoUacveZVPKFXoqphTxwbzYwl
- Metrics: likes 1 / comments 1 / shares 1（與 D+1/D+2 完全持平，FB 公開頁面未登入可讀讚數/留言數/分享數，views 不對外公開不可讀）
- 唯一一則留言仍是作者本人置頂補連結，非讀者留言，0 條讀者互動需分桶。

## 本輪摘要

- 3 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏）：0 條新增（locadia641231 沿用 D+1 已處置結論）
- Bucket D（立場質疑）：0 條
- Bucket E（正面互動）：1 條新回覆（alden.0202），其餘 4 條沿用前幾輪回覆
- Bucket F/G：1 條（zannaex 書籤型留言），log only
- Reply shipped：1（Threads Bucket E，1 次成功 0 重試）
- Factual fix：0（無事實錯誤需修文章）
- 殘留訊號：alden.0202 D+2「查無蹤跡」判斷本輪證實為平台渲染間歇性抑制而非真實移除，供未來 harvest 遇到同類「留言消失」時優先假設渲染問題、隔日重查再下結論，而非直接判定已移除；X 登入牆持續（第 6 天）；前一日（8/21）無 cron 紀錄，本輪為接續讀取，未發現因跳過一天而遺漏的新留言
