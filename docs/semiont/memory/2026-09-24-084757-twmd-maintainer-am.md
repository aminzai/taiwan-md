# 2026-09-24-084757-twmd-maintainer-am — 三篇投稿譯文收下；倒數中的警報在清單上愈來愈小聲；讀者等了 28 天的查證，路一直有一條短的

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:30 fire → 08:34 BECOME 完成 → 08:36 三個 merge → 08:38 致謝 → 08:39 看門狗修補 → 08:41 #1609 查證突破 → 收官 +0800（3 merge + 3 heal/fix + 2 LESSONS + 1 memory）
> 資料來源：`git log %ai` + `gh pr view --json mergeCommit` + `gh api actions/runs` + `~/.taiwanmd/auth-*`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05，最大缺口 review_coverage=19，少 20.25 分）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 量 `main...origin/main` 得 `2 0`，本機純領先兩個 babel commit，**沒有分岔**。3 個 ready PR（aminzai 連續第七天三篇，0 draft，未達 High-stake ≥5，Review mode 成立）、5 個 open issue（今天 0 新）、Discussions 最新 #1757 已於 09-20 由維護者逐條回過、`pr-ci-armed` 三個 PR 都 ARMED 三條 check 全過、main 四條 workflow 最新一次全綠。babel dispatcher 五個 writer 正在主工作樹寫（ACTOR_BUSY），全程沒動 destructive git（DNA #35）。

**閘門跑在隔離工作樹**：因為 dispatcher 正在寫主工作樹的 index，把 PR 檔案複製進主樹再跑檢查，有被它的下一個 `git add` 掃走的風險（LESSONS `staged-files-leak-into-a-parallel-writers-commit`）。改用 `git worktree add --detach` 開一棵臨時樹，在裡面放 PR 檔案跑全部閘門——既滿足 Stage 2「用 main 的檢查器量」的診斷紀律（工具是 main 的版本），又不碰 dispatcher 的 index。收官時 `worktree remove`。

## 三篇投稿譯文（#1768 de 心戰／#1769 hi 阿里山林業鐵路／#1770 ar 台灣造船業）

三篇都是單檔新增、0 刪除、CLEAN、無紅旗。先 `--add-assignee @me` 認領（Step 3.0），再在隔離樹跑：`article-health --profile=ci-deploy` 三篇 **hard=0 warn=0**，`target-language-check` 0 fail，`translation-ratio-check` 三篇 OK 且結構逐項對得上母稿（心戰 5 段 11 腳註 21 連結／阿里山 8 段 11 腳註 20 連結／造船業 7 段 14 腳註 22 連結，全部一比一，沒有摘要式壓縮），`sourceCommitSha` 三篇都對到母稿現在的 HEAD。frontmatter `author` 是 `'Taiwan.md Contributors'`、`featured: false`，不是紅旗 #7／#6。

**Step 3.4 footnote audit 換了一把更合身的尺**：pipeline 寫「抽樣 ≥3 個 footnote URL WebFetch」，那是為「投稿者自己寫的新文章」設計的。譯文的腳註是從母稿繼承的，母稿那批來源早已驗過，逐一重打一次網路只是重驗別人已驗的東西。改成比對**譯文與母稿的網址集合**：三篇各 10／15／18 條，`comm` 雙向差集**全空**——沒有新增、沒有丟失、沒有改寫。翻譯層最該防的是「模型替一句話補一個看起來合理的來源」，集合比對正面回答了這件事，而且比抽樣強（抽樣只看 3 條，集合看全部）。

三篇 `gh pr merge --merge` 落地（`ecc043055`／`1dff9cc20`／`db37a1d20`），三個 PR 狀態都是 MERGED。致謝照 burst 規則整批一則留在 #1768，另兩篇留指標。

收官前 `sync-translations-json.py` 補登記表三行（`001098168`，scope 驗過 1 檔）。origin 併回本機用 merge 不用 rebase（dispatcher 在寫，不改寫歷史，DNA #35），`079147430`，檔案交集 0。

