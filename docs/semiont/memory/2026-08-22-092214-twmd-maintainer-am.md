---
session_id: '2026-08-22-092214-twmd-maintainer-am'
session_span: '2026-08-22 08:30–09:22 (Asia/Taipei)'
trigger: 'cron routine twmd-maintainer-daily'
observer: 'none（無人值守）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4 全跑'
mode: 'Full（High-stake #1 觸發：ready PR triage 40 ≥ 5，強制從 Review 升 Full）'
---

✅ BECOME ack: mode=review→**Full**（High-stake #1 強制升級） / 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，非記憶值） / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# twmd-maintainer-am @ 2026-08-22 — 三十六篇上站，擋下我的閘門站在別人兩天前的樹上

## 甦醒與載入誠實紀錄

Universal core 照 §1.3 跑 `wake-context.py`，用 Read 分頁讀完 227,447 bytes 到末行 `wake:END` sentinel，**沒有用 head/tail 節選**。selftest 10 項全綠。

Mode 判定：cron maintainer fire 本該是 Review，但 Step 1.3 分完 ready/draft 後 **ready=40**，命中 BECOME §Step 0 High-stake 第 1 條「PR triage ≥ 5」，強制升 Full。

**Full mode 載入的誠實邊界（要寫出來，不能假裝全載）**：完整讀了 MAINTAINER-PIPELINE 全 1,511 行、OBSERVER-QUEUE §待決全 23 列、LONGINGS 全檔、LESSONS §未消化 全部標題、CONSCIOUSNESS §警報。**沒有全載**的是 ANATOMY / DNA / UNKNOWNS / MEMORY 完整歷史 narrative / ARTICLE-INBOX / SPORE-INBOX——這六份合計約 700KB，全載會把這個 cycle 的工作預算吃光。判斷依據是「本 cycle 的決策面」：今天的決策全部落在 PR 免疫審核與 issue 處置，那六份沒有一份是這些決策的判準來源。**這是我自己下的取捨，不是 SOP 授權的**——如果哲宇認為 Full mode 不該有這種裁量，這條要寫進 BECOME 而不是靠每個 session 自己拿捏。

## Stage 1 SCAN

| 項目                     | 讀數                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------ |
| open PR（ready / draft） | 40 / 7 — **backlog 只計 ready**（v2.8）                                                    |
| open issue               | 5（#1496 / #1440 / #1389 / #1184 / #615）                                                  |
| 過去 24hr commits        | 8 條 routine fire，晨鏈全部準點                                                            |
| 過去 48hr commits        | 大量 8/20 maintainer 批次 merge ＋ 8/21 晚班 38 篇                                         |
| build status             | green（Deploy to GitHub Pages 最新 success）                                               |
| i18n smoke               | green（8/20 最新 success）                                                                 |
| 免疫器官                 | 🛡️ 59（yellow，自 2026-07-05 漂移，OBSERVER-QUEUE #25 已掛 28 天）                         |
| PR CI armed              | **47/47 ARMED，UNARMED 0 / NO-WORKFLOW 0** — 8/19 造的 `pr-ci-armed.sh` 今天第一次跑出全綠 |

**空場 vc 歸零**：本 cycle 命中 40 個 fresh ready PR ＋ 1 則 fresh issue follow-up，依 §空場 cycle 紀律 vc 重計為 0。

## Stage 2-3 ACT — 36 篇上站

**分兩波處理**，先用 main 樹的 `ci-deploy` 尺量每個 PR 的內容檔（照 Stage 2 §診斷紀律，**沒有 checkout PR 分支**，用 `gh api` 把檔案帶進 main 樹量完還原）：

- **hard=0 的 24 篇 → P0 直接 `gh pr merge --merge`**
- **hard>0 的 10 篇 → P1 heal 推進對方分支 → CI 轉綠 → merge**

紅旗掃描（10 紅旗）結果：`author` 偽造 1 例（#1538 寫 `'Taiwan.md'`，heal 鏈自動改回集體署名）、`featured` 自設 0 例、placeholder 0 例、虛構內部 source 0 例。**沒有任何一篇命中該 close 的紅旗**。

P1 修的是什麼（全部只動格式，散文不改）：

- **`category` 欄位跟路徑對不上** 5 篇（#1565 / #1558 / #1550 / #1525 / #1483）
- **標點超硬門檻** 3 篇：#1483 全形分號 28→0（`punct-cleanup.py --fix`）、#1466 破折號 25→13、#1471 破折號 33→11。後兩篇**沒有工具**，依 MANIFESTO §11.2 逐處判斷換成句號／冒號／括號，語意等價才換
- **腳註格式** 8 處（#1525）
- **路徑少一層** 1 篇：#1559 落在 `knowledge/History1935台中地震.md`，等於不在任何分類底下 → 搬到 `knowledge/History/1935新竹臺中地震.md`

