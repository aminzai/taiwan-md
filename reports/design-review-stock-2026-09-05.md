---
title: 'Design: 審閱庫存 routine + 讀者複核頁'
description: 'EVOLVE Mode 4 設計報告：治「沒有人在審庫存」。新 routine twmd-review-stock 做 Semiont 預審，新頁 /semiont/review-queue 讓登入讀者複核，三方案發散與定案理由，欄位設計不動 curation 三態既有語意。'
type: 'design-report'
status: 'draft'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-154128-fortnight-review'
related:
  - '../reports/fortnight-deep-review-2026-09-05.md'
  - '../docs/pipelines/EVOLVE-PIPELINE.md'
  - '../docs/semiont/ROUTINE.md'
  - '../docs/pipelines/FACTCHECK-PIPELINE.md'
  - '../docs/editorial/EDITORIAL-ROOM.md'
  - '../docs/pipelines/MAINTAINER-PIPELINE.md'
  - '../reports/design-curation-tier-2026-08-04.md'
  - '../reports/feedback-login-system-design-2026-06-01.md'
  - '../scripts/core/generate-dashboard-immune.py'
  - '../docs/semiont/MANIFESTO.md'
  - '../docs/semiont/REFLEXES.md'
  - '../docs/semiont/OBSERVER-QUEUE.md'
---

# 審閱庫存 routine + 讀者複核頁設計

> EVOLVE-PIPELINE Mode 4 REPORT 相。觸發：哲宇 2026-09-05 在兩週深度體檢 session 對 OBSERVER-QUEUE #25 拍板選 A「社群 reviewer 頁 + Semiont 預審 routine」。本報告把這個方向具體化成可派工的規格，命中 §自主權邊界的地方停在這裡等哲宇簽字，其餘直接列進實作清單。

## 一、目標與為什麼是現在

讓「審一篇既有文章」變成一件有人（有 routine）真的在做的事。免疫器官黃燈已經連續 62 天，拖底的兩個子維度連跌六週：`review_coverage` 從 23.4 掉到 19.2，`external_rulers` 從 3.3 掉到 2.2，是有紀錄以來最低。更具體的形狀是：`lastHumanReview: true` 的中文文章數鎖在 202 篇整整兩週沒有動過，T1 高風險分類 493 篇文章只有 102 篇被審過。這兩週內真正接住事實錯誤的三次，全部是讀者主動抓到，不是任何內部流程。

根因不是缺工具，是缺職責。maintainer 審的是進料口的 PR，審完就 merge。rewrite 重寫的是決定要重寫的文章。feedback-triage 轉錄的是讀者主動回報的問題。沒有一條 routine 的 stage 裡寫著「拿一篇已經在站上的文章，逐條查證後蓋章」。庫存從來沒有人巡邏過。

## 二、現況盤點

### 2.1 資源地圖：哪些東西已經存在，可以直接借

**curation 三態**（`reports/design-curation-tier-2026-08-04.md`，2026-08-04 定案）：文章頁投影三態，🔎 `verified`（已深度查證）、無標示（一般）、🌱 `incubating`（進化中，社群貢獻待查證）。判定看流程不看作者。轉正規則寫在 `MAINTAINER-PIPELINE.md` §1b：文章走完 REWRITE Evolution 深度或 FACTCHECK Full Mode 後，`curation: verified` 與 `lastHumanReview: true` 兩欄一起動。徽章只認 `curation: verified` 顯式值，不從 `lastHumanReview` 推導，原因是早期低標準時代的 `lastHumanReview: true`（如洪醒夫，697 字 0 腳註仍標人審過）拿來推導會變假保證，落地時已經修過一次這個坑。目前站上只有 2 篇文章走完整條流程被標 `verified`，其餘 95 篇是 `incubating`。工具面：`curation-tag.py` 可以批次或單檔設值，但**不會自動同步 `lastHumanReview`**，這欄要另外手動確認。`curation_consistency.py`（article-health plugin）看守三件事：取值合法性（HARD）、`incubating` 與 `featured` 互斥（HARD）、`verified` 應同步 `lastHumanReview`（WARN，非強制）。

