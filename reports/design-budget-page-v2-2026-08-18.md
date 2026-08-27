---
title: 'design-budget-page-v2-2026-08-18'
description: 'EVOLVE Mode 4 設計＋研究報告：/budget「總預算十年」上線第二天的視覺化、資訊結構與手機版體檢——量測 5 組截圖（desktop／390／dark／en／en-390）、逐區逐圖診斷、發散兩案、定案十七項升級與驗收。'
type: 'migration-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-18
last_session: '2026-08-18-budget-v2'
related:
  - 'design-ly-budget-page-2026-08-17.md'
  - 'research/2026-08/ly-budget-research-D.md'
  - '../docs/editorial/graph.md'
  - '../docs/pipelines/EVOLVE-PIPELINE.md'
  - '../src/templates/budget.template.astro'
  - '../src/styles/budget.css'
---

# 總預算十年 v2：讓圖在手機上讀得到，讓每張圖只說一件事

> EVOLVE-PIPELINE **Mode 4**（THINK → DIVERGE → REPORT → IMPLEMENT，報告先於實作）。
> 觸發：哲宇 2026-08-18「派一支 fable agent 對整理視覺化、全面資訊結構優化、還有手機版做完整的深度研究報告＋進化升級，讓人看得懂、有洞見，圖表跟 UI/UX 對閱讀跟互動的人更有幫助」。
> 量測工具：repo 內 playwright（`budget-shot.mjs`，用完刪），五組（desktop 1280／mobile 390／dark／en／en-390）逐區逐圖截圖＋DOM 量測，截圖與 `before-measure.json` 在 `scratchpad/budget-v2/`。dataviz 調色驗證：`validate_palette.js` 光暗兩套八槽全 PASS（光版 3 槽對底 <3:1，靠直接標籤與縫隙補救，屬允許的 WARN）。

---

## 〇、一句話結論

昨天的頁在桌機上成立，在手機上沒有：八張 SVG 在 390px 寬的最小字級是 **4.5px**（viewBox 760 縮到 324px，比例 0.426），設計報告 §九.3 寫的「min-width 560 ＋橫向捲動」沒有進 CSS。這一輪最重要的一件事是**每張圖同時算兩套幾何（寬 760／窄 380），用 CSS media query 切換**，不橫向捲動、不放大字、不做兩套資料；第二件是把「一張圖一件事」補齊：河流圖把「提案與法定之間的距離」畫成看得見的色帶、100% 堆疊面積改成占比 slope、執行率從「看不出差別的子彈條」改成「一目了然的百分比量表」；第三件是資訊結構：hero 的目錄從八個名詞升成八句 takeaway（三分鐘版），加一條黏頂子導覽，§0 流程加一列七站總覽讓手機讀者三秒知道全貌。

---

## 一、現況診斷（每一區一段：讀者看到什麼、卡在哪、截圖）

量測摘要（`before-measure.json`）：

| 量 | desktop 1280 | mobile 390 | en 1280 | en 390 |
| --- | --- | --- | --- | --- |
| 頁高 | 20,391px | 23,417px（26 屏） | 23,441px | 28,886px（32 屏） |
| 首屏到第一張 SVG | 2,941px | 3,860px（4.3 屏） | 3,656px | 4,862px（5.4 屏） |
| SVG 顯示寬／比例 | 989px／1.30 | 324px／0.426 | 同左 | 同左 |
| SVG 最小字級 | 13.7px | **4.5px** | 13.7px | **4.5px** |
| 末端標籤出框 | 0 | 0 | fn-abs 3、fn-share 3、multi 2 | 同左 |
| 最長區 | §5 3,652px | §5 5,273px | §5 4,340px | §5 6,563px |
| §0 流程區 | 1,653px | 2,688px | 2,091px | 3,283px |

