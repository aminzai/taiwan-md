# Orient 評閱 v6（guide_orient_reviewer_5 複讀，orient-inputs-reread）

## 0. Python 逐欄比對結果（v6 vs v5）

```
readerQuestion      EQUAL
subjectExplanation  EQUAL
candidateAngles[0]  EQUAL
candidateAngles[1]  EQUAL
candidateAngles[2]  EQUAL
candidateAngles[3]  EQUAL
uncertainties[0]    EQUAL
uncertainties[1]    EQUAL
uncertainties[2]    EQUAL
uncertainties[3]    EQUAL
uncertainties[4]    EQUAL
uncertainties[5]    EQUAL
uncertainties[6]    EQUAL
uncertainties[7]    EQUAL
uncertainties[8]    DIFFERENT（唯一差異）
```

`data` 底下四個欄位鍵值集合相同；除 `uncertainties[8]` 外全部逐字相等。

`uncertainties[8]` 兩版內容：

- v5：「v5 重交註記（revision 25）：orient 內容與 v2–v4 逐字相同。重交原因：冷讀站後研究報告新增 §11（八條查證），工具以 orient v1 曾列研究報告為 artifact 為由要求退回 orient。」
- v6：「v6 重交註記（revision 30）：orient 內容與 v2–v5 逐字相同。重交原因：研究報告 §11 第 3 條依 investigate v3 評閱更正一處數字，工具以 orient v1 曾列研究報告為 artifact 為由要求退回。」

兩者都是**流程性重交說明**（記錄本次退回/重交的觸發原因——這次是研究報告 §11 第 3 條依 investigate v3 評閱更正一處數字），不含任何對油價機制、金額、機制史本身的新主張或修改。確認 v6 在實質內容上與已 accept 的 v5（進而與 v4）完全相同。

## 1. 本輪複讀說明

本輪是同一位評閱員（guide_orient_reviewer_5）對同一份 orient 內容的第二次審查，`contextDisclosure` 如實填 `orient-inputs-reread`（並非全新 context 的 fresh-context-orient-inputs-only）。由於 python 比對已確認 v6 與上一輪已通過的 v5 在 `readerQuestion`／`subjectExplanation`／`candidateAngles`／`uncertainties[0-7]` 逐字相同，唯一變動的 `uncertainties[8]` 是流程記錄而非內容主張，因此上一輪（v5）逐項覆核的四項標準結論在 v6 全部延續有效，重述如下：

### readerQuestion 是否為真讀者問題

問題（「這是不是同一筆錢、誰先付、什麼時候算清」）具體場景化、貼近 brief 描述的讀者，沒有預先包裝答案。**通過。**

### subjectExplanation 是否一般人聽得懂

全程白話（不用「7D3B」「亞鄰最低價原則」等術語），用具體數字（32→32.7 元 vs 半年吸收近兩百億、千億補貼、兩千多億增資）讓讀者感受到「牌價小變動、帳上大金額」的落差，收尾三問對應 candidateAngles 的軸線，未提前給答案。**通過。**

### candidateAngles 是否 ≥2、每個可被推翻、未宣判核心矛盾

四個角度（A 帳的角度／B 機制史／C 誰決定誰監督／D 價格訊號）彼此正交，每個都附上可用 Stage 1 材料直接檢驗的具體推翻條件（如 1,014.31 億對應年度預估價差而非週報累計 198.5 億、2025/12 門檻在專案機制下是否仍實際運作、石油管理法是否本就授權行政部門、中油用油結構是否流向產業柴油），沒有任何一條提前宣判金流形狀或責任歸屬的答案。**通過。**

### uncertainties 是否為具體必驗未知

前八條逐一指向可查證的具體對象（金額十倍差距待驗、三種金額寫法版本分歧、專案機制與既有級距對應關係未定、待補 PDF 材料、現場報導缺口坦承查無不等於沒發生、立法院審議進度確定性邊界、2018 回收條款是否曾執行、spine 型態流程記錄），第九條為本次重交流程記錄，不稀釋前八條密度也非空話充數。**通過（前八條扎實，第九條為流程記錄非內容未知，不構成扣分）。**

## 結論

複讀確認 v6 相對於已通過的 v5，實質內容（readerQuestion／subjectExplanation／candidateAngles／uncertainties[0-7]）逐字未動，唯一變動的重交註記只是記錄「研究報告 §11 第 3 條依 investigate v3 評閱更正一處數字」觸發工具退回，屬流程軌跡而非需要重新查證的內容主張。四項 orient 標準的判斷不因此改變。

**verdict：accept。**
