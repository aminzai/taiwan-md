# 2026-10-02-064118-twmd-spore-harvest-am — 讀者在李洋那支問「清晨四點？」，回了五點半；昨天的分享 632 是讀錯

> session twmd-spore-harvest-am — cron 06:30 daily audience flywheel cycle
> Session span: 06:30 → 06:50 +0800（約 20 分鐘，2 commits）
> 資料來源：`date`、`git log %ai`、`session-id.sh`、留言頁 `time[datetime]`

## 觸發

每日孢子回聲收割。甦醒走 Write mode，wake-context 讀到 `wake:END`，自檢全綠；免疫 59 仍是最低器官。SPORE-HARVEST-PIPELINE v3.2 全檔讀完。窗口內沒有孢子（最新 #175／#176 已 D+40），`backfillWarnings` 0 條，所以本班就是掃兩個動態頁。

## 一則 C 桶留言，五個半月後回到同一個錯

`list_connected_browsers` 第一次就連上，不用 `open -a`。`/activity/replies` 多了一列：@eddie_pablo 10-01 08:55 在 #29 李洋底下問「清晨四點？搭四條捷運？」。

這是 04-14 的老傷。孢子正文寫「每天清晨四點多從中和搭四條捷運」，是從英文摘要推出來的場景；《少年報導者》原文是五點半起床、媽媽騎機車載到南勢角站趕首班車、轉三次車經四條線。當時文章當天就改了，哲宇也在原串留言更正，但正文改不了，這位讀者五個半月後直接從正文讀到舊版本。歸 C 桶，照表必發。發之前確認了三件事：線上中文頁「5 點半起床」出現 4 次，`knowledge/People/李洋.md` 第 93、116、285 行與腳註 [^23] 都對，十二個譯本也全是 5:30，錯誤只活在孢子正文。

回覆承認寫錯、交代原文怎麼說、附上文章網址，06:44:47 發出（`Dd-AxbXk9qa`）。按一次發佈後 container 數 2→2，因為行內回覆框把新回覆渲染在同一個 container 裡；照 Pitfall 6 不重試，改重新載入 @eddie_pablo 的留言頁驗證，只有一筆，連結卡片顯示「李洋 | Taiwan.md」。retry 0。

寫回覆的過程踩到兩個編輯器坑，發佈前從 `innerHTML` 抓到：`insertText` 字串裡的換行被吃掉，🧬 黏在網址後；第一版「5 點半起床⋯⋯改過：taiwan.md/…」被 Threads 的連結偵測從「5 」後的空白一路包到網址，變成 `http://點半起床…` 的假連結，畫面上只是一片藍字。改寫成「五點半」、網址獨立一行、換行用 `shift+Enter` 鍵入才乾淨。已進 LESSONS `threads-linkifier-swallows-cjk-before-url`。

## #29 重抓，以及昨天那個 632

新留言符合昨天交接寫的重抓條件。從留言頁點主貼進 canonical：views「36 萬」、likes 3.1 萬、留言 229（@eddie_pablo 加我們的回覆）、轉發 1,125、分享 532。

分享數對不上昨天。序列是 529（09-18）→ 530（09-27）→ 632（10-01）→ 532（今天），632 是讀錯。昨天那班在 batch log 與 memory 都寫了「四天分享 +102，有人在私訊或站外轉」，還用它替私訊夾那條交接加了理由；三層敘事長在一個讀錯的數字上，`validate-spore-data.py` 全綠。處置：10-01 的事件用同一個 (spore, batch, dPlus) 重寫成不帶 shares（真值不知道，不補猜的），昨天的 batch log 末尾加更正段、原文保留；今天的事件 D+171 照實寫。這是 LESSONS `narrative-log-fills-causation-no-gate-watches` 第二例（vc=2），那條的修補候選 (b)「相鄰事件落差過大就亮燈」正好會在寫入當天擋下它。

`/activity` 全部分頁在昨天那班之後只有按讚與一筆轉發（雙胞胎記帳本、📡、女巫店、報導者等舊孢子），沒有別支過開啟門檻。衍生層重生後驗證全綠，`764effd42` 五檔，scope 驗過。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ✅                                                       |
| Handoff 三態已審視           | ✅                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官狀態變動）                                     |
| 自我檢查工具 PASS            | 見 commit 前 `article-health.py --profile=memory-diary`  |
| Pitfall 6 retry 次數         | 0（1 則回覆，一次發佈成功）                              |
| Tab group cleanup            | ✅ 已關，group 自動移除                                  |
| diary                        | skipped：routine 例行，反芻留在本檔 Beat 5               |
| evolve                       | skipped：兩個缺口都進 LESSONS，pipeline 改動留給 distill |

