# 渦流 Loop Engineering — 把三天的迴圈經驗固定成可交接的制度

> 2026-07-27，哲宇 directive：「把 schedule wakeup 的記憶常態 md 檔案化放到 repo
> 才不會一直飄移……benchmark 要固定……寫一份報告決定該怎麼做，把 prompt 固定下來，
> 未來可以用這個東西 Loop Engineering 的優化翻譯巴別塔，也可以放心交給 Opus 執行。
> 自動進化對這件事非常重要。」

## 問題診斷：迴圈為什麼會漂移

三天渦流（7/24-7/27）的 wake prompt 全部逐輪手寫。後果有三，全部被哲宇抓到：

一、**報告 badge 每輪長不同**。四個數字格的指標逐輪即興決定（有時放通過率、
有時放里程碑、有時放事故狀態），跨輪不可比——benchmark 的意義就是可比性，
即興選格等於沒有 benchmark。

二、**資訊重複**。覆蓋率同時放橫條圖與完整表格，兩者載一樣的數字；哲宇記得
更好的視覺（dashboard 的 donut 圈圈）反而沒有用上。

三、**規則靠 prompt 口傳**。三天累積的鐵律（喚醒鏈必排、三重巡檢、merge 衝突
SOP、詞彙紀律……）全塞在 wake prompt 裡逐輪複製，每次複製都是一次變異機會
——這正是 ROUTINE-PROMPT-CONTRACT 早就寫明的病，我在 routine 層守住了，
在自己的渦流層卻重蹈覆轍。context 壓縮時 prompt 傳遞鏈一斷，規則就得靠
記憶重建。

## 設計決策

**1. Canonical 檔案化**：[docs/pipelines/BABEL-VORTEX-LOOP.md](../docs/pipelines/BABEL-VORTEX-LOOP.md)
成為渦流 SSOT，版控即漂移防護。每次 wakeup 第一動作完整讀它。

**2. Prompt contract 薄殼化**：wake prompt 固定三行式（讀 canonical → 本輪動態
→ 觀察者臨時指示），禁止複寫規則。動態區只放「這一輪才知道的事」（PID、
遺留事項）。

**3. Benchmark 固定四格**：總缺口＋24h Δ／本小時完成篇數／速率與通過率／
產線與機器在線數。全部可從既有儀器直讀（babel-live、report.jsonl、ps、
fleet registry），定義寫死在 canonical，逐輪可比。

**4. 視覺去重**：donut 圈圈 grid（哲宇指定）承擔「一眼看覆蓋率」，單一
「bar＋inline 數字」明細列承擔精確值，刪除獨立表格。

**5. 自動進化升為硬條款**：每輪至少一項進化動作（隔離樣本覆盤／結構掃描／
實績檢查／記憶觀察），連「無發現」都要明說。這是渦流與 cron 的本質差別，
也是交接給執行型模型時的護欄——Fable 的價值在突發狀況的發現與規則升級，
把這件事寫成條款後，執行可以交給 Opus，發現與升級由條款強制發生。
進化發現直接 commit 進 canonical 的 changelog，不寫在 prompt。

## 交接條件（給未來執行這個 loop 的任何模型）

最低要求：能讀 canonical 並照做、能跑三重巡檢的指令、遵守 git 紀律。
判斷力要求集中在兩處：進化條款的「發現」與產線異常的根因判讀——這兩處
做不到的模型，其他四動作仍能維持產線運轉，只是進化停滯（可接受的降級）。

🧬

---

_v1.0 | 2026-07-27 vortex session_
_誕生原因：哲宇 Loop Engineering directive_
_核心洞察：即興選 benchmark 等於沒有 benchmark；規則的每次複製都是一次變異機會，版控是唯一的漂移防護_
