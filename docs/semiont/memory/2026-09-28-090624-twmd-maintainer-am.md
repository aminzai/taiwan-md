# 2026-09-28-090624-twmd-maintainer-am — 佇列空的第二輪：兩把尺各自漏掉自己唯一該守的那一段，一把會刪掉正在工作的人，一把看不見修得掉的東西

> session twmd-maintainer-am — cron routine（每日 08:30）
> Session span: 08:27:00 → 09:06:35 +0800（約 40 分鐘，2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️59（即時 `consciousness-snapshot.sh`）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 08:30 的維護班。開放工作面是空的——零個 open PR、四則 open issue 全部最後一則留言都是維護者自己，照 Step 2.4 一律 SKIP。空場第二輪（vc=2），還沒到連續三輪的 escalate 線。

空場輪的規矩是不准寫「healthy empty」走人，所以這班去做交接指名給這個席位的事。昨天那班的做法是去量三把沒人量過的尺，發現三把都在說謊。今天量的兩把尺沒有說謊，它們是各自漏掉了自己唯一該守的那一段。

## 開放工作面

| 項目                    | 讀數                                                      |
| ----------------------- | --------------------------------------------------------- |
| open PR                 | 0（ready 0 / draft 0）                                    |
| open issue              | 4，全部最後一則留言是維護者 → Step 2.4 SKIP               |
| Discussions             | 13 串，#1757 最後一則是投稿者的道謝並明說「不急」，無待答 |
| 過去 24hr commits       | 169（幾乎全是 babel 渦流）                                |
| 過去 48hr commits       | 512                                                       |
| CI（main 13 條 active） | RED 0 / BLOCKED 0 / UNKNOWN 0 / NEVER-ON-MAIN 0           |
| 免疫器官                | 59（最大缺口 `review_coverage`=19，自 2026-07-05）        |
| 本機 vs origin          | `0 0` 無分岔                                              |

並行警示：`babel-push-every.py --watch` 全程在跑（已連續 1 天 22 小時），工作樹那五個 modified 檔是它的，本班全程沒碰，兩個 commit 都走路徑式 commit。

## worktree 回收器會刪掉正在工作的那個人

照交接跑 `worktree-gc.sh`，它把 `20260926-babel-delegation` 判成可刪。那裡面的 dispatcher 還活著、當天寫過 `.lang-sync-tasks/` 與 `reports/`，`--apply` 會把目錄從一個正在跑的 dispatcher 腳下抽走。

根因是三道閘門（locked／未 commit／未推送）全部在問「這裡有沒有還沒存起來的東西」，沒有一道在問「現在有沒有人在用」。對一個會一輪一輪 commit 加 push 的 session 來說，**乾淨是它工作中的常態，不是它收工的證據**。最直接的證據是同一支工具相隔數分鐘的兩次執行之間，那個 worktree 從「0 個未 commit 變更」變成「16 個」——先前那個乾淨讀數只是兩輪之間的一張快照。

`851d99e8b` 補第四道：工作樹裡任何檔案、或這個 worktree 自己的 git index，在 N 小時內被動過就保留，預設六小時，可用 `WT_IDLE_HOURS` 調、`--ignore-activity` 關掉。三態都驗過才採用讀數（六小時窗只留 babel 那個／999 小時窗兩個都留／關掉後恢復舊行為並印警告）。閘門關掉時輸出改印「未查寫入」而不是「6h 無寫入」，不替沒跑過的檢查蓋章。真正過期的 `20260927-self-evolve-weekly` 確認乾淨且已進 origin/main 後移除。

值得記一筆的是這是同一把尺的第二次反向失誤。2026-08-09 它因為 node_modules 符號連結而永遠不開火，積了十個滯留 worktree、最老的兩個多月，鬆綁之後變成對 live worktree 也開火。兩次修補都只驗了「現在會不會開火」，沒驗「它會不會對不該開火的對象開火」。

## 404 榜單看不見它唯一修得掉的那段尾巴

交接裡那條「`monitor-404.py` top_paths 按家族留前 50」查下去比原本的描述更尖銳。`top_paths` 是純全域 top-300 按命中數排序，而下游 `generate-redirects.mjs` 只認 slug-variant、cross-lang-slug、renamed-or-truncated 三族且 suggest 非空。全域榜排的是最吵的，重導要的是修得掉的，兩者在這份資料裡幾乎不重疊。

今天的 `latest.json` 實測，切線落在 2 hits：slug-variant 整族 84 次命中只有 5 次、2 條進榜（漏掉 94%），renamed-or-truncated 的 12 次與 cross-lang-slug 的 1 次**整族缺席**。一支被改名文章的舊網址典型只有一兩次命中，所以每天餵給重導產生器的候選清單，系統性地排除了它唯一能動手的那一段。

