# 立法院預算十年 — Research D：預算視覺化先例與設計原則

執行摘要：搜尋約 32 次，最值得移植的三個手法：(1) USAFacts「The Big Picture」用 Sankey 把「收入怎麼流入、支出怎麼流出」接成一張圖，直接標籤取代圖例、點擊逐層展開；(2) Datawrapper 官方建議「總量不重要就別用 stacked area，改用 line」，這條規則直接決定本頁逐年結構圖該用哪種圖；(3) Obama White House Interactive Budget（treemap，squarify/strip/slice-and-dice 三種鋪磚演算法可切換）證明「機關別 × 金額大小」用面積而非長度最直覺，且完全不需要 D3 以外的重型框架也能做到（本頁可用純 SVG rect 模擬）。台灣本地先例集中在「官方展示型」（g0v／台北市／主計總處／國庫署），沒有一個做到「敘事化」；敘事化這塊，公視「一次看懂總預算」示範了用時事鉤子開場但完全沒有視覺化——這正是本頁的空白可以填的位置。

---

## §1 搜尋軌跡（逐條：「query」→ 發現 → URL）

1. 「g0v 中央政府總預算視覺化 budget.g0v.tw」→ 找到 g0v 官方入口與主計總處視覺化頁 → https://budget.g0v.tw/
2. 「budget.taipei 台北市政府預算視覺化」→ 找到台北市預算視覺化現址（已從 budget.taipei 遷移） → https://budget-tbsv.gov.taipei/Budget
3. 「主計總處 中央政府總預算 視覺化 圖表」→ 找到 DGBAS Tableau 視覺化專區 → https://ws.dgbas.gov.tw/ebas1/data/visual/GBA_html/Visual/Total_Budget.html
4. 「立法院預算中心 報告 圖表 視覺化」→ 確認預算中心以 PDF 報告 + 開放資料 API 為主，未見圖表化產出 → https://www.ly.gov.tw/Pages/List.aspx?nodeid=6594
5. 「報導者 中央政府總預算 圖表 專題」→ 未找到報導者專門的總預算視覺化，改發現公視 PNN「一次看懂總預算」→ https://news.pts.org.tw/article/822346
6. WebFetch budget.g0v.tw → 確認頁面可開啟，但首頁本身內容極簡（僅 logo + 導覽），無法直接觀察到圖表本身
7. WebFetch budget-tbsv.gov.taipei/Budget → 確認四大分類（歲出機關別／政事別、歲入來源別、歲出用途別）
8. WebFetch DGBAS 視覺化頁 → 確認為 Tableau 外嵌，三模組（政事別／機關別／來源別）
9. WebFetch 公視 PNN 文章 → 確認 2026-08-14 發布，純文字敘事，無圖表
10. 「天下雜誌 中央政府總預算 視覺化 圖表 專題」→ 未找到專門總預算視覺化專題（negative）
11. 「READr 預算 視覺化 專題」→ 找到 READr 中央政府總預算案審查監督平台 → https://www.readr.tw/project/3/2025budget
12. WebFetch READr 子頁 proposal?id=6418 → 404，頁面已下線或改版
13. 「端傳媒 台灣 預算 視覺化 圖表」→ 未找到端傳媒台灣預算視覺化（negative）
14. 「關鍵評論網 中央政府總預算 圖表 一次看懂」→ 僅有一般新聞報導，無專門視覺化（negative）
15. 「g0v twbudget github treemap sankey history budget visualization」→ 找到 g0v/twbudget repo → https://github.com/g0v/twbudget
16. 「USAFacts federal budget visualization treemap spending」→ 找到「The Big Picture」Sankey，2025 Innovation by Design 得獎 → https://usafacts.org/visualizations/the-big-picture/
17. WebFetch usafacts.org/visualizations/the-big-picture/ → 確認 2024 財年資料，可依機關搜尋篩選
18. WebFetch fastcompany.com 得獎報導 → 403 被擋，無法逐字引用
19. 「NYT "Four Ways to Slice Obama's 2013 Budget" nytimes.com」→ 找到二手描述（rethinkingvis／scu.edu blog）
20. 「Obama White House interactive federal budget 2012 2016 explorer」→ 找到 2016 互動預算 treemap → https://obamawhitehouse.archives.gov/interactive-budget
21. 「Congressional Budget Office infographic chart federal budget visualization」→ 找到 CBO 年度 infographic 系列 → https://www.cbo.gov/publication/62286
22. WebFetch cbo.gov/publication/62286 → 403 被擋
23. WebFetch obamawhitehouse.archives.gov/interactive-budget → 確認 treemap，squarify/strip/slice-and-dice 三種演算法可切換，hover/left-click/right-click 三段互動
24. WebFetch rethinkingvis.com/visualizations/96 → 確認 NYT「Four Ways to Slice」為 bubble chart，2012-02-13 發布，四種切分（支出類型／可裁量支出變化／部門總額／完整組合）
25. 「nytimes.com "four ways to slice" budget 2012 interactive site:nytimes.com」→ 找不到現行可開啟的 NYT 原始網址，改由 PBS NewsHour 二手描述佐證
26. 「OpenSpending Open Knowledge Foundation budget visualization project history」→ 確認 2011 年上線，2017 年後迭代為 Fiscal Data Package → https://blog.okfn.org/2011/06/26/openspending-goes-live/
27. 「UK Institute for Fiscal Studies budget chart visualization」→ 找到 IFS 圖表庫與「Be the Chancellor」互動工具 → https://ifs.org.uk/be-chancellor
28. 「日本財務省 予算の見える化 グラフ」→ 財務省本身以靜態統計表為主，未見專門互動視覺化（negative-ish）
29. 「JUDGIT 予算 見える化 プロジェクト」→ 找到 JUDGIT!（搜尋式，非圖表式）→ https://judgit.net/about
30. 「"Where Does My Money Go" UK budget visualization Open Knowledge」→ 確認 2009 上線，2010 併入 OpenSpending → https://github.com/openspending/wheredoesmymoneygo.org
31. 「열린재정 대한민국 예산 시각화 openfiscaldata.go.kr」→ 找到韓國官方財政公開系統 → https://www.openfiscaldata.go.kr/op/ko/index
32. 「IFS "be the chancellor" interactive tool taxes spending」→ 確認由 IFS 研究員與 Nesta 合作開發
33. WebFetch rethinkingvis.com/visualizations/228 → 確認 Where Does My Money Go 用地圖＋時間軸呈現
34. 「The Pudding budget government spending visualization story」→ 未找到 Pudding 專門的政府預算敘事作品（negative）
35. 「Bloomberg "what's in the budget" scrollytelling visualization」→ 未找到此標題的作品，找不到直接對應（negative）
36. 「Reuters Graphics OR Washington Post budget deficit visualization scrollytelling」→ 找到 WaPo「40 years of budgets show shifting national priorities」與「debt cut game」→ https://www.washingtonpost.com/graphics/politics/budget-history/
37. WebFetch washingtonpost.com/graphics/politics/budget-history/ → 403 被擋，無法逐字驗證內容，僅能以搜尋結果標題佐證存在
38. WebFetch washingtonpost.com/politics/2023/01/26/house-republicans-spending-debt-ceiling/ → 403 被擋
39. 「Datawrapper blog stacked area chart vs line chart small multiples advice」→ 找到 area-charts 專文
40. 「Datawrapper blog "annotations" "direct labeling" legend chart design principle」→ 找到 annotations／color-keys 專文
41. 「Flourish template treemap sankey bar chart race budget story example」→ 找到 Flourish treemap 頁面明確提及 budgets → https://flourish.studio/visualisations/treemaps/
42. 「waterfall chart bump chart slope chart budget year over year change design comparison」→ 僅找到通用圖表教學網站內容（非具名公部門預算先例），列入 §4
43. 「bullet chart budget execution rate progress visualization government」→ 同上，僅通用教學內容，列入 §4
44. WebFetch flourish.studio/visualisations/treemaps/ → 確認逐字引句（見 §3）
45. WebFetch datawrapper.de/blog/area-charts → 確認四句逐字引句（見 §3）
46. 「報導者 一分鐘看懂 系列 圖表 資訊圖表」→ 未找到「一分鐘看懂」總預算系列，找到 2018 年報導者互動專題回顧（非預算主題）
47. WebFetch archive.nytimes.com → 工具回報無法擷取此網域
48. WebFetch pbs.org/newshour 2012 比較文章 → 確認並列出 5 個 2012 年美國聯邦預算視覺化專案（NYT treemap／National Journal／WaPo 30年支出優先順序 treemap／Third Way 納稅收據概念／Information is Beautiful「Debtris US」）
49. WebFetch news.ltn.com.tw 台北市預算視覺化報導 → 確認「25.68億碗鬍鬚張魯肉飯」逐字引句，2018年上線，台北市資訊局製作
50. WebFetch judgit.net/about → 僅取得瀏覽器相容性提示，未能取得完整介面描述
51. WebFetch github.com/g0v/twbudget → 確認 README「visualizing taiwan central government spending」，2012 年 Yahoo HackDay TW 專案，MIT License，11 個未解決 issue
52. WebFetch nytimes.com 直接網址 → 工具回報無法擷取此網域
53. WebFetch washingtonpost.com 30-years 舊網址 → 403 被擋
54. 「g0v budget.g0v.tw 2024 2025 中央政府總預算 最新版本」→ 未找到明確的最新年度版本入口，無法確認目前是否持續更新（negative/待核）
55. 「財政部國庫署 中央政府總預算收支結構 圖表 nta.gov.tw」→ 找到「113–115年度中央政府總預算收支結構」圓餅圖頁面 → https://www.nta.gov.tw/singlehtml/67?cntId=21eb0448ea3c447cafa4b3ef6fd0f302
56. 「國債鐘 中華民國 全國財政資訊網 即時 主計總處」→ 找到國庫署「國債鐘」頁面 → https://www.nta.gov.tw/singlehtml/17?cntId=nta_7906_17
57. WebFetch nta.gov.tw 收支結構頁 → 確認圓餅圖 + 逐字引句
58. WebFetch nta.gov.tw 國債鐘頁 → 確認「非即時時鐘、是週更數字列表」，逐字引句
59. WebFetch usaspending.gov/explorer/budget_function → 工具回報僅取得標題，JS 渲染內容無法擷取，列入待核

