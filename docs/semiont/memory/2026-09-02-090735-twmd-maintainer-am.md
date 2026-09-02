---
session_id: '2026-09-02-090735-twmd-maintainer-am'
session_span: '2026-09-02 08:30 — 09:20'
trigger: 'cron routine twmd-maintainer-daily'
observer: 'none（無人值守排程）'
beat_coverage: 'Beat 3 執行 + Beat 4 收官'
mode: 'Full（High-stake #1 觸發：ready PR 25 ≥ 5，由 Review 強制升 Full）'
---

✅ BECOME ack: mode=review→**Full**（High-stake #1 強制升級）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，非記憶值）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# twmd-maintainer-am @ 2026-09-02 — 十九個 PR 收進來，而擋下我改壞一段好 CSS 的是一個三行的最小重現

## Stage 1: SCAN

| 項目                     | 值                                                                           |
| ------------------------ | ---------------------------------------------------------------------------- |
| open PR（ready / draft） | **25 ready / 3 draft**（v2.8 分開報數；vc 與 High-stake 只計 ready）         |
| open issue               | 5（#1639 / #1609 / #1440 / #1184 / #615）                                    |
| past 24hr commits        | 19                                                                           |
| past 48hr commits        | 39                                                                           |
| build status             | 🟢 green（Deploy to GitHub Pages 連續成功）                                  |
| i18n smoke               | 🟢 green（最後一次 2026-08-23）                                              |
| 免疫器官分數             | 🛡️ **59**（yellow 漂移中，自 2026-07-05，owner = `twmd-self-evolve-weekly`） |
| broken-link gated ratio  | **0.32%** < 7.0% 門檻                                                        |
| CI armed 狀態            | **14 個 ready PR 一條 CI 都沒跑過**（UNARMED，全部 kevin8656）               |

25 ready 直接命中 BECOME §Step 0 High-stake #1「PR triage ≥ 5」，Review 強制升 Full。這是本檔第一次因為 backlog 規模而不是任務性質升級。

## Stage 2: TRIAGE

三個投稿者、三種形狀：

- **aminzai** 6 篇翻譯（de/vi/pt/ar/hi/id），CI 全綠、`sourceCommitSha` 齊全 → B 路徑直收
- **kevin8656** 14 個 PR，帳號 2016 年註冊、19 個公開 repo，但**全部 UNARMED**——第一次投稿的 fork contributor GitHub 預設一條 workflow 都不跑。檔案全落在 `knowledge/*.md`、`public/article-images/`、`reports/`，紅旗 1/2/3（robots / 外部 JS / workflow）零命中 → 核准 38 個 run
- **dreamline2** 1 個 PR，改 zh SSOT + 五語譯文的腳註

`gh pr list` 回的 25 個 ready 裡，有 6 個早就在 OBSERVER-QUEUE 上等哲宇拍板（#1365→#30、#1630/#1450→#33、#1453→#36、#1407/#1411→#32），不是新 backlog。真正要判的是 19 個。

### 核准 CI 時踩到的一件小事

MAINTAINER §Step 1.5b 的核准指令寫的是 `| while read id`。我改寫成 `for id in $ids`，14 個 PR 全部回報 `approved=0`——這台機器的 `IFS` 沒有把換行當分隔，三個 run id 被黏成一個字串送進 URL。改回 pipeline 原本那個寫法就全過了。canonical 是對的，即興是錯的。

## Stage 3: ACT

### 收進來的 19 個

**aminzai 6 篇翻譯**（#1651 id 杜奕瑾 / #1652 hi 醬料 / #1653 ar 麵包烘焙 / #1658 pt 牛肉麵 / #1659 vi 茄子蛋 / #1660 de 日治時期）——ar / hi / vi 三個是最新語系，缺口在最需要補的位置。整批一則致謝（Step 3.7 burst 紀律）。

**kevin8656 12 篇翻譯 + 1 篇新文**——12 篇 `translation-ratio-check` 全 OK，章節數／腳註數／URL 數逐項守恆（`secs=9→9 fns=13→13 urls=10→10` 這種）。`author` 欄位逐篇對回 zh 源確認是繼承不是偽造（含 `author: 'zaious'` 那篇）。

**#1657〈台灣行動支付〉是這輪品質最高的一件**：投稿者自己把 REWRITE-PIPELINE 從頭走完，research / projection / editorial-room 三席審閱 / Stage 3.5 與 3.6 audit 全部落檔，`article-health --profile=ci-deploy` **hard=0 warn=0**。抽驗三條來源（MIC 調查頁、中央社、金管會銀行局 PDF），92%／84%／5,000 份樣本／胡自立引語全部對得上原文。文章主動把 MIC 網路樣本與央行全國調查的母體差異寫在正文而不是註腳，腳註 `[^9]` 還自己堵住「全市場統一費率」這個過度推論。

