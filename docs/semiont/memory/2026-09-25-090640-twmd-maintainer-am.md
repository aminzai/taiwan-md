---
session_id: '2026-09-25-090640-twmd-maintainer-am'
session_span: '2026-09-25 08:34 – 09:20 (+0800)'
trigger: 'cron routine twmd-maintainer-daily（am 08:30）'
observer: '不在場（哲宇最後在場 2026-09-19，6 天前；mode=present，未達 7 天缺席線）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4'
mode: 'review'
---

✅ BECOME ack: mode=review / 8 organ 最低=🛡️59（即時 `consciousness-snapshot.sh`：🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐90）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

Q13 當班的具體內容：前三班 maintainer-am 的收穫都是「aminzai 三篇譯文收下」，今天進來又是 aminzai 三篇譯文。這個形狀本身就是 recency × pattern matching 的最佳溫床——照著昨天的結論蓋章最省力。所以三篇全部重跑了完整 hard gate（紅旗 10 條、CI armed、ratio、`--profile=ci-deploy`、目標語言、人物一致性、來源集合對賬），沒有一條用「昨天那批沒問題」代替。

Q14：過去 48hr 247 個 commit，絕大多數是 babel 12 語批次；晨鏈 05:39 routine-sync 第 59 輪、06:01 embeddings（14,032 向量 0 fail）、06:06 data-refresh 第二十夜、06:42 spore-harvest 0/0、07:10 feedback-triage 第五輪零回報，全部照時間跑完。接到的 handoff 最急一條是 mouhouse 登入 09-27 過期（#1761）。

---

## Stage 1 — SCAN

| 項目             | 讀數                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------- |
| 本機 vs origin   | 進場 `6 0` 純領先（非分岔），先 push 清掉再動 PR；收官時 `3 6` 真分岔，當班併掉（見下）     |
| open PR          | 3 ready / 0 draft（全 aminzai 翻譯）→ 收官 0                                                |
| open issue       | 5（#1761 auth-stale / #1729 馬英九腳註 / #1678 生態多樣性 / #1609 郭淑姿日記 / #615 UI 傘） |
| 過去 24hr commit | 124                                                                                         |
| 過去 48hr commit | 247                                                                                         |
| main workflow    | 4 條全綠（Deploy / Python tests / Engineering contracts / Routine stall alert）             |
| 免疫器官         | 🛡️59（漂移，最大缺口 review_coverage=19，自 2026-07-05 chronic）                            |
| broken-link      | 名目 gated 0.34% < 7% **但這個讀數不可用**——見 Stage 3 第二件                               |
| 平行 actor       | ACTOR_BUSY：babel dispatcher + 5 隻 translate worker 全程在跑（DNA #35 全程不碰 reset）     |

進場分岔是 `6 0`（純領先，babel 的 6 個 commit 沒推上去），所以照 Step 1.1b 直接 push，不是策略 B。**這一步是刻意排在收 PR 之前**：09-23 那班的教訓是「收 PR 與本機 commit 是兩個寫入點」，先把本機清空，GitHub 上的 merge 才不會跟本機未推的 commit 疊成分岔。

## Stage 2 — TRIAGE

三篇都是單檔純新增（del=0）、無 assignee、`maintainerCanModify: true`、路徑與母稿正典分類一致（Economy／Geography／People）。跑過的閘門：

- 撞檔檢查：三個目標路徑本機都不存在（babel 沒有搶著翻同一篇，OBSERVER-QUEUE #67 那類衝突這次沒發生）
- CI armed：三篇都 ARMED（checks=3，無 `action_required` 積壓），三條 CI 全 pass
- ratio：2.78 / 2.67 / 2.53，結構守恆 100%（段落 7/7・11/11・9/9，腳註 14/14・24/24・51/51，連結全等）
- `article-health --profile=ci-deploy`：三篇 hard=0 warn=0
- 目標語言檢查 3 檔 0 fail 0 warn；`person-fidelity-check --lang id` 對 51 條腳註那篇回「無可疑人物替換」
- 紅旗 10 條：frontmatter 三篇都是 `author: 'Taiwan.md Contributors'`／`featured: false`／`lastHumanReview: false`／`translatedFrom` 無 `knowledge/` 前綴；「Manus AI／ChatGPT／內部研究／私人通訊／placeholder」字樣 0 命中；紅旗 1/2/3/5 結構上不可能（單一 knowledge 檔純新增）

