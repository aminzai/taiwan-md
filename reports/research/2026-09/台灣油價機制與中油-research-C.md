# 台灣油價機制與中油 — Research C：價格訊號與分配、亞鄰對照、人的聲音——誰受益、誰批評、加油站前的人

執行摘要：搜尋約 36 次（WebSearch 20 ＋ WebFetch 15 ＋ curl 逐字抓取 1），最重要的查證更正：（1）中油現任總經理是張敏，不是方敏（Stage 0 報告誤植，董事長方振仁與總經理張敏經中油官方新聞稿與立法院預算報告封面雙重確認）；（2）TVBS World 4/6 報導「absorbed more than NT$90.6 billion」是「億→billion」換算錯誤，正確量級約 NT$90 億（同時期風傳媒中文報導同樣寫「吸收超過90億元」），不可引用 906 億這個數字；（3）淡江大學廖惠珠並非單純的凍漲批評者——她 3/25 投書警告中油「資產負債表嚴重弱化」，但 9/15 另一篇投書轉而論證台灣需要這些補貼以保住半導體供應鏈的用電用油韌性，兩篇立場不同、都要收。

## §1 搜尋軌跡（逐條，不可省、不可事後重組）

1. 「IMF Fiscal Monitor April 2026 energy subsidies regressive」→ 找到 imf.org 官方 PDF 全文連結 → https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf [英][一手]
2. 「廖惠珠 淡江大學 中油 資產負債表 Taipei Times」→ 帶出 TVBS 對她 3 月投書的轉述，但未給原文 URL → 需另搜 [中][反方]
3. 「資源エネルギー庁 燃料油価格激変緩和補助金 2026年3月19日 再開」→ 政府 2026/3/19 出貨分起重啟補助，正式名稱改為「中東情勢を踏まえた緊急的激変緩和措置」，與 2022-2025 舊制脫鉤重新設計 → https://hojyokin-portal.jp/news/194 [日][一手轉述]
4. 「한국 최고가격제 유류세 2026 4월 27일 고유가 지원금」→ 고유가 피해지원금 4/27 起分階段發放 → https://m.korea.kr/news/policyNewsView.do?newsId=148962496 [韓][一手]
5. WebFetch https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf → WebFetch 工具回傳編碼亂碼，改用 Bash `pdftotext -layout` 本機解析成功，取得逐字（見 §2-1）[一手][英]
6. WebFetch https://www.meti.go.jp/chuto_josei/pdf/260319_2.pdf → 403 拒絕存取，日本官方 PDF 本輪未能直接取得逐字 [存疑]
7. WebFetch https://m.korea.kr/news/policyNewsView.do?newsId=148962496 → 取得「高油價受害支援金」逐字分級金額（見 §2-2）[一手][韓]
8. 「"Fiscal Monitor" April 2026 IMF "energy subsidies" regressive quote wealthier households benefit」→ 搜尋摘要沒有逐字，但帶出 imf.org 新聞稿與 Globe and Mail 報導連結 → https://www.imf.org/en/news/articles/2026/04/15/tr-04152026-press-briefing-transcript-fiscal-monitor-spring-meetings-2026 [英]
9. WebFetch 上述 imf.org 逐字稿頁 → 403 拒絕存取 [存疑]
10. WebFetch https://www.theglobeandmail.com/business/industry-news/energy-and-resources/article-imf-warns-against-broad-fuel-subsidies-to-deal-with-energy-shock/ → 取得「Targeted, temporary cash transfers that do not mask higher prices would be a far better option」逐字，及全球政府債務數字 → [英][權威二手]
11. Bash `grep -n -i "regressiv"` 本機 pdftotext 結果 → 定位到 page ix 前言逐字段落（見 §2-1）
12. Bash `sed -n` 查看 page 18 附近段落 → 找到「Governments with fuel subsidy regimes would face higher subsidy costs...absorption of losses by SOEs to shield consumers」（見 §2-1）
13. 「Liao Huei-chu Tamkang Taipei Times CPC balance sheet oil」→ 帶出 TVBS 轉述與另一篇 9/15 投書標題「Why CPC, Taipower need subsidies」→ https://www.taipeitimes.com/News/editorials/archives/2026/09/15/2003864269 [英][一手]
14. 「中油 6129億 吸收 自疫情起 經濟部 報告 增資 350億」→ 帶出經濟日報 4/8 原始報導 → https://money.udn.com/money/story/5612/9428787 [中][一手]
15. WebFetch 上述兩則 → 廖惠珠 9/15 投書其實主張「補貼必要（半導體供應鏈）」，與 3 月投書立場不同；經濟日報確認 6,129 億吸收金額對應淨值 861 億、累積虧損 792 億、負債比 92%（見 §2-1）
16. 「site:taipeitimes.com Liao Huei-chu CPC」→ 找到 3/25 投書「Managing Taipower's, CPC's debt amid chaos」→ https://www.taipeitimes.com/News/editorials/archives/2026/03/25/2003854413 [英][一手]
17. 「Taipei Times Liao Huei-chu Tamkang "balance sheet" CPC Taipower April 2026」→ 確認同一篇 3/25 投書
18. WebFetch 3/25 投書 → 取得「With severely weakened balance sheets, it is unclear how CPC and Taipower can obtain sufficient financing and compete internationally for supplies」逐字（見 §2-1）
19. 「交通部 計程車 油價 折讓 每輛 1.5萬 追加預算 中東 2026」→ 補助從 6,000 元加碼至 1.5 萬元，5/20 起申請，全台約 9 萬輛計程車受惠，經費暴增至 13 億 → https://news.pts.org.tw/article/812145 等多條 [中][一手]
20. 「能源署 汽油 柴油 銷售量 統計 2026年 凍漲 期間 3月 4月 消費量」→ 只找到動態查詢系統入口頁，未取得逐月數字 → https://www.moeaboe.gov.tw/ECW/populace/content/wfrmStatistics.aspx?type=2&menu_id=1300&sub_menu_id=5691（記入負向清單）
21. 「綠色和平 地球公民 台灣氣候行動網絡 油價凍漲 補貼 化石燃料 2026年 聲明」→ 帶出經濟日報 4/14 民團記者會報導 → https://money.udn.com/money/story/7307/9440515 [中][反方]
22. 「梁啟源 中經院 台經院 油價 凍漲 補貼 評論 2026」→ 帶出 ETtoday 舊文（見 §4 negative findings，日期經核實為 2014 年，不可用）
23. WebFetch https://money.udn.com/money/story/7307/9440515 摘要版 → 取得四位發言人姓名與立場摘要，但為求逐字改用 curl 重抓
24. Bash `curl -sL -A 'Mozilla/5.0...'` https://money.udn.com/money/story/7307/9440515 → 完整取得 4/14 記者會逐字內容（見 §2-4）[中][一手][反方]
25. WebFetch https://finance.ettoday.net/news/422994 → 核實發布日期為 2014/11/7，非 2026 年時事評論，排除（見 §4）
26. WebFetch https://news.pts.org.tw/article/812145 → 確認計程車補助細節但未含逐字引語
27. 「中油 董事長 方振仁 總經理 立法院 答詢 淨值 逐字 2026」→ 找到中油官方新聞稿「新任董事長方振仁、總經理張敏就任」與立法院 115 年度預算報告封面（2026/5/7），確認總經理是張敏非方敏 → https://www.cpc.com.tw/News_Content.aspx?n=28&s=94632 [一手]
28. 「台灣石油工會 凍漲 中油 意見 聲明 2026」→ 帶出壹蘋新聞網 2026/6/1 中油 80 週年慶報導，工會理事長陳嘉麟逐字 → https://news.nextapple.com/finance/20260601/5AE966969630FE14C8C5CB8D6753E7AA [中][一手]
29. WebFetch 上述壹蘋新聞網頁 → 取得陳嘉麟完整逐字（見 §2-6、§3）
30. 「加油站 排隊 台灣 2026年9月13日 漲價前夕 車潮」→ 僅找到中油/經濟部調價公告，無現場排隊報導 → 記入負向清單
31. 「加油站 排隊 2026年3月29日 汽油 明起調漲 台灣」→ 僅找到經濟部 3/28 公告（3/30-4/5 各漲 1.7/1.5 元），無現場排隊報導 → 記入負向清單
32. 「中油 亞鄰比較表 cpc.com.tw 日本 韓國 香港 新加坡」→ 定位到官方頁面路徑 cpc.com.tw/cp.aspx?n=58／n=66／n=2827，但未能擷取當週動態表格數字
33. WebFetch https://www.cpc.com.tw/cp.aspx?n=92 → 頁面為導覽結構，未含亞鄰比較表數字（記入負向清單）
34. 「新加坡 香港 汽油 補貼 2026 中東戰爭 政府 措施」→ 香港政府 4/9、4/29 兩波措施：商用車柴油每公升補貼 3 元（約 1.8 億港元，至 6/29 止）、的士/公共小巴/校巴石油氣每公升補貼 0.5 元（約 3,840 萬港元）→ https://www.info.gov.hk/gia/general/202604/29/P2026042900787.htm [中][一手]；新加坡查無 [負向清單]
35. 「PTT Dcard 亞鄰最低價 油價 台灣 討論 熱門」→ 查無「亞鄰最低價」專門高聲量貼文，僅有一般漲價新聞轉貼串 [負向清單]
36. 「計程車司機 貨運業 遊覽車 凍漲 油價 說法 2026 受訪」→ 帶出 TVBS 5/21 Uber 司機簡修智報導與 UDN 6/10 全國汽車駕駛人權益聯盟理事長劉鴻樟報導 → https://news.tvbs.com.tw/money/3205346、https://udn.com/news/story/7266/9556477 [中][質地]
37. WebFetch 上述兩則 → 取得司機逐字（見 §3）
38. 「油價 降價 2026年6月底 加油站 民眾 反應」→ 搜尋結果多數混入中國大陸油價新聞（news.qq.com／chinanews.com／sina.cn），**簡體來源警戒，明確排除**；僅確認台灣 6/22-6/28 汽油降 1 元、柴油降 0.7 元的官方公告，無台灣現場民眾反應報導 [負向清單][簡體警戒]

