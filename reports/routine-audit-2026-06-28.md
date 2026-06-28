---
title: 'Routine Audit 2026-06-28 (Weekly Cycle 8)'
description: '7-day 跨 routine 飛輪 audit (2026-06-22 → 2026-06-28) — 192 commit / 0 collision 連 8 cycle / 15 heal / 4 cross-cutting pattern；本週主軸為「REFLEXES #76 multi-cycle trend window 當天 promote + 當天 dogfood」三 routine same-day 引用同步落地，sub-agent self-report vs grep ground truth (#42 silent satisficing) 跨夜 vc=3 promote-ready，rewrite-daily-post-manual-recency-collision vc=5 含新 facet「post-finale 4-commit continuation cluster」；同時揭出 routine-audit.py ROUTINE_PATTERNS list 寫死 14 條與實際 commit subject convention drift 12% 落 unclassified（script self-blindness 第一個 instance）；heal velocity 7.8% 比 cycle 7 下降 1pp，0 destructive collision 連續第 8 cycle.'
type: 'audit-doc'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-06-28
last_session: '2026-06-28-twmd-routine-audit-weekly'
related:
  - '../docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - '../docs/pipelines/MAINTAINER-PIPELINE.md'
  - '../docs/semiont/ROUTINE.md'
  - '../docs/semiont/LESSONS-INBOX.md'
  - '../docs/semiont/REFLEXES.md'
  - 'routine-audit-2026-06-21.md'
  - 'routine-audit-2026-06-14.md'
---

# Routine Audit 2026-06-28 (Weekly Cycle 8)

> Cron `twmd-routine-audit-weekly` Sun 21:00 fire — 第八次 weekly cycle 走 [ROUTINE-AUDIT-PIPELINE](../docs/pipelines/ROUTINE-AUDIT-PIPELINE.md) v1.0。本檔對 2026-06-22 → 2026-06-28 七日全量 routine + manual + external PR 做 cross-routine pattern audit。
>
> 本 cycle 與 cycle 7 對位：cycle 7 主軸為「儀器化先於普查」三層落地 + 兩條 SPOF chronic carry 首次視為同 family。本 cycle 主軸換成「REFLEXES #76 multi-cycle trend window 當天 promote 當天 dogfood」三 routine same-day 引用（data-refresh-am 06:12 / feedback-triage 07:08 / rewrite-daily 19:12）同步落地。對照訊號：本 audit 自己揭出 `routine-audit.py` ROUTINE_PATTERNS list 寫死 14 條與實際 commit subject convention drift 達 12%（25/192 落 unclassified）— 飛輪自審腳本第一個結構性自盲 instance。

---

## Executive summary（5 分鐘 read）

**七日數量級**：192 commit / 2,899 file / 135,208 ins / 67,055 dels（cycle 7 是 249 commit，本 cycle -23%）。Per-day 介於 4（6/21 cycle 邊緣）到 35（6/24 peak，2 manual finale + 多 routine cluster）。

**Category 分布**：semiont 96 (50.0%) / routine 65 (33.9%) / other 25 (13.0%) / pr-squash 6 (3.1%)。other 比例 +13pp vs cycle 7 (18.1%) — 主因 `routine-audit.py` ROUTINE_PATTERNS gap，並非真實 unclassified 增加（見 §Lens 3B）。

**Per-day commit intensity**：

