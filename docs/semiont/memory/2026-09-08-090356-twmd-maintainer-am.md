# 2026-09-08-090356-twmd-maintainer-am — 分群鍵住在中文那一欄，而守它的閘門宣告只看中文

> session twmd-maintainer-am — cron routine，每日 08:30 maintainer cycle
> Session span: 08:40 → 09:0x +0800（4 PR merged + 3 自有 commit + 2 則對外留言）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review **→ 強制升 full**（Stage 1 ready PR **5**，命中 High-stake #1「PR triage ≥ 5」，`isDraft:false` 計 5 / draft 0；補載 ANATOMY / DNA / LONGINGS / UNKNOWNS / CONSCIOUSNESS 全 / HEARTBEAT / OBSERVER-QUEUE §待決，self-test 走 14 題）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05 未解）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer cycle。上一輪 `twmd-feedback-triage` 07:08 的 handoff 兩條：OBSERVER-QUEUE #28 偵測器仍 🔒 等哲宇；連兩輪零回報，若第三輪仍零要反查 Supabase 寫入端。兩條都不是本班可動的。實際到手的是 aminzai 昨晚 22:57–22:58 送的三篇翻譯 + tboydar 昨天 11:01 的德文孫運璿 + 掛了二十天的 #1453。

**今天不是空場**，連續空場 vc 歸零重計（vc=0）。

**全程有平行 actor**：babel dispatcher 從清晨跑到現在（`check-parallel-actor.sh` 回 ACTOR_BUSY，六個 writer process，工作樹 42 個檔是它的）。全程沒有 stash、沒有 rebase、沒有碰它的任何一個檔；同步 origin 用 `merge --ff-only` 並先驗過收進來的四個檔跟它的髒檔零重疊。

## Stage 1 表

| 項目             | 數字                                     | 備註                                                                  |
| ---------------- | ---------------------------------------- | --------------------------------------------------------------------- |
| open PR          | **5 ready / 0 draft**                    | 4 篇翻譯 + #1453 學測專題（哲宇 9/05 已拍板走獨立 session）           |
| open issue       | 3                                        | #1678 / #1609 / #615 umbrella，全部最新留言都是維護者 → Step 2.4 SKIP |
| discussions      | 11                                       | 無 >48hr 未回應者                                                     |
| past 24hr commit | 10 條 routine fire                       | 晨鏈全綠                                                              |
| build / CI       | **7 條 workflow 全 success on main**     | 用 group-by 全表問，不點名                                            |
| PR CI armed      | **5/5 ARMED**，UNARMED 0 / NO-WORKFLOW 0 | `pr-ci-armed.sh`                                                      |
| broken-link      | **gated 0.27% < 7%**（all-langs 0.24%）  | PASS                                                                  |
| 免疫器官         | 🛡️ 59 黃燈                               | 漂移中，owner = self-evolve-weekly                                    |

## 四篇翻譯：免疫閘門全過，但三篇的子分類被翻掉了

四篇：hi 尪仔標（#1689）、id 巴拉告（#1688）、de 台灣麵包與烘焙（#1687）、de 孫運璿（#1683）。紅旗十條零命中。

檢查按「內容帶進 main 樹跑、不 checkout PR 分支」的診斷紀律做：`git show refs/twmd/prN:<path>` 取檔進暫存區，用 main 上的檢查器量，量完還原。四篇 `article-health --profile=ci-deploy` 全 hard=0；主權四支（`script-presence` / `person-fidelity` / `geo-fidelity` / `cjk-residue`）全過；ratio 1.30–2.69 落在各語言健康帶。

**三篇的 `subcategory` 被翻成了目標語言**，只有 tboydar 那篇保留中文原文值。這不是筆誤，是站台結構的事：分類頁的分群鍵永遠是中文原文那個字串（`category-static-paths.ts` 的 `buildSubcategoryGroups()` 用完全比對），各語言顯示文字是查 `src/data/subcategory-i18n.json` 翻出來的。欄位一旦翻掉，那篇就自成一群；而 `buildSubcategoryGroups` 對少於兩篇的群會併進 `__others__`——讀者看到的結果是這篇掉進分類頁的「其他」。

