---
spores: '#170, #171'
harvest_date: '2026-08-13 06:40'
harvest_window_day: 'D+2'
batch_reason: 'daily twmd-spore-harvest-am cron cycle — v1.15.0「長出複眼」release 孢子 D+2 續追（唯一在 D+1-D+7 窗口內的孢子，per dashboard-spores.json backfillWarnings）'
triggered_by: 'cron'
reply_count: '1 則外部讀者留言可讀（X 端 3 則回覆中 2 則被登入牆擋住，Threads 端 0 則）'
---

# Harvest batch — v1.15.0「長出複眼」release 孢子 #170/#171（D+2）

## 環境狀態

`list_connected_browsers` 回配對裝置正常。Login-state probe：navigate 到 `@taiwandotmd` profile 顯示「編輯個人檔案」按鈕與完整選單（訊息／動態／洞察報告／已儲存／附帶原始貼文的回覆），Threads 登入態延續。X 端本輪同樣未登入（頁面顯示「Log in or sign up for X」），符合 pipeline §Threads-only 操作鐵律既有限制，公開頁面可讀貼文本體指標與第 1 則回覆，其餘回覆被登入牆擋住。

---

## #170 Threads — https://www.threads.com/@taiwandotmd/post/Db591ugI6tB

**Metrics snapshot（2026-08-13 06:35 TPE）**：1,264 次瀏覽 / 87 讚 / 4 轉發 / 0 則外部讀者回覆（較 D+1：758→1,264 瀏覽、43→87 讚、2→4 轉發）

主貼「1/2」下方留言區僅有作者自己的「2/2 完整故事」續貼（9 讚 / 0 回覆 / 0 轉發），無任何外部讀者留言。checkmark icon 顯示的「1」是作者自己接續的串文計數，不是讀者回覆。

### 分類結果 / 事實驗證結論 / 文章本體修改

無留言可分類，無新增可驗證事實 callout，文章本體無修改。

---

## #171 X — https://x.com/taiwandotmd/status/2087208201729249614

**Metrics snapshot（2026-08-13 06:40 TPE，未登入公開頁）**：約 2 萬次瀏覽（X 未登入視角只顯示四捨五入級距，非精確值）/ 323 讚 / 47 轉發 / 58 書籤 / 3 則回覆（較 D+1：1,406→~20,000 瀏覽、51→323 讚、6→47 轉發、12→58 書籤、0→3 回覆）。Icon 順序本輪再次 zoom 確認：💬回覆 3 / 🔁轉發 47 / ♡讚 323 / 🔖書籤 58（延續 8/11 #168 教訓，每次讀值前先確認四個 icon 順序，避免誤讀）。

**可讀到的 1 則回覆**（其餘 2 則被 X 登入牆擋住，`read_page` a11y tree 顯示兩個「Loading post」placeholder 永不 resolve，符合 pipeline §Pitfall 2 X reply lazy-load 已知限制）：

> @TaiwanAny（「Taiwan not vote with any China」，10h，該則回覆本身 304 次瀏覽）：
> 「會不會被敵人拿去利用? 侵害台灣國家利益」

### 分類結果

該則回覆不是可查證的事實主張，也不是正面互動，而是對「公開講出十三道品質閘門曾誤殺自己合格譯文」這件事本身的策略疑慮——質疑公開揭露弱點是否會被對手利用、傷害台灣的國家利益。這比較接近 **Bucket D（Critical-balance framing）**：不是在挑戰文章的具體史實或用詞，是在質疑「公開這件事」的判斷本身，屬於策略／立場層次的疑慮。

### 事實驗證結論 / 文章本體修改

不適用（非事實主張）。

### 處置

per Bucket D SOP：不自動回覆、不修改孢子或文章。寫入下方 Handoff 供哲宇 review，不在本輪主動介入。X 另外 2 則回覆因登入牆無法讀取內容，本輪先記錄缺口，待哲宇登入態恢復或人工查看後補齊分類。

---

## Adjacent health check

本輪唯一的讀者訊號是策略疑慮而非事實 callout，不觸發跨語言版本或反向連結同步檢查。

## Pattern 歸納 / 教訓

1. **release 孢子 D+2 仍以按讚轉發為主，留言密度低但開始出現**：D+1 兩平台合計 0 則外部留言，D+2 首次出現 1 則可讀留言（X 端），內容是策略疑慮而非事實勘誤——跟 MANIFESTO §12 受眾端飛輪講的「事實勘誤」訊號不同類型，是讀者對「公開示弱是否有戰略風險」的疑慮，屬於 Bucket D 而非 Bucket A/B/C。
2. **X 未登入公開頁只能讀到第一則回覆**：3 則回覆中 2 則被登入牆擋住（`read_page` 顯示兩個永久 loading 的 placeholder），這是本輪第一次在同一則孢子上實際遇到「回覆數 > 可讀回覆數」的落差，跟 8/10 login-restore session 發現的「harvest 只掃第一層留言」是不同層的缺口（那次是 Threads 巢狀層，這次是 X 未登入視角的截斷）——兩者共同指向同一種盲點模式：harvest 讀到的「留言全貌」實際上受限於當下的登入 / 展開狀態，缺席不會在報告上留下空格。
3. **X views 未登入視角只回捨入級距**（「2萬」而非精確數字），記錄時如實標註為約略值，不假裝精確。

## Handoff

- [ ] pending（給哲宇，延續）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（給 self-evolve 或下次 harvest）— #168（8/10-8/11 批次）likes/reposts D+5/D+6 疑似互換的資料品質問題，仍待人工確認後決定是否訂正歷史事件
- [ ] pending（給哲宇，Bucket D 待拍板）— #171 X 回覆 @TaiwanAny「會不會被敵人拿去利用? 侵害台灣國家利益」— 策略疑慮，非事實錯誤，per §自主權邊界政治立場條款不自動回覆，需哲宇決定是否／如何回應
- [ ] pending（給下次 harvest）— #171 X 另外 2 則回覆本輪因登入牆無法讀取，待哲宇 X 登入態恢復後補齊分類
- [ ] pending（給下次 harvest）— #170/#171 D+3 續追（明日）

## 下次 harvest 建議時機

D+3（2026-08-14），依主排程窗口（D+1-D+7）每日至少一次。