## §2 Findings（依子題分節；只寫世界，不寫任務）

### 2-1 財政與分配：IMF、廖惠珠、CPC 帳本

【來源】https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf
— IMF《Fiscal Monitor》2026 年 4 月號，前言（page ix）
【逐字】「Broad-based energy subsidies are distortionary, fiscally expensive, regressive, and difficult to unwind and carry sizable international spillovers. When supply is constrained, demand must adjust worldwide.」（署名 Rodrigo Valdés，Director, Fiscal Affairs Department）
【信度】一手

【來源】https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf
— 同刊物 page 18，討論「中東戰爭延長」情境下各國財政曝險
【逐字】「Governments with fuel subsidy regimes would face higher subsidy costs, as governments intervene through subsidies, tax adjustments, administered pricing, and the absorption of losses by SOEs to shield consumers. These measures shift the cost of global price shocks directly onto public finances.」
【信度】一手（注意：這兩段是通論性段落，並未點名台灣或中油，是「適用於台灣個案的通則」而非「IMF 專門評論台灣」，引用時需誠實標注這個區別）

【來源】https://www.taipeitimes.com/News/editorials/archives/2026/03/25/2003854413 — Taipei Times 投書，作者廖惠珠（淡江大學經濟系教授），2026/3/25
【逐字】「With severely weakened balance sheets, it is unclear how CPC and Taipower can obtain sufficient financing and compete internationally for supplies.」
【信度】一手

