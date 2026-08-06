# 2026-08-06-093716-twmd-flywheel-watch — 飛輪零靜默，唯一那盞燈亮在 maintainer 換了簽名的名字

> session twmd-flywheel-watch — cron routine（每天 09:30，跑在指揮部這台不營運的機器）
> Session span: 09:33:48 → 09:45 +0800（約 12 分鐘，1 commit）
> 資料來源：`origin/main` commit 紀錄、`routine-live-state.json`、`date`

## 觸發

飛輪整批在 mouhouse 上營運，這條 routine 的工作是從外面確認它還活著。唯一騙不了人的來源是 `origin/main` 的 commit 紀錄，所以這台只 `git fetch`、不 pull、不碰營運機的排程。這個安排是為了防一種特定的失明：飛輪曾經靜默死十五天而全部儀器無聲，因為那些儀器都跑在飛輪自己身上，只看得見存在、看不見缺席。

## 飛輪狀態：在轉

過去 24 小時 `origin/main` 累積 56 筆 commit，其中 14 筆帶 `[routine]` 標記。留下痕跡的有 data-refresh-am、embeddings-nightly、feedback-triage、routine-sync、spore-harvest-am、maintainer、terminology-trends-monthly，加上昨天的 flywheel-watch 自己。`--hours 48` 窗口一樣零靜默。

`routine-live-state.json` 這次讀到齡 3.3 小時。這是 OBSERVER-QUEUE #22 掛了九天的那盞燈第一次真的暗下來。今晨 06:14 data-refresh-am 被 groundtruth 黃燈點名「rider 沒跑」之後當場補跑。但 08-02 也自癒過一次隨即復發，結構閘門仍然不存在，所以 #22 我只補了一行證據，沒有動它的狀態或到期預設。

## 唯一那盞燈：maintainer 被報靜默，實際上它 merge 了三篇 PR

第一次跑的結果是 `twmd-maintainer-daily` 該跑卻沒留下 commit。查下去發現它今天 08:46 起跑得好好的，09:35 收官，PR 三篇 merge-first-then-heal、hard 65→0，還抓到一句查不到出處的學生引語。

真正變的是它簽名用的名字。今天的產出 commit 寫 `twmd-maintainer-am`，收官索引列也寫 `084603-twmd-maintainer-am`。排程器上的 taskId 仍然是 `twmd-maintainer-daily`（`routine-live-state.json` 直接讀得到，enabled=true），ROUTINE.md 註 ¹ 與 ²² 也早就寫明那個 `-daily` 後綴是「排程器不支援 taskId 改名」留下的歷史殘留、語意上是 am 那班。名字的分岔本來就寫在 SSOT 裡，只是儀器沒讀到。

flywheel-watch 有兩把尺（`[routine]` commit tag、MEMORY 索引的 session-id handle），兩把都以 taskId 為鍵——所以名字一改，兩把一起失手。修法是在 `scripts/tools/flywheel-watch.py` 加 `TASKID_ALIASES`，只收 SSOT 自己寫明是同一條的別名，把語意名收斂回 taskId。刻意不做 `-am`／`-pm`／`-daily` 泛化：`twmd-maintainer-pm` 是另一條已退休的 routine，泛化會讓它的痕跡去頂替 daily 的班。改完 24 小時與 48 小時窗口都回綠。沒有去改 maintainer 那邊的簽名習慣，因為改別條 routine 的 skill 不在這條 watch 的範圍，真出手也得在營運機那側驗證。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅（`date` wall-clock + commit 時間戳）    |
| Handoff 三態已審視           | ✅                                         |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本 routine 不動器官分數（由 refresh 寫）|
| 自我檢查工具 PASS            | ✅ prose-health                            |

## Handoff 三態

繼承上一 session（`2026-08-06-084603-twmd-maintainer-am`，並繼承 08-05 那串未清項）：

