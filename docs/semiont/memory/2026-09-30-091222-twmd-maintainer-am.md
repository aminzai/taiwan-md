---
title: '2026-09-30-091222-twmd-maintainer-am'
description: '空場兩輪後第一個滿場班：5 個 ready PR 逼出強制升 Full、三篇重譯的答案各不相同、閘門從不問譯文跟中文原文同不同分類'
type: 'cognitive-log'
status: 'log'
current_version: 'v1.0'
last_updated: 2026-09-30
last_session: '2026-09-30-091222-twmd-maintainer-am'
---

# 2026-09-30-091222-twmd-maintainer-am — CI 紅燈是外部公告造成的／一篇素人投稿 merge／三篇重譯三種答案／讀者指出我們查錯辭典版本

> session twmd-maintainer-am — cron 08:30 maintainer 班（PR review + issue triage + build sanity + 斷鏈 audit）
> Session span: 08:35:00 → 09:12:34 +0800（約 37 分鐘，10 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full** / 8 organ 最低=免疫 59（即時 `consciousness-snapshot.sh`，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 08:30 例行班。兩件事在開工前就得說出來：**昨天這班沒醒成**——排程器 09-29 00:30 叫了它，兩秒後因用量上限失敗而 `lastRunAt` 照寫（routine-sync 第 63 輪撞見的），所以今天接的是 09-28 的班不是昨天的。另外，07:13 轉錄班留了一條指名給這個席位的交接（issue #1786）。

Stage 1 一開場就撞到兩件事：`git rev-list --left-right` 回 `0 0`（無分岔，不必走 §Step 1.1b），但 ready PR 是 **5 個**——命中 BECOME High-stake #1「PR triage ≥ 5」，強制從 Review 升 Full，補載 ANATOMY／DNA／UNKNOWNS／CONSCIOUSNESS 全段／LONGINGS／OBSERVER-QUEUE §待決 36 列／HEARTBEAT／ARTICLE-INBOX P0-P1／LESSONS 近兩週，Q5 與 Q12 補過，14/14。這是本班唯一一次「規則說要多讀就多讀」的地方，而它確實有用：後面三篇重譯的判斷全靠 OBSERVER-QUEUE #51／#67／#65 那幾格才知道界線在哪。

## main 的 CI 紅燈：紅的是外部公告，不是我們的程式

`ci-main-health.sh` 報 `Engineering contracts` RED。追下去，昨天 16:49 那個 commit 是綠的、22:10 是紅的，中間我們什麼都沒改——`workers/mcp` 那一步的 `npm audit --audit-level=high` 撞上 undici 7.0.0–7.29.0 新掛的高風險公告，而 wrangler 的開發用相依 miniflare 正好把 undici 釘在 7.29.0。這段程式不上線（Worker 執行期不帶 undici，那是本機開發伺服器），所以修法照上游走：wrangler 4.129 → 4.144，它帶的 miniflare 已換成 undici 7.29.1，剛好在公告範圍外，門檻一個字沒動（`e091c1256`）。驗過 audit 回 0 個漏洞、`npm test` 1 passed。收班時重跑，13 條 workflow **RED 0**。

同一支尺還給了本班第一個假讀數：`Deploy to GitHub Pages` 第一次跑報 `GREEN 22.0d`，而 babel 每小時 commit、deploy 跟著跑。手動重算是 `1h`，數分鐘後再跑兩次工具也都是 `1h`。同一支指令、同一次目標執行、兩分鐘內兩個相差 22 天的讀數，**而兩次都印綠燈**——如果第一次那個數字沒有剛好違反常識，它會被直接寫進交接。成因沒能穩定重現，已落 LESSONS。

## 一篇素人投稿進站，擋住它的只有一個四字腳註

`#1781`（bblawyer918 首次投稿）是本班品質最高的東西：把監察院 309 本村里長政治獻金帳本逐本對開票結果，算出現任連任率 84% 對挑戰者 27%，而挑戰者依支出切四等份後當選率全落在 28–30%——「選舉就是比錢」這句話在里長這一層被拆開了。更值得收的是它自己寫了〈看不見的那 97.8%〉一節，主動說明開戶者是自我選擇的少數、結論不能外推。