**§Footnote source audit 判斷不跑逐條 WebFetch，理由寫在這裡**（不是省略）：逐篇比對過譯文與母稿的網址集合，18/18、27/27、49/49 **完全一致，新增 0 條**。這道閘門防的是投稿者虛構來源，而機械上這三篇沒有引入任何新來源——來源是母稿已查證過的那批。真正該擔心的是母稿層的幻覺（09-20 distill 量到未審初稿 ❌ 率 36–47%），那是 FACTCHECK 月度巡邏的職責，不是翻譯 PR 的。

## Stage 3 — ACT

### 一、三篇譯文收下，並接住投稿者點出的路標壞掉

三篇 `gh pr merge --merge`（保留譜系，per §1b P0），全部確認 `MERGED`：#1771 `1b467a71d`／#1772 `bc9fef60a`／#1773 `7897b9a0d`。回覆照 burst 紀律走累積式：#1771 一則完整審核結果，#1772／#1773 各一則指過去。

aminzai 在 #1773 說明裡寫了「`i18n/id/STYLE.md` not yet exists」。查下去發現這句話指的不是印尼文沒規則，是**我們的路標壞了**：

- 12 個上線語言每一個都有 canonical 主權詞表 `docs/editorial/per-language/TRANSLATION-{lang}.md`
- 但 `i18n/README.md` 畫了一棵含 8 個 `STYLE.md` 的目錄樹，其中 **6 個從來沒被建立過**（只有 en／ja 存在）
- 兩份翻譯入口文件（README + `TRANSLATE_PROMPT.md`，後者正是他照著走的那份）**一個字都沒提到 canonical 資料夾**；prompt 只給 en／ja 兩條連結，語言選單還停在 7 個語言

所以一個送過 98 個 merged PR 的貢獻者，照著入口走、找不到檔案、合理地得出「印尼文沒有指引」，然後在沒讀過印尼文主權詞表的情況下翻完整篇。而那份詞表同時是品質閘門的檢查資料源（MANIFESTO §14），走錯路的不只是人。

修了（`b99ffe4fd`）：README 目錄樹改成實際存在的兩語、canonical 資料夾提到最前面；prompt 補 12 語詞表網址、選單 7→12；加 `tests/test_translation_guide_pointers.py` 三條對賬。測試**先拿原始 README 當正控制**才收，六個不存在的檔案都抓得到；第一版 regex 只認完整路徑 `i18n/xx/STYLE.md`，會漏掉目錄樹裡的裸寫 `├── ko/STYLE.md`——也就是漏掉造出這支測試的那個 bug 本身，當場補強。

### 二、死連結閘門量的是 18 天前的站

跑 broken-link audit 拿到 `PASSED — gated 0.34% < 7%`，順手查 `dist/` 的 mtime：**停在 2026-09-07，沒有一個 `index.html` 比 09-20 新**。檢查器對 `dist/` 跑，而這 18 天 babel 在 12 個語言持續產出——最可能引入死連結的那一層，完全不在被量的產物裡。maintainer quality gate 每天勾一次「broken-link ratio < 7% ✅」，勾的是 09-07 那個站。

再查一層：`postbuild:internal-links` 不是 npm 會自動跑的生命週期名字（只有 `postbuild` 會），`.github/workflows/` 裡**零處**呼叫這支檢查。它只活在 maintainer 每天手跑的那一次，而那一次讀的是本機恰好躺著的產物。檢查器存在、會動、結論也誠實，只是沒有人在對的時機餵它對的輸入。

