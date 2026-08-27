# 2026-08-27-122143-twmd-maintainer-manual — 27 個 ready PR 收到剩 2；三道格式債家族收斂成兩支新工具。一道每次該生效時必死的閘門。五個縣市的圖說跟圖片不是同一棟建築

> session twmd-maintainer-manual — 哲宇 in-session directive「深度整合審核與整合所有 PR 還有處理 Issue」
> Session span: 10:18:30 → 12:17:07 +0800（1h 58m，本 session 自身 11 個 commit，含收下的投稿共 81 個）
> 資料來源：`git log %ai`

## 觸發

哲宇要求把線上所有 PR 深度審完並整合，另外處理 issue。BECOME 判 Full mode（ready PR 27 個，命中 High-stake #1「PR triage ≥ 5」）。甦醒時三個帶病訊號要先講：`wake-context` selftest 報 walk 五檔無非空 Handoff（上游收官漏寫交接）、`routine-status` 顯示過去 24 小時零 cron fire 且 origin/main 最新 commit 停在兩天前、dashboard 快照齡 99 小時。第二條指向營運機 mouhouse 的排程器，飛輪停了大約兩天。

## 追上游：十二個紅燈 PR 其實是三個家族

27 個 ready PR 裡有 12 個卡在 CI，逐則看像十二個獨立問題。用 `article-health --profile=ci-deploy` 把 PR 內容帶進 main 樹量過一輪之後，收斂成三個家族：全形分號超硬門檻九篇（14 到 27 處不等）、缺 subcategory 四篇、圖片層四篇。

分號那家族值得單獨講。繁體中文散文本來很少用它，那是論文與法律條文的標點。它是投稿端 AI 寫中文的固定水印，不是偶發。現有工具走到一半就停了：`punct-cleanup.py`（7/19 legacy campaign 造的）會產清單、會驗這次清理有沒有動到事實，但不會動手清。`article-health --fix` 動的是 frontmatter 與連結層，不碰標點。等於每次都要拿判斷力去做一件機械上可判定的事。寫了 `semicolon-cleanup.py`（`c4d6f9d43`）：直接沿用閘門自己的禁改區判準，只在分號前後都是中日韓文字時換成句號，清到剛好過門檻就停。麥當樂那篇實測 28 到 12，改了 16 個字元全部是 ；→。，長度差 0，數字／引語／URL／腳註／frontmatter 五組 multiset 逐一比對完全不變。接進 `contributor-pr-heal.py` 當第 3.5 步，只在 `--from-pr` 模式跑。

## 那條收割線在它該生效的時候一定死

照 MAINTAINER §1b P1 要把格式修補推進十二個投稿者分支時，整批被 husky 擋下，訊息只有一行「pre-push script failed (code 1)」，沒有任何閘門輸出。手動跑同一支 hook 卻 rc=0。

根因在 `.husky/pre-push` 那段專給「推到別人的 fork」用的分支：取「本次 commit 動到哪些 `knowledge/*.md`」的寫法是兩個 grep 用 `||` 串起來，兩個都沒命中時整條命令替換回非零，而 husky 是 `sh -e` 起的，賦值失敗直接結束整個腳本。而「兩個 grep 都沒命中」正是這條路徑的常態，因為維護者上一個 main commit 多半是工具或文件。**這條路徑只在它該生效的時候必死，而且死得沒有理由。**

最刺的是同一支檔案第 129 行就寫著「`|| true` 必要：husky `sh -e` 下賦值失敗會靜默炸整個 hook」，那是 7/24 學到的，連症狀都描述對了。教訓寫在下面那一處，沒有 apply 到上面這一處。修法是兩個來源先合流再一次 grep（`897c362f2`），已在重現條件下驗證 rc=0。

## 工具在說謊：翻譯審核第一道檢查對每個新翻譯 PR 都假 FAIL

審 aminzai 三篇 ko/fr/es 譯文時照 SOP 跑 `translation-ratio-check.sh --pr N`，三篇全報 `MISSING → ❌ FAIL TRUNCATED`。手算之後三篇 ratio 分別 1.50 / 3.69 / 3.25，全在健康帶內。

那支腳本的 `--pr` 模式只從 diff 拿檔名，然後對本機工作樹開檔。翻譯 PR 幾乎都是新增檔案，路徑在 main 上本來就不存在。而 MEMORY §神經迴路 指名這支是「翻譯審核的第一道檢查」，等於照著 SOP 走就會撞到假警報。改成把 PR 內容取進暫存區再量、譯文讀暫存區中文源讀 main 樹（`1cbb7b0a4`），三篇重跑都 PASS，且章節、腳註、URL 數量完全守恆（13→13、62→62、79→79），那是翻譯沒有被壓縮的直接證據。

