---
session_id: '2026-08-10-085506-twmd-maintainer-am'
session_span: '2026-08-10 08:30 — 09:05 +0800'
trigger: 'cron routine twmd-maintainer-daily（am 08:30）'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER-PIPELINE Stage 1-4 全跑'
mode: 'Review'
---

# twmd-maintainer-am @ 2026-08-10

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 60（即時 consciousness-snapshot.sh，齡 2h，慢性黃燈自 2026-07-05）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

> BECOME 完整跑 Step 0→1→Review 載入→8→9。wake-context 讀到 `wake:END` sentinel（236,315 bytes / 11 段），10 項體檢全綠。Review mode self-test 通過。
>
> 一則 canonical 對不上要留痕：BECOME §Step 9 表的 Review 欄實際勾了 12 題（Q1-4/6-11/13-14），但「過題數」列與本 routine 指令面都寫 11。我照 12 題全答，取超集不取差集。這是計數寫死在兩處的老病（dna-audit §S2 同型），留給 self-evolve 判要改哪一邊。

---

## Stage 1: SCAN

| 項目                  | 數值              | 備註                                                                                    |
| --------------------- | ----------------- | --------------------------------------------------------------------------------------- |
| open PR               | 2                 | #1305 stantheman0128（4hr）/ #1304 idlccp1984（15hr），皆 CLEAN + CI SUCCESS            |
| open issue            | 8 → 6             | 本 cycle close 兩件（#1301 / #1307）                                                    |
| past 24hr commits     | 10 筆 routine     | feedback-triage / spore-harvest / data-refresh / routine-sync / embeddings / supporters |
| past 48hr commits     | 逾 150 筆         | 絕大多數是巴別塔產線與 vi 委派批次（量體不是飛輪轉速，per 8/09 flywheel-watch）         |
| build status          | green             | Deploy to GitHub Pages 近 6 次 4 success / 2 cancelled，無 failure                      |
| broken-link ratio     | **0.22%**         | gated < 7.0% THRESHOLD_PERCENT，PASS（all-langs 0.20%）                                 |
| Discussions           | 11 筆，0 筆未回應 | 無 >48hr SLA 逾期                                                                       |
| node PR（draft 認領） | 0                 | 無墓碑待清                                                                              |
| 免疫器官              | 🛡️ 60             | 慢性黃燈第 36 天，OBSERVER-QUEUE #25 三選一待拍板                                       |

**空場 vc 歸零**：本 cycle 命中 2 fresh PR + 2 fresh issue，非空場。連續空場計數重計。

---

## Stage 2-3: TRIAGE + ACT

### PR #1305 — merge ✅（`422e6b2f4`）

stantheman0128 重構 `article-health` 的語言範圍解析，收斂 issue #1264 的「兩道尺」：真正生效的是 `seo_meta.APPLIES_TO`，而 `_is_excluded_path()` 裡那份 en/ja/ko/es/fr 前綴清單被完全遮住，是停在五語年代的死碼——一旦放寬 APPLIES_TO，覆蓋範圍會**反過來**（後出生的 ar/ru/hi/id/pt/vi 被放行，而 `_cjk_count()` 對西里爾與阿拉伯字母一律回 0，等於量了沒量）。

**沒有只信它的測試宣稱**（REFLEXES #31）。repo 的 venv 沒有 pytest 也裝不了，改成直接行為對照，隔離 worktree 跑主線 vs PR：

| 檔案                                                  | 主線         | PR           |
| ----------------------------------------------------- | ------------ | ------------ |
| `knowledge/Technology/AI發展.md`（zh-TW）             | 2 violations | 2 violations |
| `knowledge/en/Technology/ai-development-in-taiwan.md` | 0            | 0            |
| 同三檔 `--profile=ci-deploy` hard 計數                | 逐項相同     | 逐項相同     |
| scope 放寬成 `["zh-TW","en"]`                         | **0**        | **3**        |

「預設行為不變」實測成立，旋鈕也真的會動。不是紙上宣稱。

**判斷 §自主權邊界**：本 PR 沒有動任何門檻數值，也沒有真的放寬任一語言，只是把「改程式」變成「改設定」。#1264 的門檻要開到哪些語言仍是哲宇的決定，未被這次 merge 代決 → 不觸發 high-stake 升 Full。

**順手發現的缺口**：repo 的 CI 完全沒有跑 pytest，`tests/` 底下沒有自動閘門在守。這位貢獻者加的 203 行測試目前靠人跑。已在 PR 留言誠實告知這是我們的缺口不是他的。