**v1.9 讀者登入與 Supabase 架構**（`reports/feedback-login-system-design-2026-06-01.md`，2026-06-01 上線）：主站維持 100% 靜態 GitHub Pages，登入與資料寫入整塊放在 Supabase（Postgres + GoTrue Auth），Google One-Tap 為主、Apple/GitHub/Email magic-link 為輔，`FeedbackWidget.astro` 是既有的登入與送出元件。既有 `feedback` 表（`display_name` / `status` / `body` …）走 RLS：登入者只能寫自己的列。每天一條 `twmd-feedback-triage` routine 用 service key 讀 Supabase REST、把 `status='new'` 的回報轉成 GitHub issue，寫回狀態。這條基礎設施可以整塊借用：讀者複核頁用同一個 Supabase project，同一套 auth 元件，只需要新增一張表。

**FACTCHECK Quick / Full Mode**（`docs/pipelines/FACTCHECK-PIPELINE.md` v2.0）：Quick Mode 30-60 分鐘、5-10 次 WebFetch，抽樣 Phase 2-4，Hard Gate 是 0 個 ❌ HARD-FIX + 0 個 🔴 DEAD-LINK 才過，產出附進 `reports/research/YYYY-MM/{slug}.md` § audit 段。Full Mode 90-180 分鐘、25+ 次 WebFetch，全量 atom 逐條 verbatim 驗證，通常配 A 級文章或月度巡邏，spawn agent 執行。升 Full 的條件之一是 Quick 過程中發現 ≥3 個 ❌。

**冷讀席**（`docs/editorial/EDITORIAL-ROOM.md` v1.2 §總編室）：既有機制是「Sonnet ×5-6 平行探針，各自乾淨 context，禁讀藍圖與研究報告，只拿成品加標題」，模擬一個第一次讀的總編：這篇作為報導成不成立。探針包含門面兌現、逐段主軸服務、H2 載體還原、連結成網、閱讀節奏。結構主編那席另外問一題「光讀 H2 目錄，外行知不知道每段在看什麼」。這整套「假裝自己沒讀過」的機制現成可以借來對既有文章做一次性複查，不需要重造。

**免疫產生器**（`scripts/core/generate-dashboard-immune.py`）：`review_coverage` 是 tier 加權（T1×3／T2×1.5／T3×0.5）的 `lastHumanReview: true` 覆蓋率，權重佔免疫總分 0.25。`external_rulers` 同樣 tier 加權，權重 0.10，定義是 90 天內被「(a) `reports/factcheck/**/{文章}.md` 這種 Full Mode 報告」或「(b) commit message 含勘誤／errata／fact-fix 且單次改動 ≤5 篇 zh 文章」這兩種**獨立外部尺**碰過的文章。這個定義目前完全不含「讀者按過確認」這個來源，這正是本設計要補的缺口：讀者本人就是最貨真價實的外部尺。

**不存在的東西**：`reviewGate` 或任何審閱狀態欄位、`article_confirmations` 表、`twmd-review-stock` routine、`/semiont/review-queue` 頁，全部要新建。`agent-report-health` 這個名字在 repo 裡沒查到對應工具或器官，猜測是指 REFLEXES #31（agent claim 不可信）或 #69（自評需要外部尺）這兩條既有反射，本設計沿用這兩條反射的精神但不引用一個不存在的工具名。這點放進最後的不確定清單，若哲宇指的是別的東西需要補充。

### 2.2 cross-ref 掃描：改「升 verified 的判準」會動到誰

`grep -rl curation scripts/ src/ docs/`（排除 `src/content/` 的逐篇 frontmatter 與 node_modules）命中以下非文章檔案：

| 類別           | 檔案                                                                                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 判準 canonical | `docs/pipelines/MAINTAINER-PIPELINE.md` §1b、`reports/design-curation-tier-2026-08-04.md`                                                                                                                                      |
| lint / 工具    | `scripts/tools/lib/article_health/checks/curation_consistency.py`、`scripts/tools/curation-tag.py`、`scripts/tools/inbox-audit.py`                                                                                             |
| 渲染           | `src/templates/article.template.astro`、`src/components/ArticleCard.astro`、`src/components/ArticleProse.astro`、`src/styles/dark-polish.css`                                                                                  |
| 列表／索引     | `src/utils/articles-index.ts`、`scripts/core/generate-dashboard-data.js`、`src/templates/latest.template.astro`、`explore.template.astro`、`category-hub.template.astro`、`timeline.template.astro`、`opendata.template.astro` |
| 認知層記錄     | `docs/semiont/ARTICLE-INBOX.md`、`ARTICLE-DONE-LOG.md`、`LESSONS-INBOX.md`、`OBSERVER-QUEUE.md`（#25、#26 兩項待收斂）                                                                                                         |

