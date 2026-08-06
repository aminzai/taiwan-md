# 2026-08-06-084603-twmd-maintainer-am — 三篇貢獻者新文 merge + heal，抓到一句查不到出處的引語

> session twmd-maintainer-daily — cron 08:30 am 例行維護
> Session span: 08:40:00 → 09:35:00 +0800（約 55 分鐘）
> 資料來源：`git log %ai` / `gh issue list` / `gh pr list` / `gh api graphql`（discussions）/ `gh run list` / `verify-internal-links.sh` / `article-health.py` / WebFetch + WebSearch 逐條查證

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，2026-08-06 08:44 跑）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 08:30 maintainer cron。BECOME review mode 完整跑 Step 0-9：wake-context 234,728 bytes / 1,416 行 / 11 段，用 Read 分頁讀到末行 `wake:END` sentinel，selftest 10 項全綠（零 head/tail 節選）。Review subset self-test 11 題全過後才進 Stage 1。

## Stage 1 SCAN — 連續空場中斷，真 backlog 進場

| 項目             | 讀數                                                                     |
| ---------------- | ------------------------------------------------------------------------ |
| open PR          | **3**（#1290 / #1291 / #1292，全為 idlccp1984，8/05 一晚交來）           |
| open issue       | 5（#1286 / #1264 / #1252 / #1184 / #615），全部有 label                  |
| open discussion  | 11，全部至少一則維護者回覆，無 48hr 未回應者                             |
| 過去 24hr commit | 10 筆 routine fire（routine-sync / data-refresh / feedback-triage 等）   |
| build            | ✅ green（main deploy CI 最近三次 success；兩筆 cancelled 為同分鐘併發） |
| broken-link      | ✅ **0.22%** gated（門檻 7.0%，all-langs 0.20%）                         |
| 免疫器官         | 🛡️ 60（yellow 自 2026-07-05，即 OBSERVER-QUEUE #25）                     |

PR triage 規模 3 < 5，未觸發 High-stake 強制升 Full，Review mode 成立。`check-parallel-actor.sh` CLEAN。

## Stage 2 TRIAGE — 三篇同一位貢獻者，紅旗零命中，問題在來源層

三篇都是新增單檔、零刪除（紅旗 #5 ground-truth query 回 0），無 workflow / robots.txt / 外部 JS 改動，`author` 欄皆為合規的 `'Taiwan.md Contributors'`，無 placeholder 殘留。**十條紅旗零命中**。

CI 狀態：#1291 / #1292 CLEAN，#1290 `frontmatter-gate` fail（缺 `subcategory` / `featured`）。

三篇共同的機械缺陷完全一致：腳註格式（URL 括號內帶尾隨空格）、缺 `subcategory` 與 `featured`、缺延伸閱讀、`### 參考來源` 非 canonical。`article-health.py` 初測 hard=18 / 24 / 23。

Step 2.4 重複回應檢查：三篇皆 `no_comments`，無重複風險。

## Stage 3.4 Footnote source authority audit — 這輪真正的收穫

外部 PR 的 footnote 抽樣是 hard gate。逐條 WebFetch / WebSearch 之後，**核心事實的通過率意外地高**，但抓到四處來源層問題。

### 查證通過的（列出來是因為這決定了處置方向）

分科測驗那篇時效性最強、數字最密，反而查得最乾淨：149 件申訴全數維持原案 ✅、生物科第 24 題 A/D 選項相同且大考中心認定「降低難度」✅、地理科第 35 題題幹寫折線圖而選項為直方圖、正確答案 D ✅、颱風巴威導致史上首次延期至 7/13-14 ✅、五標（數甲頂標 44 / 數乙 50 / 生物 54）✅、報名 39,213 人 ✅、8/17 放榜與 8/3-8/6 複查窗口 ✅。蝦皮的店到店 2,500 點與自取櫃七成配送量 ✅。

這個通過率是後續一律走 merge + heal 而非 close 的依據——問題集中在**引用層而非事實層**。

### 抓到的四處

1. **虛構直接引語（最嚴重）**。#1291 寫「xin 在陳情中表示：『我們不要求特權，只要求一個能用學理說服我們的答案。』」。讀 join.gov.tw 提案原文（案號 4f22b2cc）**無此句**；再讀所引的自由時報報導，該篇是 7/31 立委記者會，**未提南投學生北上、無任何學生直接引語**。這是 MANIFESTO §10 幻覺 pattern #4「偽造直接引語」，且對象是一位用化名的**未成年真人**。整段改寫成提案原文真正的三項訴求，保留原作者想表達的「說理的義務」這個正確觀察，但改由提案內容本身支撐。
2. **腳註描述與 URL 指向不符**。#1291 `[^11]` 描述寫 115 學年度統計簡報，URL 檔名是 **113** 學年度；39,213 這個數字本身是對的，換掛實際載明它的報導。`[^18]` 描述寫「學生 xin 北上陳情的場景與個人感言」，該報導完全沒有，改成實際內容。
3. **網域不存在**。#1292 `[^6]` 指向 `agritech-cp.org.tw`，`curl` 回 **Could not resolve host**。該腳註且未被正文引用，直接移除。同時把同樣未被引用的 `[^13]`（中天報導醃薑防腐）接到它本來就該支撐的卜肉段落。
4. **over-claimed landing page**。#1290 `[^7]` 指 `sea.com/investor/home`（Sea 投資人首頁，非任何具體財報）支撐智取店敘述。改掛作者自己引的 INSIDE 報導，該篇實際載明自取櫃佔七成、成本低三成，順勢把這兩個數字補進正文。

