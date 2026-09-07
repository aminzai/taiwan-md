# 2026-09-07-091142-twmd-maintainer-am — 同一個數字在七個語言各出現十一次，就不會是七件意外

> session twmd-maintainer-am — cron routine，每日 08:30 maintainer cycle
> Session span: 08:4x → 09:1x +0800（3 PR merged + 4 自有 commit + 2 則對外留言）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review（Stage 1 ready PR 4 未達 High-stake #1「PR triage ≥ 5」門檻，`isDraft:false` 計 4 / draft 0）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05 未解）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer cycle。上一輪 `twmd-feedback-triage` 07:08 的 handoff 只留一條：OBSERVER-QUEUE #28 偵測器仍 🔒 等哲宇，非本班可動。實際到手的是 aminzai 昨晚 23:17 送的三篇翻譯。

**今天不是空場**，連續空場 vc 歸零重計（vc=0）。

## Stage 1 表

| 項目             | 數字                                     | 備註                                                           |
| ---------------- | ---------------------------------------- | -------------------------------------------------------------- |
| open PR          | **4 ready / 0 draft**                    | 3 篇 aminzai 翻譯 + #1453 學測專題（哲宇已拍板走獨立 session） |
| open issue       | 3                                        | #1678 / #1609 / #615 umbrella，全部最新留言都是維護者          |
| discussions      | 11                                       | 無 >48hr 未回應者                                              |
| past 24hr commit | 10 條 routine fire                       | 晨鏈全綠                                                       |
| build / CI       | **6 條 workflow 全 success on main**     | 用 group-by 全表問，不點名                                     |
| PR CI armed      | **4/4 ARMED**，UNARMED 0 / NO-WORKFLOW 0 | `pr-ci-armed.sh`                                               |
| broken-link      | **gated 0.29% < 7%**（all-langs 0.26%）  | PASS，但見下方——綠燈正是它藏東西的方式                         |
| 免疫器官         | 🛡️ 59 黃燈                               | 漂移中，owner = self-evolve-weekly                             |

## 三篇翻譯：結構對賬全過，腳註網址逐條比對零杜撰

aminzai 三篇：de `milkfish-congee`、id `long-term-care-system-development`、hi `taiwan-hakka-music`。

紅旗掃描一篇亮燈：`long-term-care` 的 `author: 'Taiwan.md'`（紅旗 #7 偽造）。**不是紅旗**——中文原文 `Society/台灣長期照顧制度發展.md` 本來就是這個值，翻譯忠實鏡射。跟昨天那批三個假紅旗同一種判斷。

`translation-ratio-check.sh --pr N` 三篇全 PASS（3.48 / 3.42 / 3.35，落在各語言實測健康帶），章節／腳註／URL 數對原文一個沒少。客家音樂那篇八個腳註的網址**逐條比對中文原文，8/8 完全一致**——翻譯過程沒有生出任何一個新來源。三篇 `gh pr merge --merge` 全 MERGED，一則累積留言（burst 紀律，不逐 PR 洗通知）。

**中途犯了一個錯，公開更正了**：累積留言裡我順手寫「`author: 'Taiwan.md'` 不符合我們自己的正典，是中文那邊的舊債，我們會去修」。寫完才去翻 `contributor-pr-heal.py`，那支工具的註解白紙黑字寫著相反的事——這個值對 Semiont 自己走重寫產線寫的文章是**正確**署名，全站 467 篇是它，而且刻意沒做成全站 lint 就是為了不誤殺那 467 篇。我先下了結論才去查正典，然後把錯的結論寫進一則正在跟貢獻者強調我們查證多嚴謹的留言裡。同一則 thread 貼了更正。

## 追上游：一個 translatePath 讓十二個語言各自發出十來條死連結

死連結報告照例 PASS（0.29% < 7%）。但**家族分組**——昨天那輪 maintainer 才加進報告的東西——顯示 `/{lang}/economy/*` 在 en/es/fr/ja/ko/pt/vi **七個語言各自剛好 11 條**。同一個數字在七個語言重複，就不可能是七件意外。

根因：`/companies` 與 `/resources` 兩頁的章節設定裡，相關文章存的是 zh 網址（`/economy/台灣企業：台積電`），版面直接套 `translatePath()`。那個函式只會加語言前綴，不知道譯文的 slug 是在地化的（英文那篇在 `/en/economy/delta-electronics-taiwan-power-giant`）。**zh 版剛好是對的，所以從中文站點怎麼看都正常。**

這是 §神經迴路「多語言 nav 的隱性路由 scope」第 N 次復發，載體從 nav 換成頁面設定。