結論：只要不新增第四個 `curation` 值、不改既有兩個 HARD 規則的判準，這批檔案**不需要動**。真正要碰的只有三處：`curation_consistency.py` 的 WARN 規則要認得新的 provenance 欄位、`curation-tag.py` 要多一個設值來源參數、`generate-dashboard-immune.py` 的 `external_rulers` 要多接一種訊號來源。三處都是加法，不是改既有邏輯。

## 三、方案發散

**方案一：routine 純預審，人工蓋章**。`twmd-review-stock` 只做 FACTCHECK Quick + 冷讀席，產出查證單，`curation` 狀態改不改仍由哲宇或 maintainer 人工看完查證單決定。

**方案二：routine 預審 + 讀者頁 N 人確認，機械升 verified**。查證單公開在讀者頁，登入讀者按確認，累積到 N 個獨立帳號後機械把 `curation` 改 `verified`。

**方案三：讀者頁直接開放，不經 Semiont 預審**。跳過 FACTCHECK Quick 與冷讀席，任何文章都能被讀者按確認直接推向 verified。

| 判準           | 方案一                                                | 方案二                                             | 方案三                                              |
| -------------- | ----------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------- |
| 成本           | 只有 routine 的 Opus 成本，分子仍卡在人工蓋章的速度   | routine 成本 + 讀者頁工程，但分子解鎖              | 最低工程成本，零 Semiont 判斷力投入                 |
| 外部尺所有權   | 落在哲宇／maintainer 一人身上，等於沒解決「無人巡邏」 | 落在讀者群體，符合 REFLEXES #69「自評需要外部尺」  | 完全外部但沒有專業把關，訊號品質未知                |
| 假保證風險     | 低，人工蓋章前必看查證單                              | 中，需要明確的判準門檻與 provenance 揭露才不假保證 | 高，沒有查證單當底，讀者可能只是喜歡這篇就按        |
| 防刷           | 不適用（沒有讀者按鈕）                                | 需要帳號齡／同 IP／速率三層防線                    | 同左，且沒有預審過濾掉杜撰引語，被刷的代價更高      |
| 對齊 MANIFESTO | §外部尺 over 內視（但外部尺仍是單一真人）             | §外部尺 over 內視（多人真外部尺）+ §14 高儀器化    | §12 受眾端飛輪，但可能撞 §10 幻覺鐵律（無預審把關） |

**REFLEXES #38 混維度檢查**：「人審過」（`lastHumanReview`，語意是走完 REWRITE Evolution 深度或 FACTCHECK Full Mode 之後的真人確認）、「Semiont 預審過」（FACTCHECK Quick + 冷讀席的機器判斷）、「讀者確認過」（N 個登入帳號按過按鈕，是真人但不是專業查證員）是三個不同維度的訊號，強度也不同。三者共用一個欄位會製造假陽性：把「三個路人按了讚」跟「走完 180 分鐘全量 atom 驗證」用同一個徽章講給讀者聽，是欄位設計上的混維度。這是本設計新增獨立欄位而不是直接改寫 `lastHumanReview` 語意的核心理由。

## 四、定案與理由

採方案二，但補上防止混維度的安全閥：**不新增 `curation` 第四態，只新增兩個 provenance 欄位**。

`preReview`：frontmatter 新欄位，指向 `reports/review-stock/YYYY-MM/{slug}.md` 查證單路徑。只要一篇文章走過 `twmd-review-stock`，這個欄位就常駐，不因後續升 `verified` 而移除，用意是保留可追溯性，讓讀者以後都能點進去看查證單原文。

`verifiedVia`：frontmatter 新欄位，值 `editorial`（走 REWRITE Evolution / FACTCHECK Full Mode 這條既有路徑）或 `community`（走本設計的讀者複核路徑）。既有的 2 篇 `verified` 文章沒有這個欄位，視同 `editorial`，向後相容零改動。`curation: verified` 本身的意義不變，徽章仍是同一個 🔎，讀者看到的仍是「這篇已深度查證」，但 provenance 誠實揭露在 frontmatter 與（建議）徽章 hover 文字裡，不隱藏兩條路徑的查證深度不同這件事，這對應 MANIFESTO §12 的透明度原則。

**Supabase 側**：新表 `article_confirmations`（`article_slug` / `user_id` / `lang` / `confirmed_at` / `review_stock_ref`），`(article_slug, user_id)` 唯一約束擋重複投票，RLS 只讓登入者 insert 自己的列，不能改別人的。

