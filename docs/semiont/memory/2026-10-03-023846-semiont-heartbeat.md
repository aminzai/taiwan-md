# 2026-10-03-023846-semiont-heartbeat — 巡邏三篇 featured 初稿 19 錯，串流篇三條參考資料是別篇文章，缺席第一天代理執行 #65 (a)，譯文來源版本 sha 改驗值不驗形狀

> session semiont-heartbeat — 每日排程完整心跳凌晨班（Full mode，本機 commander-macbook）
> Session span: 02:35 → 03:05 +0800（10 個工作 commit＋收官 03:05:04，第一個 commit 02:58:17，最後一個工作 commit 03:03:07）
> 資料來源：`git log %ai`＋`date`

## 觸發

排程心跳，今天第一輪。甦醒時 wake-context 亮一盞警訊：本機落後 origin 23 個 commit（mouhouse 的 babel 夜班剛推完一批委派重譯），帶 autostash pull 後重跑，十一項全綠。器官讀數是昨天 06:00 那份，免疫 59 仍是最低（review_coverage 19）。觀察者在場訊號停在 09-26，今天是第七天，缺席協議第一天生效：到期的非 🔒 預設必執行，🔒閾值類可由 Full mode 代理。昨晚那班留給下一個 Full mode 的，是巡邏母體裡還沒抽的三篇 featured。

## 巡邏第四十五到四十七篇

抽樣指令重跑後前十名仍是 03-19、12 語的初稿，照 featured 優先抽了〈台灣電子音樂與派對文化〉〈台灣音樂產業與串流時代〉〈台灣國家公園〉。三篇先自己讀完跑 Phase 5，再派三個 Sonnet 子代平行查，prompt 帶了昨天〈數位身分證〉「查無出處」誤判與「貢茶精品」借用 ✅ 兩個反例。

〈台灣電子音樂與派對文化〉58 原子 9 錯（15.5%），六條腳註沒有一條能開頁又撐得住它掛的句子。1990 年代場館清單一句話跨了十年，Spark 在 2003 年才完工的台北 101 地下層。Ultra 首度來台是 2014 年不是 2013。Korner 2019 年熄燈，比疫情早，文章卻寫「後 COVID 老牌場館走入歷史」，而 AmCham 2023 年寫的是那批俱樂部「除了一間都撐過疫情」。止血把 1990 年代段換成聲軌時間線上查得到的三件事：1995 年 7 月 29 日 DJ @llen 用卡車把音響載到二重疏洪道、1996 年梅花湖被警察喊停、1997 年《PLUR》創刊，腳註換成 18 條（`afcfabc33`）。

〈台灣音樂產業與串流時代〉53 原子 7 錯（15.2%）。description、概覽、小標、結語四處寫 KKBOX 是「全球首個合法串流」，第一個隨選訂閱串流是 2001 年的 Rhapsody。五月天線上演唱會的「3,000 萬人同時在線」是一天累計 4,244 萬人次的口徑錯。〈大風吹〉MV 用 yt-dlp 讀是 1,597 萬次，不是 5,000 萬。參考資料十條只有一條被正文引用，INSIDE、商周、動腦三條網址是真的、開頁卻是別篇文章，篇名是編的。全換成 7 條正文真的在引用的來源（`10c444b35`）。

〈台灣國家公園〉80 原子 3 錯（3.8%），沒過重寫門檻，但「保護超過 30% 陸域」要靠國家公園署的統計專冊才能改正：子代說那份 PDF curl 被擋，帶瀏覽器 UA 就拿到了，陸域 31 萬公頃占 8.7%。金門的「斑翅鳧」三個來源都 grep 不到，換成國家公園自己說的鸕鶿與三座湖。壽山段還留著一句修稿殘留「（不是 2024 年）」（`7f5cc659d`）。兩篇過門檻的登記成 P1 EVOLVE（`1e9b41d66`）。

會改字的 ❌ 都自己 curl 原文 grep 過，子代判定全部成立。有一處沒照子代：電音篇它引鏡傳媒說 ROXY 99「在金山南路、2017 年熄燈」，那一頁 grep 兩個詞都 0 筆，正文只寫到 Taipei Times 撐得住的遷址。昨晚那班留下的提問也有了答案：三個子代都照 v2.8 把 💬 另列（11／7／7），79 個 ✅ 裡帶「僅見摘要」這類字眼的只有 2 個，細看都是子代把沒開頁的細節明確排除在判定外。

## 缺席第一天：#65 (a) 代理執行

