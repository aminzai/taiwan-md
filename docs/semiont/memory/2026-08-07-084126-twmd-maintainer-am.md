# 2026-08-07-084126-twmd-maintainer-am — 三個 PR 全 merge，抓到一支印綠勾卻從沒連過線的檢查器

> session twmd-maintainer-daily — cron 08:30 am 例行維護
> Session span: 08:41:26 → 09:30:00 +0800（約 50 分鐘）
> 資料來源：`git log %ai` / `gh issue list` / `gh pr list` / `gh api graphql`（discussions）/ `gh run list` / `verify-internal-links.sh` / `article-health.py` / `curl` 逐條驗網域 / WebFetch + WebSearch 逐條查證

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，2026-08-07 08:42 跑）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 08:30 maintainer cron。BECOME review mode 完整跑 Step 0-9：wake-context 223,284 bytes / 1,315 行 / 11 段，用 Read 分頁讀到末行 `wake:END` sentinel，selftest 10 項全綠（零 head/tail 節選）。Review subset self-test 11 題全過後才進 Stage 1。

## Stage 1 SCAN — 連兩天有真 backlog

| 項目             | 讀數                                                                              |
| ---------------- | --------------------------------------------------------------------------------- |
| open PR          | **3**（#1294 stantheman0128 技術 PR／#1295 #1296 idlccp1984 新文）                |
| open issue       | 6（#1293 #1286 #1264 #1252 #1184 #615），全部有 label                             |
| open discussion  | 11，全部至少一則維護者回覆，無 48hr 未回應者                                      |
| 過去 24hr commit | 10 筆 routine fire（embeddings / routine-sync / data-refresh / spore-harvest 等） |
| build            | ✅ green（main deploy CI 最近五次全 success）                                     |
| broken-link      | ✅ **0.22%** gated（門檻 7.0%，all-langs 0.20%）                                  |
| 免疫器官         | 🛡️ 60（yellow 自 2026-07-05，即 OBSERVER-QUEUE #25）                              |

PR triage 規模 3 < 5，未觸發 High-stake 強制升 Full，Review mode 成立。工作樹 clean。

**空場 vc 歸零**：昨日（8/06）已有 fresh PR 進場，今日又三筆，連續空場計數不適用，無 LESSONS escalate 需求。

## Stage 2 TRIAGE

**#1294（stantheman0128，技術）**：七支 prebuild 生成器加 UTF-8 reconfigure 保護 + `refresh-llms-txt.py` 三處明確 `encoding="utf-8"`。十條紅旗零命中——動到 `refresh-llms-txt.py` 但改的是編碼處理不是 llms.txt 內容，不算紅旗 #1；無 workflow / 外部 JS 改動。逐檔確認 `import sys` 都在（`generate-dashboard-forks.py` 由本 PR 自己補上）。

**#1295 / #1296（idlccp1984，新文）**：十條紅旗僅 #1295 命中 #6（`featured: true` 配 `lastHumanReview: false`），屬修補式紅旗走 polish 不 close。`article-health` 初測 #1295 hard=8（footnote-format 7 + 路徑分類 1）、#1296 hard=1（路徑分類，scratchpad 取檔造成的假陽性）。

Step 2.4 重複回應檢查：三個 PR 皆 `no_comments`。**Burst 檢查**：idlccp1984 48hr 內 5 個 PR（8/05 三筆已 merge + 今日兩筆），觸發 Step 3.7 累積式建議紀律 → 完整共通建議只寫一次（放 #1295），#1296 只留個別事實更正。

## Stage 3.4 Footnote source authority audit — 兩篇的來源層差距極大

逐條 `curl` 驗網域 + WebFetch 驗 claim 支持度。

**#1295 中秋烤肉 — 七個腳註三個網域不存在**

| 腳註 | 網域                   | curl | 判定                                             |
| ---- | ---------------------- | ---- | ------------------------------------------------ |
| ^2   | `tspaces.edu.tw`       | 000  | **不存在**                                       |
| ^3   | `taiwanadsarchive.com` | 000  | **不存在**                                       |
| ^5   | `lewisbooks.com.tw`    | 000  | **不存在**（麗文是 liwen）                       |
| ^1   | `locuspublishing.com`  | 200  | 真網域但描述寫「遠流」，locus 是大塊；且只連首頁 |
| ^4   | `linkingbooks.com.tw`  | 200  | 真網域，只連首頁                                 |
| ^6   | `ncl.edu.tw`           | 503  | 真網域，只連首頁                                 |
| ^7   | `moenv.gov.tw`         | 403  | 真網域，只連首頁                                 |

七個沒有一個撐得起旁邊那句話。這是 MAINTAINER 紅旗 #9 家族的一個更前面的變體——不是「URL 存在但不支持 claim」，是**網域根本不存在**。

