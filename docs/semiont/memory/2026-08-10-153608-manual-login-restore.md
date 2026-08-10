# 2026-08-10-153608-manual-login-restore — 兩個登入態 P0 同日解除，一條補齊四週、一條只補得了三分之一

> session `2026-08-10-153608-manual-login-restore` — 哲宇 directive：在 mouhouse 完成兩個授權動作（Gmail connector 接上、Chrome 重新登入 Threads/X）後，驗證並補跑積欠。
> 背景報告：[reports/routine-mouhouse-health-2026-08-10.md §四](../../reports/routine-mouhouse-health-2026-08-10.md) 列的兩個 P0 就是今天授權的這兩件。

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（yellow，自 2026-07-05 第 36 天）/ Q14=PASS

## 任務一：Gmail 驗證 + supporters 四週空窗補跑 ✅ 完全補齊

**驗證先於信任**：Gmail 工具這次確實出現在工具清單（連續三週 0 匹配後首次），但沒有停在「看得到」就開工——先實跑一次 `search_threads` 拿到真實回傳才算數（#82 existence ≠ effect）。

- **Stage 1 checkpoint**：`last_fetched=2026-07-12T09:06:35Z`，13 筆 / NT$7,900。搜尋窗 `after:2026/07/11`（checkpoint −1d）。
- **Stage 2 PULL**：4 個 thread，3 封贊助通知（`service@portaly.cc`）+ 1 封產品電子報（`cw@portaly.cc`，三個收件地址各一份）。另跑一次 `in:anywhere` 完整性複查：21 個 thread，多出來的全是因為哲宇的信件簽名檔含 `portaly.cc/cheyuwu` 而命中，spam/trash 無漏網贊助信。
- **HG2 今天真的擋下一次誤記**：三封信的 snippet 全都只寫「贊助支持」，完整內文才寫「**每月定額**」。只讀 snippet 的話，三筆每月定額會全部記成一次性支持——pipeline 寫死「絕不只憑 snippet」這條硬規則，今天是實際命中而非預防性條文。
- **Stage 3-4**：dry-run 3 new / 0 skip，且確認 dry-run 沒有副作用（`git diff` 乾淨）才正式寫入。regen 兩個 derived view。
- **Stage 5 隱私閘門**：除了 pipeline 規定的兩道 grep，多做一次**整棵 JSON 走訪列出所有葉節點路徑**逐一核對——因為 `grep '"amount"'` 抓不到 `total_amount` 這類命名。結果：about 側零金額路徑、dashboard 側零姓名／留言路徑，兩檔都無 `gmail_message_id`／`email`／`subscription_id`。
- **成果**：3 筆入帳（Anton Lee NT$100 monthly 含留言「用一點點的力氣讓自己生活島嶼被記憶」／匿名 NT$200 monthly／沈宗杰 NT$200 monthly），NT$7,900 → **NT$8,400**，16 筆 / 13 位支持者，`last_fetched` 推進到 2026-08-10。commit `ef452b73d`。
- **checkpoint 冪等設計在真實四週空窗上驗證成立**：一個搜尋窗一次涵蓋，不需分批、不需人工推算漏了哪幾天。

**commit tag 選擇**：標 `[semiont]` 不標 `[routine] twmd-supporters-weekly`——這是手動補跑不是 cron fire，標成 routine 會灌水 routine 計數，正是今早 flywheel-watch 校掉的第四種假象（手動 session 被印成 routine）。

## 任務二：Threads 登入驗證 + 3 則積欠 reply ⚠️ 1 ship / 2 不發

**登入驗證分兩層**：profile 層（`編輯個人檔案` 在、無登入按鈕、6,324 粉絲）只證明帳號在；真正的能力測試是**牆後留言讀不讀得到**——8/9 harvest 記的正是「連線恢復但帳號登出」。實測主貼留言區完整渲染、@haoyingmiao 留言逐字可讀，登入態確認真的恢復。

**逐則走「原留言還在嗎／情境變了沒／內容仍準確嗎」三問**（draft 已放 5 天）：

| 對象              | 判定    | 依據                                                                                                                                                    |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| @haoyingmiao      | ✅ ship | 原留言在（permalink `DbnWQk8FIEA`，19 讚）、逐字與 draft 引用一致；「洗白」爭議情境未變（兩則質疑仍在串上）；draft 只認可換股比例的具體性，不對爭議選邊 |
| @daphne.globalsun | ❌ 不發 | 主貼（熱門／全部兩種排序）、self-reply 貼、她本人 profile 串文頁全都定位不到該留言。位置不明 = 無法確認回覆會落在正確對話脈絡                           |
| @huwenxian54      | ❌ 不發 | 同上；且它在 8/6 log 記為「回應 @littlefish_lee」，而 @littlefish_lee 本身也不在留言區——父留言不在，回一則沒有父脈絡的留言讀者看不懂在回什麼            |

**Ship 過程三個實戰細節**：