- **Hero**（`before-desktop-00-fold.png`、`before-mobile-00-fold.png`）：H1、副標、詩句、四張 stat、一列八個目錄字。stat 在手機二欄不換行，好。目錄只是名詞（「十年河流」「立法院的手」），沒告訴讀者每一區的結論；en 版第三張 stat 顯示 **`NT$48000M`**（`fmtYi` 的英文分支把 480 億拼成 `480`+`00M`），是格式 bug（`before-mobile-en-bp-hero-stats.png`）。
- **§0 預算怎麼過**（`before-desktop-s0.png`、`before-mobile-s0.png`）：七張等重卡片，桌機 4+3 兩排、手機一路排到 2,688px（en 3,283px）。內容正確、法源齊，但沒有一眼看得到「七站順序」的總覽，手機讀者要滑三屏才知道有七站；「351 天的故事」只在第三張卡最下面一行紅字，沒有任何時間比例的視覺。
- **§1 十年河流**（`before-desktop-s1.png`、`before-dark-chart-c-river.png`）：三線都擠在 y 軸 2–3 兆，0–4 兆的下半張是空的；lede 說「兩條線之間的距離就是這一頁要講的事」，但 114 年度提案 3.13 兆對法定 2.92 兆的缺口在圖上只有幾個像素，法定線下方整片面積填色又把時期底色帶蓋掉。dark 版「立法院法定」末端標籤被 `.bg-s0.bg-endlab { stroke }` 規則描成藍色描邊字（文字穿了序列色，違反 dataviz「text never wears the data color」）。第二張 GDP／債務圖標題是名詞（「歲出占 GDP 比率與債務比率」），40.6% 法定上限只在段落裡。
- **§2 錢往哪裡去**（`before-desktop-s2.png`、`before-en-chart-c-fn-abs.png`）：兩張同形的堆疊面積（絕對值＋100%），九類八色＋灰超過 dataviz 序列梯的 7–8 槽上限；細層（社區環保、一般補助、債務）在絕對值圖上沒有末端標籤，值只在表格；en 版右邊界寫死 150px，「Education, science & cul」「General administration 3」被裁掉；y 軸在英文頁仍印「4兆」。100% 版要回答的是「誰升誰降」，Datawrapper 原話「If you want to show that one share overtook another one, consider a line chart instead」（研究 D §3）——堆疊面積的層在中間，讀者比較的是厚度差，不直觀。
- **§3 部會的十年**（`before-desktop-s3.png`、`before-en-chart-c-multi.png`、`before-mobile-chart-c-rank.png`）：排序條 22 列在桌機清楚；圖例兩項座標寫死（x=78），「115 年度（提案）」和「105 年度」黏在一起。小倍數 16 格 4 欄，en 版機關全名與 `+75%` 撞字（「Ministry of National Defense+75%」），手機整張縮到 324px 沒有一格能讀；「105＝100 指數」讀者要換算，只有右上角 `+154%` 是人話。
- **§4 立法院的手**（`before-desktop-s4.png`）：刪減比例折線是全頁形狀最好的一張（八年平、一年尖、一年回落）；但「八年窄帶 1.0–1.25%」只在標題，圖上沒有帶；kicker 第三句「日曆卻翻到了八月」在這一區沒有任何視覺對應（逐年三讀日期不在資料層）。刪凍表桌機雙欄、手機單欄，可讀。
- **§5 兩年的角力**（`before-desktop-s5.png`、`before-mobile-s5.png`）：全頁最長（手機 5,273px）。三張「幾天」卡是三個大數字，沒有比例；18 條時間軸每條等距，2024-01 到 2026-08 的兩年半被壓成一樣的行距，「在門外站了三百多天」看不出長度；文化表與三方說法是文字層，正確但密。
- **§6 編了，花了多少**（`before-desktop-s6.png`、`before-mobile-chart-bp-defense.png`）：子彈條的灰軌（法定）被藍條（決算 97%）幾乎蓋滿，讀者眼睛讀到的是「條一年比一年長」（那是預算規模，§1 講過了），執行率只剩條尾文字——視覺通道沒有編碼 takeaway。國防四塊積木在手機最後一段 654 被裁成「6…」（dataviz 反例：`overflow: hidden` 裁掉標籤）；「政事別國防 5,488」只在 figcaption，沒標在條上。
- **§7 怎麼讀**（`before-desktop-s7.png`）：六張口徑卡＋來源＋下載＋延伸閱讀，結構清楚；「每人 12.8 萬」這個最有感的換算埋在第四張卡。
- **通用**：所有圖表 hover tooltip 只有折線圖有 JS 交叉線，其餘靠 SVG `<title>`（touch 裝置看不到）；目錄不黏頂，20,000px 長頁只靠右下角「回頂」；每張圖的 `<details>` 資料表預設收合（次要層，可收）。