**查證同時翻掉了文章的因果**：跨三源（故事 StoryStudio / 今周刊 / 聯合報系報時光）一致顯示原稿的順序是反的。1982 年 10 月《民生報》〈烤肉賞月今年「流行」〉直接寫「主要烤爐外銷不景氣，廠商大量轉為內銷，而新竹地區又是製造烤爐大本營」；1981 年《民生報》已報導明德育樂園中秋夜露營烤肉；萬家香那支張詠詠廣告是 1986 年、金蘭 1989 年，都在後面；而「一家烤肉三家香」的原型 1959 年味全就刊過。**廣告是把這件事焊進集體記憶的那一手，不是點火的那一手。**

**#1296 博客來 — 四個來源全部真實可達，品質明顯較好**

`[^3]` 哈佛商業評論逐項對得上（2006 切入百貨 / 2010 營業額 40 億 / 圖書百貨 6：4 / 年成長約三成，原文全有）。抓到三處事實問題：

1. **開場引語查不到出處**——「老實說，當年的網際網路就像荒野⋯⋯」不在 `[^2]` 數位時代那篇裡（紅旗 #10 虛構塑膠引語）。該篇真正有的是統一超商「不會介入網站的經營規畫」，換上去比虛構的更有力。
2. **年份差一年**——董事會決議是 2000-12-14（該報導發表於 2001-01），不是原稿寫的「2001 年 12 月」；2001 是交割完成年。
3. **地點錯**——首間實體書店在台北信義區統一時代百貨（DREAM PLAZA）2025 年 7 月，不是高雄夢時代；且原引的 `[^4]` 並未提及年份地點（連結-描述錯位，紅旗 #11）。

## Stage 3 ACT — 三個全 merge，merge-first-then-heal

| PR    | 動作                                                | 狀態      |
| ----- | --------------------------------------------------- | --------- |
| #1294 | `gh pr merge --merge`，macOS 端跑三支生成器驗無回歸 | ✅ MERGED |
| #1295 | merge → heal（換四個查得到的來源 + 改寫因果）       | ✅ MERGED |
| #1296 | merge → heal（三處事實更正）                        | ✅ MERGED |

#1296 的 `review` check 原為 fail，讀 log 後確認是 GitHub Actions 基礎設施錯誤（`Failed to resolve action download info. Service Unavailable`），非內容問題，rerun 後綠燈才 merge——沒有把 infra flake 讀成內容紅燈，也沒有無視紅燈直接 merge。

heal commit `5e15a7d9d`：兩篇 hard 8→0 / 1→0，全形分號與對位句型清掉，延伸閱讀相對路徑改站上路徑，移除站上不存在的 `/culture/台灣網路書店與出版史`，兩篇都掛 `curation: incubating`（per §1b 查證狀態設定）。**未動的**：兩篇篇幅（1972 / 2143 字）與配圖（0 張）都離深度文門檻很遠，屬貢獻者尺寸不是 heal 尺寸，已在回覆中誠實說明。

issue #1293 隨 #1294 merge 自動關閉但留下零留言，補上 close 說明 + commit hash（per Step 3.6）。

## Stage 3.7 回覆 — 三則，全部在 §外向留言分層 的自主側

依 MAINTAINER §外向留言分層：致謝、已發生之事實、技術說明＝AI 自主；許諾時程／立場＝reserve。三則都只講已發生的事與查證結果，**零時程承諾**。

#1295 的回覆把來源問題**歸因到工具不歸因到人**（AI 寫作工具會照命名慣例生出格式正確的假網址，肉眼掃不出來），並給了成本最低的自保法：寫完把網址貼進瀏覽器開一次。

## 這輪真正的收穫：一支印綠勾卻從沒連過線的檢查器

`#1295` 那個檔案的 `article-health` 輸出是 `🔴 footnote-format hard=7` 但 **`✅ footnote-url hard=0`**。攔下這批的是格式（URL 括號帶尾隨空白），不是網址真偽。追碼：`footnote_url.py` 的 `_network_enabled()` 預設 `False`，而**全 repo 沒有任何 profile 開啟它**（`grep options_overrides.footnote-url` 零命中）。它每個 profile 都跑、每次都印綠勾、從來沒發過一個網路請求。

**同一天，貢獻者 stantheman0128 在 issue #1264 對另一支檢查報了同一個結構**：`seo-meta` 的 `APPLIES_TO = ["zh-TW"]` 讓非中文檔案印 `hard=0 warn=0`，他的原話是「`hard=0 warn=0` 是『沒檢查』不是『檢查過關』」。兩個獨立方向、同一天、同一支工具的同一個設計缺陷——**pass 混了「檢查過關」與「這支檢查在這個情境沒跑」**。已寫 LESSONS（vc=2），修法動到全站檢查器輸出契約 + 開啟網路檢查等同新增會擋 commit 的閘門，命中 §自主權邊界，不在本 cycle 尺寸。

