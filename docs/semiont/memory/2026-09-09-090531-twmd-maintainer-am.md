# 2026-09-09-090531-twmd-maintainer-am — 文件寫著四道閘，產線只走三道，那道沒接上的漏了三千多處

> session twmd-maintainer-am — cron routine，每日 08:30 maintainer cycle
> Session span: 08:37 → 09:2x +0800（7 PR merged + 5 自有 commit + 3 則對外留言）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review **→ 強制升 full**（Stage 1 ready PR **8**，命中 High-stake #1「PR triage ≥ 5」，`isDraft:false` 計 8 / draft 0；補載 ANATOMY §生命週期+§資源地圖 / DNA 全 / CONSCIOUSNESS §警報+§適應性反應 / OBSERVER-QUEUE §待決 / LESSONS §未消化標題全覽 / MAINTAINER-PIPELINE 全檔，self-test 走 14 題）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05 未解）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer cycle。上一輪 `twmd-feedback-triage` 07:09 的 handoff 是「反查寫入端已兌現，殘留未知是今天送一筆會不會成功」，不是本班可動的。到手的是 tboydar 昨天送的四篇德文人物 + aminzai 今晨的三篇（de/id/hi）+ 掛了二十一天的 #1453。

**今天不是空場**，連續空場 vc 歸零重計（vc=0）。

**全程有平行 actor**：babel dispatcher 連續第三天在跑（`check-parallel-actor.sh` 回 ACTOR_BUSY，六個 writer process）。全程沒 stash、沒 rebase、沒碰它的任何一個檔；每次動檔前先 `git status` 確認那支檔是乾淨的。

## Stage 1 表

| 項目             | 數字                                     | 備註                                                             |
| ---------------- | ---------------------------------------- | ---------------------------------------------------------------- |
| open PR          | **8 ready / 0 draft**                    | 7 篇翻譯 + #1453 學測專題                                        |
| open issue       | 3                                        | #1678 / #1609 / #615，最新留言都是維護者 → Step 2.4 SKIP         |
| discussions      | 11                                       | 無 >48hr 未回應者                                                |
| past 24hr commit | 10 條 routine fire                       | 晨鏈全綠                                                         |
| build / CI       | **1 條紅：Engineering contracts**        | 用 group-by 全表問，不點名——點名式只看得到造它的人想得到的那幾條 |
| PR CI armed      | **8/8 ARMED**，UNARMED 0 / NO-WORKFLOW 0 | `pr-ci-armed.sh`                                                 |
| broken-link      | **gated 0.27% < 7%**（all-langs 0.24%）  | PASS；dist 是 9/07 的，數字帶兩天齡                              |
| 免疫器官         | 🛡️ 59 黃燈                               | 漂移中，owner = self-evolve-weekly                               |

## CI 紅燈：倉庫沒動，是新的資安通報讓閘門翻紅

昨晚 22:17 的 `Engineering contracts` 掛在 `workers/mcp` 那一步：`npm audit` 讀到 sharp 0.35.2 的 libheif 高風險通報，而這個 sharp 是 wrangler → miniflare 一路帶進來的開發相依。repo 本身零改動。

上游的 miniflare 目前把 sharp 寫死在 0.35.2，升 wrangler 沒用；npm 建議的 `--force` 會把 wrangler 降回 4.15.2（跨大版本回頭）。改用 `overrides` 把 sharp 拉到官方修好的 0.35.4，本機照 CI 那一行原樣跑過三段全綠（`c7d6cfa20`）。

## 七篇翻譯：全綠，而且腳註來源一條都沒動過

tboydar 四篇德文人物（林獻堂 #1690、三毛 #1691、張忠謀 #1692、羅大佑 #1693）、aminzai 三篇（de 鼎泰豐 #1694、id 陳樹菊 #1695、hi 台灣山椒魚 #1696）。紅旗十條零命中。