---

## 二、資訊結構重排提案

### 案 A：流程開頭（現況）＋三分鐘版覆蓋

保留九區順序（§0 流程在前，因為「提案／法定／決算」是後面每張圖的前置知識，也是哲宇 8/17 明確要求放開頭的資訊圖表），但在 hero 加一層「三分鐘版」：把八個目錄名詞升級成八句 takeaway（每句都是該區 H2 的濃縮，也是跳轉連結）；§0 加一列七站總覽 chip，手機讀者先看到全貌再往下滑卡片。長區不合併，只加黏頂子導覽讓讀者知道自己在哪。

### 案 B：結論先行、流程後置

hero 之後直接進 §1 河流，§0 流程移到 §6 之後、§7 之前當「附錄：預算怎麼過」；§5 兩年的角力拆成 §5a（時間：日曆條＋天數）與 §5b（文化與媒體：表＋三方說法）；§2／§3 合併成「錢往哪裡去（政事別＋機關別）」一區。

### 判準與定案

| 判準 | 案 A | 案 B |
| --- | --- | --- |
| 哲宇 8/17 directive「開頭要一段預算要經過哪些流程」 | 守住 | 違反，需回頭問 |
| 首屏到第一張圖距離（mobile 3,860px） | 靠七站總覽＋卡片瘦身縮短，仍在 §0 之後 | 直接縮到 ~1,200px |
| 破壞 cross-ref | 無（anchor `#s0`–`#s7` 不動，其他語言 route、lang-switch、延伸閱讀 chip 都靠 id） | `#s5` 拆成兩個 id，12 語 toc key 全部重編 |
| MANIFESTO §自主權邊界 | 無 | 大改資訊架構屬「大規模重構」灰區，該先問 |
| 讀者模型 | 不懂預算的人先學會口徑，再看圖 | 懂的人直達結論 |

**採 A**。理由：三分鐘版（八句 takeaway）已經把「先給結論」做到 hero，不必搬區；§0 靠七站總覽把「全貌」壓到一屏；§5 的長度用「日曆條」把時間比例畫出來之後，文字層可以保持密度（那是資料誠實的一部分：三個天數三個起點，全部具名）。案 B 的 §5 拆分與 §2/§3 合併都值得再想，寫進 §八風險「留給人決定」。

---

## 三、圖表逐張診斷與升級

每條：現況 → 問題 → 改法 → 為什麼（錨定 graph.md 條文或 dataviz 條文；數字附算式，資料一律來自 `src/data/ly-budget.json`）。