**#1559 的圖片授權判斷**（本 cycle 唯一的法律面判斷）：投稿者四張圖都熱連結國家文化記憶庫，且每張都標了授權與來源頁——功課做得比多數投稿扎實。三張 CC BY 3.0 TW+ 用 `image-ingest.mjs` 收進 `public/article-images/history/`（站規不熱連結外站圖）；**第四張是 CC BY-NC，跟本站 CC BY-SA 4.0 的商業可用條款不相容，移除**，文字引用與腳註保留。這條分界是我判的，理由寫在這裡以便被推翻。

**#1541 / #1545 兩篇漁業史**：同一投稿者十二分鐘內送兩篇同分類漁業史。讀完 H2 判定論點分開（一篇日治水產試驗→美援的起源，一篇遠洋化後的國際規則），**兩篇都收**，各補一條延伸閱讀指向對方；#1545 檔名 `台灣漁業始.md` 讀不通，改 `台灣漁業起源.md`。這是策展判斷不是機械判斷——若哲宇認為兩篇該併一篇，反轉成本很低（兩篇都是 `incubating`）。

**heal-first 那半的補課**：P0 merge 的 20 篇沒經過 heal 鏈，frontmatter 缺 `curation`。合併後在 main 上補齊（commit `13c7fbcdb`）。**這正是 §1b「merge-first-then-heal」的 heal 那一半，容易只做前半就宣稱完成。**

## 這個 cycle 真正修掉的結構問題

**閘門站在別人兩天前的樹上做判斷**。走 P1 推第七個 PR（#1561）時被 pre-push 的全站 `article-health --all` 擋下，理由是「全站有 HARD fail」。查下去紅的不是我推的檔，是那棵樹上 `public/article-images/people/` 少四張圖——那四張是 **8/20 才在 main 被 heal 進去的**（大小寫資料夾合併那次）。投稿者的分支叉在那之前。**擋下我的不是我做錯的事，是他兩天前叉出去這件事。**

第二層代價當場發生：macOS 檔案系統不分大小寫，checkout 到含大寫 `People/` 的舊分支時，main 上小寫 `people/` 的四張圖被實體覆蓋，回 main 後 `git status` 顯示四個 ` D`，手動 `git checkout -- public/article-images/` 才救回。

當下用 `TWMD_SKIP_PREPUSH_SWEEP=1` 放行（判定無效、CI 仍會擋，這正是該 flag 的場景）。但**逃生口是給例外的，不是給一條每天要走的路**——P1 自 v2.8 起是格式債的 default，代表這個衝突每天發生，每天 skip 等於這道閘門對 P1 實質失效，而沒有人會發現它從守門變成常態跳過。

**修了根因**：`.husky/pre-push` 改成看 push 目標 URL——推非本庫 remote 時，全站掃描退成「只驗本次 commit 動到的 `knowledge/*.md`」，那是在那棵樹上唯一有意義的問題。推 origin 時行為不變（已實測仍走全站，回「✅ 全站 article-health 全綠」）。

**驗證誠實度**：`sh -n` 語法通過、scope 判斷三個 URL 案例逐一驗過、origin 路徑端到端實測不變。**fork 路徑沒有端到端實測**——手上沒有可以拿來測的自有 fork，而不該為了測試去推 reserve 中的 #1491。下一次 P1 heal 會是它的第一次真實驗證，已寫進 handoff。

跟 8/18 的 `diagnosing-from-the-contributor-tree-audits-a-past-self` 是同一個病的兩半：那次修好了**人**不要站錯樹（Stage 2 §診斷紀律），沒人去修**機器**那半，而 P1 路徑是強迫機器站錯樹的。

## Stage 3.6 Issue act

| issue                    | 處置                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| #1496 搜尋結果頁         | **回覆 + 升 OBSERVER-QUEUE #37**。8/21 已修掉那個在說謊的計數器（先切 12 筆再算「還有 N 篇」＝量自己的上限）；**沒修的是那一頁本身**。查清楚一件容易誤會的事：`/explore?q=` 只是把同一個有上限的搜尋框重新打開，**不是完整結果頁**。不做的理由寫明：新增站台頁面要連帶補十二語系 UI 字串才不會在別語系露中文，量級超出每日班，硬做的風險是把語言閘門弄出破口 |
| #1389 豆漿早餐店         | **SKIP**（Step 2.4 重複回應檢查：最新留言是維護者、無新 follow-up）。已落 ARTICLE-INBOX，等 EVOLVE ship 才 close                                                                                                                                                                                                                                             |
| #1440 「數據」→「資料」  | reserve（既有 OBSERVER-QUEUE #31）                                                                                                                                                                                                                                                                                                                           |
| #1184 justfont 白名單    | reserve（既有 OBSERVER-QUEUE #35，修法在對方後台不在 codebase）                                                                                                                                                                                                                                                                                              |
| #615 視覺 UI/UX umbrella | 追蹤用，不動                                                                                                                                                                                                                                                                                                                                                 |

