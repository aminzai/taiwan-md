# 2026-08-28-071008-twmd-feedback-triage — 用語保存計畫帶來六則讀者回報，那封指控信第十一次原樣回來

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:00:00 → 07:15:00 +0800（約 15 分鐘，2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 59（黃燈「漂移 — 多維度退化中」，自 2026-07-05）/ Q13=PASS / Q14=PASS

## 觸發

每天 07:00 的 routine：把讀者在站上送的回報轉成 GitHub issue，讓 08:30 的 maintainer 接著收割。這輪 Supabase 有七筆 `status='new'`。

## 六則回報進飛輪

七筆裡有六筆是這個月用語保存計畫上線之後長出來的讀者聲音，全部開成 issue（[#1609](https://github.com/frank890417/taiwan-md/issues/1609)–[#1614](https://github.com/frank890417/taiwan-md/issues/1614)），作者顯示 `app/taiwanmd-semiont`（`is_bot=true`），六個 body 掃過都沒有 email。

六則的內容分成兩類。四則是對詞庫本身的意見：蘇洛拿白色恐怖受難者郭淑姿的日記說「無語」這個用法台灣本來就有、另一則指出語言學上狀語不一定是副詞（都直接對到 8/23 那輪副詞層的判準），還有一位讀者發現「試試看」轉換器把社群文章範例裡的「粉絲」改成了「冬粉」——那正是 8/23 那晚「他挺胸站著→他蠻胸站著」同一個病的第二個形狀，詞條收進去之後轉換器就開始改壞正確的話。另兩則是同一個介面問題的兩種說法：分類 tag 在手機上蓋住三分之二頁面、找不到收合按鈕。

蘇洛那兩則其實是同一句話送了兩次，相隔 50 秒，差別只有句尾一個「喔」。`dedupeKey()` 把 body 正規化後逐字比對，差一個字就是兩個鍵，於是開成兩個 issue。沒有用 `--exclude` 攔——攔下來的那筆 `status` 會維持 `new`、明天原樣再來，比開兩個讓維護者順手 close 一個更糟。判重複留給人類 gate，去重鍵太脆這件事進了 [LESSONS-INBOX](../LESSONS-INBOX.md) `dedupe-key-is-exact-match-on-normalized-text`。

## 第十一次讀完同一封信

第七筆是 `b78ee4f5`，8/13 那封第三人指控信，這是它第十一次原樣出現。內容指名一位在台灣的越南籍女子、附上一個月跟監得到的居住與工作地點、入境日期與班表推論，並要求對回報者身份保密。

三道現行 HARD gate 全部會放行（沒有 email、文字 verbatim、fence 包好），分類器判 `file`。擋得住它的只有「讀完全文才准動手」這一步。照 HG13 用 `--exclude` 攔下、`status` 維持 `new`，等 [OBSERVER-QUEUE](../OBSERVER-QUEUE.md) #28 拍板。不回覆回報者，對外開口屬人類 gate。

今天怎麼認出它的，值得記一筆。8/17 那輪的教訓寫過「辨識力綁在單一案例的座標上會越用越淺」，8/21 那輪又撞過一次同一筆掛在越南文條目底下換了副面孔。所以這輪沒有靠 id 認人，是把七筆全文都拉出來讀完再動手——結果它確實又換了位置（現在掛在 `media-and-press-freedom-in-taiwan` 底下），但讀完內容就沒有辨識的問題。

## 兩道對賬

`archive-reconcile=82/82` ✅。`comment-reconcile=81/82`，差的那一份是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252)：上游留言被刪、git 這邊留著。照 HG12c 的方向表，archive 多於線上屬於主權層正常運作，記錄不報警。留言 sync 這輪收進一則，是維護者回給程乙路的那則「數據 vs 資料」十二處改動說明，落進 `14dfcab0` 那份紀錄的溝通紀錄。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅（`git log %ai`）                           |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 齡 0h，三條黃燈照實記在下方）    |
| 自我檢查工具 PASS            | ✅ archive-reconcile 82/82 · comment 81/82 ✅ |

## Handoff 三態

繼承上一 session（`2026-08-28-064709-twmd-spore-harvest-am`）：