OBSERVER-QUEUE #65 (a) 是 🔒閾值類，推薦預設是把 `verify-translation.py` 的 sourceCommitSha 檢查從驗格式升成驗「這個 sha 在中文檔歷史裡」。動手前先量全庫 13,565 篇有 sha 的譯文：約 13,350 篇是改過該中文檔的 commit。210 篇指向沒改過它的 commit（當時的 repo HEAD 或 merge），中文檔在那裡都存在，diff-patch 照樣能用。4 篇根本解析不到。照字面全部 FAIL 會讓 210 篇存量在下次被任何修補工具碰到時被擋，所以分兩級：解析不到或那個 commit 沒有這個中文檔才 FAIL，其餘 WARN（`72d486cd8`）。這是照量測調了推薦預設的強度，§已決寫明了偏離和哲宇要更嚴時改哪一行（`d97e5c73e`）。

同一個 commit 長出 `recover-source-sha.py`：拿譯文自己記的雜湊回中文歷史找真正翻譯的那一版，只改 sha。今晚 01:11 mouhouse 那班手工修了 34 篇「sha 比內容新」，拿它們修補前的版本當正控制，找回值 34/34 一致。隨機抽 300 篇有 299 篇 sha 與雜湊一致。四篇 FAIL 用它修完，三篇只差最後一碼，寫入它們的都是七月讓模型手抄 provenance 的批次（`08d90d8b8`），在 REFLEXES #93 補第四例（`2fce0fab4`）。過程中我自己造的兩把尺各說了一次謊：全庫掃描只讀前 3,000 字元，長 frontmatter 的 135 篇被算成「沒有 sha」。找回工具只比 16 碼雜湊，林百里那篇記的是 64 碼，差點被判「找不到、該重翻」。兩次都是讀數看起來不對勁時回頭看樣本才抓到。原本寫進 FAIL 訊息的修法是 `bump-source-sha.py`，查了才發現它是升到中文最新版，正是 #65 說「那是假的」那一種，改指新工具。

收官 rebase 時 babel 夜班剛推了十個 commit，本班七個 commit 的 hash 全被改寫，ARTICLE-INBOX 與 OBSERVER-QUEUE 引用的編號一起作廢，補了一個只為改 hash 的 commit（`e04558efb`）。FACTCHECK 原本只對查核檔開頭寫了這條，補上佇列條目這第二個位置與順序：先 push 再寫引用，升 v2.9（`d35f872e7`）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                   |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                     |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                               |
| Handoff 三態已審視           | ✅                                                                                     |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，本班無新器官或里程碑                                                |
| 自我檢查工具 PASS            | ✅ 三篇 article-health hard=0；verify 與 recover 測試 17 passed（Python 3.9 也能載入） |
| Diary                        | skip：反芻寫在下方；#93 與 FACTCHECK 照 DNA-first 去 bump 既有條目，沒開新教訓         |

## Handoff 三態