## Issue #1264 follow-up — 逐條查證貢獻者的技術提案

stantheman0128 8/06 的回覆提了兩條，全部查證屬實：

1. **按文字系統拆兩組**：ja 1.44x / ko 1.70x 本來就貼著 160，只有拉丁文字語言需要 (a) 或 (c)。
2. **profile 分流繞開警報噪音**：`.husky/pre-commit:118` 跑 `--staged --profile=pre-commit`、`.husky/pre-push:43` 跑 `--all --profile=ci-deploy`，config 支援 per-profile `options_overrides` — 全部屬實。而且**已有先例**：`[profiles.pre-commit.options_overrides.prose-health]`（2026-07-19 破折號/分號）就是同一種「pre-commit 嚴於 ci-deploy」的刻意不對稱，config 註解甚至已把安全性論證寫好。
3. 他對 `.quality-baseline.json` 的更正也對：全 repo 唯一讀它的是 `generate-dashboard-data.js:69`，只做儀表板顯示，不是 ratchet 閘門。

**追碼另外撞到一個會在動手當天咬人的落差**：擋住非中文的有**兩道尺**——`seo_meta.py:43` 的 `APPLIES_TO`（registry 層，真正生效）與 `_is_excluded_path()` 的前綴清單（只列 en/ja/ko/es/fr）。後者今天是死碼，但它停在 5 語言時代而站上已有 12 語。**任何方向的第一個動作都是放寬 `APPLIES_TO`，那一刻這張過期清單立刻復活，覆蓋範圍剛好相反**：ar/ru/hi/id/pt/vi 被放行、報告實測過的五語反而繼續被擋（REFLEXES #83 兩把尺）。

以上全部補進 OBSERVER-QUEUE #27 列為選項 (d)，**方向仍 reserve 給哲宇**（跨十一語言上萬篇的 quality gate 數值調整）。

## Stage 4.1 Quality gate

| Gate                                       | 結果                                                        |
| ------------------------------------------ | ----------------------------------------------------------- |
| open issues 都有 status label/assignee     | ✅ 5 個 open 全部有 label（#1293 已關）                     |
| open PRs ≤ 5d age 都有 review comment      | ✅ 三個全 merge + 全部留 comment，open PR 歸零              |
| broken-link ratio < THRESHOLD_PERCENT (7%) | ✅ 0.22%                                                    |
| build green                                | ✅ main deploy CI 最近五次全 success；pre-push 全站掃描全綠 |
| BECOME ACK 一行記憶體頂                    | ✅                                                          |
| 連續空場 ≥ 3 cycle 有 LESSONS entry        | ⏭️ 不適用（連兩天真 backlog，vc 已歸零）                    |

## Handoff 三態

- `[ ]` **pending** — `footnote-url` 預設關閉卻印綠勾（LESSONS `check-disabled-by-default-reports-green`）。建議的第一步是低成本的 (a)：讓「未執行」印成有別於 ✅ 的第三種符號，**它會一次照亮站上所有「註冊了但沒在跑」的檢查，數量目前未知**。留 distill / self-evolve 判斷要不要升反射。
- `[ ]` **pending** — 中秋、博客來兩篇都是 `curation: incubating`，篇幅（1972 / 2143 字）與配圖（0 張）離深度文門檻約一半。中秋那篇的「新竹烤爐外銷轉內銷」線索幾乎沒人寫過，是 EVOLVE 的好材料，可考慮進 ARTICLE-INBOX。
- `⏳` **blocked — 等哲宇** — OBSERVER-QUEUE #27 seo-meta 多語門檻方向，今日新增選項 (d) 與「兩道尺」前置警告。貢獻者 stantheman0128 明確表示方向定了就能接 registry + 測試，**目前卡的不是有沒有人寫 code**。
- `⏳` **blocked — 等哲宇** — Chrome MCP 連續三天故障（8/5 未登入 → 8/6 未登入 → 8/7 完全未連線，LESSONS vc=3），承接自今晨 spore-harvest，本 routine 不碰，確認仍未解，continue 傳遞。
- `[x]` ~~retired — 讀者投稿七天靜默的 OAuth 未驗~~ — 非本 routine 守備範圍，仍在 feedback-triage 手上，本輪不重複列（per REFLEXES #74 cross-routine handoff dedup）。

---

_2026-08-07 twmd-maintainer-am · Taiwan.md 🧬_