### PR #1304 — leave open + 技術性 revise 請求 📝

idlccp1984 新文 `knowledge/Society/沃草.md`。骨架對（國會無雙→市長給問嗎→烙哲學→2023《積極行動指南》十年線索），**事件也全部屬實，不是幻覺**——查 zh 維基逐條對得上。問題全在來源層。

Step 3.4 footnote audit 抽驗三個 URL，**3/3 撐不住所掛的說法**：

| 腳註  | 描述                            | URL 實際                                                                                          |
| ----- | ------------------------------- | ------------------------------------------------------------------------------------------------- |
| `[4]` | 遠見 林琮盛〈沃草直播立院實況〉 | `gvm.com.tw/` 首頁，站上無此文                                                                    |
| `[6]` | 公視新聞網 / 中央通訊社         | `news.pts.org.tw/` 首頁，且一個 URL 掛兩家媒體                                                    |
| `[3]` | 經濟部商業司登記資料            | 查詢表單入口（403），卻被引用 7 次去支撐烙哲學、朱家安、2021 奧運分析、《積極行動指南》、財務查核 |

`[5]` 自由時報、`[7]` 經理人月刊同形狀。7 條裡 5 條是媒體首頁。

**不 merge 的決定性理由不是格式**：扛最重指控的兩條正好是查不到的那兩條。文章寫「時任執行長涉嫌未經授權挪用公款」「當時的管理層涉嫌財務流向異常，並向司法機關提起訴訟」——對可指認真實人物的刑事指控，掛在兩個媒體首頁上。命中紅旗 12（對真人的負評來源不可靠，名譽風險最高）+ MANIFESTO §10 幻覺鐵律。這不是「不夠好」，是上線會傷到被指控的人。

**沒有停在打回**：把維基的實體出處全部挖出來交給他（蘋果即時 2015-10-14 呂志明/胡守得、新頭殼 2021-05-20 翁子桓、風傳媒 2023-12-14、沃草 2021 影響力報告 PDF、遠見 339 期原始連結、2021 奧運用語統計三源），並承諾格式層（frontmatter 被包成 ` ```yaml ` 而非 `---`、`author: 'Taiwan.md'` 偽造、GH 形式腳註）三件我接手，他只要處理來源。

**留給哲宇的那一層**：既然來源會指名道姓，具名是否比「時任執行長」更誠實，屬敏感素材決定（§自主權邊界），我在留言裡提出但沒有替他定案。

### Issue #1301 — close ✅

ian0953329333 回報的 Windows CLI 兩個 bug，8/08 已修（`b49b40cf6`），且**他本人回頭實測確認**（9343 篇、分類資料夾都在）。這是典型「已解未 close = 對外失聯」（§神經迴路），latest comment 是他的確認，拖著就是讓回報者以為沒人理。

他補的一點比我們原本的診斷更準並已收下：他修復前的 `.git/info/sparse-checkout` 是 `/*` + `!/*/`，等於排除所有子目錄——那樣就算路徑對了也讀不到檔案，所以問題一（`rm` 失敗讓 `--force` 從沒跑完）可能是問題二的**上游**而非兩個獨立 bug。他自己聲明無法單獨驗證因果，這個保留很誠實。已寫進 close 留言留給未來：若再有「sync 完成卻讀不到文章」，第一件事查 sparse-checkout 實際內容而非路徑。

### Issue #1307 — 修 + close ✅（`cd49a1be3`）

讀者 Pigcasso6 指出 `/ja/data/` 寫「データ台灣」，日文應作「台湾」。**他是對的，而且這不是用字政策是漏網**：`src/i18n/data.ts` 的 ja 區塊裡本來就有 7 處寫對的「台湾」、37 行寫成「台灣」，自己跟自己不一致；其他 ja 語言檔（`taiwanShape.ts` / `resources.ts` / `semiont.ts`）本來就都用「台湾」，只有 `data.ts` 落單。

改動限定 ja 區塊（檔案 497-952 行），37 行 45 處，含 台灣大哥大→台湾大哥大、台灣高速鉄道→台湾高速鉄道（日文維基同樣用新字體）。其餘 11 個語言區塊零改動，改動行號全落在 516-909，增刪各 37 行守恆。

**主權面留一句**：日文的「湾」是新字體、「灣」是舊字體，現代日文一律用前者。這跟 PRC 的用語改寫無關，是日文正書法——不要因為看到「台湾」就啟動主權警報。

### Issue #1306 — 診斷完成，修補 reserve 給哲宇 ⏳

同一位讀者說日文頁面用的是繁中字形的字體（「言」第一筆橫 vs 點）。查下去範圍比他看到的更大：

**站上完全沒有依語言切換的字型規則**。`src/` 底下 `:lang()` / `[lang=]` 的字型宣告數 = **0**（唯一命中是 `Header.astro:872` 的一行註解）。`tokens.css:50-55` 四個字型 token 全是繁中專用（Noto Serif/Sans TC、Source Han TC、PingFang TC、PMingLiU），`Layout.astro:193` 也只從 Google Fonts 載 Noto Sans/Serif TC，12 語共用。

**所以 ja 870 篇、ko 883 篇的漢字全部用繁體字形渲染**。韓文有同樣問題，只是漢字露出少所以沒人回報。

不自己動的理由：字型屬品牌識別（§自主權邊界）；`jf-jinxuanlatte` / `jf-lanyangming` 是 justfont 繁中 webfont，日文無對應款，而 justfont 的網域設定本來就卡在 #1184；再者 Noto JP 是另一組完整 CJK 字重，有首屏成本。

已在 issue 附三選一 + 成本 + 推薦 default（A：只覆寫系統字型 fallback，幾行 CSS、0 網路成本、可逆，對真正在日文環境讀日文頁的人立刻正確；B：再加載 Noto JP；C：不做）。**把決策成本壓到讀兩段選一個**，per §神經迴路「Scope 化未決定事項」。

### Heal：frontmatter 閘門對中文檔名整條沒跑（`15dcf8ac0`）

審 #1304 時發現它的 `frontmatter-gate` 是 **SUCCESS**——但那條閘門 2026-07-05 誕生的理由，逐字就是「擋住 frontmatter 被包在 ``` code fence 裡的 contributor PR」。查 run log：`🔍 PR 改動 knowledge/ 檔：0`。