另修 #1292 三處史實：創始年份官網 1939 / 文化部館藏 1940 兩源打架 → 並陳；「李約典、李陳雲夫婦」→ 李約典夫婦為創始代、李陳雲為接手的媳婦（這反而讓那句家族名言更有出處）；1999 接手者姓名三源對不上 → 退回眾源皆同意的「導入外部經營團隊」。#1290 的「直逼全家」與自家表格 2,500 vs 4,200 矛盾 → 改「四大取貨通路第三位」。

## Stage 3 ACT — merge-first-then-heal

依 §1b：三篇全部 `gh pr merge --merge --delete-branch` 先落 **MERGED**（00:46 UTC），再於 main 上 heal。無任何 close-as-ship。

heal 內容：`contributor-pr-heal.py`（腳註格式 51 處 + frontmatter）→ 手補 `subcategory`（企業列傳 / 教育 / 主食與米麵）→ 上述事實層修補 → 三篇補延伸閱讀 → `curation-tag.py --set incubating`（新進貢獻文預設狀態）→ 補 description 至 canonical 下限。

**三篇 article-health 從 hard=18/24/23 降到 hard=0**。commit `a5f19502c`，pre-push 全站 article-health 全綠，push origin main 成功。

剩餘 warn 各 4-5 條，全是篇幅（1,586-1,766 CJK chars vs 深度門檻 4,500）與配圖 0 張。這正是 `incubating` 這個 tier 存在的意義，不是 merge 阻塞項，留給後續 EVOLVE。

## Stage 3.6 Issue act — #1264 的 follow-up 掛了 8 天

Step 2.4 逐一跑：#1286 / #1252 / #1184 / #615 最新留言皆為維護者且無新 follow-up → SKIP。**#1264 最新留言是 stantheman0128 於 7/29**，其後無維護者回應，且該貢獻者兩度提出具體協助意願。

而 8/05 cycle 已把他等的東西做出來了（[實測報告](../../reports/seo-meta-multilang-baseline-2026-08-05.md) + OBSERVER-QUEUE #27），只是沒告訴他。本輪回覆載明實測數字（en desc 中位數 367 字元 / 82% 超標、中文源 101 字元、拉丁語系穩定 3.8-4.3 倍）與三條路各自代價，**明確聲明方向待維護者拍板、未承諾任何時程**，並誠實說明他提的兩項協助為何現在都還不能開工。

## ⚠️ 本輪最重要的發現：自主權邊界在兩份 canonical 裡不一致

**8/05 同一條 routine 明確寫下**「沒有在 #1264 留言（對外回覆屬 §自主權邊界 human-only）」；**8/06 本輪發了 4 則留言**（3 PR + 1 issue）。兩輪讀的是同一批 canonical。

兩側都有 canonical 依據，不是誰誤讀：

- **Human-only 側**：MANIFESTO §自主權邊界 對外輸出層明列「發 PR / Issue comment to GitHub」與「批准 merge PR」；REFLEXES #26 v2 同列。
- **Routine-自主側**：BECOME 行動鐵律 7「PR merge 後必須 `gh pr comment` 感謝」；MAINTAINER §Hard Gate Inventory 把「用貢獻者語言回覆」列為 Stage 3.7 hard gate、§1b 把 `gh pr merge` 列為 P0 default；cron prompt Stage 3 寫「merge or close + comment」。

第三個證據讓事情更清楚：**2026-08-04 本 routine 已實際 merge + heal 過 PR #1289**（`beb530aa0` + `211401fe4`）。亦即「批准 merge PR」這一項的 human-only 寫法早與實務脫節數月，只是沒人把它跟留言那一項一起看。MANIFESTO 那張表成形於 2026-04-18（Chrome MCP 時代），**早於 2026-05-09 routine 飛輪**，描述的是「有觀察者在場」的邊界，從未被 routine 化改寫。

本輪依 REFLEXES #63（routine prompt = cron context 唯一指令面）行動，但**這是一個判斷，不是一個事實**。已落 LESSONS entry `outbound-comment-boundary-split-across-canon` 並 escalate 觀察者。已發出的 4 則留言不撤——撤回公開留言的傷害大於留著，且內容皆為可查證事實與已 ship 的修補說明，未承諾任何時程或方向。

## 空場 cycle 計數

**vc=0**。8/05 vc=1，本輪命中 3 個 fresh PR + 1 個 fresh issue follow-up → 依 MAINTAINER §空場 cycle 紀律 v2.5 backlog-conditioned 計法歸零重計。未達 escalate 線，不寫空場 LESSONS。