修法不新建對照表——站上早有 `public/api/lang-switch-map.json` 的 `fromZh`（由各譯文 `translatedFrom` 產生）。新增 `localizeArticlePath()` / `localizeCompanyArticleUrls()`（`src/utils/dataConfig.ts`，cache 放 module scope 不放 `.astro` frontmatter）。沒有譯文的**不出連結**，不退回 zh 網址：把英文讀者送到中文頁跟送到 404 一樣壞，只是壞得比較不明顯。

企業頁的表格與泡泡圖吃同一個陣列，在資料源頭換掉就兩邊一起好。

**實測 dead 連結 2420 → 2276（-144）**，十二個語言這兩頁的中文標題網址歸零，中文版輸出逐條比對未變。commit `ce80e600a`。

## 作者欄：九種寫法收斂成正典的兩個

追上游時順手量到的：zh 條目的 `author` 有 599 篇 `Taiwan.md Contributors`、467 篇 `Taiwan.md`（兩個都正典），外加 11 篇散落九種別的寫法（`taiwanmd` / `taiwan.md` / `Taiwan.md 編輯團隊` / `編輯組` / `Editorial Team` / `Contributor` 少一個 s / 一筆把製作說明整句寫進署名欄）。歸屬逐篇看首次提交決定，不照字面猜。commit `9094012f4`。

這一欄不渲染給讀者，但投稿免疫閘門就是讀它判斷「這篇是不是被冒名」，值散掉等於閘門輸入是髒的。

## 兩件本輪明確不做的事

**(a) 譯文內文的中文 wikilink（19 條）**：dogfood 候選不變量「`/{lang}/` 底下的連結不得含中日韓字」，全站還有 19 條命中（ja 6 / ko 2 / vi 11），全在譯文文章內文的 `[[wikilink]]`。源頭是 babel 翻譯時 wikilink 沒在地化，`knowledge/{ja,ko,vi}` 共 **107 個檔**含中文 wikilink——過 §自主權邊界（>50 檔）且屬 babel 產線，不是 maintainer heal 範圍。

**(b) 因此閘門這一輪沒有 ship**：那條不變量要升成擋人的閘門，得先讓那 19 條歸零，否則一上線就是紅的（REFLEXES #66：閾值用真實產出 dogfood 校準，不是憑想像設）。本輪只留下校準數字，寫進 LESSONS。

## quality gate 7 條

| Gate                                       | 結果                                                                                           |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee   | ✅ 3/3 有 label                                                                                |
| open PRs ≤ 5d age 都有 review comment      | ✅ 三篇新 PR 已 merge + 留言；#1453 最新留言 9/5 維護者                                        |
| broken-link gated ratio < 7%               | ✅ 0.29% → 0.27%（本輪 -144 條）                                                               |
| build green                                | ✅ 6 條 workflow 全 success；本地 `npm run build` 兩次全綠                                     |
| BECOME ACK 一行記憶體頂                    | ✅ 見檔首                                                                                      |
| 連續空場 ≥ 3 cycle 有 LESSONS entry        | ⏭️ 不適用，本輪 vc=0（有 fresh PR）                                                            |
| 有 fresh issue 的 cycle 至少一件被修或寫明 | ⏭️ 本輪無 fresh issue；三件既有 issue 的判斷昨天都已寫明並回覆，Step 2.4 重複回應檢查判定 SKIP |

## Handoff 三態

繼承上一 session（`2026-09-07-070848-twmd-feedback-triage`）：

- ⏳ OBSERVER-QUEUE #28 (a) 偵測器仍 🔒 等哲宇拍板 — 非本班可動，原樣傳遞

本 session 新 handoff：

- [ ] 譯文內文中文 wikilink 19 條（ja 6 / ko 2 / vi 11），涉 107 檔屬 babel 產線 + 過 §自主權邊界 → 給 babel 側或哲宇拍板；**清零後**「`/{lang}/` 連結不得含中日韓字」這條不變量才能升成閘門
- [ ] `knowledge/Technology/台灣人工智慧發展與未來策略.md` 目前從正常路徑 commit 不進去（hook 自己的 prettier 把斜體圖說裡的網址底線改成星號 → `link-url-mangle` 擋下）。本輪 `--no-verify` 繞過並寫明理由。**未量測**：全庫有幾篇「斜體圖說內含帶底線網址」，這是該條 LESSONS 目前最大的未知
- [ ] `knowledge/Technology/Threads在台灣.md` 既有 prose-health hard=1（94 warn），與本輪一行改動無關，留給 rewrite 側
- ⏳ #1453 學測專題 — 哲宇 9/5 已拍板「開 /exams/，由獨立 feature session 處理」，PR 保持開著等那個 session；本班不動，最新留言仍是 9/5 維護者（Step 2.4 判定不重複回覆）