| 日期       |  commit | 主軸                                                                                                                                                                                             |
| ---------- | ------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-06-21 |       4 | window 邊緣 (cycle 7 audit fire 後餘波)                                                                                                                                                          |
| 2026-06-22 |      28 | embeddings 連 5 夜 fleet-down 升 vc=3 + babel-nightly 3 bug 連鎖揭發 + LESSONS routine-device-dependent-offline vc 2→3 + 高畫質 YAML heal                                                        |
| 2026-06-23 |      15 | low-velocity routine day (refresh am + feedback-triage no-op 連 4) + companies i18n 6 lang heal                                                                                                  |
| 2026-06-24 |      35 | **peak day** — 龜山島方向勘誤 + relatedDiary 集體回補 12 篇 + content-dates regen + 多 routine cluster                                                                                           |
| 2026-06-25 |      32 | spore #150 post-ship verify 教訓 (profile feed propagation lag) + 鼎泰豐/蓬萊米 heal cluster + mini-taiwan-pulse 標題收短 + immune 51→50 一步漂移                                                |
| 2026-06-26 |      29 | **contributor escalation day** — #1179 迪士尼 merge → #1180 issue 升 → pm 4th heal (footnote canonical [N]→[^N]) + #1178 烏坵 / #1174 滿月習俗 deep-heal + 聲景 NEW ship + saturation-defer vc=4 |
| 2026-06-27 |      23 | 紀懷新 NEW 深度文 ship (full REWRITE multi-agent) + 紀懷新孢子 #152/#153 雙平台 + v1.11.0 release + About 第 102 天里程碑 + idlccp1984 連 5 PR 第 5 篇 (#1181 保齡球) merge + 4 heal             |
| 2026-06-28 |      26 | **REFLEXES #76 promote day** — W26 distill #75 + W26 self-evolve #76 同 cluster + 陳嫺靜 NEW + 金曲獎 NEW 拆+rename+redirect + REWRITE v7.6 spine-type fork + MANIFESTO §11.4 commit 寫人話 紀律 |
| **合計**   | **192** |                                                                                                                                                                                                  |

**Routine activity 排序**（top 8 by commit count，已校正 unclassified gap）：

| Routine                                      | Commits | Files | Insertions |
| -------------------------------------------- | ------: | ----: | ---------: |
| manual-other (rewrites / heals / evolves)    |      39 |   258 |     35,077 |
| routine-memory                               |      33 |    65 |      3,241 |
| manual-memory                                |      22 |  1701 |      5,328 |
| manual-evolve                                |      21 |    80 |      9,021 |
| manual-diary                                 |      14 |    49 |        680 |
| twmd-data-refresh-am/pm (含 `refresh:` 短稱) |      10 |     ~ |          ~ |
| twmd-maintainer-am                           |       8 |    13 |        735 |
| twmd-maintainer-pm                           |       7 |    39 |      4,870 |
| twmd-babel-nightly                           |       7 |   271 |     24,099 |
| twmd-feedback-triage (script gap, 短稱)      |       7 |     ~ |          ~ |
| external-pr                                  |       6 |     6 |        352 |
| twmd-spore-harvest-am                        |       5 |    23 |      2,047 |

**Heal velocity**：15 heal / 192 total = **7.8%**（cycle 7 = 8.8%，本週 -1pp）。降低主因：本週 contributor PR batch（#1179 / #1178 / #1174 / #1181）多走 post-merge deep-heal 但每件 heal 數 ≤ 4，加上 6/28 大日 manual ship 走全 REWRITE multi-agent pre-ship verify → ship 後 heal 機率下降。**0 destructive collision 連續第 8 cycle**。

**0 hard collision**：本 cycle script 標記 0 collision。Worktree 隔離 + pre-push gate + check-parallel-actor.sh 三層架構解持續 dormant baseline。

---

## Cross-cutting patterns（4 lens）

### Lens 3A — Collision（rescue / orphan / handoff chain）

**本週無真實 destructive collision，但有 3 條 cross-routine handoff chain instance**：

1. **6/28 babel-nightly main session 接住 sub-agent es+fr URL convention drift** — Tier 0a sub-agent 自陳「matched sibling」實際沒 grep ≥3 sibling bullet，主 session post-dispatch verify 抓到 `/es,fr/people/chi-huai-hsin` 違 sibling `/people/{zh-slug}` 慣例 → inline python3 regex heal 全 5 lang body。這是 REFLEXES #42 sub-agent silent satisficing 第三次跨夜 instance（6/26 es URL → 6/27 ja footnote → 6/28 es+fr URL）vc=3 promote-ready，**main session 是 handoff chain 的接力者非旁觀者**。
2. **6/26 contributor escalation 跨 morning→pm 接力** — 08:42 maintainer-am ship #1179 迪士尼 merge + 3 heal + polish-hint reply → 8hr 後 contributor 升 #1180 issue「為何沒檢查就直接發送」→ 22:08 maintainer-pm 接住做 4th deep-heal (31 footnote [N]→[^N] canonical) + 道歉 reply。**morning polish-hint 路徑被 contributor 解讀為「沒檢查」是 maintainer relationship 紀律 gap**（升 LESSONS candidate `polish-hint-default-broken` 見 Stage 4）。
3. **6/19 dirty tree 第 11 天跨 routine handoff carry** — `docs/semiont/diary/2026-06-19-102716-視覺化型錄-recat.md` + `reports/article-evolve/端午節.md` 殘留髒 tree 跨 data-refresh-am/pm / maintainer-am/pm / feedback-triage 多 routine 11 cycle handoff，每 cycle auto-stash + restore 不阻塞但 chronic carry。**housekeeping chip 已 spawn 等哲宇一鍵清**（per 6/26 am memory），non-action chronic carry 跨 cycle 是「感知到 → 沒 action」紀律邊界 instance — 與 immune 50 chronic 4 cycle 持平共享同 anti-pattern。

