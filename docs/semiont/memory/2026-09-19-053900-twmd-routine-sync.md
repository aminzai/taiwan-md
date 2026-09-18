# 2026-09-19-053900-twmd-routine-sync — 第 53 輪對賬：本機三層一致，但 origin 側藏著哲宇前一天 ship 的 news-lens 探測器改動，取回並同步到機器

> session twmd-routine-sync — cron routine（每日 05:30 Asia/Taipei）
> Session span: 05:36 → 05:39:16 +0800（~4 分鐘，1 commit `bbc0694cc`）
> 資料來源：`git log %ai` + `routine-sync.py` 兩次輸出 + `git diff --stat HEAD origin/main -- <routine 層>`

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

排程任務。讓這台機器的 routine prompt 與排程設定跟 git SSOT 三層對賬，排在晨鏈之前。上一輪（09-18 第 52 輪）handoff 留了一句：分岔期間「本機三層一致」跟「與 SSOT 一致」是兩件事，儀器只量前者，交叉比對 origin 側要手動做。今天那道手動比對第一次抓到東西。

## 本機全綠，origin 那側不是

`routine-sync.py` 第一次跑 18/18 in-sync，exit 0。照 SOP 這裡可以安靜收工。但接著跑上一輪補的那行 `git diff --stat HEAD origin/main -- docs/semiont/routine-prompts/ docs/semiont/ROUTINE.md`，出來兩個檔有差：ROUTINE.md v2.25→v2.26，`twmd-news-lens-weekly.md` 多了一段 Stage 3.5。追到 origin 的 `35927d795`，哲宇 09-18 13:44 從 commander-macbook 親手 ship 的：探測器（外部媒體掃描 × 知識庫缺口）停擺 138 天後接回 news-lens-weekly 當第四源，ROUTINE.md 註 ²⁶ (b) 明寫「不用在營運機新建排程項目，`twmd-routine-sync` 05:30 會把新 prompt 同步過去」。

也就是說，這條 routine 被哲宇當成交付管道寫進了 canonical，而它的儀器在分岔期間根本看不見要交付的東西。本機 main 領先 826 落後 737，那個 commit 在落後的那 737 裡。

## 怎麼取回

方向沒有疑義（origin 新、本機舊、哲宇本人 ship），所以動手。整個 commit cherry-pick 不行，它還改了一個只存在 origin 的 memory 檔，會撞 modify/delete 衝突。改成逐檔 `git checkout origin/main --`：routine 層兩檔，加上 prompt 直接指到的 `EVOLVE-PIPELINE.md §news-lens-probe-output` 與 `twmd-news-lens`、`twmd-probe` 兩個 skill。五個檔在 merge-base 之後本機零改動、工作樹乾淨，取回後逐一 `git hash-object` 對 `origin/main:<path>` 全部相同，pre-commit prettier 跑過之後再驗一次仍相同。後三個檔超出 SOP 列的 `git add` 範圍，但只同步 prompt 而不帶它指到的 pipeline 段落，等於在這台機器排一條指向不存在章節的 routine；三個檔跟 prompt 是同一個 origin commit 的一個單位，一起取回，這裡明記。

取回後 `routine-sync.py` 如預期報 `twmd-news-lens-weekly prompt-drift`（git 新），`--apply --stamp 2026-09-19` 把 prompt 寫進 `~/.claude/scheduled-tasks/`，舊版存證 `reports/routine-prompt-drift/2026-09-19-exhibitions-mac-mini-local-twmd-news-lens-weekly.md`，再跑一次 18/18 exit 0。cron 與 enabled 沒有 ⏰／🔌 行，不需要動 MCP。`bbc0694cc` 六個檔 scope 驗過。

Push 照前五輪處置延後：737 落後加上 babel dispatcher 手上 28 個髒檔，pre-push 的 rebase 會跨過 🔒 的分岔決策（OBSERVER-QUEUE 本機 #56／origin #68）。這次延後不損失任何東西，五個檔的內容本來就在 origin，同步方向是 origin→機器。

## 收官 checklist

| 檢查項                       | 狀態                                               |
| ---------------------------- | -------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                 |
| Timestamp 精確               | ✅                                                 |
| Handoff 三態已審視           | ✅（上一輪工具候選升為第一優先，繼承既有 blocked） |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無器官狀態變更）                       |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile）          |

## Handoff 三態

繼承（不變，本輪未觸碰）：

- ⏳ blocked：main 本機分岔（本輪 ahead827/behind737），雙邊獨立譯文取捨等哲宇選 A/B/C（origin 側 OBSERVER-QUEUE #68／本機側 #56 撞號，推薦 B）；安全網分支 `20260912-unpushed-routine-queue` 續追。
- ⏳ blocked：issue #1729（馬英九腳註）等 FACTCHECK Full mode；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板。
- ⏳ blocked：issue #1733（用語庫「消息」判定）等維護者判斷。

本 session 新 handoff：

- [ ] pending（工具候選升第一優先，1-file，本輪實證）— `routine-sync.py` 對賬前 `git fetch`，把 `origin/main:docs/semiont/routine-prompts/` 與 `ROUTINE.md` 納入第四方比對；本機 HEAD 與 origin 在 routine 層有差時印一行 `🌐 origin 側 routine 層與本機不同（N 檔，最新 commit <hash>）` 並讓 exit 非 0，不自動 apply。上一輪寫的是「應該進儀器」，本輪證明不進儀器就靠當班記得手動 diff——今天記得了，下次不一定。
- [ ] pending（下一班 news-lens-weekly，09-21 週日 01:00）— 第一次帶 Stage 3.5 跑。開場的 `git pull origin main` 在分岔期間會失敗，照其他 routine 的處置改 fetch；EVOLVE-PIPELINE §news-lens-probe-output 與兩個 skill 本機已有（`bbc0694cc`），格式範本 `reports/probe/2026-09-18.md` **本機沒有**，要用 `git show origin/main:reports/probe/2026-09-18.md` 看。
- [ ] pending（分岔合併時留意）— `bbc0694cc` 五個檔 blob 與 origin 相同，merge 時應無衝突；若走 rebase 會被當重複 patch 自動丟掉，都正常。

## Beat 5 — 反芻

連續十一輪零漂移，第十二輪本機還是零漂移，差別只在上一輪多問了一句「origin 那側呢」。今天那句話有了答案。哲宇把這條 routine 寫進 canonical 當作新 prompt 到營運機的唯一通道，而這條 routine 在分岔期間是盲的：它量機器對本機 git，本機 git 對 origin 的那一段沒有人量。連續綠燈建立在一個前提上，前提失效的那天綠燈照樣亮。上一輪把補驗寫成 handoff 是對的，但 handoff 傳遞的是資訊，不是急迫性（REFLEXES #15 第 13 次驗證）；這次是當班剛好照做了才抓到，下一個當班不一定。所以工具候選從「應該」升成「第一優先」。

🧬

---

_v1.0 | 2026-09-19 05:39 +0800_
_session twmd-routine-sync — 第 53 輪 cron 對賬，本機零漂移但 origin 側 news-lens 探測器改動取回並同步到機器_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發；上一輪 handoff 的 origin 側交叉比對首次命中_
_核心洞察：儀器只量它被設計來量的那一段；分岔期間 SSOT 的全貌在本機 git 之外，連續綠燈證明的是「本機三層一致」而非「與 SSOT 一致」。哲宇把 routine-sync 當交付管道寫進 canonical 的同一天，管道對交付物是盲的。_