1. **全部 SVG：兩套幾何**。現況 viewBox 760 一套；問題 390px 下字 4.5px；改法：每個元件在 frontmatter 用 `layout(W)` 算兩次（wide 760／narrow 380，實作時從 400 調到 380 才把手機刻度推到 9.8px），輸出兩個 `<svg>`，CSS `@media (max-width: 720px)` 只顯示窄版（`display:none` 的那個不進無障礙樹）；narrow 版 x 刻度改每 5 年、右邊界依最長標籤動態算、min 90 max 130；資料表只一份。為什麼：graph.md §七.⑥「手機讀得懂（字不小、不擠）」；§八反例「SVG 字級跟著容器無限放大／縮小」的反面；比橫向捲動好，因為折線圖橫捲會把 x 軸切成兩段（讀者要記住左半邊才能比右半邊）。
2. **§1 河流**：拿掉法定線下面的面積填色（它把時期底色帶蓋掉，且 dataviz「area fill 只給單序列」）；在「行政院原列」與「立法院法定」兩線之間填暖色帶（`bg-gapband`），帶寬＝刪減額；114 年度那一段自然變成全圖最寬的一段。為什麼：graph.md §三.7「一圖一重點」＋ lede 明說主角是兩線之間的距離。算式：帶高＝`proposed − legal`，2025 = 31,324.7 − 29,249.7 = 2,075.0 億。
3. **§1 GDP／債務**：h4 改斷言「歲出占 GDP 十年在 9.6–11.1% 之間；債務比從 33.0% 降到 25.2%」（`min/max(gdpPct)`＝9.59／11.14；`debtPct[0]`＝33.0、`debtPct[2025]`＝25.2），原名詞標題降成副標。40.6% 上限不畫：這個數不在資料層（只在 i18n 段落），本輪不手抄常數進 template，寫進 §八交人補資料欄位。為什麼：graph.md §三.1「標題說重點」。
4. **§2 政事別絕對值**：修 en 出框（右邊界依最長標籤估寬）；y 軸單位依語言（`兆`／`T`）；圖下加一列九類圖例（色票＋名稱＋115 年度值＋占比），DOM 文字、AI 可讀。為什麼：dataviz「legend always present for ≥2 series」；graph.md §三.12 多語標籤留呼吸；占比欄同時回應「換成占比的切換不能藏」——不做切換，並排給。
5. **§2 100% 堆疊 → 占比 slope**：新元件 `SlopeChart`，左 105、右 115，九類各一條線，兩端直接標名與 %；強調社福／國防／教科文，其餘退灰。算式：占比＝`functionsByYear[y][id] / Σ functionsByYear[y]`，105：社福 23.7%、教科文 19.7%、國防 15.9%；115：27.4%、18.3%、18.1%。中段（112–113 國防落到第四）留在段落文字，slope 不假裝有中段。為什麼：研究 D §3 Datawrapper 逐字；graph.md §二「slope（剛好兩點）」；手機上 slope 是縱向的，天生適合窄螢幕。
5b. **§2 四大支出十年成長率**（orchestrator 8/18 轉達哲宇點名的洞見）：一張四列橫條，值＝`(v115 − v105) / v105`：社福 +80.8%（8,318.0／4,600.7）、國防 +77.4%（5,488.1／3,093.0）、經濟發展 +60.3%（4,274.6／2,667.2）、教科文 +45.6%（5,566.3／3,823.8）；教科文那列強調，其餘退灰；軸從 0 起、條尾直接標 %。放在 slope 之後、段落 p1 之前，h4 斷言「四大支出裡教科文十年成長最慢：+46%，社福 +81%、國防 +77%、經濟發展 +60%」。為什麼：graph.md §三.10「強調＋灰色脈絡」（故事是「其中一個」）；§三.5 長條從 0；四列不需要圖例。用既有 `RankBars` 加 `unit="%"`。
6. **§3 排序條**：圖例改動態排（第二項 x＝第一項估寬＋24）；narrow 版標籤欄縮到 90、值標籤緊貼條尾；資料表加「占比」欄（`now / Σ agenciesByYear[115]`，國防部 18.5%、文化部 0.90%）。為什麼：graph.md §三.2 直接標籤；占比放表不放條尾，是因為 22 列條尾已有值＋增減兩個數，第三個數會變成 dataviz 反例「每個點都標數字」。
7. **§3 小倍數**：每格改成獨立 `<svg>` 放進 CSS grid（桌機 4 欄、手機 2 欄自然回流，每格 viewBox 180 寬，手機每格約 170px 顯示＝比例 0.94，字 11px）；標籤與終點值分兩行（估寬撞到就下移），en 全名不再壓字；h4 改斷言「以 105 年度為 100，勞動部走到 254、經濟部 251、財政部 86」（`2970.7/1168.0×100`＝254.3；`1480.3/590.0×100`＝250.9；`1689.4/1960.5×100`＝86.2）。為什麼：graph.md §二 small multiples 共用 y 鐵律不變；只改容器。
8. **§4 刪減比例**：加「八年窄帶」底帶（`min/max(cutPct 2016–2024)`＝1.04–1.25%，rect＋標籤「八年都在 1.04–1.25%」）；narrow 版同 1。三讀日期逐年圖不做（資料層只有 114／115 兩個日期），寫進 §八。為什麼：graph.md §三.7 annotation 是第一公民；帶的上下界從資料算，不手抄。
9. **§5 日曆條**（新元件 `CalendarStrip`）：一條 2025-08 → 2026-08 的時間軸，標「院會通過 8/21、送達 8/31、§51 期限 11/30、年度開始 1/1、付委 4/17、三讀 8/14」（前五個從 `events` 依日期取，年度開始＝`${ce}-01-01` 曆年制），§54 運作期（1/1–8/14）塗底；下方三條「天數」bar 各自從三讀日往回量 351／266／115 天並標說話者，圖註明寫「三種算法起點不同，圖上一律從三讀日往回量」。算式：8/14 往回 351 天＝2025-08-28、266 天＝2025-11-21、115 天＝2026-04-21；送達→三讀 348 天、期限→三讀 257 天（與 §0 第三站「逾期 257 天」一致）。為什麼：graph.md §二「時間」用時間軸；現況 18 條等距清單沒有時間比例；三個數字各歸說話者（MANIFESTO §自主權邊界：立體群像不裁決）。
10. **§6 執行率**：從「灰軌＋藍條」改成「每年一條 0–100% 量表」：藍＝決算÷法定，尾端淺色＝未執行，條尾標「未執行 X 億（Y%）」；圖例兩項。算式：2018 未執行＝19,669 − 19,094.1 = 574.9 億（2.92%），2022 = 371.4 億（1.65%）——十年最寬與最窄。為什麼：dataviz「A single ratio against a limit → Meter」；graph.md §三.5 長條從 0 起（0–100% 仍從 0）；原圖視覺通道編的是規模不是率。
11. **§6 國防積木**：段寬 <12% 不放段內數字（654 那段），值留圖例；條上加一根刻度線標「政事別國防 5,488」（`function_only / total`＝57.8% 位置）。為什麼：dataviz 反例「label clipped by too-small segment」；graph.md §三.11 說明公約。
12. **hero stat en 格式**：`fmtYi` 英文分支改 `≥1 兆 → NT$X.XXT`、`≥10 億 → NT$X.XB`、其餘 `NT$X00M`：480 億 → `NT$48.0B`。`fmtAxis` 加語言參數（`兆`／`T`）。
13. **末端標籤描邊 bug**：刪 `.bg-s0.bg-endlab { stroke }`；文字一律 ink token。
14. **tooltip 通用化**：一支 JS 對所有 `[data-chart]`：折線圖保留交叉線＋同 x 全序列讀數；條／段／格以 mark 為 hit target，`pointerdown`（touch）也觸發，讀 `<title>` 內容用 `textContent` 塞進 `.bg-tip`。無 JS 時原生 `<title>`＋資料表照舊。為什麼：dataviz interaction「tooltips enhance, never gate」「on bars the mark is the hit target」；graph.md §三.9 visible-by-default——tooltip 只複述已在圖上／表裡的值。
15. **黏頂子導覽**：hero 之後一條 `.bp-subnav`（八個 chip），`position: sticky; top: 56px`（站 header 固定 56px），JS IntersectionObserver 加 `.is-active`；`.bp-section { scroll-margin-top: 48px }` 補 subnav 高度（global `scroll-padding-top: 92px` 不動）。手機同一條，橫向捲動 chip。為什麼：20,000px 單頁的 wayfinding；不藏內容。
16. **三分鐘版**：hero 目錄八項各加一句 takeaway（新 key `budget.toc.sN.take`），排成兩欄卡；同一組字串在 subnav 只用短名。為什麼：graph.md §三.7「文字與圖協作」；資訊結構案 A 的核心。
17. **§0 流程**：頂上加七站 chip 總覽（三色三階段，取既有 step title）；手機卡片瘦身（誰／期限併一行、內距縮）；不收合任何內容（`what` 是各站的核心說明，收合＝藏內容；改用密度處理）。