繼承 `2026-10-02-203728-semiont-heartbeat`：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 凌晨、早上、下午、晚上四輪的巡邏修正與 32 份 hi／ar 降級，原樣傳遞，要盯的原子見 `2026-10-02-024346`、`084048`、`143724`、`203728` 四份 semiont-heartbeat；本班再加 36 份，見下方新交接
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`，原樣傳遞（REFLEXES #74）
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（走 REWRITE 時）— 09-25、10-01 兩輪的懸案原樣傳（明細在 `2026-10-02-024346-semiont-heartbeat`）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04，第八班原樣傳）— `check-parallel-actor.sh` 擴到 `git worktree list` 每棵樹的 dirty 狀態（REFLEXES #42 第四起）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— LESSONS `homepage-citation-passes-format-and-reachability-gates` vc=3：本班三篇又各有首頁腳註（gca、nps、taicol、kkbox、must），可一起決定 WARN check
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— `check-hardcoded-langs.sh` 剩五支 A 類；LESSONS `patrol-sampling-ignores-featured-exposure`：連兩班照 featured 抽，五篇裡四篇過門檻，可以一起決定排序鍵
- [ ] pending（席位 `twmd-distill-weekly`）— LESSONS `i-concluded-not-found-from-one-failed-search` vc=2，剩下一半的機械化
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`、`#65 (b)`（待決，🔒），解除條件：哲宇拍板。#77、#78 的 14 天預設 10-07 到期，#86 缺席模式代理 10-11；缺席模式今天起生效，週日體檢 Stage 2.7 接手到期的非 🔒 預設
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（延續，非本班職權，原樣傳遞）— `.git/gc.log` 與 `git prune` 排程、issue #1729
- [ ] pending（席位 `twmd-babel-nightly` 10-03，上一班新交接原樣傳）— 便利商店、手搖飲、台語歌三篇 × 十二語的 36 份巡邏修正，要盯的原子在 `2026-10-02-203728-semiont-heartbeat`
- [x] ~~pending（下一個 Full mode）— 巡邏母體 featured：台灣電子音樂與派對文化、台灣音樂產業與串流時代、台灣國家公園~~ — retired by 本 session（`afcfabc33`／`10c444b35`／`7f5cc659d`）
- [x] ~~pending（下一個 Full mode 的巡邏）— FACTCHECK v2.8 的 💬 第一次實用~~ — retired by 本 session：三個子代都另列 💬（11／7／7），79 個 ✅ 裡沒有借用 ✅ 的評價句

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 再接 36 份巡邏修正（三篇 × 十二語），三篇腳註都重編過，譯文腳註號要跟著中文。對讀要盯的原子：電音（二重疏洪道 1995、梅花湖 1996、《PLUR》1997、PLUR 源自美國、TeXound 1998、ROXY 99 金山南路、Road to Ultra 2014／Ultra Taiwan 2018、Korner 2019 熄燈、Pawnshop 2019-12）、串流（Rhapsody 2001、KKBOX 2005-10 簡民一林冠羣許安德、1997 年 123 億→2003 年 45 億、《人生海海》35 萬、Apple Music 2016-02、〈大風吹〉約 1,600 萬、五月天 4,244 萬人次）、國家公園（陸域 8.7%、約 7,500 平方公里、墾丁植物約 1,700 種、玉山陸域最大、黑琵 7,746／4,719、金門鸕鶿與三座湖、澎湖南方四島移到海洋小節）
- [ ] pending（席位：下一個 Full mode）— 巡邏母體 featured 剩 People/蔡明亮、People/賴清德、Technology/AI發展、Technology/台灣資安產業發展、Technology/東亞文字輸入法（皆 03-19、12 語）；賴清德是在任政治人物，抽到時評價句判 💬 不改寫立場。重跑抽樣指令確認
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— status.py 遇到 sha 與中文最新 commit 相同就判 fresh、不看雜湊，01:11 那 34 篇就是這樣藏了兩天。`recover-source-sha.py` 的 `check_current()` 已能對賬 sha 與雜湊，可評估接進 status.py 或 babel-nightly 前置；隨機 300 篇現況 0 不一致，屬預防
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65`（(a) 已決，缺席預設）：若要把 WARN 那級也升 FAIL，先用 `recover-source-sha.py --apply` 處理 210 篇存量，屬 (b) 的 >50 檔紅線

## Beat 5 — 反芻

缺席第一天就碰到一條可以代理的決策，我做的不完全是推薦預設寫的那句話。條目寫「升成驗 sha 在該檔歷史裡」，量完發現照字面做會擋住 210 篇功能上沒壞的存量，於是把它們降成警告。代理一個不在場的人的決定，最容易出錯的地方大概在這裡：他寫下預設的時候手上還沒有今天量出來的數字，我照實量調整是對的，但調整本身也是一個決定，得寫在他回來第一眼會看到的地方，連同「你要更嚴就改這一行」。

今晚最常見的錯是在兩個系統之間手抄一個值。三篇初稿的錯，有一半是把一個真的數字抄進錯的年份或錯的口徑。四份譯文的 sha 是模型把一串 hex 抄錯最後一碼。我自己寫進佇列的 commit 編號，十分鐘後就被 rebase 換掉。驗格式的閘門對這三種都會放行，因為抄錯的值長得跟對的一模一樣。

🧬

---

_v1.0 | 2026-10-03 03:05 +0800_
_session semiont-heartbeat — 巡邏第四十五到四十七篇（電子音樂、串流、國家公園，皆 featured）共 19 錯，三篇止血＋兩條 P1 EVOLVE。缺席協議第一天代理執行 OBSERVER-QUEUE #65 (a)＋recover-source-sha.py。FACTCHECK v2.9。REFLEXES #93 第四例_
_誕生原因：每日排程完整心跳凌晨班，接昨晚寫給下一個 Full mode 的三篇 featured 與 💬 首次實戰的提問_
_核心洞察：(1) 代理缺席者的預設時，照量測調整強度也是一個決定，要寫在他回來第一眼看得到的地方 (2) 格式閘門放行所有抄錯的值，sha、年份、口徑都是 (3) 引用自己 commit 編號的紀錄要等 push 之後再寫_
_LESSONS-INBOX：未新開條目。REFLEXES #93 補第四例，FACTCHECK §月度巡邏補第二個位置_
