# 2026-09-18-053800-twmd-routine-sync — 第 52 輪對賬 18/18 in-sync，連續第十一輪零漂移；首次加驗 origin 側 routine 層亦零差異

> session twmd-routine-sync — cron routine（每日 05:30 Asia/Taipei）
> Session span: 05:38:00 → 05:38:06 +0800（~6s 對賬，0 commits 在對賬本身）
> 資料來源：`git log %ai` + `git rev-list --left-right --count origin/main...HEAD` + `git diff --stat HEAD origin/main -- docs/semiont/routine-prompts/`

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

排程任務。讓這台機器的 routine prompt／排程設定跟 git SSOT 三層對賬，排在晨鏈（data-refresh／harvest／feedback／maintainer）之前，確保晨鏈醒來時讀到的是對齊過的 prompt。

## 三層對賬

`python3 scripts/tools/routine-sync.py` 跑出 18/18 `in-sync`，exit=0。沒有 prompt 漂移，也沒有 cron／enabled 狀態漂移，照 SOP「exit 0 = 三層一致，安靜收工」不動任何檔案。這是連續第十一輪零漂移（第 48～51 輪：2026-09-14／15／16／17 皆零漂移，本輪第 52）。

## 補了一把之前沒量的尺：origin 那側的 routine 層

前幾輪的判讀有一個縫：`routine-sync.py` 拿來當 SSOT 的是本機 git，而本機 main 落後 origin 五百多個 commit。`check-parallel-actor.sh` 今天直接把這點印出來（「讀取層同時失真：本地 ls / cat 反映的是 548 個 commit 前的狀態」）。也就是說，若哲宇或另一台機器在裁決期間對 origin ship 了 routine 改動，本機三層再怎麼一致也看不到，這正是這條 routine 存在要抓的那種分岔。

本輪加做一個唯讀交叉檢查：`git diff --stat HEAD origin/main -- docs/semiont/routine-prompts/ docs/semiont/ROUTINE.md scripts/tools/routine-sync.py` 為空，且 merge-base 之後 origin 沒有任何 commit 碰過 routine 層。結論是本機三層與 origin 的 routine SSOT 四方全部一致，本輪零漂移的判斷這次有 origin 側背書，而非只有本機自證。這個檢查應該進 routine prompt 或 `routine-sync.py` 本身（見 handoff）。

## Main 分岔續漲，本輪不碰

`git rev-list --left-right --count origin/main...HEAD` 顯示 `548 757`（behind 548／ahead 757；前夜第 51 輪是 ahead668/behind203——ahead +89，behind 一夜 +345，origin 側漲幅首次遠大於本機側）。behind 暴漲的來源要看 origin 側 commit 才知道，不在本 routine 職責內，留給裁決者判讀。`check-parallel-actor.sh` 回報 `ACTOR_BUSY`：babel/lang-sync writer process 仍在跑（PID 31458 等六個），working tree 有 31 個 babel dispatcher 正在寫的 modified／untracked 檔。照既有判讀（memory 2026-09-13～17 routine-sync 五則）跳過 `git pull`，只 `git fetch`，不 `git add` 任何非本 session 的檔。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅                                        |
| Handoff 三態已審視           | ✅（新增一條 pending，繼承既有 blocked）  |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無狀態變更）                  |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile） |

## Handoff 三態

繼承（不變，本輪未觸碰）：

- ⏳ blocked：main 本機分岔（ahead757/behind548），雙邊獨立譯文取捨等哲宇選 A/B/C（origin 側 OBSERVER-QUEUE #68／本機側 #56 撞號，推薦 B）；安全網分支 `20260912-unpushed-routine-queue` 續追。
- ⏳ blocked：issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程；`twmd-spore-pick-daily` / `twmd-spore-publish-daily` 停用三個月未拍板。
- ⏳ blocked：issue #1733（讀者質疑用語庫「消息」判定）等維護者判斷是否升 `needs-verification`。

本 session 新 handoff：

- [ ] pending（工具候選，1-file）— `routine-sync.py` 對賬前先 `git fetch`，把 `origin/main:docs/semiont/routine-prompts/` 也納入比對；本機 HEAD 與 origin 在 routine 層有差異時印一行 `🌐 origin 側 routine 層與本機不同（N 檔）`，不自動 apply。分岔期間「本機三層一致」跟「與 SSOT 一致」是兩件事，今天靠手動 diff 補上，下一班可以直接寫進儀器。

## Beat 5 — 反芻

第十一輪零漂移，routine 本身沒有新東西。今天的差別在於回頭問了一句：這條 routine 的尺量的是什麼？它量的是「機器 vs 本機 git」，而本機 git 在分岔期間已經不是 SSOT 的全貌。連續十輪綠燈都建立在一個沒說出口的前提上（本機 git ≈ origin），前提在 9 月初分岔後就不成立了，只是沒人把它跟這條 routine 連起來看。今天用一行 diff 把前提補驗，結果剛好還是綠的，所以沒有東西壞掉；但它讓「零漂移」這個結論多了一個 origin 側的證人，這比綠燈本身有價值。

🧬

---

_v1.0 | 2026-09-18 05:38 +0800_
_session twmd-routine-sync — 第 52 輪 cron 對賬，零漂移零動作；首次交叉驗 origin 側 routine 層_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發_
_核心洞察：分岔期間「本機三層一致」與「與 SSOT 一致」是兩個命題，routine-sync.py 只量前者；origin 側 routine 層本輪 diff 為空，零漂移結論首次有 origin 背書。behind 一夜 +345 是 origin 側新形狀，歸裁決者判讀。_
