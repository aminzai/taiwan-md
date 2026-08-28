# 2026-08-28-092206-twmd-maintainer-am — 兩則讀者回報追上游長出一道 CI 閘門；三則詞庫回報挖出 594 條會改壞正確台灣話的轉換規則

> session twmd-maintainer-am — cron routine（08:30 am cycle）
> Session span: 08:33:00 → 09:22:06 +0800（約 50 分鐘，6 merge commit + 1 fix commit）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→**強制升 Full**（ready PR 7 ≥ 5，High-stake #1） / 8 organ 最低=🛡️免疫 59（即時 `consciousness-snapshot.sh`，非記憶值；🫀90 🧬95 🦴90 🫁85 🧫100 👁️90 🌐83） / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 08:30 maintainer cycle。進場時 7 個 ready PR（觸發 High-stake #1 強制升 Full mode）、9 個 open issue，其中六則是今晨 07:10 feedback-triage 剛轉進來的讀者回報。

## Stage 1 掃描

| 項目              | 數值                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| open PR           | 10（ready 7 / draft 3），全部 ARMED，無 UNARMED / NO-WORKFLOW                                                                |
| open issue        | 9（6 則今晨新進）                                                                                                            |
| 過去 24hr commit  | 6 條 routine fire（embeddings / routine-sync / data-refresh / spore-harvest / feedback-triage，另有 8/27 maintainer-manual） |
| 過去 48hr commit  | 80+（含 8/27 manual cycle 的 29 個 PR merge）                                                                                |
| build             | 綠（CI Deploy 8/27 23:16 success）                                                                                           |
| broken-link ratio | 0.27% < 7% 門檻                                                                                                              |
| 免疫器官          | 59（yellow，自 2026-07-05 掛著，權責 self-evolve-weekly）                                                                    |

## 五個 PR：merge 前差點誤判一個孤兒

七個 ready PR 裡兩個在 OBSERVER-QUEUE 保留（#1453 學測模板屬 #36、#1365 KENJI 屬 #30），剩五個全部 CLEAN + CI 三綠。aminzai 三篇新語言翻譯（ar 白先勇 / hi 滷肉飯 / id 日治時期）、tboydar 兩篇（en 黃土水 + 一個跨五語六檔的 frontmatter heal）。

值得記的是 #1605 這個，它的 diff 顯示在 `knowledge/vi/Society/pts-public-television-service.md` 刪掉五行，其中包含 `translatedFrom` — 那是語言器官的孤兒防護 file-level SSOT，照理不該被刪。照 MAINTAINER §診斷紀律把 PR 檔帶進 main 樹量（不 checkout PR 分支），結果是六個檔每一行刪除都對應一個真的重複鍵，`translatedFrom` 在該檔本來就有兩份、刪完剩一份。**看起來像破壞的其實是修復**，而分辨這件事只花了一次 `git show refs/twmd/pr1605:` 加一段 awk。五個 PR 走 §1b P0 全部 `gh pr merge --merge`，回覆按 Step 3.7 burst 紀律整批各一則（aminzai 三篇一則、tboydar 兩篇一則）。

## 兩則讀者回報追上游：篩選列吃掉三分之二畫面

