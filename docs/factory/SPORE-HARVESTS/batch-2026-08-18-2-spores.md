---
spores: '#170, #171'
harvest_date: '2026-08-18 06:40'
harvest_window_day: 'D+7'
batch_reason: 'daily twmd-spore-harvest-am cron cycle — v1.15.0「長出複眼」release 孢子 D+7 續追（唯一在 D+1-D+7 窗口內的孢子，per dashboard-spores.json backfillWarnings；D+7 為主排程窗口最後一天）'
triggered_by: 'cron'
reply_count: '1 則外部讀者留言可讀（X 端 4 則回覆中僅 1 則登入牆外可見，Threads 端 0 則）'
---

# Harvest batch — v1.15.0「長出複眼」release 孢子 #170/#171（D+7，主排程窗口最後一天）

## 環境狀態

`list_connected_browsers` 回配對裝置正常（單一 local browser）。Login-state probe：navigate 到 `@taiwandotmd` Threads profile 顯示「編輯個人檔案」按鈕與完整選單，Threads 登入態延續。X 端本輪仍未登入（頁面顯示「Log in or sign up for X」＋「Continue to X」蓋板），**連續第七輪未恢復**（D+1 起首次記錄，D+2〜D+7 持續）。

---

## #170 Threads — https://www.threads.com/@taiwandotmd/post/Db591ugI6tB

**Metrics snapshot（2026-08-18 06:40 TPE）**：1,349 次瀏覽 / 89 讚 / 1 引用 / 4 轉發 / 1 分享（較 D+6：1,344→1,349 瀏覽 +5，讚／轉發／分享持平）

主貼「1/2」下方留言區僅有作者自己的「2/2 完整故事」續貼（10 讚 / 0 回覆 / 0 轉發），無任何外部讀者留言，跟 D+3〜D+6 判讀一致——已連續第六輪 0 外部回覆。

### 分類結果 / 事實驗證結論 / 文章本體修改

無留言可分類，無新增可驗證事實 callout，文章本體無修改。

---

## #171 X — https://x.com/taiwandotmd/status/2087208201729249614

**Metrics snapshot（2026-08-18 06:40 TPE，未登入公開頁）**：2.4 萬次瀏覽（級距顯示未變）/ 351 讚 / 51 轉發 / 60 書籤 / 4 則回覆（較 D+6：轉發 52→51，其餘四項數字持平；51 落在 D+4 也出現過的既有波動帶內，非新異常）。Icon 順序本輪核對一致：💬回覆 4 / 🔁轉發 51 / ♡讚 351 / 🔖書籤 60。

**可讀到的 1 則回覆**（其餘 3 則被 X 登入牆擋住，公開頁只渲染第一則）：

> @TaiwanAny（「Taiwan not vote with any China」，8月12日）：
> 「會不會被敵人拿去利用? 侵害台灣國家利益」（497 次瀏覽，與 D+6 持平）

跟 D+2〜D+6 讀到的同一則，回覆計數維持 4，未見新增。

### 分類結果

同 D+2〜D+6 判定：**Bucket D（Critical-balance framing）**——質疑「公開揭露品質閘門曾誤殺自己合格譯文」這件事本身是否會被對手利用、傷害台灣國家利益，屬策略／立場層次疑慮，非事實主張。

### 事實驗證結論 / 文章本體修改

不適用（非事實主張）。

### 處置

per Bucket D SOP：不自動回覆、不修改孢子或文章。沿用 D+2〜D+6 已寫入的 Handoff，待哲宇 review。

---

## Adjacent health check

本輪唯一的讀者訊號延續 D+2〜D+6 的策略疑慮（同一則），不觸發跨語言版本或反向連結同步檢查。

## Pattern 歸納 / 教訓

1. **X 轉發數在既有波動帶內小幅回落（52→51）**：views/likes/comments/shares 四項數字跟 D+6 逐位對齊，僅轉發數波動 1，且 51 這個值 D+4 已出現過，屬既有量測雜訊，非新訊號。長尾曲線持續處於平台期。
2. **Threads 端連續第六輪 0 外部回覆**：1,344→1,349 瀏覽（+0.4%），互動基本持平。
3. **X 登入牆滿七天未恢復**：已從「單日缺口」累積成跨週未解的環境前置條件缺口，延續單一累積訊號的寫法，不逐日重複記錄。
4. **D+7 為主排程窗口最後一天**：per SPORE-HARVEST-PIPELINE §主排程，D+1-D+7 每日至少 1 次的 cadence 到今天收尾，之後轉 D+14/D+30 milestone harvest 節奏——下次針對 #170/#171 的 harvest 預期是 2026-08-25（D+14）左右，非明日繼續每日追。

## Handoff

- [ ] pending（給哲宇，延續）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（給 self-evolve 或下次 harvest）— #168（8/10-8/11 批次）likes/reposts D+5/D+6 疑似互換的資料品質問題，仍待人工確認後決定是否訂正歷史事件
- [ ] pending（給哲宇，Bucket D 待拍板，延續 D+2〜D+6）— #171 X 回覆 @TaiwanAny「會不會被敵人拿去利用? 侵害台灣國家利益」— 策略疑慮，非事實錯誤，per §自主權邊界政治立場條款不自動回覆，需哲宇決定是否／如何回應
- [ ] pending（給哲宇）— X 登入態連續第七天未恢復（D+1 起），3/4 則 #171 回覆持續讀不到內容，建議哲宇有空時重新登入該瀏覽器的 X 帳號
- [ ] pending（給下次 harvest）— #170/#171 D+7（2026-08-18）主排程窗口已收尾，下次針對這批孢子的 harvest 轉為 D+14（約 2026-08-25）milestone 節奏，非明日繼續 daily追

## 下次 harvest 建議時機

D+14（約 2026-08-25），milestone harvest（Step 1+5+7，只抓新留言歸檔）。主排程 D+1-D+7 daily cadence 今天（D+7）收尾。
