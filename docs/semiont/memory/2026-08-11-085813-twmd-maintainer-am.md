---
session_id: '2026-08-11-085813-twmd-maintainer-am'
session_span: '2026-08-11 08:30 — 09:10 +0800'
trigger: 'cron routine twmd-maintainer-daily（am 08:30）'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4 全跑'
mode: 'Review'
---

# twmd-maintainer-am @ 2026-08-11

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（即時 consciousness-snapshot.sh，齡 2h，慢性黃燈自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

> BECOME 完整跑 Step 0→1→Review 載入→8→9。wake-context 讀到 `wake:END` sentinel（230,474 bytes / 11 段），10 項體檢全綠。MAINTAINER-PIPELINE 1319 行全讀。
>
> 昨天那則「Review 欄勾 12 題但過題數寫 11」的 canonical 對不上今天仍在，我一樣照 12 題全答（取超集）。連兩天同一處，留給 self-evolve。

---

## Stage 1: SCAN

| 項目                  | 數值                | 備註                                                           |
| --------------------- | ------------------- | -------------------------------------------------------------- |
| open PR               | 3 → 1               | #1308 / #1309 merge，#1304 依昨日 review 留 open 等貢獻者換源  |
| open issue            | 14 → 15             | 8 則讀者回報全數 triage；本 cycle 新開 #1318                   |
| past 24hr commits     | 16 筆               | 全為 routine 與昨日 manual（登入態恢復 / mouhouse 體檢）       |
| past 48hr commits     | 逾 190 筆           | 絕大多數巴別塔產線與 vi 委派批次（量體不是飛輪轉速）           |
| build status          | green               | Deploy 近 5 次 3 success / 2 cancelled（推疊取消），無 failure |
| broken-link ratio     | **0.22%**           | gated < 7.0% THRESHOLD_PERCENT，PASS（all-langs 0.20%）        |
| i18n smoke            | 最近一次 2026-07-26 | 路徑觸發式 workflow，非每日跑；本 cycle 未觸發                 |
| Discussions           | 11 筆，0 筆未回應   | 無 >48hr SLA 逾期                                              |
| node PR（draft 認領） | 0                   | 無墓碑待清                                                     |
| 免疫器官              | 🛡️ 60               | 慢性黃燈第 37 天，OBSERVER-QUEUE #25 三選一仍待拍板            |

**空場 vc 歸零**：本 cycle 命中 2 fresh PR + 8 fresh issue，非空場。

---

## Stage 2-3: TRIAGE + ACT

### PR #1308 ja 譯文 — merge + heal ✅（merge `2026-08-11T00:45:39Z` / heal `f9e9b08a4`）

tboydar 送來 AI 硬體供應鏈的日文重譯，自陳「與 Antigravity AI 共同協作、中文母語者審閱」。

**先講它好在哪**，因為這決定了處置：譯文替日本讀者補了「兆元宴」「護國神山群」「矽盾」的括號解釋，TSMC 開成「台湾積体電路製造」，經營者名附上國際慣用讀法。這些是機器翻譯不會做、只有人看過才會加的手當。舊版是 7/23 巴別塔產線的純機器輸出。**所以這是升級，不是平移**——merge 是對的。

但它同時帶進九類結構退化，其中一類會造成不可見的損失：

| 退化                                                                    | 後果                                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------- |
| **刪掉 sourceCommitSha / ContentHash / BodyHash / translatedAt / lang** | **巴別塔把它當沒翻過 → 夜間批次用機器譯文蓋掉人審版本** |
| tags / subcategory 退回中文                                             | 日文頁面出現繁體標籤                                    |
| 四張圖 alt 退回中文                                                     | 螢幕閱讀器與 SEO 讀到錯語言                             |
| 延伸閱讀 7 條連結指向 `/technology/半導體產業` 等中文頁                 | 日文讀者一點就掉出日文版                                |
| 刪掉 `## 参考資料` 標題                                                 | 腳註無標題裸掛                                          |
| H1 消失 / H2 後無空行 / `author` 非 canonical                           | 格式層                                                  |