**不做的**（列出來是為了對抗「第一個想到的方案」，也留給人決定）：政事別「切換絕對值／占比」按鈕（藏一半資訊，graph.md §三.9 鐵律，改並排）；treemap（研究 D 先例，但十一年時序才是本頁主軸，treemap 只給單年切片）；D3／Canvas 一律不碰。

---

## 四、手機版專章

- **首屏**：hero 三行詩＋四 stat＋三分鐘版八句，約 1.5 屏；八句 takeaway 是手機讀者的「摘要層」，不用滑到底才知道結論。
- **字級**：兩套幾何後，narrow 版 SVG 顯示比例 ≈ 338/380 = 0.89，`bg-tick` 11px → 9.9px、`bg-rowlab` 12px → 10.8px、末端標籤 12px → 10.8px；驗收以量測 `minTextPx ≥ 9.5` 為門檻（原 4.5）。
- **橫向捲動 vs 重排**：折線／堆疊／排序／執行率／slope／日曆條全部重排（narrow 幾何）；只有資料表 `<details>` 內的 `<table>` 保留容器內橫捲（既有 `.bg-table-wrap`）。
- **觸控互動**：`pointerdown` 顯示 tooltip，點空白處或第二次點同一 mark 關閉；交叉線折線圖在 touch 上用 `pointermove` 同樣可用。
- **黏頂目錄**：40px 高，chip 橫捲，當前區高亮；`prefers-reduced-motion` 不影響（沒有動畫）。
- **閱讀節奏**：§0 加總覽 chip；§5 日曆條讓「三百多天」有長度；§3 小倍數 2 欄回流；每區「延伸閱讀」chip 維持在區尾。
- **收合**：只有資料表與（既有的）閱讀器設定收合，其他一律可見（graph.md §三.9）。