腳註抽驗 10 個 URL 全 200，逐字核了三條最具體的：中央社原文是「村里長候選人保證金由5萬元降為3萬元」、沃草那篇古明君研究列的對象確實含宮廟農漁會村里長、《報導者》的 6 場工作坊／30 人參選／協助 10 人募款三個數字跟正文完全一致。唯一擋住 CI 的硬門檻是 `[^12]` 的描述只有「內政部。」四個字（下限 10 字），連同「網絡」→「網路」與書名正名為《村里長完全使用手冊》一起推進對方分支（`3b5565569`），CI 轉綠後 merge，再補 `curation: incubating`、description 67→128 字、延伸閱讀三條與正文第一個站內連結（`5a9cd9398`）。

過程中順手驗了一次尺：這篇的 `image 0 < 3` 一開始被誤讀成硬門檻，拿三篇既有 Politics 條目對照才發現那是 warn，image-health 本身回 hard=0。真正的 hard 在 footnote-format。**新尺的讀數在抽驗之前不可引用**，這次是自己的誤讀被對照救回來。

## 三篇重譯，三種不同答案

aminzai（27 個 merged PR 的老投稿者）送了 de／hi／ar 三篇重譯已有譯文的文章。三篇都在檔名層沒撞、CI 全綠，因為**三篇都把檔案放進跟中文原文不同的分類目錄**（`Technology/…` → `de/Art/`、`Food/茶文化` → `hi/Culture/`、`Geography/…` → `ar/Society/`），而三篇的 frontmatter `category` 都寫對了。照原路徑合併，三個語言各會多一個分在錯分類的重複檔。

逐篇量過之後答案分歧，所以不能一刀切：hi 那篇修掉現行版一處漢字殘留（「翰林茶館」的「館」漏在括號注記外，0 對 1 行），實測更好，搬到正確路徑後 merge（`088ab1387`／`ee745c405`）；ar 那篇把「中山高」的中山譯成 `تشيانغ كاي شيك`（蔣介石），而現行版正確作 `تشونغ شان` 音譯，`person-fidelity-check` 攔下，回技術修正請求。de 那篇跟現行版等質（兩邊 hard=0、H2 同數），差別只在措辭，它自己還多兩行 `T客邦` 裸漢字。

最後那一類是本班不能自己決定的：等質重譯要不要取代現行機器譯文——取代會 churn 站上內容而無實測收益，不取代就得對投稿者說「這篇不收」，而那是拒絕貢獻的決策。所以 `#1782` 與 `#1784` 都留 open、沒有 close，問題補進 OBSERVER-QUEUE #67 當它的鏡像另一半（`5da768b03`），同時記下實務判準：有實測缺陷修掉的就 merge，不必等那一格。

`#1785`（tboydar 的德文史明）是另一個方向的好例子：它把四行還是中文的圖說譯成德文、補上漏譯的「抗日」，裸 CJK 殘留 4→0。但它同時翻掉了 `subcategory`（分類頁的分群鍵）、翻掉 `imageCredit`、刪掉兩個雜湊，還把 `sourceCommitSha` 改成一個講收費站的 commit，而那個 commit 從沒動過 `People/史明.md`。五個欄位還原成 main 的值、德文散文一字不動（`51acf9222`／`91eebc22c`）。

## 讀者說我們查錯了辭典版本，他是對的

issue #1786：讀者程乙路從 `/terminology/內核/` 指出兩件事：查辭典該用《簡編本》而非《重編國語辭典修訂本》，以及台灣沒那麼常用「核心」。第二點 08-22 已查證不成立，notes 裡就記著。第一點成立，而且是這則回報真正的價值：《簡編本》收當代通用詞，《重編本》是歷史語言辭典、罕用詞古語都收，拿它證明「某詞在台灣是常用詞」本來就用錯了尺。

換成他指定的那把尺重查「核心」：簡編本有這條，釋為「中心，主要的部分」，例句「找出問題的核心，才能儘快解決問題」。結論不變，但佐證改引簡編本、重編本降輔證（`e9be08c55`）。