## 倒數中的警報，在唯一會被掃到的畫面上愈來愈小聲

issue #1761 是 `auth-watchdog.sh` 自己開的票：mouhouse 的 Claude Desktop 登入 30 天到期，過期會讓排程照 fire、`lastRunAt` 照更新，而每個 routine session 被「Sign in again」擋回——2026-08-23 那次就是這樣四天零產出。

量 ground truth（不看留言）：`~/.taiwanmd/auth-login-date` = 2026-08-28，`auth-watchdog.state` 已是 `critical`，**預估 2026-09-27 過期，距今 3 天**。而觀察者最後在場是 09-19，**已缺席 5 天**。

看門狗每 12 小時補一則留言，倒數逐則遞減（5 天 → 4 天 → 4 天 → 3 天），四則內容其餘一字不差。**但標題還停在開票那天的「約 5 天後過期」**，而且會一路錯到過期當天。

根因在 `$TITLE` 的生命週期：它只有 `gh issue create` 那一次用得到，既有 issue 存在時走的是 `gh issue comment`，標題從此不動。後果是最該被一眼看見的那張票，在**唯一會被一眼掃到的畫面**（`gh issue list`／GitHub issue 清單）上，隨著愈接近臨界而愈安靜——大聲程度跟急迫度反向移動。

修了兩處（`320bfacc9`）：既有 issue 也跑 `gh issue edit --title`；標題改寫**絕對過期日期**而不是相對天數——凍住的相對天數是錯的，凍住的絕對日期還是對的。新標題由腳本自己算出來（`--dry-run` 擷取，不手抄，per REFLEXES #93），驗出「預估 2026-09-27 過期，剩約 3 天」跟日曆對得上，同步改到 live issue。

**另外兩條宣告過的管道，今天實測都不通**：

- Remote Control 未連線 → 推播送不出去（試了，回 not sent）
- `~/.config/taiwan-md/credentials/telegram.env` 不存在 → 看門狗裡那段 Telegram **從來沒有執行過**（REFLEXES #52 (f) 宣稱的豁免從未被觀察到生效過，同一形狀）

三條管道各自以不同方式退化，**沒有任何東西在量管道本身的健康**。issue 留言把這三件事講清楚了（含 commit hash）。登入本身只有哲宇能做，維護班不碰憑證。

## 讀者等了 28 天的那條，路一直有一條短的

issue #1609（讀者蘇洛，08-27 開，今天**第 28 天**）：主張「無語」在台灣本有用法，證據是白色恐怖受難者郭淑姿的日記，挑戰詞條 `無語.yaml` 的 `fork_point: ~2010s`。

前三輪回覆都是真進展：08-28 立誠信標註、08-31 定位到國家人權博物館出版的兩冊＋黃文源投書引的是「無聊／不聊」、09-14 縮到「第二冊為第一順位」並找到中研院臺史所檔案館〈葉盛吉文書〉的原件目錄，結論寫「數位影像須到館調閱，**線上無全文**」。

那句話對檔案館那條路是對的，但它漏了另一條。本輪一次搜尋就撞見：《郭淑姿日記》全文已收在中研院臺史所「**臺灣日記知識庫**」（`taco.ith.sinica.edu.tw/tdk/`），是該庫第 21 種，1944-1953 共 **904 則、約 34 萬字**，附手稿影像，而且提供**全文檢索**。搜尋摘要當線索不當結論（REFLEXES #16），實際 fetch 該庫的〈關於〉頁核對過這些數字，也 fetch 了條目頁確認存取條件。

查證成本從「跑一趟檔案館、翻兩冊實體書」降到「**檢索一個詞**」，而前三輪替它縮小的分冊優先序，在全文檢索面前全部失去意義。

**卡點只剩一個，而且是我過不去的那種**：全文需要登入帳號，而註冊帳號是人的動作，AI 不得代勞。所以這條今天的狀態是——缺的不再是線索、不再是範圍、也不再是力氣，**缺的是一次登入**。

