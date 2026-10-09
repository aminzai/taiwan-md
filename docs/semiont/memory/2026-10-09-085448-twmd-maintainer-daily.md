---
title: '2026-10-09-085448-twmd-maintainer-daily'
description: '九個 ready PR 升 Full、昨天上線的稽核工具讀錯真紅、德文兩份譯本同時在線、政治迷因投稿進待決'
type: 'session-log'
status: 'log'
apoptosis: 'never'
current_version: 'v1.0'
last_updated: 2026-10-09
---

# 2026-10-09-085448-twmd-maintainer-daily — 昨天上線的尺讀錯第一個真紅／〈楊德昌〉德文兩份譯本同時服務／七條週班沒回來是週期不是故障

> session twmd-maintainer-daily — cron 排程（am 08:30）
> Session span: 08:30 → 09:09:03 +0800（約 39 分鐘，4 commits）
> 資料來源：`git log %ai` + `gh pr/issue/run list` + `scripts/tools/{consciousness-snapshot,ci-main-health,npm-audit-sweep,pr-ci-armed,routine-status,verify_internal_links,check-slug-consistency,budget-pace}` + `get_usage`

✅ BECOME ack: mode=review→**FULL**（high-stake #1：9 ready PR ≥ 5）/ 8 organ 最低=🛡️60 免疫（即時 `consciousness-snapshot.sh`）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer 班。`gh pr list` 回九個 ready PR（0 draft），命中 BECOME §Step 0 high-stake #1「PR triage ≥ 5」，所以 review mode 當場升 Full，補載 ANATOMY／DNA／HEARTBEAT／UNKNOWNS／LONGINGS／OBSERVER-QUEUE §待決 全 39 列之後才進 Stage 1。

本班刻意沒全載的兩份：`ARTICLE-INBOX`（2,695 行）與 `SPORE-INBOX`（1,315 行）。它們是寫文與孢子的 intake buffer，對 PR triage 不載重。`inbox-signal.sh` 的 count 已在 groundtruth，需要查重時 grep-on-demand。LESSONS 讀的是 98 條未消化標題而非全文。寫在這裡是因為「評估後決定不做」要寫明理由，沉默地沒讀不算。

## 七個 PR 被擋在同一格紅燈，而那一格有人等著

分岔檢查 `0 0`（無分岔，Stage 1.1b 不觸發）。`ci-main-health.sh` 13 條 workflow 裡 **Engineering contracts 紅著**，齡 2 小時。九個 PR 全部 ARMED（CI 真的跑過，不是零檢查），逐篇看 check rollup：七篇（#1791／#1793／#1794／#1795／#1797／#1799／#1800）**只有 `contracts` 一條紅**，其餘全綠——正是 OBSERVER-QUEUE #94 列的那七篇，紅的原因在庫外，他們只是路過的人。

Step 3.0 的 v2.16 子規則（授權住在對話裡）在這裡救了一次：九篇逐篇抓留言串，#1797 有一則 10-08 01:14 的批次回覆，裡面寫著 **「不要為了讓 CI 轉綠而去動你的分支⋯⋯等 #94 那格落地之後我會統一重開這七個 PR」**。那是前一班對投稿者的公開承諾，只存在於留言串裡，檔案層完全看不到。所以本班不碰那七篇、不 admin override——#94 是 🔒 等真人、到期 10-22，而 stantheman0128 已經被告知不要動手。#1798 CONFLICTING（56 檔）也在同一則留言裡交代過處置順序（先收 #1797 的檢查器再重跑 `--fix`），他不需要手動解衝突，本班同樣不碰。

## 昨天上線的那支尺，讀錯了它上線要讀的第一個真紅

`npm-audit-sweep.sh` 是 10-08 本班照 LESSONS `external-advisory-reddens-a-gate…`（vc=3）做的機械化，當天 13 個 pytest ＋三個正控制全綠。今天它報 `harvest/ui` 五條 high，其中 `fast-glob` 標 **`fix=minor`**，總結於是印「剩下的在小版本內修得掉」並叫下一班跑 `npm audit fix --package-lock-only`。

那個指令對這五條零改動。實測跑完 lockfile 一個字沒變，npm 自己說的是 `fix available via npm audit fix --force / Will install tailwindcss@4.3.3, which is a breaking change`。病根在把 npm 的裸 `fixAvailable: true` 當成「在小版本內修得掉」：npm 把 `isSemVerMajor` 放在真正要動的那個祖先上，傳遞依賴只拿到裸 true——`fast-glob` 的 `via` 指向 `micromatch`，後者回 `{tailwindcss@4.3.3, isSemVerMajor: true}`。修在 `6de1f2ebe`：裸 true 先沿 `via` 走一遍，找到 major 祖先就繼承判定並計入 blocked，五條現在全印 MAJOR、誤導那行消失，720 passed。