【來源】https://www.taipeitimes.com/News/editorials/archives/2026/09/15/2003864269 — Taipei Times 投書，作者同為廖惠珠，2026/9/15，標題「Why CPC, Taipower need subsidies」
【逐字】文中主張台灣約 90% 全球先進晶片依賴台灣半導體供應鏈，電力與油品價格「never fully reflected their cost」，2026 上半年 GDP 成長 13.72%（半導體與資通訊產業帶動），因此中油、台電在 2030 年前是台灣唯一能快速大量採購原油因應用電需求成長的企業，補貼是保住這條供應鏈的必要成本
【信度】一手（同一位作者半年內兩篇投書立場明顯不同：3 月警告財務風險、9 月轉為論證補貼必要性，兩篇都要收，不可只引一篇代表她的立場）

【來源】https://www.taipeitimes.com/News/editorials/archives/2026/07/03/2003860140 — Taipei Times 社論「CPC was smart to freeze prices」，作者魏季宏（Taiwan International Cultural and Educational Public Interest Association 理事長），2026/7/3
【逐字】「the NT$17.7 billion that CPC has absorbed to date has helped to shield Taiwan's entire economy」；「CPC sits upstream of virtually all other companies. Once oil prices rise, the impact is felt across the supply chain from transport costs and raw materials to prices at street-side snack stalls.」；「The government's strategy has been to position the firewall for inflation right at the gate.」
【信度】一手（此為 11 週凍漲後、6 月底降價當週發表的社論，是最直接支持凍漲政策的公開論述之一）

【來源】https://world.storm.mg/articles/1125769 — The Storm Media 英文版社論「Taiwan's Trillion-Dollar Energy Trap: Why the IMF Is Sounding the Alarm」，2026/4/28
【逐字】「According to the Ministry, CPC has absorbed NT$612.9 billion in costs since the COVID-19 pandemic, through the Russia-Ukraine war, and into the current US-Iran conflict. The result is NT$79.2 billion in accumulated losses and a debt ratio of 92 percent.」
【信度】權威二手（換算單位正確：612.9 billion = 6,129 億，79.2 billion = 792 億，與下條中文一手數字一致）

【來源】https://money.udn.com/money/story/5612/9428787 — 經濟日報「美伊戰火影響 中油累計吸收6,129億 擬增資、融資共計6,500億救財務」，2026/4/8
【逐字】截至 2026 年 3 月底：淨值 861 億元、累積虧損 792 億元、負債比率突破 92%；累計未足額調整的吸收金額 6,129 億元；改善方案三項：增資 3,500 億元（經濟部已核請行政院同意 2027 年先挹注 1,687 億元，含填補 2025 年底待填補虧損 770 億元、撥付 917 億元供天然氣穩定供應建設）、專案融資 3,000 億元、政府預算撥補
【信度】一手

【來源】https://news.tvbs.com.tw/english/3170632 — TVBS World，2026/4/6
【逐字】「CPC Corporation (台灣中油) has absorbed more than NT$90.6 billion (around US$2.83 billion) since the U.S.-Iran war began Feb. 28 — a figure that now exceeds its entire net worth of NT$85.4 billion」
【來源】https://www.storm.mg/article/11118912 — 風傳媒中文版「累積虧損792億元！美伊戰火打出中油財務黑洞」，2026/4/8
【逐字】「立委質疑，中油為了避免物價波動而吸收超過90億元」
【信度】權威二手（數字校正：TVBS 英文版寫「NT$90.6 billion」是「億→billion」換算誤植——90.6 億新台幣應譯為約 NT$9.06 billion，而非 NT$90.6 billion；同時期中文報導寫「超過90億元」，量級與經濟部 3/30 官方公布的「2/28–3/29 累計逾69.9億」銜接一致。淨值 854 億 vs 861 億兩則報導數字接近，屬同一量級的正常誤差範圍，惟吸收金額的「億／billion」換算錯誤需在文章中避免沿用英文原始寫法）