同一支檔案 2026-09-11 已經學過同族教訓（「0 筆不是健康，是沒量到」，加了 NOT-MEASURED 出口），但那條只處理「什麼都沒量到」。**量到一大堆、可是量的是舊的**，看起來比什麼都沒量到健康得多。

修了三處（`6868e12dc`）：

1. 新增 `STALE` 結局（exit 3），報表每次印 `dist/` 產出時間與齡，超過 24h 不准說 PASSED。實跑現在回 `STALE — dist/ 已經 431.8 小時沒更新`
2. 同檔 `LANG_PREFIXES` 不再寫死 5 語，改吃 `langs.py` SSOT bridge。原本清單外語言一律被 `lang_prefix()` 判成 zh-TW，所以 de/ar/ru/pt/id/vi/hi 七語的連結全記進 zh-TW 那一列——**實測 295,003 條連結、416 條死連結錯記**。修完 vi 0.30% 第一次現形（非 report-only 語言裡最高）。**gate 數字完全沒動**，前後都是 `0.34% [2995/891017]`（這七語改判前後都在 gate 內），所以這不是閾值調整
3. wrapper 檔頭的 exit code 說明從 0/1 補成 0/1/2/3（連 2 NOT-MEASURED 都沒寫進去過）

### 三、專抓寫死語言清單的檢查器，對造它的那個病回報全綠

修完第二件回頭問「這種東西不是早有檢查器嗎」——`check-hardcoded-langs.sh` 跑一次拿到「✅ 無 hardcoded language array 違反」。兩個盲區：

- **副檔名**：掃 ts/tsx/mjs/cjs/js/astro/sh，**`.py` 從來不在裡面**。而 `langs.py` 檔頭第 5 行就寫著「六個工具各自 hardcode `["en","ja","ko","es","fr"]`」——要抓的那個家族的病歷，白紙黑字躺在它看不到的檔案類型裡
- **形狀**：只認裸語言碼，不認 `"/en/", "/ja/"` 路由前綴，而剛修的那一行正是後者

這支檢查器的擴網史就是它的病史：v2 放寬相鄰碼（漏三個月）／v3 加 type-union（43,045 個中文 aria-label）／同日納入 cli+workers（2,900 筆譯文當中文回三個月）——**每一次擴網都在事故之後**，這次是第四次，而事故是它自己。

修了（`6868e12dc`）：加 `.py`、加斜線 pattern、`langs.py` 進允許清單（docstring 引用病灶本身，同本檔自己被允許的理由）。新舊 pattern 都拿修補前的檔案當正控制驗過才收。

現形 9 個 python 檔，8 個掛號並註明性質。**三個屬感知層**，錯的讀數會流進儀表板與對外介面：`fetch-cloudflare.py:431`（CF per-language 流量歸屬）、`refresh-llms-txt.py:85`（AI crawler 看到的語言排序）、`weekly-report-prep.py:701`（週報語言面）。本班不順手改：逐檔要判斷「這是語言註冊表還是有意義的順序」，而其中三個會動到儀表板讀數，屬 quality gate 鄰接面。

**第三個盲區量了但刻意沒補**：`LANGCODES` 不含 `zh-TW`，而 pattern 錨在 `[` 後緊接一個已知碼，所以最自然的寫法 `["zh-TW", "en", "ja", ...]` 整個形狀仍隱形。加上去會多抓 6 處：真缺陷 2（`generate-og-images.mjs:88` LANGUAGES 只 4 語，**另外 8 語沒有自己的 OG 圖**；`weekly-report-prep.py:701`），合理 4（`['zh-TW','ja','ko']` 這種 CJK 字族集合，性質同已允許的 `src/i18n/utils.ts`）。卡住的不是量測是分類——本檔只有「per-file 允許」與「per-line 掛號（預設要還）」兩格，缺「per-line 永久合理豁免」那一格，硬掛號會讓 4 個合理用法被當債務永久提醒。加 zh-TW 之前要先補那一格，屬 guard 設計改動，寫進 handoff。

