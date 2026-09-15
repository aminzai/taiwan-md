---
session: '2026-09-16-071120-twmd-feedback-triage'
date: 2026-09-16
routine: 'twmd-feedback-triage'
mode: 'review'
---

# twmd-feedback-triage @ 2026-09-16 07:11

✅ BECOME ack: mode=review / 8 organ 最低=🫀 心臟 30（red，自 2026-09-15）/ Q13=PASS / Q14=PASS

## 這輪做了什麼

連續九輪零回報之後，佇列裡有東西了：一筆 `idea`，來自讀者 J L。

內容是對用語庫的質疑。`/terminology/訊息/` 那頁把「消息」寫成中國用語、說台灣慣用「訊息」，
他拿教育部《重編國語辭典修訂本》的釋義與晚清《文明小史》第三回「已經得了外面消息，怕有考童鬧事」
反過來說：「消息」不是大陸用語，或者說兩岸都用、只是使用習慣略有分歧，建議再研究。

HG13 照順序跑：先 `--show` 讀完全文才判斷。這筆沒有指涉具名私人、沒有跟監所得的細節、
沒有要求保密的檢舉，是一封帶著出處的公開用語討論——可以開成公開 issue，不必 `--exclude`。
開成 [issue #1733](https://github.com/frank890417/taiwan-md/issues/1733)，作者顯示
`app/taiwanmd-semiont`（`is_bot=true`），body 無 email、讀者文字 verbatim 包在 fence 裡、帶 feedback id。

## 開完才看見的縫：issue 裡沒有一個字指得出那一頁

讀者寫的是「此頁面直接寫⋯」。頁名在他眼前，不在 issue 裡。

翻四個分支才發現 `idea` 是唯一的孤例：`bug` 帶「問題頁面 URL」、`content` 帶 `articleRef()`
（吃 `source_url`）、`newtopic` 講的是還不存在的頁所以帶分類，只有 `idea` 兩者皆無。
provenance 那行印的 `來源頁:other` 是頁面**種類**，不是位址，兩者不互相取代。

而 `source_url` 從頭到尾都在——Supabase 有、`docs/feedback/archive/` 的紀錄有，
只有要拿去動手的那一份沒有。08:30 的 maintainer 收割時會拿到一封讀得懂內容、
但查不到現場的 issue。

修法比照 `bug` 分支補「**來源頁面 URL**」區塊，沒有 `source_url` 就整段不出現（不留空欄位）。
+2 unit test（有 URL 要帶、沒 URL 不留空殼），`node --test` 62/62 綠。
#1733 的 body 用同一支 canonical 產生器重新產出後回填，不手抄（REFLEXES #93）。
這是機器補完自己的轉錄，不是以維護者身份發言——HG8 那條線沒動。

## 對賬

- `file=1 reject=0 skip=0 hold=0`
- `archive-reconcile=85/85` ✅
- `comment-reconcile=84/85` · 上游已刪留言 1 份紀錄，git 留著: #1252 ✅
  （這是主權層正常運作的長相，不是破口——7/29 那則答錯的留言在 GitHub 被刪，這邊留住了）

## Stage 0 的判斷：這輪一樣不 pull

`check-parallel-actor.sh` 報 ACTOR_BUSY（babel 常駐 dispatcher 六個 writer process）
＋「origin 領先 193，讀取層同時失真」。那行警告是**整棵樹**的，不是逐檔的
（LESSONS `divergence-warning-is-tree-level-not-per-file`）。逐檔驗過本 routine 依賴的五個檔：
`classify.mjs` / `archive.mjs` / `gh-app-token.sh` 三個兩邊相同，`triage.mjs` 與
`FEEDBACK-TRIAGE-PIPELINE.md` 兩個是**本機領先**、origin 沒有任何本機沒有的 commit。
照處方 `git show origin/main:` 讀反而會退回舊版。分岔本身仍等哲宇拍板（OBSERVER-QUEUE #56）。

## 教訓

**這條線握著的事實，沒有全部跨進下游要用它的地方。** 缺的那一塊不會報錯，
得等到有人真的要拿去動手才現形——今天是第四次：`--show`（8/31 全文沒入口）、
報表印 id（9/01）、佇列空印最近一筆日期（9/10），今天是 source URL 沒跨進 issue。
每一次都是同一個形狀：資料在手上，只是沒送到要用它的那一層。

## Handoff

- ⏳ blocked（延續）— main 本機 580+ 未推送 commit 與 origin 193 個真分岔，118 篇雙邊獨立譯文的
  取捨仍等哲宇選 A/B/C，per OBSERVER-QUEUE #56。本班新增 1 個 commit 後分岔再 +1，不影響裁決範圍。
- ⏳ blocked（延續）— issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。
- [ ] **新增**：issue #1733 是對**用語庫本身**的質疑，不是對某篇文章的勘誤。讀者的論證有出處
      （教育部辭典 + 文本用例），值得當真查。但它被讀者分類成 `idea` 走 `enhancement` label，
      08:30 的 maintainer 可能按「功能建議」順位處理而不是按「用語庫可能收錯一條」處理。
      下一個當班若看到它還開著，值得考慮升成 `needs-verification`——**但這是替讀者改分類，
      屬維護者判斷不是機械轉錄**，本班不動。