### 2-2 亞鄰對照：日本、韓國、香港、新加坡

【來源】https://hojyokin-portal.jp/news/194 — 補助金ポータル，2026/3
【逐字】「政府は2026年3月19日出荷分から、ガソリン価格を抑えるための補助を再開する方針」
【信度】權威二手（日本經產省官方 PDF https://www.meti.go.jp/chuto_josei/pdf/260319_2.pdf 本輪 WebFetch 回傳 403，無法直接取得逐字，此為轉述二手，正式名稱為「中東情勢を踏まえた緊急的激変緩和措置」，與 2022-2025 年施行的舊制「燃料油価格激変緩和補助金」是脫鉤重新設計的新措施，不宜混為同一制度的延續。補助對象是石油元売業者/批發端，機制是把汽油零售價壓在約每公升 170 日圓左右，超過部分由政府補貼；柴油、重油、燈油比照汽油同額補貼；航空燃油補貼額為汽油補貼額的四成）

【來源】https://m.korea.kr/news/policyNewsView.do?newsId=148962496 — 대한민국 정책브리핑（韓國政府官方政策簡報）
【逐字】弱勢層（基礎生活保障對象）55萬韓元、次貧困階層／單親家庭 45萬韓元，上述對象若居住非首都圈或人口減少地區再加 5萬韓元（合計最高 60萬韓元）；其餘 70% 國民：首都圈 10萬韓元、非首都圈 15萬韓元、人口減少優惠支援地區 20萬韓元、特別支援地區 25萬韓元；弱勢層 4/27–5/8 優先申請發放，其餘 70% 國民 5/18–7/3 申請發放，資金使用期限至 8/31
【信度】一手（此頁未提及 26.2 兆韓元追加預算總額或與最高價格制／油稅減免的直接關聯，這兩項數字目前只查到 TVBS World 轉引 Reuters 的版本，見下條）

【來源】https://news.tvbs.com.tw/english/3170632 — TVBS World，2026/4/6，引用 Reuters
【逐字】「Japan is tapping 800 billion yen (around US$5.02 billion) in reserve funds to finance direct subsidies. South Korea proposed a 26.2 trillion won (around US$17.3 billion) supplementary budget. Indonesia budgeted 381.3 trillion rupiah (around US$22.4 billion) for energy subsidies, according to Reuters.」
【信度】權威二手（本輪未能直接取得 Reuters 原始報導核對，這三個數字目前只有 TVBS 這一個轉引來源）

【來源】https://www.info.gov.hk/gia/general/202604/29/P2026042900787.htm — 香港特區政府新聞公報，2026/4/29
【來源】https://www.info.gov.hk/gia/general/202604/09/P2026040900662.htm — 香港特區政府新聞公報，2026/4/9
【逐字】香港自 2026/4/30 起推出商用車柴油補貼每公升 3 港元（估計成本約 1.8 億港元，為期兩個月至 6/29 止）；的士、公共小巴、校巴石油氣補貼每公升 0.5 港元（估計約 3,840 萬港元）；並成立「跨部門監察燃油供應專責組」評估地緣政治變化下的燃料供應與定價
【信度】一手（這推翻了「日韓有補貼、台灣以外亞鄰都靠市場」的簡化預設——香港對商用車／的士的柴油與石油氣同樣有政府直接補貼，只是補貼對象鎖定營業用車而非全體消費者，與台灣、日韓的「全民零售價」補貼邏輯不同）

【來源】（新加坡）本輪多組中英文搜尋查無新加坡政府因本次中東戰爭對燃油實施補貼的官方消息
【信度】存疑——不可從「查無報導」推論新加坡「沒有」補貼，只能誠實記錄本輪未查到

【來源】https://news.tvbs.com.tw/english/3170632 — TVBS World，2026/4/6（同一天 CPC 官方數字）
【逐字】「Taiwan's 95-octane gasoline at NT$33.9 per liter compares with NT$49.5 (around US$1.55) for 95-octane in South Korea, NT$85.9 (around US$2.68) for 95-octane in Singapore, and NT$132.1 (around US$4.13) for 98-octane in Hong Kong.」
【信度】權威二手（同一天四地價格並陳的快照，比「亞鄰最低價」這個抽象說法更具體；中油官網「亞鄰各國比較表」cpc.com.tw/cp.aspx?n=58／n=66／n=2827 有更完整的逐週資料，但本輪 WebFetch 只定位到頁面路徑，未能擷取到本週〈9/14–9/20〉的動態表格數字）

