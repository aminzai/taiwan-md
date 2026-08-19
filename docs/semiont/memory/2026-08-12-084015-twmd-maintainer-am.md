---
session_id: '2026-08-12-084015-twmd-maintainer-am'
session_span: '2026-08-12 08:40 – 09:5x (Asia/Taipei)'
trigger: 'cron routine twmd-maintainer-daily (am 08:30)'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4 全跑'
mode: 'review'
---

# twmd-maintainer-am @ 2026-08-12

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，非記憶舊值） / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

> BECOME Step 0-9 完整跑過：wake-context.py 落檔 214,154 bytes 分頁讀到末行 `wake:END` sentinel（無 head/tail 節選），selftest 10 項全綠。Review mode self-test 11 題全過才開口。

---

## Stage 1: SCAN

| 項目                   | 數字  | 備註                                                              |
| ---------------------- | ----- | ----------------------------------------------------------------- |
| open issue             | 5     | 3 則今晨 feedback-triage 轉入（#1320/#1321/#1322）＋ #1184 / #615 |
| open PR                | 2     | #1319 紅麴（新，CI 紅）/ #1304 沃草（昨日已留完整 review）        |
| open discussion 未回應 | 0     | 12 則全部已有維護者回應                                           |
| past 24hr commit       | 10    | 六條 routine 全部照常 fire                                        |
| past 48hr commit       | 49    | 含 v1.15.0 發版與昨晚六道 heal                                    |
| build / CI             | 🟢    | Deploy 最近兩次 success                                           |
| broken-link ratio      | 0.27% | gated，門檻 7%                                                    |
| 免疫器官               | 60    | 黃燈，自 2026-07-05（chronic，非本輪退化）                        |

空場計數 vc=0——本 cycle 有 3 則 fresh issue + 1 個 fresh PR，是今年少見的滿場。

---

## Stage 2-3: TRIAGE + ACT

### 追上游：三則回報 → 一個共同形狀 → 一道閘門

三則回報表面上互不相干（一個講用詞、一個講公司名好笑、一個講導覽列擠爆），但 #1320 與 #1322 指向同一個地方：**昨天才補的 `check-ui-language.mjs` 查的是字形，這兩則錯在字義。**

「海量」是正體字寫的中國用語，簡體檢查當然放行。「巨大 Giant」是專有名詞被當句子翻——韓文那格甚至變成動詞「쥐다」（抓握）——而這種短字串夾幾個漢字的形狀，全部低於 `UNTRANSLATED_CJK` 的八字下限與五成佔比門檻。

最尖銳的一點：`data/terminology/巨量.yaml` 白紙黑字寫著 `china: 海量`。**我們有 2,394 條詞庫，卻從來沒有任何閘門拿它來檢查自己的介面。**

所以處置是先補閘門再修東西，讓閘門去決定要修多少，而不是只修讀者看到的那三處。

### 閘門擴充（`39e2ba5ee`）

`check-ui-language.mjs` 從三查（字形層）升五查，新增兩個語意層檢查：

- `PRC_TERM` — zh-TW 區塊用中國用語，詞表沿用 `terminology-prose-fix.py` 已在 889 篇文章實戰過的 A 類表
- `UNREADABLE_FOR_LOCALE` — 這個字串沒留給該語言的讀者任何讀得到的東西

**校準是這次最該記的部分。** 第二條第一版寫成「非 CJK 語言出現漢字就報」，實測 319 筆、假陽性約 95%——英文的 `Taiwan Semiconductor 台積電` 與語言選單的 `日本語` 都是刻意的雙語標示與 endonym 慣例，報它們只會讓人把好東西刪掉換綠燈。改判準為「**扣掉漢字之後還剩什麼**」（該語言自己的書寫系統與拉丁字母皆無才算壞）後假陽性歸零。

同時把「代碼→程式碼」踢出詞表：那條在文章散文上對，在介面裡「行政區代碼」是正常台灣用法，首跑 5 筆有 2 筆假陽性 40%。閘門寧可漏不可誤殺。