這同時**獨立核過 #94 的判斷**：3.x 真的沒有任何版本收得掉，唯一修法仍是升 tailwindcss 4。那一格的結論沒變，變的是通往它的尺不再自相矛盾。昨天的正控制沒抓到，是因為 fixture 全是手寫的單層公告、沒有一個帶傳遞鏈。

## 〈楊德昌〉在德文有兩份譯本，兩個網址都在服務

昨天合併 PR #1801 之後德文比其他語言多一篇，交接把它傳過來。查下去是 `de/People/edward-yang.md`（tboydar，09-09）與 `de/People/yang-dechang.md`（aminzai，10-07）兩個檔的 `translatedFrom` 都指向 `People/楊德昌.md`，而且**兩個網址實測各回 200**。

動手前先量全庫：十二語、13,554 組（語言 × 來源）配對裡只有這一組重複，是單例不是家族。保留哪一份兩把尺同向。`yang-dechang` 是 en 與其餘十二語共用的 slug（slug 一致性的 SSOT 就是對齊 en），而 `cjk-residue-check` 對 aminzai 那份回 0 行、對 tboydar 那份回 1 行（腳註 `[^11]` 的「500輯」沒譯出）。其餘四把尺兩份都一樣乾淨。所以退役 `edward-yang`、補 301（那條路徑從 09-09 就在線上），`58392ee24`。

查完才看到的一層：其他十二語頁面的 `hreflang="de"` **全部指向我剛退役的那個 duplicate**。下次 build 會重生成指到唯一的那個 de 檔，期間由 301 接住。也就是說這個重複不只是多一個網址，它還是十二語的 de 替代連結實際指過去的那一個。

`check-slug-consistency.py --all` 在這件事上今天照印全綠：它問「該在的 slug 在不在」，不問「同一個語言同一個來源有幾個檔」。真正叫出來的是每日刷新的逐語言篇數落差。

## 政治迷因投稿：機械面四行可解，要決的是另一件事

PR #1802（idlccp1984）〈來來來，怎麼樣、怎麼樣〉。按診斷紀律把內容檔帶進 main 樹用 main 的檢查器量，不 checkout PR 分支。單一 hard 是 frontmatter 整塊被 ` ```yaml ` 圍籬包住、不是 `---`。照那樣合併 Astro 不會建路由，那段 YAML 會變成文章頂端一塊灰色程式碼區塊，兩個 CI 紅燈同源。把圍籬換掉之後 hard 從 1 變 3（露出缺 `category`／`subcategory`），四行補完實測 `hard=0 passed=True`。

腳註逐條點過：八條非 Threads 網址全 200，但 `[^6]` 中選會那頁的 HTML 裡找不到它引的三個票數，`[^8]` 報導者那頁寫的是 25＋7＝32、沒有「33」也沒提 7/13 南投案。而「33」本身站得住。南投縣議員陳玉鈴 2025-07-13 投票、未過門檻，另外查到的。所以那是**來源撐不住句子**不是算錯，講法差很多，寫進留言前先查清楚這件事值得。

內容的查證紀律比多數投稿好：它一路把可查證紀錄、政治人物自述、社群說法分三層講，明寫起源缺少可獨立核對的原始影音。要決的是另一件事。主角是現任立法委員、最後一段發生在上週，而標題把起源寫成「從王鴻薇的挑釁動作」，正好是正文刻意不下定論的那一點。政治立場與策展門檻是四紅線之二，缺席模式也不代理。掛 `reserved-for-observer`、PR 不關、留言只給技術事實與既有六個 subcategory 值、不承諾時程，選項與成本進 OBSERVER-QUEUE #96。

順手修掉投稿者撞上的那個陷阱：閘門叫他去對 `SUBCATEGORY.md`，而那份檔案沒有 Politics 這一節（`allowed_subcategories('Politics')` 回空陣列），所以照訊息查是查不到答案的。訊息改成 SSOT 沒收該分類時改指既有文章的值並附一行跑得動的指令（`f2b11a541`）。正典補不補是編輯層決定，沒代做。

## 七條週班沒回來是週期，不是故障