【來源】https://news.tvbs.com.tw/english/3170632
【逐字】「Those governments are using direct budget allocations, while Taiwan relies primarily on CPC to absorb costs. This approach shields government budgets in the short term but concentrates risk on the state-owned company.」
【信度】權威二手（這是機制差異的核心論點：日韓是政府預算直接補貼給元売業者/批發商，台灣是先讓國營中油自己墊，之後才用追加預算補回去）

### 2-3 誰受益：追加預算裡的分配

【來源】https://news.ltn.com.tw/news/politics/breakingnews/5561920 — 自由時報，2026/9/3
【逐字】「因應中東衝突民生安定措施編列1875億元，包含補貼中油汽柴油凍漲經費1014億元、補貼家用液化石油氣凍漲84億元、台電電價凍漲711億元，以及交通部補貼國內航空票價、計程車油價折讓等共26億元、農業部補貼化學肥料原料漲幅與遠洋漁船作業、靠港整補經費總計40億元。」（經濟部次長賴建信 9/3 行政院會後記者會發言）
【信度】一手（1014+84+711+26+40=1875，加總與官方公告數字吻合，此條把「誰受益」的具體分配一次列清楚：中油汽柴油、桶裝瓦斯用戶、台電電價用戶、國內航空乘客與計程車業者、化肥使用的農民與遠洋漁船）

【來源】https://news.pts.org.tw/article/812145 — 公視新聞網，2026/6（計程車補助加碼）
【來源】https://money.udn.com/money/story/7307/9553375 — 經濟日報，計程車油價補助加碼報導
【逐字】計程車油價補助自每車 6,000 元加碼至最高 1.5 萬元（維持每公升折抵 5 元），5/20 起開放登記、8/31 截止申請、可使用至 2026/12/31，全台約 9 萬輛計程車符合資格（7.2 萬輛已完成登記），交通部總補貼經費約 13 億元
【信度】一手

【來源】https://news.tvbs.com.tw/local/3225926 — TVBS 新聞網，計程車補助影音報導
【逐字】「中東局勢價飆漲！計程車補助『6千提升至1.5萬』 年底前都可用」
【信度】一手（與上條互證加碼幅度）

【負向清單】能源署逐月汽柴油銷售量統計（用以驗證「補貼期間消費量是否不減反增、節能訊號是否被壓」）——查到官方統計入口頁 https://www.moeaboe.gov.tw/ECW/populace/content/wfrmStatistics.aspx?type=2&menu_id=1300&sub_menu_id=5691，但這是動態查詢系統，本輪工具（WebSearch／WebFetch／curl）都無法擷取到 2026 年 3–8 月具體銷售量數字，**這是本題「誰受益／節能訊號」falsify 清單裡最關鍵的一塊缺口，配額內未及查**，需要下一輪用能親自登入查詢介面或另尋能源統計年報 PDF

【負向清單】家用汽油 vs 運輸業柴油的消費結構逐年數字（能源署能源統計年報/月報）——同上，本輪未查到具體數字表

### 2-4 環團與學者：對「凍漲」本身的公開意見

【來源】https://money.udn.com/money/story/7307/9440515 — 經濟日報「能源供給動盪 民團籲推動節能運動非僅靠補貼」，記者林敬殷，2026/4/14 12:05
— 主辦：主婦聯盟環境保護基金會、綠色公民行動聯盟、台灣氣候行動網絡研究中心；地點：立法院；記者會名稱「面對能源危機 凍漲治標節能治本」
【逐字】國立中山大學公共事務管理研究所教授兼所長張瓊婷：「進口能源補貼的意思是用補貼後的價錢在過活，比方說一桶油100元，政府補貼60元，補貼後會讓大家以為是用40元過日子，但這種情況可能會排擠到其他如教育還有社會福利的重要支出。」
【逐字】主婦聯盟環境保護基金會執行長吳碧霜：「油電補貼是短期的止痛，但若沒有改變用電的行為或制度的設計，問題將一再重演。」「今天台灣面對的是一個社會選擇問題，是選擇用補貼方式解決危機，還是選擇建立更有韌性的能源社會。」
【逐字】綠色公民行動聯盟資深研究員陳詩婷：「台灣有高達55%的電力是由工業部門使用，理應承擔相應的節電責任……經濟部設定的節電率偏低，無法有效驅動產業進行深度節能」，呼籲加嚴能源大用戶與超大用戶節電率目標、公開未達標企業名單
【逐字】中央研究院經濟研究所研究員蕭代基：「政府現在對各種公共事務都採用非常多補貼，形成『補貼成癮』現象，應該讓能源價格調整反映成本」，另建議把節省下來的錢返還或普發給低收入戶家庭
【信度】一手（這組記者會是本輪查到唯一直接針對「油價／電價凍漲」政策本身——而非石化擴建——提出批評的環團／學者集體發言，命中任務清單第 4 題核心）

【負向清單】綠色和平、地球公民基金會、環境權保障基金會三個機構個別對「油價凍漲」本身的聲明——查無；綠色和平本輪能查到的僅有 2026/1/27 對中油新四輕擴建的抗議（既有 Stage 0 finding），與凍漲政策是不同議題