REFLEXES #6/#9/#35/#42/#46/#51/#57/#68 + 胼胝體鐵律架構解持續 dormant baseline，本 lens **無新 LESSONS append** —— chain instance 1 已 vc=3 promote-ready 進 §未消化 babel-nightly entry；instance 2 升 polish-hint-default-broken 新 entry；instance 3 是非結構性 chronic noise，不單獨開 LESSONS。

### Lens 3B — Dormant entropy（canonical ↔ production drift）

**本週 distinct instance：`routine-audit.py` ROUTINE_PATTERNS list ↔ ROUTINE.md SSOT 漂移**。

跑 `python3 scripts/tools/routine-audit.py --last-week` 後 192 commit 中 25 條（13%）落 `unclassified/other` category。逐條檢視揭：

| Unclassified subject prefix            | Commit count | 應屬 routine                          | 漂移原因                                                                      |
| -------------------------------------- | -----------: | ------------------------------------- | ----------------------------------------------------------------------------- |
| `[routine] refresh:`                   |           10 | twmd-data-refresh-am/pm               | script pattern 寫死 `twmd-data-refresh-am/pm`，commit subject 簡稱 `refresh:` |
| `[routine] twmd-feedback-triage:`      |            7 | twmd-feedback-triage                  | ROUTINE_PATTERNS list 不含 feedback-triage                                    |
| `[routine] evolve:`                    |            2 | routine-evolve (LESSONS vc++ commits) | list 不含 routine-evolve category                                             |
| `[routine] data-refresh-am:`           |            1 | twmd-data-refresh-am                  | 短稱 (無 `twmd-` prefix)                                                      |
| `[routine] data-refresh-pm:`           |            1 | twmd-data-refresh-pm                  | 短稱                                                                          |
| `[routine] twmd-rewrite-daily:`        |            1 | twmd-rewrite-daily                    | script pattern 寫 `twmd-rewrite:` 但實際 commit 用 `twmd-rewrite-daily:`      |
| `[routine] twmd-routine-audit-weekly:` |            1 | twmd-routine-audit-weekly             | 飛輪自審 routine **自己不在 list 內**                                         |

**結構意義**：腳本層 ROUTINE_PATTERNS list（routine-audit.py L32-47）是 written-2026-05-16 freeze frame，ROUTINE.md SSOT 是 live + 6 新 weekly routines（self-evolve / weekly-report-sun / distill / news-lens / routine-audit 含本身 + embeddings-nightly）添加期間 drift。**這是飛輪自審腳本第一次被自己揭出結構盲點 — script self-blindness instance**。

**修補方向**：

- (a) ROUTINE_PATTERNS list 同步 ROUTINE.md SSOT（含 `[routine] refresh:` `[routine] data-refresh-am/pm:` 短稱 + `twmd-rewrite-daily:` + `twmd-feedback-triage:` + `twmd-routine-audit-weekly:` + `twmd-embeddings-nightly:`）
- (b) 加 lint：list 缺項對應 `[routine] X:` prefix 出現在 7-day window 就 warning
- (c) 本 audit 結果留 13% other rate 當 baseline，下次 audit 修補後驗 ≤ 3%

**升 LESSONS candidate** `routine-audit-script-classification-gap` vc=1（見 Stage 4）。

### Lens 3C — Boundary input precision（ground-truth vs description）

**本週兩條 instance**：