羅心怡 8/23 說「關鍵字頁面無法收合，找不到收合的按鈕，擋住觀看詞彙的畫面」（[#1612](https://github.com/frank890417/taiwan-md/issues/1612)），Casai かさい 8/26 說「分類 tag 沒有摺疊，在手機上閱覽直接蓋住 2/3 的頁面」（[#1614](https://github.com/frank890417/taiwan-md/issues/1614)）。兩則指向同一條 sticky 篩選列。

量出來的根因是：那一列有 6 個分歧類型加 46 個子分類共 53 顆按鈕，全部攤開，整條 sticky。在 375×812 實測佔 **65% 的視野**，跟讀者說的「2/3」幾乎是同一個數字。至於「找不到收合的按鈕」，那條列從設計時就沒有收合控制。

修法是給它收合控制，預設值走 media query 不走 JS（手機收起、桌機展開，關掉 JavaScript 也是這行為），收起時按鈕寫出目前篩的是什麼，手機上選完分類自動收起。實測 65% → 8%，桌機 34%（原樣）→ 可收到 10%。

補閘門的部分是這次的重點：新增 `scripts/tools/check-sticky-viewport.mjs` 加 `.github/workflows/sticky-viewport-gate.yml`，用 375×812 真的渲染，量每個 sticky/fixed 元素**擋住**多少視野，超過 35% 擋下。門檻拿站上 10 個代表性頁面實測校準（健康頁面 7–13%，出事那頁 65%，中間空了五十個百分點），不是憑感覺設的。負向測試也做了：把 dist 那頁改回展開狀態，閘門報 41% ❌ 且 exit 1，還原後 ✅ exit 0。

造這支的過程自己踩了兩個坑，都寫進檔頭當警語。第一版量「元素多高」而不是「擋住多少」，把 `/map` 那個整個收在畫面外的抽屜（高 487px、可見 0px）報成違規 — 在閘門的位置量錯東西就是假陽性的起點。第二版會間歇性回報「這頁沒有 sticky 元素」，同一頁兩次跑一次 13% 一次 0 個，而空清單被印成 ✅ 等於閘門在說謊。現在等版面安定再量，量不到用 ⚠️ 自己的符號報並 exit 1。

## 三則詞庫回報：一則變成 594 條

讀者 A 回報「試試看」把社群範例裡的「粉絲」轉成「冬粉」（[#1613](https://github.com/frank890417/taiwan-md/issues/1613)）。查下去 `粉絲.yaml` 寫「中國：粉絲 → 台灣：冬粉」，那只在食物義成立，藝人的粉絲台灣本來就這樣講。照 8/22「挺」那條立下的作法加 `auto_convert: false`。

轉換器早就有這個開關，所以缺的是**系統性找出哪些詞條該掛旗子的東西**，在此之前每一個都要等讀者先撞到。所以造了 `terminology-autoconvert-sweep.py`：拿轉換器真正在用的規則去掃我們自己寫的 1,132 篇中文 SSOT，會改到自家正文的規則就是候選誤轉。**掃出 594 條**，讀者撞到的那條排第 45 名，前幾名是市場→行銷 2,719 處、保存→存檔 1,730 處、支持→支援 796 處。

第一版掃描報了一條「N → 已讀」命中 7,661 次。查下去是我自己的尺壞掉：轉換器先檢查 `N/A` 再去括號，我寫成先去括號再切斜線，於是 `N/A（概念差異）` 變成單一個字母 `N`。稽核工具跟被稽核對象用不同的尺，量出來的是尺的差異。改成逐行對齊之後幽靈消失。

順著同一條線還抓到第二個真 bug：目標值的括號註解沒被清掉，所以「網紅」會被換成「網紅（已通用；早期說「部落客」「網路名人」）」，整段說明塞進使用者文字裡。全站 17 條規則是這形狀，其中 5 條根本沒轉換、只塞註解。「偷感」甚至會被換成「無公認對應」五個字。已在 `converter.astro` 清掉目標值註解並跳過清完等於原字的規則，實測讀者那句話現在輸出「粉絲」留著、「網紅」留著、軟件→軟體、視頻→影片、硬核→硬派。

蘇洛的兩則裡，#1611「狀語不一定是副詞」指到 `副詞.yaml` 寫「台灣：副詞／中國：状语」— 副詞是詞類、狀語是句子成分，不同層級不能對照。已改成正確對照並加 `auto_convert: false`。這則最值得記的是另一件事：**我們自己 2026-07-10 的詞庫審查七週前就把這條標成 WRONG，理由跟讀者講的一字不差**，然後它在站上又待了七週。#1609/#1610 是同一則回報五十秒內送兩次，#1610 標重複關閉。#1609 拿郭淑姿日記挑戰「無語」的斷代主張，日記原文我沒查證，所以只在詞條加誠信標註記下爭議、明講 fork_point 是待驗證推測，沒有照未查證的說法改判定 — 那跟當初照一則留言串下結論是同一個毛病的兩面。

## 本 cycle 沒做的與為什麼

`/map` 的側欄一度被閘門報成違規，實測是畫面外的抽屜，假陽性，未動。`無語` 的轉換未關閉（見上）。343 條事實錯誤與 594 條誤轉候選整批動到 >50 檔，命中 §自主權邊界，升 OBSERVER-QUEUE #43 附三個選項與成本，未自主執行。本機 `npm run build` 一開始全紅，是 `marked-cjk-friendly` 在 package.json 但 node_modules 沒裝，`npm install` 補一個套件後轉綠 — 跟本次改動無關，CI 前一晚是綠的。

## 收官 checklist

| 檢查項                       | 狀態                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                            |
| Timestamp 精確               | ✅（`git log %ai`）                                                           |
| Handoff 三態已審視           | ✅                                                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（即時 snapshot，未改檔）                                                   |
| 自我檢查工具 PASS            | ✅ pre-commit / pre-push 全綠（全站 article-health、UI 語言、模板語言三閘門） |

## Quality gate（MAINTAINER Stage 4.1，7 條）

| Gate                                   | 結果                                                  |
| -------------------------------------- | ----------------------------------------------------- |
| open issue 都有 status label / 處置    | ✅ 6 則新回報全處置（5 close + 1 保留待查證）         |
| open PR ≤ 5d age 都有 review comment   | ✅ 5 merge 全回覆，2 保留項在 OBSERVER-QUEUE 已有紀錄 |
| broken-link ratio < 7%                 | ✅ 0.27%                                              |
| build green                            | ✅                                                    |
| BECOME ACK 一行在記憶體頂              | ✅                                                    |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ 不適用（本 cycle 真 backlog，vc 歸零）             |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ 五件修掉並附 commit `8680e1666`                    |

## Handoff 三態

繼承上一 session（`2026-08-28-071008-twmd-feedback-triage`）：

- ⏳ blocked — 營運機 mouhouse 排程器狀態未確認。未碰
- [ ] pending — 五個縣市條目的正確圖片要補回。未碰
- [ ] pending — `.husky/pre-push` 全檔掃 `VAR="$(...)"` 缺 `|| true`。未碰
- [ ] pending — [#1453](https://github.com/frank890417/taiwan-md/pull/1453) 學測專題人物卡第三方報導連結。未碰（屬 OBSERVER-QUEUE #36）
- ⏳ blocked — [#1365](https://github.com/frank890417/taiwan-md/pull/1365) KENJI 知名度門檻等哲宇拍板。未碰（屬 #30）
- ⏳ blocked — OBSERVER-QUEUE #39-#42 四項。未碰
- [ ] pending — 免疫分數 59「漂移」黃燈連續多輪，權責在 self-evolve-weekly。未碰
- [ ] pending — w.is_solis 對 #175 留言的質疑落在 human-only 邊界。未碰
- [ ] pending — sophie990329「字典誰編的」考慮開一篇說明文章。未碰
- [ ] pending — 「特別」這個副詞要排進 terminology 查證候選清單。未碰
- [ ] pending — 空窗期間 #175/#176 留言區的非 pipeline 人工回覆需哲宇確認來源。未碰
- ⏳ blocked — `b78ee4f5` 指控信第十一次攔下。未碰（屬 OBSERVER-QUEUE #28）
- [x] ~~pending — [#1613](https://github.com/frank890417/taiwan-md/issues/1613) 粉絲/冬粉誤轉，建議由 terminology routine 接手~~ — retired by 本 session：不只補了那一詞，追上游造了 sweep 工具並修掉轉換器的註解注入 bug，`8680e1666`
- [x] ~~pending — [#1609](https://github.com/frank890417/taiwan-md/issues/1609)/[#1610](https://github.com/frank890417/taiwan-md/issues/1610) 同一則回報兩次送出，maintainer 收割時擇一 close~~ — retired by 本 session：#1610 標重複關閉

本 session 新 handoff：

- [ ] pending — [#1609](https://github.com/frank890417/taiwan-md/issues/1609) 郭淑姿日記是否含「無語」用法待查證。下一步：`twmd-terminology-trends-monthly` 接手核對原文（收錄書目 / 館藏 / 線上全文擇一），核完回該 issue 告知讀者，並依結果決定 `無語.yaml` 的 fork_point 要不要改判定
- ⏳ blocked — OBSERVER-QUEUE #43「詞庫事實錯誤與策展判斷要不要拆兩條路 + 594 條誤轉規則怎麼收」。解除條件：哲宇在三個選項中拍板（推薦 default (a)），default-action 日期 2026-09-30。工具已就緒（`terminology-autoconvert-sweep.py` 產候選、`reports/terminology-review/2026-07-10/flagged.md` 產錯誤清單）
- [x] ~~pending — `.github/workflows/sticky-viewport-gate.yml` 尚未在 CI 跑過一次~~ — retired by 本 session：收官 push 觸發第一次 run（sha `8680e166`）success，CI 量到的十頁數字跟本機一致（最高 13% < 35%），Playwright 安裝與 http-server 兩步都過
- [ ] pending — 正式站驗證已做（`https://taiwan.md/terminology/` 手機 8%、選完標「篩選 · 醫療」；轉換器輸出「粉絲」與「網紅」留著、軟件→軟體、視頻→影片）。下一步：D+2 回頭看 #1612 / #1614 兩位回報者有沒有後續回應
- [ ] pending — `/map` 的 `.sidebar-panel` 在手機上高 487px、目前收在畫面外。閘門判定為假陽性未動，但那是「抽屜打開之後多高」沒有被任何東西看著。下一步：確認它展開時的行為是否也該受同一條門檻約束

## Beat 5 — 反芻

今天有兩件事長成同一個形狀。閘門造到一半，我發現自己量的是「元素多高」而不是「它擋住多少」。掃描跑第一輪，我發現自己重寫了一個「意思差不多」的清洗函式，於是憑空長出一條要把全站的 N 換成「已讀」的規則。兩次都是我做了一把尺去量別人，而尺本身跟被量的東西不同調。抓到它們的是**具體的數字看起來不對**，我的推理沒幫上忙：487px 的抽屜怎麼會擋住畫面，7,661 次命中怎麼可能沒人發現。數字大到荒謬的時候比較好抓，那些量錯一點點的呢。

另一件事更值得留下來。七週前我們自己的稽核把 `副詞.yaml` 標成 WRONG，理由跟今天讀者講的一字不差，然後它繼續在站上待了七週，直到一個叫蘇洛的人自己撞上去。發現是有發現的，發現之後把它跟 128 條真的需要哲宇判斷的東西打包成一件事送進待決佇列，於是 343 條根本不需要任何人拍板的事實錯誤，跟著排隊排了七週。升級的顆粒度本身變成了修復的阻塞點。這條寫進 LESSONS（`escalation-granularity-blocks-remediation`），我覺得它比今天修掉的任何一個 bug 都重要：我一直以為「發現問題」跟「修好問題」之間的斷點在意願或工時，今天看到的斷點在**打包方式**。

🧬

---

_v1.0 | 2026-08-28 09:22 +0800_
_session twmd-maintainer-am — 5 PR merge / 6 讀者 issue 五件修掉 / 新增一道 CI 閘門與一支詞庫掃描 / 升 OBSERVER-QUEUE #43_
_誕生原因：每日 08:30 maintainer cycle，進場 7 ready PR + 6 則今晨轉入的讀者回報_
_核心洞察：兩則講同一件事的回報量出 65% 的視野遮蔽，補閘門時自己踩了「量替身不量本體」與「空結果印成綠燈」兩個坑；一則詞條回報追上游變成 594 條會改壞正確台灣話的規則；七週前自己標對的錯誤因為跟策展判斷打包在一起而沒被修，最後由讀者從外面告訴我們_
_LESSONS-INBOX 候選：`escalation-granularity-blocks-remediation`（已 append）、`local-deps-drift-makes-local-build-red-while-ci-green`（已 append）_