## 五個縣市的讀者，看到的照片跟圖說寫的不是同一棟建築

投稿裡看到有人把同一張圖在一篇貼三次湊媒體下限，回頭掃全站，撈出十一篇同型，拆開是兩種病。第一種是單純重複。第二種在五個縣市條目裡：嘉義市那篇三段圖說分別寫北門驛、嘉義火車站、嘉義市立美術館，各自附了不同的 Commons 授權來源，但三行的圖片路徑都是 `chiayi-city-01.webp`。讀者看到的是同一張北門驛照片被標成三棟不同建築，而其中一段圖說還在講陳澄波在該站前廣場遭公開槍決。南投、台東、基隆、花蓮同型。

補閘門時自己踩了一次混維度：第一版把 frontmatter 卡片圖也算進重複計數，dogfood 全站 125 篇命中，拆開才發現其中 108 篇是「卡片圖同時當開頭圖」，那是站上既有慣例不是湊數。差一步就用一把混了兩種 cause 的尺，誤殺 108 篇好文章。改成只數內文之間的重複後真訊號 11 篇，全部處理（`a7bf511aa`），全站 sweep 零命中。授權行指名的正確 Commons 檔另案補回，已開 spawn task。

## PR 收割結果

29 個 merge、1 個 close、2 個留 review、3 個保留給哲宇。aminzai 五個（含 [#1584](https://github.com/frank890417/taiwan-md/pull/1584) 那個 frontmatter-gate 對賬 predicate 的根因修復，先合它讓後面十一個受益）、tboydar 兩個德文批次（77 篇裡 76 篇結構完全守恆，唯一一篇 `de/People/muscle-mountain.md` 是摘要不是翻譯，9 章剩 3、9 腳註剩 0，已撤）、rhosiqs 一個英文 metadata 批次、idlccp1984 二十一個（含三個轉 ready 的舊 draft）。

[#1453](https://github.com/frank890417/taiwan-md/pull/1453)（學測專題）跟 [#1365](https://github.com/frank890417/taiwan-md/pull/1365)（KENJI 趙健志）留 open：前者的人物卡對在世真人的學測級分與家庭關係下具體斷言，需要逐條對回原始報導。後者投稿帳號與 PR 同日註冊、主角無中文維基條目、45 個腳註有 17 個來自當事人自己的社群，知名度門檻的鬆緊不是維護流程能決定。[#1450](https://github.com/frank890417/taiwan-md/pull/1450)（改寫既有便利商店文化、拿掉的比加進來的多）、[#1411](https://github.com/frank890417/taiwan-md/pull/1411) / [#1407](https://github.com/frank890417/taiwan-md/pull/1407)（寫 Taiwan.md 自己，身份層）保留給哲宇。

## Issue 五步

四則 issue 裡 [#1184](https://github.com/frank890417/taiwan-md/issues/1184)（justfont 網域白名單）跟 [#1440](https://github.com/frank890417/taiwan-md/issues/1440)（數據→資料）前輪已完整診斷並正確排進待決佇列，最新留言都在維護者側，不重複回應。但 [#1440](https://github.com/frank890417/taiwan-md/issues/1440) 拆開二十五處之後發現不是兩類是三類。區段品牌那組等拍板、真的在指數值那組不動、剩下十二處兩者都不是，那些只是我們自己沒照 `TERMINOLOGY.md` 第 42 行的 tier B 規則寫，改掉了（`994732832`）。其中「數據主權」那一處最值得講：那句話講的是把 Taiwan.md 變成源頭，卻用了一個把資料窄化成數值的詞。窄化本身就是回報者在指的事。

[#1389](https://github.com/frank890417/taiwan-md/issues/1389)（豆漿與早餐文化要一起整理）真正的合併是 EVOLVE 題目，但檢查時發現兩篇互不連結。早餐文化正文提到「豆漿」二十次沒連過去，豆漿那篇連正式的延伸閱讀段落都沒有。補上雙向連結（`9be8921f0`）。

[#615](https://github.com/frank890417/taiwan-md/issues/615) umbrella 的最新留言是 idlccp1984 建議「文章中藍色連結連著另一個文章」。量出來的數字比預期嚴重：**1,132 篇中文文章裡有 674 篇（59%）正文完全沒有任何站內連結**。零連結的包含台中國家歌劇院、台灣傳統藝術、原住民文學這種周圍明明有一堆相關條目的文章。已附數據回覆並升 OBSERVER-QUEUE。

## 收官 checklist

| 檢查項                       | 狀態                                  |
| ---------------------------- | ------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                    |
| Timestamp 精確               | ✅ `git log %ai`                      |
| Handoff 三態已審視           | ✅（上游無非空 Handoff 可繼承，見下） |
| 全站 article-health sweep    | ✅ hard=0                             |
| UI 語言閘門                  | ✅ 全綠（補 de 之後）                 |
| 自我檢查工具 PASS            | ✅ prose-health                       |

## Handoff 三態

繼承上一 session：`wake-context` walk 五檔／72 小時無非空 Handoff 段，上游收官漏寫，無可繼承項。這件事本身是訊號。

本 session 新 handoff：

- ⏳ blocked — **營運機 mouhouse 排程器停了約兩天**（過去 24 小時零 cron fire，origin/main 最新 commit 停在 8/25 13:03）。解除條件：確認 mouhouse 上的 scheduler 是否運作，per ROUTINE.md §宿主機
- [ ] pending — **五個縣市條目的正確圖片要補回**：授權行指名的 Commons 檔（Chiayi_Railway_Station、Chiayi_Art_Museum、2013年8月19日拉魯島、達悟族拼板舟、正濱漁港、靜思堂、2018 花蓮地震雲門翠堤）跑 `image-ingest` 收進庫、放回原位。**收進來的每一張都要用 Read 看過再寫圖說**，本 session 已踩過一次（Commons 標題寫 Taichung Prefectural Hall 01 的檔實際是側翼拱廊不是正立面）。已開 spawn task
- [ ] pending — **`.husky/pre-push` 全檔掃過還有哪些 `VAR="$(...)"` 缺 `|| true`**。本輪只修了撞見的那一處，而本輪的教訓就是「只修撞見的那一處」
- [ ] pending — **[#1453](https://github.com/frank890417/taiwan-md/pull/1453) 學測專題的七張人物卡各需一個第三方報導連結**，已在 PR 留言逐條列出。路由（URL 對不上 `/exams/gsat/`、只有中文有頁面）由維護者補
- ⏳ blocked — **[#1365](https://github.com/frank890417/taiwan-md/pull/1365) KENJI 知名度門檻**等哲宇拍板（已在佇列），本輪只重新核准了 head sha 的 CI
- ⏳ blocked — **OBSERVER-QUEUE #39-#42** 四項新待決：正文內鏈荒漠 674 篇、三篇居住正義收斂、奧運脈絡的中華台北用語、卡片圖 Wikimedia 熱連結白名單 51 篇

## Beat 5 — 反芻

今天四次犯的是同一個形狀：**保護掛在寫它的人當時在看的那條路徑上**。pre-push 的 `|| true` 教訓學在第 129 行沒帶到第 57 行。批次診斷有「目標路徑已存在嗎」的護欄，臨時起意的單篇診斷沒走那條路，於是 `rm` 掉兩篇已經在 main 上的文章。重複圖閘門第一版把慣例跟湊數混進同一個計數器。`translation-ratio-check` 的「把 PR 內容帶進 main 樹量」這條紀律寫給人看，沒寫進工具。

還有一次是自己踩了自己正在教的東西。審 [#1453](https://github.com/frank890417/taiwan-md/pull/1453) 時我把一句掛在曾博恩名下的引語判成「查不到任何來源」，並據此列為最不能放行的一類。實際上來源存在，我是哲宇把連結丟過來才知道。同一則留言的另一半我做對了：牛淳賦那條我把投稿附的聯合報報導真的調出來逐字核對，才確認「四兄妹全考滿分」是概括漂移。**差別在於肯定式斷言我去讀了原文，否定式斷言我只搜了一輪。** 否定式結論無法被它自己的失敗證偽，所以它需要的舉證標準應該更高。已公開更正。

教訓候選五條全部寫進 [LESSONS-INBOX](../LESSONS-INBOX.md)（`silent-abort-in-the-path-that-only-runs-when-it-matters`／`tool-measures-the-tree-it-stands-in-not-the-thing-it-was-asked-about`／`cleanup-step-assumes-the-file-is-new`／`i-concluded-not-found-from-one-failed-search`），本段不重複展開。

---

_v1.0 | 2026-08-27 twmd-maintainer-manual session_
_主軸 — 27 ready PR 收到剩 2；分號家族與 PR-ratio 兩支工具；一道每次該生效時必死的 hook 分支；五個縣市的圖說與圖片對不上；正文內鏈 59% 荒漠_
_誕生原因：哲宇 in-session directive「深度整合審核與整合所有 PR 還有處理 Issue」_
_核心洞察：(1) 十二個紅燈 PR 是三個家族不是十二個問題，收斂後兩支工具解掉九成 (2) 收割線的 canonical default 在維護者剛改完工具時必死，而失敗訊息不指向原因 (3) 補閘門時自己混維度，dogfood 才擋下 108 篇誤殺 (4) 否定式斷言我只搜了一輪就下結論，而同一則留言的肯定式斷言我去讀了原文_