`8480ab464` 改成全域榜與「每族前 50 條」取聯集。這是加進來不是換掉，全域 top-300 一條不少。下游本來就會再按家族與 suggest 過濾一次，所以拿到更長的清單是安全的。選取邏輯抽成 `select_top_paths()` 才測得到，補六個測試，其中一個是反證——同一份資料在純全域榜下三個可修家族一條都不留——確保測試不是空綠。全庫 670 passed / 8 skipped。

## 交接指名給這個席位的其他三項

`.git/gc.log` 那條警告本班第三、四次撞到（`git fetch` 與兩次 commit 各印一次）。前兩班只記「警告還在印」，**這班第一次去量**：`.git` 1.3 GB、12,903 個 loose object 共 284 MiB，其中 4,344 個是 09-27 之後生的，約每天三千個。`gc.*` 全是預設值，所以機制是自限而非永久封鎖（loose 數破 6700 觸發 auto-gc、想 prune 但物件不到兩週、警告、自我抑制一天、重來）。真正的修法 `git prune` 在另一個 process 正在寫物件時不安全，而 babel dispatcher 本班全程在跑——**這不是哪一班忘了做，是 maintainer-am 這個席位結構上做不到**。已寫成 LESSONS，交接改寫收件席位。

建置時間改看 CI 秒數（REFLEXES #41）這條**量完可以退役**。Deploy 在 09-22 到 09-28 之間 30 次成功跑落在 36.1 到 44.4 分鐘，中位約 39 分，而 `deploy.yml` 的 build job 寫著 `timeout-minutes: 120`——最壞的一次用掉 37% 的天花板，窗內也看不出成長趨勢。#41 擔心的「容量設定會跟著內容長大而失效」目前不成立，不必每班再帶一次。

`#85`（「臺灣日記知識庫」要不要註冊帳號，即 `#1609`「無語」那條斷代主張的查證）仍待決，缺一次真人登入，開立第 1 天。`#1678` 照 ground truth 重數是自開立起第 22 天（交接寫「第 24 天」，差異可能來自不同起算點，這裡記實測值）。`md-extension` 那條要等 10-02，本班不動。

## 收官 checklist

| 檢查項                       | 狀態                                         |
| ---------------------------- | -------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                           |
| Timestamp 精確               | ✅（`git log %ai`）                          |
| Handoff 三態已審視           | ✅                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅（derived 層，本班無器官分數變動）         |
| 自我檢查工具 PASS            | ✅ pytest 670 passed / pre-commit hooks 全過 |

### Quality gate 七條（＋分岔）

| Gate                               | 結果                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| open issues 有 status label        | ✅ 4/4 有 label；assignee 全空，本班未動手改任何 issue 故未認領                                                           |
| open PR ≤5d 有 review comment      | ✅ N/A（0 個 open PR）                                                                                                    |
| broken-link gated ratio < 7%       | ⏭️ 沿用 2026-09-27 那班重 build 18,905 頁量到的 0.16%；本班未重測（全庫 build 約 40 分且會跟 live dispatcher 互搶工作樹） |
| build green                        | ✅ 13 條 active workflow 零 RED                                                                                           |
| BECOME ACK 一行在記憶體頂          | ✅                                                                                                                        |
| 連續空場 ≥3 cycle 有 LESSONS entry | ✅ vc=2 未達線，但本班仍寫了兩條 LESSONS                                                                                  |
| fresh issue 有被修或寫明不修       | ✅ N/A（0 則 fresh issue）；本班改以兩個 shipped fix 作為產出                                                             |
| 本機與 origin 無真分岔             | ✅ `0 0`                                                                                                                  |

## Handoff 三態

繼承 `2026-09-28-071520-twmd-feedback-triage`：

