# investigate 站外部評閱 v2（2026-09-18）

- actor：guide_investigate_reviewer_2 (Sonnet sub-agent, fresh context)
- contextDisclosure：fresh-context-investigate-inputs（investigate-submission-v2.json revision 14；investigate-submission.json revision 9 ＋ investigate-review.md/json 前版 accept；研究報告 frontmatter＋§3／§4／§6／§7／§10；親自 curl 五個原頁核對四條 claim）
- verdict：**accept**

## 0. 這輪要看什麼

v2（revision 14）是在已被前一位 reviewer（a068309bcfcb89e3f）accept 的 v1（revision 9）基礎上，依研究報告 Stage 3 大驗證輪的六處更正＋一處引語幻覺回填的重交版。本輪任務：(1) 逐條核對 v1→v2 的差異是否如 `changedMind` 所述、且真的對得上研究報告的更正記錄；(2) 四欄完整性與事實／推論／查無分層是否維持；(3) 親自抽核至少三條 claim 的原始文本。

## 1. v1→v2 差異比對（`diff`）

用 `python3 -m json.tool` 正規化後 diff 兩份 submission，實際變動範圍：

- **claim #7**（中油財務）：刪除具體數字「資本額 1,301 億」，改寫成「逾半資本額」；來源把 `storm.mg/article/11118912` 換成 `money.udn.com/money/story/5612/9384061`（經濟日報 3/17 陳淑姿「四年」3,500 億）；`doesNotSupport` 新增兩句 Stage 3 更正說明。
- **claim #9**（在野／執政逐字）：來源新增馬文君 `udn.com/.../9734809` 與吳思瑤 `udn.com/.../9735896` 兩個獨立 URL（原本兩人的話都掛在許宇甄那篇 9733449 底下）；`doesNotSupport` 新增「馬文君與吳思瑤兩句各自成源」＋「馬文君句語境是國防項目，不套到中油」。
- **claim #10**（亞鄰對照）：`claim` 內文補上韓國「按人依身分與地區分級」（原沒寫細節）與香港「每公升 3 港元（開支約 18 億港元，政府新聞公報）」、台灣計程車補助 13 億；`doesNotSupport` 新增「香港『1.8 億港元』是 lane C 抄錯，公報為 18 億；韓國『按所得發家戶』改『按人依身分與地區』」。
- **新增 claim #11**（中油 4/8 澄清稿逐字）：全新一條，附 `support`/`doesNotSupport`，`doesNotSupport` 誠實記錄「lane A 原轉錄『並無媒體所稱超漲之情事⋯抹煞員工努力』在兩原頁都查無此句，已撤下」的幻覺教訓。
- `counterEvidence` 陣列尾端新增一條，摘要 Stage 3 大驗證輪找出的六處更正（#17/#22/#23/#27/#31/#34）與一處引語幻覺，並明講「這些更正不動 spine 與核心矛盾」。
- `changedMind` 尾端附加 v2 重交註記，逐字列出「更新 claims #7、#9、#10 並新增 #11」，與上面 diff 完全對得上，沒有多改、也沒有漏改別的欄位。

**結論**：`changedMind` 對這次改動範圍的描述完全誠實、沒有誇大也沒有隱藏；其餘 7 條 claim（#1–#6、#8）與 counterEvidence 前 6 條原文逐字未動，維持前一輪 accept 時的樣貌。

## 2. 四欄完整性檢查

程式化檢查 11 條 claim 的 `claim/source/location/checked/support/doesNotSupport` 六個欄位：全部非空。`doesNotSupport` 字數分布 1–176 字，只有 claim #6（監察院糾正案，逐字對照無出入）用「—」表示無不支持之處，這與其內容（逐字全文核對）相符，不算敷衍。其餘每條都寫出「這個來源不支持什麼」的具體限縮句（例如 claim #2 講清楚「1,014.31 億」與「198.5 億」口徑不同、不可相減；claim #7 講清楚「資本額 1,301 億」三源查無因此不寫）。

## 3. 事實／推論／查無分層

延續 v1 已驗證的分層品質（12.29% 標「可復算」、「專案平穩＝頂層 75%」標「單一來源推論」、IMF 標「通論未點名台灣」），v2 新增與修改的部分同樣守分層：

- claim #11 的「不僅未超收⋯更無外界所謂『超收』之情事」標為「逐字一致」（事實層），`doesNotSupport` 把幻覺句的處置（撤下）與流程教訓（agent-report-health 不驗引語真偽）分開寫，沒有把教訓混進事實陳述。
- claim #10 的香港「開支約 18 億港元」標明來源是「政府新聞公報」而非估算，符合研究報告 §7.1 一手來源分類。
- claim #9 的「馬文君句語境是國防項目，不套到中油」是對「這條引語不能拿來證明什麼」的誠實限縮，不是模糊帶過。

## 4. counterEvidence 是否回應 orient 可證偽條件