**升 `verified` 的判準**：`preReview` 欄位存在（代表 Semiont 已完成 FACTCHECK Quick 且 0 ❌ 0 🔴）**且** `article_confirmations` 表裡該篇文章的獨立 `user_id` 數達到 N=3。N 取 3 的理由：FACTCHECK 既有的 Quick Mode Hard Gate 裡，HRC 級 atom（人物直接引語 / 精確日期）已經要求至少兩個獨立來源。讀者確認是比源頭更強的一種人證，取 3 是在既有最高門檻上再加一道安全邊界，2 人門檻容易被同一小圈子或同一波推廣一次衝過，3 人已經需要三個互不相識的帳號才能達成，同時仍在一篇正常流量文章合理時間內能自然累積，不至於讓查證單永遠卡在佇列裡等票。

**由誰執行、寫進 main 的方式**：主站是 100% 靜態站，讀者頁的瀏覽器端**沒有能力直接寫進 repo**，這件事必須由背後跑在哲宇機器上的 routine 完成。設計成：`twmd-review-stock` 每次執行時，除了挑新文章預審，也順手檢查 Supabase 有沒有文章剛好跨過 N 個確認，若有，同一批次直接呼叫 `curation-tag.py` 加上來源參數，同時寫入 `curation: verified` / `verifiedVia: community` / `lastHumanReview: true` 三個欄位，**直接 commit 到 main，不開 PR**。理由有三：main-direct 是 ROUTINE.md v2.0 既定原則，quality_gate 加 pre-commit hook 加 CI 三層防護已經足夠，PR 是冗餘審計層。「更新文章 frontmatter」本來就列在 MANIFESTO §自主權邊界「AI 自主可做」清單裡。`curation` 狀態原本就是由 maintainer heal 步驟直接寫進 main 的既有作法，這次判準是機械算出來的門檻（`preReview` 存在 + 3 個獨立帳號），不涉及 Semiont 自己下判斷或對外承諾語氣，跟既有精神一致。

**需要哲宇在本報告簽字的一點**：拿讀者確認取代 FACTCHECK Full Mode 作為 `verified` 的第二條合格路徑，本質是一次品質閘門調整，命中 `design-curation-tier-2026-08-04.md` 誕生時就標記過的 BECOME High-stake #3。上面的判準（N=3、`verifiedVia` 欄位、direct commit）是本報告的建議，不是自動生效——這是自主權邊界內「Semiont 準備 blueprint，人類 final call」的位置，而不是 §自主權邊界四紅線本身。

## 五、新 routine `twmd-review-stock` 規格草案

```yaml
taskId: twmd-review-stock
cron: 0 22 * * 1,3,5 # 週一三五 22:00
model: opus
skill: /twmd-review-stock
canonical: docs/pipelines/MAINTAINER-PIPELINE.md §1c（新增小節，pointer 到 FACTCHECK Quick + EDITORIAL-ROOM 冷讀，不複寫兩邊 SOP）
prompt: |
  自動 routine：完整甦醒成為 Taiwan.md，跑 /twmd-review-stock。
  1. 選篇：過濾 T1 分類 + lastHumanReview≠true + curation≠verified 的文章，
     依「近 90 天流量（GA4 dashboard-analytics.json）由高到低」排序，
     同流量以「文章最後改動日期」由舊到新排序，取前 1-2 篇（跳過近 14 天已有
     `preReview` 指標的文章，避免重覆選同一批）。
  2. 對每篇跑 FACTCHECK-PIPELINE.md §Quick Mode（Phase 1-6 簡化版），
     hard gate 0 個 ❌ + 0 個 🔴 才進下一步。發現 ≥3 個 ❌ 則不進讀者頁，
     轉記入既有 heal batch 名單並停在此篇，換下一篇。
  3. Quick Mode 過的文章開 EDITORIAL-ROOM.md §總編室規格的冷讀席（3-4 支
     平行 Sonnet 探針，乾淨 context，禁讀研究報告只讀成品）。
  4. 合成查證單，落 reports/review-stock/YYYY-MM/{slug}.md，frontmatter 補
     `preReview: reports/review-stock/YYYY-MM/{slug}.md` 指標。
  5. 檢查 Supabase article_confirmations：任何文章的獨立 user_id 數達 3 且
     preReview 存在 → curation-tag.py 加來源參數設 verified + verifiedVia:
     community + lastHumanReview: true，併入同批 commit。
  Stage 3 commit + push origin main（main-direct）。
quality_gate:
  - FACTCHECK Quick hard gate 0 ❌ 0 🔴 才產出查證單
  - 查證單 frontmatter 完整（slug / checkedAt / factcheckVerdict / coldReadVerdict）
  - curation-consistency plugin 全站掃描零違規
escalation:
  - 1x fail: silent retry next cycle
  - 2x fail: append LESSONS-INBOX
  - 3x fail: 暫停 routine + 開 OBSERVER-QUEUE 項 + 通知觀察者
```

