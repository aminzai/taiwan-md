# 2026-09-04-084247-twmd-maintainer-am — 讀者說「載入很久」，追下去是整站在字型慢的時候變成永久空白頁。四個投稿收進來，一句活了四個月的引語被換掉

> session twmd-maintainer-am — cron routine，每日 08:30 maintainer cycle
> Session span: 08:42:47 → 09:13:22 +0800（約 31 分鐘，5 個自有 commit + 4 個 merge commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=full（review 起手，Stage 1 掃到 8 個 ready PR，命中 High-stake 觸發 #1「PR triage ≥ 5」強制升 Full）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05 未解）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer cycle。Stage 1 掃到 8 個 ready PR、3 個 draft、5 個 open issue，其中 1 個 issue 與 4 個 PR 是昨天以後才進來的新場。今天不是空場。

## 字型閘門：一個沒有出口的閘門，四個月

idlccp1984 開的 #1666〈頁面載入時間太長〉是一份寫得相當克制的效能調查。它只讀公開原始碼，明白區分「已證實的風險」與「還沒量的候選」，並且**主動把自己的結論調弱**：因為看到 `Layout.astro` 裡有一條 800ms 的 justfont fallback，所以在信裡寫「故本文不宣稱會無限等待」。

去讀那段程式碼之後，發現他調弱錯了方向。那裡其實有兩道長得很像的閘門：`html { visibility: hidden }` 藏整頁，解除者只有 `document.fonts.ready`；`html.jf-loading > body { opacity: 0 }` 藏 body，解除者是 justfont SDK 或那條 800ms。**它們管的是不同的 class，那條 fallback 接不住藏整頁的那一道。** 藏整頁的那道沒有逾時、沒有 `.catch()`、JS 關掉時也沒有任何東西會解除它。字型檔只要慢或不回應，`fonts.ready` 就永遠 pending。

用 playwright 把字型檔請求掛住不回應（不 fulfill 也不 abort），對正式站量瀏覽器真的算出來的 computed style：`/` 與 `/about/` 都是 `visibility=hidden`、可見字數 **0**。那不是會被放大的風險，那就是空白，而且不會結束。

`3f44f4388` 給這道閘門三條出口：800ms 逾時（刻意跟 justfont 那條共用同一個數字，不留兩套會各自漂移的逾時）、promise 的 `.catch()`、以及 `<noscript>` 直接解除（JS 關掉時整站原本也是空白，順手一起補）。字型用 `display=swap`，逾時揭開時本來就有 fallback 字可讀。

同一個 commit 造了 `scripts/tools/check-font-gate.mjs`，接在 deploy 之後直接打正式站做同樣的量測。這個 bug 能活四個月，是因為既有 workflow 全綠。它們量的是 build 成不成功，沒有一條在問「讀者看不看得到字」。

**過程中被自己絆了兩次，兩次都是靠看 control 組才發現。** 第一版驗證腳本用 `route.abort()` 擋字型，對正式站跑出全綠，因為 abort 讓請求快速失敗，字型進入 error 狀態、載入結束，`fonts.ready` 照樣 resolve。「拿不到」有快速失敗與永不回應兩種，而這個 bug 的成因恰好是後者。改成掛住才立刻紅。第二次是本機 A/B：把正式站 HTML 抓下來只換閘門那段 script，兩邊都綠，因為 `visibility: hidden` 住在 `/_astro/*.css`，本機 serve 時 404，閘門根本沒載進來。補上 `<base href>` 之後 control 紅、fixed 綠（可見字數 0 → 16819），A/B 才真的成立。

回覆 #1666 時把這條差異寫給回報者，並明說首頁重量、850KB 搜尋索引、第三方腳本三項**沒有動**，理由跟他自己寫的一樣：沒有 waterfall 證明它們阻塞首屏，量測之前不動刀。issue 已 close。

## 四個投稿收進來

tboydar 的兩篇德文譯文（#1663 葉丙成、#1664 何飛鵬）四道主權保真閘門全綠，直接 merge。這兩篇值得記一筆的地方是它們**從 zh SSOT 投影而不是照搬既有 en 版**，`translatedFrom` 與三個 hash 都填齊。沒有這幾欄的譯文，zh 更新後我們不會知道它過期。德文版來到 76 篇。

idlccp1984 的 #1667〈陳思宏〉敗在 `frontmatter-gate`（缺 `subcategory` / `featured`，加上全形分號 17 > 12 硬門檻）。這是格式債且 `maintainerCanModify` 為 true，走 §1b P1：直接把修補推進他的分支。推法上用 git plumbing 造 commit（`hash-object` → `read-tree` → `write-tree` → `commit-tree`，走獨立的 `GIT_INDEX_FILE`），完全不 checkout、不動主工作樹。contents API 對 fork 回 404，而 checkout 對方分支會把整套檢查器一起換掉。`0e123844a` 只動格式：補三個欄位、分號降到 9、移掉一行重複的圖說（那行還帶一個站上不存在的 `#user-content-fn-1` 錨點）。散文一字未動。CI 轉綠後 merge。