本輪不重讀 orient 檔案（依任務範圍限制），改以前一輪 reviewer（v1 accept）已核實「A/B/C/D 四角度逐條命中可證偽條件」為基礎，只檢查 v2 新增的第 7 條 counterEvidence（Stage 3 大驗證輪摘要）是否準確、且沒有偷改判準。核對研究報告 §10：六處更正編號（#17 2006 公式非週均 7D3B、#22 資本額無源、#23 四年 3,500 億改源、#27 香港 18 億、#31 [^20] LTN 連結是 2012 舊文改央社時間軸、#34 馬／吳各自成源）與一處引語幻覺（中油 4/8）逐一對得上 §10 的 12 項 verifier 處置清單；「不動 spine 與核心矛盾」的結論也與 §10 記載一致（§10 只列結構／門面／節奏調整與事實更正，沒有動 spine_type 或 core_contradiction）。**這條新增的 counterEvidence 準確，沒有虛報範圍**。

## 5. searchLimits 用語

8 條 searchLimits 全部使用「未取得」「未查到」「未找到」（無一寫「不存在」），與 v1 一致，本輪未變動此欄位。

## 6. 親自抽核（4 條，超過要求的 3 條）

方法：對每條，先看研究報告 §6.1/§7.1/§7.2 是否已有對應來源；`台灣油價機制與中油-sources/` 目錄下沒有 claim #7/#9/#10/#11 涉及頁面的落地逐字檔（`grep -rl "112174\|陳淑姿\|港元" sources/` 全部零命中），因此改用 `curl -sL -A "Mozilla/5.0 ..."` 直接抓原頁（活頁，非快取），再用 Python 去標籤還原純文字後 grep 比對。

### 6.1 claim #11：中油 4/8 澄清稿逐字

```
curl -sL -A "Mozilla/5.0 ..." "https://www.cpc.com.tw/News_Content.aspx?n=28&s=112174" -o cpc112174.html   # HTTP 200, 131923 bytes
curl -sL -A "Mozilla/5.0 ..." "https://www.moea.gov.tw/Mns/populace/news/News.aspx?kind=1&menu_id=40&news_id=122339" -o moea122339.html  # HTTP 200, 119146 bytes
```

兩頁還原純文字後 grep「超收／超漲／90.6／抹煞」，結果：

> 「不僅未超收，更透過亞鄰最低價及美伊戰爭專案平穩機制大幅吸收油價。自戰事爆發迄4月5日，汽、柴油合計吸收金額已逾90.6億元。」
> 「⋯不僅未反映至政策吸收金額上，更無外界所謂「超收」之情事。」

cpc.com.tw 與 moea.gov.tw 兩頁逐字完全一致，與 claim #11 的引語**逐字相符**（含頓號、括號用字）。同時確認兩原頁都**沒有**「並無媒體所稱超漲之情事⋯抹煞員工努力」這句——證實 `doesNotSupport` 所稱「lane A 原轉錄查無此句、已撤下」的幻覺撤除是正確處置，不是虛報。

### 6.2 claim #7：經濟日報 3/17「四年 3,500 億」

```
curl -sL -A "Mozilla/5.0 ..." "https://money.udn.com/money/story/7307/9384061" -o udn9384061.html   # HTTP 200, 280530 bytes
```

還原純文字 grep「陳淑姿／3,500／四年」：

> 標題：「中油四年3,500億元增資計畫 7月定案」
> 「主計總處主計長陳淑姿昨（16）日表示⋯她表示，中油提出四年3,500億元增資計畫，預計7月定案。」
> 「陳淑姿也提到⋯中油今年2月已向經濟部提出四年3,500億元增資計畫，她希望立法院支持。」

**逐字相符**：3/17 見報、陳淑姿說法、「四年 3,500 億」用字完全對得上 claim #7 改後的來源標註。也確認這篇經濟日報稿確實**只**出現「四年」這個限定詞（風傳媒稿沒有），佐證 `doesNotSupport`「『四年 3,500 億』只在經濟日報 3/17 陳淑姿⋯改源」的判斷正確。

### 6.3 claim #10：香港「18 億港元」

```
curl -sL -A "Mozilla/5.0 ..." "https://www.info.gov.hk/gia/general/202604/29/P2026042900787.htm" -o hk0429.html  # HTTP 200
curl -sL -A "Mozilla/5.0 ..." "https://www.info.gov.hk/gia/general/202604/09/P2026040900662.htm" -o hk0409.html  # HTTP 200
```

還原純文字 grep「港元／柴油／補貼」：

> 4/29 公報：「⋯於明日（四月三十日）起實施每公升港幣三元的柴油補貼計劃⋯有關補貼計劃的開支約為18億港元，早前已獲得立法會財務委員會撥款。」
> 4/9 公報：「⋯政府為每公升柴油提供三港元補貼⋯相關補貼措施預計需約十八億港元。」