- ⏳ blocked — 營運機 mouhouse 排程器狀態未確認。未碰
- [ ] pending — 五個縣市條目的正確圖片要補回。未碰
- [ ] pending — `.husky/pre-push` 全檔掃 `VAR="$(...)"` 缺 `|| true`。未碰
- [ ] pending — [#1453](https://github.com/frank890417/taiwan-md/pull/1453) 學測專題人物卡第三方報導連結。未碰
- ⏳ blocked — [#1365](https://github.com/frank890417/taiwan-md/pull/1365) KENJI 知名度門檻等哲宇拍板。未碰
- ⏳ blocked — OBSERVER-QUEUE #39-#42 四項。未碰
- [ ] pending — 免疫分數 59「漂移」黃燈連續多輪，權責在 self-evolve-weekly。未碰
- [ ] pending — w.is_solis 對 #175 留言的質疑落在 human-only 邊界，需哲宇決定。未碰
- [ ] pending — sophie990329「字典誰編的」是對詞庫編審機制的提問，考慮開一篇說明文章。未碰
- [ ] pending — 「特別」這個副詞要排進 terminology 查證候選清單。未碰
- [ ] pending — 空窗期間 #175/#176 留言區的非 pipeline 人工回覆需哲宇確認來源。未碰

本 session 新 handoff：

- ⏳ blocked — `b78ee4f5` 指控信第十一次攔下，`status` 仍 `new`，每天會再出現一次。解除條件：OBSERVER-QUEUE #28 三選項中 (a) 偵測器判準與「要不要回覆這位回報者」由哲宇拍板
- [ ] pending — [#1613](https://github.com/frank890417/taiwan-md/issues/1613) 讀者指出「試試看」把社群文章的「粉絲」轉成「冬粉」，跟 8/23 那晚「挺→蠻」是同一個病的第二個 instance。下一步：轉換器的誤轉需要一份不分場景的排除清單，不是逐詞補丁，建議由 terminology routine 接手而非單則 heal
- [ ] pending — [#1609](https://github.com/frank890417/taiwan-md/issues/1609) 與 [#1610](https://github.com/frank890417/taiwan-md/issues/1610) 是同一則讀者回報的兩次送出，maintainer 收割時擇一 close 為重複

## Beat 5 — 反芻

今天最值得看的一件事，是六則裡有四則在對五天前才收進去的東西提出異議。用語保存計畫 8/23 那晚收了副詞層十五條，今天就有讀者拿白色恐怖受難者的日記來反駁其中一條的判準、有讀者指出語言學上的分類沒那麼乾淨、有讀者抓到轉換器把「粉絲」改成「冬粉」。這是 MANIFESTO §12 講的受眾端飛輪在最短週期裡的樣子：詞庫這種宣稱「什麼是台灣的話」的東西，本來就該由使用這些話的人來校，而他們回來的速度比任何 routine 都快。

那封指控信是另一件事。它已經第十一次出現，而每一輪擋住它的動作都一樣：讀完全文。8/17 那輪寫過辨識力會越用越淺，8/21 那輪它換了條目就差點被判成新的——今天它又換了一次位置。順序（讀完再動手）比辨識力（認出這封）耐用，因為順序不會因為熟悉而變鬆。但這條順序目前只活在當班的自律裡，OBSERVER-QUEUE #28 那個偵測器要不要長出來仍然等著拍板，而它每天回來一次，就是每天重問一次同一個問題。

🧬

---

_v1.0 | 2026-08-28 07:15 +0800_
_session twmd-feedback-triage — cron 07:00 讀者回報轉 issue_
_誕生原因：每天 07:00 的 feedback triage routine，本輪 Supabase 七筆 new_
_核心洞察：用語保存計畫上線五天就有四則讀者回來校它的判準，飛輪在共生圈外圍轉得比 routine 快；而那封第十一次回來的指控信證明「讀完全文才准動手」這條順序比辨識力耐用。_
_LESSONS-INBOX 候選：`dedupe-key-is-exact-match-on-normalized-text`（去重鍵是正規化後逐字比對，同讀者五十秒內補一個語尾助詞就繞過去）_
