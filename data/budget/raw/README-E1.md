# 中央政府總預算 歲出機關別預算 — 原始檔案清單（E1：機關別十年資料）

本清單只記錄本任務（機關別預算逐年抓取）下載的檔案。若目錄下出現其他檔名（如
`fy_debt-timeseries-nta.csv`、`fy108-zhengshibie-table-mof.pdf`、
`fy114-zongshuoming-dgbas.pdf`、`fy115-zongshuoming-dgbas.pdf`），那是同一資料頁面
下其他子任務（負債時間序列／政事別／總說明）抓的材料，不在本清單記錄範圍內，抓取當下
本目錄即已存在，未予異動。

所有抓取方式皆為 `curl -L`（xls/xlsx 直接下載）；抓取日期：2026-08-17。

| 檔名 | 來源 URL | 下載日期 | 內容 | 抓取方式 |
|---|---|---|---|---|
| `fy105-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/105/105ctab/105c歲出機關別預算總表.xls | 2026-08-17 | 105年度中央政府總預算（法定）歲出機關別預算總表，主管別彙總（經常門＋資本門），29 個主管別列項 | curl |
| `fy106-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/106/106ctab/106c歲出機關別預算總表.xls | 2026-08-17 | 106年度法定預算，同上結構 | curl |
| `fy107-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/107/107ctab/107c歲出機關別預算總表.xls | 2026-08-17 | 107年度法定預算，同上結構（蒙藏委員會裁撤後首年） | curl |
| `fy108-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/108/108ctab/108c歲出機關別預算總表.xls | 2026-08-17 | 108年度法定預算，海岸巡防署改制海洋委員會首年 | curl |
| `fy109-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/109/109ctab/109c歲出機關別預算總表.xls | 2026-08-17 | 109年度法定預算 | curl |
| `fy110-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/110/110ctab/110c歲出機關別預算總表.xls | 2026-08-17 | 110年度法定預算 | curl |
| `fy111-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/111/111ctab/111c歲出機關別預算總表.xls | 2026-08-17 | 111年度法定預算 | curl |
| `fy112-歲出機關別預算總表-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/112/112ctab/112c歲出機關別預算總表.xls | 2026-08-17 | 112年度法定預算，數位發展部＋國家科學及技術委員會（原科技部）首年 | curl |
| `fy113-歲出機關別預算總表-dgbas.xlsx` | https://ws.dgbas.gov.tw/001/Upload/461/relfile/11333/232850/C歲出機關別預算總表.xlsx | 2026-08-17 | 113年度法定預算，農業部／環境部改制首年（頁面：https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=232850 ，標題「113年度中央政府總預算」不含案字） | curl |
| `fy114-歲出機關別預算總表-dgbas.xlsx` | https://ws.dgbas.gov.tw/001/Upload/461/relfile/11333/234914/C歲出機關別預算總表.xlsx | 2026-08-17 | 114年度法定預算（立法院2025-01-21三讀通過原始法定預算，不含同年8/29追加預算案）（頁面：https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=234914） | curl |
| `fy115-歲出機關別預算總表-proposed-dgbas.xlsx` | https://ws.dgbas.gov.tw/001/Upload/461/relfile/11333/235176/b歲出機關別預算總表.xlsx | 2026-08-17 | 115年度中央政府總預算**案**（行政院2025-08-21提出，尚未經三讀修正之提案數）。立法院已於2026-08-14三讀通過並刪減480億元，但主計總處截至抓取當下（2026-08-17）尚未上架三讀後的法定機關別表，故本檔僅能作為 proposed 版本使用，見 `extracted/agency-by-year.json` notes | curl |
| `fy105-歲出機關別預算表-detail-dgbas.xls` | https://ws.dgbas.gov.tw/public/data/dgbas01/105/105ctab/105c歲出機關別預算表.xls | 2026-08-17 | 105年度歲出機關別預算表（單位預算逐款明細，非彙總總表），僅用於交叉核對「行政院主管」彙總數內含哪些次級機關（國發會／陸委會／原民會／客委會／主計總處／人事總處／故宮／公平會／NCC／中選會／國史館），供 `agency-by-year.json` notes 引用，非時間序列資料 | curl |

## 資料頁面對照（供追溯，非檔案本身）

| 年度 | 頁面標題 | 頁面 URL | 法定/提案 |
|---|---|---|---|
| 105 | 105年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=103682 | 法定 |
| 106 | 106年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=103716 | 法定 |
| 107 | 107年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=103752 | 法定 |
| 108 | 108年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=104361 | 法定 |
| 109 | 109年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=104329 | 法定 |
| 110 | 110年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=103854 | 法定 |
| 111 | 111年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=200358 | 法定 |
| 112 | 112年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=230689 | 法定 |
| 113 | 113年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=232850 | 法定 |
| 114 | 114年度中央政府總預算 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=234914 | 法定 |
| 115 | 115年度中央政府總預算案 | https://www.dgbas.gov.tw/News_Content.aspx?n=3625&s=235176 | 提案（尚無法定版頁面） |

判斷「法定」依據：頁面標題不含「案」字，且檔名前綴為 `C`（歷史上 `C`=法定預算、`B`=預算案，見 83-91 年度舊版命名 `83C14F.HTM` vs `83B41402.HTM`）；105-112 年度舊制路徑則是 `dgbas01/{yr}/{yr}ctab/{yr}c...`（`ctab`=法定，對照 `Btab`=提案）。