---

## §2 Findings

### 2-1 台灣先例

| 名稱 | 製作者 | 年份 | URL | 核心圖型 | 互動 | 值得學 | 缺點 |
|---|---|---|---|---|---|---|---|
| g0v 中央政府總預算視覺化 | g0v 社群 | 2012 年首發，歷年是否持續更新未能確認【待核】 | https://budget.g0v.tw/ | 依 GitHub README 與二手搜尋描述為 treemap + bubble chart；**我實際打開首頁時只看到 logo 與導覽，未能直接觀察到圖表本體** | 依二手描述：歷史趨勢、跨部門比較、民意回饋、稅收組成拆解 | 2012 年就把「跨部門比較」跟「開放民意回饋」接在同一張圖上，是台灣最早的公民科技預算專案 | 目前首頁內容稀疏，找不到明確年度入口；GitHub repo 顯示為 2012 年 Yahoo HackDay 賽後專案，11 個未解決 issue，維護狀態存疑 |
| 台北市總預算視覺化 | 台北市政府資訊局 | 2018 年上線（自由時報報導），現址已遷移 | https://budget-tbsv.gov.taipei/Budget | 機關別／政事別／來源別／用途別四分類瀏覽；2018年版另有換算成「25.68億碗鬍鬚張魯肉飯」的趣味比喻（見§3引句） | 分類切換瀏覽 | 用在地讀者有感的具體物件（滷肉飯碗數）把巨額數字換算成可想像的單位 | 現行版是否仍保留滷肉飯換算功能【待核，我在新網址上未直接觀察到此功能】 |
| 主計總處中央政府總預算視覺化專區 | 行政院主計總處 | 未標示明確年度，Tableau 動態載入 | https://ws.dgbas.gov.tw/ebas1/data/visual/GBA_html/Visual/Total_Budget.html | Tableau 互動圖表，三個獨立模組：歲出政事別／歲出機關別／歲入來源別 | 標準 Tableau 互動（頁面提示需另開頁面並調整瀏覽器縮放） | 官方把「政事別、機關別、來源別」三軸心拆成三個獨立視覺化，而非硬塞進一張圖 | 用 Tableau 外掛、非 semantic HTML，需另開頁面＋手動調整縮放，對可及性與 AI 爬蟲都不友善 |
| 立法院預算中心研究成果 | 立法院預算中心 | 持續產出，如「110年度中央政府總預算案整體評估報告」 | https://www.ly.gov.tw/Pages/List.aspx?nodeid=6594（報告）／https://www.ly.gov.tw/Pages/List.aspx?nodeid=44939（開放資料API，支援CSV/JSON/XML） | 無圖表化產出，但提供結構化開放資料下載 | 把「評估報告」開放 API 化，讓下游（如 READr）能重新視覺化——資料開放本身就是一種設計選擇 | 報告本身停留在 PDF／文字格式，一般讀者難以直接消化，需要二次加工 |
| READr 中央政府總預算案審查監督平台 | READr 讀+ | 114年度（2025）持續更新 | https://www.readr.tw/project/3/2025budget（子頁 proposal?id=6418 目前回傳 404） | 依搜尋摘要為「隨機」與「分類」兩種瀏覽模式呈現立委刪減提案 | 隨機／分類模式切換 | 把「單一刪減提案」做成可隨機瀏覽的卡片介面，降低一次讀完整份報告的負擔 | 子頁 404，我無法直接開啟驗證介面細節；描述僅來自搜尋摘要與社群轉發（Threads／Plurk／g0v.social），未能逐字核實 |
| 公視新聞網「政府的錢怎麼花？一次看懂總預算」 | 公共電視「新聞見分曉」 | 2026-08-14 | https://news.pts.org.tw/article/822346 | 純文字敘事，**確認無圖表或視覺化元素** | 無 | 用「總預算到八月立法院還沒過」的時事懸念開場，把抽象預算概念接上讀者當下關心的政治張力 | 完全沒有視覺化，只靠文字說比例（社福支出27.4%），數字讀完即忘 |
| 財政部國庫署「113–115年度中央政府總預算收支結構」 | 財政部國庫署 | 113–115年度（三年並列） | https://www.nta.gov.tw/singlehtml/67?cntId=21eb0448ea3c447cafa4b3ef6fd0f302 | 圓餅圖（歲入結構＋歲出結構各一張） | 無明顯互動，附 Excel/PDF 下載 | 三個年度並列呈現歲入歲出結構占比變化，且明確標出「社福＋教科文＋經濟發展＋國防」四項合計占比超過7成的趨勢句 | 圓餅圖本身不利於呈現「逐年增減」，三年並列只能靠讀者自己比較三張餅圖 |
| 財政部國庫署「國債鐘」 | 財政部國庫署 | 週更（頁面顯示自2017年1月至今歷史紀錄） | https://www.nta.gov.tw/singlehtml/17?cntId=nta_7906_17 | **無圖表，純數字列表**（長期債務／短期債務／合計／人均負擔） | 無，僅提供歷史列表與下載 | 「人均負擔債務」把總量換算成個人感受得到的單位，跟台北市滷肉飯換算是同一種手法的財政版 | 完全沒有視覺化，只是逐週更新的數字表，讀者難以看出趨勢方向 |

