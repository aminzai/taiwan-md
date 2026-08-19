---
spores: '#170, #171'
harvest_date: '2026-08-12 06:35'
harvest_window_day: 'D+1'
batch_reason: 'daily twmd-spore-harvest-am cron cycle — v1.15.0「長出複眼」release 孢子 D+1 首次 harvest（唯一在 D+1-D+7 窗口內的孢子）'
triggered_by: 'cron'
reply_count: '0 則外部讀者留言需要分類或回覆'
---

# Harvest batch — v1.15.0「長出複眼」release 孢子 #170/#171（D+1 首次 harvest）

## 環境狀態：Chrome MCP 連線正常，Threads 登入態延續

`list_connected_browsers` 回配對裝置正常。navigate 到 `@taiwandotmd` 後畫面顯示「編輯個人檔案」、左側選單完整（訊息／動態／洞察報告／已儲存），確認登入態延續前幾輪的恢復狀態。X 端仍是未登入態（右側顯示「Log in or sign up for X」），符合 pipeline §Threads-only 操作鐵律的既有限制，本輪未嘗試登入，改用公開頁面讀取指標。

---

## #170 Threads — https://www.threads.com/@taiwandotmd/post/Db591ugI6tB

**Metrics snapshot（2026-08-12 06:35 TPE）**：758 次瀏覽 / 43 讚 / 2 轉發 / 0 則外部回覆

貼文是雙串文（1/2 主文 + 2/2「完整故事」連結卡片），a11y tree 讀到主文按鈕標示「已回覆 1」——這是作者自己接續的 2/2 串文，不是讀者留言；主貼與續貼下方留言區均無外部讀者回覆。2/2 續貼另有 6 讚、0 回覆、0 轉發。D+1 首次 harvest，無歷史數值可比對。

### 分類結果 / 事實驗證結論 / 文章本體修改

無留言可分類，無新增可驗證事實 callout，文章本體無修改。

---

## #171 X — https://x.com/taiwandotmd/status/2087208201729249614

**Metrics snapshot（2026-08-12 06:40 TPE）**：1,406 Views / 51 讚 / 6 轉發 / 12 書籤 / 0 回覆

X 端未登入，公開頁面即可讀到完整指標列（回覆／轉發／讚／書籤四個 icon 已用 zoom 確認順序，避免 8/11 #168 那種數字誤讀）。回覆 icon 旁無數字 = 0，跟主貼文案相同（同文案 + inline UTM s171），無新增可分類訊號。D+1 首次 harvest，無歷史數值可比對。

### 分類結果 / 事實驗證結論 / 文章本體修改

無留言可分類，無新增可驗證事實 callout，文章本體無修改。

---

## Adjacent health check

兩篇本輪均無新增事實 callout，未觸發跨語言版本或反向連結同步檢查。

## Pattern 歸納 / 教訓

1. **release 孢子 D+1 純指標 harvest，0 讀者留言**：v1.15.0 發布不到 24 小時，兩平台合計 2,164 views、94 讚、8 轉發，engagement 集中在 like/repost 沒有留言互動——跟過往病毒孢子（如黃崇仁、EZWAY）D+0-D+1 常見的高留言密度不同，meta release 型孢子（B 冷知識型 · meta release 里程碑）讀者反應模式偏「按讚轉發不留言」，屬正常分布不是異常。
2. **X 端未登入公開頁精確讀值＋zoom 確認 icon 順序**：延續 8/11 #168 教訓（likes/reposts 疑似連續兩天記錄互換），本輪對 4 個 X icon 主動 zoom 截圖比對順序（回覆／轉發／讚／書籤），一次到位避免同類誤讀。

## Handoff

- [ ] pending（給哲宇，延續）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（給 self-evolve 或下次 harvest）— #168（8/10-8/11 批次）likes/reposts D+5/D+6 疑似互換的資料品質問題，仍待人工確認後決定是否訂正歷史事件
- [ ] pending（給下次 harvest）— #170/#171 D+2 續追，觀察 release 孢子後續是否出現讀者留言（目前 D+1 零留言）

## 下次 harvest 建議時機

D+2（2026-08-13），依主排程窗口（D+1-D+7）每日至少一次。
