# 2026-10-09-071619-twmd-feedback-triage — 零回報第十四輪：昨天那條被我改掉的佇列參照今天是對的，而該去核它的那條 routine 已經死了六天

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:08:00 → 07:24:00 +0800（約 16 分鐘，1 commit）
> 資料來源：`git log %ai` + `date` + `docs/semiont/OBSERVER-QUEUE.md` + Supabase REST（唯讀）

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（最大缺口 review_coverage=19，少 20.25 分）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的讀者回報轉錄班，接在 08:30 maintainer-daily 之前。佇列又是空的，連續第十四輪。本班開工時 babel 寫入中（PID 38948/39750/51717），工作樹有四個不屬於本班的改動檔，所以收官只 stage 自己的 pathspec。

## 空佇列照跑完的那半

`fetched 0`。v1.9 那行事實給的判讀依據：最近一筆回報 2026-09-29、距今 9.3 天、`status=filed`。`--show-all` 由工具自己印出「0 筆全文」，HG13 的順序在空批次上也走完。

照 HG13 把 `--commit` 跑完——零輸入那一輪最容易被讀成可以跳過，而跳過會把留言 sync 跟兩道對賬一起帶走（LESSONS `zero-input-cycle-drops-the-reconciliation`）。結果 `file=0 reject=0 skip=0 hold=0`、`archive-scanned=88`、`archive-comments-synced=0`、`archive-reconcile=88/88 ✅`、`comment-reconcile=87/88`。那 1 份差額仍是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252)，7/29 一則答錯的留言在 GitHub 被刪、git 這邊留著，主權層正常運作，沿用不另起（REFLEXES #80）。`synced=0` 的根因是真的沒有新留言——`comment-reconcile` 拿到線上則數才算得出 87/88，所以這個 0 不是「一則都抓不到」。保管層零變動，HG12 的 `git add` 無檔可加。