檢查照「內容帶進 main 樹跑、不 checkout PR 分支」的診斷紀律：`git show refs/twmd/prN:<path>` 取檔、量完刪回（七個路徑都先驗過 `git ls-files` 確認是新檔，不是已在 main 的檔——`rm` 對前者才是對的）。七篇 `article-health --profile=ci-deploy` 全 hard=0；`script-presence` / `person-fidelity` / `geo-fidelity` 全過。

**兩件值得記的**：

1. **subcategory 七篇全部保留中文原文值**。昨天那輪四篇裡三篇翻掉、進了 OBSERVER-QUEUE #51；今天七篇零命中，同日上線的 `subcategory-translation-parity` 也零報。一天的樣本不夠說閘門有效，但方向對。
2. **腳註 URL 逐條對照原文，136 條零新增零改動**（去重後與各自的中文版完全一致）。翻譯最常見的失手是順手補一個看起來合理的來源，這批一條都沒有。

七篇 `gh pr merge --merge` 全 MERGED。兩則對外留言走 burst 紀律（同一投稿者整批一則）。

## 追上游：閘門寫進了 pipeline，但沒有任何一支程式呼叫它

德文那批順手拿 `cjk-residue-check` 掃全庫當背景對照，143 行裡大半是合法的（腳註引的中文維基條目名、圖片作者的中文帳號、德文引號 `„懋"` 裡的字形解釋——那支的豁免清單沒收德文的下引號），但混著三篇真的壞掉。換上判準更精準的 `cjk-adjacency-check`（漢字直接黏在拉丁字母上），掃十個非漢字語系：

**3,967 處 / 1,557 檔**。其中帶簡體字的高信心漏譯 **461 處 / 284 檔**——`विभिन्न节点`、`Ван Юнцин提出了`、`benar-benar动手`、`مدرسة国语`。簡體字不可能是刻意保留的原文對照。

回頭查為什麼一路沒人擋：`grep -rn "cjk-adjacency" scripts/` **零命中**。`SQUEEZE-MODELS-MAX-PIPELINE` 把它列為「四道閘之一」，產線的 `translate.py` / `patch-translate.py` 呼叫的只有 `cjk-leak-check`，而那支對非漢字語系要求「連續 N 個以上漢字」——兩三個字的短片段正好在門檻底下，那正是 adjacency 2026-08-09 被造出來要補的盲區。

**這不是忘了接**。那支的 docstring 自己寫了為什麼刻意獨立：「那支正在被線上產線呼叫，批次跑到一半改它的判準會讓同一批的前後段用不同標準驗收。」當時的判斷是對的，代價是它誕生時就處在「造好了但沒接上」的暫時狀態，而沒有任何東西在追蹤這個暫時狀態什麼時候該結束。**暫時的未接線跟永久的未接線，長得一模一樣。**

處置：德文那三處當場修（`Đài水`= 越南文的台黏著沒翻的水，四處都是「淡水」；`das麻辣` 缺空格；`Taoyuan市政府新聞稿` 翻一半）——德文全庫命中從 14 降到 7，剩下七處全是誤報。存量 1,557 檔超過五十檔紅線 → OBSERVER-QUEUE #52，三個選項＋推薦 A（先接線擋增量，簡體那 284 檔優先清），並寫明接線要等這批 babel 收工。量測落 `reports/translation-fused-residue-2026-09-09.md`。

## 一條幻覺連結，順著投稿追回中文原文

印尼文陳樹菊那篇報了兩條連結目標不存在。追回中文原文，源頭在 `knowledge/People/陳樹菊.md`：`/lifestyle/台東市集` 跟 `/society/台灣慈善文化` 兩篇從來沒存在過——寫的時候「想到應該有這樣一篇」，然後九個語系各抄了一份。

改指既有的兩篇（台灣市場文化與傳統市場、台灣志工文化與公益參與），連結文字與描述一併改成對得上新目標的說法，不留「文字寫 A、連到 B」的錯位。**譯文那側不手動追改**：改了中文的內容雜湊之後 babel 會把九個語系標成待更新，讓它自己流過去——這是 SSOT 架構本來就該有的走法，手動追九檔反而是繞過它。已在給 aminzai 的留言裡講明這是原文的問題、不是他的。