落檔（`b159eeaa5`）：寫進 `無語.yaml` 的 `pending_verification.locations` 第一順位（帶 ⭐）與 `needs`，散文 notes 也補一段。`terminology-pending-verification.py` 讀得到，確認新路徑真的送進了會動手的那一層（per `held-fact-never-crosses` vc=5 —— 只寫 GitHub 留言就是那條教訓的形狀）。**判定一個字沒動**：`fork_point` 仍是 `~2010s`、仍標「被一份一手史料挑戰、尚未核對」。用語立場屬 §自主權邊界，維護班只補查證路徑（REFLEXES #79）。回覆讀者時把「你等了 28 天，而這件事本來第一週就該查完——不是因為難，是因為前三輪都在同一條比較貴的路上往前推」講出來。

## 五則 open issue 的判斷

今天 0 則新 issue。

- **#1609**（郭淑姿日記，第 28 天）— **本輪實質推進**，見上。仍 open，等一次登入。
- **#1678**（生態多樣性，第 19 天）— 09-06 已實質回覆並 ship 過連結修補；剩下是母稿骨架重寫，屬 REWRITE 不屬 maintainer heal。核過 `ARTICLE-INBOX` 第 445 行 entry 真在、`P1` `pending`、研究（陳貞志 25 倍數字、四個來源）預先寫好。**但本輪多問了一層**：它為什麼躺了 19 天？查 `ROUTINE.md` 排程表——`twmd-rewrite-daily` 標 ⏸️，哲宇 2026-07-25 directive「兩台都先 disable，我先手動控制」，狀態是 `manual-by-decision`、**無到期日、且明寫「不得由週期檢查自動加期限或重開」**。所以這不是飛輪故障，是已決的設計；但它的副作用是**所有出口在生成線上的讀者 issue，等待時間沒有上限，而且沒有任何一道在量**。不重開、不加期限（REFLEXES #80 sustain 紀律：已決條目後續 cycle 靜默是 continuity 不是 renew），只把這個因果寫進交接讓哲宇看得到。
- **#1729**（馬英九腳註，第 8 天）— 仍等 Write mode FACTCHECK Full。狀態未變。
- **#1761**（登入過期）— 見上，本輪修了告警管道，登入待哲宇。
- **#615** — umbrella，無動作。

四則最新留言都是維護者且無新 follow-up 的，Step 2.4 SKIP，不補罐頭回覆；#1609／#1761 是有新事實才回。

**天數的算法講清楚免得下一班再漂**：`twmd-feedback-triage` 07:10 那班數的是 **issue 建立日起算、含當日**（#1609=28、#1678=19）。本班沿用同一個基準，沒有改寫成「狀態未變」。讀者實際等待更久（#1609 的站上回報日是 08-23，到今天 32 天）。

## 收官 checklist

| 檢查項                                           | 狀態                                                                                         |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee         | ✅ 5 則都有 label；#1761 有 assignee，其餘為有據留開                                         |
| open PRs ≤ 5d age 都有 review comment            | ✅ 3 則全 merge 並留言（burst 規則整批一則）                                                 |
| broken-link gated ratio < 7%                     | ✅ 0.34%（all-langs 0.31%）                                                                  |
| build green                                      | ✅ main 四條 workflow 最新一次全 success                                                     |
| BECOME ACK 一行記憶體頂                          | ✅                                                                                           |
| 連續空場 ≥ 3 cycle 有 LESSONS entry              | ✅ 不適用——本輪 3 個 fresh PR，**空場 vc 歸零**                                              |
| 有 fresh issue 的 cycle 至少一件被修掉或寫明原因 | ✅ 今天 0 則 fresh issue；舊 issue 中 #1609 實質推進、#1761 修掉告警管道，其餘逐一寫明阻塞層 |
| 本機與 origin 無真分岔                           | ✅ Stage 1 `2 0` 純領先；收 PR 後自造 `2 6`，當班 merge 併掉（`079147430`），push 後 `0 0`   |

## Handoff 三態

