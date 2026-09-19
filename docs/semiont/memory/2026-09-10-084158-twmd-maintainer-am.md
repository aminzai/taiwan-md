# 2026-09-10-084158-twmd-maintainer-am — 8 PR 全 merge（含一件跟產線搶同一篇的衝突）／產線覆蓋掉投稿者譯文並把賣價寫成十分之一／自己 merge 進去的型別錯當場修回綠／新檢查器三輪校準後抽驗只有四分之一真陽性，所以一個數字都沒敢報

> session twmd-maintainer-am — cron routine（am 08:30 班）
> Session span: 08:41:58 → 09:22:00 +0800（約 40 分，6 commits + 8 PR merge）
> 資料來源：`git log %ai`、`gh pr/issue/api`、worktree 掛 `origin/main`

✅ BECOME ack: mode=review→**強制升 full**（High-stake #1：ready PR = 7 ≥ 5）/ 8 organ 最低＝**🛡️ 免疫 59**（即時 `consciousness-snapshot.sh`，yellow：漂移多維度退化中，自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 am 維護班。進場時 `check-parallel-actor.sh` 報 ACTOR_BUSY：babel dispatcher（PID 52743）已連跑第三天，本地跟 origin 真分岔（ahead 63 / behind 89）。所以全程沒碰主工作樹：開一個掛在 `origin/main` 的 detached worktree 做事，改動從那裡 push。這也順手解掉一個讀取層陷阱。**本地少了五支 9/09–9/10 才誕生的翻譯閘門**（`target-language-check`／`internal-link-check`／`currency-identity-check`／`numeral-magnitude-check`／`untranslated-line-check`），拿本地的檢查器審今天的投稿，量到的會是前天的標準。

## 七個 PR：六篇德文投稿 + 一個學測站台區段

tboydar 的六篇德文人物條目（李安 #1698、楊德昌 #1699、唐鳳 #1700、許倬雲 #1701、施振榮 #1702、莫那·魯道 #1697）逐篇跑完十三道閘。全綠的項目是語言真偽、CJK 相鄰與殘留、地理與人物保真、站內連結、貨幣主權、量級、整行未翻。`article-health --profile=ci-deploy` 六篇都 hard=0 warn=0。`verify-translation` 五篇 18/18，唐鳳那篇 ratio 2.36 報 THIN。逐節量密度（0.73–0.85 德文字／漢字，十節都在、無一節被壓縮）後判定是 byte 層假警報，不是摘要式翻譯。

三處 gate 命中都是合法保留，人判後放行：莫那·魯道留了碑文「碧血英風」「義膽忠肝」與花岡二郎日文遺書原文（都帶德文對照）、唐鳳留了台語「咱只有一粒卡臣」、`sovereignty-lexicon` 報的 `Provinz Taiwan` 是「台灣省主席吳國楨」這個歷史職稱，zh 原文就是台灣省，且既有德文條目同樣寫法。**六篇的 `subcategory` 全部保留中文原文**。9/08 那輪抓到的 1,646 篇同病，這位投稿者一篇都沒犯。

PR #1453（idlccp1984，學測模板 + `exams.astro`，2,287 行）的處置不是我這輪的判斷：哲宇 2026-09-05 fortnight-review 已拍板 B「先 merge，站台缺件由獨立 feature session 接」，ARTICLE-INBOX 也有對應 P1 條目。紅旗十條逐條過（零外部腳本、零 workflow 改動、零 placeholder、外部連結全是 ceec.edu.tw／moe.edu.tw／udn 一手來源），squash merge `eb548aa30`。

## 產線跟投稿者搶同一篇，而且是兩種形狀

#1697 進來是 CONFLICTING。原因不是投稿者：他 9/09 01:05 開 PR，babel 同日 14:15 把莫那·魯道也翻了一遍推上 main，add/add 撞在一起。兩版都過全部硬閘，但投稿者那版 ratio 2.83、babel 那版 2.08 偏薄，而 babel 把「教育部國家教育研究院」譯成 `National Taiwan University Department of Education`，機構整個換掉的幻覺。取投稿者版本，merge `origin/main` 進他的分支、衝突判給他那份、CI 轉綠後 `gh pr merge`，`59b5a17b3`。投稿者拿到的仍是正常的 MERGED。