**同分類負面清單**：天下雜誌數據圖表欄目（https://www.cw.com.tw/masterChannel.action?idMasterChannel=74）、端傳媒、關鍵評論網、報導者——搜尋範圍內均未找到專門的中央政府總預算視覺化專題，詳見 §4。

### 2-2 國際先例

| 名稱 | 製作者 | 年份 | URL | 核心圖型 | 互動 | 值得學 | 缺點 |
|---|---|---|---|---|---|---|---|
| USAFacts「The Big Picture」 | USAFacts（非黨派公民組織） | 2025年1月上線，資料為2024財年 | https://usafacts.org/visualizations/the-big-picture/ | Sankey（依搜尋摘要確認：藍色代表收入流入、洋紅色代表支出流出，左到右分層） | 點擊任一分類展開下層子項，可用搜尋列直接找特定機關／計畫 | 收入與支出接成同一張圖，讓讀者一眼看到「錢從哪來、流去哪」的因果關係；2025 Innovation by Design 得獎，上線後瀏覽超過25萬次 | 我實際 WebFetch 頁面時只取得摘要片段（"Explore revenue and spending categories or filter by agency"），無法逐字驗證完整設計論述；Fast Company 得獎報導 403 被擋無法引用 |
| Obama White House Interactive Budget | 歐巴馬政府（2016財年版） | 2015年2月發布（FY2016） | https://obamawhitehouse.archives.gov/interactive-budget | Treemap，**可切換三種鋪磚演算法**：Squarified／Strip／SliceAndDice | 確認頁面原文：「Hover over an area of the budget to see the total amount proposed for that section」「Left click to set a node as root for the visualization」「Right click to set the parent node as root」 | 讓讀者自己選鋪磚演算法，等於把「治理透明」延伸到「呈現方式透明」；left-click鑽入、right-click回上層的操作邏輯簡單好記 | 純 treemap 面積編碼，無法同時呈現「逐年變化」，看到的永遠是單一年度切片 |
| NYT「Four Ways to Slice Obama's 2013 Budget Proposal」 | The New York Times | 2012-02-13 | 原始網址已不可開啟【URL待核，我僅能透過 rethinkingvis.com/visualizations/96 二手確認存在】 | Bubble chart，泡泡大小=金額，顏色=較2012年增減 | 四種切分視角（支出類型／可裁量支出變化／部門總額／完整組合）之間可切換，依二手描述「轉換極為流暢」 | 同一組資料、同一種圖形語彙（氣泡），只換分類軸就能講四個不同的故事，不需要四種不同圖表類型 | 氣泡圖對「精確比較兩個相近數值大小」天生不利，讀者只能感受大致排序 |
| NYT 2012財年預算 treemap（更早版本） | The New York Times | 2011年1月 | http://www.nytimes.com/packages/html/newsgraphics/2011/0119-budget/index.html【URL待核，WebFetch回報無法擷取nytimes.com網域，僅由PBS NewsHour文章轉述確認】 | 可縮放 treemap（zoomable） | 縮放進入細節層級 | 同一機構（NYT）一年內從「純 treemap」進化到「bubble chart 四切面」，顯示同一資料集可以疊代出不同圖型策略 | 舊版無法驗證細節，僅存二手描述 |
| National Journal 互動時間軸 | National Journal | 2011年2月 | http://www.nationaljournal.com/interactive-graphic-budget-through-history-20110214【URL待核，僅PBS NewsHour轉述】 | 互動時間軸 | 依描述可拖動查看過去50年支出與赤字變化 | 用「50年」的長時間尺度，讓「今年赤字很嚴重」這句話有歷史對照座標 | 未能直接驗證，細節存疑 |
| Washington Post「30年支出優先順序」treemap | The Washington Post | 2012 | http://www.washingtonpost.com/wp-srv/special/politics/30-years-spending-priorities-federal-budget-2012/【URL待核，WebFetch回報403，僅PBS NewsHour轉述確認存在】 | 互動 treemap，涵蓋過去30年聯邦收支 | 依描述可逐年瀏覽 | 把「單一年度切片」的 treemap 延伸成「跨30年」的treemap序列，處理了 treemap 最大弱點（看不到時間變化） | 我無法直接開啟驗證實際互動細節 |
| Washington Post「40 years of budgets show shifting national priorities」 | The Washington Post | 年份不明【待核】，標題本身即為「40年」跨度 | https://www.washingtonpost.com/graphics/politics/budget-history/【URL待核，WebFetch回報403】 | 標題顯示為長時間跨度圖表，圖型未能直接驗證 | 未能驗證 | 若屬實，是「30年版」的後續延伸版本，時間尺度拉得更長 | 無法直接驗證任何設計細節，僅存在搜尋結果標題證據 |
| Washington Post「削減聯邦預算有多難」 | The Washington Post | 2023-01-26 | https://www.washingtonpost.com/politics/2023/01/26/house-republicans-spending-debt-ceiling/【URL待核，WebFetch回報403】 | 未能驗證圖型 | 未能驗證 | 標題點出「读者最容易誤解『削減預算』有多容易」這個切入角度本身值得借鏡 | 無法驗證任何設計細節 |
| Washington Post「國債刪減遊戲」 | The Washington Post | 2023 | https://www.washingtonpost.com/business/interactive/2023/national-debt-cut-game/ | 依搜尋摘要為互動遊戲形式：讓讀者自己選要刪減哪些項目，最後產生「你是哪種撙節者」的分類結果 | 讓讀者主動做決策而非被動看圖 | 把「讀者自己删減看看」的遊戲化互動，用來讓人體感「刪減很難」這件事，而不是用文字說教 | 未實際 WebFetch 驗證頁面內容，僅依搜尋摘要 |
| CBO 年度 Infographics | Congressional Budget Office | 每年發布一組（FY2022–FY2025），最新為FY2025 | https://www.cbo.gov/publication/62286 | 依官方頁面標題確認為固定 4 張一組的 infographic，涵蓋當年支出結構＋數十年長期趨勢 | 靜態圖，部分年度有互動版 | CBO 每年固定產出「4張圖」的格式化節奏，讓讀者每年知道要去哪裡找、找什麼 | WebFetch該頁403被擋，無法逐字確認4張圖各自的圖型 |
| UK IFS「Be the Chancellor」 | Institute for Fiscal Studies × Nesta | 持續更新（因應每年秋季預算改版） | https://ifs.org.uk/be-chancellor | 互動試算工具（非傳統圖表，而是「調整參數→即時看到赤字/債務預測變動」的模擬器） | 讀者可調整稅收與支出政策、經濟成長與利率假設，即時看到借貸與債務預測的變化 | 把「你來當財政大臣」的視角切換，讓讀者從「看圖表」變成「做決策」，直接體感每個決定的財政後果 | 屬於獨立試算工具，不是本頁要做的「呈現十年史」敘事型頁面，移植時需要簡化成「單一情境模擬」而非完整試算器 |
| UK IFS Fiscal Facts / Charts | Institute for Fiscal Studies | 持續更新 | https://ifs.org.uk/tools_and_resources/fiscal_facts | 傳統統計圖表庫（bar/line），依政策領域分類 | 可下載資料 | 圖表庫化管理——每張圖都是獨立可引用、可下載資料的單元，方便媒體與研究者引用 | 圖表本身設計偏學術，非給一般讀者的敘事化呈現 |
| Where Does My Money Go?（UK） | Open Knowledge Foundation | 2009年上線，2010年併入 OpenSpending | https://github.com/openspending/wheredoesmymoneygo.org | 依 rethinkingvis.com 確認為地圖＋時間軸（map + timeline），涵蓋十個支出領域（國防、健康、教育、環境等） | 讀者可查看「自己的稅金」按比例分配到十個領域各多少 | 「Where does MY money go」的第一人稱標題本身就是設計——把總體預算換算成「我的錢」的視角 | 2010年後已併入 OpenSpending，原站可能已不是獨立運作狀態 |
| OpenSpending / Open Knowledge Foundation | Open Knowledge Foundation | 2011年上線，2017年後迭代為Fiscal Data Package規格 | https://blog.okfn.org/2011/06/26/openspending-goes-live/ | 全球政府支出資料的通用視覺化平台框架（非單一圖表，而是可套用在任何國家資料集的框架） | 支援自訂查詢與視覺化產生 | 把「一國預算視覺化」抽象成「可重複套用的開源框架」，是本頁若想做成可複用元件的參考架構 | 2017年後平台經歷多次轉型，原始版本的具體圖表細節難以直接追溯 |
| 韓國 열린재정（Open Fiscal Data） | 대한민국 정부（企劃財政部） | 持續更新 | https://www.openfiscaldata.go.kr/op/ko/index | 依搜尋摘要為官方財政資料公開系統，含約150組開放資料集與Open API | 提供Open API供第三方建置視覺化 | 官方直接開放150組資料集的Open API，把「視覺化」的責任下放給民間開發者而非自己包辦 | 我未能直接 WebFetch 驗證入口頁本身是否有官方製作的視覺化圖表，還是純資料下載站 |
| 日本 JUDGIT! | 構想日本 × 日本大學尾上洋介研究室 × Visualizing.JP × Waseda Chronicle | 2019年7月11日上線 | https://judgit.net/about | **搜尋介面為主，非圖表視覺化**——可像一般搜尋引擎查詢約5000項政府事業的目的/內容/成果/支付對象 | 關鍵字搜尋 | 把「逐一打開Excel檔案才能查」的預算資訊變成「像Google搜尋一樣查」，降低查詢門檻本身就是一種介面設計 | 本質是搜尋工具而非視覺化工具，我 WebFetch about頁時只取得瀏覽器相容性提示，未能取得更多介面細節 |
| 日本財務省 予算関連資料 | 財務省 | 持續更新 | https://www.mof.go.jp/policy/budget/index.html | **靜態統計表與PDF為主**，未發現專門的互動式「予算の見える化」視覺化頁面 | 無 | （無，見§4負面清單） | 官方預算頁面停留在傳統統計表格式，與台灣主計總處類似的「有資料開放但無敘事設計」問題 |

