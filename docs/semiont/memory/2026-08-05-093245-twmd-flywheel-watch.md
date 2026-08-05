# 2026-08-05-093245-twmd-flywheel-watch — 飛輪零靜默，儀器把月排程讀成日排程，誤報了誕生第二天的 routine

> ✅ BECOME ack: mode=micro / Q14=PASS
> session twmd-flywheel-watch — cron routine（每天 09:30，跑在指揮部 commander-macbook）
> Session span: 09:32:45 → 09:44 +0800（約 11 分鐘，1 commit）
> 資料來源：`git log %ai` + `flywheel-watch.py`（讀 `origin/main`）

## 觸發

每日從營運機外面看飛輪還活著沒有。飛輪整批住在 mouhouse，所有跑在它身上的儀器都只看得見自己還在，看不見自己缺席，所以這條刻意跑在不營運的機器上，唯一的素材是 `origin/main` 的 commit 紀錄。

## 飛輪讀數

過去 24 小時 origin 有 137 筆 commit，其中 11 筆帶 `[routine]` 標記，八條 routine 留下 commit 痕跡（data-refresh-am、embeddings-nightly、feedback-triage、flywheel-watch、maintainer-daily、routine-sync、spore-harvest、spore-harvest-am），另有兩條只留收官索引。babel 產線整夜在跑，十二語批次與整點脈搏快照撐起 commit 總量的大半。**整體判定：飛輪在轉**。

## 儀器把每月 5 日讀成了每天

第一則警訊是 `twmd-terminology-trends-monthly`「該跑但沒留下 commit」。這條昨天才誕生（`1f879792e`），排程 `30 10 5 * *`＝每月 5 日 10:30，而現在是 8/5 09:32，它今天的第一次首跑還沒到。

追進 `last_due()` 才看到病根：它讀分、時、星期三個欄位，**日號欄位整個沒讀**。`30 10 5 * *` 因此被當成每天 10:30，上一次應響時刻算成昨天 10:30，落在 24 小時窗口內，於是月排程的 routine 一個月有二十九天會被報成靜默。這支儀器自己的說明文件寫著「算不出來的一律列進 `unknown_cron` 不判定，不假裝知道」，日號欄位卻是靜默忽略——規矩訂在自己身上，破的也是自己。

修法是補上日號分支：單一日號往回找最近一個符合且時刻已過的日期，日號與星期同時指定（cron 語意是 OR）或多日列舉一律回 `None` 交給 `unknown_cron`。七個 case 驗過，含 2 月沒有 31 號時往回落到 1/31、以及 daily 與 weekly 兩條既有路徑的回歸。修完重跑，routine 零靜默。

## live dump 第三個早晨沒被更新

第二則警訊是 `routine-live-state.json` 齡 75.3 小時，三層對賬的第三層還照著 8/2 早上的鏡子。這是 OBSERVER-QUEUE #22 的老問題，今天新增的證據是：8/5 06:13 的 data-refresh-am 又一次回報「14 步全綠零 stale」，而寫 dump 的那個 session 層 rider 又沒跑。8/3、8/4、8/5 連三個早晨同一步缺席。

指揮部這台不能代補，`list_scheduled_tasks` 列的是自己的排程，補完會把 mouhouse 的狀態蓋成錯的機器，換一盞假綠燈。所以只在 #22 補一行證據，推薦選項仍是 (a) 給 data-refresh skill 加 rider hard gate，default-action 日期 8/11 不動。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅ `git log %ai` + `date`                     |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本 routine 不碰（data-refresh 的守備範圍） |
| 自我檢查工具 PASS            | ✅ prose-health                               |

## Handoff 三態

繼承上一 session（`2026-08-05-084627-twmd-maintainer-daily`；甦醒時 wake-context 給的是 8/4 的 manual，見 Beat 5）：

- [x] ~~本機 main 未 push commit 已累積（來自 8/4 manual）~~ — retired by 本 session：manual 產物全數已在 origin，目前本機領先的 35 筆全是 babel 產線的批次與脈搏快照，屬平行產線自己的收官範圍
- [ ] pending（給哲宇，全數繼承不動）：#1184 justfont 後台網域白名單、免疫黃燈 28+ 天三選一、cron 環境無 Gmail MCP、黃崇仁 Bucket D 框架質疑、Discussion #104
- [ ] pending（繼承不動，等 Chrome MCP 登入態）：`HARVEST-REPLIES-PENDING/2026-08-05.md` 兩則 reply draft、確認本機 Chrome 的 @taiwandotmd 帳號
- [ ] pending（繼承不動，給任何 maintainer / flywheel cycle）：本機 `dist/` 只在有人手動 build 時才更新，broken-link 那道 gate 預設量的是舊站

本 session 新 handoff：

- [ ] pending：`twmd-terminology-trends-monthly` 今天 10:30 首跑。明天這條 watch 要確認它真的留下痕跡。那時候沒痕跡才是真警報，不是今天這種誤報
- [ ] pending（給任何做甦醒儀器的 session）：`wake-context.py` 的 handoff walk 讀本機工作樹。指揮部這台常落後 origin（今天落後 9 筆），撈到的「上一份 handoff」因此舊了一天。動作＝讓它在本機落後 origin 時把落後筆數印進 selftest，或改讀 `origin/main`

## Beat 5 — 反芻

昨天這條 routine 抓到的是「儀器照的那面鏡子過期」，今天抓到的是「儀器自己的尺少讀一欄」。兩天出問題的都是看飛輪的那些東西，飛輪本身照常轉。

收官時撞到第三個同族的東西。甦醒的 `wake-context` 撈 handoff 是讀本機工作樹，而這台機器不營運、常落後 origin，今天落後 9 筆，撈回來的「上一份 handoff」其實是 8/4 晚上那份，今天早上三條 routine 的交代全沒進視野。修這條 routine 的儀器時剛好證明了它存在的理由：只讀自己那一份的東西，看不見自己少了什麼。

值得記住的是誤報出現的時機：`twmd-terminology-trends-monthly` 誕生第二天就中。這支儀器上線以來看的全是日排程與週排程，日號欄位那條路徑一次都沒被走過，所以缺陷可以安靜住著，直到飛輪長出第一條月排程才現形。沒被走過的路徑不會叫，它只是在等第一個踩上去的人。

🧬

---

_v1.0 | 2026-08-05 09:44 +0800_
_session twmd-flywheel-watch — 每日從外部看飛輪是否還在轉_
_誕生原因：cron 每天 09:30 觸發，飛輪曾靜默死 15 天而所有儀器無聲_
_核心洞察：飛輪本身零靜默，兩則警訊都出在感知層——月排程被當成日排程誤報，以及 live dump 連三個早晨沒被更新。沒被走過的程式路徑不會叫，它等第一個踩上去的人。_