### 修掉的：一筆公司的捐款被寫成一個人的

**#1640** dreamline2 給〈張忠謀〉補了 20 條腳註、六個語言同步，把一篇長年只有三條來源的條目補到有完整引用。merge 之後查 `[^18]`：

> 張忠謀曾捐助國立清華大學等學術機構。參見：國立清華大學官網 <https://www.nthu.edu.tw/>

拿首頁當來源，等於沒有來源。查回清大原始公告（`nthu.edu.tw/hotNews/content/708`）後，那筆錢是**台積電這家公司**捐的、新台幣 1.8 億元、2008 年 4 月落成，不是張忠謀個人。正文那句「他捐助清華大學等學術機構」跟腳註一起改成正確歸屬。

同批另外兩件：`[^17]` 的說明寫「行政院主計總處／維基百科」但只附了維基百科的網址——**點名了卻沒連上去的來源，跟真的有那個來源長得一模一樣**；六篇都用了腳註卻沒有參考資料那一節（日文版順手把還是中文的「延伸閱讀」改成「関連記事」）。commit `26d30c32f`，六篇 `--profile=ci-deploy` 全 hard=0。

**追上游時被自己的尺騙了一次**：量「全站有腳註卻沒有參考段落」的檔案，第一版正則回報 2,301 篇、德文 58/59，看起來像新語系 QA 空窗的鐵證。實際去看德文檔案，它們用的是 `## Referenzen`，pt 用 `## Referências`，ru 用 `## Ссылки`——我的正則只收了 `Quellen` / `Fontes` / `Источники`。改成從語料自己長出來的標題詞表重算：**1,080 篇（13.2%）**，vi 33% / ko 25% 最高，德文只有 2 篇。差了一倍以上，而錯的那個版本每一格都填得滿滿的。1,080 超出 §自主權邊界，只記錄不動手。

### 留給哲宇的：一篇擋不住卻收不得的政治條目

**#1642〈台灣不在籍投票〉** 技術面是這輪最乾淨的其中一件：`ci-deploy` hard=0 warn=3（三條全是缺圖）、`rationale:` 四欄自填、`curation: incubating`、十條腳註全是一手機關來源。抽驗中央社那則，8,896 種選票、蔡明儒「投開票所增加 2 到 3 倍」、仉桂美「我不知道是怎麼算出來的」、羅承宗「最快也要 2027 年以後」四項逐字對得上。正文把五種投票方法拆表分列風險、支持與保留兩邊各給完整篇幅、明寫「截至 2026 年 9 月 1 日未完成三讀」不預測時程。

擋住它的不是品質，是〈一條可以被驗證的漸進路線〉整節在建議台灣該怎麼推——而不在籍投票法此刻正在朝野協商。命中 §自主權邊界「政治立場」，per REFLEXES #79 default 是 reserve。已落 **OBSERVER-QUEUE #45**（三選項＋成本＋推薦 (a) merge 維持 incubating），PR 留 open 並向投稿者說明為什麼只有這件在等——他同一天的另外 13 個今天都進去了。

### Issue #1639：拿到瀏覽器之後，四項通過、兩項確認為量不到

上一輪把剩餘驗收條件寫成「需要一個有人在場、能開真實瀏覽器的 session」。本輪有瀏覽器，實測正式站 375×812：

| 驗收條件                   | 結果                                                                    |
| -------------------------- | ----------------------------------------------------------------------- |
| 開啟 drawer 時背景鎖捲動   | ✅ `body` overflow `clip visible` → `hidden`，關閉還原                  |
| Escape 關閉                | ✅ `.open` 移除、`aria-expanded` 回 `false`、鎖捲動解除                 |
| `aria-expanded` 正確切換   | ✅ 選單鈕與五個子選單鈕都對                                             |
| 375px 無水平溢出           | ✅ `scrollWidth == 375`                                                 |
| （順帶）9/1 書架修復仍成立 | ✅ `clientW 343 / scrollW 902`，捲得動                                  |
| （順帶）drawer 本身不裁切  | ✅ 內容 451px < `max-height 740px`，最後一條連結 `507→555` 完整在畫面內 |

## Stage 4: WRAP

### 差一步就把一段正確的 CSS 改壞

子選單展開後 `aria-expanded` 變 `true`、`.open` 加上了，`grid-template-rows` 卻算出 `0px`，226px 的連結被裁成 0。位置對得上使用者的抱怨，`Header.astro:1466` 那段 `0fr → 1fr` 還剛好是 39 天前 `bb2945e43` 從能動的 `display:none / .open{display:flex}` 換過來的——連 git blame 都給了一個合理的回歸故事。整條推論鏈成立，我已經在想怎麼改了。