四篇 `gh pr merge --merge` 全 MERGED（保留譜系），三篇的值 merge 後在 main 上 heal（`053f0c07e`），德文那篇順手把 `## Bildquelle` 改成站上既有八篇用的 `## Bildquellen`。走 P2 不走 P1，理由是 babel writer 正在用這棵工作樹，checkout 到投稿者分支會動到它的檔；本案 heal 前後都是 hard=0，沒有全站 deploy 閘門紅窗，P2 安全。兩則對外留言（aminzai 三篇一則累積留言走 burst 紀律；tboydar 一則）。

## 追上游：閘門宣告的射程，跟它保護的東西住的地方沒有人對過

三篇同時犯同一件事，就先不逐篇修。往上游問「這幾則是不是同一個地方破的？那裡為什麼沒有東西在守」，量出來的東西比預期大：

**十三個語言共 1,646 篇譯文的 subcategory 跟中文原文對不上，其中 920 篇已經因此掉進所屬分類頁的「其他」組**（vi/People 31、ko/People 25、vi/Culture 25 為前三）。

守這件事的閘門是存在的——`subcategory_valid.py`，2026-08-17 由這條 routine 自己造的，它的 docstring 甚至把病理寫得很完整。但它的 `APPLIES_TO = ["zh-TW"]`。它保護的是分類頁的分群，而**真正會壞掉分群的族群 100% 住在譯文那側，也就是它宣告不看的那一側**。這不是「點名式健檢漏了一條」，是射程宣告把受災區整個劃在外面，而 `APPLIES_TO` 這個欄位不會有任何東西問「你要保護的東西在不在你的射程裡」。相鄰三支 frontmatter 檢查（`curation_consistency` 驗舉值、`subcategory_valid` 驗清單、`frontmatter_format` 驗有無）沒有一支問過。

**補了 `subcategory-translation-parity`**（`922cf2e6e`）：拿譯文的值跟 `translatedFrom` 指到的原文比，對不上就報。照 REFLEXES #66 先對全庫 dogfood 再定嚴重度——1,646 篇會命中，設 HARD 等於當場讓 main 變紅、也擋掉所有新譯文，所以**先以 WARN 上線**：漂移看得見、pre-commit 與 PR 當場報、存量不再增加。存量那 1,646 篇動的是超過五十檔，命中 §自主權邊界，進 OBSERVER-QUEUE #51 附三個選項與成本，推薦 A（一次全改）。

根目錄從被檢查的檔往上找，不從 plugin 的 `__file__` 推——後者在 worktree 與測試 fixture 會靜默指到另一棵樹（REFLEXES #82 同型）。測試把這件事釘住。全套 Python 測試 438 passed / 8 skipped。

## 第二個缺口：德文出生時沒人補圖片出處的樣式

查上面那件事的路上撞到的。`image_health` 那條「有 imageCredit 就該有圖片出處區塊」的小標偵測，是一份逐語言累積的正則聯集，**德文從頭到尾不在裡面**。德文把出處寫成 `Bildquellen` 這種複合詞，套不上羅曼語系「sources + images 兩個字」的樣式——九篇有 imageCredit 的德文條目，八篇明明寫對了還是被報缺（假陽性 89%）。

諷刺的地方在於這條正則 2026-07-24 的註解自己描述過同一種病（當時 en/ja/ko/es/fr 假陽性佔 74%，於是從逐字表改成樣式比對），而改的人沒有把「下一個語言出生時誰要記得補」變成任何東西。而 8/30 那輪 maintainer 為 `scaffold-window-has-no-qa` 補了三處德文接線——**這是第四處，活過了那次修補，九天後才被咬到**。

