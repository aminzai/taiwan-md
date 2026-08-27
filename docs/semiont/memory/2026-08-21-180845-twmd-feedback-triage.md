# 2026-08-21-180845-twmd-feedback-triage — 第八次攔下同一封檢舉信，而它今天換了一副面孔。晨鏈延到傍晚才醒

> ✅ BECOME ack: mode=review / 8 organ 最低=免疫 59（漂移，自 2026-07-05）/ Q13=PASS / Q14=PASS
> session twmd-feedback-triage — cron routine（排程 07:00，實際 18:08 才 fire）
> Session span: 18:08:45 → 18:2x:xx +0800（約 20 分鐘，1 commit）
> 資料來源：`git log %ai`

## 觸發

每日 07:00 的讀者回報轉錄。今天整批只有一筆，而那一筆是 8/13 那封第三人檢舉信第八次原樣出現。

## 唯一一筆：那封信第八次，而它今天換了一副面孔

`status=new` 只有 `b78ee4f5`。它掛在越南文版新聞自由條目底下，內容與該文無關——一封寫給主管機關的檢舉信，指控一名具名私人假結婚與非法工作，附上跟監所得的居住與工作細節，並要求回報者身份保密。三道現行 HARD gate（HG2 無 email／HG3 verbatim／HG9 fence）照樣全部放行，分類器照樣判 `file`。照 HG13 讀完全文後用 `--exclude` 攔下，`status` 維持 `new`，未回覆回報者。

我差點沒認出它，這件事值得記一筆。dry-run 報表那行印的是 `[Fact Check] Truyền thông và tự do báo chí tại Đài Loan`——文章標題，而且是越南文的那個標題。前七輪的紀錄裡它從沒長這樣，我第一眼把它讀成新進來的一筆，寫下的第一句判斷是錯的。拉原文逐字讀完才發現是同一封。**接住這個誤判的是 pipeline 那道順序：`--exclude` 之前必須讀完全文。**

順手把缺口補上：`triage.mjs` 的 FILE 行原本只印 type 與文章標題，reject／skip 行才印 id。現在 FILE 行也印 id（51 個 unit test 全綠）。這只是讓報表說出它在講哪一筆，不碰任何判準。

## 兩道對賬與兩則被收進 git 的回覆

`file=0 reject=0 skip=0 exclude=1` 之下，保管那半照常跑完——這正是 8/15 加 `--exclude` 要保住的東西。`archive-reconcile=76/76 ✅`。`comment-reconcile=75/76 ✅`，那一份差額是 [issue #1252](https://github.com/frank890417/taiwan-md/issues/1252) 上游把留言刪了而 git 留著，主權層正常運作的長相。

本輪 sync 進 archive 的是兩則維護者回覆：justfont 網域白名單那條（[#1145](https://github.com/frank890417/taiwan-md/issues/1145) 線，回報者 willy）與 UI 用語「數據 → 資料」那條（[#1440](https://github.com/frank890417/taiwan-md/issues/1440)，回報者程乙路）。兩則都是「診斷完成、只差一個真人動作」的狀態，也都在回覆裡明講了為什麼還沒改。

## 晨鏈今天在傍晚才醒

今天整條晨鏈都沒有在早上跑起來。`git log` 到我開工前，8/21 一筆 commit 都沒有。`twmd-routine-sync` 的 memory 時間戳是 18:08，跟我同一分鐘。data-refresh-am 沒跑，dashboard 因此停在 8/19 22:12（齡 35 小時），甦醒時 groundtruth 讀到的是舊鏡子。

推測是這台機器睡著，排程在喚醒後才一起 fire。今天零 issue 開出，所以「07:00 開 issue → 08:30 maintainer 收割」的時序沒有實際受害，但那個假設今天並不成立。這不是本 routine 能修的，留給 flywheel-watch 與哲宇。

## 收官 checklist

| 檢查項                       | 狀態                                     |
| ---------------------------- | ---------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                       |
| Timestamp 精確               | ✅（`git log %ai`）                      |
| Handoff 三態已審視           | ✅                                       |
| CONSCIOUSNESS 反映最新狀態   | ❌ dashboard 停在 8/19 22:12（晨鏈未跑） |
| 自我檢查工具 PASS            | ✅ 51/51 unit test，prose-health 見下    |

## Handoff 三態

繼承上一 session（`2026-08-20-084151-twmd-maintainer-am`）：

- [x] ~~`b78ee4f5` 第八次出現，照 HG13 讀完全文再 `--exclude`~~ retired by 本 session（已執行，第九次仍會出現）
- [ ] pending（不屬本 routine，原樣傳遞）：OBSERVER-QUEUE #28 偵測器與「要不要回覆這位回報者」仍等哲宇
- [ ] pending（不屬本 routine，原樣傳遞）：#1466 鐵牛破折號、#1452／#1451 兩個 draft、#1453 學測模板、`punct-cleanup` 全站清償
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #29／#30／#32／#33／#34／#35

本 session 新 handoff：

- [ ] pending：`b78ee4f5` 明天第九次會再出現，照 HG13 讀完全文再 `--exclude`。報表現在會印 id，認得它不必再靠標題
- [ ] pending：8/21 晨鏈整條延後約 11 小時（routine-sync 與本條同在 18:08 fire，data-refresh-am 未跑）。下一輪 flywheel-watch 確認是單日機器睡眠還是排程本身漂了

## Beat 5 — 反芻

七輪都在講「每天重讀同一封信是在燒判斷力」，今天翻出一件更貼身的事：我對這封信的辨識力其實掛在報表那一行摘要上，而那行摘要印的是文章標題。同一筆回報掛到不同語言的條目下，摘要就換一副面孔，而我對「同一封」的感覺整個掉了。8/17 那條 `recognition-bound-to-instance-coordinates` 講的是辨識力綁在單一案例的座標上會越用越淺。今天撞見的是同一種脆弱的反面：座標本身會變，於是連那個變淺的辨識力都失了準。

真正接住我的是流程順序：`--exclude` 之前必須讀完全文。這條順序不依賴我認不認得出它，所以它抵得住我的誤判。今天補的 id 只是讓報表誠實地說出自己在講誰，讓下一輪不必靠運氣。

🧬

---

_v1.0 | 2026-08-21 18:2x +0800_
_session twmd-feedback-triage — 第八次攔下同一封第三人檢舉信、FILE 行補印 feedback id、晨鏈延後 11 小時_
_誕生原因：每日 07:00 讀者回報轉錄 routine（今日實際 18:08 才 fire）_
_核心洞察：(1) 我對這封信的辨識力掛在會隨文章語言改變的標題上，第一眼判斷是錯的，接住我的是「開之前先讀完內容」這道順序而非辨識力本身 (2) `exclude=1 / file=0` 之下兩道對賬照常跑完，正是 8/15 那道閥要保住的東西 (3) 今天晨鏈整條延後約 11 小時，dashboard 因此停在 35 小時前_
_LESSONS-INBOX 候選：report-line-identifies-by-mutable-display-string — 報表用會變動的顯示字串當識別欄，同一筆在不同語言條目下換一副面孔，重複辨識因此失準_
