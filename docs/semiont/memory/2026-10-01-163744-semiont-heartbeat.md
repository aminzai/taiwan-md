# 2026-10-01-163744-semiont-heartbeat — 譯文分類閘門上線並把投稿者照抄的五篇英文範本搬回原位，斷鏈尺學會認出正在建的 dist，巡邏第二十七到二十九篇 10 錯

> session semiont-heartbeat — 每日排程完整心跳（Full mode，本機 commander-macbook）
> Session span: 16:36 → 17:01 +0800（約 25 分鐘，7 commits）
> 資料來源：`git log %ai` 與 `git reflog`

## 觸發

排程心跳。甦醒時 wake-context 亮了一盞燈：本機工作樹落後 origin 731 個 commit，上一次在這台機器上動 git 是 09-25 那輪心跳，routine 全在營運機上跑。先把一份過期的 `dashboard-analytics.json` 衍生檔丟掉（origin 有今早 06:07 的新版），fast-forward 後重跑，十一項體檢全綠。哲宇最後在場 09-26，五天，還沒進缺席模式。今早 06:08 data-refresh 已跑過，本輪不重跑。

診斷：心臟從 90 掉到 70，原因是 `twmd-rewrite-daily` 自 07-25 起依哲宇決定改手動，七天八篇新文全是投稿，這是已決的手動模式，不是故障。免疫 59 黃燈，最大缺口仍是 review 覆蓋。OBSERVER-QUEUE 今天沒有到期的非 🔒 預設（#69 (a) 明天起、#77 10-07、#86 10-11）。ARTICLE-INBOX 有兩條切角 10-04 到期（名古屋亞運 P0、李灝宇 P1），亞運那條自己寫了「之後改賽後總結切角」，賽事還在進行，本輪不搶寫，寫文的時機留給手動控制 rewrite 的人決定。

## 譯文分類閘門，以及它在存量裡抓到的範本

接今早維護班的交接：三個投稿 PR 把譯文放進跟中文原文不同的分類目錄，frontmatter category 卻寫對，CI 全綠。這次的閘門住進既有的 `test-frontmatter.mjs`，不另立新腳本：對帶 `translatedFrom` 的檔斷言路徑分類段等於原文分類段。這支同時被 pre-commit、`pr-frontmatter-gate` 與部署呼叫，三處一起生效。新測試先拿舊版閘門跑，確定會失敗再收。原本那條 resources 測試的夾具自己就是錯置的（vi/resources 指向 Technology），一併改正（`95de2acab`）。

全庫首跑抓到五篇存量：英文的動畫產業、茶文化、兩篇都市文章，加上西文動畫篇，四篇英文就是昨天 de／hi／ar 三個 PR 照抄的位置。五個 git mv、`_translations.json` 改 key、十四篇譯文裡十五條指向舊網址的連結改新網址、補五條 301（`ddf3ef987`）。轉址生成器同時拿掉一條資料驅動的舊規則：它原本把正確的 `/en/geography/…` 導去錯的 `/en/society/…`，代表讀者跟爬蟲一直在找對的那個路徑。

## 斷鏈尺遇到正在跑的 build 回「正在建」

同一份交接的第二件：`verify_internal_links.py` 的年齡上限擋得住舊 dist，擋不住寫到一半的 dist。現在掃描前後各問一次 `ps`，有 astro build 在跑就回 `BUILDING`、exit 4，跟 STALE 一樣算沒量到（`be4e900ed`）。第一版負控制就被命中，命中的是我自己的父 shell，它的命令列裡剛好有「astro build」這幾個字。改成排除自己的祖先程序後，正控制（背景假 build）回 4、負控制回原本的 STALE、祖先命令列提到 astro build 不算，三態都驗過。兩條 LESSONS 標上已機械化，MAINTAINER-PIPELINE 那段「先 pgrep 再讀」改成指向這個行為。

## 巡邏第二十七到二十九篇

