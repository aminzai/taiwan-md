---
title: '讀者回報裡的第三人指控：一則不能開成 public issue 的回報'
description: '2026-08-14 twmd-feedback-triage cycle 攔下一則以檢舉為目的、指控具名私人的站上回報。記錄攔截理由、當班處置，以及分類器在這個類別上的缺口與三條修補路線。'
type: 'incident-and-design'
status: 'awaiting-observer'
date: 2026-08-14
session: '2026-08-14-070000-twmd-feedback-triage'
related:
  - 'docs/pipelines/FEEDBACK-TRIAGE-PIPELINE.md'
  - 'docs/semiont/MANIFESTO.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
---

# 讀者回報裡的第三人指控

> 本檔刻意不寫被指控者的姓名、居住地區、入境日期、工作場所描述，也不引用回報原文。
> 那些內容留在 Supabase 的原始紀錄裡（`feedback id: b78ee4f5-e1af-4876-93d6-852694246e58`），
> 哲宇要看時直接查該筆。把它們抄進 git 就等於用另一個形式完成了本檔要攔下的那件事。

## 發生了什麼

2026-08-14 07:00 的 `twmd-feedback-triage` cycle 抓到一筆 `status=new` 的站上回報，掛在越南文版
`/vi/society/media-and-press-freedom-in-taiwan`（傳媒與新聞自由）底下。

它跟那篇文章沒有關係。內容是一封寫給主管機關的檢舉信：回報者自稱調查人員，指控一名具名女性
涉及假結婚、非法工作與人口偷渡網絡，附上跟監所得的居住與工作細節，要求「調查與核實」，
並請求對自己的身份保密。

分類器的判斷是 `file` — 類型 `content`，準備開一個標題為 `[Fact Check] Truyền thông và tự do
báo chí tại Đài Loan`、帶 `needs-verification` 與 `from-feedback` 標籤的公開 issue，
內文 verbatim 收錄全文。

## 為什麼沒有開這個 issue

開下去會發生四件事，每一件都不可逆：

1. **一名私人的姓名會跟一組未經查證的犯罪指控一起，永久掛在公開 repo 上**，被搜尋引擎索引、
   被 AI 爬蟲收走。她不是公眾人物，沒有回應管道，也不知道自己被寫在那裡。
2. **跟監所得的個人資料會被公開**：居住狀況、工作場所、入境時間點。這些是對一個私人的
   監視結果，Taiwan.md 沒有任何立場把它們散布出去。
3. **回報者本人的處境會變糟**。他明確要求身份保密，而 issue 的 provenance 區塊會署上他的
   `display_name`。這道規則（HG2 只放 display_name 不放 email）設計時想的是保護回報者，
   在這個情境裡它反而把人推出去。
4. **收件人根本不是我們**。這是給移民署或警政單位的檢舉，送到一個知識庫的回報表單是誤投。
   我們既無權查證，也不該替任何一方留下紀錄。

MANIFESTO §自主權邊界的「敏感素材決定 — AI 準備 blueprint，人類 final call」正是這一類；
REFLEXES #79 的預設姿態也是 reserve。所以本 cycle 的處置是攔下來交給哲宇，不是自己裁決。

## 當班怎麼做的

| 動作                         | 結果                                                                                    |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| `triage.mjs`（dry-run）      | 跑了，看到分類結果是 `file`                                                             |
| `triage.mjs --commit`        | **沒跑**。`triage.mjs` 沒有排除單筆的參數，跑下去就會開那個 issue                       |
| Supabase status              | **維持 `new`，沒有任何 out-of-band 寫入**（HG12b 的誕生原因就是繞過主權層的手動改狀態） |
| 留言 sync + HG12b/HG12c 對賬 | 用 canonical 純函式單獨跑完（見下）                                                     |
| 回覆回報者                   | 沒有。對外開口是人類 gate                                                               |

兩道對賬的結果跟正常 cycle 一樣乾淨：

```
archive-scanned=74 archive-comments-synced=0
archive-reconcile=74/74 ✅
comment-reconcile=73/74 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅
```

`#1252` 是 7/29 那則在 GitHub 被刪、git 這邊留住的留言，主權層正常運作，不是破口。

之所以要另外跑這一段，是因為 8/13 那輪剛留下的教訓（`zero-input-cycle-drops-the-reconciliation`）：
這條 routine 的保管職責跟轉錄職責是兩個獨立變數，不能因為轉錄那半停手就讓核帳一起消失。
今天是那條教訓的鏡像 — 不是沒有輸入，是輸入不能轉錄。

## 缺口：分類器沒有這個類別

`detectSpam()` 擋的是廣告的形狀：太短、賭場關鍵字、四個以上連結、洗版字元、全大寫加連結。
這則回報一項都不中。它很長、很有條理、沒有連結、語氣正式。**它在機器眼中跟一則高品質勘誤
長得一模一樣**，差別只在讀懂內容之後才存在。

`detectInjection()` 也不會響，因為它確實沒有夾帶指令。

於是這條線上目前唯一擋住它的東西，是當班 session 讀了內容之後的判斷。那正是 REFLEXES #15
說的「memory 是自律，canonical SOP 才是閘門」裡的自律那一側。**明天 07:00 的 cycle 會再遇到
同一筆**，因為狀態維持 `new`；接得住與否取決於下一個 session 有沒有一樣讀完再動手。