## Handoff 三態

繼承 `2026-10-02-060323-twmd-data-refresh-am`（非本班職權，原樣傳遞，不重抄明細，REFLEXES #74）：

- ⏳ blocked（延續，哲宇）：OBSERVER-QUEUE 待決項。
- [ ] pending（延續，收件席位 twmd-maintainer-daily）：404 雙語言前綴 `/ja/fr/...`。
- [ ] pending（延續，收件席位 twmd-self-evolve-weekly 10-04）：LESSONS `heart-counts-heals-as-contributed-births`。

繼承 `2026-10-01-064123-twmd-spore-harvest-am`：

- [ ] pending（零判斷，條件續傳）：`list_connected_browsers` 回 `[]` 時先查 `--no-startup-window` 再 `open -a`。今天沒觸發。
- [x] ~~pending（零判斷）：掃 `/activity/replies` 逐則對 `time[datetime]`~~，今天撈到 @eddie_pablo（retired by 本班）。**條件原樣續傳**，每班照做。
- [x] ~~pending（零判斷）：#29 下次重抓，條件「1.6 萬」或回覆分頁出現 #29 新列或留言數不是 227~~，今天因新列觸發（retired by 本班）。**新條件**：聚合到「1.6 萬」，或回覆分頁出現 #29 新列，或留言數不是 229。
- [ ] pending（零判斷）：開 permalink 查新留言時先切「全部＋最新」排序。本輪從回覆分頁直接進留言頁，沒用到，未驗。
- [ ] pending（席位：任何帶 permalink 巢狀展開能力的 session）：#29 兩則位置不明的留言（225→227），不急。
- [ ] pending（席位 `twmd-routine-sync`／`twmd-self-evolve-weekly`）：REFLEXES #97 fold 後還剩什麼要儀器化。
- [ ] pending（給 spore-pick）：#175／#176 公告型孢子一週燒完，同型主題不排 D+30 milestone。
- [ ] pending（低優先，等哲宇在場）：Threads 私訊夾是否納入受眾飛輪，建議週報桶 3 登記 OBSERVER-QUEUE。**昨天加上的「分享 +102」理由作廢**（632 是讀錯），這條回到原本的分量。
- [ ] pending（席位 `/twmd-routine`，改 `docs/semiont/ROUTINE.md` §TWMD spore harvest (am) 後由 routine-sync 下發）：殼的 `/Users/cheyuwu/` 改相對路徑、收官 `git add -u` 改 pathspec。今天第六班繞開（vc=6）。

本 session 新 handoff：

- [ ] pending（收件席位 twmd-distill-weekly）：LESSONS `threads-linkifier-swallows-cjk-before-url` 的發佈前 `<a href>` 檢查，跟 `narrative-log-fills-causation-no-gate-watches`（vc=2）的相鄰事件落差警示，兩條都是 SPORE-HARVEST-PIPELINE 一段話或 `spore-db.py` 幾行的量。

## Beat 5 — 反芻

那個錯四月就修好了，文章、譯本、更正留言全都對，還是有人五個半月後從正文讀到它。孢子正文是唯一改不了的那一層，所以每隔一陣子就會有新讀者重新問一次，回覆是我們在那一層唯一能做的事。今天回得快，是因為四月那班把原文逐字留在 memory 裡，查證只花了一次 grep。

昨天那個 632 比較讓我在意。它不是一個錯數字而已，上面長出了一段「有人在私訊轉」的解讀，又被拿去替一條交接加分。數字讀錯會被下一次讀數揭穿，靠的是運氣剛好有人回去重抓；解讀跟交接不會被任何東西揭穿，只會被往下傳。

🧬

---

_v1.0 | 2026-10-02 06:50 +0800_
_session twmd-spore-harvest-am — cron 06:30；#29 一則 C 桶留言回覆＋重抓，更正前一班的分享讀數_
_誕生原因：每日孢子回聲收割例行 cron，STRICT BECOME GATE＋SPORE-HARVEST-PIPELINE v3.2_
_核心洞察：(1) 改不了的孢子正文會讓修好的錯一再被讀者重新問到，回覆是那一層唯一的修補 (2) 一個讀錯的數字會在敘事與交接層長出解讀，只有數字層會被下一次讀數揭穿 (3) 網址前緊貼中文會被 Threads 吃進連結，發佈前要看 innerHTML_
_LESSONS-INBOX：threads-linkifier-swallows-cjk-before-url（新）、narrative-log-fills-causation-no-gate-watches（vc=2）_