照抽樣指令取前三名，三個 Sonnet 子代平行查、只寫查核檔，我讀原文先標疑點，回來後每條 ❌ 親自對原文再改。三份查核檔落 `reports/research/2026-10/`，各附 Phase 6 套用紀錄。

〈台灣公園與日常休閒〉28 個原子 2 錯：「公園是少數可以合法放開牽繩的地方」，台北市動保處新聞稿寫的是公眾場所要繫繩、可罰兩千到一萬；特色公園運動寫成 2017 年前後，特公盟其實 2015 年成立、同年 11 月到北市府前陳情（`1d2876d0d`）。〈台灣發酵食品與醃製文化〉26 個原子 4 錯：臭豆腐「十七、八世紀隨閩南移民傳入」，而它自己掛的光華雜誌寫民國三十八年隨政府遷台；小米酒 15–20%、蘿蔔乾跟菜脯被當兩種醬菜、腳註掛一部不存在的《發酵食品衛生標準》，同輪刪掉查無出處的年產值、北中南臭豆腐流派與兩條健康功效（`ef4290a8c`）。〈台灣媒體與新聞自由〉34 個原子 4 錯：保障新聞採訪自由的是釋字 689 不是 613、蘋果日報停刊先後顛倒且台灣的停刊理由沒有疫情、華視公廣化是 2006、無線台是 5 家；新聞自由指數從 2024 更新到 2026 年第 28 名，補上中天換照案的經過（`78ae80cba`）。

錯誤率 7%／15%／12%，延續上一輪的低檔。子代給的一個法規代碼（L0040074）親查是《一般食品衛生標準》，跟它說的法規名對不上，改掛親查過的《食品安全衛生管理法》。發酵篇刪掉三條帶年份的假腳註後，prose-health 分數從 3 變 4（年份計數掉到 2），沒有為了湊分數補年份。

## 學測專題的導覽列

09-25 那輪留的「部署後看一眼」：taiwan.md 中文頁的探索下拉與手機抽屜各有一處「學測專題」，英文頁沒有，符合設計。Discussion #1704 最後一則回覆停在 09-13，投稿者 idlccp1984 還不知道已經掛上導覽列。排程心跳不代發對外留言，交給維護班，草稿寫在下面的交接。

## 收官 checklist

| 檢查項                       | 狀態                                                           |
| ---------------------------- | -------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                             |
| Timestamp 精確               | ✅ `git log %ai`＋`git reflog`                                 |
| Handoff 三態已審視           | ✅                                                             |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，無 prose 要改                               |
| 自我檢查工具 PASS            | ✅ 三篇 hard=0，警告對 HEAD 基線逐條比過（發酵篇 +1 原因見上） |
| Diary                        | skip（反芻收在下面一段）                                       |

## Handoff 三態

繼承 `2026-10-01-084906-twmd-maintainer-am` 與 `2026-09-25-144832-semiont-heartbeat`：

