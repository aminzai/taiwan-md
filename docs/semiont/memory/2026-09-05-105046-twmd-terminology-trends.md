# 2026-09-05-105046-twmd-terminology-trends — demand-rank 解析器修復 / 10 詞入庫含 3 條誤判翻案 / 查重防線延伸進既有條目的敘述文字

> session twmd-terminology-trends — cron routine（月度用語趨勢觀察，第三輪常規）
> Session span: 10:15:00 → 10:51:00 +0800（約 36 分鐘，2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=write / 8 organ 最低=🛡️ immune 59（黃燈，漂移中，非本輪範圍）/ Q14=PASS

## 觸發

`twmd-terminology-trends-monthly` 每月 5 日 10:30 例行觸發，走 TERMINOLOGY-TRENDS-PIPELINE.md
7 stage：SC 需求缺口排序 → 多切面搜索 → 雙防線查重 → 高信心入庫 → 月度趨勢報告。

## Stage 1 就先撞到工具自己的 bug

跑 `terminology-demand-rank.py --days 28` 第一步就 crash：`AttributeError: 'dict' object has
no attribute 'strip'`。追下去是這支腳本自帶的簡化版 YAML 解析器不認得 `notes: |` 這種區塊純量——
[副詞](../副詞.yaml)、[粉絲](../粉絲.yaml)、[無語](../無語.yaml) 三個既有詞條的 notes 內文都貼了
issue 連結，`https://github.com/...` 裡的冒號被解析器當成續行的巢狀 key，notes 從字串變成 dict。
修法是讓解析器認得 block scalar 的縮排邊界，續行內容不再逐行當 key-value 解析
（`73dba45f2`）。修完重跑，249 個中國詞查詢、15,153 曝光、MISSING 47／MAPPING 33 正常輸出。

## Stage 2-4：搜索、查證、入庫

6 個切面搜索（Threads 支語現場／PTT 近月新串／中國年度流行語榜單／誤判鑑定案例／SC 需求詞源
逐一查證／上輪追蹤詞回查）後入庫 10 條，最有價值的是 3 條誤判翻案：「確實」台語辭典本來就有、
「痛點」源自英文 Pain Point 直譯跟中國無關、「串流」根本查反了方向——中國說「流媒體」，
「串流」才是台灣自己的用詞。另外收了 4 條真實分歧（攢錢／帶貨／數位游民／娛樂圈）、2 條新興
觀察詞（不配得感／賽博對賬，後者跟上輪的活人感／預制感同屬 2025《咬文嚼字》十大流行語）、
1 條爭議未定（治癒，兩邊說法都有道理，不下判定）。完整報告在
[reports/terminology-trends/2026-09.md](../../../reports/terminology-trends/2026-09.md)（`932696457`）。

雙防線查重這輪多了一層發現：有 6 個候選查完才發現「早就有」，但資訊住在既有條目的 `etymology`
敘述文字裡而不是 `display.china` 欄位值——像「下午好」被 [早安.yaml](../../../data/terminology/早安.yaml)
的 china_path 一句話帶過、「避雷」被 [踩雷.yaml](../../../data/terminology/踩雷.yaml) 記成同一組平行
發展詞族。單純比對欄位值抓不到，這輪把查重範圍延伸到連既有條目的敘述文字都掃過一輪才攔下。

## QA 四件套

全庫 2,419 檔 yaml parse 0 失敗；`terminology-charcheck.js` 台灣欄簡體外洩 0；
`terminology-yaml-dedup.py` 掃到既有 8 組跨來源重複（互動/交互、伺服器/服務器等 2026-03-30
匯入時就存在的舊資料，跟本輪新增的 10 條無關，未新增重複）；`extract-china-terms.py` 重生偵測
26A+5B、16 fps 不變（本輪 0 條新增 detection 規則，10 條全是會製造假陽性的標準中文詞，維持
保守 opt-in）。

## 收官 checklist

| 檢查項                       | 狀態                        |
| ---------------------------- | --------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                          |
| Timestamp 精確               | ✅                          |
| Handoff 三態已審視           | ✅（無新增 blocker，見下）  |
| CONSCIOUSNESS 反映最新狀態   | ✅（本輪未觸及 organ 分數） |
| 自我檢查工具 PASS            | ✅ QA 四件套全綠            |

## Handoff 三態

繼承（跟本 routine 相關的部分，其餘沿用 twmd-maintainer-am 09:01 handoff）：

- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤（本 session 未動，非本 routine 範圍）

本 session 新增：

- [ ] pending（下輪）— 「底層 vs 基層」頻率位移，本輪證據不足未入庫，@thiankiu.to 已點出方向，
      下輪可鎖定「基層員工」「基層民眾」等具體搭配詞驗證
- [ ] pending（下輪）— demand-rank 的 MISSING 清單本輪近三分之二是語意雜訊（「這」「什麼」
      「氛圍」之類），可評估要不要加泛用詞黑名單預過濾；>1 file 工具改動，先記候選不自主施作
- [ ] pending（下輪）— 邪修／漂亮飯／薅羊毛 收編進度純關鍵字搜索已經拿不到新訊號，需要更聚焦
      的定量方法（站內查詢量或固定帳號觀察）才追得動

## Beat 5 — 反芻

這輪三個誤判翻案（確實／痛點／串流）有個共同結構：讀者查證的方向都是「這是不是支語」，
但答案都指向反方向——串流甚至直接查反，中國自己說的是「流媒體」。三次獨立命中同一種偏誤，
值得留意「支語」判準本身帶有一種預設方向性：看到兩岸都在用的詞，直覺先問「這是不是中國傳來
的」，卻很少反過來問「這會不會是台灣傳過去的、或本來就各自平行發展的」。踩雷／奧步／窩心／
水準／素質／確實／痛點／串流，累積到第八個誤判翻案案例，這條偏誤本身可能夠格寫進 LESSONS-INBOX
了，留給下次 distill 判斷是否升 canonical。

🧬

---

_v1.0 | 2026-09-05 10:51 +0800_
_session twmd-terminology-trends — 月度用語趨勢觀察第三輪常規_
_誕生原因：cron `twmd-terminology-trends-monthly` 每月 5 日 10:30 例行觸發_
_核心洞察：(1) 排序工具自己的簡化 YAML 解析器不認得區塊純量，续行裡的 URL 冒號會誤判成巢狀 key
(2) 誤判翻案案例在查證方向上有系統性偏誤，八個案例全部都是「以為是支語結果查反」而非「以為
不是支語結果真的是」(3) 查重防線要抓的不只是欄位值重複，還有資訊藏在既有條目敘述文字裡的隱性重複_
_LESSONS-INBOX 候選：支語誤判方向性偏誤（累積 8 例：踩雷／奧步／窩心／水準／素質／確實／痛點／串流，
全部方向都是「以為是支語，查證後發現不是或方向相反」，尚未出現反向案例，值得記錄這個不對稱性）_
