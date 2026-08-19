---
spores: '#172, #173, #174'
harvest_date: '2026-08-20 06:40'
harvest_window_day: 'D+2'
batch_reason: 'daily audience flywheel cycle — routine twmd-spore-harvest-am'
triggered_by: 'cron'
reply_count: '6 visible on Threads (5 distinct reader authors + 1 已知 platform-suppressed gap) / X 5 未讀 login wall 延續 / Facebook 1 作者自留言非讀者回覆'
---

# 2026-08-20 D+2 harvest — budget-總預算十年 三平台第二輪

三則孢子（#172 Threads / #173 X / #174 Facebook）皆為 8/18 發佈的「總預算十年」特別企劃，本輪為 D+1（8/19）之後的第二次 harvest。

## #172 Threads

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Metrics（harvest 前）: views 4,678 / likes 301 / comments 10 / reposts 65 / shares 53
- Login-state probe：PASS（個人檔案／編輯個人檔案／洞察報告可見，帳號已登入）

### 留言逐字 + 分桶（本輪新讀到 + 上輪殘留未回覆）

| Author        | 留言原文                                             | Bucket                    | 處置                                                                                  |
| ------------- | ---------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------- |
| locadia641231 | 體育部呢？                                           | B                         | 已於 D+1 驗證 + 回覆，本輪確認回覆仍在，無新動作                                      |
| chipher       | 這個讚耶！把難懂的總預算數據，用圖表變得讓人容易看懂 | E                         | **本輪已回覆**（見下）                                                                |
| liyangyang411 | 推推資訊整理得很詳細                                 | E                         | **本輪已回覆**（見下）                                                                |
| rosie_forosie | 推整理                                               | E                         | **本輪已回覆**（見下）                                                                |
| hyhct943      | 擴一個                                               | E（低信號）               | **本輪已回覆**（見下）                                                                |
| zannaex       | 留己看                                               | F（bookmark，非互動內容） | skip（同 D+1 判斷）                                                                   |
| alden.0202    | （D+1 曾見「預算編列跟養魚一樣...」）                | —                         | **本輪在主串與各自 permalink 均查無此留言**，判斷為已被平台或作者移除，非本輪處置範圍 |

**巢狀回覆 gap 追查**（per [REFLEXES 2026-08-16 lesson](../../semiont/MEMORY.md) 巢狀回覆不留缺口記號）：主帖顯示 comments=14（含本輪新增 4 則回覆），逐一開啟 5 位讀者留言各自的 permalink 頁面，全部回「尚無回覆」，無巢狀層級被漏讀。改用「全部＋最新」排序重新讀取主串，頁尾出現 Threads 原生訊息「**部分新增回覆無法顯示。瞭解詳情**」——header 計數與可見留言數之間的落差是**平台端自行抑制顯示**（非本工具讀取遺漏），本輪缺口記號留在此處，供未來 harvest 若持續出現同落差時交叉對照。

### Bucket E 回覆執行（本輪四則，Chrome MCP execCommand insertText）

四則皆為 D+1 已存在但未回覆的正面互動留言，本輪逐一補回覆，each post-ship verify 用 `[data-pressable-container]` count diff + reload 確認新增 1 則、無重複：

| Author        | 回覆內容                                                        |
| ------------- | --------------------------------------------------------------- |
| chipher       | 謝謝你喜歡！這批圖表是想讓大家不用啃數字表格也能看懂錢往哪走 🧬 |
| liyangyang411 | 謝謝你的支持，整理十一年資料真的花了不少功夫 🧬                 |
| rosie_forosie | 謝謝你 🧬                                                       |
| hyhct943      | 謝謝你幫忙擴散 🧬                                               |

第一則（chipher）click 送出後 `[data-pressable-container]` count diff 顯示 after==before（false negative），但截圖確認回覆已實際發佈成功（timestamp「1分鐘」+ 內容比對一致），**未觸發 Pitfall 6 重試**——先看畫面再判斷是本輪避免 duplicate ship 的關鍵動作。後三則 count diff 皆正常顯示 after>before，各 1 次成功、0 重試。

- Metrics（harvest 後回填）: views 4,678 / likes 302 / comments 14 / reposts 66 / shares 53

## #173 X

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views 9,644 / replies 5 / reposts 196 / likes 578 / bookmarks 88
- **X 登入牆連續命中**（延續 8/17 起同狀態，本輪第 N+1 次驗證）：瀏覽器未登入 X，「See all the replies」蓋版擋住留言內容，5 則 reply 內容本輪無法讀取。Metrics 五個數字在登入牆之前的 header 區塊可讀，已照常入帳。

## #174 Facebook

- URL: https://www.facebook.com/61576525376323/posts/pfbid02iQux9KoUcNtxZHLVdFQ9R2oFXTH8X3EQmauC8XJ3CoUacveZVPKFXoqphTxwbzYwl
- Metrics: likes 1 / comments 1 / shares 1（與 D+1 完全持平，FB 公開頁面未登入可讀讚數/留言數/分享數，views 不對外公開不可讀）
- 唯一一則留言仍是作者本人置頂補連結，非讀者留言，0 條讀者互動需分桶。

## 本輪摘要

- 3 spore 全數 harvest 完成，數字已寫入 `spore-db.py add-metrics`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/C（事實錯誤）：0 條
- Bucket B（缺漏）：0 條新增（locadia641231 沿用 D+1 已處置結論）
- Bucket D（立場質疑）：0 條
- Bucket E（正面互動）：4 條，**本輪全數回覆**（D+1 累積未回覆的 4 則今日清空）
- Bucket F/G：1 條（zannaex 書籤型留言），log only
- Reply shipped：4（Threads Bucket E，各 1 次成功 0 重試）
- Factual fix：0（無事實錯誤需修文章）
- 殘留訊號：alden.0202 D+1 留言本輪查無蹤跡（平台/作者移除，非本輪可處置範圍）；X 登入牆持續；Threads「部分新增回覆無法顯示」平台端訊息首次觀察到，留待後續 cycle 交叉驗證是否為固定落差來源
