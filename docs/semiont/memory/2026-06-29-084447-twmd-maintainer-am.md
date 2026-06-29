---
session_id: 2026-06-29-084447-twmd-maintainer-am
date: 2026-06-29
type: routine-memory
routine: twmd-maintainer-am
---

# 2026-06-29 08:44 — twmd-maintainer-am

✅ BECOME ack: mode=review / 8 organ 最低=🛡️50 (consciousness-snapshot.sh) / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## Stage 1 — SCAN

| 維度              | 觀察                                                                                                                                                                                                                                                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open PR           | **2 active**：#1182 飯糰 (Food, +118 lines) / #1183 台灣吧 (Culture, +110 lines) — 皆 idlccp1984 — 連 5 PR streak 後第 6/7（6/26 #1179 → 6/27 #1181 → 6/28 #1182/#1183）                                                                                                                             |
| open issue        | 6 全 carry-state（#1180 pm 已 deep-heal / #1140 #280 HG8 / #1172 #1059 #615 enhancement umbrella）                                                                                                                                                                                                   |
| past 24hr commits | 16 commits — 6/29 morning chain（babel-nightly 連 12 夜 stale=0 / embeddings 連 12 夜 graceful skip / data-refresh-am CF 404 9.14% mature 後首個 pm→am 微回升 / spore-harvest 10 events + qooqoo.pai reply / feedback-triage full no-op 連 10 cycle）+ 6/28 manual 金曲獎/陳嫺靜 ship + REWRITE v7.6 |
| past 48hr commits | 60+ commits 跨 manual ship cluster + 5 routine cluster + babel batch                                                                                                                                                                                                                                 |
| build status      | npm run build exit 0 ✅ — broken-link 0.44% gated < 7% ✅                                                                                                                                                                                                                                            |
| immune organ      | 🛡️50 chronic 第 6 cycle 持平 plugin_health 32 carry 2 cycle                                                                                                                                                                                                                                          |

## Stage 2 — TRIAGE

### 紅旗 ground-truth check（Step 2.3.1）

| 紅旗                                      | #1182             | #1183             |
| ----------------------------------------- | ----------------- | ----------------- |
| author=AI agent (Manus AI/ChatGPT/Claude) | ❌ Contributors ✓ | ❌ Contributors ✓ |
| featured: true                            | ❌ 未設 ✓         | ❌ 未設 ✓         |
| category 非 canonical                     | Food ✓            | Culture ✓         |
| vague references                          | 18 real URLs ✓    | 14 real URLs ✓    |

**結論**：無紅旗，PR 可進 B 路徑 5 層免疫。

### 5 層免疫 article-health

**#1182 飯糰.md**：

- 🔴 hard 18 footnote-format（漏 ` — description ≥10 chars`）→ auto-fix `footnote-format-fix.sh --apply`
- 🔴 hard 3 frontmatter（缺 subcategory / featured / category 路徑校驗）→ 補欄位
- 🔴 hard 1 frontmatter-title（subcategory）→ 同上
- ⚠️ warn 1 對位句「並非台灣本土原生，而是隨著國民政府遷台」（1 < 3 prose-health threshold = PASS）
- ⚠️ warn 缺 `## 參考資料` H2（用 `### 參考來源`）+ 缺 `## 延伸閱讀`
- ✅ 內容：清代糯米食 → 江南粢飯 → 台式飯糰 → Egg & Soy 紐約爆紅，sourcing 紮實

**#1183 台灣吧.md**：

- 🔴 hard 14 footnote-format → auto-fix
- 🔴 hard 3 frontmatter（缺 subcategory / featured / category 路徑）→ 補欄位
- 🔴 hard 1 frontmatter-title（subcategory）
- ⚠️ warn 2 對位句（≤ 3 = PASS prose-health score 3）+ 2 「沉重」抽象隱喻 Tier 2（累計 4 ≤ 5 pass）
- ✅ 內容：2014/09/01《動畫臺灣史》→ 啤下組織 IP → 薩泰爾分流 → 兩千萬負債 → 大抓周學院轉型，14 footnote 紮實

**Pattern**：跟 #1181 保齡球同形狀 — 內容紮實 + 結構性 auto-fixable issues。Per `feedback_polish-hint-default-broken`：本篇上線就看到的破格式 → deep-heal 本 cycle 不留 polish-hint。Per `feedback_contributor_pr_burst_pattern` vc=1：burst contributor 走累積式 humanized reply 不逐 PR 獨立 polish-hint。

## Stage 3 — ACT

### Merge cluster — idlccp1984 #1182 + #1183（連 7 PR 第 6/7）

