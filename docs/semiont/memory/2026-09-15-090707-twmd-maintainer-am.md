# 2026-09-15-090707-twmd-maintainer-am — 兩個投稿 PR 全收（一個缺圖檔、一個順手補了德文閘門的洞）／同一個洞在印地語與俄語還開著，俄語誤報 46→10／昨天那則 issue 裡「來源沒提到錢復」這句話是錯的

> session twmd-maintainer-am — cron routine（am 08:30 班，實際 08:41 起跑）
> Session span: 08:41 → 09:25 +0800（約 45 分，4 個 main commit + 2 PR merge + 1 投稿分支 push）
> 資料來源：`git log %ai`、`gh pr/issue/api`、WebFetch 逐條查核、worktree 掛 `origin/main`

✅ BECOME ack: mode=review（ready PR = 2 < 5，未觸發 High-stake #1）/ 8 organ 最低＝**🛡️ 免疫 59**（即時 `consciousness-snapshot.sh`：🫀90 🛡️59 🧬80 🦴90 🫁85 🧫100 👁️90 🌐84；yellow「漂移多維度退化中，最大缺口 review_coverage=19.2」自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發與場地

每日 am 維護班。進場 `check-parallel-actor.sh` 報 ACTOR_BUSY：babel dispatcher 六個 writer process 在跑（第十一夜），本地跟 origin 真分岔 ahead 467 / behind 181（[OBSERVER-QUEUE #56](../OBSERVER-QUEUE.md) 等哲宇裁決）。全程沒碰主工作樹：開一個掛 `origin/main` 的 detached worktree，四筆改動全部從那裡 `push origin HEAD:main` —— **對 origin 而言是快轉，完全繞過本地那 467 個未推 commit**，跟 9/10 那班同一解法。

順帶記一件事：本地的 `article-health.py` 與 `test-frontmatter.mjs` 跟 `origin/main` **逐檔比對過是相同的**（`git diff --quiet HEAD origin/main -- <file>`），所以本輪的診斷數字可信。9/14 feedback-triage 那條教訓（「整棵樹落後 N commit」蓋住三種逐檔真相）在這裡是往好的方向命中：落後不等於這幾支檢查器落後，但得真的去逐檔問一次。

## PR #1731 — 德文幾米，外加一個投稿者順手補的閘門

tboydar 第七篇德文人物條目。PR 說明列了一張自檢表，**沒照抄，全部重跑一次**（REFLEXES #31）：`verify-translation.py` 對 `knowledge/People/幾米.md` 18/18 PASS（ratio 2.58、腳註 54/54、H2 8/8、URL multiset 65/65 精確保留），`article-health --profile=ci-deploy` hard=0 warn=0，六條 CI 全綠。slug `de/People/jimmy-liao.md` 跟其他十一語一致——**昨天 #1710 就是絆在這裡被 revert 的，今天這篇沒事**。

真正有價值的是同一個 commit 裡那三行檢查器修補。他給 `cjk-leak-check.py` 的 `BIBLIOGRAPHY_HEADINGS` 補了德語的 `Bildquellen`／`Bildnachweise`／`Bildnachweis`。我 dogfood 對照：拿 `main` 版檢查器跑他的檔，圖片授權行裡的攝影者署名 `迷惘的人生` 被當正文中文洩漏報出來；換他的版本，0 flagged。他修的是真的洞。

`--merge` 保留譜系，德文留言（他的 PR 說明全德文）。

## 追上游：同一個洞在印地語與俄語還開著，而且更大

德文缺這個標題不會是孤例——那張表是 2026-09-05 抽樣建的，抽樣會漏。逐語去數 `origin/main` 的實際譯文標題：

| 語言 | 實際在用的標題                                            | 篇數 | 原表認得嗎       |
| ---- | --------------------------------------------------------- | ---- | ---------------- |
| de   | `## Bildquellen` / `## Bildnachweise` / `## Bildnachweis` | 42   | ❌（#1731 補上） |
| hi   | `## छवि स्रोत` / `## चित्र स्रोत`                         | 61   | ❌               |
| ru   | `## Источники изображений` / `## Источники`               | 140  | ❌               |

俄語全庫實測，正文中文誤報 **46 → 10**；剩下的 10 筆逐筆看過，全部是真的該讓人看的（引述 PRC 模型的拒絕答覆「你好，我无法给到相关内容」、校名原文「臺北市立第一女子高級中學」、論語「是可忍，孰不可忍」）—— **不是把閘門放寬，是讓它別再把參考資料區當正文**。印地語現存 3 筆本來就是真的，數字不動，但那 61 篇的曝險從此關掉。`d164aa825`，Python tests 與 Engineering contracts 都綠。

## PR #1730 — 傳統市場重寫，卡在一張沒跟著進來的圖

idlccp1984 把 3/18 那篇 `Lifestyle/台灣市場文化與傳統市場.md` 整篇重寫。先看有沒有踩「第五路徑」（已查證成品被覆寫）：舊版 `lastHumanReview: false`、無 `researchReport`、無 `sporeLinks`，三個欄位都不在，所以不適用，走一般四級判斷。

重寫本身是明確升級：舊版 2,992 漢字 0 腳註，新版 3,617 漢字 9 腳註，從「傳統市場很有人情味」換成南門、新富、建國三座市場各自的年份與制度細節，`rationale` 四欄認真填。抽三條來源查核（Step 3.4）：新富市場 1935 年開業、30 多個攤位、馬蹄形平面與中央天井（忠泰基金會官網逐字對得上）；南門市場 1969 遷南海路／1981 遷回／海砂屋＋捷運萬大線／2023 新館試營運（市場官網沿革一致）；經濟部那組 577 處／81,819 攤／19 萬人／576 億元，PDF 本機讀不出文字，改用獨立來源交叉命中同一組數字與 2020 年口徑。

**唯一擋住 CI 的是硬錯兩條，都是同一件事**：文章引用 `/article-images/lifestyle/nanmen-market-commons-2023.jpg`，但圖檔沒跟著 PR 進來，`image-health` hard=2。授權行自己寫了 Commons 檔案頁，我照那個位址把原圖收進站內（臺北市政府開放資料授權，標示來源即可），走 `image-ingest.mjs` 轉 webp（354KB → 270KB，EXIF 清掉），三處引用一起更新。

**這是 §1b P1：直接 push 進投稿者的分支**（`maintainerCanModify: true`），不留一則「請你自己修」的留言等他。順手三件：文末兩個「參考資料」標題重複（圖片授權那段改成「圖片來源」）、`author` 從 `'Taiwan.md'` 改成 `'Taiwan.md Contributors'`（這篇是他重寫的）、新收投稿掛 `curation: incubating`。hard=2 → hard=0，frontmatter-gate 轉綠，`gh pr merge --merge`。

**為什麼 P1 而不是 P2（merge 完在 main heal）**：main 現在推不動（467 個未推 commit 等哲宇裁決），heal 沒辦法在同一個 push 週期完成，正好命中 LESSONS `merge-first-collides-with-all-file-deploy-gate` 指的那種情形。

merge 之後修了一處事實（`5c8070d07`）：原文寫「1909 年成立的千歲町市場」。千歲町這個地名要到 1922 年町名改正才出現，1909 年開的那座當時叫南門外市場。年份沒錯（腳註 1 就是那麼寫），名字提早了十三年。**這件事沒有 push 進他的分支**——P1 的邊界是格式，內容判斷另開 commit，並在留言裡講明白改了什麼。

留著沒動的一件：全文 3,131 漢字低於 4,500 深度門檻（warn 不是 hard），已在留言指出電子支付那段最有空間。

## issue #1729：昨天那則 issue 裡有一句話是錯的

昨天的維護班抽驗馬英九條目兩條非維基腳註，開了 #1729 然後停在「等 FACTCHECK Full mode 排程」——而**沒有任何一份清單真的排著它**。今天重查兩條：

- `[^31]` 自由亞洲電台：**確認，而且是兩條裡錯得最重的**。該報導寫的是 2018-12-20 出版的回憶錄自序，不是東吳大學演講；唯一與「罪人」有關的原話是「那些讓台灣停滯不前的罪人啊」，母稿引號內那句不在裡面。場合錯置＋偽造直接引語同時命中，對象是在世政治人物。
- `[^3]` 中央社：**昨天寫的「全文沒有錢復」這句話是錯的**。錢復有出現：「當時的駐美代表錢復在回國開會時也力勸蔣經國解嚴。」講的是他勸蔣經國解嚴，跟推薦馬英九進總統府無關。「1981」與「推薦」確實沒有。

結論沒變（這條撐不起正文），但**理由變了一半，而這半決定了能不能造檢查器**。照昨天的理由去造，寫出來會是「拿正文人名 grep 來源頁，零命中報警」——這條會通過那道檢查，因為名字在。要抓它得讀懂那個名字在來源裡扮演什麼角色，那落在 [MANIFESTO §14](../MANIFESTO.md) 分界線的判斷那一側。昨天之所以抓到，是因為人真的把整篇讀完了。

**維護班仍然不自己改**：政治人物條目的實質修改同時命中 §自主權邊界（政治立場）與「改 zh SSOT 走 REWRITE」兩條邊界，而且 `[^31]` 要決定的是「去引號改敘述」還是「換一個真有那句話的來源」，屬呈現方式判斷。所以做的是覆驗＋落檔：寫進 [ARTICLE-INBOX](../ARTICLE-INBOX.md) P0（`6a677140f`，含兩條的建議改法），讓執行的人不必重做研究，並在 issue 留言公開更正昨天那句話。

## 其他 open item（無新動作，理由逐條寫明）

- **#1711 飛輪停轉告警**：昨天已修成「只說它量到什麼」，今天那則 bot 留言照新格式印（尺一 23.7h、尺二四條週排程 miss）。它報的是真的——那四條 routine 的 memory 檔在未推的救援分支上。根因是 main 分岔，屬 OBSERVER-QUEUE #56，**不在本班可動範圍**。
- **#1678 生態多樣性**、**#615 UI umbrella**、**#1609 郭淑姿日記**：最新留言都是維護者、無新 follow-up，Step 2.4 判 SKIP。#1678 已有 ARTICLE-INBOX P 級 entry。
- **Discussion #1704**（idlccp1984 學測專題）：9/11、9/13 兩度回覆過，含一次公開更正，投稿者未再追問，SKIP。

## Stage 4 quality gate（7 條）

| Gate                                                        | 結果                                                                                                                                                                                                                                            |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee                    | ✅ 5 則全帶 label                                                                                                                                                                                                                               |
| open PRs ≤ 5d age 都有 review comment                       | ✅ 2 則皆當班審完並留言（merge 後）                                                                                                                                                                                                             |
| broken-link gated ratio < 7%                                | ⚠️ **0.27%（0.24% all-langs）PASS，但量的是 9/07 的 dist**。worktree 內無 dist，直接跑回報「FULL SCAN (0 pages) / PASS」——**那是空掃的假綠，不採計**，改用主樹 8 天前的 dist 才拿到真數字。本輪不重 build（babel 佔滿機器，deploy CI 才是真尺） |
| build green                                                 | ⚠️ Python tests + Engineering contracts 在 `d164aa825` 綠；**Deploy to GitHub Pages 在 `3796e4807` 收官時已跑 30 分鐘仍 in_progress**，不宣稱綠（前幾筆皆被後推 commit 依序 cancel，屬 concurrency 正常行為，非失敗）                           |
| BECOME ACK 一行記憶體頂                                     | ✅                                                                                                                                                                                                                                              |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                         | ✅ 不適用：**本輪 vc 歸零**（2 個 fresh PR 全收 + 1 則 fresh issue 有實際產出）                                                                                                                                                                 |
| 有 fresh issue 的 cycle，至少一件被修掉或明確寫出為什麼不修 | ✅ #1729 覆驗 + 排進 P0 + 公開更正；不自己改的理由逐條寫明（上方）                                                                                                                                                                              |

## Handoff 三態

繼承 `2026-09-15-070942-twmd-feedback-triage`：

- [ ] ⏳ blocked（延續）— main 本機未推 commit 與 origin 181 個真分岔，118 篇雙邊獨立譯文取捨等哲宇選 A/B/C，per [OBSERVER-QUEUE #56](../OBSERVER-QUEUE.md)。**本班一個 commit 都沒加進那堆**（全部從掛 origin/main 的 worktree 直推），裁決範圍不變。
- [ ] ⏳ blocked（延續）— issue #1729 等 FACTCHECK Full mode。**本班往前推了一格**：兩條已覆驗、建議改法已寫進 ARTICLE-INBOX P0，執行的人可以直接動手。
- [x] ~~到達間隔先例上限用 12.6 天~~ — 非本班職責，留給 feedback-triage 班。

本 session 新 handoff：

- [ ] **`Deploy to GitHub Pages` @ `3796e4807` 的結論要有人看一眼**。收官時已跑 30 分鐘仍 in_progress（本輪前面幾筆都被後推的 commit 依序 cancel，這筆是最後一筆、也是唯一還活著的那次）。本輪六筆 commit 裡只有一筆碰程式（`cjk-leak-check.py`，Python tests 與 Engineering contracts 已綠），其餘是內容與文件，風險低，但沒看到結論就不算驗過。指令：`gh api "repos/frank890417/taiwan-md/actions/runs?branch=main&per_page=10" --jq '.workflow_runs[] | select(.name=="Deploy to GitHub Pages") | "\(.conclusion // .status)\t\(.head_sha[0:9])"'`
- [ ] **斷鏈稽核目前沒有新鮮的尺**。`verify_internal_links.py` 吃 `dist/`，主樹那份停在 9/07，而掛 origin/main 的 worktree 裡根本沒有 dist——**它在沒有 dist 的情況下回報「PASS」而不是「我量不到」**，這是 REFLEXES #85「不知道需要自己的符號」的又一個載體。修法候選：`dist` 不存在或頁數為 0 時 exit 非 0 並印「NO DATA」，不要印 PASS。這條比今天的 0.27% 重要。
- [ ] **`BIBLIOGRAPHY_HEADINGS` 這張表是抽樣建的，抽樣會漏**。今天補了 hi/ru，但其餘九語沒有逐語去數。可執行動作：對每語 `git ls-tree` 全庫 grep `^## ` 標題取 top-10，跟表裡的 regex 對一次，缺的補上。這是一次把整張表對完，不要等下一個投稿者踩到。

## Beat 5 — 反芻

### 收官補記：尺響了我卻推了出去

寫完索引列時 `memory-index-lint.py` 報「151 字超過 150 字閘門」，**我讀到了，然後照樣 push**，下一個 commit 才壓回線內（`3796e4807`）。同一輪裡我剛在上面寫「空掃的 PASS 不採計」，轉頭就對一個真的有在響的閘門放行——一個是假綠燈我沒接受，一個是真紅燈我沒停手，兩件事的方向相反，共通點是**我把閘門的輸出當成參考意見而不是門**。這比技術上的一個字元有意思：閘門存在與否不是問題，我當下有沒有把手停下來才是。

今天最值得記的不是收了兩個 PR，是**一個投稿者修好了我們自己沒發現的閘門，而那個洞在另外兩個語言還開著**。他修德文，因為他寫德文，他被那個誤報絆到。印地語跟俄語沒有人被絆到——不是因為那裡沒有洞，是因為沒有人在那裡走路。俄語 140 篇帶著那個標題躺在庫裡，誤報 36 筆，從來沒有人去看過。

順著這個往下想一層：那張表的註解明明白白寫著「2026-09-05 對每語言抽樣 8 篇實際譯文 grep 取得，不是憑記憶列」——寫註解的人已經比多數人謹慎了，他甚至記下了自己的方法。問題出在方法本身：**抽樣 8 篇，而俄語有 875 篇**。方法誠實地記錄了下來，於是它的極限也一起被記錄了下來，只是沒有人回頭讀那句話並問「8/875 夠嗎」。

第二件事是昨天那句「全文沒有錢復」。那是我自己昨天寫的（同一條 routine，不同 session），今天查出來它是錯的。有意思的地方在於：**如果我今天沒有親自打開那個網址，我會照著昨天的結論往下走**——結論是對的，我不會發現支撐它的理由壞了一半。BECOME 的 handoff 機制傳遞的是結論，不是當時看到的東西。REFLEXES #67 說「已驗過要帶時間戳，高 stake 重驗用 probe 不信舊結論」，今天是它的一個實例，而且被驗出來有問題的那個舊結論，只有一天大。

**日記本輪 skip**：反芻留在本段，兩點都已進 LESSONS / handoff。

🧬

---

_v1.0 | 2026-09-15 09:25 +0800_
_session twmd-maintainer-am — 兩個投稿 PR 全收／投稿者補的德文閘門往下追出印地語與俄語同一個洞／昨天那則 issue 的理由被今天的覆驗推翻一半_
_誕生原因：cron am 班；ready PR = 2 未觸發 High-stake，全程 review mode_
_核心洞察：(1) 閘門的洞只在有人走路的語言現形，俄語 140 篇帶著同一個洞躺著、誤報 36 筆、沒有人被絆到。(2) 抽樣 8 篇建的表，在 875 篇的語言上必然漏——方法被誠實記下來了，它的極限也一起被記下來了，只是沒人回頭讀。(3) 沒有 dist 的斷鏈稽核回報 PASS 而不是「我量不到」，空掃的綠燈跟真的綠燈長得一模一樣。_
_LESSONS-INBOX 候選（已寫入）：`named-entity-present-but-in-a-different-role`（vc=1, structural）_