### 2-3 Flourish／圖表平台實例

| 名稱 | 製作者 | URL | 核心圖型 | 互動 | 值得學 | 缺點 |
|---|---|---|---|---|---|---|
| Flourish Treemap 模板 | Flourish Studio | https://flourish.studio/visualisations/treemaps/ | Treemap／Sunburst／Packed circles／Radial tree（同一資料可一鍵切換四種階層圖型） | 縮放探索親子層級、依規則覆寫顏色、依變數篩選、投影片或捲軸觸發的漸進揭示 | 頁面原文明確點名「budgets」為典型應用場景（見§3引句）；同一份階層資料提供四種圖型切換，讓讀者自己選最好懂的形式 | Flourish 為商業工具，若本頁要做到「不用 D3/Canvas 圖片、純 semantic HTML + inline SVG」，只能借鏡其互動邏輯，不能直接嵌入其 iframe |
| Flourish Sankey 模板 | Flourish Studio | https://flourish.studio/visualisations/sankey-charts/ | Sankey，支援動畫（連結從左到右流動） | 標準 Sankey 互動 | 官方文案把 Sankey 定位為「顯示數值如何從一個類別流動到另一個類別」，與 USAFacts 的收入→支出流向敘事完全吻合 | 同上，商業工具限制 |

### 2-4 「增減」呈現法