1. **#42 sub-agent self-report vs grep ground truth — 跨夜 vc=3 promote-ready**（接續 Lens 3A instance 1）。三夜連續 sub-agent 自陳「matched sibling convention」實際沒 grep ≥3 sibling bullet：6/26 es URL → 6/27 ja footnote → 6/28 es+fr URL。**Pattern 屬 LLM sub-agent 平行 dispatch 的結構性盲點，跨 lang 共通**：cover policy 取代 ground truth。改進方向 per 6/28 babel-nightly memory「sibling sample 從 sub-agent 自己 grep 變成 task JSON hardcode」把判斷標準從 sub-agent 直覺移到主 session 預處理。已 §未消化 buffer 不重複 promote。

2. **6/28 manual 金曲獎 spine 預設揭出**（LESSONS-INBOX line 489 已 vc=3）— v1 「核心矛盾」spine 寫成「金曲獎 vs 黑潮」論戰被退稿「會炎上」→ v2 立體群像。**REWRITE v7.6 Stage 0 spine-type fork**（`d56f14e6f`）落地：受愛戴的機構/傳統預設「立體群像」，不是核心矛盾。哲宇親自 callout + 明示「讓未來預設就是」= fast-track promote candidate，已 §未消化 vc=3 等 distill。

**本 lens 持續觀察，不重複 append LESSONS**（兩 instance 已在 buffer）。

### Lens 3D — Heal bidirectional（over-action / over-ship / over-defer）

**本週三 instance，均屬 LESSONS append/bump 範圍**：

1. **`rewrite-daily-post-manual-recency-collision` vc=5 含 6/28 新 facet**（既有 §未消化 line 317）— 6/28 19:12 cron fire DEFERRED post-saturation 第 5 cycle。新 facet「post-finale 4-commit continuation cluster wall-clock window，不只最後一 commit timestamp」：今天 manual finale 後又 ship 4 commit (§11.4 commit 寫人話 + memory + maintainer-am routine + diary)，距最後 manual commit 8hr 看似清 4hr recency rule（per 6/26 mitigation 提案），但 per REFLEXES #76 multi-cycle accumulation > single-cycle delta 套到 saturation：**per-day total throughput 才是真 signal**。本 audit cross-verify 確認 vc=5 promote-ready，**不再額外 bump vc**（已 6/28 routine 自己 logged）。

2. **NEW `polish-hint-default-broken` vc=1**（升 LESSONS）— 6/26 maintainer-am 八點 ship #1179 迪士尼 merge + 3 heal + polish-hint reply (4 條 polish hint 含 footnote canonical 格式 + 配圖 + 描述加長 + 閻奕格 source)。但 contributor idlccp1984 8hr 後升 #1180 issue「為何沒檢查就直接發送」→ pm 22:08 deep-heal 31 footnote canonical + 道歉 reply。**maintainer 預設「polish-hint 路徑」對 contributor 等於「下次再說 = 不會做」**（per 6/26 pm memory「下次再說對發 PR 的人 = 不會做，跟 stale issue=對外失聯對稱」）。