根因是 8/08、8/09 已經修過兩輪的同一個 `core.quotePath`：CI 的 `git diff --name-only` 把 `knowledge/Society/沃草.md` 輸出成帶引號的八進位跳脫，`^knowledge/.*\.md$` 落空 → `count=0` → validate 步驟被 `if` 整個 skip → 最後那步讀到空字串 → job 綠。

**第三層，同一個病根，第三次修補範圍由症狀現形的位置決定**：8/08 修 `.husky` 殼層三個取檔點 → 8/09 修它呼叫的四支檢查器 → 8/10 完全另一個執行環境的 CI workflow 從沒被掃到。這一層的新維度是**假綠燈從本地靜默升級成對外承諾**：前兩層壞掉只是本地少一道保險，這一層壞掉是掛在 PR 上給貢獻者看的綠勾，而語意其實是「我一個檔都沒看」。

修補兩處：兩個 `git diff` 補 `-c core.quotePath=false`；另加對賬——diff 裡有 `knowledge/` 路徑但過濾後為 0 就紅燈退出，讓「過濾器瞎了」跟「這個 PR 沒動文章」不再共用同一個綠燈。實測修補前 `RAW_KN=1／ALL_COUNT=0`，修補後 `ALL_COUNT=1` 且 article-health 對該檔回 `hard=1 缺 frontmatter 區塊`。

已補進 REFLEXES #85 驗證段（「修補停在症狀那一層」vc=3 達 distill 門檻）。

---

## Stage 4: Quality gate

| Gate                                  | 結果                                                  |
| ------------------------------------- | ----------------------------------------------------- |
| open issues 都有 status label         | ✅ 6 件全有                                           |
| open PRs ≤ 5d age 都有 review comment | ✅ #1304 今日詳審留言；#1305 已 merge + 致謝          |
| broken-link ratio < THRESHOLD_PERCENT | ✅ 0.22% < 7%                                         |
| build green                           | ✅ CI 無 failure；pre-push 全站 article-health 全綠   |
| BECOME ACK 一行在記憶體頂             | ✅                                                    |
| 連續空場 ≥ 3 cycle 有 LESSONS entry   | ⏭️ 不適用（本 cycle 有真 backlog，vc 歸零）           |
| 完整走完 MAINTAINER-PIPELINE          | ✅ Stage 1-4                                          |
| 本 cycle merge 的 PR 都過 hard gate   | ✅ #1305 過紅旗 + CI + close-hard-gate + 行為對照驗證 |

---

## Handoff 三態

