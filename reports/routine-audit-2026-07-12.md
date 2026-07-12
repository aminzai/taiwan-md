---
title: 'Routine audit 2026-07-12 (W28)'
description: '7-day 跨 routine 飛輪自審 — 246 commit / 16 heal / 0 dysfunctional collision / 4 lens findings / 2 新 LESSONS 候選'
type: 'audit-doc'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-12
routine: 'twmd-routine-audit-weekly'
window: '2026-07-05 21:17 → 2026-07-12 21:17 (7d)'
related:
  - 'docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'reports/routine-audit-2026-07-05.md'
---

# Routine audit 2026-07-12 (W28)

第 10 週飛輪自審。上週（W27）2026-07-05 audit 走完 6 stage 後，本週產出 246 commit / 84 routine fires 分佈於 17 routine，其中 5 條被 sensor 誤標「沉默死亡」的黃燈實際上已在過去 24-48hr 復活但未 auto-retire。四條 cross-cutting lens 掃出兩個新結構性 pattern 進 LESSONS-INBOX，一個 defer 給哲宇拍板。

---

## Executive summary（5 分鐘 read）

| 面向             | 數字 / 說明                                                                                                                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 窗口             | 2026-07-05 21:17 → 2026-07-12 21:17（7 day）                                                                                                                                                             |
| Commit 總量      | 246 條（1,458 檔 / +137,593 / -59,652）                                                                                                                                                                  |
| 分類             | semiont=146 / routine=84 / pr-squash=9 / other=7                                                                                                                                                         |
| Routine fire     | 84 條 across 12 個 twmd-\* routine（見 §逐 routine 表）                                                                                                                                                  |
| Heal             | 16 條（07-06 frontmatter cluster / 07-11 dna-checkup 4 heal 波 / 07-12 tea-panorama pre-push sweep）                                                                                                     |
| Collision        | 0 條 dysfunctional；6 條 adjacent-time cross-routine pair 全屬 design（morning chain spore-harvest → feedback-triage 30min / Sunday reflection chain news-lens → weekly-report → distill 55-57min 序列） |
| 4-lens finding   | 3D 全綠 / 3A green / 3B 兩條發現（stale alerts + thick mirror debt） / 3C wake-guard root-caused + fixed                                                                                                 |
| LESSONS 候選     | 2 條新 append（alert-does-not-retire-on-recovery + thick-scheduled-task-mirror-debt）                                                                                                                    |
| Vc bump 既有     | 0（3 條既有 §未消化 entry 本週無新 instance）                                                                                                                                                            |
| Distill-ready 標 | 0（兩條新 candidate 均 vc=1，未達 3）                                                                                                                                                                    |

**Handoff carry**：14 條 thick scheduled-task mirror 舊債（Session 172122-manual handoff 提出）本 audit 記錄為 LESSONS，defer 給哲宇拍板批次瘦身節奏。

**routine 感知層警訊**：`dashboard-alerts.json` 五條 `routine-silent-*` 黃燈 firstSeen 2026-07-10 都仍在，實際 5 條 routine 都在過去 48hr 內恢復 fire + commit（見 §Stage 3B）。alert schema 缺 retire condition = sensor exit 端說謊。

---

## 逐 routine 詳細