交接鏈掛著一個沒人核過的問題：額度黑完之後日班全回來、週班一條都沒回來，這個不對稱是什麼。把 `ROUTINE.md` §排程表跟日曆對一次就結束了。今天 10-09（四），五條週日班的下次 fire 是 **10-11**，supporters 是 10-12，terminology-trends 是 11-05。**10-05 到 10-11 之間這七條沒有任何一次排定的 fire**。日班每天來一次所以 10-08 早上就全現身，週班一週來一次而那一次落在停擺窗口裡。兩把尺都只量「距上次應 fire 多久」、不量「下次什麼時候」，所以週期差會長得像故障。

另外自己讀了 live 狀態確認七條 `enabled=True`（只有 founder-lens 是 False，那是 7/26 哲宇刻意停的），沒有只靠另一班的回報。

比「它們還在不在」更實際的那一格：今天額度 36%、推估約 65.6 小時後用完（約 10-12 02:30）。週日 01:00–21:00 那五條都落在耗盡之前，最晚的 routine-audit 還有約五個半小時餘裕。而 **supporters（10-12 01:00）距推估耗盡只剩約一個半小時**，週日五條有四條是 Opus、跑完會把速度往上推，所以那一條很可能再漏一次。寫進 #1788 讓 10-11 那趟自己回答。

## 收官 checklist

| 檢查項                          | 狀態                                                       |
| ------------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄    | ✅                                                         |
| Timestamp 精確（`git log %ai`） | ✅                                                         |
| Handoff 三態已審視              | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態      | ⏭️ 本班未改器官分數（derived 層，refresh 每日重生）        |
| 自我檢查工具 PASS               | ✅ 720 passed / 8 skipped。`observer-queue-lint` 40 列全綠 |

## 品質閘門七條

| 閘門                                             | 結果                                                                                   |
| ------------------------------------------------ | -------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee         | ✅ 六條：#1790／#1789／#1786／#1609 已 assign，#1788 帶 `routine-stall`，#615 umbrella |
| open PRs ≤ 5d age 都有 review comment            | ✅ 九篇都有（七篇 10-08 批次回覆、#1802 本班、#1798 同批次回覆內交代）                 |
| broken-link gated ratio < gate                   | ✅ 0.15% < 7.0%（all-langs 0.14%）。**但 dist 齡 23.3h，不含本班改動**，見下方交接     |
| build green                                      | ⚠️ deploy GREEN，**Engineering contracts RED**（#94 🔒，非本班可解）                   |
| BECOME ACK 一行記憶體頂                          | ✅                                                                                     |
| 連續空場 ≥ 3 cycle 有 LESSONS entry              | ⏭️ 不適用：本班有真 backlog（9 ready PR + 一個合併後的資料缺陷），vc 歸零              |
| 有 fresh issue 的 cycle 至少一件被修掉或寫明不修 | ✅ 無新 issue。#1788 的未決問題核掉並落檔                                              |

## Handoff 三態

繼承 `2026-10-09-071619-twmd-feedback-triage`：

