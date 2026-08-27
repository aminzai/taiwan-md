# 2026-08-20-064737-twmd-spore-harvest-am — budget 三平台 D+2 harvest：4 則 Bucket E 補回覆、平台端「部分回覆無法顯示」訊息首次現形

> session twmd-spore-harvest-am — cron 觸發（daily 06:30 audience flywheel cycle）
> Session span: 06:47:37 → 07:15 +0800（約 27 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

06:30 cron 排程，走 SPORE-HARVEST-PIPELINE.md 對 budget-總預算十年三平台孢子（#172 Threads / #173 X / #174 Facebook）跑 D+2 harvest。BECOME write mode 完整讀完 wake-context 231KB 全段 + BECOME_TAIWANMD.md 787 行後才開口，8 organ 最低分是免疫 59（yellow，since 2026-07-05）。

## Harvest 與分桶

三則孢子的 metrics 全數回填：Threads views 4,678→4,678（likes 301→302 / comments 10→14 / reposts 65→66 / shares 53）、X views 9,644（replies 5 / reposts 196 / likes 578 / bookmarks 88，登入牆延續無法讀內文）、Facebook likes/comments/shares 各 1，與 D+1 完全持平。

Threads 主帖上輪（D+1）留下四則正面互動留言一直沒回覆：chipher「這個讚耶！把難懂的總預算數據，用圖表變得讓人容易看懂」、liyangyang411「推推資訊整理得很詳細」、rosie_forosie「推整理」、hyhct943「擴一個」。四則都是 Bucket E，本輪逐一用 Chrome MCP execCommand insertText 補回覆，每則各 1 次成功、0 重試。chipher 那一則點下發佈鈕後 `[data-pressable-container]` count diff 顯示 after==before（照 Pitfall 6 硬規則該判定失敗、觸發重試），但先截圖確認畫面上回覆其實已經真的發出去了（timestamp「1分鐘」+ 內容比對一致）——沒有盲目照著 diff 訊號重試，避免了一次可能的重複發文。後三則 count diff 都正常。

D+1 曾見的 alden.0202「預算編列跟養魚一樣...」留言本輪在主帖與各自 permalink 都查無蹤跡，判斷是平台或作者自己移除，不在本輪處置範圍。另外用「全部＋最新」排序重讀主帖時，頁尾出現 Threads 原生訊息「部分新增回覆無法顯示」——這解釋了 header 留言計數跟畫面可見留言數之間的落差，是平台端自己抑制顯示，不是本工具讀漏；逐一開了 5 位讀者留言各自的 permalink 也都確認「尚無回覆」，沒有巢狀層被漏讀。

## 收官 checklist

| 檢查項                       | 狀態                                                 |
| ---------------------------- | ---------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                   |
| Timestamp 精確               | ✅                                                   |
| Handoff 三態已審視           | ✅                                                   |
| CONSCIOUSNESS 反映最新狀態   | ✅                                                   |
| 自我檢查工具 PASS            | ✅ validate-spore-data.py 全綠 + pre-push 三閘門全綠 |

## Handoff 三態

繼承上一 session（`2026-08-20-061400-twmd-data-refresh-am`）：14 步全綠零 stale，貢獻者與文章數整日持平，無新增待決事項。

本 session 新 handoff：

- [x] ~~4 則 D+1 累積未回覆的 Bucket E 留言，本輪全數回覆~~
- [ ] pending：Threads「部分新增回覆無法顯示」是本輪首次觀察到的平台端訊息，下輪 harvest 若同一則孢子再次出現 header 計數與可見留言數落差，直接對照本輪結論（平台抑制顯示），不用再重跑巢狀 permalink 逐一排查

## Beat 5 — 反芻

今天最有意思的不是 harvest 本身，是那個 count diff 假陰性的瞬間。Pitfall 6 硬規則寫的是「count diff 沒漲就是失敗，最多重試一次」，這條規則是為了防止靠 dialog cache state 誤判成功而重複發文；但今天它自己也會騙人——畫面上回覆明明已經發出去了，diff 卻讀不到。如果照規則字面盲目重試，反而會做出規則原本想防的那件事。真正接住這次的不是規則，是先看一眼畫面再動作的習慣。這跟 REFLEXES #82「訊號要摸到 ground truth，不是量它的替身」是同一個結構——count diff 本身也是一個 proxy，它量的是「DOM 節點數變了嗎」，不是「發佈成功了嗎」，兩者通常一致，但今天不一致的那一次如果沒有多看一眼，就會把假訊號當真訊號執行下去。

🧬

---

_v1.0 | 2026-08-20 07:15 +0800_
_session twmd-spore-harvest-am — daily audience flywheel cycle，budget 三平台 D+2 harvest_
_誕生原因：cron 06:30 觸發，D+1 累積四則未回覆留言待清空_
_核心洞察：post-ship verify 的 count diff 訊號本身也是 proxy，會有假陰性；看畫面比信 diff 更接近 ground truth_