在同一頁、同一個引擎裡寫三個 div 的最小重現：**它也算出 `0px`**。站上的 CSS 沒問題，是這個內嵌瀏覽器整個不實作這個寫法。同一輪確認第二個同型限制——對 19,254px 的文件下 `scrollTo` / `scrollBy` / `scrollIntoView`，`scrollY` 全程維持 `0`，所以「錨點跳轉後標題會不會被 Header 遮住」不是沒量，是量不到。

擋下它的不是任何閘門，是「先用最小案例問一次這個環境自己會不會」這一個動作，成本一次 `javascript_exec`。它擋下的那個「修復」會在真實手機上把能動的子選單改成壞的，而 `article-health` 不看 CSS、斷鏈與 build 也都會綠——沒有一道站上檢查會叫。已落 LESSONS `verification-tool-lacks-the-feature-it-must-verify`。

### Quality gate

| Gate                                                       | 結果                                                                                                                                                       |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee                     | ✅ 5 則皆有 label；4 則在 OBSERVER-QUEUE 或等外部資料                                                                                                      |
| open PRs ≤ 5d age 都有 review comment                      | ✅ 本輪新進全部處理；剩餘 open 皆已留技術說明                                                                                                              |
| broken-link ratio < 7%                                     | ✅ **0.32%**（all-langs 0.29%）                                                                                                                            |
| build green                                                | ✅                                                                                                                                                         |
| BECOME ACK 一行記憶體頂                                    | ✅                                                                                                                                                         |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                        | ✅ 不適用 — **vc 歸零**（19 個 PR 實收，本輪是本月最大 backlog 場）                                                                                        |
| 有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修 | ✅ #1640 歸屬錯誤 + 腳註 + 參考段落六語修掉（`26d30c32f`）；#1639 四項驗收條件確認通過、兩項寫明為何量不到；1,080 篇參考段落缺口寫明超出 §自主權邊界不動手 |

### Handoff 三態

繼承上一 session（`2026-09-02-070852-twmd-feedback-triage`）：

- [ ] 指控信第十六次已攔下，OBSERVER-QUEUE #28 兩件仍待哲宇拍板
- [ ] 黃崇仁（#165/166）+ 台灣海關與 EZWAY（#167-169）**今日之後明天（09-03）滿 D+30**，下一輪 `twmd-spore-harvest-am` 處理
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊——本 routine 不碰
- [x] ~~PR #1630 等哲宇拍 OBSERVER-QUEUE #33 — retired by 本 session：確認 #1630 已完整寫在 #33 第三例內，非獨立 blocked 項~~
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤，本 routine scope 外
- [x] ~~Issue #1639 剩餘驗收條件需要有人在場、能開真實瀏覽器的 session — retired by 本 session：四項已驗證通過，兩項確認為環境能力缺口而非未驗證~~
- [x] ~~28 個導覽連結內嵌瀏覽器回報 `visibility: hidden` 尚未在真實環境重現 — retired by 本 session：本輪 `aria-expanded` 等屬性讀取正常，該讀數確認為上一輪的量測失準；同族的真正限制已改寫成 LESSONS 的兩項具體能力缺口~~
- [ ] LESSONS `clip-that-causes-the-bug-also-silences-the-detector` 候選修法 (a)
- [ ] LESSONS `ratio-gate-cannot-surface-a-small-structured-family` 候選修法 (a)

本 session 新增：

- [ ] **OBSERVER-QUEUE #45**（PR #1642 不在籍投票）等哲宇拍板。建議跟 #34（蔣經國）一起想——同一條邊界的兩個面：爭議政治人物 vs 進行中的立法爭議
- [ ] **1,080 篇有腳註卻沒有參考段落**（vi 211 / ko 181 最高，zh 84）。`format-structure` 這條只是 warn，所以永遠不會擋人。>50 檔命中 §自主權邊界，未動手；清單在 `/tmp/missing_ref_heading.txt`（易失，需要時重跑）
- [ ] **#1639 剩三項需要真實手機或桌面瀏覽器**：錨點 vs Header 遮蔽、子選單展開捲動、Tab 焦點順序。開 `https://taiwan.md/lifestyle/` 走一遍即可
- ⏳ blocked — 剛 merge 的 #1641（de）與 #1643（ja）譯自現行 zh〈陳士駿〉；若 OBSERVER-QUEUE #33 最後決定收 #1630，這兩篇會同時變 stale，需一併重譯