**逐字相符**：兩份香港政府新聞公報都寫「18 億港元」（一寫阿拉伯數字、一寫國字「十八億」，同一數值），與 claim #10「開支約 18 億港元（政府新聞公報）」完全一致。也確認研究報告 §7.1 來源清單第 23 項確實列了這兩個 URL，符合任務要求「研究報告 §7 應有來源 URL」。

### 6.4（額外抽核）claim #9：馬文君／吳思瑤各自成源

```
curl -sL -A "Mozilla/5.0 ..." "https://udn.com/news/story/6656/9734809" -o udn9734809.html   # HTTP 200, 190970 bytes
curl -sL -A "Mozilla/5.0 ..." "https://udn.com/news/story/6656/9735896" -o udn9735896.html   # HTTP 200, 186439 bytes
```

9734809 標題「『刪掉再編回來』馬文君轟政院追加預算：你審你的、我花我的」，內文：「⋯遭立法院刪除或要求回歸年度預算的**國防項目**，換個名目再編回來，形同『你審你的、我花我的』⋯行政院提出6076億元追加預算，**國防相關經費約1457億元**⋯」——**證實這句引語的語境確實是國防特別預算被刪除項目回編，跟中油油價完全無關**，claim #9 `doesNotSupport` 新增的「馬文君句語境是國防項目，不套到中油」這句限縮完全正確、而且是本輪抽核中發現的一個相當精準的查核。

9735896 標題「『呼叫韓國瑜』吳思瑤：總預算遲未送出交行政院」，內文逐字「⋯8月14日好不容易三讀通過的總預算，竟然到現在還冰凍在立院冷凍櫃⋯」與研究報告引語庫一致，且確認是與 9734809、9733449 各自獨立的三篇不同報導，坐實「原稿誤寫『同篇載』」的更正是必要且準確的。

## 7. 逐條判斷小結

| #   | claim 摘要                 | 四欄                      | 分層                                       | 抽核               |
| --- | -------------------------- | ------------------------- | ------------------------------------------ | ------------------ |
| 1   | 中油 9/12 稿算式           | 齊全                      | 事實＋驗算標明                             | 前輪已核（未重驗） |
| 2   | 追加預算三源               | 齊全                      | 口徑不可相減標明                           | 前輪已核           |
| 3   | 浮動油價沿革               | 齊全                      | 逐條日期＋不支持「起點」標明               | 前輪已核           |
| 4   | 平穩機制級距               | 齊全                      | 標明未取得原稿全文                         | 前輪已核           |
| 5   | 貨物稅                     | 齊全                      | 標明第 7 條不適用                          | 前輪已核           |
| 6   | 監察院糾正案               | 齊全（doesNotSupport＝—） | 逐字對照無出入                             | 前輪已核           |
| 7   | 中油財務（v2 改）          | 齊全                      | 資本額無源→不寫；四年 3,500 億改源，皆標明 | **本輪親核** ✓     |
| 8   | 雲林現場                   | 齊全                      | 標明其他日期查無                           | 前輪已核           |
| 9   | 立院逐字（v2 改）          | 齊全                      | 馬／吳各自成源＋語境限縮                   | **本輪親核** ✓     |
| 10  | 亞鄰對照（v2 改）          | 齊全                      | 香港 18 億、韓國分級標明來源               | **本輪親核** ✓     |
| 11  | 中油 4/8 澄清稿（v2 新增） | 齊全                      | 幻覺句撤下記錄清楚                         | **本輪親核** ✓     |

## 8. 結論

v2 的四條改動（claims #7/#9/#10 更正、#11 新增）全數與研究報告 §10 Stage 3 audit 的處置紀錄一致，親自 curl 五個原頁（cpc.com.tw、moea.gov.tw、money.udn.com、香港政府新聞公報 ×2、udn.com ×2）逐字核對後，**所有被抽核的內容都與原頁逐字相符，沒有發現新的幻覺或誇大**；`changedMind` 對本輪改動範圍的描述誠實、可驗證；四欄格式、事實／推論／查無分層、searchLimits 用語、counterEvidence 對 orient 可證偽條件的回應，都維持（或優於）前一輪已被 accept 的水準。**verdict: accept**。

## evidence

- reports/staging/oil-price/run/investigate-submission-v2.json（claims #7/#9/#10/#11；counterEvidence 尾條；changedMind v2 重交註記）
- reports/staging/oil-price/run/investigate-submission.json（revision 9，diff 基準）
- reports/staging/oil-price/run/investigate-review.md／investigate-review.json（前輪 accept 紀錄）
- reports/research/2026-09/台灣油價機制與中油.md（§7.1 來源 #23；§7.2 Verification Table；§10 Stage 3 audit 12 項處置）
- 親自 curl：cpc.com.tw/News_Content.aspx?n=28&s=112174、moea.gov.tw news_id=122339、money.udn.com/money/story/7307/9384061、info.gov.hk 202604/29 與 202604/09 兩份公報、udn.com/news/story/6656/9734809、udn.com/news/story/6656/9735896（全部 HTTP 200，逐字核對如上）