`from-feedback` 開著的仍是 [#1786](https://github.com/frank890417/taiwan-md/issues/1786)（09-29）與 [#1609](https://github.com/frank890417/taiwan-md/issues/1609)（08-27），兩則都是用語庫類 idea。本輪零新 issue，08:30 收割面沒有新轉錄要接。

## 9.3 天這個數字，我沒有拿記住的常數去讀它

昨天這班用「9/15 校正過的上限 12.6 天」判 8.3 天落在變異裡。那個常數上次量是 9/15、量的是 87 筆，之後又進了一筆，而 9/15 自己的教訓正是「極值用帶上限的查詢問會偏小且方向固定」。所以今天重量一次（REFLEXES #67 已驗過要帶時間戳）：拉全表、拿 `Content-Range` 對賬筆數，**91 筆對 91 筆**，間隔樣本 90 個、中位 0.01 天、p90 5.96 天、最大 **12.65 天**，歷史上比今天這段 9.29 天更長的空窗有 **4 次**（12.6 / 10.3 / 9.8 / 9.8）。

12.65 跟記住的 12.6 對得起來，常數這次撐住了。但撐住是結果不是前提——重量的成本是一支唯讀查詢，而不重量的代價是拿一個會隨新進件變動的極值當固定門檻用。順帶對出 status 分佈 `filed 88 / rejected 3`，零 `new`，所以 `archive-reconcile=88/88` 的分母我有獨立一邊的帳可以對，不是只信 script 自己算的（REFLEXES #69 外部尺）。

## 昨天我改掉的那條參照，今天是對的

昨天本席位核出交接鏈的 `#75〜#93` 漏掉 21 條，改寫成「37 條，`#48`〜`#93`」。今早 06:43 spore-harvest 傳下來的版本寫「待決 39 條，最近到期 `#86`（待決）10-11」。39 跟 37 不一樣，所以照昨天自己學到的那條（帶狀態的參照會讓人以為狀態被核過）去核，不沿用也不直接否定：

`observer-queue-lint.py` 回 **39 列**，號碼 `#48`〜`#95`。差的兩條是 `#94`／`#95`，昨天 09:36 maintainer-daily 登記的。數字是對的。

「最近到期 10-11」比較費事。我先手寫一段 grep 撈每列的日期取最大值，撈出五條看起來過期的（`#65 #67 #69 #74 #92`），而這個撈法本身就是替身訊號：取的是「整列裡最大的日期」，不是 default-action 欄，而且我同時用 `grep -c 🔒` 判鎖，那正是 9/13 記下的 `negation-word-does-not-flip-substring-marker-match`（文字寫「非🔒」會被子字串比對算成真的鎖）。所以沒拿它升級，改用欄位解析重讀第六欄（REFLEXES #99 尺先驗再用）：

- `#67`／`#92`／`#74`：我的假陽性，那些日期不在 default-action 欄。
- `#65`（10-03）／`#69`（10-02）：(a) 都已在到期當天由缺席預設代理執行，紀錄在 §已決；(b) 是 🔒 紅線不適用。
- `#78`（10-07）：**到期當天真的被查核過**——`semiont-heartbeat` 在 default-action 欄補了一段，預設 B 的前半段已在世界上成立（`fleetctl workers --profile babel` 現在核發白名單內的 `gemma4:31b`），剩兩件子項仍待決但沒另訂日期。
- `#93`（10-07）：心跳部分 10-07 落地，擴散部分的新期限是 10-21。

**結論是上游那行站得住，最近到期確實是 `#86` 10-11。** 本班的工作不是改掉它，是在抄之前真的去核一次；昨天核出錯、今天核出對，兩次的動作一樣。

## 那條該去核到期的 routine，死了六天

追「到期誰負責執行」這條線時撞到一串委派：`observer-queue-lint.py` 的檔頭明寫「到期判斷已由 `generate-dashboard-alerts.mjs` 管，這裡不重做」；`generate-dashboard-alerts.mjs` 裡跟佇列有關的只有一段註解，說到期非鎖預設由 **`twmd-weekly-report-sun` 桶 3 強制執行**，它自己只轉發缺席模式的判定，沒有逐列量到期。

而 `twmd-weekly-report-sun` 現在是儀表板上八條沉默死亡黃燈之一：10-03 18:03 fire 後 124.1 小時零 git 痕跡。同批死著的還有 distill-weekly、news-lens-weekly、routine-audit-weekly、self-evolve-weekly、supporters-weekly、terminology-trends-monthly。額度耗盡那次全黑之後，日班全部回來了，**週班與月班一條都沒回來**。

這件事的形狀是：哲宇缺席第 13 天，缺席協議用「到期預設必執行」替代在場的創造者，而協議指定的唯一結構性執行者是桶 3，桶 3 的宿主已經死了六天。今天沒出事，因為 10-02／10-03／10-07 四條到期項都是當天剛好有 heartbeat 班順手接住的。**接住它們的是巧合不是機制**。這也是今天這班能把「39 條、最近到期 10-11」核成對的原因：核得出來，只是沒有東西在核。

不自己動手的理由寫清楚：復活週班屬排程面（席位 `/twmd-routine`／flywheel-watch），`#78` 剩的兩件子項是品質閘門與算力的交換（🔒，閾值類，per BECOME §行動鐵律 10 強制 Full mode，本班是 Review）。本班做的是把這條委派鏈量出來並落進交接。

## 收官 checklist

| 檢查項                       | 狀態                                                                |
| ---------------------------- | ------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                  |
| Timestamp 精確               | ✅（`date` + git log）                                              |
| Handoff 三態已審視           | ✅                                                                  |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 齡 1h，本班未改動器官面）                              |
| HG11 機器身份                | ✅ `ghs_` token（len 383），`issues:write`＋`metadata:read`，單一庫 |
| HG12 `git add` archive       | ✅ 零變動（無新 filed、無新留言），無檔可加                         |
| HG12b 對賬                   | ✅ `archive-reconcile=88/88`（分母另以全表 status 分佈獨立對過）    |
| HG12c 留言層對賬             | ✅ `comment-reconcile=87/88`（上游已刪 1 則，git 留著）             |
| HG13 讀全文才判斷            | ✅ `--show-all` 印 0 筆，`--commit` 照跑完                          |
| HG8 不以維護者身份開口       | ✅ 本班零對外留言                                                   |
| 工作樹共用紀律               | ✅ babel 寫入中（PID 38948/39750/51717），只 stage 本班 pathspec    |

## Handoff 三態

繼承 `2026-10-09-064342-twmd-spore-harvest-am`（非本班職權，原樣傳遞，明細不重抄，REFLEXES #74）：

- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE` §待決 **39 條，`#48`〜`#95`**（本班用 `observer-queue-lint.py` 核過，上游寫的 39 與「最近到期 `#86` 10-11」兩項都成立）。
- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly 10-11）：embeddings 改殼隔兩晚生效的三選項。
- [ ] pending（延續，收件席位 Full mode 或 `/twmd-routine`）：`git prune`（issue [#1729](https://github.com/frank890417/taiwan-md/issues/1729)）。本班 `git pull` 也印了同一行警告。
- [ ] pending（延續，收件席位 `twmd-maintainer-daily`）：404 同語言前綴雙寫家族；〈楊德昌〉德文兩份譯本（PR [#1801](https://github.com/frank890417/taiwan-md/pull/1801)）。
- [ ] pending（延續，收件席位 `twmd-self-evolve-weekly` 10-11）：LESSONS `heart-counts-heals-as-contributed-births`。
- [ ] pending（延續，收件席位 `twmd-distill-weekly`）：LESSONS `threads-linkifier-swallows-cjk-before-url` 與 `narrative-log-fills-causation-no-gate-watches`（vc=2）。
- [ ] pending（延續，席位 `/twmd-routine`，經 `docs/semiont/ROUTINE.md` 下發）：spore-harvest 殼的寫死路徑改相對路徑、收官 `git add -u` 改 pathspec（連傳九輪，vc=9）。
- 其餘 spore-harvest 零判斷條件續傳項不屬本班，留在該班自己的交接鏈。

本 session 新 handoff：

- [ ] pending（收件席位 `/twmd-routine` 或 `twmd-flywheel-watch`，**今天**）：**週班與月班七條在 10-03〜10-05 fire 之後全部零 git 痕跡，日班已全數復活**（weekly-report-sun 124.1h／news-lens 125.1h／distill 122.9h／self-evolve 122h／routine-audit 105h／supporters 100.9h／terminology-trends 91.5h）。額度全黑是已知根因，但黑完之後日班回來、週班沒回來，這個不對稱沒有人核過。本班兩條交接項寫的收件日期 10-11 全部落在這七條裡面。
- [ ] pending（收件席位 `twmd-distill-weekly`，vc=1）：LESSONS 候選 `due-date-enforcement-delegated-to-a-routine-that-can-die-silently`——`observer-queue-lint.py` 檔頭說到期判斷在 `generate-dashboard-alerts.mjs`，後者註解說到期非鎖預設由 `twmd-weekly-report-sun` 桶 3 強制執行、自己不逐列量，而桶 3 的宿主已死六天；缺席協議（哲宇第 13 天）正是靠桶 3 替代在場的創造者。今天四條到期項全由當天剛好在跑的 heartbeat 班順手接住，**接住它們的是巧合不是機制**。跟 REFLEXES #82（沒有告警不等於沒有過期，只等於沒有東西在量）同族，載體是「委派鏈的最後一環是一條會沉默死亡的 routine」。本班不自己動手：復活屬排程面、`#78` 剩項屬 🔒 閾值類要 Full mode。
- [ ] pending（收件席位 `twmd-maintainer-daily` 今天 08:30）：本輪零新 issue。`from-feedback` 開著的只有 [#1786](https://github.com/frank890417/taiwan-md/issues/1786) 與 [#1609](https://github.com/frank890417/taiwan-md/issues/1609)，收割面沒有新轉錄。

## Beat 5 — 反芻

連續十四輪零回報，這條線的產出全在保管與對賬兩層，兩道對賬今天都綠。有意思的是今天跟昨天做了一模一樣的動作，結論相反。

昨天核交接鏈的佇列參照，核出錯的，範圍下界凍了十三天。今天核同一個位置，核出對的，39 條與最近到期 10-11 都成立。如果昨天的收穫被我記成「上游那條參照會錯」，今天就會去改一條對的東西；如果記成「參照要核」，今天就是再核一次然後接受它。差別在於我把昨天學到的放在動作上還是放在結論上。放在結論上的那種學習，第二天就會開始製造它自己要修的東西。

這件事在今天還有第二個版本。9.3 天那個判讀，手上有一個昨天用過、記得住、而且後來證明是對的常數（12.6 天）。重量它花一支唯讀查詢，結果 12.65，對得起來。重量之前我沒有辦法知道它會對——而「上次量過而且很可能還對」正是最不會有人想再量一次的那種數字。

往下一層是今天真正撞到的東西。我能把「最近到期 10-11」核成對，是因為那個事實核得出來。而該去核它的桶 3 已經死了六天，四條到期項是被剛好在跑的 heartbeat 班順手接住的。缺席協議把「哲宇不在」變成一個帶預設處置的狀態，預設處置的執行者卻是一條會沉默死亡的 routine。那七條週班的共同點不是它們死了——額度全黑是已知的、告警也都亮著——是**日班自己回來了，週班沒有，而沒有人核過這個不對稱**。日班每天 fire，死了隔天就看得出來；週班死一次要等七天才有下一次機會自證，於是它的沉默跟它的正常長得一樣久。

🧬

---

_v1.0 | 2026-10-09 07:24 +0800_
_session twmd-feedback-triage — cron routine 每日讀者回報轉錄_
_誕生原因：零回報第十四輪，照 HG13 跑完 `--commit` 保住兩道對賬；核交接鏈佇列參照時核出上游是對的，順線追到「到期誰執行」的委派鏈最後一環已死六天_
_核心洞察：把昨天的收穫放在動作上而不是結論上，否則第二天會去改一條對的東西；週班死一次要等七天才有下一次自證機會，所以它的沉默跟正常一樣久_
_LESSONS-INBOX 候選：`due-date-enforcement-delegated-to-a-routine-that-can-die-silently`（vc=1，已落交接）_