## #1453 學測專題：第二十一天，量了才知道還差多遠

idlccp1984 9/08 又問了一次何時上架。哲宇 9/05 已拍板開 /exams/ 區段，卡住的是三件事，今天量了兩件：

- **多語**：站上開 13 個語系，模板的 `gsatCopy` 只有 `'zh-TW'` 與 `en` 兩份，其餘 11 個走 `?? gsatCopy['zh-TW']`——德文、阿拉伯文、印地文讀者會看到滿頁中文。合併即上線，這個狀態不能對讀者開。
- **人物卡**：描述含對在世真人的具體事實（「一家四兄妹全考滿分、大哥二哥已任外交官」「醫學系讀九年」「考試院長之子」），每張各需一則第三方報導。逐張查，不是格式問題。
- **URL**：模板註解寫 `/exams/gsat/`，`src/pages/exams.astro` 建出來是 `/exams/`。我們自己改。

留言逐條講清楚，並明說**不能給日期**（對外承諾時程是真人的事）。他建議加唐鳳，回覆說明那要跟其他人物卡一起處理。PR 保持開著。

## Issue：兩則都留著，理由是判斷不是省略

- **#1678 生態多樣性（遊蕩犬貓威脅）**：9/06 已答，缺的是正文實質改寫（那篇零腳註、2,091 字），走 REWRITE 不在 maintainer heal 範圍，研究已落 ARTICLE-INBOX。最新留言是維護者、無新 follow-up → Step 2.4 SKIP。
- **#1609 郭淑姿日記的「無語」**：8/28、8/31 兩輪已答，卡在調閱國家人權博物館出版的兩冊日記；查證已排進用語趨勢 routine。同樣 SKIP（REFLEXES #80：已 escalate 的 chronic 條目，後續 cycle 靜默不是 renew）。

## Quality gate（7 條）

| 條目                         | 結果                                                          |
| ---------------------------- | ------------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE | ✅ Stage 1-4 全跑                                             |
| PR 分流按 §collect-and-merge | ✅ 全 B 路徑，7 merged / 1 leave-open 附理由                  |
| routine PR backlog ≤ 3       | ✅ 0（routine main-direct 不開 PR）                           |
| broken-link gated ratio < 7% | ✅ 0.27%（dist 9/07，數字帶兩天齡）                           |
| build green                  | ✅ 紅的那條當場修掉（`c7d6cfa20`），推上去後看下一輪          |
| merge 的 PR 都過 hard gate   | ✅ 紅旗 10 條 + CI + article-health ci-deploy + 主權三支      |
| 有 fresh issue 至少修一件    | ✅ 無 fresh issue；本輪仍有四件實修（CI／德文三篇／幻覺連結） |

## Handoff

- `[ ]` **pending — OBSERVER-QUEUE #52 等哲宇拍板**：譯文漏譯存量 1,557 檔（高信心 284 檔）。接線動作本身還卡一個時機條件：babel dispatcher 收工後才能接，否則是批次跑到一半改驗收標準。
- `[ ]` **pending — adjacency 接線前要先補三類誤報**：相對連結目標 `](/technology/AI發展)`、wikilink、括號內小寫品牌名 `g0v`。補在 `cjk-leak-check.legit_spans()` 這份共用清單裡，不要第四支各寫一份（REFLEXES #83 第三次現形）。
- `[ ]` **pending — #1453 /exams/**：三件缺口已量化寫進 PR 留言，等專門 session。
- `⏳ blocked — #1609\*\* 等調閱《郭淑姿日記》兩冊；owner = 用語趨勢 routine。
- `⏳ blocked — #1678\*\* 等〈生態多樣性〉重寫；研究已在 ARTICLE-INBOX。
- `[x]` ~~retired — 昨天 handoff 的「七篇新譯文 subcategory 是否又被翻掉」：今天七篇零命中，parity 閘門零報~~