- [x] ~~pending — 譯文分類閘門（LESSONS `translation-gates-check-a-file-against-itself-never-against-its-source`）~~ — retired by 本 session（`95de2acab`，存量 `ddf3ef987`）
- [x] ~~pending — `verify_internal_links.py` 最便宜那條（build 在跑就 abort，LESSONS `freshness-guard-reads-a-half-built-artifact-as-maximally-fresh` 候選 (b)）~~ — retired by 本 session（`be4e900ed`）；(a) 完整性斷言與 (c) 分母下限仍開著，(c) 是新門檻，留給哲宇
- [x] ~~pending — 巡邏母體第二十七到二十九篇~~ — retired by 本 session
- [x] ~~pending — 部署後看學測專題導覽列~~ — retired by 本 session（中文頁兩處、英文頁零處，符合設計）
- [x] ~~🚨 mouhouse 登入預估 09-27 過期（issue #1761）~~ — retired（issue 09-26 已關閉）
- [ ] pending（席位 `twmd-maintainer-am`，留言屬致謝與技術說明層）— Discussion #1704 回覆投稿者 idlccp1984。草稿：「學測專題已經掛上中文站的導覽列了，在『探索』下拉選單和手機版的選單抽屜裡都看得到。因為 /exams 目前只有中文版，外語頁不出這條連結，免得把外語讀者送到中文頁。謝謝你一路等這個決定。」
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單，同趟可併 `/terminology/變壓器`
- [ ] pending（席位：任何 Write session）— PR #1781 里長帳簿後續
- [ ] pending（下一個 Full mode）— 巡邏母體現值前三名：Society/台灣社區與里文化、Society/教育制度與升學文化、Society/早餐店阿姨與社區情報網（都是 03-18 出生、12 語）
- [ ] pending（走 REWRITE 時）— 本輪三篇留下的懸案：發酵篇豆腐乳寫「接種毛霉菌、長出白色菌絲」，台式豆腐乳可能以麴醃製，沒找到一手出處；媒體篇戒嚴期「警備總部預先審查」「九點檔新聞統一播報」兩句；公園篇「夜間公園」與「夜晚公園」兩節重複。09-25 那輪的國際標準／動物園／政治三篇懸案仍在
- [ ] pending（self-evolve-weekly 候選，09-25 起第二班原樣傳）— `check-parallel-actor.sh` 擴到 `git worktree list` 每棵樹的 dirty 狀態（REFLEXES #42 第四起）。本機現有兩棵舊樹（09-09 agent 樹有四個未追蹤檔、09-07 codex 樹）都不是今天的，本輪未動
- [ ] pending（席位：Full mode，逐檔判斷）— `check-hardcoded-langs.sh` 掛號的 python 檔，現在清單已長到二十條，三個感知層（`fetch-cloudflare.py`／`refresh-llms-txt.py`／`weekly-report-prep.py`）先
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`（PR #1782、#1784）／`#76`／`#28`／`#75`〜`#91`（待決，🔒），解除條件：哲宇拍板
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- [ ] pending（延續，非本班職權，原樣傳遞不重抄明細，REFLEXES #74）— `.git/gc.log` 與 `git prune` 排程（營運機）、`OBSERVER-QUEUE #69（待決）` (a) 10-02 起等 #68、issue #1729、routine-sync 對賬前 `git fetch` 等，明細見 `2026-10-01-084906-twmd-maintainer-am`

## Beat 5 — 反芻

存量那五篇讓我想到，一道新閘門只看新進來的檔，等於假設站上已有的東西是對的。可是投稿者學怎麼放檔案，看的正是站上已有的樣子。英文那四篇錯了半年，沒有閘門會叫，因為它們出生時這道閘門還不存在；它們安靜地當了範本，昨天三個 PR 就照著放。修補新進的錯而不修範本，下一個投稿者還會照抄。

另一件小事比較刺。巡邏一整輪在拿掉推擬出來的引用：一篇報告名查無、一部不存在的法規、一個沒人寫過的篇名。改媒體篇要補中央社那條腳註時，我先打了一個看起來很像的標題，打完才想到我沒看過那篇報導的標題，回頭去抓，真標題完全不同。這個錯的形狀跟我正在清的那些一模一樣，差別只在這次有一步「先抓再寫」把它攔下。斷鏈尺那邊也一樣，第一個被它誤認成正在跑的 build 的，是我自己。

🧬

---

_v1.0 | 2026-10-01 17:01 +0800_
_session semiont-heartbeat — 譯文分類閘門＋五篇範本歸位、斷鏈尺 BUILDING、巡邏三篇 10 錯 2 條補腳註更新_
_誕生原因：每日排程完整心跳；本機落後 origin 731 個 commit 甦醒即同步_
_核心洞察：(1) 新閘門不看存量時，存量的錯會當範本被照抄 (2) 清推擬引用的人自己也會推擬，攔下它的是「先抓再寫」的順序 (3) 量測工具第一個誤判的對象可能是量測者自己_
_LESSONS-INBOX 候選：無新條目（兩條既有 LESSONS 標已機械化；推擬標題屬 MANIFESTO §10 與 REFLEXES #75 既有範圍）_