繼承 `2026-09-24-071058-twmd-feedback-triage`：

- ⏳ blocked（延續）— issue [#1729](https://github.com/frank890417/taiwan-md/issues/1729) 馬英九腳註，等 Write session 帶哲宇 review 的 FACTCHECK Full mode。本班重驗：仍 open，最後更新 09-18（第 8 天）。
- [x] ~~pending（給 08:30 maintainer-am，資訊）— `from-feedback` 兩則 #1609 第 28 天、#1678 第 19 天無 assignee~~ — retired by 本班：兩則都不再是「只被計數」的狀態。#1609 本輪把查證路徑縮到剩一次登入並落檔進詞條；#1678 的等待成因追到 `twmd-rewrite-daily` 已決暫停（見下方新 handoff）。**天數基準沿用建立日含當日**，下一班續量不要換基準。
- [ ] pending（延續，1-file 候選，給 `twmd-distill-weekly`）— LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5，候選機械化「出口完整性檢查」仍未做。本班 #1609 落檔時手動做了一次這件事（驗 `terminology-pending-verification.py` 真的讀得到新路徑），算第 6 個 instance。
- [ ] pending（指定席位 09-27 `twmd-self-evolve-weekly`）— `routine-sync.py` 對賬前 `git fetch`，另外讓 `load_live()` 印鏡像 mtime。
- [ ] pending（延續）— build perf、`.git/gc.log`、`monitor-404.py` 觀察、pathspec 收官索引殘影。
- [ ] pending（延續，零判斷，給下一班 spore-harvest）— 掃 `/activity/replies` 逐則對 `time[datetime]`；#29 李洋按讚聚合要到「1.4 萬」才開。

本 session 新 handoff：

- 🚨 **給哲宇，3 天內**（給任何一班：看到就在報告第一行複述，不要讓它沉下去）— **mouhouse 登入預估 2026-09-27 過期**（登入日 08-28，看門狗 state 已 `critical`）。過期的後果有前例：13 條 routine 照 fire、`lastRunAt` 照更新、每個 session 被擋回，四天零產出。**只有哲宇能做**（在 mouhouse 上打開 Claude Desktop 重新登入）。本班已把標題修成會跟著倒數走、並改寫絕對日期（`320bfacc9`），但**另外兩條管道實測都不通**：Remote Control 未連線、`telegram.env` 不存在。等於現在只剩 GitHub 一條路在對一個缺席 5 天的人說話。
- [ ] pending（1-file 候選，給 `twmd-self-evolve-weekly` 或 distill）— 讓看門狗在 `critical` 時對三條管道各做一次可達性自檢，把結果寫進 issue 本文（推播送出了沒、`telegram.env` 在不在），讓「沒人回應」跟「根本沒送到」分得開。這是 REFLEXES #38 (g) 零維度在**告警管道層**的形狀：現在這兩件事在紀錄上同形。
- [ ] pending（給哲宇，資訊，不要求動作）— `twmd-rewrite-daily` 已決暫停（07-25 directive，manual-by-decision，無到期日）的一個副作用，本班第一次把因果接起來：**出口在生成線上的讀者 issue，等待時間沒有上限也沒有任何一道在量**。#1678 是現成的例子——研究做完、`ARTICLE-INBOX` P1 就位、`⏸️` 是對的決定，而讀者已經等 19 天，且沒有任何機制會讓這個數字變得刺眼。不重開、不加期限（#80 sustain），只把這件事放到哲宇看得到的地方；要不要為這類 issue 設一個「等待上限就開一次手動 rewrite」的約定，是他的決定。
- [ ] pending（給下一班 maintainer-am，方法沿用）— 譯文 PR 的 footnote audit 用「跟母稿比對網址集合」取代「抽樣 ≥3 條 WebFetch」，本班三篇全空差集。比抽樣強（看全部不看 3 條）且不重驗母稿已驗的來源。若連兩班同樣好用，值得進 `MAINTAINER-PIPELINE` §Step 3.4 當譯文 PR 的分支規則。

🧬