值得指出的是：三道現行 HARD gate 在這則回報上全部會通過。HG2 沒有 email、HG3 verbatim 沒改
一個字、HG9 隱形字元剝乾淨且包了 fence。**閘門量的是回報者的文字有沒有被正確搬運，沒有一道
在問這段文字搬到公開處會傷到誰**。這跟 8/11 那輪「六條閘門全綠而讀者的問題一個都沒解決」
是同一種形狀，只是後果的方向反過來：那次是沒做到好事，這次是差點做成壞事。

## 三條修補路線（給哲宇拍板）

### (a) 加一道「第三人指控」偵測，命中走既有的 `hold`

`classify.mjs` 已經有 `hold` 這個狀態（batch-cluster guard 在用）：不開 issue、不動狀態、
產一份 consolidated 報告給維護者。新偵測器命中就走同一條路。

- **成本**：一個 deterministic 偵測器 + 單元測試，約半天，含校準。
- **風險**：假陽性。一則正當的勘誤如果引用了某人的爭議（政治人物條目的勘誤很常這樣），
  可能被誤 hold。但 hold 的代價只是延後與人工看一眼，不會丟掉回報，比誤開低得多。
- **難處**：判準要寫成機器讀得懂的形狀。可用的訊號有：回報內容與所在文章零重疊、
  出現「調查／檢舉／核實／舉報」類請求語、指涉具名個人並描述其住居或工作、
  要求保密身份。單一訊號都不夠，要組合加權。
- **附帶好處**：`hold` 的報告產生器目前會把回報全文寫進 `reports/feedback-clusters/`。
  這個類別必須改成只寫形狀不寫內容，否則 hold 本身就洩漏了一次。

### (b) 不寫偵測器，改寫 `triage.mjs` 加 `--exclude <id>` 參數

讓當班 session 能排除特定筆之後正常跑完 `--commit`，對賬跟留言 sync 都不受影響。

- **成本**：極小，一小時內。
- **限制**：這是把判斷完全留在人身上的方案，只解決「攔下來之後流程還能跑完」，
  不解決「誰來攔」。適合當 (a) 的配套，不適合單獨用。

### (c) 什麼都不加，靠 handoff 與本檔傳遞

- **成本**：零。
- **代價**：這筆會每天出現在 `status=new` 裡，每天由當班 session 重新判斷一次。
  只要有一次沒讀完就動手，就會開出去。REFLEXES #15 對這種安排的判決已經寫得很清楚了。

**推薦 default：(a) + (b) 一起做**，(b) 先上（成本低、立刻解除明天的風險），
(a) 排進下一個有觀察者在場的 session 做校準。

**不推薦自行執行的理由**：新增品質閘門在 BECOME §行動鐵律 10 是強制升 Full mode 的高風險
動作，而閘門判準訂得太寬會靜默擋掉正當勘誤 — 那是 8/09 `gate-triggers-content-degradation-incentive`
剛記過的那種傷害。這種東西不該由一條 07:00 無人在場的 routine 當場決定形狀。

## 還有一件事需要哲宇決定

**要不要回覆這位回報者，以及回什麼。** 他送出的是一份檢舉，合理的回應是告訴他這裡是知識庫、
這類事情要向移民署或警察機關提出。但那是一次對外開口，per §自主權邊界屬人類 gate。
在他收到任何回應之前，這筆會一直停在 `new`。

## Handoff

- 該筆維持 `status=new`，**不要開成 issue**（feedback id `b78ee4f5-e1af-4876-93d6-852694246e58`）
- 明天以後的 feedback-triage cycle 讀到本檔或 handoff 就照樣攔，直到哲宇拍板
- OBSERVER-QUEUE #28 是這件事的正式出口，標 `🔒 等真人`（§自主權邊界四紅線不適用 default-action）

🧬

---

## 附記：2026-08-15 cycle（第二次攔下，(b) 已 ship）

該筆原樣再出現在 `status=new`（8/14 沒動狀態的必然結果，feedback id 同）。當班第二次攔下：
未開 issue、未改 status、未回覆回報者。

跟昨天不同的是保管那半的走法。昨天為了不開這個 issue，整條 `--commit` 沒跑，兩道對賬是當班
用 canonical 純函式手動補的；今天把本檔 §(b) 做掉了 —— `triage.mjs --exclude <id>`
（`partitionExcluded()` 純函式 + 5 unit test，打錯的 id 印 `⚠️` 不靜默，`main()` 改成只有被
當指令跑才執行好讓純函式可被 test import）。實跑 `--commit --exclude b78ee4f5…`：

```
[triage] done · file=0 reject=0 skip=0 hold=0 exclude=1 · archive-scanned=74 archive-comments-synced=0
[triage] archive-reconcile=74/74 ✅
[triage] comment-reconcile=73/74 · 上游已刪留言 1 份紀錄,git 留著: #1252 ✅
```

同步升 HG13 進 pipeline v1.6、薄殼 skill、cron prompt 三層（`routine-sync.py --apply` 印「三層一致」），
明天以後的 cycle 由 prompt 指名攔這筆，不再只靠當班有沒有讀完 handoff。

**沒有動的部分**：§(a) 偵測器（判準校準屬高風險，理由見上）與 §還有一件事需要哲宇決定
（要不要回覆這位回報者）原封不動。OBSERVER-QUEUE #28 仍 `🔒 等真人`。

🧬