【負向清單】梁啟源、中經院、台經院、台大經濟系 2026 年對本次凍漲的具體評論——查無。搜尋「梁啟源 中經院 台經院 油價 凍漲 補貼 評論 2026」帶出的 ETtoday 報導「今日凍漲導致未來大漲 梁啟源：油電價應隨成本調整」經 WebFetch 核實**發布日期為 2014 年 11 月 7 日**，是十二年前的舊文，與本次美伊戰爭凍漲事件無關，不可誤植為 2026 年評論引用

### 2-5 人的聲音：加油站前與方向盤後

【來源】https://www.ctee.com.tw/news/20260322700647-431401 — 工商時報，記者周麗蘭，2026/3/22 21:07
【逐字】「23日凌晨零時起，汽、柴油價格各調漲1.8元及1.4元……雲林科技工業區旁的雅虎加油站晚間8點半每一個入口至少排隊10輛，民眾直呼『1.8元，很有感！』」「加油站人員臨時以三角錐隔出排隊路線，機車和汽車一樣要排隊，沒有豁免的權利。」「一輛小發財車載著4、5個油桶，一次加滿！一名婦女加滿20公升，很開心『省了36元，省就是賺』。」「80多歲陳姓阿嬤說，上個月瓦斯已經漲100元，今天看到新聞說油價要漲，她趕緊騎摩托車要去加，可惜油箱還是滿的。」
【信度】一手（Ctrl-F 可驗）

【來源】https://news.tvbs.com.tw/money/3205346 — TVBS 新聞網，2026/5/21 21:59
【逐字】Uber 司機簡修智：「去年每月油錢只需幾千元，但因油價上漲，這個月加油多花了好幾千元，只能停在路邊等單，不敢一直開車繞行。」
【逐字】職業駕駛顧問公司業者洪宏法：「6000元雖不無小補，但駕駛更在乎整體交通大環境，若物價沒有真正穩定下來，民眾不想出門消費，也不會叫車。」
【信度】一手

【來源】https://udn.com/news/story/7266/9556477 — 聯合新聞網，2026/6/10
【逐字】全國汽車駕駛人權益聯盟理事長劉鴻樟：「職業駕駛需要的是合理調整運價，並非拿人民納稅錢撒幣。」
【逐字】交通部長陳世凱回應：運價屬地方政府權責，建議工會向地方政府提出，交通部將視需要協助；強調每車最高補貼1.5萬元的目的是減輕油價上漲負擔、鼓勵搭乘公共運輸
【信度】一手

【來源】https://news.nextapple.com/finance/20260601/5AE966969630FE14C8C5CB8D6753E7AA — 壹蘋新聞網，2026/6/1，中油 80 週年慶祝大會
【逐字】台灣石油工會理事長陳嘉麟：「（中油）還要加上一個叫做立法院」；「國外的油氣公司都賺翻了，中油則背負國營事業的責任，為了配合政府政策而凍漲」；「外面的風浪越大，中油站就越站在最前面，外面漲最凶的時候，中油更是吸收最多」
【信度】一手（工會訴求：夜點費併入工資、調薪高於公務員、一年兩退，盼政府盡快撥補中油財務）

【負向清單】3/29（3/30 漲 1.7 元前夕）加油站現場排隊報導——查無，僅有經濟部/中油調價公告本身
【負向清單】9/13（9/14 漲 0.7 元前夕）加油站現場排隊報導——查無，與 Stage 0 既有 negative finding 一致，本輪追加搜尋仍未查到
【負向清單】4 月凍漲期間、6 月底降價當週的台灣加油站現場報導——查無（搜尋「油價 降價 2026年6月底 加油站 民眾 反應」時搜尋結果混入大量中國大陸油價新聞，簡體來源警戒排除）
【負向清單】小吃店、貨運業、遊覽車業者、漁民本人受訪逐字——查無，僅查到計程車／Uber 司機與相關公會代表的說法
【負向清單】PTT／Dcard 公開討論中「亞鄰最低價」相關高聲量貼文——查無符合條件的貼文

### 2-6 中油作為政策工具的自我陳述

【來源】https://www.cpc.com.tw/News_Content.aspx?n=28&s=94632 — 台灣中油官方新聞稿「台灣中油公司新任董事長方振仁、總經理張敏就任」
【來源】https://ppg.ly.gov.tw/ppg/SittingAttachment/download/2026050727/PPGB60500_4200_21066_1150508_0003.pdf — 立法院第11屆第5會期經濟委員會第13次全體委員會議「中油公司115年度營業預算報告」封面，2026/5/7
【逐字】封面列名「董事長 方振仁　總經理　張　敏」
【信度】一手（**人事校正**：Stage 0 報告寫的「總經理方敏」有誤，正確姓名是張敏；中油人事沿革為李順欽〔董事長〕／方振仁〔總經理〕→ 方振仁〔董事長〕／張敏〔總經理〕）

【來源】https://www.cna.com.tw/news/afe/202603180132.aspx — 中央社，2026/3/18
【逐字】經濟部次長賴建信：「近兩週中油油價吸收金額新台幣33億元」；「中東戰事期間，中油在亞鄰最低價之下仍吸收6成」
【信度】一手（此為經濟部次長代表機制發言，非中油自身高層，但直接對應任務清單「吸收至少六成」的查證）

