# 大罷免 — Stage 3.6 成品總驗三關 audit

- article: knowledge/History/大罷免.md（觸發：A 級＋預期大眾政治題，HARD）
- 執行：2026-07-16，與 stage35 同 round

## 3.6.1 原子重驗 fan-out

3 個 adversarial verifier 按**成品段落**分工（非研究子題切法），四種 drift 全數掃過：

1. **引號逐字 diff**：抓到 2 處——陳曉煒「20 份」（編輯自算和塞引號）、判決理由「貪圖便利」（媒體轉述兩版本不一致）→ 分別還原逐字／de-quote。其餘全部引語（簡嘉佑×2、幫幫忙、小詩、朱立倫、黃國昌、柯建銘、游盈隆、布羅德斯基、中選會、Templeman、GTI、Brookings 英文句）逐字 hold。
2. **詮釋 gloss**：抓到 2 處——Taiwan Insight「組織上獨立於民進黨」（推論延伸）、「Everyone was glad…」歸屬（實為 Polk 1848 語、作者借喻）→ 均改寫。柯建銘「一手策畫」的轉述式指控 framing 經冷 context verifier 確認正確（2B 炎上席修正在成品層兌現）。
3. **footnote-claim 綁定**：抓到 5 處掛錯或弱錨（[^2]/[^4]/[^5]/[^25]/[^29]/[^40]/[^42]）→ 全部 repoint 或拆分（新增 [^49]-[^52]）。
4. **writer 自漂移（superlative＋日期高發區）**：抓到 3 處——「隔年」（憲判日期）、「前一個月」（總預算時序）、「近 300 天」（來源無此數）→ 全部修正。plugin `quote-fidelity` QF2 列的 superlative 原子（「唯一」×2「史上第一次」）逐條對源 hold（陳柏惟唯一有 CNA 雙源、總預算跨年首次有今周刊）。

## 3.6.2 順稿

- 281 字牆段（徐巧芯答辯段）→ 拆兩段（R4）
- 開場「加上兩週前…這一波」指代含糊 → 重寫為「二十五案同日投票」
- timeline 模組兩列與正文時序對齊（2024/12 三法／2025/01 總預算＋聯盟）
- 修正後全文重讀：段間 narrative bridge 完整、「尺的第 X 格」母題七次變奏無複誦感（2E 論點兌現席逐字對照確認）；prose-health score 3 ≤ 3 pass

## 3.6.3 視覺同步

- hero 青鳥人潮（概覽前）／議場標語圖貼 s2 職權修法段（Tier A 主體）／曹興誠圖貼 s3 聯盟段（人物對位）／公視 iframe 貼 s4a 攻防段（內容同構：正反陣營拚聲量）——媒體與旁鄰 prose 全部同題
- caption 全數具體非泛用；媒體不相鄰堆疊；結尾前無新媒體（靜止收尾）；`</div>` 與 `_caption_` 間空行 ✓
- 7 個 tw-\* 模組全部有「來源：」列（viz-health hard=0）；模組數字與 prose 一致（checker C 逐項驗算）

## Result: PASS