---

## 五、互動層

無 JS 底線：所有 SVG 有 `<title>`、每張圖有 `<details>` 資料表、hero takeaway 是純連結、subnav 是純 anchor。JS 只加四件事：折線交叉線（既有）、通用 tooltip（新，含 touch）、subnav scroll-spy（新）、tooltip 內容一律 `textContent`（不用 innerHTML 拼字串——現況 `tip.innerHTML = rows.map(...)` 改掉，dataviz 「labels are untrusted data」）。不加篩選、不加切換、不加動畫。

---

## 六、定案＋實作清單

| # | 檔 | 動什麼 |
| --- | --- | --- |
| 1 | `src/utils/budgetViz.ts` | `fmtYi` en 分支修 B／T；`fmtAxis(v, unit, lang)`；新增 `estTextW(str)`（CJK 12／拉丁 6.5）供所有元件共用 |
| 2 | `src/components/budget/LineChart.astro` | `layout(W)` 兩套幾何；`gapBand`（兩序列之間填色）；`bands`（水平底帶＋標籤）；`subtitle` 副標；narrow 每 5 年一刻度；拿掉 `.bg-s0.bg-endlab` 依賴 |
| 3 | `StackedArea.astro` | 兩套幾何；右邊界動態；y 軸依語言；圖下 HTML 圖例（值＋占比）；`subtitle` |
| 4 | `RankBars.astro` | 兩套幾何；圖例動態排；表加占比欄（`shareOf` prop）；`unit="%"` 模式給四大支出成長率圖 |
| 5 | `SmallMultiples.astro` | 每格獨立 SVG＋CSS grid；標籤兩行；`subtitle` |
| 6 | `ExecutionBars.astro` | 改 0–100% 量表；未執行尾標；兩套幾何 |
| 7 | 新 `SlopeChart.astro` | 兩點斜率圖（占比 105→115），強調列，兩套幾何，資料表 |
| 8 | 新 `CalendarStrip.astro` | FY2026 日曆條＋三條天數 bar，兩套幾何，資料表 |
| 9 | `budget.template.astro` | hero 目錄→三分鐘版；subnav；§0 七站總覽；§1 拿掉 area、加 gapBand；§2 換 slope；§3 表占比；§4 band；§5 日曆條；§6 量表＋積木刻度；JS tooltip／scroll-spy 重寫 |
| 10 | `budget.css` | narrow/wide 切換、subnav、三分鐘版、七站 chip、量表、slope、日曆條、圖例列、國防刻度、修 endlab stroke |
| 11 | `src/i18n/budget.ts` | zh-TW＋en 新 key（下表）；**Read 最新版再 Edit，不整檔 Write**（orchestrator 8/18 已改 `s2.h2`／`s2.p1`） |
| 12 | `data/budget/i18n/{ja,ko,es,fr,vi,id,pt,hi,ar,ru}.json` | Edit 追加同一組 key（英文值）；`_pending-translation.json` 列 key |
| 13 | `_keys.json` | 若腳本依它對賬則同步（檢查 `check-budget-i18n.py` 只讀 budget.ts en → 不必動，仍同步以免漂移） |