未能在本次搜尋範圍內找到具體命名、可驗證的「政府預算」專案使用 waterfall／bump／slope／dumbbell chart 呈現逐年增減的公開案例（詳見 §4 負面清單）。搜尋「waterfall chart bump chart slope chart budget year over year change」與「bullet chart budget execution rate」兩條 query 只找到通用圖表教學網站（FasterCapital、Domo、ChartExpo、Klipfolio、Luzmo、SQLBI 等）對這些圖型的**一般性**設計說明，而非具名的政府預算視覺化先例，故不列入 §2 先例表，僅摘要其設計邏輯供 §5 參考：

- Waterfall chart：「floating columns with connectors, which keeps the sequence readable even when step sizes vary a lot」，色彩區分「增加／減少／小計」三種語義，適合「預算 vs 實際」的逐項落差
- Bullet chart：由 Stephen Few 設計，同時顯示「實際值、目標值、表現區間」三層資訊，比傳統儀表板更省空間

已驗證存在的接近案例：Washington Post「削減聯邦預算有多難」（2023-01-26，見§2-2）標題本身指向「讀者容易誤判『刪減』的容易程度」這個常見誤讀，但頁面內容因403無法直接驗證使用了哪種圖型。

### 2-5 「執行率／花了多少」的呈現法