【來源】https://www.storm.mg/article/11118912 — 風傳媒，2026/4/8
【逐字】「中油董事長方振仁指出，目前規劃融資額度為3,000億元」；經濟部長龔明鑫：「融資是要借新還舊，透過現在較低的利息來先還清過去的舊債」
【信度】一手（中文原文，方振仁專案融資 3,000 億元的規劃數字）

【來源】https://news.tvbs.com.tw/english/3170632 — TVBS World，2026/4/6
【逐字】「CPC president Chang Min (張敏) said April 1 that the formula no longer reflects the company's actual crude oil import sources, which now come primarily from the United States rather than the Middle East」；「CPC will commission third-party think tanks — including the Chung-Hua Institution for Economic Research, the Taiwan Institute of Economic Research and the Taiwan Research Institute — to review the formula」
【信度】權威二手（此為英文報導轉引張敏 4/1 談話，中文逐字原文本輪未查獲，只能降級標注，不可當中文逐字引用；但確認了總經理姓名應為張敏而非方敏，與上條人事校正互證）

【負向清單】中油官方或工會使用「破產重整」字眼的逐字紀錄——查無，Stage 0 提到的「董事曾示警最快明年資不抵債」本輪未查到「破產重整」的原始出處
【負向清單】董事長方振仁「淨值」「嚴重」等字眼的中文逐字（TVBS 英文報導寫"severe"是轉譯，非中文逐字）——查無中文原始出處，不可作逐字引語使用

## §3 引語庫（能當文章聲音的 verbatim）

- 「省了36元，省就是賺」— 雅虎加油站加滿 20 公升的婦女，2026/3/22，https://www.ctee.com.tw/news/20260322700647-431401，Ctrl-F 可驗 ✓
- 「上個月瓦斯已經漲100元，今天看到新聞說油價要漲，她趕緊騎摩托車要去加，可惜油箱還是滿的」— 80多歲陳姓阿嬤（記者轉述非直引），同上，Ctrl-F 可驗 ✓（非直引，記者敘述句）
- 「1.8元，很有感！」— 雅虎加油站排隊民眾（記者轉述非直引），同上
- 「去年每月油錢只需幾千元，但因油價上漲，這個月加油多花了好幾千元，只能停在路邊等單，不敢一直開車繞行」— Uber 司機簡修智，2026/5/21，https://news.tvbs.com.tw/money/3205346，Ctrl-F 可驗 ✓
- 「6000元雖不無小補，但駕駛更在乎整體交通大環境，若物價沒有真正穩定下來，民眾不想出門消費，也不會叫車」— 職業駕駛顧問公司業者洪宏法，同上
- 「職業駕駛需要的是合理調整運價，並非拿人民納稅錢撒幣」— 全國汽車駕駛人權益聯盟理事長劉鴻樟，2026/6/10，https://udn.com/news/story/7266/9556477，Ctrl-F 可驗 ✓
- 「外面的風浪越大，中油站就越站在最前面，外面漲最凶的時候，中油更是吸收最多」— 台灣石油工會理事長陳嘉麟，2026/6/1，https://news.nextapple.com/finance/20260601/5AE966969630FE14C8C5CB8D6753E7AA，Ctrl-F 可驗 ✓
- 「國外的油氣公司都賺翻了，中油則背負國營事業的責任，為了配合政府政策而凍漲」— 陳嘉麟，同上
- 「油電補貼是短期的止痛，但若沒有改變用電的行為或制度的設計，問題將一再重演」— 主婦聯盟環境保護基金會執行長吳碧霜，2026/4/14，https://money.udn.com/money/story/7307/9440515，Ctrl-F 可驗 ✓
- 「政府現在對各種公共事務都採用非常多補貼，形成『補貼成癮』現象」— 中央研究院經濟研究所研究員蕭代基，同上
- 「一桶油100元，政府補貼60元，補貼後會讓大家以為是用40元過日子」— 中山大學公共事務管理研究所教授張瓊婷，同上
- 「With severely weakened balance sheets, it is unclear how CPC and Taipower can obtain sufficient financing and compete internationally for supplies.」— 廖惠珠（淡江大學經濟系），Taipei Times，2026/3/25
- 「the NT$17.7 billion that CPC has absorbed to date has helped to shield Taiwan's entire economy」— 魏季宏，Taipei Times 社論，2026/7/3
- 「Broad-based energy subsidies are distortionary, fiscally expensive, regressive, and difficult to unwind and carry sizable international spillovers.」— Rodrigo Valdés，IMF Fiscal Monitor 前言，2026/4，page ix

## §4 Negative findings（搜了沒找到什麼——防下輪重搜＋防幻覺補洞）