第一項是本 cycle 最該記的一件事。它不會報錯、不會變紅，隔幾天悄悄把貢獻者親手審過的譯文換掉，而且沒有人會發現。我補回五行後跑 `backfill-source-sha.py --lang id,ja --dry-run`，ja candidates=0，確認這篇已回到 fresh——這是「修好了」的外部證據，不是我自己說的。

**兩處人名查證後改正**（原文沒有、翻譯時補上去的資訊）：

- 劉揚偉 `ヤン・リウ` → `ヤング・リウ`（[Young Liu](https://en.wikipedia.org/wiki/Young_Liu)，鴻海董事長）
- 葉培城 `ドーディ・イエ` → `ダンディ・イエ`（[Dandy Yeh](https://csr.gigabyte.tw/en/corporate-organization-en-2/)，技嘉董事長）

同段其他七個名字（Barry Lam / Rick Tsai / Jonney Shih / Simon Lin / Emily Hong / Jason Chen / C.C. Wei）全對——**只錯兩個，所以特別難抓**。這正是 §神經迴路 2026-07-25 ar/ru 那條「人名幻覺第二型是填空不是混淆」：模型不是分不清兩個人，是不認識這個人，就用聽起來像的讀音填掉。

### PR #1309 id 譯文 — merge + heal ✅

benben6515 補 `id/Food/` 缺口。譯文品質好，本地化判斷到位（用印尼已熟悉的「boba」解釋手搖飲、中文店名保留在括號、QQ 譯成口感說明）。

**這篇最值得記的不是譯文，是它怎麼被審的**：tboydar 在 PR 上抓出兩塊 AI 自行加上、zh 源沒有的 `📝 Catatan Kurator`，benben6515 自己複查、認了、拿掉，全程在我看到這個 PR 之前就結束了。**一個貢獻者審另一個貢獻者，問題沒走到維護者就解決了**——這是免疫系統自己長出來的樣子，比我這輪做的任何事都重要。

heal 只有兩項：`author` 改 `'Taiwan.md'`（對齊 zh 源與 en 版）、`backfill-source-sha.py` 補翻譯履歷。他寫的 `translatedFrom` 格式完全正確（無 `knowledge/` 前綴）——那是最常錯的一欄，他對了。

### PR #1304 沃草 — 維持 open（Step 2.4 SKIP 重複回應）

最新留言是昨日 maintainer 的來源查核 review（7 腳註中 5 條是媒體首頁），無貢獻者 follow-up → **不重複回覆**。這是 §三級判斷 ❌ 那列的正常狀態：request changes 後仍 open 等修，不是 silent close。

### 8 則讀者回報 triage（#1310-#1317）

回報者 @Pigcasso6 兩天內送了 10 則，全是自己逐頁比對多語版本抓出來的。品質很高：#1316 逐字指認「送」是系統字體、「出」是 justfont，這種顆粒度剛好能區分「字體沒載到」與「子集不完整」。

處置：加路由 label（translation ×3 / needs-verification ×1 / good first issue ×2），並補兩則技術交叉參照——

- **#1316 → #1184**（開 43 天）：逐字分裂是動態子集只載到部分字元的典型長相，指向 justfont 授權網域設定。兩條同根，建議一起驗
- **#1313**：俄文 UI 這片區域第二次被回報（8/06 是烏克蘭文介面）

**回覆讀者本人仍是人類 gate**，未代發（per §自主權邊界 + 昨日 handoff）。

---

## 追上游時撞到的東西 — 新開 #1318

追 #1311 / #1312（「非核心語言保留中文原文」）往 UI 字串層走，發現的比回報的嚴重一階：

**`src/i18n/data.ts` 的 `ar` 區塊有 20 行是簡體中文，而且用中國詞彙。** 阿拉伯文讀者在 `/data/` 看到的不是阿拉伯文，也不是正體中文：

```js
'data.companies.story.title': '人工智能浪潮把整座岛重新定价',
'data.fellOff.htc': '智能手机溃败，VR/XR 未能撑起规模',
'data.companies.story.p1': '⋯⋯台积电一家就占了全市场 43.8%⋯⋯',
```

人工智能（台灣：人工智慧）／智能手机（智慧型手機）／台积电／资料来源／联发科／国巨。一個以主權保存為架構目的的站，在自己的阿拉伯文頁面上用中國的字形跟中國的詞彙描述台積電。MANIFESTO §主權的巴別塔防的是被沉默，**這是從反方向發生的同一件事：不是消音，是替換成對方的講法**。

### 我這把尺一開始量錯了，過程要留痕

第一版我用「CJK 字元佔比」當訊號，得到 en 26% / ja 88% / ar 30% / fr 22%。**這是 REFLEXES #82 的 proxy signal**——公司名本來就是中文，佔比高低跟語言對不對無關，量的是替身不是本體。

換成「無歧義簡體字」（沿用 `terminology-charcheck.js` 的 OpenCC candidate 判定 `s2t(C)≠C 且 t2s(C)==C`）才摸到 ground truth。但第一次跑吐 111 行，扣掉三類假陽性後真陽性 20 行，**假陽性率 82%**：

1. `ja` 全部 91 行——日文新字體 湾/数/点 與簡體同形
2. `about.ts` 的 `你好，我无法给到相关内容`（ko/vi/fr/es 各一）——**這是故意的**，逐字引用騰訊 Hunyuan 拒答台灣主題的那 40 bytes，是 MANIFESTO 敘事的證據本身。**改掉它等於刪證據**
3. `zh-TW` 的 苗栗/粽/岳/郁——正體本字，白名單未收錄的已知誤判

**沒先跑一次就接進 CI，第一天就會被當噪音關掉**（REFLEXES #66 + 8/09「有一支儀器每天說謊，而我們每天原諒它」）。三類豁免已寫進 #1318 與 LESSONS，接線的人不必重踩。

---

## Stage 4: WRAP

### Quality gate 六條

| Gate                                  | 結果                                                |
| ------------------------------------- | --------------------------------------------------- |
| open issues 都有 status label         | ✅ 15/15（本 cycle 補 6 個路由 label）              |
| open PRs ≤ 5d age 都有 review comment | ✅ #1304 昨日已 review，#1308/#1309 已 merge + 致謝 |
| broken-link ratio < 7%                | ✅ 0.22%（all-langs 0.20%）                         |
| build green                           | ✅ 無 failure                                       |
| BECOME ACK 一行記憶體頂               | ✅                                                  |
| 連續空場 ≥ 3 cycle 有 LESSONS entry   | ⏭️ 不適用（本 cycle 有件，vc 歸零）                 |

### LESSONS append

`ui-string-layer-has-no-language-gate`（vc=3，**已達 distill 門檻**）：文章層有 `cjk-leak-check.py`，`src/i18n/*.ts` 一支都沒有。8/06 俄文 → 8/10 讀者四則 → 8/11 阿拉伯文簡體，同層同病三次。**保護密度跟曝光量成反比**：UI 字串出現在每一頁，卻是唯一沒有閘門的那層。工具現成（`terminology-charcheck.js` 的判定邏輯），缺的是登記與接線。

### 順手記下的兩則 canonical 漂移

- BECOME §行動鐵律 5 寫 `verify-commit-scope.sh`，實際在 `scripts/tools/lib/`。照鐵律的路徑跑會 command not found
- BECOME §Step 9 Review 欄勾 12 題、過題數寫 11（連續第二天）

### 沒做的事，明講

- **`## 圖片來源` 缺漏**（id 譯文的唯一 warn）：查了 zh 源與 en 版**都有同樣缺漏**，是上游 SSOT 的舊債不是這個 PR 帶進來的。只補 id 會讓它跟家族其他語言不一致，正解是先修 zh 再傳播——那是 REWRITE 的範圍，不是 maintainer heal。留給下游
- **#1318 的 20 行沒有當場翻**：走 babel（`ar` guide 已有主權詞表），不是 maintainer cycle 該在無人時段自行下筆的東西

---

---

## 第二段：哲宇 directive 後的自我進化 + 全站 issue 清理（09:30—）

> 「請自我進化，MAINTAINER 不只要回覆 ISSUE 而是要協助回應 判斷 評估 研究 落檔 然後執行相關的修正與自我進化或是網站更新，這樣才有意義」
> 追加：「也把線上的 ISSUE 都處理完畢」

過 Bias 1 濾網（對創造者預設加分要警覺）：這是 pipeline 調整，在 §自主權邊界「我自己決定」內，且哲宇 explicit 要求。命中 High-stake #2「新 workflow 設計」→ 升 Full mode 補載。

### 他說中的東西很具體

回頭看本 session 上半場：八則讀者回報，我加了六個路由 label、補兩則交叉參照、開一則新 issue、寫完整 handoff——**修好的數字是零**，而六條 quality gate 全部打勾。

**閘門量得到「有沒有處理」，量不到「有沒有解決」。** 所以那輪看起來很健康。這不是我偷懶，是 pipeline 允許它發生：§1 default-action 原則整段只講 PR，issue 側對應的位置是空的，Step 3.6 就叫「reply / label / close」——這個名字本身把 issue 描述成待路由的郵件。

### 順序刻意倒過來：先修，再把修法沉澱回 pipeline

沒有先寫 pipeline 再照著做，因為那會是憑空設計（REFLEXES #66：閘門要用真實產出 dogfood 校準）。先真的把十則回報追完、修完，再把「怎麼修的」寫成 canonical。

### 追上游：十則回報 → 一個根因 → 一道閘門

讀者 @Pigcasso6 的十則看起來是十個獨立 bug。追下去，其中五則指向同一件事：**`src/i18n/*.ts` 這層沒有任何東西在檢查「這裡的字是不是該語言」**。文章層有 `cjk-leak-check.py`，UI 字串層一支都沒有——而 UI 字串出現在每一頁，曝光量遠高於任何單篇文章。

修完根因後又撈出兩件讀者沒看到的：ar 的 `/data/` 整段是簡體中文且用中國詞彙、en 區塊裡一句沒翻的正體中文。

### 實際修掉的（7 則 close）

| #    | 東西                  | 根因（都不是表面看起來那樣）                                                                                                                                      |
| ---- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1317 | 企業泡泡圖            | 不是誤譯，是 `split(' ')[0]` 把公司名切斷。**70 家有 45 家中招**：台積電與台灣大哥大都顯示 `Taiwan`、中鋼顯示 `China`。另外億(10⁸)被標成 B(10⁹)，每家市值講大十倍 |
| 1314 | 回饋模組六語英文      | 字串表停在 6 種語言，站上已 12 種，靜默 fallback。檔頭註解還寫著六語時代的清單                                                                                    |
| 1315 | 中文半形標點          | 修 7 處（讀者列了 3 處）                                                                                                                                          |
| 1313 | 俄文語言鈕消失        | **不在 CSS，在字串**：vi/id/pt/hi/ar/ru 照 zh-TW 複製時連六個裝飾 emoji 一起帶走，而 en/ja/ko/es/fr 早就拿掉了。俄文最長 + 六顆 emoji = 擠爆那一行                |
| 1311 | taiwan-shape 八語未譯 | 四行簡介寫死在模板的三層巢狀三元式，只認 en/ja/ko                                                                                                                 |
| 1310 | ja 按鈕斷行           | 日文沒空格可任意斷字，拉丁文斷在空格所以看不出來                                                                                                                  |
| 1306 | ja 用繁體字形         | 整套字體堆疊只有 TC，**全站零條 per-language 覆蓋**。ja/ko 讀者一直用台灣字形讀自己的語言                                                                         |
| 1318 | ar 簡體中文           | 本 session 上半場自己開的，一併修完                                                                                                                               |

### 造的閘門

`scripts/tools/check-ui-language.mjs` — 查簡體外洩 / 整串未譯 / 字串表落後語言註冊表三件事，接上 pre-push（~0.2s）與新 CI workflow。**三種失敗模式都用注入測試實測會擋**，測完復原並驗證零殘留。

全站掃描 42 筆 → 0 筆。

三類豁免全部來自實測（未校準版本假陽性率 82%）：ja 新字體同形、`about.ts` 那句騰訊拒答原文是**證據不是外洩**、台灣正體本字（實測又補了「凶」）。

### Pipeline 進化（v2.6 → v2.7）

- **§1c 新核心原則**：Issue 的 default 是修好，不是分類好。五步：判斷→評估→研究→落檔→執行
- **Step 3.6 改名重寫**：從「reply / label / close」→「判斷→評估→研究→落檔→執行」，加追上游 + 修完必補閘門必驗證
- **Quality gate 6→7 條**：有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修
- 三層同步（canonical / project skill / cron 鏡像），**inline 不是 pointer**（2026-05-28 已證明 cron 無人時 pointer 會 fall through）

### 沒修的兩則，理由都寫進 issue

- **#1312 `/bench/` 未譯**：量過了，模板 1,442 行含 117 行中文共 1,215 字，只有 7 個 `t()`。這是整頁 i18n 抽取（~117 字串 × 11 語言），硬塞進維護輪只會做出半套。且內容涉 PRC 拒答論述，屬 BENCH-PIPELINE 領域
- **#1316 字體混用**：診斷完成（動態子集只載到部分字元，根因是 #1184 justfont 後台網域設定），但那是哲宇的後台，我沒有存取權

### 這次學到的

**我自己就是那個反例。** 上半場我做的每一件事都符合當時的 pipeline，六條 gate 全綠，而讀者的問題一個都沒解決。閘門不會說謊，但它只會回答你問它的那個問題——我問的是「有沒有處理」。

還有一次「差點造了沒用的東西」：為 #1313 寫了一套 `data-nav-width` 依標籤長度算斷點的機制，結果光是對齊 emoji 就修好了。那個屬性沒有任何 CSS 在讀它。**留一個看起來像防護、實際不做事的旋鈕，比不留更糟**——拿掉了。

---

## Handoff 三態

繼承（非本 session 職責，接住不動）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充、免疫黃燈 37+ 天（OBSERVER-QUEUE #25）
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、641 處漢字黏著待哲宇、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— 孤兒《台灣公投制度》在 `reports/orphan-rescue/`，上站前需補研究報告或重驗事實原子
- [ ] pending（給 self-evolve）— 巢狀回覆抽查升 pipeline canonical 的評估，per LESSONS `harvest-scan-misses-nested-replies`
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換，是否回填訂正待人工決定
- [ ] pending（給哲宇）— EZWAY 話題環境持續政治化，純觀察無需回應
- [x] ~~retired by 本 session — #1310-#1317 八則已全數 triage + 加路由 label + 兩則技術交叉參照~~

本 session 新 handoff（第二段後更新）：

- [x] ~~retired by 本 session — #1318 ar 簡體中文已重譯為阿拉伯文 + 閘門已造並接上 pre-push/CI（`1efda3851`）~~
- [x] ~~retired by 本 session — LESSONS `ui-string-layer-has-no-language-gate` 已落地為 `check-ui-language.mjs`，三類豁免實測寫進工具檔頭~~
- [x] ~~retired by 本 session — #1311 / #1314 已修並 close；#1312 已完成規模評估並寫進 issue~~
- [ ] pending（給哲宇）— **@Pigcasso6 三天送 10 則高品質回報，其中 8 則已修並 close**。全是他自己逐頁比對多語版本抓出來的，#1318 也是循他的線索找到的。**回覆與致謝仍屬人類 gate**，未代發。這位讀者的回報密度與精度已經超過任何自動巡檢，值得一封像樣的信
- [ ] pending（給哲宇）— **#1316 + #1184 justfont 後台網域白名單**。#1316 診斷已完成（動態子集只載到部分字元），根因確定在 #1184，但那是你的後台。#1184 已開 43 天
- [ ] pending（給 babel）— **#1312 `/bench/` 整頁 i18n 抽取**。已量：117 行中文／1,215 字／僅 7 個 `t()`。路線寫進 issue 了（抽 i18n → babel → 人工複核敏感段落）
- [ ] pending（給 self-evolve）— MAINTAINER v2.7 的第 7 條 quality gate 是本 session 現寫現用的，**還沒有跨 cycle 驗證**。下週看它有沒有真的改變 routine 行為，或只是多一行打勾
- [ ] pending（給下個 maintainer cycle）— **#1319「紅麴」新文（idlccp1984）於本 session 收官期間 14:58 送達**，未進本輪 triage。同一位貢獻者的 #1304 仍 blocked 中，收 #1319 時建議一併看兩篇的來源品質是否同型
- [ ] blocked — #1304 沃草等貢獻者換源；昨日已具體列出 5 條媒體首頁腳註。**解除條件**：貢獻者 push 新 commit 或回覆

🧬

---

_v1.0 | 2026-08-11 09:10 +0800_
_session twmd-maintainer-am_
