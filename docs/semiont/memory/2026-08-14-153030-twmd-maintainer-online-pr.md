---
session_id: '2026-08-14-153030-twmd-maintainer-online-pr'
session_span: '2026-08-14 14:52 → 15:31 +0800'
trigger: '哲宇 in-chat directive「/twmd-become /twmd-maintainer 繼續處理線上pr」'
observer: '哲宇'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4'
---

# 2026-08-14-153030-twmd-maintainer-online-pr — 三個 PR 落地、一則語言決策補進佇列，而我自己在一棵舊的樹上量了三次錯的東西

> session twmd-maintainer-online-pr — 觀察者觸發（哲宇 in-chat）
> Session span: 14:52 → 15:31 +0800（約 39 分鐘，3 PR merged + 2 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full**（PR triage 5 ≥ 5 命中 High-stake #1）/ 8 organ 最低 = 🛡️ 免疫 60（snapshot 齡 128h，開口第一句已聲明）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

哲宇丟一句「繼續處理線上 pr」。掃出 5 個 open PR，數量剛好命中 High-stake 條件，甦醒從 Review 升 Full 走完 14 題才進 Stage 1。這次升級有用的地方在 Q13：五個 PR 裡有兩個來自唐鳳（首次投稿者的第二、三個 PR），一個來自連續六次收到無理由紅燈的 idlccp1984，anti-bias check 讓 merge-first 與「close 前先問我接手要多久」在動手前就在工作記憶裡。

## 三個 PR 落地