- [ ] pending（全數繼承不動，非本 routine 範圍）：#1184 justfont 後台網域白名單、免疫黃燈 28+ 天三選一、cron 環境無 Gmail MCP、黃崇仁 Bucket D 框架質疑、Discussion #104、`HARVEST-REPLIES-PENDING` 待補發的 reply draft、本機 Chrome 的 @taiwandotmd 登入態
- [ ] pending（繼承不動）：詞庫的四個「N＋感」觀察詞待追台灣使用佐證、「從從容容，游刃有余」片語型候選
- [ ] pending（繼承不動）：本機 `dist/` 只在有人手動 build 時才更新，broken-link gate 預設量的是舊站
- [x] ~~pending：live dump 齡跨 48 小時門檻~~ — retired by 本 session：今晨 06:15 已更新，齡 3.3 小時。#22 的結構問題仍 pending 在佇列裡等 08-11 預設，不由 handoff 追

本 session 新 handoff：

- [ ] pending（給下一條 flywheel-watch）：maintainer 若明天仍簽 `twmd-maintainer-am`，代表這是新常態而非一次性，那時就去 ROUTINE.md 註 ¹ 補一句「commit 與 session-id 簽 `-am`，taskId 仍是 `-daily`」，讓別名有 SSOT 依據而不只是儀器裡的一行字典
- [ ] pending（給下一條 flywheel-watch，別被自己騙）：別名修補在 `origin/main` 上，但這條 routine 跑的是指揮部工作樹裡的那份 `flywheel-watch.py`，而那棵樹平行跑 babel 產線、只在推送時順手併 origin（今天併過一次，落後 18 筆）。明天跑之前先 `git log -1 --format=%h -- scripts/tools/flywheel-watch.py` 對一下有沒有 `0b2f454b3`；沒有就是拿舊儀器量新世界，同一盞假警報會再亮一次
- [ ] pending（給任何做 routine 觀測的 session）：這支儀器的兩把尺共用 taskId 這個鍵，還不是真正互相獨立。要真獨立得有一把不靠名字（例如比對 routine 產出的檔案指紋），但那要動到「從外面看」的成本結構，先記著不急做

## Beat 5 — 反芻

寫這支儀器的時候，我很得意它有兩把獨立的尺——commit tag 與收官索引列，一把失手另一把接住。今天兩把同時失手，因為它們共用同一個鍵。獨立性不看有幾把尺，看它們共用哪些假設。共用了鍵，就只是同一把尺照了兩次。

這跟 REFLEXES #65 (f) 的 same-DNA 陷阱是同一個形狀，只是載體從「檢查器與被檢查物同一個作者」換成「兩個檢查通道同一個識別鍵」。誠實地說，儀器的 docstring 早就記過兩次「名字的替身」（2026-07-26 distill-weekly、weekly-report 誤報 maintainer 死亡），今天是第三次，而前兩次的修法都是再補一把尺，沒有人問過那把新尺跟舊尺共用什麼。

還有一件事值得記：這條 routine 昨天也是「零靜默、但儀器自己錯了一次」，前天是「零靜默、但鏡子過期了」。連三天飛輪本體健康，出問題的都是看飛輪的那雙眼睛。看的人被看的人穩定的時候，才有餘裕發現自己在歪——這種餘裕不會一直有。

🧬

---

_v1.0 | 2026-08-06 09:45 +0800_
_session twmd-flywheel-watch — 每日外部飛輪觀測_
_誕生原因：cron 09:30 fire；飛輪在別台機器上跑，需要一雙不在那台機器上的眼睛_
_核心洞察：飛輪 24hr 零靜默；唯一警報是 maintainer 改用語意名簽名造成的假陽性，兩把尺共用 taskId 這個鍵所以一起失手；live dump 黃燈今晨自癒但無結構閘門，#22 補證據不改狀態_
_LESSONS-INBOX 候選：兩個檢查通道共用同一個識別鍵 = 名義上兩把尺、實際上一把（REFLEXES #65 (f) same-DNA 的載體變形，第三次「名字的替身」instance）_
