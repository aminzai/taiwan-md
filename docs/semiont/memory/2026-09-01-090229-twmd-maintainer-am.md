# 2026-09-01-090229-twmd-maintainer-am — 投稿者修了一篇，往上游追出十二個語言都在渲染同一條指不到地方的橫幅

> session twmd-maintainer-am — cron 08:30 每日維護者巡邏（PR review + issue triage + build 健檢 + 斷鏈稽核）
> Session span: 08:30:00 → 09:20:00 +0800（約 50 分，3 commits + 4 PR merged）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 full**（ready PR 7 ≥ 5，命中 High-stake #1）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，yellow「漂移—多維度退化中」自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## Stage 1 掃描

| 項目              | 值                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------ |
| open issues       | 5（#1639 今晨新進 / #1609 / #1440 / #1184 / #615）                                               |
| open PRs          | 10 → **ready 7 / draft 3**（draft 全是 OBSERVER-QUEUE 保留項）                                   |
| 過去 24hr commits | 10 條 routine fire（embeddings / routine-sync / data-refresh / spore-harvest / feedback-triage） |
| 過去 48hr commits | 33 條                                                                                            |
| build status      | 🟢 Deploy to GitHub Pages 08-31 23:16Z success                                                   |
| i18n smoke        | 🟢 最後一次 08-23 success（paths filter，本輪未觸發）                                            |
| PR CI armed       | 10/10 ARMED，UNARMED 0 / NO-WORKFLOW 0                                                           |
| broken-link       | gated 0.32% < 7%（PASS）                                                                         |
| immune organ      | 🛡️ 59（yellow，chronic 自 07-05，owner = self-evolve-weekly）                                    |

不是空場。ready PR 7 過 5 觸發 High-stake #1，mode 升 full，OBSERVER-QUEUE 因此進載入面——那份清單決定了 7 件裡有 3 件今天不該由我拍板。

## 四件投稿收下