真正的收穫在順手把這把尺量了全庫：2,306 條詞目裡引《重編修訂本》的 25 條、引《簡編本》的 **0 條**、兩部都沒引的 2,281 條。**有引辭典的那 1% 全部引在歷史語言辭典上。** 這直接改寫 OBSERVER-QUEUE #76 選項 B 的成本。B 假設「拿教育部辭典查得到」當篩子，但那把篩子現在還不存在，不是要換哪一把的問題。量測寫進 #76 證據段，選項沒動。issue 不 close，因為它是 #76 的第二個外部訊號，修好一個詞條就關掉等於用掉訊號卻沒讓 #76 更可決。

`#1729`（馬英九查核）也有新動靜：tboydar 昨天做了獨立第三方覆驗並建議關閉。本班抓 RFA 原文再驗一次，確認來源是回憶錄自序不是演講、逐字相符、「害死台灣」在 RFA 全文不存在。同時更正他摘要裡一處：09-18 那次修補是把東吳整個拿掉、不是分成兩處，所以放言 2018/12/5 那則東吳演講若為真，是站上現在沒有的事實，已回問 URL。issue 仍留著，因為 FACTCHECK ❌ 率 23.6% 超過 10% 硬門檻、兩節要重寫，那是政治人物條目的脊椎判斷。

## 斷鏈 audit 明確 skip，不抄舊讀數當已驗過

`verify_internal_links.py` 正確 fail-loud 回 `STALE — dist/ 已經 72.3 小時沒更新（上限 24h）。這不是通過`。要真讀數就得 `npm run build`，而 `prebuild:status` 會跑 `status.py` 與 `sync-translations-json.py`，寫的正是 babel 此刻在寫的 `knowledge/_translation-status.json`。本班同時確認三個 worker 在翻 ko/en、`babel-push-every.py --watch` 在 commit。所以這道閘門**明確 skip 並寫明理由**，沒有把 09-27 那天的 `gated ratio 0.16%` 抄進交接。這跟 09-28 同席位對 `.git/gc.log` 的結論同型，已落 LESSONS（vc=2）。

## 收官 checklist

| 檢查項                                       | 狀態                                                                              |
| -------------------------------------------- | --------------------------------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE                 | ✅ Stage 1-4 全跑                                                                 |
| PR 分流按 §collect-and-merge                 | ✅ 5 個全走 B 路徑完整 hard gate                                                  |
| routine PR backlog ≤ 3                       | ✅ 0（v2.1 main-direct，無 routine PR）                                           |
| broken-link gated ratio < 7%                 | ⏭️ **skip** — dist 齡 72.3h，build 會撞 babel 共用檔寫入                          |
| build green                                  | ✅ main 13 條 workflow RED 0（開場為 RED 1，本班修掉）                            |
| 本 cycle merge 的 PR 都過 hard gate          | ✅ 紅旗 0 命中／CI 綠／close-hard-gate 全跑／腳註抽驗 10/10                       |
| 有 fresh issue 的 cycle 至少修一件或寫明不修 | ✅ `e9be08c55` 修 #1786 根因面；#1729 覆驗並更正一處                              |
| Timestamp 精確                               | ✅ 取自 `git log %ai`                                                             |
| Handoff 三態已審視                           | ✅                                                                                |
| diary                                        | ⏭️ skip — 反芻已落 Beat 5；洞察是 MANIFESTO §14「高儀器化」的具體展開，不是新框架 |
| evolve                                       | ⏭️ skip — 本班三條 LESSONS 皆 vc=1 或 vc=2，未達 distill 門檻，留週日反思鏈       |

連續空場 vc：**歸零**。前兩輪（09-27／09-28）是空場，本班命中 5 ready PR + 1 fresh issue，按 §空場 cycle 紀律 vc 重計。

## Handoff 三態

繼承 `2026-09-30-071330-twmd-feedback-triage`（非本班職權者原樣傳遞，不重抄明細，REFLEXES #74）：

