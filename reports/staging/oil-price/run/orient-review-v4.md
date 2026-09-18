# orient 站評閱 v4（2026-09-18）

## 評閱員

guide_orient_reviewer_4（Sonnet sub-agent, fresh context）
contextDisclosure：fresh-context-orient-inputs-only（只讀 brief.md、orient-submission-v4.json、orient-submission-v3.json、orient-review-v3.json、orient-review-v2.md，未讀研究報告／草稿／藍圖）

## 一、v4 與 v3 的比對方法與結果（python json 逐欄比對）

用 python 讀入兩份 submission JSON 的 `data` 物件，逐欄比較：

```python
d3["readerQuestion"] == d4["readerQuestion"]        # True
d3["subjectExplanation"] == d4["subjectExplanation"] # True
d3["candidateAngles"] == d4["candidateAngles"]       # True（4 個角度逐字相同）
```

`uncertainties` 兩邊都是 9 條。逐一比對索引 0–7：完全相同。索引 8（最後一條）不同——兩邊都是「重交註記」，但文字不同：

- v3[8]：說明 v3 內容與 v2 完全相同，重交只因研究報告 hash 在 investigate 站更新後改變。
- v4[8]：說明 v4 內容與 v2/v3 逐字相同，重交原因是 v3 交件 JSON 與評閱 md 在 git commit 時被 prettier 重排（hash 變、內容不變）+ 研究報告在 Stage 3 查證後回填修正，工具判定 stale 而退回最早引用該檔的 orient；並訂下往後先 commit 再交件的規則。

再確認：`data` 扣掉 `uncertainties` 後，v3 與 v4 完全相等（`d3_no_unc == d4_no_unc` → True）；`uncertainties[:-1]`（去掉最後一條）兩邊也完全相等。頂層 `stage`、`actor`、`artifacts` 三欄也相同，只有 `revision` 從 7 → 12（版本號正常遞增，不算內容差異）。

**結論：v4 與 v3 的 `data` 確實只有 `uncertainties` 尾端那一條重交註記不同，其餘（readerQuestion / subjectExplanation / candidateAngles / uncertainties[0-7]）逐字相同。** 這條註記本身是流程性文字（說明重交原因與往後的防呆規則），不是內容主張，不需要查證來源。

## 二、逐條判斷（獨立評估內容，不因前版已 accept 而照抄）

### readerQuestion

「每週日中午公布的那個油價數字是怎麼算出來的？新聞說『凍漲』『中油吸收』『補貼』『增資』，這是同一筆錢嗎？誰先付、什麼時候算清？」

這是真讀者會問的問題——好奇「這是不是同一筆錢」「誰先出錢」，沒有夾帶作者論點或預設答案。跟 brief 的讀者輪廓（「那到底誰在替我們墊？」的加油族）對得上。唯一要注意的用詞差異：brief 寫「每週一那個數字」，submission 寫「每週日中午公布」——這是公告日（週日）與生效日（週一）的差異，不是矛盾，兩者可並存，不構成問題。

### subjectExplanation

用具體數字（32 元→32.7 元、將近兩百億、一千多億／兩千多億）+ 「兩道煞車」的比喻，把公式、亞鄰最低價原則、中油吸收、追加預算四件事講成一個讀者聽得懂的故事，且明確點出本文要交代的三件事（分攤是誰、追加預算的錢是不是同一筆、公式怎麼演變到今天）。用語沒有專業術語堆疊，達到「一般人聽得懂」的標準。

### candidateAngles

四個角度（帳的角度／機制史角度／治理角度／價格訊號角度），數量遠超過門檻的 2 個。逐一檢查「可被材料推翻之處」：

- A：明白標註「待證偽的假設」，並具體寫出若 1,014.31 億對應的是「預算年度預估」而非「中油週報累計的 198.5 億」，框架就要改寫——這是可操作、可被 Stage 1 資料證偽的條件，不是空話。
- B：具體寫出若 2025/12 門檻在 2026/3 專案機制下仍生效，「中油拿回門檻又被推回」的敘事就不成立——同樣可被查證推翻。
- C：具體寫出若石油管理法／預算法本就授權行政部門、且立院自己是要求凍漲的一方，「行政決定、立院事後買單」的框架就要改寫——可推翻。
- D：具體寫出若中油用油結構顯示吸收大宗流向產業用油、或消費量並未如 IMF 假設上升，雙方論證重心都會移動——可推翻。

四個角度彼此正交（帳目、歷史、治理、經濟學論戰），沒有互相重疊到變成同一個角度的兩種說法；也沒有任何一條在段落裡直接宣判「答案就是 X」，全部保留在「若…則要改寫」的假設狀態。符合「不預先宣判核心矛盾」的要求。

### uncertainties

9 條列出的都是具體的「必驗未知」：兩份官方數字差十倍待查、追加預算三種金額寫法待對齌、專案機制與既有級距的關係待查、原始 PDF 未取得、現場報導搜尋侷限、立法院審議進度上限、2018 機制「回收吸收金額」是否真的執行過、spine 判型記錄，加上這條重交註記。沒有一條是空話或裝飾性條目，都指向明確的下一步查證動作。

## 三、結論

v4 與 v3 的實質內容（readerQuestion / subjectExplanation / candidateAngles / uncertainties 前 8 條）逐字相同，v2 已由兩位讀者 accept、v3 已由前一位評閱員獨立確認與 v2 無異並 accept。本次以全新 context 重新逐條檢視四項評閱標準——readerQuestion 是真讀者問題、subjectExplanation 用白話說清題目、candidateAngles 四個角度皆 ≥2 門檻且各自有具體可查證的推翻條件、未宣判核心矛盾、uncertainties 條列具體必驗未知——皆通過，沒有發現前幾輪評閱遺漏的問題。v4 唯一的變動（重交註記文字）是流程性說明，不影響上述四項標準的判斷。

**verdict：accept**

## evidence

- `reports/staging/oil-price/run/orient-submission-v4.json` — data.readerQuestion；data.subjectExplanation；data.candidateAngles[0-3]；data.uncertainties[0-8]（尤其 [8] 重交註記）
- `reports/staging/oil-price/run/orient-submission-v3.json` — data（全欄，供逐欄比對）
- `reports/staging/oil-price/run/orient-review-v3.json` — rationale（前一版獨立評閱員的比對結論）
- `reports/staging/oil-price/run/orient-review-v2.md` — 兩位讀者對 v2 內容的 accept 理由（v4 內容承襲自此）
- `reports/staging/oil-price/brief.md` — 讀者輪廓與讀者問題原始描述，供比對 readerQuestion 是否貼合