新 i18n key（zh-TW／en 同時加，十語 append 英文值）：

`budget.toc.s0.take`～`budget.toc.s7.take`（8）、`budget.hero.brief`（三分鐘版標題）、`budget.subnav.label`、`budget.s0.overview`（七站總覽 aria）、`budget.s1.chart.gap`（色帶標籤「刪減額」）、`budget.s1.chart2.take`、`budget.s2.chart2.take`、`budget.s2.legend.share`、`budget.s2.slope.left`／`right`、`budget.s2.growth.take`、`budget.s2.growth.sub`、`budget.s3.chart2.take`、`budget.s3.table.share`、`budget.s4.band`、`budget.s5.cal.title`、`budget.s5.cal.sub`、`budget.s5.cal.approved`、`.sent`、`.deadline`、`.fystart`、`.referred`、`.passed`、`.s54`、`.note`、`budget.s6.exec.spent`、`budget.s6.exec.unspent`、`budget.s6.exec.take`、`budget.s6.defense.tick`、`budget.tip.close`。共 37 個（實作時多了 `budget.s2.growth.take`／`sub`、`budget.s2.slope.left`／`right`）。另改三個既有 key 的 zh／en 值：`budget.s2.lede`（100% 版→斜率圖）、`budget.s6.lede`（灰軌藍條→量表）、`budget.s6.chart.title`（法定 vs 決算→執行率）；十語舊譯列在 `_pending-translation.json` 的 `changed_keys`。

---

## 七、驗收（2026-08-18 實測）

- `npx astro build`：**EXIT 0**，13,753 頁；`dist/{,en,ja,…}/budget/index.html` 十二語全在。
- `python3 scripts/tools/check-budget-i18n.py`：十語 **219 keys 全綠**（missing 0／extra 0／empty 0）。
- prose-health（新增與改動的 zh 字串抽成臨時 md）：hard 0；第一輪 warn 全形分號 7 處 → 改句號／頓號後 warn 只剩「無 URL 來源／年份」這種文章層判準（UI 字串不適用）。
- 五組截圖前後對照（`scratchpad/budget-v2/`，逐張看過）：

| 量 | before | after |
| --- | --- | --- |
| mobile 390 SVG 最小字級 | **4.5px**（`before-mobile-chart-c-*.png`） | **8.9–10.1px**（`after-mobile-chart-c-*.png`；8.9 是 slope 一個縮字標籤，其餘 ≥9.4） |
| mobile-en 末端標籤出框 | 8 處 | **0** |
| en 1280 末端標籤出框 | 8 處（fn-abs 3／fn-share 3／multi 2） | **0** |
| 頁面橫向捲動 | 無 | 無 |
| 黏頂子導覽 | 無 | `after-mobile-scrolled-s3.png`／`after-desktop-scrolled-s3.png`：sticky top＝header 底緣（96／108px），scroll-spy 高亮「部會的十年」 |
| touch tooltip | 無 | `after-mobile-tap-tip.png`：點條出現「國防部 · 115 年度（提案）：5,614 億｜105 年度：3,201 億」 |
| 桌機首屏 | `before-desktop-00-fold.png` | `after-desktop-00-fold.png`（hero ＋ 三分鐘版八句） |
| 手機首屏 | `before-mobile-00-fold.png` | `after-mobile-00-fold.png`（八句改緊湊清單） |
| 頁高 mobile／desktop／en | 23,417／20,391／23,441 | 26,937／21,880／25,587（三分鐘版 ＋ 圖例列 ＋ 日曆條 ＋ 成長率圖的代價） |