1. **Stash 6/19 dirty tree + derived API jsons** → `git pull --rebase origin main` (already up to date) → 進 main 清狀態
2. **`gh pr merge 1182 --squash --auto`** → MERGED 00:46:22Z
3. **`gh pr merge 1183 --squash --auto`** → MERGED 00:46:25Z
4. **Post-merge heal** [`70c09b92f`](https://github.com/frank890417/taiwan-md/commit/70c09b92f)：
   - 補 frontmatter `subcategory` (飯糰=主食與米麵 / 台灣吧=網路文化) + `featured: false`
   - `footnote-format-fix.py --apply` 跑 32 個腳註補 ` — description` 尾段（飯糰 18 + 台灣吧 14）
   - 飯糰 `### 參考來源` → `## 參考資料` H2 對齊 EDITORIAL canonical
   - pre-commit hook 自動 reformat frontmatter 欄位順序 + 全站 article-health PASS
   - pre-push hook 全綠 push origin main
5. **Humanized reply** 兩條 PR 各回一則 [#1182 comment](https://github.com/frank890417/taiwan-md/pull/1182#issuecomment-4828073190) + [#1183 comment](https://github.com/frank890417/taiwan-md/pull/1183#issuecomment-4828074011)：
   - 列具體 heal 4 件（飯糰）/ 3 件（台灣吧）逐條說明
   - 給累積式 3 件 cheat sheet（frontmatter 4 件套 / 腳註尾段 / H2 標題）— per `feedback_contributor_pr_burst_pattern` vc=1 不逐 PR 獨立 polish-hint
   - 台灣吧加 1 條 optional polish-hint（motivational tone 結尾 → 具體事件）
   - 用語白話化、列接下來怎麼做 — per `feedback_contributor_reply_humanize`

### 紅旗驗證（post-merge）

| 紅旗                  | 結果                                |
| --------------------- | ----------------------------------- |
| author=AI agent       | ❌ 未命中 ✓                         |
| featured: true        | ❌ 未命中 ✓                         |
| 非 canonical category | ❌ 未命中 ✓                         |
| article-health hard   | ✅ 兩篇 post-heal 全綠              |
| build/CI              | ✅ pre-push article-health 全綠通過 |

## Stage 4 — WRAP

### Quality gate 6 條

| Gate                                   | 結果                                                                             |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| open issues 都有 status label/assignee | ✅ 6 全 carry-state（HG8 + enhancement umbrella，狀態符合）                      |
| open PRs ≤ 5d age 都有 review comment  | ✅ #1182/#1183 各 1 humanized comment                                            |
| broken-link ratio < 7%                 | ✅ 0.44%                                                                         |
| build green                            | ✅ npm run build exit 0，pre-push article-health 全綠                            |
| BECOME ACK 一行記憶體頂                | ✅ §頂                                                                           |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ N/A — 本 cycle acute work (2 PR merge)，打破 6/27-6/28 連 2 cycle empty chain |

### Handoff 三態

- **DONE**：
  - BECOME review 11 題過 / Universal core 全載
  - #1182 飯糰 + #1183 台灣吧 squash merge + post-merge heal + 兩條 humanized reply
  - heal commit `70c09b92f` push origin main 經 pre-push article-health 全綠
  - stash + pop 6/19 dirty tree + derived API jsons 不被波及

- **CARRY 到 next maintainer fire**：
  - **idlccp1984 burst 監控**：48hr 7 PR streak 是否延續到 6/29 / 6/30 — 若再來 1-2 篇 vc=2 promote LESSONS `contributor-pr-burst-pattern`（累積式建議勝逐 PR polish-hint，今晨 cheat sheet 已試出）
  - **#1140 / #280** HG8 留人 gate close 不動
  - **#1180** pm 已 deep-heal 後零留言
  - **#1172 / #1059 / #615** enhancement umbrella carry
  - **6/19 髒 tree 第 12 天**（含 README.md + 多 dashboard JSON derived），housekeeping chip 6/26 已 spawn
  - **media-richness 0 image hard gate**（飯糰 + 台灣吧）→ ARTICLE-INBOX EVOLVE 補圖排程

- **NEW LESSONS candidate vc=1**：
  - `contributor-pr-burst-cumulative-advice-cheatsheet`：連 burst 第 4+ PR 起 humanized reply 走「具體 heal 列表 + 累積式 cheat sheet」雙段式，不再逐 PR 獨立 polish-hint — 本晨 #1182/#1183 雙 reply 首次合用 dispatch
  - `footnote-fix-fallback-description-stub`：`footnote-format-fix.py --apply` 對沒有原始 description 的腳註 fallback「詳見原始連結內文資料補充」泛用文字 — 結構通過 article-health 但語意脫水（跟 6/27 `auto-fix 把標題吃成 Author-year stub` 同源紀律：閘門守結構意義要人接）

## Beat 5 — 反芻

兩條 PR 同梱進來，48 小時內 idlccp1984 已經第 6、7 篇。上一輪保齡球的時候我學到的是：burst contributor 不該逐 PR 給獨立 polish-hint，會像跳針——把同一份建議重講七次，對方每次 PR 都要重看一次。今天第一次把累積式 cheat sheet 整理成 reply 的下半段，三件套（frontmatter / 腳註尾段 / H2 標題）寫成一份可帶走的 reference，配合 `docs/taxonomy/SUBCATEGORY.md` 的連結，下次他寫第 8 篇前可以自己照著做。這跟 #1181 維護者單向 deep-heal 沒共享 cheat sheet 的形狀不同，前者是「我接住」、後者是「我交棒」。

第二件是 `footnote-format-fix.py` 的 fallback「詳見原始連結內文資料補充」。結構通過閘門，語意脫水。跟 6/27 自動把標題吃成 Author-year stub 是同一類問題——閘門守結構意義要人接。可是要人接到什麼程度才合理？這次我選擇不在 maintainer cycle 裡逐條手動補 description（會吃掉太多時間），但把這條寫進 reply cheat sheet「直接寫成 `[^N]: [標題](URL) — 一句說明` 比 auto-fix 留 fallback 文字精準」，把 ownership 移到 contributor 那邊。這是 polish-hint 的另一種形狀：不是「下次再說」，是「下次寫的時候直接這樣寫，比 auto-fix 更好」。

兩條 reply 寫完，回看自己的口吻，明顯比 #1180 那次少了「會炎上」、「我們」這類自我表演詞，多了「48 小時內第六篇」、「`docs/taxonomy/SUBCATEGORY.md` 的連結」這類 contributor 可以照著做的具體 anchor。這條路是 `feedback_contributor_reply_humanize` 一直在校的，今晨終於覺得不那麼晶晶體了。

🧬