| Routine                     | Fire 次數 | Files | Ins/Dels        | Health                                                                                                                                              |
| --------------------------- | --------: | ----: | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `twmd-data-refresh-am`      |         6 |   166 | +24,468/-22,572 | 🟢 6/7 fire（07-10 miss）—— 07-11 起連 2 cycle CF 404 vc=5→vc=6 跌破 16% 達門檻                                                                     |
| `twmd-data-refresh-pm`      |         6 |   178 | +24,125/-20,393 | 🟢 6/7 fire（07-09 miss）—— 14-step 全綠                                                                                                            |
| `twmd-babel-nightly`        |         6 |   198 | +15,823/-3,969  | 🟡 5/7 unique dates fire（07-08, 07-10 miss）—— 07-12 00:51 4-tier cascade 全滅走 Tier 0b metadata backfill 25 篇 `b590be002`                       |
| `twmd-embeddings-nightly`   |         6 |    22 | +22/-22         | 🟢 6/7 fire（07-10 miss）—— 連 7 夜 bge-m3 0 fail / PASS                                                                                            |
| `twmd-feedback-triage`      |         6 |    12 | +358/-0         | 🟢 6/7 fire（07-10 miss）—— 07-12 復活 run，唯一 new 是哲宇 plumbing test「測試測試」→ reject-as-test 不開公開 issue                                |
| `twmd-spore-harvest-am`     |         6 |    21 | +790/-38        | 🟢 6/7 fire（07-10 miss）—— 07-12 #154 柯智棠 D+5 觸底穩定期五指標 stable                                                                           |
| `twmd-maintainer-am`        |         7 |    13 | +772/-1         | 🟢 7/7 fire（07-10 12:47 延遲從 08:30 到中午）—— 07-12 ellenlee 第 2 波 3 PR 全清（#1219 self-fix review-pr.sh / #1217 media / #1218 AI 硬體 4 篇） |
| `twmd-maintainer-pm`        |         2 |     6 | +249/-2         | ⏸️ 07-08 起 disabled（ROUTINE.md v2.14 對齊 live），2 fire 皆 pre-disable（07-05, 07-07）                                                           |
| `twmd-distill-weekly`       |         1 |     — | —               | 🟢 W28 Sunday 03:09 fire —— §未消化 2 條全 defer 給哲宇 + SPORE-INBOX pending=49 落 [30,50) 警示 + MEMORY 索引 rollup 57→40 + 17 歸檔               |
| `twmd-weekly-report-sun`    |         1 |     — | —               | 🟢 W28 Sunday 02:14 fire —— v4.1 一鍵七節 checkup + Resend id `b0105104` / 桶 1 零項 + 六條進 roadmap draft                                         |
| `twmd-news-lens-weekly`     |         1 |     — | —               | 🟢 W28 首份週報 `reports/news-lens/2026-07-12-w28.md`；出口 disabled 走 v2.6 分支 propose 0 條進 SPORE-INBOX                                        |
| `twmd-self-evolve-weekly`   |         2 |     — | —               | 🟢 W28 Sunday 04:18 fire —— 訊號選擇層三 pattern 收乾：`#82` 新反射 + `#69 (g)` form-vs-meaning + `#65 (f)` same-DNA `1f4a08f45` `1eeb9079c`        |
| `twmd-rewrite-daily`        |         1 |     — | —               | 🟡 07-12 19:10 fire 為 ABORT — daily 飛輪已於 13:57 tea-panorama depth EVOLVE 用完 (vc=8 per REFLEXES #64)                                          |
| `twmd-routine-audit-weekly` |         1 |     2 | +240/-1         | 🟢 07-05 21:17 fire (last cycle) —— 本 session 是 cycle 10                                                                                          |

**Reader-friendly note**：14 條 twmd-\* routine 中，daily nightly / morning routine 都在 07-10 那天集體 miss 一次 fire（feedback-triage / babel / data-refresh-am / embeddings-nightly / spore-harvest-am），07-11 起全部恢復正常。這與 07-12 wake-guard session 發現的 wake-context 通道截斷（cron session `| head` 自截導致記憶層 silent 消失）時間軸不完全重疊——07-10 miss 早於 wake-context 儀器誕生（07-11 22:09），因此 07-10 miss 屬 separate cause，可能是 macOS scheduled-tasks 服務層某次重啟或觀察者本地機器狀態。日誌層無明確跡證，本 audit 記錄為 event 不推論 root cause。

---

## Cross-cutting patterns（4 lens）

### 3A. Collision lens — 🟢 綠燈

7-day 窗口 6 條 adjacent-time cross-routine pair 全屬 design chain：

| 序列                                 | 出現次數 | 說明                                                                              |
| ------------------------------------ | -------: | --------------------------------------------------------------------------------- |
| spore-harvest-am → feedback-triage   |        4 | 06:40 → 07:10 morning chain（30min offset per ROUTINE.md v2.7 morning chain SOP） |
| news-lens-weekly → weekly-report-sun |        1 | Sunday 01:17 → 02:14（55 min，reflection chain 半夜整點）                         |
| weekly-report-sun → distill-weekly   |        1 | Sunday 02:14 → 03:09（55 min，同上 chain）                                        |

無 orphan process / rescue commit / detached worker instance。sibling collision `selective git add` 模式（per ROUTINE.md §sibling-routine-collision-handling）本週未觸發。

### 3B. Dormant entropy lens — 🟡 兩條發現

**Finding 1: alert-does-not-retire-on-recovery**

`public/api/dashboard-alerts.json` 五條 `routine-silent-*` 黃燈 firstSeen 2026-07-10，實際五條 routine 都已在 07-11 + 07-12 連續兩次 fire + commit：

| Alert code                                             | firstSeen  | 實際最新 fire (commit hash)                                | 齡   |
| ------------------------------------------------------ | ---------- | ---------------------------------------------------------- | ---- |
| `routine-silent-taiwanmd-routine-twmd-feedback-triage` | 2026-07-10 | 2026-07-12 07:13 (`4b22f999d`)                             | 2 天 |
| `routine-silent-twmd-babel-nightly`                    | 2026-07-10 | 2026-07-12 00:51 (`b590be002`) + 07-11 00:56 (`39a393816`) | 2 天 |
| `routine-silent-twmd-data-refresh-am`                  | 2026-07-10 | 2026-07-12 06:16 (`9d96bd596`) + 07-11 06:13 (`6ab16064c`) | 2 天 |
| `routine-silent-twmd-embeddings-nightly`               | 2026-07-10 | 2026-07-12 05:17 (`2bf168de6`) + 07-11 05:16 (`86798c4be`) | 2 天 |
| `routine-silent-twmd-spore-harvest-am`                 | 2026-07-10 | 2026-07-12 06:41 (`da002bcd0`) + 07-11 06:41 (`1da2337d7`) | 2 天 |

齡 2 天，未達 ROUTINE-AUDIT §Hard Gate「>14 天升 OBSERVER-QUEUE」門檻。但 sensor recovery blind spot 是結構性的（不會靠齡值 alone 治好）：alert 只掃 entry event（`fire=true` 停了），沒掃 retire event（`fire=true` 又開了）。已 append LESSONS §未消化 `alert-does-not-retire-on-recovery` vc=1，屬 REFLEXES #82 proxy signal antipattern 家族子案例。

**Finding 2: thick-scheduled-task-mirror-debt**

`routine-sync-check.py` 揭 14 條 mirror 違反 ROUTINE.md §薄殼鐵律 30 warn / 50 hard 行閾值：

| Routine mirror                  | 行數 | 狀態    |
| ------------------------------- | ---: | ------- |
| `twmd-spore-publish-daily`      |  192 | 🔴 hard |
| `twmd-maintainer-pm`            |  100 | 🔴 hard |
| `twmd-maintainer-daily`         |  100 | 🔴 hard |
| `twmd-babel-nightly`            |   79 | 🔴 hard |
| `twmd-spore-pick-daily`         |   78 | 🔴 hard |
| `twmd-distill-weekly`           |   66 | 🔴 hard |
| `twmd-spore-harvest-am`         |   66 | 🔴 hard |
| `twmd-news-lens-weekly`         |   60 | 🔴 hard |
| `twmd-routine-audit-weekly`     |   60 | 🔴 hard |
| `twmd-data-refresh-pm`          |   58 | 🔴 hard |
| `twmd-data-refresh-am`          |   58 | 🔴 hard |
| `twmd-self-evolve-weekly`       |   55 | 🔴 hard |
| `twmd-weekly-report-sun`        |   49 | 🟡 warn |
| `twmd-music-media-audit-weekly` |   43 | 🟡 warn |

僅 3 條合規：`twmd-rewrite-daily` (20) / `twmd-embeddings-nightly` (28) / `twmd-feedback-triage` (19)。1 條 orphan：`twmd-supporters-weekly`（07-12 172122-manual 新誕生 routine，PR #1221 pending review，SSOT 尚未列入 ROUTINE.md）。

Session 172122-manual handoff 明確 pointer「留給下一輪 routine-audit-weekly 或哲宇拍板」。本 audit 收下 handoff，記錄為 LESSONS §未消化 `thick-scheduled-task-mirror-debt` vc=1，defer 給哲宇拍板批次瘦身節奏（14 檔跨 routine 大改屬 §自主權邊界，per REFLEXES #79 主權留哲宇 default reservation）。

**Finding 3: counts-drift 33 drift / 39 宣稱點**

`counts-drift-lint.py` warn mode：

- 8+ 條 frontmatter `last_updated` 落後 git mtime（Stage 4.5 語意 vs 機械 regen 判斷）
- 8 條 i18n home stats（847 vs 851），下次 `data-refresh` 自癒
- 1 條 dashboard-vitals totalArticles 落後 live（同上，routine 自癒）
- 1 條 `docs/pipelines/README.md` 索引 36 宣稱 vs 35 實存（缺 RESEARCH-AGENT-PROMPT.md / WRITER-PROMPT.md）

多為 chronic warn，routine 自癒或 self-evolve 定期補。本 audit 不特別 flag。

### 3C. Boundary input precision lens — 🟢 wake-guard root-caused + fixed

07-12 wake-guard session (140619) 抓到並修好一條**開機通道截斷**的結構性 boundary issue：

- **問題**：wake-context 全段輸出 ~200KB 超過 Bash tool ~30K 字元輸出上限。7/11 儀器誕生後 12 小時內，9 條 cron 甦醒（Opus 4.7/4.8 transcript 取證）自行 `| head -120〜-500` 截斷，記憶面整層消失。fail-loud selftest 排在最尾端第一個被截。
- **架構解 v2**：儀器 v2 完整內容落檔 `.taiwanmd/wake-context.latest.md`，末行 wake:END sentinel 帶總 bytes；stdout 只留 manifest + selftest（小到不可能被截斷）。BECOME v2.5 §1.3 立三條讀取鐵律：Read 分頁到 sentinel / ⛔ 禁 head/tail/awk 節選 / ⛔ 禁讀 harness 記憶層。
- **REFLEXES**：本事件是 `#82 proxy signal antipattern` 新 instance —— fire=true ≠ 完整讀取。已在 07-12 self-evolve-weekly 04:18 promote canonical。

本 audit 補記錄：本 session 用 Read 分頁讀完 wake-context (204,874 bytes / 1,281 行) 到 wake:END sentinel，boundary input precision 這一 lens 本週已由上游 session 主動修補，無新 finding。

### 3D. Heal bidirectional lens — 🟢 綠燈

16 條 heal 全屬正確 heal，無 over-action / over-ship / over-defer 反射式偏誤：

- **07-06 cluster (7 heal)**：frontmatter 對齊 / 藍白系列圖片攝影者署名 / PERSONA-PIPELINE 薄殼收斂 / 張忠謀延伸閱讀補齊
- **07-11 dna-checkup 4-heal 波 18:45-19:13**：量尺排序方向假設修正 / lessons-distill vc 抽取邊界 / 三個核心器官死指標與寫死計數 / counts-drift ground truth 從過期鏡子換 live —— 屬同一 session ruler-fixing 收成，跟 REFLEXES #65 (f) same-DNA 陷阱 promote 同 cycle。
- **07-12 tea-panorama 2 heal**：pre-push sweep 接住 pre-existing HARD (博客 → 部落格) + 補 3 張配圖。屬 `manual-evolve` session 內收官 heal。
- **07-11 ellenlee 2 heal**：註冊 3 篇 en 譯本 / 4 篇 merge 後引用瑕疵 —— maintainer 收 contributor batch 標準流程。
- **07-12 external PR #1219** (78ae45b9): `fix: handle translated article paths in PR review` —— 由 contributor ellenlee 自己 fix 自己前一波 PR review 造成的 CI 病灶，maintainer-am merge。

無 close-over-merge / defer-over-action instance。

---

## LESSONS-INBOX 候選 table

| Entry                               | Type |  vc | Severity              | Defer 給哲宇   |
| ----------------------------------- | ---- | --: | --------------------- | -------------- |
| `alert-does-not-retire-on-recovery` | 新   |   1 | tactical → structural | 否（工具改進） |
| `thick-scheduled-task-mirror-debt`  | 新   |   1 | structural chronic    | 是（14 檔）    |

無既有 §未消化 entry 收到本週新 instance，無 vc bump。

---

## 進化建議

| P      | 建議                                                                                                                                                                                                                                                        | Owner        |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **P1** | `scripts/tools/build-dashboard-alerts.mjs`（或對應 generator）加 routine-silent recovery detector：檢查過去 24hr git log routine name commits 有無，有則 auto-retire（或降級 info）。避開 alert 面板變墓碑                                                  | routine 自決 |
| **P1** | `routine-sync-check.py --heal-thin` mode 造橋：對 14 thick mirror 生成薄殼 diff proposal（保留 STRICT BECOME GATE + Stage pointer + rate limit 條款），觀察者可一次 review 14 條 PR（or 分批 self-evolve 挑 1-2 條每週瘦身）—— **不自動 apply，defer 哲宇** | 造橋 → defer |
| **P2** | `twmd-supporters-weekly` orphan → PR #1221 merge 後補進 ROUTINE.md live 排程表                                                                                                                                                                              | maintainer   |
| **P2** | 07-10 mass silence 未有 post-mortem — 若下週再現同型 miss，觸發 root-cause investigation（可能 macOS scheduled-tasks 服務層問題）                                                                                                                           | manual       |
| **P3** | counts-drift 8+ frontmatter `last_updated` 落後 git mtime 條目，等下次 dna-audit 或 self-evolve 週 cycle 處理，不新開 issue                                                                                                                                 | 定期 routine |

---

## 跟 W27 (2026-07-05) audit 的差別

W27 audit 收成：144 commit / 12 heal / 3 新 LESSONS + 4 vc+1（含 orchestrator-aggregate-on-receive 促成 REFLEXES #81 promote / spine-type-by-subject #77 / cadence signature + reservation posture + fire-sustain #78/#79/#80）—— routine 飛輪同週高產反射 promote 波。

W28 本 audit 收成：246 commit（+71%）/ 16 heal（+33%）/ 2 新 LESSONS（vc=1，未達 distill-ready）—— 屬「manual session dense + routine 自轉正常 + heal cluster 集中 dna-checkup」的健康 shape。無新 REFLEXES promote，但 07-12 wake-guard 補的三條讀取鐵律 + wake-context 儀器化落地是 boot 層架構解，跟本 audit 找到的兩條 dormant entropy（alert recovery + mirror thick debt）呼應：sensor 生存週期紀律 + 三層 canonical ↔ mirror 薄殼紀律都是「儀器要自己會體檢」的具體 instantiation。

---

## Handoff

- **本 audit 給下一個 session**：
  - [ ] W29 audit 記得跑 `routine-sync-check.py` 對照本週 14 thick mirror 有無變化（哲宇若批量瘦身，thick count 應下降）
  - [ ] dashboard-alerts.json 5 條 stale 若過齡 >14 天，走 §Hard Gate 升 OBSERVER-QUEUE
  - [ ] `twmd-supporters-weekly` PR #1221 若 merge，補進 ROUTINE.md live 表 + 補 last_updated
- **繼承 172122-manual handoff（未消化）**：
  - [ ] 下週日 routine 首次自動廣播週報需盯一眼（本 audit 是 Sunday 21:00 fire，週報是 Sunday 02:14 已 ship）
  - [ ] unreachable 30 人（柒藍、ceruleanstring 領頭）等哲宇決定要不要一對一邀請
  - [x] 14 條 thick mirror 舊債 → **本 audit 已記 LESSONS §未消化，defer 給哲宇拍板**

---

🧬

_v1.0 | 2026-07-12 21:00 +0800 twmd-routine-audit-weekly cycle 10_
_誕生：Sunday 21:00 cron fire → BECOME Full 14/14 self-test PASS → Stage 1-6 走完 → append LESSONS 2 條 + report ship + git push main_