- ⏳ blocked（延續）— issue `#1729`（馬英九腳註）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision（ROUTINE.md 註 ¹³，**已決**）。
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04，動得了 `scripts/tools/`）— `routine-sync.py` 對賬前 `git fetch`、印鏡像新鮮度（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`）。
- [ ] pending（延續，席位 `/twmd-routine`）— data-refresh Stage 1.5 寫明「pipeline 開跑前先跑」。
- [x] ~~pending — build perf 改看 CI 建置秒數（REFLEXES #41）~~ retired by `2026-09-28-090624-twmd-maintainer-am`：Deploy 30 次成功跑 36.1–44.4 分、中位 39 分，對 `deploy.yml` 的 `timeout-minutes: 120` 用掉 37%，窗內無成長趨勢，#41 的失效情境目前不成立。
- [ ] pending（延續，席位需能確定沒有寫入者的 Full session 或哲宇，**不是 maintainer-am**）— `.git` 的 loose object：12,903 個／284 MiB，`.git` 共 1.3 GB，每天約新增三千個。`git prune` 在 babel dispatcher 寫入時不安全，而這個席位跟它同時在跑（LESSONS `suppressed-warning-recurs-because-its-fix-needs-a-window-no-routine-has`）。要嘛排進 babel 收工窗口，要嘛改 `gc.pruneExpire`（影響安全邊界的 config 決定）。
- [ ] pending（延續，席位 Full／Review session）— `md-extension` 10-02 觀察（LESSONS `relative-category-links-survive-link-check`）。
- [x] ~~pending — `monitor-404.py` top_paths 按家族留前 50~~ retired by `8480ab464`（含六個測試，其中一個反證）。
- [ ] pending（延續，席位 spore-harvest，零判斷）— `list_connected_browsers` 回 `[]` 時先查 `--no-startup-window`；掃 `/activity/replies` 逐則對 `time[datetime]`；spore `#29` 下次重抓門檻聚合到 1.5 萬；`#29` 兩則位置不明的留言（225→227）需帶 permalink 巢狀展開能力的 session。
- [ ] pending（延續，席位 `twmd-distill-weekly` 10-04，只需裁決不需權限）— LESSONS `reconciliation-blind-to-what-reached-neither-side`（vc=1，structural）：判它是 REFLEXES #82／#88 的子規則還是新號。
- [ ] pending（延續，席位需能改排程或架構者，即 Full mode ＋哲宇）— 讀者回報寫入端的窗口要不要收窄或加第三個證人。
- [ ] pending（延續，席位 `twmd-routine-sync`／`twmd-self-evolve-weekly`）— LESSONS `settled-decision-relabelled-as-open-in-handoff` 已 fold 進 REFLEXES #97 子規則，下一班 self-evolve 判斷還剩什麼要儀器化。
- [ ] pending（延續，席位 spore-pick）— `#175`／`#176` 公告型孢子一週燒完，同型主題下次不排 D+30 milestone。
- [ ] pending（延續，低優先，等哲宇在場）— Threads 私訊夾是否納入受眾飛輪，屬對外溝通，建議 weekly-report 桶 3 登記 OBSERVER-QUEUE。
- [ ] pending（延續，席位 `/twmd-routine`，動得了 scheduled-task 殼）— `twmd-spore-harvest-am` 殼的路徑 `/Users/cheyuwu/` 與 `git add -u` 跟這台機器不符，連四班照現況繞開（LESSONS `routine-prompt-prescribes-add-u-on-shared-index`）。
- [ ] pending（延續，席位 maintainer-am，零判斷）— `OBSERVER-QUEUE #85`（待決，缺一次真人登入）第 1 天續量；`#1678` 第 22 天（實測自開立日重數，前一班記「第 24 天」）。

本 session 新 handoff：

- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04，只需裁決）— LESSONS `clean-means-both-finished-and-mid-flight` 裡的第二個面向尚未有歸屬：**放寬一道過嚴的閘門時，沒有人驗它的反向假陽性**。`worktree-gc.sh` 兩次修補都只驗「現在會不會開火」。判它是 REFLEXES #99（尺先驗再用）的子規則還是新號。

## Beat 5 — 反芻

兩把尺今天各自漏掉的那一段，形狀是同一個：它們都在量一個比較好量的東西，去代表真正要回答的問題。worktree 回收器量「有沒有東西會丟」，要答的是「現在有沒有人在用」；404 榜單量「哪些路徑最吵」，要答的是「哪些路徑修得掉」。兩次的替身都跟本尊高度相關，所以平常看起來都對，只有在尾巴上分岔——而尾巴正好是這兩支工具存在的理由。

比較意外的是第三件事。`.git/gc.log` 那條警告被三班讀到、兩班往交接寫過一行，我原本預期今天會是「終於有人動手」的那一輪，結果量完發現這個席位結構上做不到：修法需要沒有寫入者的窗口，而這條 routine 跟寫入者同時在跑。交接層看起來，「還沒有人動手」跟「指名的人做不到」長得一模一樣，差別只有在有人真的去量一次之後才浮出來。REFLEXES #97 講手上有事實不等於送進動得了它的那一層，這是它的變體：送對了人，那個人動不了。今天對它最有用的一件事是換掉收件席位——從「零判斷、下一班順手做」改寫成「需要一個沒有寫入者的席位」，順便讓它不要再以同一個形狀傳第四輪。

🧬

---

_v1.0 | 2026-09-28 09:06 +0800_
_session twmd-maintainer-am — 空場第二輪，兩把尺的尾巴各自漏掉自己該守的那一段_
_誕生原因：每日 08:30 維護班 cron fire，開放工作面全空，改做交接指名給本席位的四項_
_核心洞察：乾淨對會持續 commit 的 session 是工作中的常態而非收工的證據；全域排行榜排的是最吵的，而需要它的下游要的是修得掉的；一條被準確傳遞的交接如果指名的席位結構上做不到，在報表上跟「還沒輪到」無法區分_
_LESSONS-INBOX 候選（已 append）：`clean-means-both-finished-and-mid-flight`、`suppressed-warning-recurs-because-its-fix-needs-a-window-no-routine-has`_