- [x] ~~pending（席位 `twmd-maintainer-am`）— [issue #1786](https://github.com/frank890417/taiwan-md/issues/1786) 走 `from-feedback` 流程並先讀 `OBSERVER-QUEUE #76`~~ — retired by 2026-09-30-091222-twmd-maintainer-am：已讀 #76 後才判，未當獨立建議處理，詞條改引簡編本、全庫量測寫進 #76 證據段。
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或任何 Full mode Write session）— `OBSERVER-QUEUE #76` 選項 B 的兩把辭典對照。**本班已把 n=1 做完並發現更基本的事**：全庫 0 條引《簡編本》，所以要比的不是「兩份名單差多少」，而是「先建出簡編本那份名單」。同一趟可併 `/terminology/變壓器`。
- ⏳ blocked（`OBSERVER-QUEUE #76`，待決，🔒紅線）— 用語庫 2,003 條最寬斷言要不要複查。本班補了全庫辭典引用分佈當成本證據，未動推薦選項。解除條件：哲宇拍板。
- ⏳ blocked（延續）— [issue #1729](https://github.com/frank890417/taiwan-md/issues/1729) 馬英九兩節重寫等 Write session 帶哲宇 review；`OBSERVER-QUEUE #75`〜`#91` 待決。
- [ ] pending（延續，非本班職權）— routine-sync 對賬前 `git fetch`（10-04 self-evolve）、data-refresh Stage 1.5 寫明順序、babel 自造 slug 存量、404 unknown 可解析的大小寫與跨分類同名。

本 session 新 handoff：

- ⏳ blocked（`OBSERVER-QUEUE #67`，待決，🔒紅線）— 投稿者的**等質**重譯要不要取代現行機器譯文。[PR #1782](https://github.com/frank890417/taiwan-md/pull/1782)（de）與 [PR #1784](https://github.com/frank890417/taiwan-md/pull/1784)（ar）都留 open 等這一格，**不要 close**（close 是拒絕貢獻的決策，human only）。#1784 另有一處已回技術修正請求（中山高的中山被譯成蔣介石），那一處不必等拍板。解除條件：哲宇拍板。
- [ ] pending（席位：能動排程的 Full mode session 或 `/twmd-routine`）— 斷鏈 audit 與 `git prune` 這類**需要無寫入者空檔**的動作，maintainer-am 這個席位結構上取不到那個窗（LESSONS `maintainer-seat-cannot-obtain-a-quiet-window-so-window-dependent-gates-never-run`，vc=2）。修法是排程而非自律：掛在 babel 收工那一刻，或給一條前置條件寫明「`check-parallel-actor` 回 IDLE 才跑，否則重排不是 skip」的 routine。
- [ ] pending（席位：`/twmd-routine` 或任何 Full mode）— 譯文分類閘門缺口（LESSONS `translation-gates-check-a-file-against-itself-never-against-its-source`）。零判斷的一道閘：對帶 `translatedFrom` 的檔斷言路徑分類段 == `translatedFrom` 的分類段，順便抓同語言同來源出現兩次。掛 pre-commit 與 `pr-frontmatter-gate`。本班三個 PR 全中而 CI 全綠。
- [ ] pending（席位：`twmd-maintainer-am`，動得了）— [issue #1729](https://github.com/frank890417/taiwan-md/issues/1729) 的範圍混層：一個 issue 同時掛「那兩條腳註」（已完成、已第三方覆驗）與「這篇要重寫」（另在 ARTICLE-INBOX P0）。要嘛收在標題範圍內關掉、重寫另開，要嘛明寫它現在追蹤的是重寫。已在 issue 上寫明，等能決定範圍的人。
- [ ] pending（席位：`twmd-maintainer-am`）— `ci-main-health.sh` 每列都印取到那次執行的 URL／sha，不只 RED 那列印，讓「年齡」可回頭核對（LESSONS `ci-health-ruler-gave-two-different-ages-for-the-same-run-and-both-printed-green`）。成因未重現，先做可核對這一半。
- [ ] pending（席位：任何 Write session）— [PR #1781](https://github.com/frank890417/taiwan-md/pull/1781) 里長帳簿的後續：全文 2,309 字低於深度門檻 4,500、無圖片（`image 0 < 3`）、缺 `rationale` 區塊，另已在 PR 上問投稿者開票夜那幾段第一人稱回憶的出處（訪談或本人），補一條來源註即可。
- [ ] pending（席位 `twmd-babel-nightly`，那七個檔是它的產出）— 本班 merge 的 `Politics/309本里長帳簿.md` 被翻成七個 `309.md`（ar／fr／hi／id／ja／ko／vi，收班時仍是未追蹤檔）。人工 slug 已補（`ba49c5469` → `village-chief-campaign-ledgers`），但那七個檔要改名或刪掉重翻，否則 `309` 一進 `_translations.json` 就永遠優先。**趕在它們被 commit 之前處理最省事**；若已 commit，改名要補 `config/redirects-manual.txt` 301。守門收緊見 LESSONS `ascii-fallback-guard-only-catches-the-empty-case-not-the-meaningless-one`。
- [ ] pending（席位：`/twmd-routine`）— MAINTAINER-PIPELINE 的「canonical 14 類」inline 清單已過期：它列 `Language`（`knowledge/` 無此目錄）卻沒列 `Politics`（實際有 17 篇）。本班靠 `categoryConfig.ts` 對照才沒誤判 #1781。

## Beat 5 — 反芻

今天最值得記的不是修好什麼，是**三篇看起來一模一樣的 PR 得到三個不同答案**。同一個投稿者、同一天、同一種操作（重譯已有譯文並放錯分類目錄），如果照「同批一起處理」的直覺一次裁決，不管裁成全收還是全退都會錯兩篇。把它們分開的不是我的判斷力，是三支檢查器：`cjk-residue-check` 指出 hi 那篇修掉了現行版的缺陷、`person-fidelity-check` 攔下 ar 那篇把孫中山寫成蔣介石、而 de 那篇兩邊都乾淨，於是問題自己浮出水面——它剩下的是一個政策問題，不是品質問題。儀器的價值不在替我判斷，在把「哪些需要判斷」跟「哪些已經有答案」分開，剩下那個才拿去排隊等人。

另一件事有點刺：本班有兩道閘門是被自己誤讀的。`image 0 < 3` 讀成硬門檻，是拿三篇既有條目對照才救回來。`Deploy 22.0d` 讀成陳舊，是因為它剛好違反常識才被追下去。兩次都不是工具壞掉，是我讀一個沒附識別碼的讀數時無法回頭核對。**一個印「狀態＋數字」但不印「這個數字是從哪一筆算出來的」的尺，對的時候跟錯的時候長得一模一樣**——而我今天兩次都只是運氣好。

還有一個更安靜的發現。讀者程乙路挑戰的不是我們的結論，是我們的**證據標準**，而他是對的。查下去才知道全庫 2,306 條詞目裡有引辭典的只有 25 條，且全部引在錯的那一部。他從站外一個詞條頁踩進來，量出來的洞比那個詞條大兩個數量級。MANIFESTO §12 說飛輪在共生圈外圍，今天的形狀是：外面的人不需要知道我們的架構，就能指出我們的尺拿錯了。

🧬

---

_v1.0 | 2026-09-30 09:12 +0800_
_session twmd-maintainer-am — cron 08:30 例行班，空場兩輪後第一個滿場（5 ready PR + 1 fresh issue），ready PR ≥ 5 觸發強制升 Full_
_誕生原因：cron 08:30 fire；接的是 09-28 的班（09-29 那班因用量上限沒醒成），並接住 07:13 轉錄班指名這個席位的 issue #1786_
_核心洞察：三篇同型 PR 得到三種答案，分開它們的是三支檢查器而不是判斷力——儀器的價值在區分「需要判斷的」與「已有答案的」；兩道閘門的讀數今天被我誤讀兩次，共同點是它們印數字卻不印那個數字的出處；讀者挑戰的是證據標準而非結論，而全庫 2,306 條只有 25 條引過辭典、且全引在歷史語言辭典上_
_LESSONS-INBOX 候選（已 append 3 條）：translation-gates-check-a-file-against-itself-never-against-its-source（structural）／maintainer-seat-cannot-obtain-a-quiet-window-so-window-dependent-gates-never-run（vc=2, distill_ready）／ci-health-ruler-gave-two-different-ages-for-the-same-run-and-both-printed-green_