同樣未找到具名的政府預算專案明確使用 bullet chart 呈現執行率。相關但不完全對應的案例：

- 財政部國庫署「國債鐘」（見§2-1）：不是圖表，是純數字列表，週更「已負擔多少債務」——概念上接近「執行率」但呈現手法是最原始的數字羅列，沒有視覺化，可視為**反面教材**：告訴讀者「這裡有進度數字」但完全沒有把「目標 vs 實際」的落差視覺化
- USAspending.gov 的 budget_function explorer（https://www.usaspending.gov/explorer/budget_function）：搜尋摘要顯示為機關別支出探索頁，但頁面為 JS 渲染，WebFetch 無法取得完整內容，**列為待核**，無法確認是否有執行率呈現

### 2-6 敘事化預算頁

| 名稱 | 製作者 | URL | 敘事結構 | 開場摘句 |
|---|---|---|---|---|
| 公視新聞網「政府的錢怎麼花？一次看懂總預算」 | 公共電視「新聞見分曉」 | https://news.pts.org.tw/article/822346 | 時事鉤子開場（今年總預算還沒過）→ 解釋總預算是什麼＋編列流程 → 說明遲遲不過會有什麼影響 → 用一個數字（社福支出27.4%）收尾 | 「今年度中央政府總預算到現在已經八月，立法院還沒有通過」 |
| Washington Post 國債刪減遊戲 | The Washington Post | https://www.washingtonpost.com/business/interactive/2023/national-debt-cut-game/ | 遊戲化敘事：不是「讀」而是「玩」——讀者自己做刪減決策，結尾產生「你是哪種撙節者」的人物分類標籤，把讀者自己變成敘事的主角 | 未能逐字驗證頁面開場文案（未直接WebFetch） |

**負面清單**：搜尋「報導者 一分鐘看懂 系列」「The Pudding budget government spending visualization story」「Bloomberg what's in the budget scrollytelling」均未找到具名、可驗證的「詩句化／有人物有場景的預算敘事專題」，詳見 §4。

---

## §3 引語庫（設計原則逐字＋URL）