- `[x]` ~~pending（本班）：〈楊德昌〉德文兩份譯本（PR #1801）~~ → retired by 本班，`58392ee24`（退役 `edward-yang`＋301，重複 1 → 0）
- `[x]` ~~pending（本班）：404 同語言前綴雙寫家族~~ → retired by 本班：19,321 個 dist HTML 掃過，`/(lang)/(same lang)/` 雙寫前綴 **0 次命中**，證實 data-refresh 的判斷（外部爬蟲拼的，站體不產生），本機無事可修
- `[ ]` pending（延續，收件席位 `/twmd-routine` 或 Full mode）：`git prune`（issue [#1729](https://github.com/frank890417/taiwan-md/issues/1729)）。本班每個 git 指令仍印那四行警告
- `⏳` blocked（延續，哲宇）：`OBSERVER-QUEUE` §待決 **40 列，`#48`〜`#96`**（本班新增 #96，`observer-queue-lint` 全綠；最近到期 `#86` 10-11）
- `⏳` blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly 10-11）：embeddings 改殼隔兩晚生效的三選項
- `[ ]` pending（延續，收件席位 `twmd-self-evolve-weekly` 10-11）：LESSONS `heart-counts-heals-as-contributed-births`
- `[ ]` pending（延續，收件席位 `twmd-distill-weekly`）：LESSONS `threads-linkifier-swallows-cjk-before-url` 與 `narrative-log-fills-causation-no-gate-watches`（vc=2）
- `[ ]` pending（延續，席位 `/twmd-routine`，經 `ROUTINE.md` 下發）：spore-harvest 殼寫死路徑改相對路徑、收官 `git add -u` 改 pathspec（連傳十輪，vc=10）
- `[ ]` pending（延續，收件席位 `/twmd-routine` 或 `twmd-flywheel-watch`）：**週班七條沒回來這條已核完**（見上，是週期不是故障，`enabled=True` 七條皆在），剩下的是額度節律，歸 `OBSERVER-QUEUE #93`

本 session 新 handoff：

- `[ ]` pending（收件席位 `twmd-maintainer-daily` 明天，或任何 Full mode）：**斷鏈 audit 的讀數建立在 23.3 小時前的 dist 上**，不含本班退役的 de 檔。0.15% 這個數字對昨天的站體成立，對今天的不確定。明天那班若 dist 仍 > 24h 會自己 fail-loud 成 STALE。想當天確認就跑 `npm run sync:build`（v2.15 已驗過在 babel 滿載時零碰撞），不要用 `npm run build`
- `[ ]` pending（收件席位 `twmd-maintainer-daily` 或 `twmd-babel-nightly`）：本班退役 de 檔之後，**十二語的 `hreflang="de"` 要在下次 build 重生成**才會指到 `yang-dechang`。推送觸發的 deploy 應該就會做掉。下一班順手 `grep -o 'hreflang="de" href="[^"]*"' dist/ja/people/yang-dechang/index.html` 確認一眼
- `[ ]` pending（收件席位 `twmd-distill-weekly`，vc=1）：LESSONS `checker-counts-presence-not-multiplicity` 的候選機械化，`check-slug-consistency.py` 加一道「每組（語言 × `translatedFrom`）剛好一個檔」斷言。判準機械、零誤判空間、全庫 13,554 組跑幾秒
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #96`）：PR [#1802](https://github.com/frank890417/taiwan-md/pull/1802) 要不要上站。已掛 `reserved-for-observer`、PR 不關、技術事實已給投稿者。**不要照 P0 default 合併它**
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #94`，到期 10-22）：七個投稿 PR 等 contracts 那格紅燈。前一班已公開承諾「#94 落地後統一重開這七個 PR 觸發重跑，你不用重推」。**那個承諾要由收到它的那一班兌現**，不要讓投稿者自己動分支

## Beat 5 — 反芻

今天最值得留下的不是修了什麼，是**昨天的我留下的那支尺今天讀錯了它存在的理由**。`npm-audit-sweep.sh` 是為了「紅燈在哪一道、還有幾道在後面」而造的，13 個測試加三個正控制全綠，而它上線後面對的第一個真紅就被它標成相反的處置。正控制是對的紀律，但 fixture 是作者寫的，所以它繼承作者的盲點——我昨天想得出「真紅／量不到／乾淨」三種情境，想不出「裸 true 其實卡在祖先的 major」這一種，因為那個形狀要等真實資料才會出現。「驗過」的強度上限是 fixture 的真實度，不是測試的條數。

第二件同形狀：`check-slug-consistency.py` 今天對一個兩個網址同時在線的重複印全綠。它問的是存在，而缺陷是多餘。這兩件事放一起看是同一個病。**檢查器問得出來的問題，等於造它的人當時想像得出來的問題**，而這個限制本身不會出現在任何讀數裡。三條教訓已進 LESSONS-INBOX，不在這裡展開。

第三件是收斂的：七條週班「沒回來」這個擔憂在交接鏈裡傳了兩班，核起來只需要把 cron 跟日曆對一次。有些警報不需要修法，需要的是有人去看一眼它在問什麼。而它之所以傳得下來，正是因為它寫得很具體（七條、各自的小時數），具體讓它讀起來像已經被查過了。

🧬

---

_v1.0 | 2026-10-09 09:09 +0800_
_session twmd-maintainer-daily — cron am 08:30，9 ready PR 升 Full mode_
_誕生原因：每日 maintainer 班，九個 ready PR 命中 high-stake #1 強制升 Full_
_核心洞察：昨天上線的稽核尺把唯一需要判斷的那一欄讀反，而它的正控制全綠。正控制的覆蓋面等於作者想像得出的輸入形狀；同日第二例是存在性檢查看不見「多餘」，讓一個雙網址重複印全綠；而交接鏈傳了兩班的週班警報，核法只是把 cron 跟日曆對一次。_
_LESSONS-INBOX 候選（已 append）：positive-controls-only-cover-shapes-the-author-imagined / checker-counts-presence-not-multiplicity / gate-demands-a-value-its-own-reference-cannot-supply_
