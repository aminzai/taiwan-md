---
spores: '#165, #166, #167, #168'
harvest_date: '2026-08-10 07:05'
harvest_window_day: 'D+6'
batch_reason: 'daily twmd-spore-harvest-am cron cycle — 黃崇仁 + 海關報關與EZWAY 兩批孢子 D+6 harvest'
triggered_by: 'cron'
reply_count: '0 則新增直接回覆；讀取層無新增可分類訊號（四篇皆與 D+5 高度持平，僅 X 兩篇 views 微幅自然成長）'
---

# Harvest batch — 黃崇仁 #165/#166 + 海關報關與EZWAY #167/#168（D+6）

## 環境狀態：Chrome MCP 連線正常，帳號登入態連續第 2 天仍未恢復

`list_connected_browsers` 回傳配對裝置、`tabs_context_mcp`／`navigate`／`get_page_text` 全數正常運作。但 navigate 到 `@taiwandotmd` profile 與各 post 頁面後，頁面持續顯示「登入」按鈕與「使用 Instagram 帳號繼續」提示、留言串底部出現「登入即可查看更多回覆」——**判定仍是登出態**，跟昨日（D+5）記錄的斷點層級相同（連線層已恢復，登入層未恢復）。

本輪未嘗試登入（帳密輸入屬 human-only，超出 AI 自主範圍），僅讀取公開頁面可見內容。

---

## #165 Threads — https://www.threads.com/@taiwandotmd/post/Dblb5_4E-hH

**Metrics snapshot（2026-08-10 07:06 TPE）**：3.8 萬次瀏覽 / 790 讚 / 36 留言 / 25 轉發 / 57 分享

**與 D+5（8/9）逐一比對完全相同**：五個指標數字（views 的 K-rounded 值／likes／comments／reposts／shares）全部一致，這是繼 D+2→D+5 之後第三輪精確持平快照，確認 REFLEXES #78 Pure plateau ——這篇孢子的自然傳播週期已穩定結束。

### 可讀留言範圍（登出態下 `get_page_text` 單次讀到）

跟昨日相同，可見約 22 則留言（platform 計數 36，牆後 14 則仍不可讀）。逐一核對留言作者與內容，**與昨日記錄的清單一致，無新增留言**：置頂爭議 `@jackchen7355`「洗白」質疑（11 讚，Bucket D）、`@haoyingmiao` 具體換股數據反駁（19 讚 2 回覆，Bucket E，已知）、`@huwenxian54` 補充下市換股機制、`@figoho1849`／`@michael.tsai.1690` 台大物理系背景討論、`@a0912597052` 情緒性指控兩則（Bucket D/G）等，皆為既有分類延續。

### 分類結果

無新增留言可分類。8/6 完整分類 + 8/9 補充分類延續有效。

### 事實驗證結論 / 文章本體修改

無新增可驗證事實 callout，文章本體無修改。

---

## #166 X — https://x.com/taiwandotmd/status/2084319140907786616

**Metrics snapshot（2026-08-10 07:08 TPE）**：1,379 Views / 17 讚 / 2 轉發 / 2 回覆

較 D+5（1,362 views）+17，likes/reposts/comments 三個互動數字持平。X 留言牆持續擋住留言內容（未登入），無新增可分類訊號。

---

## #167 Threads — https://www.threads.com/@taiwandotmd/post/Dbm5PdXE181

**Metrics snapshot（2026-08-10 07:10 TPE）**：1,746 次瀏覽 / 56 讚 / 2 留言 / 3 轉發 / 3 分享

較 D+5（1,744 views）+2，其餘四個指標持平。

### 留言明細（唯一直接回覆，與 D+5 完全相同）

1. **@0991gnaw.h**（延續自 8/5）：「增編預算我就反對了。使用者付費，請直接跟消費者收錢謝謝」→ **Bucket F** 解讀分歧，延續既有判斷，不回覆

### 話題環境訊號（相關串文，非直接回覆，Bucket D 延續觀察）

「相關串文」推薦區塊仍持續出現同批高度政治化的獨立貼文（`@linchuyin1010`／`@buffyshih`「網軍假訊息」反駁 framing、`@q10242` 質疑個資外洩、`@jeromekuo` 反質疑、`@knews_taiwan` 引用媒體報導立法院預算審查角度），內容與昨日觀察到的話題環境一致，均**非對本孢子的直接回覆**。話題環境持續政治化但無新增對 Taiwan.md 孢子本身的直接事實挑戰，per DNA #26 v2 邊界規則，本輪不介入、不回覆、不修文，純觀察留痕。

### 事實驗證結論 / 文章本體修改

無。

---

## #168 X — https://x.com/taiwandotmd/status/2084520918441951650

**Metrics snapshot（2026-08-10 07:12 TPE）**：302 Views / 2 讚 / 10 轉發 / 1 回覆

較 D+5（298 views）+4，其餘三個互動數字持平。X 留言牆持續擋住深層內容，無新增可分類訊號。

---

## Adjacent health check

四篇本輪均無新增事實 callout，未觸發跨語言版本或反向連結同步檢查。

## Pattern 歸納 / 教訓

1. **黃崇仁 #165 五指標連續第三次精確持平（D+2 / D+5 / D+6 三讀完全一致）**：進一步鞏固 REFLEXES #78 Pure plateau 判斷——這篇孢子的傳播生命週期已在 D+2 前結束，後續每日 harvest 讀到的是穩態快照，不是漏抓。下次 harvest 若仍持平，可比照昨日 handoff 建議降低優先度，不需逐字重讀留言。
2. **X 兩篇孢子 views 持續緩慢自然成長（+17／+4），互動數字（likes/reposts/comments）已穩定**：X 的 view count 似乎不像 Threads 一樣在早期就完全鎖定，即便互動歸零成長，曝光仍緩慢累積——這跟 Threads 演算法推送衰減曲線不同，值得未來 batch harvest 做跨平台比較時留意（非本輪新增教訓，僅延續既有觀察）。
3. **登入層斷點連續第 2 天未解除**：斷點性質與 8/9 相同（連線層健康、登入層未恢復），不是新故障也不是惡化，是同一個待哲宇處理的 pending 項目延續。

## Handoff

- [ ] pending（給哲宇，延續，連續第 2 天）— 配對瀏覽器 Threads/X 帳號仍是登出狀態，需人工重新登入一次。這阻擋留言牆後內容讀取（14/36 則 #165 留言仍不可讀）與任何 reply-post 自動發布。本輪無 Bucket A/C/E 高信度回覆草稿因登入阻擋而延遲——兩篇孢子唯一的直接回覆都是 Bucket F/D，不觸發自動回覆需求，故本輪未因登入問題損失任何本該 ship 的內容。
- [ ] pending（給哲宇，延續）— EZWAY 報關孢子所處話題環境持續政治化（財政部關貿網路持股爭議），本輪未見對 Taiwan.md 孢子本身的直接事實挑戰，純留痕供參考，無需回應動作。

## 下次 harvest 建議時機

D+7（2026-08-11 06:30 cron，主排程窗口最後一天）。優先事項：

1. 確認登入態是否恢復；若恢復，優先讀取 #165 牆後 14 則留言 + 確認 3 則累積待 ship 的 Bucket E reply draft（@haoyingmiao／@daphne.globalsun／@huwenxian54，8/5-8/6 累積，因登入阻擋延至今日仍未 ship）能否補發
2. 黃崇仁孢子若 D+7 仍持平，可正式視為生命週期結束，之後轉 milestone harvest（D+14/D+30）