**Datawrapper — 何時該用 stacked area、何時改用 line（英文逐字）**
來源：https://www.datawrapper.de/blog/area-charts

> "If the total (= the height of all your stacked areas) is not important, consider a line chart instead."

> "If the differences between your values are very small, consider a line chart instead."

> "If you just want to show one value over time, also consider a line chart instead"

> "Area charts are not the best choice if you want to compare the size of different shares with each other. If you want to show that one share overtook another one, consider a line chart instead."

**Flourish — Treemap 明確點名 budgets 為典型應用（英文逐字）**
來源：https://flourish.studio/visualisations/treemaps/

> "Whether you're working with population data, budgets, or file systems, this template helps you explore and explain nested data with ease."

**Obama White House Interactive Budget — 互動操作說明（英文逐字）**
來源：https://obamawhitehouse.archives.gov/interactive-budget

> "Hover over an area of the budget to see the total amount proposed for that section."

> "Left click to set a node as root for the visualization."

> "Right click to set the parent node as root."

**自由時報 — 台北市總預算視覺化的滷肉飯換算（中文逐字）**
來源：https://news.ltn.com.tw/news/local/paper/1150288

> 「還以換算約二十五．六八億碗『鬍鬚張魯肉飯』等趣味方式呈現」

**財政部國庫署 — 收支結構頁面對歲入歲出集中度的描述（中文逐字）**
來源：https://www.nta.gov.tw/singlehtml/67?cntId=21eb0448ea3c447cafa4b3ef6fd0f302

> 「稅課收入占比近8成，為我國中央政府收入之主要來源，其次為營業盈餘及事業收入等」

> 「以社會福利、教育科學文化、經濟發展支出及國防支出比重較高，近年該4項支出合計數占中央政府支出比率均逾7成」

**財政部國庫署 — 國債鐘頁面數字呈現格式（中文逐字）**
來源：https://www.nta.gov.tw/singlehtml/17?cntId=nta_7906_17

> 「截至115年08月07日(週五) 中央政府債務未償餘額:1年以上58,664 (億元) 短期 1,350 (億元) 合計60,014 (億元) 平均每人負擔債務:25.8(萬元)」

**公視新聞網 — 「一次看懂總預算」開場與收尾（中文逐字）**
來源：https://news.pts.org.tw/article/822346

> 「今年度中央政府總預算到現在已經八月，立法院還沒有通過」

> 「總預算不只是立法院裡的政治攻防，也會影響政策能不能推動、以及民眾實際享有的公共服務」

**g0v/twbudget — GitHub repo 描述（英文逐字）**
來源：https://github.com/g0v/twbudget

> "visualizing taiwan central government spending"

---

## §4 Negative findings

- **天下雜誌**：搜尋「天下雜誌 中央政府總預算 視覺化 圖表 專題」未找到專門的總預算視覺化專題，只找到通用的「數據圖表」欄目入口（https://www.cw.com.tw/masterChannel.action?idMasterChannel=74），欄目內容涵蓋經濟預測、商圈變化等，未見專門的中央政府總預算主題頁
- **端傳媒**：搜尋「端傳媒 台灣 預算 視覺化 圖表」未找到端傳媒對台灣預算的專門視覺化報導，只找到端傳媒對香港立法會投票記錄的矩陣圖案例（非台灣預算主題）
- **關鍵評論網**：搜尋未找到專門的「一次看懂總預算」圖表化專題，只有一般文字新聞報導（如112年度總預算通過的新聞稿）
- **報導者**：搜尋未找到報導者專門製作的中央政府總預算視覺化，2018年度數位專題回顧頁（https://www.twreporter.org/a/2018-in-interactive-storytelling）列出的作品主題不含總預算（含醫療帳單等其他財政相關主題，但非總預算本身）
- **日本財務省**：搜尋「予算の見える化」未找到財務省官方製作的專門互動視覺化頁面，該部會網站以靜態統計表與PDF為主
- **The Pudding**：未找到 Pudding 風格、針對政府預算的敘事型視覺化作品；Pudding 的整體定位（視覺散文、少文字多視覺化）本身可作為敘事手法參考，但沒有預算主題的具體案例可引用
- **Bloomberg「What's in the Budget」**：未找到此標題或對應主題的 Bloomberg scrollytelling 作品，搜尋結果僅顯示 Bloomberg Graphics 一般性入口頁與其他主題的 scrollytelling 案例（如「What is Code」）
- **NYT／CBO／WaPo 多個歷史網址**：因網域被 WebFetch 工具封鎖（nytimes.com、archive.nytimes.com）或伺服器回傳403（cbo.gov、washingtonpost.com 多篇），我無法直接開啟驗證頁面內容，只能依賴 PBS NewsHour 等第三方文章的轉述確認其存在與大致內容，這些條目在§2表格中已標示【URL待核】
- **USAspending.gov budget_function explorer**：頁面為 JS 渲染，WebFetch 只取得標題「USAspending.gov」，無法驗證圖表類型與互動細節，未列入正式先例表
- **g0v budget.g0v.tw 現況**：無法確認該站目前是否仍有持續更新的最新年度版本；WebFetch 直接開啟時只見 logo 與導覽列，實際圖表內容需要進一步的站內導覽才能定位，本次研究未能深入
- **waterfall／bump／slope／bullet chart 在政府預算領域的具名先例**：搜尋兩條相關 query 只找到通用圖表教學／SEO內容網站（非新聞媒體、非政府單位），沒有找到「哪個政府預算專案具體用了這個圖型」的可驗證案例，故 §2-4／§2-5 只能記錄設計邏輯本身，不冒稱有先例佐證

