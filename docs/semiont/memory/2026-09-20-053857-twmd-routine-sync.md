# 2026-09-20-053857-twmd-routine-sync — 第 54 輪對賬：分岔併完後第一輪，rewrite-daily 的機器 prompt 追上昨天中午的 REWRITE 產線整併

> session twmd-routine-sync — cron routine（每日 05:30 Asia/Taipei）
> Session span: 05:30 排程 fire → 05:41 +0800（~11 分鐘，1 commit `9a9a72cc3` + 本 memory commit）
> 資料來源：`git log %ai` + `routine-sync.py` 三次輸出 + `git rev-list --left-right --count HEAD...origin/main`

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

排程任務。讓這台機器的 routine prompt 與排程設定跟 git SSOT 三層對賬，排在晨鏈之前。前一輪（09-19 第 53 輪）是分岔期間的最後一輪，靠手動比對 origin 才抓到哲宇 ship 的 news-lens 改動；當天上午 maintainer-am 把十天的分岔併完，所以這是合併後第一次對賬。

## 分岔沒了，儀器回到能看見全貌的狀態

`git fetch` 之後本機領先 origin 7、落後 0，領先的七個全是 babel dispatcher 凌晨的批次 commit，`git pull` 回「已是最新」。上一輪擔心的「本機 git 看不到 origin 側 SSOT」這個盲區，這一輪不存在：本機 git 就是 SSOT 全貌。

`routine-sync.py` 報 18 條裡 1 條漂移：`twmd-rewrite-daily` prompt-drift。diff 只有一行，git 版指向 `REWRITE-PIPELINE-SINGLE.md`，機器版還指向 `REWRITE-PIPELINE.md`。追 git log 是昨天 11:28 的 `3f9ba3fe5`（REWRITE 產線整併：v9 多檔型搬 archive、單檔型成為現行），機器檔案 mtime 停在 7 月 24 日。昨天 05:39 那輪跑在整併之前，所以今天才看到，方向沒有疑義。`--apply --stamp 2026-09-20` 把 prompt 寫進 `~/.claude/scheduled-tasks/`，舊版存證 `reports/routine-prompt-drift/2026-09-20-exhibitions-mac-mini-local-twmd-rewrite-daily.md`，再跑一次 18/18 exit 0。cron 與 enabled 沒有 ⏰／🔌 行，不需要動 MCP。

一個順帶的觀察：`twmd-rewrite-daily` 本身是 ⏸️ 暫停狀態（ROUTINE.md 註 ²¹，兩台皆停，改手動觸發）。同步一條停用 routine 的 prompt 仍然正確：停用的判準在 enabled 那一層，prompt 那一層照樣要跟 SSOT 走，否則哪天重新打開時第一班會讀到一份指向已歸檔 pipeline 的指令。

`9a9a72cc3` 只帶存證檔一個，scope 驗過；push 順利，pre-push 三道閘全綠，順便把 babel 那七個 commit 一起推上去（它們本來就在 main 上，dispatcher 自己的 push 節奏是下一輪次邊界）。推完 0/0。

收官時照 LESSONS 寫入格式先查 DNA：第 53 輪那條「對賬工具在分岔期間對 origin 盲」的教訓，REFLEXES #67 子規則（09-13 fold）已經把「routine mirror 對賬工具住在 mirror 裡」列成同構候選，所以不開新 inbox entry，改在該子規則補一行驗證（vc=3）並更新 REFLEXES frontmatter。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅                                               |
| Handoff 三態已審視           | ✅（分岔相關三條 retired，工具候選降回 pending） |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無器官狀態變更）                     |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile）        |

## Handoff 三態

繼承自 09-19 第 53 輪：

- [x] ~~⏳ blocked：main 本機分岔，雙邊譯文取捨等哲宇選 A/B/C（OBSERVER-QUEUE #68／本機側 #56）~~ — retired by 2026-09-19 maintainer-am：哲宇 in-session 拍板 #68 選 B，843 檔衝突當天上午併完；本輪實測 HEAD 與 origin 0/0。
- [x] ~~pending：下一班 news-lens-weekly 第一次帶 Stage 3.5 跑，注意 `git pull` 在分岔期間會失敗、`reports/probe/2026-09-18.md` 本機沒有~~ — retired by 2026-09-20 news-lens-weekly `778f33dfe`（01:15 已跑，分岔已併所以兩個顧慮都不成立；`reports/probe/2026-09-20.md` 落檔）。
- [x] ~~pending：分岔合併時留意 `bbc0694cc` 五檔 blob 與 origin 相同~~ — retired by 2026-09-19 合併 `e419e2aa7`，無衝突。
- ⏳ blocked：issue #1729（馬英九腳註）等 FACTCHECK Full mode；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板（ROUTINE.md 註 ¹³）。
- ⏳ blocked：issue #1733（用語庫「消息」判定）等維護者判斷。

本 session 新 handoff：

- [ ] pending（工具候選，1-file，急迫度降回一般）— `routine-sync.py` 對賬前 `git fetch`，本機 HEAD 與 `origin/main` 在 `docs/semiont/routine-prompts/` 與 `ROUTINE.md` 有差時印一行 `🌐 origin 側 routine 層與本機不同（N 檔）` 並讓 exit 非 0。分岔併完後這個盲區暫時關上，但下一次分岔（maintainer 現在有 `merge-divergence.py` 職責，理論上不會再拖十天）它會原樣回來。參照：REFLEXES #67 子規則（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`，本輪已在該子規則補一行驗證，vc=3）。

## Beat 5 — 反芻

第 53 輪的教訓是「儀器只量它被設計來量的那一段」，今天那一段又量得到了，因為外面的分岔被別班修掉了，而這條 routine 什麼都沒改。連續十一輪綠燈、一輪靠手動抓到、然後又是綠燈：三種狀態下儀器印出來的字一模一樣，差別全在儀器外面的世界。這一輪唯一真的做的事是把一條停用 routine 的 prompt 對齊到昨天的整併，五分鐘的機械工作；反芻留給一句話就夠：綠燈回來的原因值得記，因為它回來的方式（別人修好了前提）跟它下次消失的方式會是同一個。

🧬

---

_v1.0 | 2026-09-20 05:41 +0800_
_session twmd-routine-sync — 第 54 輪 cron 對賬，分岔併完後第一輪；rewrite-daily prompt 追上 REWRITE 產線整併_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發_
_核心洞察：三層對賬的綠燈只證明本機三層一致，它回來的原因（分岔被 maintainer 併掉）在這條 routine 之外；停用 routine 的 prompt 照樣要跟 SSOT 走，停用是 enabled 層的事。_