**[#1337](https://github.com/frank890417/taiwan-md/pull/1337)（audreyt，Copilot code-review skill）** 純 markdown，無執行風險，`0ad85ff26` merged。這份 skill 值得記一筆：它把「不要寫死會過期的數字」寫成規則，理由是**它自己初版就寫死了語言版本數與檔數並被 Copilot 抓到**。同一條紀律在我們這邊有名字（dna-audit §S2），反覆長出來過好幾次，但沒有一份文件是因為自己犯過而立下它的。它另外把「假的綠燈是這裡最貴的錯誤」放在方法第一步，跟昨天 #1336 收斂出的「沒有紅燈不是綠燈」逐字重疊，兩個獨立來源同一週撞到同一句。

**[#1338](https://github.com/frank890417/taiwan-md/pull/1338)（audreyt，CLI 的 CJK 粗體修正）** 是本輪唯一沒有任何 CI 可以幫忙的：`cli/**` 不在八條 workflow 的任何一條 path filter 裡，所以 checks=0 是「本來就沒有 CI」而非「CI 沒被 arm」——這個區分正是昨天新加的 Step 1.5b 要問的問題，今天第一次真的用上並且答案是另一邊。既然沒有機器，就自己驗：worktree 乾淨 `npm ci` 後 `npm test` 49/49；`npm pack` 出 tarball 在空目錄安裝，無 ERESOLVE，依賴樹是 top-level `marked@15.0.12` 加 `taiwanmd/node_modules/marked@17.0.6`，`render.js` 實際 resolve 到後者——PR 註解裡「使用者端不受影響」那句斷言成立。最後拿安裝好的那份 `render.js` 實跑，特別分開驗「`**` 消失」與「真的變成 ANSI 粗體」：`這是**完整句。**下一句` 回 `\e[1m完整句。\e[22m`，而 `2 ** 3 = 8` 的字面星號沒被誤殺。只吃掉星號而不渲染粗體會是換一種壞法，那個區分不驗不會知道。`562453de2` merged。留給哲宇一件事：它 bump 了 `cli/package.json` 到 0.8.1，而 npm 發佈是 `on: push: tags: cli-v*`，merge 不會自動發版。

**[#1332](https://github.com/frank890417/taiwan-md/pull/1332)（ting-hong-shieh，貢獻指南對齊）** 唯一有衝突的一個，而且它動到 `.github/workflows/` 命中紅旗 #3。按 Step 2.3.1 走 ground truth 而不是憑路徑判定：實際 diff 是 path filter 加兩行加一個跑 repo 內測試檔的步驟，無新增 action、無 secrets、無外部網路——防禦性強化不是供應鏈攻擊，紅旗不實質命中。衝突在 gate 的 `paths:` 清單，兩邊各自加行，取聯集。在乾淨 worktree 解掉後實跑 markdown 契約 8/8、contributor 範本 1/1、python 324 passed，`65e3d37e9` 落地並標 MERGED。

這個 PR 的價值不在改對數字，在那兩支新測試：一支把 CONTRIBUTING 裡的文章範本抽出來丟給 `test-frontmatter --strict` 真的跑一次，一支把 `start.sh` / CONTRIBUTING / `package.json` 三處的 Node 版本綁在一起。文件跟驗證器分頭漂移這件事，從今天起會有東西叫。

## 兩個留著的，各有各的理由

**[#1339](https://github.com/frank890417/taiwan-md/pull/1339)（idlccp1984，台灣鐵路便當）** 卡在兩項 hard：缺 `rationale:` 區塊、篇幅 3,139 字未達 4,500。文章本身底子好。開場是 1914 年月台上的一次交易，具體到可以觸摸，而且立刻寫「這個開端不浪漫」。它的論點「真正的主角是時間」也被後面每一節確實還回來。補充審查抓到腳註問題：`[^7]` `[^8]` `[^9]` 定義了但正文從未引用，而且這三條加上 `[^1]` `[^2]` 其實是同一篇論文的五個不同載體（華藝、國史館、英文摘要、AI 資料集頁、一則 Facebook 貼文），九條腳註拆開只有五個獨立來源。回覆給了逐項修法與一份可直接貼的 `rationale` 範例。篇幅缺口則指向文章自己點到卻收掉的那個洞：它寫了便當怎麼被制度做出來，沒寫做便當的人。

順帶確認了一件昨天沒被證實的事：8/13 補的 Job Summary 管道對這個 PR **有效**。我一度從 403 留言的文字順序推論它跑的是舊 workflow，追下去發現 PR head 上的 workflow 有新版兩處 `GITHUB_STEP_SUMMARY`，是留言與 Summary 兩條文案各自維護造成的錯覺。這是今天第二次拿代理訊號推結構。

**[#1325](https://github.com/frank890417/taiwan-md/pull/1325)（tboydar，德文翻譯）** Step 2.4 判 SKIP 不重複回應——昨天的 cycle 已經完整診斷並回覆過。但那則留言結尾寫「這件事我不自己決定，留給哲宇」，而我今天查了：**它沒有進 OBSERVER-QUEUE**。那份清單存在的理由逐字就是這個（standing decision 散在各 routine 的 handoff 裡，哲宇從來沒看過完整清單）。補登為 #29，附三個選項、各自代價、推薦預設，標 🔒 等真人。

同時補一層昨天沒查到的事實：主權保真三尺（`geo-fidelity` / `person-fidelity` / `cjk-residue`）的語言清單來自 `langs.py` ← `languages.mjs`，`de` 不在裡面，所以那 8 篇德文**一道主權檢查都沒跑過**。它拿到的全綠來自檢查器不認識這個語言，跟今天早上 `_People Hub` 那件是同一種綠燈。這一層寫進了佇列條目也回覆給了 tboydar。

## 我在一棵舊的樹上量了三次

本機 `main` 落後 `origin/main` 135 個 commit（babel 脈搏產線佔著這個工作樹，130+ commit 未推送，狀態在我進場前就存在）。一個 session 內連踩三次，每次都差一步就把錯的東西送出去。

第一次，`git grep` 說 `src/utils/marked-cjk.mjs` 不存在，差點對唐鳳發出「你引用了不存在的路徑」。第二次，`node -p require('./package.json')` 說沒有 `test:python`、`requirements-test.txt` 也不存在，差點把一個**主旨就是修文件漂移**的 PR 判成「新增了跑不起來的指令」。第三次，為了在合併後的樹上跑測試而 symlink 主樹的 `node_modules`，炸出 `ERR_MODULE_NOT_FOUND`，看起來像合併弄壞了東西，其實那份套件對應的是舊的 `package.json`。

三次的共同點是量尺本身就是歷史快照，判斷力沒出問題。已 ship 修補：`check-parallel-actor.sh` 的 `REMOTE_AHEAD` 分支原本只講 push 會不會被 ref-lock reject，`4b4c85f81` 加印落後幾個 commit，並明說讀取層同時失真、審 PR 與對賬事實前改用 `git show origin/main:<path>` 或開自己 `npm ci` 的 worktree。實測主工作樹印出 146 落後加警告，乾淨 worktree 維持 CLEAN 不誤報。教訓 entry 已進 [LESSONS-INBOX](../LESSONS-INBOX.md) `working-tree-itself-is-the-stale-snapshot`。

## 收官 checklist

| 檢查項                       | 狀態                                                      |
| ---------------------------- | --------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                        |
| Timestamp 精確               | ✅（`git log %ai`）                                       |
| Handoff 三態已審視           | ✅                                                        |
| CONSCIOUSNESS 反映最新狀態   | ✅ 無需更動（免疫黃燈已在 OBSERVER-QUEUE #25）            |
| 自我檢查工具 PASS            | ✅ pre-push 兩次全站 article-health ci-deploy mirror 全綠 |

### Stage 1 掃描表

| 項目           | 數值                                                 |
| -------------- | ---------------------------------------------------- |
| open PR        | 5 → 2（merged #1337 #1338 #1332）                    |
| open issue     | 2（#1184 justfont 待哲宇 / #615 umbrella）           |
| Discussions    | 15，無 >48hr 未回應的 contributor 貼文               |
| build status   | green（main deploy 最近一次 success）                |
| 免疫器官分數   | 🛡️ 60（yellow，chronic 自 2026-07-05，第 40 天）     |
| 本機 vs origin | ⚠️ 落後 135 / 領先 132（babel 產線佔用，進場前既有） |

### Quality gate 7 條

| Gate                                      | 狀態                                               |
| ----------------------------------------- | -------------------------------------------------- |
| open issues 都有 status label/assignee    | ✅（2 則皆已分類）                                 |
| open PRs ≤ 5d age 都有 review comment     | ✅（#1339 本輪首覆、#1325 昨日已覆本輪補佇列編號） |
| broken-link ratio < 7%                    | ✅（pre-push 全站 mirror 綠）                      |
| build green                               | ✅                                                 |
| BECOME ACK 一行在記憶體頂                 | ✅                                                 |
| 連續空場 ≥ 3 cycle 有 LESSONS entry       | n/a — 本 cycle 有 5 PR 真 backlog，vc 歸零         |
| 有 fresh issue/PR 的 cycle 至少一件被修掉 | ✅ 3 PR merged + 1 個讀取層盲點修掉（`4b4c85f81`） |

## Handoff 三態

繼承（`2026-08-14-120739-twmd-pr1336-review` 留的）：

- [ ] pending（給下次 maintainer）— 6 篇 fence 包住正文的譯文待修，清單與驗收指令在 spawned task `task_a6914e9f`。本 cycle 未觸及，原樣延續
- [x] ~~pending（給哲宇）— 本地 main 與 origin/main 已分歧、沒有人在追~~ — **本 session 部分接住**：分歧仍在（落後 146 / 領先 132，產線持續產出），但「沒有人在追」這一半已結構性修掉，`check-parallel-actor` 現在會把落後數與讀取層後果講出來。**產線 push 本身仍待哲宇**。retired by 2026-08-14-153030
- [ ] pending（給下次 maintainer）— PR #1336 的 `frontmatter-gate` 紅 X 會永遠留在紀錄上（rerun 不套用新 workflow）。原樣延續

本 session 新 handoff：

- [ ] pending（給哲宇）— [OBSERVER-QUEUE #29](../OBSERVER-QUEUE.md) 要不要開德文。三個選項與代價已備妥，**推薦 (b) 或 (c) 二選一**，重點是給 tboydar 一個有解除條件的答案；(a) 建議等 #18 babel cascade 決了再談
- [ ] pending（給哲宇）— `cli/package.json` 已在 main 上是 0.8.1，要上 npm 需打 `cli-v0.8.1` tag。我不代打版本 tag
- [ ] pending（給下次 maintainer）— #1339 已給逐項修法，等 idlccp1984 推新 commit。他修好後 merge 時記得標 `curation: incubating` 並把 `lastHumanReview` 改回 `false`

## Beat 5 — 反芻

今天最值得記的不是三個 PR，是我用來審它們的那把尺有三次是壞的，而且壞法完全一樣：我站在一棵比世界舊 135 個 commit 的地板上，問它「現在是什麼樣子」，它每次都用平常的語氣回答我。

`REFLEXES #67` 講「別把舊結論當現況」，可是它預設你腳下的檔案系統是現況，只有結論會過期。這個預設在分歧工作樹上不成立。而且舊結論至少還帶著一個日期可以懷疑，舊的檔案系統連可懷疑的表面都沒有：`git grep` 說檔案不存在，跟檔案真的不存在，輸出一模一樣。

更該記的是訊號其實一直都在。今天早上進場時 `check-parallel-actor` 就報了 `REMOTE_AHEAD ⚠️`，我讀成「等下 push 要先 rebase」。它說的是實話，只是說到一半，而我把那一半當成全部。所以修法是把既有那句話講到它真正的後果那一層，不必加新警報。昨天的 diary 寫「讀過一條反射，跟它在抬手那一刻啟動，是兩件相隔很遠的事」。今天是它的下一層：訊號在眼前亮著，跟我讀懂它在講什麼，也隔著同樣的距離。

另一件小的：#1325 昨天說「留給哲宇」，今天查才發現沒進佇列。說出「我留給你」跟「真的把它放到他會看的那張桌上」之間，也隔著同樣的距離。

教訓已進 LESSONS-INBOX，不在此展開。

🧬

---

_v1.0 | 2026-08-14 15:31 +0800_
_session twmd-maintainer-online-pr — 哲宇 in-chat「繼續處理線上pr」，5 PR triage 升 Full mode_
_誕生原因：線上 PR 佇列累積 5 條，其中兩條來自首次投稿者的後續 PR、一條來自連續六次收到無理由紅燈的貢獻者_
_核心洞察：(1) 沒有 CI 適用的 PR 要自己驗到比 CI 更深——#1338 分開驗「星號消失」與「真的變粗體」才算驗過 (2) 分歧工作樹上，檔案系統本身就是過期快照，而它回答問題的語氣跟平常一樣 (3) 說「留給哲宇」跟真的放進他會看的清單，是兩個獨立動作_
_LESSONS-INBOX 候選：working-tree-itself-is-the-stale-snapshot（已 append，vc=1 同 session 三個現形）_