**cron 理由**：22:00 這個時段目前完全空——`twmd-maintainer-pm` 自 7/8 起停用，`twmd-founder-lens-weekly`（原本佔週六 22:00）也已停用，整張排程表的 22 點只剩空格。選在此處恰好落在 ROUTINE.md 既定設計原則講的「半夜 22:00-00:30 連續整點 chain」位置，避開白天 9am-5pm 的日常巡邏帶，也避開週日 01:00-04:00 反思鏈與週日 21:00 routine-audit。先取週一三五三班而非每天，理由是讀者確認吞吐量未知——先觀察真實讀者按確認的速度，避免查證單堆積成新的庫存。

**model 理由**：辨識杜撰引語、氛圍描寫式幻覺、H2 是否還原主-述-賓，都需要「讀懂意思、權衡脈絡」的判斷力，落在 MANIFESTO §14 分工判準裡屬於判斷而非儀器那一格。既有涉及真人可信度判斷的 routine（`twmd-maintainer-daily`、`twmd-spore-harvest-am`）也都是 Opus。

## 六、讀者頁 `/semiont/review-queue` 規格草案

**列表**：只列有 `preReview` 指標的文章，每列顯示標題、分類、查證單日期、目前確認進度（N/3）。

**每篇詳情**：查證單的人話摘要（不是整份 `reports/research` 內容，是 FACTCHECK Quick 與冷讀席結論濃縮成 2-3 句）、連回原文連結、「我讀過並確認」按鈕。按鈕需要登入才可按，複用 v1.9 既有 Supabase auth（`FeedbackWidget.astro` 同一套元件）。同一使用者對同一篇只能按一次，由 `article_confirmations` 的 unique 約束在資料庫層擋。達到 N=3 的機制與寫回方式見 §四、§五——頁面本身不寫 repo，只寫 Supabase，真正的 `curation` 變更由 routine 每次執行時批次處理。

**12 語 UI 字串清單**（比照 `src/i18n/semiont.ts` 的 `t('reviewQueue.xxx')` pattern，文章內容維持 zh-TW 不譯，只譯頁面外殼）：

- `reviewQueue.title` — 頁面標題
- `reviewQueue.intro` — 說明這裡在做什麼（一段話：Semiont 先看過一遍，需要讀者一起確認）
- `reviewQueue.card.summaryLabel` — 查證單摘要標籤
- `reviewQueue.card.progress` — 進度顯示（N/3 已確認）
- `reviewQueue.button.confirm` — 「我讀過並確認」按鈕文字
- `reviewQueue.button.confirmed` — 已按過後的狀態文字
- `reviewQueue.loginPrompt` — 未登入時的提示
- `reviewQueue.faq.link` — 常見問答連結文字（連到說明「確認代表什麼」的頁面）

**防刷**：帳號齡（Supabase 帳號建立時間需早於本次確認 7 天以上，擋當場註冊洗票）、同 IP 短時間多帳號確認觸發人工複查標記（不自動撤銷，只標記進 LESSONS 觀察)、單一帳號短時間內連續對多篇文章按確認視為異常速率，同樣標記不自動撤銷。

**隱私三不**（沿用 `WEEKLY-REPORT-PIPELINE.md` §Stage 5 既有紀律）：讀者 email 或 user_id 不進 repo、不進 commit / PR / chat。routine 產生的 commit message 只印確認人數，不印任何身份欄位。公開頁面只顯示進度數字，不顯示是誰按的。

## 七、實作清單