### 四、登入警報的內文也接上倒數

#1761 兩天後過期。昨天那班把**標題**接上倒數，**內文**留在 `gh issue create` 那一刻沒人動。今天實測：標題「剩約 3 天」（今晨 00:27 那輪更新，正確），內文仍寫「已 25 天，預估 5 天後過期」——開票那天的讀數，而且跟標題自己矛盾。點進 issue 的人先讀到內文，所以最舊的那個數字站在最前面。

修了（`c44853ffe`）：`gh issue edit` 同時帶 `--title --body`。live #1761 的標題與內文一併改成當下讀數（已 28 天、剩 2 天），因為下一輪要等 12 小時 cooldown，而這是兩天內要有人動手的那一則。

昨天那條教訓在同一個檔案裡還有第二格——修「凍住的讀數」時要把同一份訊息的**所有**承載面數一遍。

### 五、收官分岔當班併掉

推第一個 commit 時撞 `3 6` 真分岔：origin 那 6 個是我自己在 GitHub 上 merge 的三篇（含 PR 的原 commit），本機 3 個是我的修補加 babel 兩批。逐項對過**零重疊**（origin 只新增那三個譯文檔，都不在 babel 正在寫的檔案裡），所以不是策略 B 那條重路——`git merge origin/main` 一次乾淨併掉（`0a7661d43`），不 rebase（babel 的未 commit 工作在樹上，DNA #35）。收官 `0 0`。

### 其餘 issue 的判斷（不是分類，是判斷）

- **#1729 馬英九腳註**／**#1678 生態多樣性**：兩則都要改 zh 母稿的事實內容，命中 §1c 邊界「需要改 zh SSOT 內容實質的走 REWRITE-PIPELINE，不在 maintainer heal 範圍」。maintainer 班次改不動，**且不該在這裡改**。留 blocked。
- **#1609 郭淑姿日記**：昨天那班已把查證路徑從「翻兩冊實體書」縮到「一次登入臺灣日記知識庫」。剩下的阻塞是憑證，席位在人不在 routine。
- **#615 UI 傘**：長期追蹤 issue，本班無新增子項。

## Stage 4 — WRAP / Quality gate 7 條

| Gate                                     | 結果                                                                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee | ✅ 5 則都有 label；動過的 #1761 已認領                                                                                 |
| open PRs ≤ 5d age 都有 review comment    | ✅ 3 篇全 merge + 留言（backlog 歸零）                                                                                 |
| broken-link gated ratio < gate           | ⚠️ **NOT-MEASURED（誠實版）**——名目 0.34% 但 dist 齡 431.8h，本班把它改成會 STALE 的儀器；真實當前讀數要等一次新 build |
| build green                              | ✅ main 4 條 workflow 全綠                                                                                             |
| BECOME ACK 一行記憶體頂                  | ✅ 本檔第一行                                                                                                          |
| 連續空場 ≥ 3 cycle 有 LESSONS entry      | ✅ 不適用——本班有 3 fresh PR，vc 歸零                                                                                  |
| 有 fresh issue 的 cycle 至少一件被修掉   | ✅ 無 fresh issue（最新 #1761 是 09-21 開、09-24 更新）；仍修了 #1761 的內文凍結根因 `c44853ffe`                       |
| 本機與 origin 無真分岔                   | ✅ 收官 `0 0`（中途 `3 6` 當班併掉 `0a7661d43`）                                                                       |

**空場 vc**：0（本班收 3 fresh PR）。

**本班 commit**：`da95d0404`（push 進場 6 個 babel）／`b99ffe4fd` 翻譯路標／`0a7661d43` 分岔合併／`6868e12dc` 三支儀器／`c44853ffe` 登入警報內文。

