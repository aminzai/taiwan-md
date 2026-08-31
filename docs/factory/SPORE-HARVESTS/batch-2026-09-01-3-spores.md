---
spores: '#172, #173, #174'
harvest_date: '2026-09-01 06:52'
harvest_window_day: 'D+14'
batch_reason: 'D+14 milestone harvest（budget-總預算十年 threads/x/facebook 三平台，per SPORE-HARVEST-PIPELINE §d+0/+1/+7/+30 cadence D+14 milestone）；當日 dashboard harvestStatus 166 筆核對後 D+1-D+7 主排程窗口全數落空（最新孢子 8/23 已過 D+7、過去一週無新孢子發布），本輪唯一到期動作是 8/18 budget 三孢子今日恰好滿 14 天'
triggered_by: 'cron'
reply_count: '0 新增（三平台皆無新讀者留言，僅既有留言與作者自身連結留言）'
---

# 2026-09-01 harvest — budget-總預算十年 D+14 milestone

Login-state probe：PASS（@taiwandotmd 個人檔案可見編輯個人檔案按鈕、6,529 位粉絲，帳號已登入 Threads）。

dashboard `harvestStatus`（166 筆）逐條核對：`withinHarvestWindow=true` 為 0 筆，跟前兩輪（8/31、8/30）同一狀態延續——最新孢子仍是 8/23 用語保存副詞層（今日 daysSincePublish=9，已過 D+7 主排程窗口，下一次到期是 8/23+14=9/6 的 D+14）。本輪唯一到期項目是 8/18 budget-總預算十年三孢子，今日剛好滿 14 天，觸發 pipeline cadence 表的 D+14 milestone（「只抓新留言歸檔」）。

## #172 Threads（budget-總預算十年，D+14）

- URL: https://www.threads.com/@taiwandotmd/post/DcKsP3Co9jm
- Metrics: views 5,051（前次 D+10 harvest 4,989）/ likes 309 / comments 15 / reposts 67 / shares 53
- 逐一核對：chipher、locadia641231、liyangyang411、hyhct943、rosie_forosie 五則留言皆已有 `作者` 回覆（2026-08-19/20），zannaex「留己看」延續歷輪判斷 skip（書籤型非互動內容）。comments 數字與 D+10 持平（15），確認 0 條新增讀者留言。

## #173 X（budget-總預算十年，D+14）

- URL: https://x.com/taiwandotmd/status/2089561276938666168
- Metrics: views 1萬（10K rounded）/ replies 5 / reposts 200 / likes 599 / bookmarks 90 — 與 D+10 harvest 數字一致
- 本機未登入 X，留言內容讀不到（沿用歷輪判斷：login wall 是環境限制不是工具故障），header metrics 五項皆與上輪相同，可合理推斷 0 新增回覆。

## #174 Facebook（budget-總預算十年，D+14）

- URL: https://www.facebook.com/61576525376323/posts/pfbid02iQux9KoUcNtxZHLVdFQ9R2oFXTH8X3EQmauC8XJ3CoUacveZVPKFXoqphTxwbzYwl
- 未登入 Facebook（頁面頂部顯示「登入」），可見公開摘要：1 個心情、1 則留言、1 次分享
- 該 1 則留言是作者本人貼的完整頁面連結（非讀者留言），與 8/23 上輪判斷一致，0 條讀者留言需處置

## 本輪摘要

- 3 spore D+14 milestone harvest 完成，數字已寫入 `spore-db.py add-metrics --d-plus 14`（唯一入口，未碰 frontmatter / SPORE-LOG.md）
- Bucket A/B/C/D：0 條（三平台皆無新讀者留言）
- Bucket E/F/G：0 條新增（既有留言均已在前幾輪處理過或屬 skip 類）
- Reply shipped：0（無新留言需回覆）
- Factual fix：0
- #175/#176（用語保存副詞層）今日 daysSincePublish=9，不在今日到期範圍（下次 D+14 milestone 為 9/6），本輪不觸碰，維持前兩輪判斷延續