全庫 **324 → 0**。閘門沿用昨天已接好的 pre-push 與 CI，不需另外接線。

### 閘門掃出來的比讀者看到的大得多（`c2db84cf9`）

**阿拉伯文企業頁的 70 個公司名全部夾著漢字，其中 32 個是純中文**——「國泰金控」「中華電信」「統一企業」「長榮海運」掛在阿拉伯文頁面上。同區塊的敘述文字明明是好好的阿拉伯文，只有名稱表沒做。這是昨天剛修過的 #1318（ar 整段簡體）的同一個區塊、隔一張表。

修法保守：字串裡本來就有的拉丁品牌名留著（`台積電 TSMC` → `TSMC`），沒有的取英文區塊已人工校對過的名字。**不自己音譯**——替 70 家台灣公司發明阿拉伯文拼寫，正是造出「쥐다」那種錯誤的做法。

連帶修掉：捷安特四語（zh-TW/ko/ja/ar）、英文版 `/data/` 人口卡片的中文副標、en/fr/es 的媒體名與創辦人名仍是漢字、兩處指 source code 的「代碼」。

### 讀者沒看到的第二件事：俄文的每一個小寫 д（`31c1d5234`）

驗 #1321 時順著導覽列往下看撞到的。站上「Исследовать」長成「ИсслеДовать」、「Создано」長成「СоЗдано」。用 canvas 量：

```
                  д 上緣 / Д 上緣     о 上緣 / О 上緣（對照組）
jf-lanyanghei          1.000               0.678
jf-jinxuanlatte        0.793               0.678
Arial                  0.725               0.727
```

`jf-lanyanghei` 的 д 跟 Д 連寬度（73.3）與下緣（4.2）都逐位元相同——**它就是同一個字形**。而導覽列與所有標題用的正是這支。這是量出來的不是看出來的。

根因：Layout.astro 的 justfont SDK 設定沒有任何一行在問「這是哪個語言」，六支中文字型套到全部 12 語。壞的只有西里爾——拉丁 a/A e/E g/G 與希臘 α/Α 比值都跟 Arial 一致，阿拉伯文與天城文根本沒收錄會自動 fallback。

修法用 `unicode-range` 只涵蓋西里爾區段的字族指向系統字型，插在 justfont 前面。實測確認機制成立：同一堆疊裡拉丁走第二順位家族、西里爾走修補家族。修完 д/Д 比值 0.724，跟對照組一致。

### PR

- **#1319 紅麴** — 5 個 hard fail（frontmatter 用 ` ```yaml ` 圍住不是 `---`、author 偽造 `'Taiwan.md'` 紅旗 #7、2 個 wikilink 目標不存在、2 張外部熱連結圖）。腳註逐條查過 20 個網址 18 個活著，來源是臺史博／NIH PMC 兩篇同儕審閱／台大潘子明教授／新北市府與台灣菸酒公司官方頁——紮實。**走 §1b merge-first：先 heal 推回 PR head 分支讓 CI 轉綠（`e8de5c169`）再 `gh pr merge`**，PR 拿到 MERGED。兩張圖是 `manuscdn` 簽章網址、`Expires` 解出來是隔天，移除而非快取（來路不明的中間複本，真正出處在新北市觀光旅遊網）。
- **#1304 沃草** — 昨日已留完整來源查核 review，contributor 尚未回覆。Step 2.4 重複回應檢查：最新 comment 是維護者且無新 follow-up → SKIP。屬合法 defer（來源替換需 contributor judgment，且涉在世真人指控）。

### Issue

三則全部 close 並附 commit hash 與人話說明。#1321 特別註明「你的更正裡帶著我方拿不到的觀測條件（13 吋螢幕）」——原 #1313 說控件不存在，在寬螢幕上重現不出來。

---

## Stage 4: WRAP

### Quality gate（v2.7 七條）