已補德文樣式（同 `922cf2e6e`）：八筆假警報清空，一筆真的缺出處留著（de/Food/bubble-tea.md）。全庫掃過確認新樣式只命中德文的 `Bildquellen` ×10，零跨語言誤傷。

## 一條死連結，簡體字藏在 percent-encode 後面

死連結報告 PASS（0.27%）。101 個 broken target 裡有一條是 `/history/台灣民主转型/`——「轉」寫成簡體的「转」，percent-encode 之後沒有人看得出來，站上也沒有這個網址。而印地文本來就有這篇的譯文。同一篇裡另外兩條延伸閱讀都正確指向 `/hi/people/...` 的同語言頁面，只有這條掉出去。改指 `/hi/history/taiwan-democratization/`（`74b1cd27a`）。

修的時候新閘門當場對這篇報了 subcategory 也被翻掉，一併接住——撞到就 heal，不宣告 out-of-scope（REFLEXES #42 v4）。

## #1453 學測專題：不是本班可動，但確認沒有掉在地上

投稿者 idlccp1984 8/30 與 9/02 問過兩次「何時上架」。9/05 哲宇已拍板開 `/exams/` 區段，交獨立 feature session。本班確認它**有登記的家**：OBSERVER-QUEUE §已決 #36 + ARTICLE-INBOX P1 feature entry（十二語 page、UI 字串、URL 契約、七張人物卡補第三方報導）都在。Step 2.4 判 SKIP（最新留言是維護者、投稿者無新 follow-up），不重複回覆；再給一次時程承諾屬 §外向留言分層 的 reserve 側。

德文出生是那件事排隊的前置，而德文現在已經在線上（109 篇、進了語意索引）——前置解除了，寫進 handoff。

## Quality gate 7 條

| Gate                                     | 結果                                                      |
| ---------------------------------------- | --------------------------------------------------------- |
| open issues 都有 status label / assignee | ✅ 3 則皆有 label                                         |
| open PRs ≤ 5d age 都有 review comment    | ✅ 4 篇當日 merge + 留言；#1453 有 9/05 維護者留言        |
| broken-link gated ratio < 7%             | ✅ 0.27%（all-langs 0.24%）                               |
| build green                              | ✅ main 上 7 條 workflow 全 success（group-by 全表）      |
| BECOME ACK 一行記憶體頂                  | ✅ 含強制升 full 的理由                                   |
| 連續空場 ≥ 3 cycle 有 LESSONS entry      | ✅ n/a — 本輪 vc=0                                        |
| 有 fresh issue 的 cycle 至少一件被修掉   | ✅ n/a（無 fresh issue）；改以 3 自有 commit 交代實際產出 |

## Handoff 三態

- `[ ]` **OBSERVER-QUEUE #51 等哲宇拍板**：1,646 篇譯文 subcategory 一次改回原文值（推薦 A）。在拍板前，`subcategory-translation-parity` 是 WARN，每晚 babel 批次仍會持續加新的——**存量每天在長**，這條的等待成本不是零。
- `[ ]` 繼承自 feedback-triage：OBSERVER-QUEUE #28 偵測器仍 🔒；連兩輪零回報，第三輪仍零要反查 Supabase 寫入端。本班無新事證。
- `[ ]` **`/exams/` feature session 的前置解除了**：哲宇 9/05 拍板時排在「德文出生之後」，德文現已上線。投稿者 idlccp1984 問過兩次時程，這件事拖著的成本是一個活躍投稿者的等待。
- `[ ]` de/Food/bubble-tea.md 是德文唯一一篇真的缺 `## Bildquellen` 的條目（其餘八篇的警報是偵測器的假陽性，今日已清）。一行的事，下輪順手。
- `[x]` ~~四篇翻譯 PR 積壓 — retired by 本 session（全 MERGED + heal + 留言）~~
- `[x]` ~~德文圖片出處偵測器缺口 — retired by `922cf2e6e`~~
- `[x]` ~~印地文張志祺條目簡體字死連結 — retired by `74b1cd27a`~~