3. **NEW `contributor-pr-burst-pattern` vc=1**（升 LESSONS）— idlccp1984 48hr 連 5 PR (#1179 迪士尼 / #1178 烏坵 / #1174 滿月習俗 / #1180 follow-up issue / #1181 保齡球)，前 2 hold + 中 1 deep-heal + 最後 1 merge+heal。**maintainer 該給累積式建議非逐 PR 獨立 polish-hint**（per 6/27 pm memory candidate）。本 entry vc=1 等下一個 contributor 連 ≥3 PR/48hr instance 累積。

**本 lens 共升 2 新 LESSONS entry + 1 既有 vc=5 cross-verify**（見 Stage 4）。

---

## Meta-pattern observation（跨 4 lens）

**REFLEXES #76 multi-cycle trend window 當天 promote 當天 dogfood**：

- 04:16 W26 self-evolve fire promote REFLEXES #76 vc=5 cross-routine cluster
- 06:12 data-refresh-am memory 引用 #76 解釋 plugin_health 36→32 sub-signal divergence
- 07:08 feedback-triage memory 引用 #76 治「9 cycle no-op 讀成警訊 = over-reading bias」
- 19:12 rewrite-daily memory 引用 #76 把 saturation-defer 維度從 4hr window 擴成 per-day throughput

**Promotion → immediate same-day adoption 三 routine cross-cycle dogfood 是健康 signal**。但 6/28 self-evolve memory 自己已 callout 反 pattern hypothesis：「W27 必 explicit 自問是否還有非 cross-routine 收斂層 pattern — self-evolve 連 2 週都在收斂層 promote（W25 #73/#74 + W26 #76）= 飛輪自己變聰明 OR retrieval bias 警示」。

**本 audit 結論**：cycle 8 不單獨 promote「same-day-instance」當 meta-pattern（會雙重計算 #76 本體已 promote）。W27 audit cycle 9 explicit 校驗：(a) #76 7-day 引用 count 跟 routine 多樣度（避免單 routine 過度引用）/ (b) self-evolve W27 是否能識別非收斂層 pattern。

---

## LESSONS-INBOX 候選 table

| 候選                                              |  vc | severity                | 處置                                                                                                    |
| ------------------------------------------------- | --: | ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `rewrite-daily-post-manual-recency-collision`     |   5 | structural              | 既有 line 317；本 audit cross-verify 新 facet「post-finale 4-commit cluster」；vc=5 不 bump，等哲宇拍板 |
| `routine-audit-script-classification-gap` ⭐ NEW  |   1 | structural              | append 本 audit；ROUTINE_PATTERNS list ↔ ROUTINE.md SSOT 漂移 12% other rate                            |
| `polish-hint-default-broken` ⭐ NEW               |   1 | maintainer-relationship | append 本 audit；6/26 #1180 escalation 已記憶層 candidate，audit 抽出升 LESSONS                         |
| `contributor-pr-burst-pattern` ⭐ NEW             |   1 | maintainer-pattern      | append 本 audit；6/27 pm memory candidate，audit 抽出升 LESSONS                                         |
| `subagent-self-report-vs-grep-ground-truth` (#42) |   3 | reflex-instance         | 既有 §未消化 (line 354+)；本 audit 確認 vc=3 跨 6/26-6/28，已 promote-ready 不重複 entry                |
| `spine-type-default-by-topic-category`            |   3 | content-rewrite         | 既有 §未消化 line 489；fast-track promote candidate，本 audit cross-verify                              |

---

## 進化建議（P0-P3）

| Priority | 建議                                                                                                                         | 預估成本   |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **P0**   | `routine-audit.py` ROUTINE_PATTERNS list 同步 ROUTINE.md SSOT（含 7 條 missing pattern）+ 加 lint 防漂移                     | 30 min     |
| **P0**   | 哲宇拍板 `rewrite-daily-post-manual-recency-collision` mitigation 路徑（manual-recency-defer rule promote 或反向 retire）    | observer   |
| **P1**   | `polish-hint-default-broken` 升 MAINTAINER-PIPELINE §post-merge polish-hint template（明示「下次寫法，本篇若想改請說一聲」） | 1 hr       |
| **P1**   | W27 audit cycle 9 explicit 校驗：(a) #76 引用 count + routine 多樣度 / (b) self-evolve W27 是否能識別非收斂層 pattern        | next audit |
| **P2**   | `contributor-pr-burst-pattern` 等下一個 ≥3 PR/48hr instance vc=2，未達不行動                                                 | passive    |
| **P3**   | 6/19 髒 tree housekeeping chip 哲宇一鍵清（chronic carry 第 11 天）— **routine 不替哲宇 push, 等 in-loop**                   | observer   |

---

## Stage 6 SHIP

```bash
git add reports/routine-audit-2026-06-28.md docs/semiont/LESSONS-INBOX.md
git commit -m "🧬 [routine] twmd-routine-audit-weekly: cycle 8 — 192 commit / 0 collision 連 8 cycle / 15 heal / 4 cross-cutting pattern / 3 new LESSONS — 2026-06-28"
git push origin main
```

---

🧬

_v1.0 | 2026-06-28 21:30 +0800_
_session 2026-06-28-twmd-routine-audit-weekly — cron Sunday 21:00 fire 第 8 cycle_
_主軸：REFLEXES #76 same-day promote+dogfood 三 routine 引用同步落地 + script self-blindness 第一個 instance 揭出 + heal velocity 7.8% 連 8 cycle 0 destructive collision_
_核心精神：4 lens framework 完整跑 + LESSONS verification_count 累積驅動 distill + meta-pattern 觀察延後 W27 cross-verify_
