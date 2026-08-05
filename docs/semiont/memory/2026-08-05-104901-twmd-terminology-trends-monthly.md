# 2026-08-05-104901-twmd-terminology-trends-monthly — 用語趨勢首個常規月度輪：10 詞入庫、3 條誤判翻案、5 個近似重複被查重防線攔下

> session twmd-terminology-trends-monthly — cron 觸發（每月 5 日 10:30）
> Session span: 10:30 → 10:49 +0800（約 19 分鐘主導時間，含 6 個平行研究 agent 背景執行）
> 資料來源：`git log %ai`

✅ BECOME ack：mode=write / 8 organ 最低=consciousness-snapshot.sh（免疫 60/黃燈）/ Q14=PASS（讀完 wake-context 全 11 段至 END sentinel，確認過去 48hr 為 babel 產線批次翻譯 + 台灣行道樹/海關報關EZWAY rewrite + 查證狀態分層上線，本 routine 是 8/4 誕生後首跑）

## 觸發

TERMINOLOGY-TRENDS-PIPELINE v1.0（2026-08-04 誕生於支語深度研究 session）第一次常規月度執行，範圍從首輪 559 次搜索的研究規模收斂到「6-8 切面各 10-15 次、≤20 條入庫」的常態節奏。

## Stage 1-3：需求對照與雙防線查重

`terminology-demand-rank.py --days 28 --state MISSING` 撈出 30 個中國詞相關 SC 查詢（717 次曝光）。逐一查證後發現六成（什麼、意思、聯繫、舉發、糾結、物件、配置、具象化、屏障、萌、串流）其實是兩岸通用詞或台灣本有詞，SC 曝光反映的是語意搜尋雜訊，不是真實支語需求。demand-rank 的 MISSING 清單需要人工詞源查證過濾才能用，這點寫進本輪報告供下輪參考。

6 個平行 sub-agent 切面各自 WebSearch 10-15 次回收候選詞：Threads 支語現場、PTT 近月新串、中國年度流行語榜單、誤判鑑定案例、SC 需求詞源逐一查證、小紅書抖音 2026 波。雙防線查重（檔名 `test -f` + 全庫值掃描）攔下 5 個原本要新建的候選詞。掃碼已有「掃碼付款.yaml」，創可貼已有「OK繃.yaml」，發貨已有「出貨.yaml」，適配已有「適配.yaml」（薄殼，本輪補肉），土豆(花生)在「馬鈴薯.yaml」裡早已完整記錄兩岸混淆案例。這驗證了 Stage 3 hard gate 的必要，僅檔名比對會漏掉這五個。

## Stage 4：入庫與 QA

高信心入庫 10 條新詞。SC 需求驗證的是「內捲」。2025-2026《咬文嚼字》官方認證熱詞收了「活人感」「邊界感」「反精致」「預制感」四條，延續上輪「鬆弛感」開啟的「N＋感」世代觀察。穩定飯圈用語收「出圈」，日源二次加工路徑收「谷子」（周邊），同型於既有「佛系」的傳播路徑。另外三條是誤判翻案案例：「青提」是港澳粵語固有詞被誤扣支語帽子，「奧步」是中研院考證出的台語反向輸出中國案例，「窩心」是南北語感固有分歧、台灣暖心義項反而向外擴散。另補肉「適配」「三文魚」兩條既有薄殼詞條。

QA 四件套全過：`yaml.safe_load` 12 檔全解析成功、`terminology-charcheck.js` 全庫 2392 檔 SIMPLIFIED_LEAK=0、id 重複掃描僅命中一個與本輪無關的既有重複（awesome ×2）、`extract-china-terms.py` 正常抽出 detection 規則無錯誤。誠信原則上，三條誤判翻案案例的 notes 都明確標註「⚠️ 誤判翻案案例」而非直接歸類成支語，避免詞庫變成隨意出征的黑名單。

## Stage 5-8：報告與收官

