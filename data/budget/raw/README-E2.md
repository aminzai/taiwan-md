# 中央政府總預算十年演變 — 一手資料清單（E2：歲入歲出總額／政事別／決算／債務／GDP占比／特別預算）

> 本清單由 sub-agent「E2」負責，範圍不含機關別（機關別由另一 sub-agent 負責，見 `README-E1.md`）。
> WebSearch + WebFetch 合計已用滿 40 次配額，以下為配額內完成的抓取結果。

| 檔名 | 來源 URL | 下載日期 | 內容一句話 | 抓取方式 |
|---|---|---|---|---|
| `fy115-zongshuoming-dgbas.pdf` | https://ws.dgbas.gov.tw/001/Upload/461/relfile/11333/235176/b%E7%B8%BD%E8%AA%AA%E6%98%8E.pdf | 2026-08-17 | 主計總處115年度中央政府總預算案總說明（完整版，11501行）。內含**參考表4**（歷年中央政府淨支出對GDP之比率，105-115年）、**參考表6**（歷年中央政府歲入歲出淨收支概況表，105-115年，105-113為決算審定數/114為法定預算數/115為預算案數）、**表3-1**（中央政府總預算及特別預算情形簡表，含債務未償餘額預估數與特別預算列表）、**表3-3**（115年度歲出政事別編列情形表）、**歲入歲出簡明比較分析表**（115本年度數/114上年度數/113前年度決算數三欄比較）。是本次研究最主要的一手資料來源。 | curl 直接下載 + `pdftotext -layout` 轉文字 + grep/sed 定位表格 |
| `fy114-zongshuoming-dgbas.pdf` | https://ws.dgbas.gov.tw/001/Upload/461/relfile/11333/233556/%E5%A3%B9.pdf | 2026-08-17 | 主計總處114年度中央政府總預算案總說明「壹、前言」章節（僅194行，非完整版）。內含114年度政事別編列前4大類金額、GDP預測、債務未償餘額占GDP預估比率。 | curl 直接下載 + `pdftotext -layout` |
| `fy108-zhengshibie-table-mof.pdf` | https://service.mof.gov.tw/public/Data/statistic/Year_Fin/108%E9%9B%BB%E5%AD%90%E6%9B%B8/htm/31030.pdf | 2026-08-17 | 財政部108年財政統計年報「表1-3 各級政府歲出淨額－按政事別分」，85-109年度時間序列。**注意：此表為中央+地方合併之「各級政府」口徑，非中央政府單獨口徑**，未採用為主要資料源（改用fy115總說明之參考表6取得中央政府單獨口徑），僅作為交叉參考保留。 | curl 直接下載 |
| `fy105-114-debt-outstanding-nta.csv` | https://lgd.nta.gov.tw/newlgd/opendata/D3-09.csv | 2026-08-17 | 財政部國庫署「歷年各級政府債務概況表」開放資料，含93-114年度中央/地方/直轄市/縣市各級政府1年以上及未滿1年公共債務未償餘額金額與占GDP前3年平均比率。已篩選出中央政府列，105-114年度。115年度尚無資料（NTA每半年更新一次）。 | curl 直接下載 CSV |
| `fy105-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=25581 | 2026-08-17 | 主計總處「105年度中央政府總預算案立法院審議結果」新聞稿，含歲入歲出原列數/審議後數/增減金額。 | WebFetch 逐字擷取後 curl 存檔 HTML |
| `fy106-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=23541 | 2026-08-17 | 同上，106年度。 | 同上 |
| `fy108-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=26834 | 2026-08-17 | 同上，108年度。 | 同上 |
| `fy109-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=24406 | 2026-08-17 | 同上，109年度。 | 同上 |
| `fy110-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=27272 | 2026-08-17 | 同上，110年度。 | 同上 |
| `fy111-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=209620 | 2026-08-17 | 同上，111年度。 | 同上 |
| `fy112-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=230687 | 2026-08-17 | 同上，112年度（僅取得歲出面數字，歲入面新聞稿內未見或未擷取到）。 | 同上 |
| `fy113-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=232744 | 2026-08-17 | 同上，113年度。 | 同上 |
| `fy114-zhuijia-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=235260 | 2026-08-17 | 主計總處「114年度中央政府總預算**追加**預算案立法院審議結果」新聞稿（114年8月29日三讀，追加819億元）。**114年度原始（非追加）審議結果新聞稿正式URL未尋得**，114年度legal/proposed數字改用fy115總說明PDF參考表6及WebSearch摘要替代，見JSON notes。 | 同上 |
| `fy115-renxing-specialbudget-ly-shenyi-jieguo-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=235407 | 2026-08-17 | 主計總處「中央政府因應國際情勢強化經濟社會及民生國安韌性特別預算案立法院審議結果」新聞稿，含114-116年度分配金額、審議減列53億元明細。 | 同上 |
| `fy115-bianlie-qingxing-dgbas.html` | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=235226 | 2026-08-17 | 主計總處「115年度中央政府總預算案編列情形」新聞稿（行政院提出數，尚未經立法院審議），含歲入歲出總額、政事別分配、債務、GDP占比等完整數字。 | 同上 |

## 未能第一手核實、僅存於 JSON notes 供查證的項目

以下項目因 40 次 WebSearch/WebFetch 配額用盡，僅取得 WebSearch 摘要或新聞交叉校對，**未直接開啟原始 PDF/新聞稿逐字核對**，已在 `extracted/totals-and-functions.json` 對應欄位標註來源與查證建議：

- 114年度原始（提出數）歲入歲出金額（僅WebSearch摘要）
- 115年度立法院審議後歲入數字（中央社數字異常，已捨棄不採信，留null）
- 前瞻基礎建設計畫各期金額（兩組矛盾數字，均未第一手核實）
- 新式戰機採購特別預算、海空戰力提升計畫採購特別預算 金額（僅WebSearch摘要，指向立法院審查報告PDF但未開啟）
- 嚴重特殊傳染性肺炎防治及紓困振興特別預算 各次追加金額（僅WebSearch摘要，4次加總與840,0億上限有落差）
- 丹娜絲颱風及七二八豪雨災後復原重建特別預算、花蓮馬太鞍溪堰塞湖災後重建特別預算 金額（完全未查得，僅知其存在）
- 107、109年度以外的部分年度政事別決算數執行細節（審計部原始總決算審核報告本身未開啟，改用主計總處總說明PDF內引註的決算審定數）
