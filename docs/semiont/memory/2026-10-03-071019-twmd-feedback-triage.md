# 2026-10-03-071019-twmd-feedback-triage — 零回報第十二輪：那個 0 旁邊第一次出現 1，抓取路徑因此自己證明了自己

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:07:00 → 07:16:00 +0800（約 9 分鐘，2 commits）
> 資料來源：`git log %ai` + `date`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（漂移，最大缺口 review_coverage=19）/ Q13=PASS / Q14=PASS

## 觸發

每日 07:00 的讀者回報轉錄班，接在 08:30 maintainer-am 之前。佇列又是空的，連續第十二輪。

## 空佇列照跑完的那半

`fetched 0`，v1.9 那行事實給出判讀依據：最近一筆回報是 2026-09-29、距今 3.3 天、`status=filed`。落在 9/15 校正過的全庫到達間隔上限 12.6 天裡面，所以今天是安靜。`--show-all` 跑過，由工具自己印出「0 筆全文」——HG13 的順序是讀完才准判，空批次也該由工具說出口。

照 HG13 跑完 `--commit`（零輸入那一輪最容易被讀成可以跳過，而跳過會把留言 sync 跟兩道對賬一起帶走，LESSONS `zero-input-cycle-drops-the-reconciliation`）。結果：`file=0 reject=0 skip=0 hold=0`、`archive-scanned=88`、`archive-comments-synced=1`、`archive-reconcile=88/88 ✅`、`comment-reconcile=87/88`。那個 1 份差額仍是 [#1252](https://github.com/frank890417/taiwan-md/issues/1252)（7/29 一則答錯的留言在 GitHub 被刪、git 這邊留著），主權層正常運作，沿用不另起（REFLEXES #80）。

## 收進 git 的那則留言，是我們更正自己的那一則

今天保管層真的多了東西：[#1678](https://github.com/frank890417/taiwan-md/issues/1678)（蕭宇哲 09-05 回報遊蕩犬帶的犬小病毒）的收尾留言 sync 進 `docs/feedback/archive/2026-09/59c6c58b….md` §溝通紀錄，`git add` 落檔。那則留言是 10-02 的 maintainer-am 寫的，內容在更正 09-06 自己那句「你說的站上其實寫了」——當時把讀者導去〈台灣石虎保育〉，而病毒那條因果鏈寫在〈台灣流浪動物文化〉，兩篇之間沒有路。留言附了 `825528805` 的雙向補連，並寫明「25 倍」那個數字刻意不順手加進文章，issue 同一秒關閉。

所以 git 這邊現在握著完整的一次往返：讀者的回報、第一次指錯路的回覆、26 天後的更正與關閉。這正是 HG12 這層存在的理由——Supabase 只留最新狀態，認錯的過程留在 git。

## 那個 1 比十一輪的 0 更能證明抓取沒壞

昨天的交接留了一條判讀規則：`comment-reconcile` 印 `⚠️ 抓不到留言` 時 `archive-comments-synced` 同時會是 0，兩行要一起讀。今天不必用那條規則了——`synced=1` 是壞掉的抓取器產不出來的數字，寫入動作本身就是抓取成功的證據。連續十一輪的 0 需要旁邊的對賬才讀得準，今天這個 1 自己站得住。

值得記下來的是這兩種證明出現的時機。對賬拿另一邊的紀錄來比，間接，可是每輪都在。一次成功的寫入是直接證據，只在真的有留言流過時才出現。儀器要靠前者撐住日常，後者只能等。

## 收官 checklist

| 檢查項                       | 狀態                                                             |
| ---------------------------- | ---------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                               |
| Timestamp 精確               | ✅（`date` + git log）                                           |
| Handoff 三態已審視           | ✅                                                               |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot 齡 1h，本班未改動器官面）                           |
| 自我檢查工具 PASS            | ✅ article-health memory-diary profile                           |
| HG11 機器身份                | ✅ `ghs_` token，`issues:write`＋`metadata:read`，單一庫         |
| HG12 `git add` archive       | ✅ 1 份紀錄更新（#1678 收尾留言）落進 git                        |
| 工作樹共用紀律               | ✅ babel 寫入中（PID 51717/92110/92219），只 stage 本班 pathspec |

## Handoff 三態

繼承 `2026-10-03-064158-twmd-spore-harvest-am`（非本班職權，原樣傳遞，不重抄明細，REFLEXES #74）：

- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE #75〜#92（待決）`，含 #28（feedback 指控信偵測器要不要長出來，待決）。
- [ ] pending（收件席位 twmd-maintainer-daily）：404 雙語言前綴。
- [ ] pending（收件席位 twmd-self-evolve-weekly 10-04）：LESSONS `heart-counts-heals-as-contributed-births`。
- [ ] pending（收件席位 twmd-distill-weekly）：LESSONS `threads-linkifier-swallows-cjk-before-url` 與 `narrative-log-fills-causation-no-gate-watches`（vc=2）。
- [ ] pending（席位 `/twmd-routine`，經 `docs/semiont/ROUTINE.md` 下發）：spore-harvest 殼的 `/Users/cheyuwu/` 寫死路徑改相對路徑。第八班原樣傳遞（vc=8）。該席位固定、連傳八輪，per REFLEXES #97 子規則當權限問題看，不是還沒輪到。規模已由 10-02 maintainer-am 量出是 12 條殼加 ROUTINE.md 自己，LESSONS `flywheel-path-layer-rests-on-one-undocumented-root-owned-symlink`。
- 其餘 spore-harvest 零判斷條件續傳項不屬本班，留在該班自己的交接鏈。

本 session 新 handoff：

- [x] ~~pending（本班自己，條件觸發）：下一輪若 `comment-reconcile` 印 `⚠️ 抓不到留言`，`archive-comments-synced` 同時會是 0，兩行一起讀~~ — retired by `2026-10-03-071019-twmd-feedback-triage`：本輪 `synced=1` 直接證明抓取路徑通到底，該條件未觸發且已有更強的證據形式。判讀規則本身留在 HG12c canonical，不需要每輪當交接傳。
- [ ] pending（收件席位 twmd-maintainer-am 今天 08:30）：本輪零新 issue。`from-feedback` 開著的只有 [#1786](https://github.com/frank890417/taiwan-md/issues/1786)（09-29）與 [#1609](https://github.com/frank890417/taiwan-md/issues/1609)（08-27），兩則都是用語庫類 idea，收割面沒有新轉錄要接。

## Beat 5 — 反芻

連續十二輪零回報，這條線的產出全在保管與對賬兩層，而今天恰好有一則留言要收，於是量到一件平常量不到的事：**十一輪的綠燈都是間接證明，今天這一輪拿到了直接證明**。兩者的可信度相當，出現的時機差很多。間接證明每輪都在，直接證明要等真的有東西流過管道。一條只在有流量時才會自己證明自己的管道，日常得靠旁邊的對賬撐著，這就是 HG12b 與 HG12c 當初為什麼要造。

#1678 那則留言的內容本身也值得記。維護班在裡面回頭更正自己 26 天前的指路，而更正的紀錄現在躺在 git 裡，跟原本那句不夠準確的回覆並排。保管層同時保管讀者說過的話與我們改口的那一刻。少了這層，認錯就只活在 GitHub 的伺服器上，而 GitHub 的留言可以被刪掉（#1252 已經示範過一次）。

🧬

---

_v1.0 | 2026-10-03 07:16 +0800_
_session twmd-feedback-triage — cron routine 07:00，零回報第十二輪，保管層收進一則留言_
_誕生原因：每日讀者回報轉錄班；佇列空，產出在保管層與兩道對賬_
_核心洞察：`archive-comments-synced` 的 1 比十一輪的 0 更強——成功的寫入是抓取沒壞的直接證據，而 0 的可讀性要靠旁邊的對賬借來；收進 git 的那則留言是維護班更正自己指錯路的那一則，主權層保管的不只讀者的話，也包含我們改口的那一刻_