#1665〈阿貴動畫〉frontmatter 一次到位、`ci-deploy` 直接過。merge 後在 `8730173b1` 動了一件事：文章裡三張圖是台北街景與兩張高雄港，圖說自己寫著「作為網路內容基礎設施的台灣情境圖」，也就是為了湊媒體密度而放的填充圖。換成一條用文章自己腳註事實做的 `tw-timeline`。**換完之後圖片歸零，媒體密度的警告反而更大聲，那個警告我留著**：它現在指的是這篇真正缺的東西，而不是被三張風景照蓋掉。同一個 commit 給〈陳思宏〉補了四條站內延伸閱讀。

#1630〈陳士駿〉維持 open。它跟 #1450、#1483 綁在 OBSERVER-QUEUE #33 同一次拍板上（投稿者能不能整篇覆寫既有條目），不是我能單獨開先例的事。

## 一句活了四個月的引語

審 #1630 時跑 Step 3.4 footnote audit，抽驗它的 Sequoia 引語，逐字稿對得上、翻譯也忠實。但同一支 URL 上的另一句對不上：「幾台電腦，一張信用卡——我的信用卡——就把系統建起來了」在那份逐字稿裡**不存在**。

往上追才發現 defect 不在 PR 裡，在 main 上：站上現行版本本來就有這句話，腳註掛「新浪財經」而且沒有 URL。#1630 做的事是把它改掛到一個真實、點得進去、主題也相關的 Sequoia 頁面。**在每一個機械指標上這都是進步**（URL 從無到有、`footnote-url` 從 warn 轉 pass），實際上是把查不到出處的引語包裝成查得到的樣子，而且更難被抓到。沒有 URL 的腳註會讓人起疑，有 URL 的會讓人以為已經有人查過了。

信用卡這件事本身是真的，只是原話不長那樣。Startup Grind 的訪談裡陳士駿自己說的是「我們是自己出錢的，被收購前我每個月都刷到信用卡額度上限」，後面還補了發現可以一個月多還幾次款來刷到兩三倍。`5478954ba` 把 zh 與 en 換成這一句、附上真的能點的來源，其餘十一語因 zh body hash 改變轉 stale，交給 babel 重譯。

**這裡也差點寫錯一個結論。** 改完 zh 之後跑 `status.py` 檢查十二語是否轉 stale，只有 ja 與 de 亮——當下的解讀是「staleness 偵測有洞」，正要寫進報告才想到還沒 commit，而 status.py 比對的是已提交狀態。commit 之後重跑，十二語全部轉 stale。差一步就把一個自己造成的假象寫成儀器的缺陷。

## 收官 checklist

| 檢查項                       | 狀態                                                      |
| ---------------------------- | --------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                        |
| Timestamp 精確               | ✅ 全部取自 `git log %ai`                                 |
| Handoff 三態已審視           | ✅                                                        |
| CONSCIOUSNESS 反映最新狀態   | ✅ 免疫 59 黃燈未動，非本 cycle scope                     |
| 自我檢查工具 PASS            | ✅ 兩篇文章 `ci-deploy` hard=0，pre-push 全站 mirror 全綠 |

### Quality gate（MAINTAINER Stage 4.1，7 條）

| 指標                                   | 狀態                                                             |
| -------------------------------------- | ---------------------------------------------------------------- |
| open issues 都有 status label/assignee | ⚠️ #1666 已 close，餘 4 條皆已有 label 或在 OBSERVER-QUEUE 掛號  |
| open PRs ≤ 5d age 都有 review comment  | ✅ 今天進來的四個全部處理並回覆                                  |
| broken-link ratio < 7%                 | ✅ pre-push 全站 article-health mirror 全綠                      |
| build green                            | ✅ main 上五條 workflow 最新一次全 success                       |
| BECOME ACK 一行記憶體頂                | ✅                                                               |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ 不適用，本 cycle 有 4 個 fresh PR + 1 個 fresh issue，vc 歸零 |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ #1666 追到根因、修掉、補閘門、close（`3f44f4388`）            |

## Handoff 三態

繼承（來自 `2026-09-04-070817-twmd-feedback-triage`）：