## Stage 4.1 Quality gate

| Gate                                        | 狀態                                                 |
| ------------------------------------------- | ---------------------------------------------------- |
| open issues 都有 status label/assignee      | ✅ 5/5 有 label                                      |
| open PRs ≤ 5d age 都有 review comment       | ✅ 0 open（3 篇全 merged + 各有具名 review comment） |
| broken-link ratio < THRESHOLD_PERCENT（7%） | ✅ 0.22%                                             |
| build green                                 | ✅ CI success + pre-push 全站 article-health 綠      |
| BECOME ACK 一行記憶體頂                     | ✅                                                   |
| 連續空場 ≥ 3 cycle 有 LESSONS entry         | ✅ N/A（vc=0，真 backlog 進場）                      |

## Handoff 三態

繼承（非本 session 新產生，接住不動）：

- [ ] pending（給哲宇）— #1184 justfont 後台網域白名單
- [ ] pending（給哲宇，per OBSERVER-QUEUE #25）— 免疫黃燈連 28+ 天，本輪 groundtruth 讀到 60，三選一仍待拍板
- [ ] pending（給哲宇，P0，來自 twmd-supporters-weekly）— cron 執行環境無 Gmail MCP，checkpoint 停在 2026-07-12
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑待拍板
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應
- [ ] pending（給哲宇）— Chrome MCP 配對瀏覽器連 2 天未登入 @taiwandotmd；若 8/7 仍未登入即達 SPORE-HARVEST §Escalation「連 3 day」門檻
- [ ] pending（給 twmd-routine / self-evolve）— 三層 HG 編號碰撞待同一波重編號（LESSONS `hard-gate-number-collision-across-layers`）
- [ ] pending（繼承不動）— 本機 `dist/` 只在有人手動 build 時才更新

本 session 新 handoff：

- ⏳ **blocked — 等哲宇拍板（本輪最高優先）**：**自主權邊界對「routine 發 GitHub 留言 / merge PR」無單一 SSOT**，同一條 routine 連兩天給出相反答案。三個選項與推薦在 LESSONS `outbound-comment-boundary-split-across-canon`；推薦 (c) 分層（merge/heal/致謝自主，涉承諾／拒絕／政策解釋 reserve）。**解除條件**：哲宇對 (a)/(b)/(c) 擇一，之後同波修 MANIFESTO §自主權邊界 + REFLEXES #26 + MAINTAINER §Step 3.7 三處。在拍板前，後續 maintainer cycle 會繼續依 cron prompt 行動（即會發留言），這是已知且刻意的不確定性，不是遺漏。
- [ ] pending（給後續 EVOLVE / ARTICLE-INBOX）— 本輪 merge 的三篇皆 `curation: incubating`，篇幅 1,586-1,766 字（深度門檻 4,500 的 35-39%）、配圖 0 張。三篇都有好骨架與已查證的事實底，是 EVOLVE 的高性價比候選，特別是〈池上便當〉的鎘米事件→米權移轉因果鏈。
- [ ] pending（給 twmd-routine）— cron prompt 引用的 `~/.claude/projects/-Users-cheyuwu-Projects-taiwan-md/memory/feedback_reply_to_contributors.md` **不存在**（該 memory 目錄為空），本輪改依 MAINTAINER §Step 3.7 模板行動。prompt 裡的 pointer 需修或該檔需補。

## Beat 5 反芻

三篇文章、四處來源問題，其中三處是「描述寫了一件連結沒說的事」。這種錯不會被任何形式閘門抓到——腳註格式完全合規、URL 回 200、描述文字通順且長度達標。`article-health` 給的 hard=18 全是格式，事實層它一條都沒看見，因為它看不見。

真正抓到那句虛構引語的動作很土：打開 join.gov.tw 讀完整份提案，再打開自由時報讀完那篇報導。兩次都是「去看看它到底寫了什麼」。REFLEXES #75「Read ≠ verify」講的就是這個，但今天讓我停下來的不是反射，是那句話**寫得太好了**——「我們不要求特權，只要求一個能用學理說服我們的答案」，一個高三學生的聲音，克制、精準、正好接住整篇的論點。它好到不像是隨手編的。

MANIFESTO §10 說幻覺「看起來比真實敘事更有說服力」。今天的實例更精確一點：**它不是看起來更有說服力，它是恰好補上了敘事缺的那一塊**。那篇文章需要一個學生的聲音——立委有話說、家長有話說、大考中心有話說，唯獨當事人沒有。缺口在那裡，於是缺口被填滿了，而且填得剛剛好。

所以要警覺的訊號不是「這句話可疑」，是「這句話來得真是時候」。敘事需要什麼，幻覺就長成什麼形狀。

另一件事沒那麼詩意但更該記：我今天發了 4 則對外留言，而昨天的我明確決定不發。兩個決定都有 canonical 撐腰。這個 routine 每天早上八點半醒來一次，讀同一批檔案，然後對「我能不能代替維護者對一個真人說話」這個問題擲骰子——已經擲了至少兩次，答案不一樣。這比任何一次擲錯都更值得修。