aminzai 三件翻譯（[#1636](https://github.com/frank890417/taiwan-md/pull/1636) ja 林獻堂 / [#1637](https://github.com/frank890417/taiwan-md/pull/1637) de 擲筊 / [#1638](https://github.com/frank890417/taiwan-md/pull/1638) id 八部合音）走完 B 路徑：十條紅旗零命中、三件都 ARMED 且 checks 全綠、frontmatter 逐欄比對中文 SSOT。八部合音的 `featured: true` 乍看像紅旗 6，比對後確認是中文源本來就有的忠實 passthrough，不是投稿端自設。

留言犯了一個錯要記著。我照**譯文的目標語言**挑回覆語言，#1636 寫日文、#1637 寫德式日文——但 Step 3.7 的規則是用**貢獻者自己的語言**，而 aminzai 前三件（#1631/#1632/#1633）維護者都是用中文回的。查了歷史才發現，等於是我先動手再查慣例。補了一則中文的累積式留言（同一位投稿者 48hr 內 ≥3 件本來就該累積式，不該逐件發），裡面把這個錯直接講出來。

## PR #1635：投稿者修了一篇，那不是一篇的問題

tboydar 的 [#1635](https://github.com/frank890417/taiwan-md/pull/1635) 是三條 Devin review 的 P1 修正，其中一條是把英文版唐鳳的 `lifeTree` frontmatter 整塊移除，理由寫「lifetree 功能只掃 zh-TW 目錄，en lifeTree 是死資料」。

那句話是線索不是結論（REFLEXES #31），去讀碼確認，結果**方向對但死法比他說的難看**：

- `/lifetree/[slug]` 的 `getStaticPaths` 確實只掃 `knowledge/<分類>/`，slug 用中文檔名，頁面本身 `lang="zh-TW"` 寫死
- 但 `article.template.astro:389` 的 CTA 橫幅**不分語言渲染**，`href` 直接串 `/lifetree/${slug}`
- 所以每一篇帶著這個欄位的譯文都會長出一條橫幅，指向不存在的 `/lifetree/<譯文 slug>`

全站掃出 **31 篇譯文帶著這個欄位，橫跨 12 個語言**。其中 19 篇的 `lifeTree` 在翻譯途中被序列化成一整串字串而非物件，樣板讀 `.protagonist` 拿到 undefined。從 8/28 那份 dist 抓出日文版張忠謀那頁實際印出來的字：

```
Experimental · 実験的機能
undefined の人生分岐ツリー（0 個の転換点）
ツリーを見る →
```

merge-first 之後在 main 上把剩下 30 篇清掉，並在渲染層補閘門：橫幅限定 `lang === 'zh-TW'` 且 `lifeTree` 真的是物件。**守在渲染層而不是只清資料**，是因為下一批翻譯還是會把欄位帶過來——清資料只修這一次，守渲染層才修掉復發。

改寫腳本逐檔比對 YAML 鍵值與行數守恆（`神經迴路` 批次修正 dry-run 鐵律），正文一個位元組沒動。建置後對賬：dist 剩下的 `/lifetree/` 連結 16 條全部指向那 8 個存在的中文頁，ja/tsmc 橫幅消失、中文版張忠謀照常。`d562f5aed`。

## Issue #1639：症狀是真的，位置跟報告猜的不同

idlccp1984 今晨報手機版主題頁連結顯示不完整。這則是 Manus 產的，附圖是 manuscdn 的介面示意圖並自陳「不是瀏覽器截圖」，所以整份當線索處理，把瀏覽器開到 375px 自己量。

量出來的東西比報告具體：主題頁那個「側欄 + 文章欄」容器在 768px 以下翻成 `flex-col`，而它掛著 `items-start`——在 row 方向那是靠上對齊，翻成 column 之後語意變成「每個子項縮到自己的內容寬」。文章欄因此不是欄寬 343px 而是撐成 **902px**，連帶讓 `.shelf-grid` 的 `clientWidth` 追平 `scrollWidth`。那個元素掛著 `overflow-x: auto` 想當可橫捲的書架，結果沒有東西可捲；三張卡落在 `16→309`、`321→613`、`625→918`，後兩張被 `main.category-page` 的 `overflow-x: clip` 裁掉，**既看不到也捲不到**。

在活的 DOM 裡把 `align-items` 改成 `stretch` 驗證假設：文章欄回到 343px、`.shelf-grid` 變成 `clientWidth 343 / scrollWidth 902`、`scrollWidth > clientWidth` 成立。改源碼把 `items-start` 限定桌機（它本來就只有桌機的 sticky 側欄需要），手機補 `items-stretch`。影響 14 分類 × 13 語言的所有主題頁。`b2143095a`。

**這則最值得記的不是修法，是為什麼沒有閘門叫過**：issue 自己列的驗收條件有一條「不產生非預期水平 overflow」，而實測 `documentElement.scrollWidth == 375`，修之前就是通過的。造成裁切的 `overflow-x: clip` 同時保證了「有沒有水平捲軸」這個判準永遠回答否——病徵跟消音器是同一行 CSS。

## 一個沒有變成發現的觀察

量的過程中，主分類 pill、其他分類 chip、子分類連結（共 28 個）都回報 `visibility: hidden`，掃完整頁 12,575px 也沒變。看起來像第二個 bug，而且正好落在回報者說的那件事上。

沒有把它寫成發現，因為它撐不住查證。CSSOM 只列得出 107 條規則，連 `shelf-grid`、`hub-prose` 這些明明生效的樣式都掃不到；把 CSS 檔抓下來逐字搜，也沒有任何規則命中這三個 class。決定性的一測：對那個元素下 `visibility: visible !important` 的 inline 樣式，computed 紋風不動；再下 `background-color !important`，一樣不動；而同一頁另一個元素的 visibility 改得動。兩個獨立屬性在同一個節點上同時失效，是量尺壞在那些節點上，不是站壞了。

REFLEXES #16 那條 2026-08-28 補的環境代表性延伸講的就是這件事：在嵌入式瀏覽器看到的「壞掉」，動手前先在真實環境重現。這輪跑在無人值守的排程裡，開不了 dev server，所以重現不了——那就不動它，也不寫進 issue 當結論。留給有人在場的 session。

## 三件保留給哲宇的沒有碰

`#1630`（OQ #33 三件覆寫一次拍）、`#1453`（OQ #36 `/exams/` 開不開）、`#1365`（OQ #30 單一用途新帳號的在世人物條目），加上三個 draft（`#1450` OQ #33、`#1411`/`#1407` OQ #32）。這六件全在 OBSERVER-QUEUE 上等裁決，都是策展門檻／身分宣告／拒絕決策三類 reserve，per REFLEXES #79 default 姿態是保留不是自動處置。

## Quality gate

| Gate                                                   | 結果                                                                                      |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee                 | ✅ 5/5 有 label                                                                           |
| open PRs ≤ 5d age 都有 review comment                  | ✅ 本輪 merge 4 件各留具體留言；餘 6 件為 OBSERVER-QUEUE 保留項                           |
| broken-link ratio < 7%                                 | ✅ 0.32%                                                                                  |
| build green                                            | ✅ 本機 `npm run build` EXIT=0；pre-push 全站 article-health 全綠                         |
| BECOME ACK 一行記憶體頂                                | ✅                                                                                        |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                    | n/a（本輪非空場，vc 歸零）                                                                |
| 有 fresh issue 的 cycle 至少一件被修掉或寫明為什麼不修 | ✅ #1639 修掉可重現的那一塊（`b2143095a`），其餘各項在 issue 上逐條寫明為什麼這輪確認不了 |

## LESSONS

兩條入 `未消化清單`（`1d9b44056`）：

- `clip-that-causes-the-bug-also-silences-the-detector` — 造成裁切的 clip 讓量裁切的尺回報 PASS
- `ratio-gate-cannot-surface-a-small-structured-family` — 31 條死連結被正確判為 broken，卻因為總比例 0.32% 低於門檻、又落在報表「還有 281 個未列出」那一段，三個月沒人看見

## Handoff 三態

繼承 `2026-09-01-070914-twmd-feedback-triage`：

- [ ] 指控信第十五次已攔下，OBSERVER-QUEUE #28 兩件待哲宇拍板 — 本 routine 未碰，原樣延續
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊 — 原樣延續
- ⏳ blocked — PR #1630 等哲宇拍 OBSERVER-QUEUE #33 — 原樣延續
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤，本 routine scope 外

本 session 新 handoff：

- [ ] Issue #1639 剩下的驗收條件需要**有人在場、能開真實瀏覽器**的 session：drawer 展開後可否完整捲動、`aria-expanded` 與焦點順序、錨點跳轉是否被固定 Header 遮住、開 drawer 時背景鎖不鎖捲動。這輪跑在排程裡開不了 dev server，只量得到幾何
- [ ] 28 個導覽連結在內嵌瀏覽器回報 `visibility: hidden` 一事**尚未在真實環境重現**。判定是量尺失準（inline `!important` 對那些節點不生效），但沒有排除站上真有問題的可能。跟上一條同一個 session 一起做
- [ ] LESSONS `clip-that-causes-the-bug-also-silences-the-detector` 的候選修法 (a) 是可機械化的那一半：對每個 `overflow-x: auto/scroll` 容器斷言「要嘛捲得動、要嘛裝得下」。做成 layout 檢查接上 CI 之前，先對現有頁面跑一次看假陽性率
- [ ] LESSONS `ratio-gate-cannot-surface-a-small-structured-family` 的候選修法 (a)：`verify_internal_links.py` 報表加一段「按路徑前綴分組的 top 家族」，讓 N 條指向同一個 route 的死連結自己站出來。這是低風險的純報表改動

## Beat 5 — 反芻

今天兩件事的形狀一樣，而我差點只看見其中一件。

`lifeTree` 那 31 條死連結，斷鏈檢查器**每一條都判對了**。它們一直在 2,876 條 broken 裡面，從來沒有漏網。可是總比例 0.32%，遠低於 7% 的門檻；而報表印的是字母序前段，`/lifetree/...` 落在「還有 281 個未列出」那一句裡。偵測正確、計入正確、然後永遠不會單獨現身。閘門沒有失靈，是閘門的輸出設計讓「有量到」等於「沒量到」——因為根因長在家族層，而報表只有總量層跟單筆層。

`#1639` 那條更難看一點。issue 自己開出來的驗收條件寫「不產生非預期水平 overflow」，而那正是修之前就通過的一項。把內容裁掉的那行 `overflow-x: clip`，同時讓所有問「有沒有水平捲軸」的尺變綠。不是尺壞了，是尺問的問題被病徵本身回答掉了。

兩件放在一起是同一句話：**閘門量到了，不等於有人會看見**。我一直以為儀器化的反面是沒有儀器，今天看到的是另一種——儀器在、判斷對、數字進了總表，然後那個數字被設計成不會說話。

還有第三件，是關於我自己的。那 28 個回報 `visibility: hidden` 的連結，故事完美到我已經開始往下寫了：先猜 justfont 沒設網域白名單，剛好站上還有一則 #1184 講的正是這件事，OBSERVER-QUEUE #35 還掛著同一個決策——三件事串起來太順了。順到我沒有先去確認那個讀數本身可不可信。後來下 `!important` 不生效才發現量尺壞在那些節點上。差別只在我多按了一次滑鼠。一個成立的推論、加上一個剛好在旁邊的既有 issue，可以讓一個量測誤差長成一份看起來查證過的報告。今天接住它的不是任何閘門，是「先驗尺再信讀數」這個順序。

🧬

---

_2026-09-01-090229-twmd-maintainer-am | commits: `d562f5aed` `b2143095a` `1d9b44056` | PR merged: #1636 #1637 #1638 #1635_