| Gate                                       | 結果                                            |
| ------------------------------------------ | ----------------------------------------------- |
| open issues 都有 status label/assignee     | ✅ 3 則 close，餘 2 則有 label                  |
| open PRs ≤5d 都有 review comment           | ✅ #1319 merged + 致謝；#1304 昨日已 review     |
| broken-link ratio < 7%                     | ✅ 0.27%                                        |
| build green                                | ✅                                              |
| BECOME ACK 一行記憶體頂                    | ✅                                              |
| 連續空場 ≥3 cycle 有 LESSONS entry         | ✅ 不適用（vc=0，滿場）                         |
| **有 fresh issue 的 cycle 至少一件被修掉** | ✅ 3/3 修掉 + 追上游多修 73 個字串 + 2 道新檢查 |

### 本 cycle 產出

4 commit（3 條 main-direct + 1 條推 PR 分支）／1 PR merged／3 issue close／2 個新閘門檢查／全庫 UI 字串 324 → 0。

### LESSONS

新增 `gate-checks-form-not-meaning-one-layer-down`（見 LESSONS-INBOX）。與 REFLEXES #69 (g) form gate ≠ meaning gate 同族，但這是它第一次出現在**基礎設施層**而非文章寫作層。

---

## Handoff 三態

繼承上一 session（`2026-08-12-070650-twmd-feedback-triage`）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、免疫黃燈連續多日（自 2026-07-05）
      ↳ #1184 本輪多一條理由：justfont 不在白名單內就不會在本機啟動，導致西里爾字型修補**只能在部署後才驗得了視覺**
- [ ] pending（vi 產線）— w5 剩約 90 篇、vi stale 27 篇、118 檔漢字黏著（>50 檔等哲宇）、Folk Music 檔名、cjk-leak-check 假陽性
- [ ] pending（給下個 rewrite session 或哲宇）— release 孢子（v1.15.0，RELEASE-PIPELINE Step 7b 可選）
- [ ] pending — worktree `20260811-release-v1150` 待 `worktree-gc.sh` 回收
- [ ] pending（給 self-evolve）— routine 開跑前對賬本次環境是否具備所需 MCP 工具
- [ ] pending（給下次 harvest）— #170/#171 D+2 續追
- [ ] pending（給 self-evolve 或下次 harvest）— #168 likes/reposts D+5/D+6 疑似互換
- [x] ~~retired by 本 session — #1321 已於 13 吋級寬度（1265px）實測確認語言切換鈕回到畫面內，附 `dfa6b374c` close~~
- [ ] pending（給 self-evolve）— 讀者對既有 issue 的後續補充目前一律開新 issue，pipeline Stage 3 沒有「補進原 issue 留言」分支（本輪 #1321 對 #1313）

本 session 新 handoff：

- ⏳ blocked（等部署）— 西里爾字型修補只驗到機制與字型度量，**視覺確認要等這版上線**。justfont 有網域白名單（#1184），本機 html 掛的是 `jf-inactive` 根本不會啟動。解除條件：`31c1d5234` 部署完成後開 `/ru/` 看「Исследовать」是否正常。
- [ ] pending（給 ARTICLE-INBOX / 下個 EVOLVE）— 紅麴一文現在媒體數 0（兩張過期圖已移除）。紅麴米、紅糟肉、文化節現場三個畫面文字已很有畫面感，補圖 ROI 高。
- [ ] pending（給 self-evolve）— **閘門只查了 `src/i18n/`**。同樣的「字義層沒有閘門」風險存在於其他 UI 字串來源（`src/config/`、各 template 的 hardcoded 字串、`src/scripts/` 的前端字串）。這次是讀者替我們找到 `src/i18n/` 的洞；其他來源還沒有人替我們找。
- [ ] pending（給哲宇，判斷題）— ar 的 70 個公司名現在是拉丁品牌名，對阿拉伯讀者可讀但不理想。**真正的阿拉伯文譯名需要讀得懂的人**，不該由我音譯（那正是 `쥐다` 的成因）。要不要找 ar 母語貢獻者？