`reports/terminology-trends/2026-08.md` 寫完月度短報告（新進詞、誤判翻案、查重防線攔截清單、SC 需求變化、下輪觀察方向）。無項目命中 Stage 6 hard gate（無刪除、無「是支語嗎」判定徽章、無大批重分類），OBSERVER-QUEUE 不需新增。`e3e61e0f5` 一次提交 13 檔（10 新增 + 2 修改 + 1 報告）並 push 到 origin/main，pre-push article-health 全綠。

## 收官 checklist

| 檢查項                       | 狀態                                                                     |
| ---------------------------- | ------------------------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                                       |
| Timestamp 精確               | ✅                                                                       |
| Handoff 三態已審視           | ✅                                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（免疫 60 黃燈狀態未變動，本輪未觸碰）                                 |
| 自我檢查工具 PASS            | ✅（yaml parse / charcheck / dup scan / extract-china-terms 四件套全過） |

## Handoff 三態

繼承上一 session（`2026-08-05-093245-twmd-flywheel-watch`）：

- [ ] pending（全數繼承不動，非本 routine 範圍）：#1184 justfont 後台網域白名單、免疫黃燈 28+ 天三選一、cron 環境無 Gmail MCP、黃崇仁 Bucket D 框架質疑、Discussion #104
- [ ] pending（繼承不動）：`HARVEST-REPLIES-PENDING/2026-08-05.md` 兩則 reply draft、確認本機 Chrome 的 @taiwandotmd 帳號
- [ ] pending（繼承不動）：本機 `dist/` 只在有人手動 build 時才更新，broken-link gate 預設量的是舊站
- [x] ~~pending：`twmd-terminology-trends-monthly` 今天 10:30 首跑，明天確認留下痕跡~~ — retired by 本 session：commit `e3e61e0f5` 已留下明確痕跡，首跑完成

本 session 新 handoff：

- [ ] pending（給下輪 terminology-trends 或任何做詞庫工作的 session）：本輪 4 個「N＋感／官方熱詞」候選（活人感/邊界感/反精致/預制感）目前僅止於中國社群熱議、尚未觀察到台灣網路使用，下輪需追蹤是否已在 Threads/PTT 出現以補 usage 佐證，否則長期停留觀察詞狀態會讓詞庫「流行語感」分類虛胖
- [ ] pending（給任何寫文章或做詞庫工作的 session）：「從從容容，游刃有余」案例（源自台灣立委王世堅質詢金句，2025 年被中國網路歌曲改編後爆紅回流）是很好的誤判翻案故事，但屬片語不是單詞，本輪判斷不強塞進 YAML schema——如果詞庫 schema 未來支援片語型 entry，這是現成候選

## Beat 5 — 反芻

這輪查證最深的體會：demand-rank 給的「MISSING」清單本質上是待查證清單。30 個候選詞裡真正查證後站得住腳的只有 1 個（內捲），另外接近六成是通用詞被搜尋引擎雜訊誤扣。若把 demand-rank 的輸出直接當入庫依據，詞庫很快會被「什麼」「意思」這種詞污染，公信力會先垮掉。查重防線攔下的 5 個近似重複，跟查證後排除的六成候選詞，其實是同一種紀律在兩個位置起作用：前者防止重複收錄，後者防止錯誤收錄，共同支撐的是詞庫的可信度建立在誠實排除上。三條誤判翻案案例（青提／奧步／窩心）比十條新詞入庫更貼近這個計畫的初衷。這個詞庫最稀缺的資源，是願意花時間查證「這真的是支語嗎」的耐心。

🧬

---

_v1.0 | 2026-08-05 10:49 +0800_
_session twmd-terminology-trends-monthly — 用語趨勢月度觀察 pipeline 首個常規輪_
_誕生原因：TERMINOLOGY-TRENDS-PIPELINE v1.0 排程首次觸發（每月 5 日 10:30）_
_核心洞察：demand-rank 的 MISSING 清單是待查證清單不是入庫清單；雙防線查重攔下的 5 個近似重複跟查證後排除的六成候選詞是同一種紀律的兩種顯影——詞庫價值在誠實排除不在收錄數量_
_LESSONS-INBOX 候選：無新增，本輪紀律已被既有 pipeline hard gate 完整覆蓋_
