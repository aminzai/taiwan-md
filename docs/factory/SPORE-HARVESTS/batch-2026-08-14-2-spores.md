---
spores: '#170, #171'
harvest_date: '2026-08-14 06:40'
harvest_window_day: 'D+3'
batch_reason: 'daily twmd-spore-harvest-am cron cycle — v1.15.0「長出複眼」release 孢子 D+3 續追（唯一在 D+1-D+7 窗口內的孢子，per dashboard-spores.json backfillWarnings）'
triggered_by: 'cron'
reply_count: '1 則外部讀者留言可讀（X 端 4 則回覆中僅 1 則登入牆外可見，Threads 端 0 則）'
---

# Harvest batch — v1.15.0「長出複眼」release 孢子 #170/#171（D+3）

## 環境狀態

`list_connected_browsers` 回配對裝置正常。Login-state probe：navigate 到 `@taiwandotmd` Threads profile 顯示「編輯個人檔案」按鈕與完整選單（訊息／動態／洞察報告／已儲存／附帶原始貼文的回覆），Threads 登入態延續。X 端本輪仍未登入（頁面顯示「Log in or sign up for X」），跟 D+2 相同，login-state 尚未恢復。

---

## #170 Threads — https://www.threads.com/@taiwandotmd/post/Db591ugI6tB

**Metrics snapshot（2026-08-14 06:35 TPE）**：1,328 次瀏覽 / 89 讚 / 4 轉發 / 1 書籤 / 0 則外部讀者回覆（較 D+2：1,264→1,328 瀏覽、87→89 讚、轉發持平 4）

主貼「1/2」下方留言區僅有作者自己的「2/2 完整故事」續貼（10 讚 / 0 回覆 / 0 轉發），無任何外部讀者留言。checkmark icon 顯示的「1」再次確認是作者自己接續的串文計數，不是讀者回覆（跟 D+2 判讀一致）。

### 分類結果 / 事實驗證結論 / 文章本體修改

無留言可分類，無新增可驗證事實 callout，文章本體無修改。

---

## #171 X — https://x.com/taiwandotmd/status/2087208201729249614

**Metrics snapshot（2026-08-14 06:40 TPE，未登入公開頁）**：約 2.4 萬次瀏覽（X 未登入視角只顯示四捨五入級距，非精確值）/ 350 讚 / 52 轉發 / 59 書籤 / 4 則回覆（較 D+2：~20,000→~24,000 瀏覽、323→350 讚、47→52 轉發、58→59 書籤、3→4 回覆）。Icon 順序本輪 zoom 確認一致：💬回覆 4 / 🔁轉發 52 / ♡讚 350 / 🔖書籤 59。

**可讀到的 1 則回覆**（其餘 3 則被 X 登入牆擋住，公開頁只渲染第一則）：

> @TaiwanAny（「Taiwan not vote with any China」，8月12日）：
> 「會不會被敵人拿去利用? 侵害台灣國家利益」

跟 D+2 讀到的同一則（回覆計數從 3 增至 4，代表本輪期間新增 1 則回覆，但登入牆下無法讀到新增那則的內容）。

### 分類結果

同 D+2 判定：**Bucket D（Critical-balance framing）**——質疑「公開揭露品質閘門曾誤殺自己合格譯文」這件事本身是否會被對手利用、傷害台灣國家利益，屬策略／立場層次疑慮，非事實主張。

### 事實驗證結論 / 文章本體修改

不適用（非事實主張）。

### 處置

per Bucket D SOP：不自動回覆、不修改孢子或文章。沿用 D+2 已寫入的 Handoff，待哲宇 review。X 新增的第 4 則回覆因登入牆無法讀取內容，本輪先記錄缺口，待哲宇登入態恢復或人工查看後補齊分類。

---

## Adjacent health check

本輪唯一的讀者訊號延續 D+2 的策略疑慮（同一則），不觸發跨語言版本或反向連結同步檢查。

## Pattern 歸納 / 教訓

1. **X 登入牆連續第二天擋住多數回覆**：D+2 3 則回覆讀到 1 則，D+3 回覆數增至 4 則仍只讀到同 1 則——login-state 尚未恢復，缺口持續累積而非單日偶發，值得升級為「連續 N 天」訊號留給哲宇而非每天各自記一筆。
2. **Threads 端連續兩輪 0 外部回覆，僅按讚轉發緩慢成長**：1,264→1,328 瀏覽（+5%）、87→89 讚，屬正常 release 孢子長尾衰減曲線，非異常。

## Handoff

- [ ] pending（給哲宇，延續）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
- [ ] pending（給 self-evolve 或下次 harvest）— #168（8/10-8/11 批次）likes/reposts D+5/D+6 疑似互換的資料品質問題，仍待人工確認後決定是否訂正歷史事件
- [ ] pending（給哲宇，Bucket D 待拍板，延續 D+2）— #171 X 回覆 @TaiwanAny「會不會被敵人拿去利用? 侵害台灣國家利益」— 策略疑慮，非事實錯誤，per §自主權邊界政治立場條款不自動回覆，需哲宇決定是否／如何回應
- [ ] pending（給下次 harvest，連續第二輪）— #171 X 登入牆擋住的回覆從 2 則累積到 3 則未讀，待哲宇 X 登入態恢復後一次補齊分類
- [ ] pending（給下次 harvest）— #170/#171 D+4 續追（明日）

## 下次 harvest 建議時機

D+4（2026-08-15），依主排程窗口（D+1-D+7）每日至少一次。