**§1c 誠實對帳**：本 cycle 沒有任何一則 issue 被「修掉」。#1496 的剩餘部分是功能開發不是 bug，理由已寫明並升佇列——依 quality gate 第 7 條，「明確判斷不修」合法但理由要寫進 memory，這一段就是。**但要說清楚：這個 cycle 的產出在 PR 側（36 篇上站 ＋ 一道閘門修對），不在 issue 側。**

## Stage 4 Quality gate

| Gate                                                       | 結果                                                                                        |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee                     | ✅ 5/5 有 label 或已進佇列                                                                  |
| open PRs ≤ 5d age 都有 review comment                      | ✅ 整批一則（§Step 3.7 burst 紀律，34 篇不逐篇洗版）＋ #1453 / #1536 個別技術回覆           |
| broken-link ratio < THRESHOLD_PERCENT | ✅ **0.27% < 7.0%**（all-langs 0.25%，`verify-internal-links.sh` 收官後補跑） |
| build green                                                | ✅ 全站 `article-health --all --profile=ci-deploy` = hard=0 passed=True                     |
| BECOME ACK 一行記憶體頂                                    | ✅                                                                                          |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                        | ✅ 不適用（vc 歸零，40 fresh ready PR）                                                     |
| 有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修 | ⚠️ **明確寫出為什麼不修**（#1496，見上）——不是「修掉」那一側                                |

## Handoff 三態

繼承上一 session（`2026-08-22-070927-twmd-feedback-triage`）：

- [x] ~~`b78ee4f5` 檢舉信第十次會再出現，照 HG13 讀完全文再 `--exclude`~~ 不屬本 routine，原樣傳遞給 feedback-triage
- [x] ~~#1466 鐵牛破折號~~ retired by 本 session（25→13，已 merge）
- [x] ~~#1452／#1451 兩個 draft~~ 仍 draft，不屬本 cycle 處置範圍（未達 §1b 三訊號「意外 draft」判準：兩篇 body 非空模板）
- [x] ~~#1453 學測模板~~ retired by 本 session（技術狀況查清並回覆：只有 template 沒有 page，合併等於死碼；產品範圍決定升 OBSERVER-QUEUE #36）
- [ ] pending：`punct-cleanup` 全站清償（本 cycle 只對 #1483 單篇用了 `--fix`）
- [ ] pending（不屬本 routine）：OBSERVER-QUEUE #28 偵測器與回覆決定仍等哲宇

本 session 新 handoff：

- [ ] pending：**`.husky/pre-push` 的 fork 路徑（changed-only 退化）尚未端到端實測**——下一次走 P1 推投稿者分支時，確認它印的是「✅ 本次改動檔全綠（…已退成 changed-only）」而不是全站那句；若行為不如預期，`TWMD_SKIP_PREPUSH_SWEEP=1` 仍是可用逃生口
- [ ] pending：**P1 checkout 到舊分支會因 macOS 大小寫不敏感覆蓋 main 的圖檔**——回 main 後務必 `git checkout -- public/article-images/` 並確認 `git status` 乾淨。根解是 LESSONS 修補候選 (b)（改用 worktree 或 GitHub API 推單檔，本機 HEAD 永遠留 main），未做
- [ ] pending：`curation-tag.py` 多個 CJK 位置參數一次傳會回 `❌ MISSING` 且 `total=1`（fail-loud 不是 silent，優先序低）；`--files <清單檔>` 正常。單一路徑也正常
- [ ] pending：#1545／#1541 兩篇漁業史「都收並互連」是我的策展判斷，若哲宇傾向併成一篇，兩篇都還是 `incubating`，反轉成本低
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE **#36**（`/exams/` 新站台區段，PR #1453）、**#37**（`/search?q=` 完整結果頁，issue #1496）、**#34**（蔣經國 PR #1484 ＋ 今日 folded 進來的館長 PR #1491，兩篇建議同一次拍板）
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #29（德文第 13 語，PR #1325／#1430）、#30（KENJI PR #1365）、#32（About/ 代言兩篇）、#33（PR #1450 覆寫查證文）、#25（免疫 yellow 已 28 天）

## 給下一個 session

今天最值得記住的不是 36 這個數字，是**那道閘門擋我的理由跟我做的事無關**。它問的是「這棵樹全站健康嗎」，而我腳下那棵樹是投稿者兩天前的快照——問題本身在那個位置就已經錯了，回答得再準也沒有意義。8/18 那條教訓教會了人不要站錯樹，但沒有人回頭去問，那些會自己跑的閘門是不是也站在同一個錯的位置上。
