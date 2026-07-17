# 視覺化系統 v3.0 深度研究與實作報告 — 模組升級 + graph.md 改版

> 2026-07-16 viz-evolution session（哲宇 goal：「完整的升級視覺化模組跟 graph.md，寫深度研究跟實作報告然後完整實作」，指定入口 [/about/視覺化模組型錄/](https://taiwan.md/about/視覺化模組型錄/)）。
> 上游：[article-visualization-design-2026-06-06.md](article-visualization-design-2026-06-06.md)（v1.0 設計）→ [viz-system-evolution-2026-06-12.md](viz-system-evolution-2026-06-12.md)（v2.0 十七模組）。
> Canonical 落地：[docs/editorial/graph.md](../docs/editorial/graph.md) v3.0。

---

## 1. TL;DR

- **主權補洞是本輪最大的修正**：renderer 硬編碼中文讓六語頁面全部渲染「資料來源：」、磚圖表頭、甚至簡體「脚注」aria——v3.0 用六語 `VIZ_STRINGS` 表補掉；同時擴充來源列 regex（Sources/出典/출처/Fuente）與縣市名正規化（EN 去 City/County 後綴、JA 県→縣、U+202F 窄空格摺疊），**EN/JA 譯版磚圖從「必然退化成 bars」變成 22/22 保真渲染**。
- **模組 17→19**：`tw-arc` 席次弧（半圓點陣＋過半線；2024 立院 113 席是站內已查證的真實需求，選舉年臨近）＋ `tw-multiples` 小倍數網格（強制共用 y 值域＋終點直接標值）；`tw-dot` 加三值列（民調點估＋區間帶，不確定性誠實呈現的最小儀器）。
- **scroll-reveal 漸進增強**：`@supports (animation-timeline: view())` + `prefers-reduced-motion` 雙護欄，預設終態全可見——外部研究確認 Firefox stable 仍 flag，「sticky 為體、動畫為飾」是 2026 的正確姿勢。
- **儀器補洞**：viz-shot 預設路徑 404 一個月修正＋空頁 fail-loud；viz-health 新增 8 條結構檢查＋ **timeline/versus/stat 納入來源 gate**（審計鐵證：被 gate 的模組缺源 0%、沒被 gate 的 41-46%——gate 集合的形狀直接決定行為，REFLEXES #82 的 gate 版變體）。
- **採用率是下一戰場**：867 篇只有 5.8% 用模組、Politics 分類 12 篇零模組、161 篇 markdown 數值表待轉——工具已備齊，載具是 69 篇品質重建 batch 與 2026 選舉內容。
- 驗證：renderer 煙霧測試 19/19、viz-shot 57 張（19 模組 × 3 變體）人眼檢視、EN/JA/zh 實頁 curl 驗證、viz-health/prose-health 閘門全過。

---

## 2. 現況診斷（主 session 親自驗證，2026-07-16）

### 2.1 使用分布：編輯模組是主力，圖表模組沒被接住

全站中文文章 `tw-*` block 使用統計（grep `^```tw-`，排除翻譯樹）：

| 模組                                                  | 次數 / 篇數 | 定位                 |
| ----------------------------------------------------- | ----------- | -------------------- |
| tw-timeline                                           | 47 / 43     | 編輯模組（主力）     |
| tw-stat                                               | 39 / 33     | 編輯模組（主力）     |
| tw-versus                                             | 37 / 28     | 編輯模組（主力）     |
| tw-figure                                             | 33 / 26     | 編輯模組（主力）     |
| tw-bars                                               | 27 / 24     | 圖表（v1.0 老將）    |
| tw-line                                               | 8 / 7       | 圖表                 |
| tw-quote / tw-slope / tw-note                         | 各 7        | —                    |
| tw-heatmap                                            | 4 / 4       | —                    |
| tw-dot                                                | 3 / 3       | v2.0 新              |
| tw-waffle                                             | 2 / 2       | —                    |
| tw-stack / tw-pyramid / tw-tiles / tw-iso / tw-source | 各 1        | **幾乎只活在型錄頁** |

**診斷**：v2.0（6/12）加的六個圖表模組，一個月後除 slope/dot 外幾乎零真實採用——「有工具 ≠ 用工具」（神經迴路老教訓）在 viz 層的重演。對照組：WRITER-PROMPT v2.1（7/13）在 read-receipt 強制「graph.md 模組宣告」後，第一篇 dogfood 產物大罷免（7/16，6,300 字）用了 7 個模組——**接線有效，缺口在圖表類模組的選用引導與 legacy 文章**。

### 2.2 主權層缺口：renderer 硬編碼中文，六語頁面破功

`renderArticleHtml(title, content)` 沒有 lang 參數（[article-render.ts:894](../src/utils/article-render.ts)）。後果：en/ja/ko/es/fr 文章頁上——

- 來源 caption 前綴一律「資料來源：」（L82、L136）
- `tw-tiles` fallback 表頭「縣市／數值」、aria「台灣縣市資料地圖」、警示「未對應縣市」全中文（L763-772）
- `tw-waffle` aria fallback「方格圖」（L297）
- 腳註 aria-label 同檔三個變體：「脚注」（**簡體**，L865）／「腳注」（L880）／canonical 是「腳註」（CITATION-GUIDE 用法）

「讓 LLM 讀得懂的視覺化＝主權的視覺化」的宣稱，在翻譯版的 metadata 層有一圈中文毛邊——對六語讀者是雜訊，對 sovereignty 敘事是自打臉。**這是 v3 P0**。

### 2.3 儀器 drift

- `viz-shot.mjs` 預設頁面路徑還是 `/society/視覺化模組型錄/`（L31-33），型錄 6/19 已 recat 到 About（`/about/視覺化模組型錄/`）——預設值直接 404，儀器名存實亡（跟 inbox-audit 同日抓的三例 gate 假閘門同構）。
- `viz-health` 只儀器化兩條（資料模組缺來源 / AI-blind 指示語），graph.md §二§四 的結構規範（line 序列 ≤3、stack 類別 ≤5、slope 恰 2 欄、waffle 加總 ≈100、pyramid 恰 3 欄）全靠人判——寫錯欄位數時 renderer 靜默 return ''，fenced block 退化成 raw code 顯示，沒有任何儀器會叫。

### 2.4 內容層機會

- 2026-11-28 地方選舉在即（roadmap 30 天方向盤 #1），elections 區已存在；graph.md §九 把「國會席次弧」列 v3 候選。選舉年的席次/得票視覺化是真實臨近需求，不是為加而加。
- graph.md §九 v3 roadmap 明列 scrollytelling-lite + DualChannel sticky showcase——LONGINGS 身體渴望「能用視覺說話」的下一步逐字寫著這兩件事。
- 69 篇單薄文重建 batch（7/16 inbox-audit 排入）即將走 REWRITE——模組升級會被這批 rewrite 直接吃到，時機正好。

## 3. 內部使用實態調查（Explore agent fan-out，主 session 抽驗）

全站 867 篇中文文章只有 **50 篇（5.8%）** 用到任一模組，共 226 個 block；前 5 名（timeline/stat/versus/figure/bars）佔 81%。四個關鍵發現：

### 3.1 Gate 集合的形狀直接決定行為（#82 proxy 活例）

被 `viz_health._DATA_MODULES` gate 的 10 個圖表模組，來源缺失率 **0%**；沒被 gate 的 tw-timeline / tw-versus / tw-stat 缺失率 **41-46%**（177 個應標源 block 中 53 個缺）。graph.md §三.8 寫「每個資料模組標來源」，但儀器集合漏了三個最高頻的編輯模組——規範在、儀器沒接線，行為就照儀器走。連 graph.md §四 和型錄頁自己的 timeline/versus 範例都沒有來源列（DNA 以身作則失敗）。

### 3.2 Politics 分類 12 篇零模組

選舉年（2026-11-28 九合一）最反常的缺口：席次、得票、門檻天生是 tw-bars/tw-stack/tw-arc 的題材，整個分類滲透率 0%。Society 是主力（54 block / 11.1%），People 241 篇只 4.6% 薄用。

### 3.3 markdown 資料表是 3.2 倍大的未開發礦

161 篇用 markdown 資料表（vs 50 篇用模組）。抽驗判準：**數值矩陣／趨勢／現況-目標類該轉模組**（高等教育大學數量表→tw-line、颱風氣候情境表→tw-heatmap、淨零能源現況-目標→tw-slope）；**質性對照／規格型錄該留表格**（蒸汽機車型號、認知作戰手法、氫氣顏色）。另找出 8 篇數字密集零模組深度文（高等教育、健保、公視、Computex、氣候危機、營養午餐等），每篇已標最該視覺化的段落。

### 3.4 翻譯層：幾何保留、文字翻譯的設計成立，但磚圖必然退化

翻譯版 tw-_ block 約 929 個（en 188 / ja 186 / ko 186 / es 186 / fr 183）。抽驗證實 graph.md §五 三層分離運作正常：標籤序列名全翻、數值一字不差、ES 版千分位在地化、`_` 強調保留。**但 tw-tiles 在 EN/JA 版必然退化成 bars**：EN 寫「Taipei City」而 alias 只有 'taipei'、JA 寫「新竹県」（日文県）——normCounty 對不上 60% 門檻，安全網觸發但地理視覺化在翻譯版全滅。另有 JA 型錄殘留中文「來源：」標籤。

## 4. 外部研究（2025-2026 最佳實踐，general-purpose agent web research）

六題結論（完整來源 URL 在 agent 回報，關鍵項列此）：

1. **CSS-only scrollytelling**：`animation-timeline` 全球支援 ~84%，但 **Firefox stable 仍在 flag 後**（Nightly 才預設開）、Safari 26.0+ 才有。結論：**sticky 為體、scroll 動畫為飾**——捲動動畫只能做「拿掉不影響理解」的進場效果，必須包 `@supports` + `prefers-reduced-motion`，預設狀態＝完全可見的終態。AI 爬蟲不捲動，內容可見性絕不依賴捲動（正好跟 graph.md §三.9 visible-by-default 同一條紀律）。
2. **編輯方法論**：FT Visual Vocabulary 仍是事實標準、無後繼者。Datawrapper 2024-26 主推「直接標註取代圖例」（資料點旁短句＋帶色關鍵詞）；2025 使用數據顯示**表格本身是最常用視覺化**（不是退路）、small multiple 圖全年爆紅。The Pudding 近作的 sticky stepper 可用純 CSS 達成 80%。
3. **AI/LLM 可讀性**：2025-26 研究證實多模態 LLM 從圖片重建數值不可靠——**文字節點才可靠**，Taiwan.md「禁 D3/Canvas、數據進 DOM」的紀律被外部研究背書。SVG 標配 `role="img"` + `<title>/<desc>`；schema.org Dataset JSON-LD 進入 LLM retrieval 層（v4 候選）；llms.txt 站上已有。
4. **選舉視覺化**：22 縣市長最適解就是現成 `tw-tiles`（等大磚解掉 choropleth 面積偏誤）；席次弧是議會語意（立院 113 席），不適合首長選舉。政黨色只用官方色、不加情緒濾鏡；選舉視覺全程 §自主權邊界。
5. **Small multiples**：同型同尺寸**共用軸域**是鐵律；3-20 格甜蜜點；每格小標＋邏輯排序；手機降欄。
6. **不確定性**：研究顯示誤差棒助長誤解；**點估＋區間帶**與分位點圖較誠實。民調呈現必標「什麼量＋信心水準＋n」——2026 選舉報導最常見的誠實性失守點，先把儀器準備好。

## 5. v3.0 設計（八個決策）

| #   | 決策                                                                                                                                                                                                                                  | 對應證據            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| D1  | **renderer i18n**：`renderArticleHtml` 加 lang 參數＋六語 `VIZ_STRINGS` 表（來源前綴／磚圖表頭／aria），修簡體「脚注」                                                                                                                | §2.2 主權破功       |
| D2  | **tw-tiles 縣市名正規化強化**：EN 去 ' city/county' 後綴、JA 県→縣                                                                                                                                                                    | §3.4 翻譯版磚圖全滅 |
| D3  | **新模組 `tw-arc` 席次弧**：半圓點陣＋過半線＋legend，2024 立院 113 席（52/51/8/2）是站內已查證的真實需求（大罷免脈絡＋2026 選舉年）                                                                                                  | §3.2 + §4.4         |
| D4  | **新模組 `tw-multiples` 小倍數折線網格**：`--- 群組` 分隔、強制共用 y 值域、終點直接標值                                                                                                                                              | §4.2 + §4.5         |
| D5  | **tw-dot 三值列**＝點估＋區間（民調誠實呈現的最小儀器）                                                                                                                                                                               | §4.6                |
| D6  | **scroll-reveal 漸進增強**：`@supports (animation-timeline: view())` + reduced-motion 雙護欄，預設終態全可見；DualChannel sticky 記為版式 pattern 不做模組                                                                            | §4.1                |
| D7  | **儀器補洞**：viz-shot 預設路徑修正（404 一個月）＋空頁 fail-loud；viz-health 加結構檢查（slope 恰 2 欄／line ≤3 序列／stack ≤5 類／waffle ≈100／pyramid 3 欄／multiples 2-20 組／空資料列）＋ **timeline/versus/stat 納入來源 gate** | §2.3 + §3.1         |
| D8  | **graph.md v3.0 + 型錄 19 模組**：§四新語法、§三＋不確定性與進場動畫紀律、§六補 MLLM 佐證、§八＋4 反例、§九 roadmap 換代；計數在下游全部去寫死（模組數以 graph.md 為準）                                                              | 全部                |

**明確不做**（邊界）：sankey/chord/network（AI 可讀性差、有替代）；tw-scatter/直方（等真實文章需求，維持 v2.0 紀律）；scroll 狀態切換式 scrollytelling（違反 visible-by-default）；schema.org Dataset JSON-LD 與黨色語意（涉對外呈現與政治色彩，列 v4 候選交哲宇）。

## 6. 實作清單與驗證紀錄

| 檔案                                                    | 變更                                                                                                                                                                                                                                                               |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `src/utils/article-render.ts`                           | 六語 `VIZ_STRINGS` + `renderArticleHtml(…, lang)` + 簡體「脚注」修正；`tw-arc` / `tw-multiples` 新分支；`tw-dot` 三值列（`_isPureNum` 嚴格判定防備註誤判）；`_srcRe` 多語來源標籤；normCounty EN/JA/U+202F 正規化；line/slope/arc SVG 補 `<title>`；檔頭計數去寫死 |
| `src/templates/article.template.astro`                  | `renderArticleHtml(title, content, lang)`                                                                                                                                                                                                                          |
| `src/styles/article-modules.css`                        | §18 tw-arc + §19 tw-multiples（沿用 data-cat 五色盤）；tw-dot 區間帶樣式；scroll-reveal 雙護欄；iso 色規則從 stack 段搬回 iso 段                                                                                                                                   |
| `scripts/tools/viz-shot.mjs`                            | 預設路徑 /society/→/about/（404 一個月）；0 模組頁 fail-loud（exit 1）                                                                                                                                                                                             |
| `scripts/tools/lib/article_health/checks/viz_health.py` | 8 條結構檢查（slope 恰 2／line ≤3／stack ≤5／waffle ≈100／pyramid 3 欄／arc 席次數字／multiples 3-20／空資料列）；`_DATA_MODULES` +arc/multiples/**timeline/versus/stat**                                                                                          |
| `docs/editorial/graph.md`                               | v3.0（§二 +2 型錄列／§三 +2 原則／§四 19 模組＋新語法／§五 renderer i18n／§六 MLLM 佐證／§七 閘門面更新／§八 +4 反例／§九 v4 候選；計數 SSOT 宣告）                                                                                                                |
| `knowledge/About/視覺化模組型錄.md`                     | 十九種：+arc（2024 立院 113 席，大罷免 fn9 中央社已查證）+multiples（衛福部三班護病比公告 2024，醫療法文章已查證）；stat/versus/timeline 範例補來源列；dot 三值列說明                                                                                              |
| 下游同步                                                | DNA.md／ANATOMY.md／LONGINGS.md／WRITER-PROMPT.md／文章如何誕生.md／SPORE-INBOX 待發文案——計數改活話或校準                                                                                                                                                         |

**驗證證據**：

1. renderer 煙霧測試 19/19 PASS（113 席點陣、過半線標籤、EN/zh/ja 三 locale、EN/JA tiles 不退化、legacy dot 回歸 byte-safe）。
2. `viz-shot` 像素閘門：19 模組 × light/dark/mobile = **57 張零失敗**，新模組六張＋歷史 cascade 受害者（quote/tiles）逐張人眼檢視——席次弧過半線正確落在第 57 席邊界、小倍數三格共用尺且強調組退灰機制正常。
3. 實頁驗證（worktree dev server）：EN 頁「Source: 」前綴＋「Footnote N」aria、JA「脚注」、zh「資料來源：」回歸不變；EN/JA 型錄磚圖 markup 層 `class="tw-tiles"`（無 fallback）；DOM 計數 arcDots=113／multCells=3／tilesCells=22／srTables=6。
4. 閘門：型錄頁 viz-health hard=0 warn=0；prose-health score 3（pass）、新增文字破折號歸零。
5. U+202F bug：babel 產物在「New Taipei」夾窄不斷行空格，直接測試抓到 → 摺疊修正後 22/22。

**交哲宇的 v4 候選**（不在本輪自主權內）：schema.org Dataset JSON-LD（站台層對外呈現）；政黨官方色映射（政治色彩語意）；DualChannel sticky 旗艦專題選題。

🧬