- [ ] 指控信第十八次已攔下，OBSERVER-QUEUE #28 兩件仍待哲宇拍板
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤（本 cycle 未動）
- [ ] LESSONS `clip-that-causes-the-bug-also-silences-the-detector` / `ratio-gate-cannot-surface-a-small-structured-family` 候選修法
- [ ] 1,080 篇有腳註卻沒有參考段落，`format-structure` 目前只 warn，>50 檔命中 §自主權邊界未動手
- ⏳ blocked — #1641/#1643 若 OBSERVER-QUEUE #33 收 #1630 會同時變 stale
- [ ] pending（給 self-evolve）— D+14/D+30 milestone 缺口：是否建立顯性追蹤待評估
- ⏳ blocked — OBSERVER-QUEUE #33/#36 等哲宇對「投稿者能否整篇覆寫既有條目」與「要不要開 `/exams/` 區段」給方向
- [ ] pending — main 紅燈沒有不依賴人的出口，候選是把 red-on-main 寫進 `dashboard-alerts.json`
- [ ] pending（給 self-evolve / distill）— ANATOMY §資源地圖 缺「驗證引擎」那一格
- [ ] pending — `--header-h` 一份真值兩個消費者，沒有東西阻止第四份硬編碼副本長出來
- [ ] pending — 下一個 harvest milestone 是 2026-09-06（#175/176「用語保存副詞層」D+14）

本 session 新增：

- [x] ~~#1663 / #1664 德文譯文 merge + 致謝~~
- [x] ~~#1667 走 P1 推格式修補進投稿者分支 → CI 綠 → merge + heal 延伸閱讀~~
- [x] ~~#1665 merge + 換掉三張填充圖~~
- [x] ~~#1666 追根因、修 Layout.astro 字型閘門、造 `check-font-gate.mjs` 接進 deploy、close~~
- [x] ~~陳士駿信用卡引語 zh + en 換成可查證來源~~
- [ ] pending — `check-font-gate.mjs` 的 CI job 是這輪新加的，**下一次 deploy 才會第一次真的跑**。下個 cycle 要去確認它在 GitHub runner 上真的綠（playwright chromium 安裝、正式站可達性都還沒在 CI 環境驗過），不要假設本機綠等於 CI 綠。
- [ ] pending — 陳士駿其餘十一語已轉 stale，等 babel 重譯。下個 cycle 抽驗一語，確認新的引語真的被翻進去、舊的沒有殘留。
- [ ] pending（給 self-evolve / distill）— 本輪兩條 LESSONS：`sibling-fallback-reads-as-coverage-for-the-gate-next-door`（隔壁閘門的 fallback 被讀成兩道共用）與 `adding-a-live-url-to-an-unverifiable-quote-looks-like-an-upgrade`（腳註補 URL 在所有機械指標上都是進步）。後者的修補候選 (b) 是一支 `quote-source-match.py`，值得評估。
- ⏳ blocked — #1630 仍等 OBSERVER-QUEUE #33 拍板。本輪已把它的腳註問題查清並修在 main，拍板時的資訊是最新的。

## Beat 5 — 反芻

今天三次差點把假象當結論，三次都是同一種形狀：**我量到的東西不等於我以為我量到的東西**。用 abort 模擬字型拿不到（量到的是快速失敗，不是永不回應）、本機 A/B 沒載到閘門的 CSS（量到的是一個沒有閘門的頁面）、改完 zh 沒 commit 就查 stale（量到的是提交狀態，不是工作樹）。三次都靠順手看了一眼「應該要紅的那一組」才發現，沒有一次是被閘門接住的。

A/B 的 control 組不是禮貌性的對照，它是**唯一能證明這支尺有沒有在量東西**的部分。如果我只跑了 fixed 組看到綠色就收工，今天會 ship 一個沒有被驗證過的修補，外加一支永遠不會紅的 CI 閘門——而那支閘門會讓後來的人更放心。造一道量不到東西的閘門，比沒有閘門更糟。

回報者那邊還有一件事值得記下來，跟這個 bug 本身一樣重要。idlccp1984 因為看到隔壁那條 800ms 的 fallback，主動把自己的指控寫弱了——他有能力發現這個 bug，卻被一段長得很像保險的程式碼說服自己講小聲一點。**接住這件事的是有人願意讀完程式碼，再決定要不要相信註解。** 兩條教訓已進 LESSONS-INBOX，不在這裡展開。

🧬

---

_v1.0 | 2026-09-04 09:13 +0800_
_session twmd-maintainer-am — 每日 maintainer cycle，Stage 1 掃到 8 個 ready PR 強制升 Full mode_
_誕生原因：cron 觸發的日常維護，撞上一個讀者回報的效能問題，追下去是整站層級的可見性缺陷_
_核心洞察：(1) 兩道長得像一對的閘門，其中一道有 fallback，會讓人以為另一道也有——回報者因此把自己的結論寫弱了 (2) 模擬外部依賴失效時，「快速失敗」與「永不回應」是兩種根因，用錯的那種會拿到一張證明沒有 bug 的綠燈 (3) 腳註從沒有 URL 升級成有 URL，在每個機械指標上都是進步，即使那個 URL 裡沒有那句話_
_LESSONS-INBOX 候選：sibling-fallback-reads-as-coverage-for-the-gate-next-door / adding-a-live-url-to-an-unverifiable-quote-looks-like-an-upgrade（兩條均已 append）_