- 查無能源署 2026 年 3–8 月逐月汽柴油銷售量具體數字（試過「能源署 汽油 柴油 銷售量 統計 2026年 凍漲」），只找到動態查詢系統入口頁，這是驗證「補貼是否壓掉節能訊號」的關鍵缺口，配額內未及查
- 查無台灣汽柴油消費結構（家用汽油 vs 運輸業柴油）逐年統計數字，同上原因
- 查無 9/13（9/14 漲價前夕）與 3/29（3/30 漲價前夕）的加油站現場排隊報導（試過「加油站 排隊 台灣 2026年9月13日」「加油站 排隊 2026年3月29日」），只查到官方調價公告本身
- 查無 4 月凍漲期間、6 月底降價當週台灣加油站現場報導（搜尋「油價 降價 2026年6月底」時大量結果為中國大陸油價新聞，簡體來源警戒予以排除）
- 查無小吃店、貨運業、遊覽車業者、漁民本人受訪逐字（試過「計程車司機 貨運業 遊覽車 凍漲 油價 說法 2026」），只查到計程車╱Uber 司機與相關公會代表的說法
- 查無 PTT／Dcard 公開討論中「亞鄰最低價」相關高聲量貼文
- 查無中油官網「亞鄰各國比較表」（cpc.com.tw/cp.aspx?n=58／n=66／n=2827）本週（9/14–9/20）的具體逐週數字，頁面路徑已定位但動態表格內容本輪工具無法擷取
- 查無新加坡政府因本次中東戰爭對燃油實施補貼的官方消息（試過「新加坡 香港 汽油 補貼 2026 中東戰爭」）——只查到香港與日韓的措施，新加坡的缺席不能推論成「新加坡沒有補貼」，只能誠實記錄未查到
- 查無 Reuters 關於日韓印尼補貼規模的原始報導（試過搜尋 Reuters 原稿），本輪只能透過 TVBS World 轉引核對
- 查無日本經產省 260319_2.pdf 官方文件逐字（WebFetch 回傳 403），亦查無韓國 26.2 兆韓元追加預算的一手官方文件（korea.kr 頁面本身未提及此數字）
- 查無綠色和平、地球公民基金會、環境權保障基金會三個機構各自對「油價凍漲」政策本身（非石化擴建）的聲明；主婦聯盟／綠色公民行動聯盟／台灣氣候行動網絡研究中心的聯合記者會（4/14）補上了同一子題的材料，但這三個機構本身仍缺
- 查無梁啟源、中經院、台經院、台大經濟系 2026 年對本次凍漲的具體評論——搜尋「梁啟源」帶出的 ETtoday 報導核實後是 2014 年舊文，已排除
- 查無中油官方或工會使用「破產重整」字眼的逐字紀錄
- 查無董事長方振仁使用「淨值」等關鍵字的中文逐字原文（僅有英文轉述的"severe"）

## §5 質地素材（給 writer：場景／意象／數字對比／結尾畫面候選）

- 3/22 雅虎加油站的畫面本身就是全篇最強的候選收尾：三角錐隔出排隊動線、機車汽車一視同仁「沒有豁免的權利」、小發財車一次扛 4、5 個油桶、婦女「省了36元，省就是賺」的開心，跟 80 多歲阿嬤騎車趕去加油才發現油箱早已加滿的小小徒勞——省小錢的即時心理 vs. 帳上千億的延遲付款，兩個時間尺度在同一個加油站裡並存
- 張瓊婷「一桶油100元，政府補貼60元，讓大家以為是用40元過日子」這個比喻可以直接轉成視覺化的價格拆解圖，跟中油自己的「7D3B 公式」拆解圖並列，形成「政府補貼的錯覺 vs. 機制的精確」對照
- 同一天（2026/4/6）的亞鄰四地價格快照：台灣 33.9 元、韓國 49.5 元、新加坡 85.9 元、香港 132.1 元——比「亞鄰最低價」這種抽象說法更適合做成一張橫向比較的長條圖
- 三種補貼模式的畫面並陳：日韓是政府直接發錢／補貼給油品批發商；香港是精準鎖定商用車與的士的柴油／液化石油氣；台灣是先讓中油自己墊、之後用追加預算補——「誰先掏錢」這個順序本身就是三地治理哲學的縮影
- Uber 司機簡修智「只能停在路邊等單，不敢一直開車繞行」——這是個體層級真實發生的節能行為改變，可以跟「查無總體銷售量數據」的缺口對照，寫成「我們看得到一個人怎麼開始省油，卻看不到全台灣是不是真的少開了車」
- 台灣石油工會理事長陳嘉麟把中油形容成「外面的風浪越大，中油站就越站在最前面」——中油作為政策防波堤的自我形象，適合承接「先墊的人」這條主線
- 廖惠珠半年內兩篇立場不同的投書（3 月警告財務風險、9 月論證半導體供應鏈需要補貼）本身是一條完整的敘事線：同一個經濟學者，隨著戰事拖長、AI 產業成長數字出爐，對「該不該補貼」的公開論述也在移動——這比單純引用一句「警告」更誠實地呈現辯論本身的動態
- 計程車補助從 6,000 元加碼到 1.5 萬元、劉鴻樟「並非拿人民納稅錢撒幣，需要的是合理調整運價」——補貼與結構性訴求之間的落差，也是「誰受益」底下一個小但具體的分歧點