- 逐區前後：`before-desktop-s{0..7}.png` ↔ `after-desktop-s{0..7}.png`；`before-mobile-*` ↔ `after-mobile-*`；`before-dark-*` ↔ `after-dark-*`；`before-en-*` ↔ `after-en-*`。
- 數字抽查（皆從 JSON 算）：slope 社福 23.7% → 27.4%（4,600.7／19,399.6；8,318.0／30,349.7）；未執行 2018 = 574.9 億（19,669 − 19,094.1）；八年帶 1.04–1.25%（`min/max cutPct` 105–113）；四大成長 +80.8／+77.4／+60.3／+45.6%；日曆條 257 天（2025-11-30 → 2026-08-14）。

## 八、風險與留給人決定的事

| 風險／未決 | 處置 |
| --- | --- |
| slope 取代 100% 堆疊會失去 112–113 國防落第四的中段形狀 | 段落文字保留該句；若哲宇要中段，改成 `SmallMultiples` 占比版（每類一格） |
| 三讀日期逐年圖（「日曆翻到八月」的十年版） | 需資料層加 `passedDate` 十一年；本輪不動 JSON 數字 |
| 40.6% 債務上限線、每人分攤（人口數） | 需 `debtCeilingPct`、`population` 進資料層；不手抄常數 |
| 十語只拿到英文的新字串（33 key） | `_pending-translation.json` 交翻譯 sub-agent |
| 黏頂 subnav 與語言 banner 疊高 | JS 量 header 底緣後寫 `--bp-sticky-top`；無 JS 退到 56px |
| §5 拆兩區、§2/§3 合併（案 B 的兩個子提案） | 涉資訊架構與 12 語 toc key，交哲宇 |
| 政治文案 | 本輪零新增評價性文案；新增字串全是圖表標籤與 takeaway（數字句） |

---

## 九、後記（實作摩擦）

1. **兩套幾何比想像中便宜**：每個元件把佈局包成 `layout(W, narrow)` 跑兩次，template 不用改；成本是 DOM 多一份 SVG（每頁約 +9 個 svg），資料表仍一份。窄版最後定 380 不是 400：390px 螢幕扣掉卡片內距後 svg 約 338px，380 → 比例 0.89 才把 11px 刻度推到 9.8px。
2. **並排兩張圖時要顯示窄版**：§2 slope ＋ 成長率並排各 500px，寬版 760 縮到 0.6 字只有 6.7px；加一條 `.bp-two-charts .bg-svg.is-narrow { display:block }` 就好。量測抓到的，不是眼睛。
3. **時期標籤在手機的三次迭代**：先撞線（top）→ 移到圖底撞 1% 的刪減線 → 最後窄版一律排到 x 軸年份下方當「時期軸」；寬版河流／GDP 圖放圖底（資料集中上半部）、刪減圖放圖頂。用碰撞檢查排行數，最多三行。
4. **英文長機關名**：排序條在放不進左欄時自動改「標籤在條上方」的兩行列（不截字，圖變高）；小倍數與 slope 用 `fitText`（先縮到 10px 再截尾加「…」，全名在 `<title>` 與資料表）。
5. **vite 監看整個 repo 根目錄**：截圖腳本放在根目錄，一改就觸發 dev server reload，正在跑的截圖會斷（「Element is not attached to the DOM」）。腳本用完已刪；下次放 scratchpad 但要 symlink node_modules，或直接用 `scripts/tools/viz-shot.mjs` 的模式。
6. **prose-health 對 UI 字串**：全形分號被抓 7 處，改成句號後過；「無 URL 來源／年份」是文章層判準，UI 字串不適用，hard 0 即可。
7. **沒做的**（都在 §八）：40.6% 上限線與每人分攤（資料層缺欄位）、逐年三讀日期圖（缺日期）、§5 拆區／§2-3 合併（資訊架構，交哲宇）。

🧬
