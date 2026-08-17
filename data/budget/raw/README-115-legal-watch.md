# 115 年度中央政府總預算「法定版」盯盤紀錄

立法院已於 **2026-08-14** 三讀通過 115 年度中央政府總預算案（歲出刪減 480 億元，
歲出總額暫改列 2 兆9,869 億7,437 萬1,000 元；歲入審議後增列 6,019 億9,939 萬元）。
主計總處截至本次查核（**2026-08-17**，即三讀後第 3 天）**尚未上架**下列兩項法定版資料，
故本次任務**未異動**任何 `extracted/*.json`。

## 查過的頁面／URL 與結果

| # | 查詢對象 | URL | 查核方式 | 結果（2026-08-17） |
|---|---|---|---|---|
| 1 | 「中央政府總預算」分類列表（找標題不含「案」字的 115 年度項目） | https://www.dgbas.gov.tw/News.aspx?n=3625 | WebFetch | 115 年度僅有一筆：「115年度中央政府總預算**案**」s=235176（提案版，含案字）。無不含案字的法定版項目 |
| 2 | 同上，帶 sms 參數重複確認 | https://www.dgbas.gov.tw/News.aspx?n=3625&sms=11333 | WebFetch | 同上，列表最上一筆仍是 s=235176 提案版；114/113/112/111/110 年度皆可見「不含案字」法定版項目，唯獨 115 年度缺 |
| 3 | 「政府預算」新聞列表（找「115年度中央政府總預算案立法院審議結果」新聞稿，比照 113 年度 s=232744 的命名慣例） | https://www.dgbas.gov.tw/News.aspx?n=3602 | WebFetch | 列表最新 10 筆（至 115-08-14 為止）皆為經濟成長率／CPI／就業等例行統計新聞稿，**無**總預算審議結果新聞稿 |
| 4 | 同上，帶 sms 參數 | https://www.dgbas.gov.tw/News.aspx?n=3602&sms=11333 | WebFetch | 搜尋結果只返回歷史年度（110/113 年度）審議結果頁與特別預算頁，無 115 年度項目 |
| 5 | 直接試探 s= 編號（114-08-14 當日新聞稿 s=236591 附近） | https://www.dgbas.gov.tw/News_Content.aspx?n=3602&s=236600 | WebFetch | 該 s 編號無效，導回首頁；未指向任何 115 年度審議結果內容 |
| 6 | WebSearch 關鍵字組合（4 次，含 site:dgbas.gov.tw 限定） | 「115年度中央政府總預算 主計總處 法定 三讀」「"115年度中央政府總預算案" 審議結果 site:dgbas.gov.tw」「主計總處 news_content n=3602 115年度中央政府總預算案立法院審議結果」「dgbas.gov.tw 総預算 審議結果 2026-08 news_content n=3602」 | WebSearch | 全部只返回：(a) 提案版頁面 s=235176、(b) 113/111/110 年度的歷史審議結果頁（比對命名慣例用）、(c) 中央社／Yahoo 新聞報導（非主計總處原文，數字與 `totals-and-functions.json` 現有 legal.expenditure 已標記為「不予採信」的來源一致） |

## 目前資料狀態（未異動）

- `data/budget/extracted/agency-by-year.json` 115 年度：`basis=proposed`，維持提案數（3兆349億7,437萬1,000元），notes 已註記與三讀後總額差距 480 億元
- `data/budget/extracted/totals-and-functions.json` 115 年度：`legal.expenditure=2986974371`（千元，2兆9,869億7,437萬1,000元，與中央社 2026-08-14 報導一致，已標記來源為新聞交叉校對非主計總處原文）；`legal.revenue=null`（歲入審議後增列組成未經官方新聞稿逐字核對，故不予填入，維持 null）

## 下次要盯哪裡（按優先序）

1. **`https://www.dgbas.gov.tw/News.aspx?n=3625`**（中央政府總預算列表）— 找標題變成「115年度中央政府總預算」（不含案字）的新項目，出現即代表法定版機關別總表上架。歷史模式（113/114 年度）此頁面通常在立法院三讀後數週內更新，s 編號會落在提案版 235176 之後（114 年度提案 s=233556 → 法定 s=234914，間隔約 1,358；113 年度提案 s=231560 → 法定 s=232850，間隔約 1,290）。
2. **`https://www.dgbas.gov.tw/News.aspx?n=3602`**（政府預算新聞列表）— 找「115年度中央政府總預算案立法院審議結果」新聞稿（比照 113 年度 s=232744 命名），通常會**早於**機關別總表上架，內含歲入審議後數、歲入增列組成、歲出減列 480 億組成的官方逐項數字。
3. 若上述任一項目出現，抓取步驟依 `data/budget/README.md` 第 8 行：
   - 機關別總表：`curl -L -o data/budget/raw/fy115-歲出機關別預算總表-dgbas.xlsx "<新URL>"` → python openpyxl 讀主管別彙總列 → 更新 `agency-by-year.json`（`basis: legal`、`source`、`agencies`，逐機關合計需與官方合計列相符且對齊 2兆9,869億7,437萬1,000元，差 <0.5%）→ 追加一行到 `raw/README-E1.md` → 跑 `python3 scripts/tools/build-ly-budget.py`
   - 審議結果新聞稿：逐字抄歲入審議後數字／組成、歲出減列組成 → 更新 `totals-and-functions.json` 的 `years["115"].legal.revenue` 與 `source`，`notes` 追加說明 → 跑 builder

## 查核紀錄

- 查核日期：2026-08-17
- WebSearch + WebFetch 用量：10 次（15 次上限內）
- 查核者：Taiwan.md 資料取得 sub-agent