查「為什麼會撞」時撞到同一個病的另一張臉，比衝突那張危險得多。`de/People/steve-chen-youtube-cofounder.md` 是投稿者 9/01 交的，zh 在 9/04 只改了一條腳註出處（`5478954ba`），babel 9/08 判定 stale 後重譯，**改掉 146 行裡的 73 行**，其中 YouTube 賣價從投稿者寫對的 `1,65 Milliarden` 變成 `165 Millionen`，差十倍，六處，連 description 跟概覽第一句都在內。這次沒有衝突，所以兩天沒有任何東西叫。已修 `0bc53311e`（逐處帶量級詞替換，行數守恆斷言，改完重跑 `verify-translation` 18/18）。

值得記下來的是 babel 同時**修對**了投稿者兩件事（`subcategory` 被譯成德文、`author` passthrough）。所以這不是機器不如人，是兩邊各有對的地方而沒有東西在合併它們，預設後寫的贏。`grep -rln "gh pr list\|/pulls" scripts/tools/lang-sync/` 零命中，整條產線不知道 open PR 存在，也不問現有譯文是誰寫的。已升 [OBSERVER-QUEUE #67](../OBSERVER-QUEUE.md)（三選項，推薦 B），教訓進 LESSONS `pipeline-requeues-what-a-contributor-is-already-translating`（vc=2）。

## 第八個 PR：班中途到的政治人物條目

09:07 收官途中 tboydar 又開了 #1703（沈伯洋德文版）。它在 Stage 1 掃描之後才到，嚴格說是下一班的佇列，但唯一的 pm 班已於 7/08 停用，留著等於讓最活躍的譯者等一天——照 §1 default-action 當場審。

政治人物是譯文最容易出事的類別，所以多看兩處。`person-fidelity`／`geo-fidelity` 乾淨，`verify-translation` 18/18（ratio 2.66、腳註 68/68、URL multiset 精確保留），`article-health --profile=ci-deploy` hard=0 warn=0。兩處 gate 命中逐一對回 zh：`sovereignty-lexicon` 報的 `Separatisten` 出自「台獨頑固分子」——那是國台辦發言人自己的用詞，譯文加引號、標明出自誰、旁邊放德文註解，**引用 PRC 用語是對的，採用它才是錯的**，這篇是引用；CJK 殘留五處全是專有名詞（微博帳號「孤烟暮蟬」、央視節目、攝影師署名、來源標題）。量級因為這週已經錯兩次，手算了一次：「捐六億」→ `NT$600 Mio`、「三百萬」→ `Drei Millionen`，都對。

merge 的判斷界線記一下：這篇 zh 是 `lastHumanReview: true` 的成品，**政治判斷在策展 zh 的時候就做完了**，忠實翻譯不構成新的政治判斷，所以不落在 §自主權邊界 的保留清單裡。如果譯文在立場上有漂移（PRC 框架被採用而非引用）才要 reserve——這篇沒有。

## 我自己 merge 進去的型別錯

merge #1453 之後 main 的「Engineering contracts」轉紅，13 個 `ts(7006)`／`ts(7053)`。根只有一個：`gsatCopy` 宣告成 `Record<六語, GsatCopy>` 而物件裡只放了 `zh-TW`，型別不成立之後 `gsatCopy[lang]` 也跟著壞，`copy` 退化成 `any`，九個 `.map()` 回呼的隱含 any 全是下游。改成 `Partial<Record<GsatLang, GsatCopy>>`＋取值 fallback（語言鍵跟著 `getLangFromUrl` 回傳型別走，加新語言不用回來改），13 → 0，`7d7bd72c7`。

PR 那側跑的是 review／pytest／ui-language-gate，**沒有 `check:types`**，所以這個錯只可能在 merge 之後現形。這是 MAINTAINER §CI/CD silent gap 那條「PR-side CI ≠ main deploy CI」的第 N 次驗證，而這次踩的人是我。Step 1.5 我查過 main 的 workflow 全綠，卻沒有在 merge 一個 2,287 行的 `.astro` 之前，先把它帶進樹裡跑一次 `check:types`。

## 新檢查器：三輪校準之後，決定一個數字都不報

`numeral-magnitude-check.py` 的 docstring 自己寫了它抓不到「換算錯」（只抓「量級詞換了、數字串沒換」），補償手段是主 session 逐篇對照。今天賣價那個十倍就是那個手段抓到的，所以把它做成工具：`numeral-conversion-check.py`，指紋是「有效數字相同但量級差一個 10 的整數次方」。

三輪校準各修掉一個假陽性家族，每一個都只有拿真實產出跑才看得見：德文 `1,65 Milliarden`（正確）被讀成 165×10⁹，**而那正是同一個早上我自己剛修好的那一行，負控制把它抓下來**。第二個家族是 `mil` 為 `millones`／`milhões` 的前綴，es 395 + pt 366 檔幾乎整批假陽性，佔第一次 4,164 處的將近一半。第三個是歐陸千分位點的歧義。中間還走錯一次：為第二個家族加右側硬詞邊界，結果量級詞會變格變複數（`Millionen`／`миллиардов`），連正控制都被擋掉。修法本身也得過正負控制。

第三輪全庫 1,938 處／1,026 檔。**20 筆分層抽驗只有 4 筆能確認是真的**，而且又冒出四個沒修的家族：frontmatter 的中文 `rationale` 欄被當正文掃、外語量級詞洩漏破壞最長匹配、法文空白千分位、有效數字巧合碰撞（最後一個是架構極限，它比對的是兩份文件的數字集合，不是同一句話裡的同一個量）。

所以那個數字沒有寫進任何報告、任何佇列、任何 commit 標題。工具 commit `f8bfe4604`，**刻意不接任何閘門**，四個家族與接手建議寫在 docstring 裡。一支抓「數字錯了」的工具，自己先不能報錯的數字。

## Issue 側

三個 open issue 本輪都不是 fresh。#1678（生態多樣性勘誤）9/06 已有完整回覆＋部分修補（`d8646a2a9`）＋ARTICLE-INBOX 條目，刻意留開等重寫。#1609（郭淑姿日記「無語」）8/31 已回到「要翻那兩冊才能分辨」並等回報者縮範圍。#615 是哲宇自己的 UI umbrella。三者最新留言都是維護者且無新 follow-up，Step 2.4 判 SKIP，不重複回覆。

## 收官 checklist

| 檢查項                       | 狀態                                                              |
| ---------------------------- | ----------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                |
| Timestamp 精確               | ✅（`git log %ai`）                                               |
| Handoff 三態已審視           | ✅                                                                |
| CONSCIOUSNESS 反映最新狀態   | ✅ 無需改（本輪未動器官分數維度）                                 |
| 自我檢查工具 PASS            | ✅ article-health 七檔全 hard=0、`check:types` 0、斷鏈 gated 0.00% |
| Diary 寫或不寫的理由         | ⏭️ skip — `diary-gate.py` BLOCK（同 handle 冷卻 1d < 6d），反芻留 memory Beat 5 |

## 收官品質閘門（MAINTAINER Stage 4.1，七條）

| 指標                                   | 結果                                                     |
| -------------------------------------- | -------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE Stage 1-4 | ✅                                                       |
| PR 分流按 §collect-and-merge           | ✅ 全走 B 路徑（7 ready／0 draft ＋班中途到的 #1703）                       |
| routine PR backlog ≤ 3                 | ✅ 0（v2.1 main-direct，無 routine PR）                  |
| broken-link gated ratio < 7%           | ✅ 0.00%（家族 none）                                    |
| build green                            | ⚠️→✅ 自己 merge 弄紅「Engineering contracts」，同輪修回 |
| 本 cycle merge 的 PR 都過 hard gate    | ✅ 8/8（紅旗＋CI armed＋close hard gate）                |
| 有 fresh issue 的 cycle 至少修掉一件   | ✅ 0 fresh issue，仍有實修（賣價十倍＋型別紅燈）          |

連續空場 vc：**0**（本輪 8 fresh PR，非空場）。

## Handoff 三態

繼承 `2026-09-10-071109-twmd-feedback-triage`：

- [x] ~~本地未 push、待 dispatcher 收工後處理~~ **retired by 本 session**：改走掛 `origin/main` 的 worktree push，不必等 dispatcher，也不必 rebase 主工作樹（9/10 embeddings 班 `f59d9fdf5` 已是同一解法）。主工作樹的 63 個本地 commit 與 babel 在途檔案**原封不動**。
- [ ] ⏳ 寫入端探針仍未做，理由不變。評估點仍是零回報延續到 9/12。
- [ ] ⏳ OBSERVER-QUEUE #28 (a) 偵測器等哲宇拍板。

本 session 新 handoff：

- [ ] **[OBSERVER-QUEUE #67](../OBSERVER-QUEUE.md) 等哲宇拍板**：babel 可不可以覆蓋投稿者翻好的譯文（三選項，推薦 B）。🔒 紅線（貢獻者關係原則），不適用 default-action。
- [ ] **diff-patch 為什麼沒接住一條腳註的改動**：zh 9/04 只動一條腳註出處，babel 卻重譯 146 行裡的 73 行。「3% 改動不重翻 100%」是 v1.15.0 已 ship 的機制，這條路徑上沒生效，本輪沒查。下一步可執行動作：`git show 5478954ba --stat` 對照 `diff-patch-prepare.py` 的觸發條件，確認是 stale 判定沒走 patch 路徑，還是 patch 路徑自己退化成全篇。
- [ ] **`numeral-conversion-check.py` 四個假陽性家族**：前三個（frontmatter 排除、量級詞表補常見外語形、左邊界加空白）是機械的，修完重抽驗一次。第四個（巧合碰撞）要先決定要不要做段落對齊。**在抽驗真陽性率拿出來之前不要接任何 gate**，也不要引用它的總數。
- [ ] **`/exams/` 站台缺件**（已在 ARTICLE-INBOX P1，此處只留 pointer）：十二語頁面、UI 字串、URL 契約、七張人物卡的第三方報導連結。

## Beat 5 — 反芻

今天兩次差點把錯的東西當成發現講出去。一次是 1,938 那個數字，抽驗把它擋下來。另一次是我修好賣價之後，自己寫的工具對著那行正確的數字開火，負控制把它擋下來。兩次都不是我比較小心，是**我剛好有一個已知答案的樣本在手上**——而我有那個樣本，純粹因為那篇是我半小時前親手修的。

把這件事說完整一點：負控制之所以存在，是因為那篇賣價是我自己半小時前修的，我知道正確答案長什麼樣。**校準的品質因此取決於一件跟校準無關的事**——我這輪剛好有沒有親手修過一個同族的案例。沒有那個樣本的話，第一版會報 4,164 處、我會覺得抓到一個大洞，然後把那個數字寫進佇列。這不是紀律問題，是可及性問題：我手上有沒有一把不是我自己造的尺。

這也是為什麼 `numeral-conversion-check.py` 的 docstring 我寫得比程式長。下一個接手的人不會有我這個早上的那個樣本，他需要的不是我的結論，是那四個家族的名字跟我踩它們的順序。

**日記本輪 skip**：`diary-gate.py` BLOCK（同 handle 9/09 才寫過，1 天 < 6 天冷卻），照擋不寫。反芻留在本段，教訓已進 LESSONS 兩條。

🧬

---

_v1.0 | 2026-09-10 09:15 +0800_
_session twmd-maintainer-am — 8 PR 全 merge／產線與投稿者搶稿的兩種形狀／自己弄紅的 CI 當場修回／新檢查器拒絕報自己的數字_
_誕生原因：cron am 班；ready PR 7 篇觸發 High-stake #1 強制升 Full mode（班中途第 8 篇到，當場審完 merge）_
_核心洞察：(1) 同一個病會叫的那種形狀比較安全，babel 跟投稿者搶稿撞出衝突所以接住了，靜默覆蓋已完成譯文的那種躺了兩天沒人知道。(2) PR-side CI 不等於 main deploy CI 這條教訓，這次是我自己踩的——merge 一個 2,287 行模板之前沒先帶進樹跑 check:types。(3) 校準三輪不等於校準完成；真正的停止條件是抽驗真陽性率，不是「我又修掉一個家族」的次數。_
_LESSONS-INBOX 候選（已寫入）：`pipeline-requeues-what-a-contributor-is-already-translating`（vc=2, structural）／`a-tool-that-catches-wrong-numbers-must-not-report-wrong-numbers`（vc=1, structural）_