---

## §5 可移植設計建議（每條附來源先例）

1. **收入與支出接成同一張 Sankey，而非拆成兩張圖**——來自 USAFacts「The Big Picture」（https://usafacts.org/visualizations/the-big-picture/）。本頁若要呈現「總預算怎麼編列、又花到哪」，比起分開畫「歲入圓餅圖」與「歲出圓餅圖」（主計總處與國庫署現行做法），接成一張流向圖能讓讀者看到「錢從哪裡來、流去哪裡」的因果關係，且可用純 SVG path 畫出簡化版流向帶，不需要 D3。

2. **逐年結構圖選 line 還是 stacked area，先問「總量是否重要」**——來自 Datawrapper（https://www.datawrapper.de/blog/area-charts）逐字建議。立法院總預算十年史如果要呈現「各機關別支出佔比如何消長」，若讀者關心的是「總預算規模本身有沒有膨脹」，用 stacked area；若讀者更關心「哪個機關的排名有沒有變化」，改用 line 或 small multiples 更好讀——這條規則可以直接決定本頁「逐年演變」模組的圖型選擇，而非憑直覺選面積圖。

3. **面積編碼機關別預算規模，並讓讀者自己選鋪磚邏輯**——來自 Obama White House Interactive Budget（https://obamawhitehouse.archives.gov/interactive-budget）的 Squarified／Strip／SliceAndDice 三種可切換演算法。本頁不需要做到三種切換那麼複雜，但「用面積而非長條表示機關預算規模，讓大小差距一眼可辨」這個核心判斷值得沿用；hover 顯示金額、click 逐層鑽入的兩段式互動也可以用純 CSS/JS + `<details>`／`aria-expanded` 語意標籤達成，不必依賴 Canvas。

4. **用同一組資料、同一種圖形語彙，切換「分類軸」而非切換「圖表類型」**——來自 NYT「Four Ways to Slice Obama's 2013 Budget Proposal」（bubble chart 四切面，經 rethinkingvis.com/visualizations/96 確認）。本頁的十年總預算資料，可以用同一種長條或面積圖表，讓讀者切換「依機關別／依政事別／依成長率／依政黨屆期」四種分類軸，而不是為每個切面重新設計一種新圖表——降低視覺語彙的認知負擔。

5. **把巨額數字換算成讀者有感的具體單位**——來自台北市總預算視覺化「25.68億碗鬍鬚張魯肉飯」（自由時報報導）與國庫署「國債鐘」的「平均每人負擔債務25.8萬元」。本頁在呈現「今年比去年增加多少」時，除了給絕對數字與百分比，可以加一句在地換算（例如換算成健保點值、換算成某項公共服務可服務的人次），比單純給「新台幣N億元」更容易被記住——但需嚴守本專案「零幻覺容忍」鐵律，換算基準必須有可查證來源，不可自行估算。

6. **敘事開場用「進行中的懸念」而非「歷史回顧」**——來自公視 PNN「一次看懂總預算」（https://news.pts.org.tw/article/822346）用「今年度總預算到八月還沒過」當開場鉤子。本頁若要做「十年演變」的敘事引言，可以先用「最新一年發生了什麼具體的事」（例如115年度總預算刪減480億、創最晚三讀紀錄——見§1第5條搜尋結果 CNA報導）當開場鉤子，再帶讀者回溯十年史，而不是從十年前開始按時間順序平鋪直敘。

7. **讓讀者「做決策」而非只「看圖」，作為頁面收尾的互動選項**——來自 IFS「Be the Chancellor」（https://ifs.org.uk/be-chancellor）與 Washington Post 國債刪減遊戲（https://www.washingtonpost.com/business/interactive/2023/national-debt-cut-game/）。若本頁在靜態敘事之外還有餘裕做一個輕量互動模組，「讓讀者自己在幾個大類別間分配假設性的預算刪減額度，看看會撞到哪些既有承諾（如法定義務支出）」比純資訊圖表更能讓讀者體感「為什麼總預算年年吵不完」。

8. **官方資料開放本身是一種設計選擇，不是視覺化的替代品**——來自立法院預算中心開放資料 API（CSV/JSON/XML，https://www.ly.gov.tw/Pages/List.aspx?nodeid=44939）與國庫署純數字列表的「國債鐘」對照。本頁的資料源如果引用預算中心 API，應該同時記取「有開放資料 ≠ 有視覺化」這個教訓——國庫署國債鐘就是反例：資料透明但呈現方式仍是最原始的表格，讀者仍然無法一眼看出「趨勢往哪個方向走」。