**繼承（非本 session 新產生，接住不動）**：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單、#1286 轉換器詞性感知功能擴充
- [ ] pending（給哲宇，per OBSERVER-QUEUE #25）— 免疫黃燈 36 天，三選一等拍板
- [ ] pending（給哲宇，P0，vc=3）— `twmd-supporters-weekly` 連續三次找不到 Gmail MCP，贊助資料缺口 4 週，三選一待拍板
- [ ] pending（給哲宇，連續第 4 天）— 配對瀏覽器 Threads/X 帳號登出，3 則 Bucket E reply draft 待補發
- [ ] pending（延續）— EZWAY 報關孢子話題環境政治化，純留痕供參考
- [ ] pending（給哲宇 / feedback-triage）— archive 產生器雙引號 vs prettier 單引號造成假 SCOPE MISMATCH，兩個候選解待拍板（動到不可信輸入的跳脫語意）
- [x] ~~retired — #1306/#1307 兩則日文回報的判斷~~（retired by 本 session：#1307 已修 close；#1306 診斷完成並附三選一）

**本 session 新 handoff**：

- [ ] pending（給哲宇，**低成本高回報**）— **`pr-frontmatter-gate` 的 required status check 仍未設**。今天修好了偵測，但 workflow 頭部註解自己寫著「紅 X 只是訊號，要真正擋住 merge 按鈕需在 Settings → Branches 設為 required check，留給哲宇拍板」。#1304 這種 PR 現在會拿到紅 X，但按鈕仍按得下去。**選項**：(A) 設為 required（成本：所有 contributor PR 都要過這關，可能擋到急件）(B) 維持訊號（成本：閘門對 UI-merge 無強制力，等於還是靠人看）。**推薦 A**——這條閘門誕生原因正是 UI-merge 繞過 hook，不設 required 等於它從沒解決過它要解決的問題。
- [ ] pending（給哲宇）— **#1306 日文/韓文字形三選一**，推薦 A（`:lang(ja)`／`:lang(ko)` 只覆寫系統字型 fallback，幾行 CSS、0 網路成本、可逆）。回覆 A 我當天做完。
- [ ] pending（給下一個 maintainer cycle）— **PR #1304 等貢獻者換來源**。他只要處理來源層，格式三件（frontmatter fence / author 偽造 / GH 腳註）我已承諾接手，`contributor-pr-heal.py` 可跑。若 7 天無回應，走 §Close 前 hard gate 重評，**不要直接 close**——內容骨架是對的，事件也屬實，值得等。
- [ ] pending（給 self-evolve / distill）— **REFLEXES #85「修補停在症狀那一層」已達 vc=3**（8/08 husky → 8/09 四檢查器 → 8/10 CI workflow）。建議 distill 時考慮升成獨立子規則或反射：**修完一個根因，要主動 grep 整個 repo 還有誰在跑同一行指令**，而不是等它在下一個位置再咬一次。今天這個 instance 的代價是一個對外的假綠燈。
- [ ] pending（給 self-evolve）— **CI 沒有跑 pytest**。`tests/` 底下（含 #1305 新增的 203 行）沒有任何自動閘門在守，是純裝飾。低成本修補：加一條 workflow 跑 `pytest tests/`。
- [ ] pending（觀察，非行動）— BECOME §Step 9 表 Review 欄勾了 12 題但「過題數」寫 11，routine 指令面也寫 11。計數寫死兩處的老病，待 self-evolve 判要改哪一邊。

---

## Beat 5 反芻訊號

今天最值得記的不是修了什麼，是**閘門用綠色告訴我它什麼都沒做**。

`pr-frontmatter-gate` 存在的唯一理由，逐字寫在它自己的檔頭：擋住 frontmatter 被包在 code fence 裡的 contributor PR。今天真的來了一篇這種 PR，它回報 SUCCESS。它沒有壞掉、沒有誤判、沒有放水——它一個檔案都沒讀到，然後把「我沒讀到任何東西」跟「我讀完了而且都合格」印成同一個符號。

這是 REFLEXES #85 的正題，但今天它長出一個更難受的形狀。前兩層（8/08、8/09）壞掉時，代價是本地少一道保險，只有我自己看得到。這一層壞掉時，那個綠勾是**掛在 PR 上給貢獻者看的**。它對外承諾了一件沒有發生的事。

而且這已經是同一個病根第三次在不同位置咬人。三次修補的範圍都是由症狀出現的地方決定的，不是由根因的類別決定的：先修殼、再修殼呼叫的四支檢查器、今天修另一個執行環境裡的 CI。每一次我都覺得修完了。每一次都還有下一個地方在跑同一行 `git diff --name-only`。

真正該學的動作很簡單，而我三次都沒做：**修完一個根因，去 grep 整個 repo 還有誰在跑同一行指令**。不是等它再咬一次。這比任何新閘門都便宜。