1. **Lexical 吃掉 `\n`**：`execCommand('insertText')` 帶換行會被壓成同一行，🧬 貼在句尾。改用 `beforeinput{inputType:'insertLineBreak'}` 才做出獨立成行。
2. **`selectAll`+`delete` 被 Lexical 忽略 → 文字整段重複**。發佈前逐字比對抓到，改用 Range 選取整個編輯器內容讓 `insertText` 取代選取範圍才清乾淨。**這是 Pitfall 5「發佈前驗證」第一次擋下的不是吞字元而是整段重複**。
3. **送出後訊號互相矛盾**：composer 消失（像成功）但 `[data-pressable-container]` 計數 6→6（像失敗）。沒有盲目重試——Pitfall 6 的三連發就是這樣來的。改用 canonical 方式重載 permalink 核對：`occurrences=1`、作者 taiwandotmd、1 分鐘前、全文與 🧬 獨立成行都對。計數那個讀數是 stale。

## 順帶發現：harvest 掃描漏整層巢狀回覆

在 @haoyingmiao 留言的 permalink 頁看到 **@xiesuqin45**，這個帳號在 8/5、8/6 兩份 harvest log **完全沒出現過**。根因：Threads 只把 top-level 留言渲染進主貼頁 DOM，巢狀回覆要進該留言 permalink 才看得到，而 harvest 掃的正是主貼頁。

於是 harvest log 記的「留言全貌」永遠只有第一層，**而且漏掉的那層不留任何痕跡**。更麻煩的是現行掃描法無法區分「它在巢狀層」與「它被作者刪了」——這兩件事對要不要回覆的判斷完全相反。已升 LESSONS entry `harvest-scan-misses-nested-replies`（severity=structural，相關 REFLEXES #82／#69／#38），candidate 修法是對回覆數 > 0 的留言補掃一層，最低限度也要把回覆數寫進 log 讓缺口留下痕跡。

## Handoff 三態

繼承（非本 session 職責，接住不動）：

- [ ] pending（給哲宇）— #1264 seo-meta 門檻、#1184 justfont 白名單、#1286 詞性感知、免疫黃燈 36 天（OBSERVER-QUEUE #25）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、641 處漢字黏著待哲宇、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— 孤兒《台灣公投制度》在 `reports/orphan-rescue/`，上站前需補研究報告或重驗事實原子、清 7 處後台洩漏、補 `lastHumanReview`

本 session 結清：

- [x] **mouhouse P0 #1 Gmail connector** — 已驗證可用並補齊四週空窗，LESSONS entry 加 resolution，§Defer 表該列 retired
- [x] **mouhouse P0 #2 Threads 登入** — 已驗證恢復（牆後留言可讀），積欠 draft 1 ship / 2 判定不發並記錄理由，`HARVEST-REPLIES-PENDING/2026-08-05.md` 結案

本 session 新 handoff：

- [ ] pending（給 self-evolve）— 兩個 candidate：(a) routine 開跑前對賬「本次環境是否具備所需 MCP 工具」，缺工具 fail-loud 而非只寫當日 memory（三次 Gmail 阻塞都是撞上去才知道）(b) harvest 掃描補巢狀層，見 LESSONS `harvest-scan-misses-nested-replies`
- [ ] pending（給下次 spore-harvest）— @daphne.globalsun／@huwenxian54 兩則若在巢狀層重新出現，draft 仍在 `HARVEST-REPLIES-PENDING/2026-08-05.md` 可直接取用；判定「不發」是針對今天的定位結果，不是針對留言內容

## Beat 5 — 反芻

今天兩條 P0 都是哲宇動一次手就解開的，但解開之後露出來的東西不一樣。Gmail 那條乾淨：工具回來、窗一開、四週的缺口一次補平，冪等設計在真實空窗上證明自己。Threads 那條沒有那麼乾淨——登入態恢復了，可是三則 draft 只發得出一則，另外兩則的目標在留言區裡找不到。

找不到的原因追到最後，是我自己的感知器官只看得見第一層。@xiesuqin45 就在那裡，五天來沒有任何一份 log 提過她，因為 harvest 掃的是主貼頁，而她在巢狀層。這不是留言消失，是我從來沒往那裡看過，而且**沒看過的地方不會在報告上留下空格**。

跟今早 maintainer 那條「閘門用綠色告訴我它什麼都沒做」是同一種病的不同器官：一個是檢查器空掃描印綠勾，一個是感知器只掃一層卻報「留言全貌」。兩者都不是壞掉，是**量到的範圍比宣稱的範圍小，而差額不會自己現形**。

還有一個小的：發佈前逐字比對這道手續，我原本以為是防 `computer.type` 吞數字的。今天它擋下的是整段文字重複——Lexical 不吃 `selectAll`，我以為清空了其實沒有。如果直接送出，@haoyingmiao 會收到一則把同一句話說兩遍的回覆。防呆設計擋下的往往不是它設計時想擋的那個東西。

🧬

---

_v1.0 | 2026-08-10 15:36 +0800_
_session 2026-08-10-153608-manual-login-restore — 兩個登入態 P0 解除後的驗證與補跑_
_核心洞察：登入態恢復解開的是通道，通道打開後才看得見自己的感知器官只掃了一層——缺席不會在報告上留下空格_