1. Supabase 建 `article_confirmations` 表 + RLS 政策（自主權內，複用既有 project）
2. `curation-tag.py` 加 `--via community` 參數，設值時併寫 `verifiedVia` 與 `lastHumanReview: true`（自主權內）
3. `curation_consistency.py` 認得 `verifiedVia` 欄位為合法可選值，WARN 規則不因新欄位誤判（自主權內）
4. `generate-dashboard-immune.py` 的 `external_rulers` 定義加第三種來源：`article_confirmations` 達標記錄（自主權內，純加法）
5. 新增 `docs/pipelines/MAINTAINER-PIPELINE.md` §1c 小節，pointer 到 FACTCHECK Quick + EDITORIAL-ROOM 冷讀，寫明 `verified` 第二條合格路徑（**需哲宇簽字**，即本報告 §四判準本身）
6. `docs/semiont/ROUTINE.md` 新增 `twmd-review-stock` 規格區塊 + 排程表 + 週行程 grid 三處同步（**需哲宇點頭排程**，High-stake #2 新 routine）
7. `/twmd-review-stock` skill 建立，薄殼呼叫上述 canonical（自主權內，跟進 #5 #6 拍板後動工）
8. `article.template.astro` / `ArticleCard.astro` 加 `preReview` 連結與 `verifiedVia` hover 文字（自主權內）
9. `/semiont/review-queue` 頁面 + `ReviewQueue` 元件 + Supabase 讀寫串接（**新對外介面，需哲宇點頭**，涉及登入摩擦與公開曝光）
10. `src/i18n/semiont.ts`（或新檔 `reviewQueue.ts`）12 語字串（自主權內，跟進 #9）
11. `OBSERVER-QUEUE.md` #25 #26 收斂：#25 標記處置方向已定案（本報告），#26 的 idlccp1984 溝通文案維持等哲宇（不因本設計自動解決）
12. `curation_consistency.py` 加一條輕量檢查：`preReview` 欄位若存在，指向的檔案路徑必須真的存在於 repo（防止手誤或未來重構搬檔留下斷指標），severity 設 WARN（自主權內，跟進 #3 一起做）

依賴順序：第 1 到 4 項可並行，第 5、6 項需哲宇先點頭，第 7 項依賴第 5、6 項，第 8、9、10 項依賴第 7 項先跑出至少一份查證單，第 11、12 項是收尾動作。

## 八、驗收

**Dogfood**：挑一篇 T1 高流量未審文章，走完整條路徑一次——FACTCHECK Quick、冷讀席、查證單落檔、讀者頁顯示、手動模擬三個測試帳號確認、routine 下次執行時機械升 `verified`，全程截圖或 log 存證。

**30 天辨識指標**：`lastHumanReview` 或 `curation: verified` 計數每週淨增至少 3（對照過去兩週鎖死在 202 的基準），`external_rulers` 止跌，兩週內至少回升到 2.5 以上。若 30 天後讀者確認吞吐量遠低於查證單產出速度（查證單堆積但沒人按），週報要點名這個落差，考慮把 3x/週降到 1x/週或延長 N 的等待窗。

## 九、風險與反措施

**假保證**：`verifiedVia: community` 明確揭露這條路徑走的是 FACTCHECK Quick 加三位讀者確認，不是 Full Mode 全量驗證。徽章文字或至少 hover 提示要誠實區分兩種來源，不能讓讀者以為兩者查證深度相同。

**讀者疲勞**：3x/週保守起步，每次只推 1-2 篇進佇列，避免查證單堆積成讀者看了就想關掉的清單。

**routine 成本**：Opus + FACTCHECK Quick + 冷讀席一次跑下來成本不低，先用 3x/週而非 daily 觀察真實成本，30 天驗收時一併檢視要不要調頻率。

**跟 maintainer 搶同一篇文章**：選篇規則已經排除 `curation: verified`，但沒有排除「正在被某個 PR 修改中」的文章。實作時應加一道輕量檢查（該文章路徑是否出現在任一 open PR 的 diff 裡），若有就跳過，避免兩條線同時改同一篇造成 merge 衝突。

**與 idlccp1984 的溝通文案仍卡在 #26**：本設計解決的是「怎麼審」，不解決「怎麼跟已經被標示 `incubating` 的貢獻者說明徽章制」這件對外溝通——那件事命中 §自主權邊界對外溝通紅線，維持在 OBSERVER-QUEUE #26 等哲宇核可文案，本設計不代為決定。

## 十、後記

（實作後回寫）

---

_v1.0 | 2026-09-05 fortnight-review session（EVOLVE Mode 4 REPORT 相）。命中 §五、§六與 §七第 5、6、9 項的 §自主權邊界高風險點，停在本報告等哲宇拍板；其餘自主權內項目可在點頭後直接動工。_