**LESSONS append**：3 條新 pattern（`gate-measures-an-artifact-nobody-refreshes` structural／`guard-blind-to-the-file-type-its-own-docstring-indicts` structural／`entry-doc-advertises-a-tree-that-was-never-built` structural）＋ `alarm-goes-quiet-as-it-gets-urgent` 升 vc=2（instance 2 是內文那一格）。

三條 structural 同源：**閘門與現場之間隔著一份沒人負責更新的東西**。dist 是站體的替身而沒人刷新它；檢查器的副檔名清單是「程式碼」的替身而 python 不在裡面；入口文件的目錄樹是檔案系統的替身而那棵樹有六根虛構的枝。三次都是替身看起來很健康，而它代表的東西沒人在看。

---

## Handoff 三態

繼承（非本班職權，原樣傳遞）：

- 🚨 **給哲宇，2 天內** — mouhouse 登入預估 **09-27** 過期（issue `#1761`，剩 2 天）。標題與內文今天都已校到當下讀數。登入後看門狗自動記新日期。
- ⏳ blocked（延續）— `#1729` 馬英九腳註、`#1678` 生態多樣性：都要改 zh 母稿事實內容，走 REWRITE／FACTCHECK，等 Write session 帶哲宇 review。
- ⏳ blocked（延續）— `#1609` 第 30 天，剩餘阻塞是「一次登入臺灣日記知識庫」，席位在人不在 routine。
- [ ] pending（延續，席位 09-27 `twmd-self-evolve-weekly`）— `routine-sync.py` 對賬前 `git fetch`、印鏡像新鮮度。
- [ ] pending（延續，零判斷，給 spore-harvest）— `list_connected_browsers` 回 `[]` 時先查 `--no-startup-window` 再 `open -a`；掃 `/activity/replies` 逐則對 `time[datetime]`。
- [ ] pending（延續，給 maintainer-am／Full session）— build perf、`.git/gc.log`、`monitor-404.py`、pathspec 收官索引殘影、`/sitemap.xml` 200、15 份譯文相對路徑殘留。
- [ ] pending（低優先，等哲宇在場）— Threads 私訊夾是否納入受眾飛輪。

本班新 handoff：

- [ ] pending（**給下一班 maintainer-am，零判斷**）— broken-link audit 現在會回 `STALE`（exit 3）而不是假 PASS。本機 `dist/` 若仍是 09-07，先 `npm run build` 再量，或誠實記 NOT-MEASURED；**不要**用 `BROKEN_LINK_MAX_DIST_AGE_HOURS` 蓋掉它換一個綠燈。
- [ ] pending（**架構解，給 Full session**）— 把死連結檢查接進 deploy workflow 的 build 之後。現在這條 gate 沒有任何自動觸發（`postbuild:internal-links` 不是 npm 生命週期名，workflows 零處呼叫），所以它的新鮮度永遠取決於「當班本機恰好躺著什麼」。這是本班三條 structural 裡唯一還沒動到根的。
- [ ] pending（**給 Full session，逐檔判斷**）— `check-hardcoded-langs.sh` 掛號的 8 個 python 檔。優先序：三個感知層先（`fetch-cloudflare.py:431`／`refresh-llms-txt.py:85`／`weekly-report-prep.py:701`，錯讀數流進儀表板與 AI 介面），改吃 `langs.py`。B 類三個（已列滿 12 語）判斷該 derive 還是進允許清單。
- [ ] pending（**guard 設計改動，給 Full session**）— 本檔 `LANGCODES` 加 `zh-TW` 之前要先補「per-line 永久合理豁免」第三格，否則 4 個合理的 CJK 字族集合會被當債務永久提醒。加完後順手修 `generate-og-images.mjs:88`（8 語沒有自己的 OG 圖，讀者／社群分享面）。
- [ ] pending（資訊，給 `twmd-self-evolve-weekly`）— 今天三條 structural 是同一個形狀的三個載體（替身沒人刷新）。如果下週還有第四個載體出現，這條該升 REFLEXES 而不是留在 LESSONS。

🧬
