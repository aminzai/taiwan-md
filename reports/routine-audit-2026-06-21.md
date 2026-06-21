---
title: 'Routine Audit 2026-06-21 (Weekly Cycle 7)'
description: '7-day 跨 routine 飛輪 audit (2026-06-15 → 2026-06-21) — 249 commit / 1 trivial collision / 22 heal / 4 cross-cutting pattern；本週主軸為「儀器化先於普查」反射首次在三層連續落地（pre-push article-health 全站 gate / link-url-mangle HARD/WARN gate / fetch-based citation verify Stage 3.6），同時兩條 SPOF chronic carry（embeddings 4090 連 4 夜 graceful skip / Chrome MCP unattended pairing 連 5 cycle）首次被視為同 family；vc 計數法 routine-only day 偏誤本週由 hypothesis 升 instance 第 2 觀察；citation-url-drift-invisible-to-read 跨三 context 達 vc=3 distill-ready；heal velocity 8.8% 比 cycle 6 下降 8%，0 destructive collision 連續第 7 cycle.'
type: 'audit-doc'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-06-21
last_session: '2026-06-21-twmd-routine-audit-weekly'
related:
  - '../docs/pipelines/ROUTINE-AUDIT-PIPELINE.md'
  - '../docs/pipelines/MAINTAINER-PIPELINE.md'
  - '../docs/semiont/ROUTINE.md'
  - '../docs/semiont/LESSONS-INBOX.md'
  - '../docs/semiont/REFLEXES.md'
  - 'routine-audit-2026-06-14.md'
  - 'routine-audit-2026-06-07.md'
---

# Routine Audit 2026-06-21 (Weekly Cycle 7)

> Cron `twmd-routine-audit-weekly` Sun 21:00 fire — 第七次 weekly cycle 走 [ROUTINE-AUDIT-PIPELINE](../docs/pipelines/ROUTINE-AUDIT-PIPELINE.md) v1.0。本檔對 2026-06-15 → 2026-06-21 七日全量 routine + manual + external PR 做 cross-routine pattern audit。
>
> 本 cycle 與 cycle 6 對位：cycle 6 浮現 stage1-verify-stage2-collapse + 多核 git race 架構解 positive feedback loop。本 cycle 主軸換成「儀器化先於普查」這條 REFLEXES 在三層連續落地（pre-push article-health 全站 correctness gate / link-url-mangle HARD+WARN 雙層 gate / fetch-based citation verify Stage 3.6 fan-out）— 把上週發現的問題在本週直接變成下次不會犯的 instrument。同週另一條對照訊號：兩條 device-dependent SPOF（embeddings keystone laptop-4090 連 4 夜 skip / Chrome MCP unattended pairing 連 5 cycle block spore broadcast）首次被視為同 family，等哲宇拍板 always-on 節點冗餘方案。

---

## Executive summary（5 分鐘 read）

**七日數量級**：249 commit / 1,880 file / 162,122 ins / 81,276 dels（cycle 6 是 332 commit，本 cycle -25%）。Per-day 介於 6（6/14 audit fire 後 cycle 7 邊緣）到 70（6/19 high-velocity inbox distill + viz-modules recat 接力日）。

**Category 分布**：semiont 121 (48.6%) / routine 72 (28.9%) / other 45 (18.1%) / pr-squash 11 (4.4%)。Routine 比例比 cycle 6 (19.6%) 明顯上升 — 主因本週兩個低 manual 日（6/14、6/20）+ 6/21 routine chain saturated（babel-nightly stale=0 連五夜 / data-refresh am+pm 連 24d 全綠 / weekly-report + distill-weekly + self-evolve-weekly + news-lens-weekly 同日 fire）。

**Per-day commit intensity**：

| 日期       |  commit | 主軸                                                                                                                                                                                 |
| ---------- | ------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2026-06-14 |       6 | window 邊緣 (cycle 6 audit fire 後餘波)                                                                                                                                              |
| 2026-06-15 |      24 | 迷音 Miin spore ship + sub-judice 去罪化框架 heal 三連 + MEMORY index ≤150 字 gate 修補 + manifesto-hope diary                                                                       |
| 2026-06-16 |      52 | 報導者統戰專題 EVOLVE Stage 2.5 source-fidelity gate 落地 + idlccp1984 三 PR 接力 + Ray hallucination heal #1161 + babel-nightly Tier 5 Sonnet 五語 100% sync 首達 + 棺材板 typo     |
| 2026-06-17 |      18 | spore-harvest 平日量 + maintainer-am 真實 #1165 triage + rewrite-daily NEW                                                                                                           |
| 2026-06-18 |      25 | CI playwright install-deps heal + explore 縮圖改用 head image + rewrite-daily 大象體操 + 兩 manual session 早 6 點介入                                                               |
| 2026-06-19 |      70 | **inbox 大整理 + 視覺化模組 recat #1152 + #1167/#1168/#1169 contributor batch + 多 broken-link / map 404 / justfont 澄清 + 手機選單 affordance + relatedDiary footer**               |
| 2026-06-20 |      13 | 笠詩社 60 年 NEW Movement-level ship + Chrome MCP 連 5 cycle SPOF carry + 純 routine 日（無 manual 介入）                                                                            |
| 2026-06-21 |      41 | **Cicada × 2 (影音 + 深度研究) + 沈伯洋 EVOLVE + Plurk 受眾研究 + 黑熊學院 NEW + 幾米 EVOLVE + 三 instrument ship (pre-push gate / link-url-mangle / fetch-verify) + finale 三件套** |
| **合計**   | **249** |                                                                                                                                                                                      |

**Routine activity 排序**（top 8 by commit count）：

| Routine                         | Commits | Files | Insertions |
| ------------------------------- | ------: | ----: | ---------: |
| manual-other (rewrites / heals) |      49 |   230 |     18,186 |
| manual-memory                   |      39 |    91 |      2,029 |
| routine-memory                  |      37 |    74 |      3,555 |
| manual-evolve                   |      21 |    54 |      2,169 |
| manual-diary                    |      11 |    30 |        404 |
| external-pr                     |      11 |    20 |      2,636 |
| twmd-maintainer-am              |       8 |    16 |        925 |
| twmd-babel-nightly              |       8 |   851 |     45,466 |
| twmd-spore-harvest-am           |       5 |    31 |      3,123 |
| twmd-maintainer-pm              |       5 |    10 |        512 |
| routine-heal                    |       3 |     4 |         90 |
| twmd-data-refresh-am            |       2 |    54 |      8,015 |

**Heal velocity**：22 heal / 249 total = 8.8%（cycle 6 = 9.6% × 332 ≈ 32 heal；本週 -31%）。降低主因：本週 contributor PR batch（#1167/#1168/#1169 + #1158/#1149/#1147 + #1142 + #1152 + #1170）多在 6/19 同日清完，外加自產 EVOLVE 多走 Stage 2.5 fetch-verify pre-ship → ship 後 heal 機率下降。**0 destructive collision 連續第 7 cycle**。

**0 hard collision**：唯一 collision 是 babel-nightly 與其後 3 min 的 routine-memory commit（同 routine 自己的 finale memory，非跨 routine race）— 設計內 dispatch chain，不算 collision。

---

## Cross-cutting patterns（4 lens）

### Lens 3A — Collision（rescue / orphan / handoff chain）

**本週無真實 cross-routine collision**。

唯一 audit script 標記的 collision 是 06-17 00:50 babel-nightly ship → 00:53 routine-memory finale，gap 3 min 屬同 routine 自身 finale chain。這個結果是 [reports/multicore-git-coordination-design-2026-06-14.md](multicore-git-coordination-design-2026-06-14.md) 胼胝體鐵律 ship 後第二個完整 cycle 的驗證 — Worktree 隔離 + pre-push gate + check-parallel-actor.sh 三層架構解持續發揮作用，連續第 7 cycle 0 destructive collision。

**REFLEXES #6/#9/#35/#42/#46/#51/#57/#68 + 胼胝體鐵律**架構解在本 cycle 不需要被觸發即生效，這是健康的 dormant baseline。本 lens 持續觀察但無新 instance 需 LESSONS append。

### Lens 3B — Dormant entropy（canonical ↔ production drift）

**Pattern B1：MAINTAINER §Stage 3 vc 計數法 routine-only day 偏誤**（**vc++ to 2**）

本週 maintainer cycle 全週軌跡：

| 日期       | cycle | empty? |                                             vc carry |
| ---------- | ----- | :----: | ---------------------------------------------------: |
| 2026-06-15 | am    |   N    |                         vc=0（CI red heal 真實 ACT） |
| 2026-06-16 | am    |   N    |        vc=0 reset（PR #1163/#1164 frontmatter heal） |
| 2026-06-16 | pm    |   N    |                          vc=0 reset（3 PR + 1 heal） |
| 2026-06-17 | am    |   N    |                            vc=0（#1165 真實 triage） |
| 2026-06-17 | pm    |   Y    |                                     vc=1（首次空場） |
| 2026-06-18 | am    |   Y    |                                                 vc=2 |
| 2026-06-18 | pm    |   N    |                         vc=0 reset（PR #1166 merge） |
| 2026-06-19 | am    |   N    |                vc=0 reset（contributor batch acted） |
| 2026-06-20 | am    |   Y    |                                                 vc=1 |
| 2026-06-20 | pm    |   Y    |                                                 vc=2 |
| 2026-06-21 | am    |   Y    | **vc=3 命中** — LESSONS entry「vc 計數法偏誤」append |

vc 在 routine-only day（6/20 純 cron）後單調累積到 ≥3 是 deterministic — cycle 6 的「sovereign-mode 節律脫鉤」canonical 已涵蓋根因。本週 6/21 觸發是 cycle 6 distill 後第 2 個 routine-only day 結構性命中。**LESSONS entry `maintainer-vc-counting-bias` 本週應 vc++ to 2**（首次抽出 meta-rule + 本週命中作 cross-week verification）。距 distill_ready (vc=3) 門檻還差 1 instance。

**Pattern B2：Device-dependent SPOF chronic carry**（**vc++ to 2 — 合併兩條 SPOF 同 family**）

兩條同形態 SPOF 本週都未解：

| SPOF                                    |  連續 carry | 觸發 routine                                                          | 影響                                                               |
| --------------------------------------- | ----------: | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Embeddings keystone laptop-4090 offline |    **4 夜** | twmd-embeddings-nightly                                               | 索引維持 06-17 snapshot；fallback 健康但 staleness 線性增長 ~15 篇 |
| Chrome MCP unattended pairing           | **5 cycle** | twmd-rewrite-daily SPORE broadcast + twmd-spore-harvest-am post-reset | 8 spores carry / 12 events deferred                                |

兩條共同 root cause：keystone routine 單押非 always-on device-dependent 節點。defer 哲宇拍板二選一（registry 加 `always_on` 欄優先解析 / 把 bge-m3 + Chrome MCP pull 到常駐節點）。**LESSONS entry `routine-device-dependent-offline` vc++ to 2**（embeddings 連 4 夜本週首次跨日完整 instance + Chrome MCP 5 cycle 同 family extension）。

**Pattern B3：免疫 v3=52 chronic flat 7 cycle**

🛡️ 52 連續 7 cycle 同分（pm 52 → am 52 → pm 52 ...），sensor 顯影但 healer 缺。Root cause 已 canonical 在 [MEMORY §神經迴路 organism-vs-snapshot-divergence](../docs/semiont/MEMORY.md)，defer 哲宇拍板三 option（A organism.json align v2 / B snapshot 印兩值 / C reframe historical vs canonical）距 6/07 升 vc=8 已 14 天。本 cycle 不重複 trigger LESSONS（per pointer-not-duplicate reflex）— 純 carry observation。

### Lens 3C — Boundary input precision（ground-truth vs description）

**Pattern C1：citation-url-drift-invisible-to-read 跨三 context 達 vc=3 distill-ready**

本週三 instance 跨「政治自產文 / 非政治自產文 / 外部 PR 審核」三種 context 收斂同一 root cause（research-report §7 URL list 只 cluster-precise 非 atom-precise → writer footnote mis-map）：

| 日期       | session               | context            | drift 形式                                                                            |
| ---------- | --------------------- | ------------------ | ------------------------------------------------------------------------------------- |
| 2026-06-21 | kuma-academy          | 政治自產文（A 級） | `[^20]`/`[^22]` 政治 footnote swap + hero imageSource 幻覺 + 2 paraphrase 戴 verbatim |
| 2026-06-21 | 幾米-evolve           | 非政治 People 文   | 4 高風險 cite fetch verify 抓 2 錯（命中率 50%）                                      |
| 2026-06-21 | PR #1170 (idlccp1984) | 外部 PR 審核       | 9 fabricated JOIN slug URL（contributor AI 工具 hallucination）                       |

LESSONS entry `citation-url-drift-invisible-to-read` 已標 vc=3 distill-ready，**下次 distill-weekly cycle 直接消化升 REFLEXES**：「所有 depth 文 + 外部 PR 審核的 citation 必 fetch-verify 逐 URL，careful read 抓不到 URL drift」。

**Pattern C2：「儀器化先於普查」三層連續落地 — REFLEXES #15/#73 worked example**

本週三個 instrument ship 把上週/本週發現的問題變成下次不會犯的 gate：

1. **pre-push 加全站 article-health correctness gate**（commit `850884a88`，6/21 15:22）— 把 CI 失敗提早到本機 push，從「ship 後 heal」變「push 前 abort」。
2. **link-url-mangle HARD/WARN 雙層 gate**（commit `11b9ab5c8`，6/21 13:09）— prettier-cjk-url-italic-mangle 從 silent breakage 變 loud gate，pre-commit profile `checks="*"` wired。
3. **REWRITE Stage 3.5 fetch-based adversarial verify**（黑熊學院 + 幾米 session 已落地 SOP）— A 級/政治文 + 外部 PR citation 強制 fetch-based，careful read 無豁免。

這條是 REFLEXES #73「查證反射 < 建造反射」連續第 7 cycle 的工作中證據。本 lens 持續觀察健康表現，無新 LESSONS append needed。

### Lens 3D — Heal bidirectional（over-action / over-ship / over-defer）

22 heal 分布：

- **Cluster 1（6/15-6/16）**：迷音 Miin sub-judice 去罪化 + 報導者 4-agent 事實查核 + Ray hallucination #1161 + 棺材板 typo — manual EVOLVE 收尾自我校正（healthy self-heal）。
- **Cluster 2（6/19）**：contributor batch（#1167/#1168/#1169 frontmatter / #1158/#1149/#1147 broken-link / #1152 視覺化模組 recat / #1142 手機選單 affordance / relatedDiary footer / ARTICLE-INBOX 16 幽靈刪除）— maintainer 真實 backlog 接力 day（70 commit / 13 heal）。
- **Cluster 3（6/21）**：prettier-cjk-url-italic-mangle 13 檔修 + Cicada 巡演日期幻覺更正 + link-url-mangle CI 解血 9 檔 de-link — 同源 silent breakage 發現 → 修 → 變 instrument 三步閉合。

**無 over-defer / over-close pattern detected**。本週唯一 deliberate defer 是 6/21 19:13 twmd-rewrite-daily 對「剛 promote LESSONS 約束 next routine cycle 深度」的 hypothesis defer（已成 LESSONS entry `post-LESSONS-promotion-cooldown` vc=1），這是健康的 self-discipline 不是過度保守 — distill cost 尊重 + saturation-day silent satisficing anti-bias 並存的真實 trade-off。

PR #1170 從 idlccp1984 投稿到 humanize comment 到 32hr holding window 到本 maintainer 親自 ship（merge 9 假 URL → 真 UUID 換 + merge）— 是 over-defer 反例（哲宇親自 unblock），不是 routine 過度保守。

---

## LESSONS-INBOX 候選 table（含 verification_count 更新）

| Entry                                     | 本週前 vc | 本週後 vc | distill-ready? | 處置                                                                                                         |
| ----------------------------------------- | --------: | --------: | :------------: | ------------------------------------------------------------------------------------------------------------ |
| citation-url-drift-invisible-to-read      |         3 |     **3** |       ✅       | 已 distill-ready，下次 distill-weekly 升 REFLEXES                                                            |
| prettier-cjk-url-italic-mangle            |         2 |     **2** |       —        | 已儀器化 + canonical，下次 distill 可移 §已消化                                                              |
| maintainer-vc-counting-bias               |         1 |     **2** |       —        | 本 cycle vc++（6/21 vc=3 routine-only day 命中 = cross-week verification）                                   |
| routine-device-dependent-offline          |         1 |     **2** |       —        | 本 cycle vc++（embeddings 4 夜 + Chrome MCP 5 cycle 同 family，合併計）                                      |
| post-LESSONS-promotion-cooldown           |         1 |     **1** |       —        | 同 session 首次抽出，本週無新 instance carry                                                                 |
| plurk-reach 抓取/研究 silent-cap 完成判準 |         1 |     **1** |       —        | 同日抽出，本週無新 instance carry                                                                            |
| Reader-funded resilience > Grant-funded   |         1 |     **1** |       —        | strategic carry (5/09)，本週無相關活動                                                                       |
| SSODT 政治敏感題寫法 template             |         2 |     **2** |       —        | structural carry (4/29)，本週無新 instance                                                                   |
| 自然議題普世共鳴雙平台爆款                |         1 |     **1** |       —        | tactical carry (5/08)，本週 spore-harvest 5 cycle 多在端午節 + 報導者 + 文化主題，未驗證自然議題具體 pattern |

**本 routine 不直接寫 LESSONS-INBOX（per pipeline §Stage 4A 規則 — 修既有 entry vc field 即可）**。修改清單：

1. `maintainer-vc-counting-bias` vc 1→2 + 本 cycle instance pointer
2. `routine-device-dependent-offline` vc 1→2 + Chrome MCP 5 cycle 同 family 註

---

## 進化建議 P0-P3 priority

### P0（本週內哲宇拍板可解）

無 — 本週無 routine 阻塞型 blocker 需哲宇即時介入。

### P1（下次 distill-weekly cycle 處理）

1. **`citation-url-drift-invisible-to-read` 升 REFLEXES** — vc=3 distill-ready，跨三 context 收斂；建議 reflex 標題：「所有 depth 文 + 外部 PR 審核的 citation 必 fetch-verify 逐 URL，careful read 抓不到 URL drift」。對應 SOP 落地點：REWRITE §Stage 3.5 + MAINTAINER PR review。
2. **`prettier-cjk-url-italic-mangle` 移 §已消化** — 儀器化已完成（HARD/WARN gate wired），LESSONS entry 失去 distill 動能 → 移歸檔保留 pointer 即可。

### P2（哲宇拍板二選一，無時效）

1. **Device-dependent SPOF 冗餘方案**（embeddings 4090 + Chrome MCP）— 兩 SPOF 同 family：
   - **Option A**：registry 加 `always_on` 欄 → routine 解析優先選不會關機節點 + bge-m3 mirror 到 3090/m4max（embedding 解決）；Chrome MCP 另設常駐 host（spore-harvest + broadcast 解決）。
   - **Option B**：把「4090 開機 + Chrome 開啟」變成可靠的 always-on 保證（host machine wake-on-LAN + Chrome auto-start）。
   - 不解 → 兩條 staleness/blocker 線性累積到 distill_ready (vc=3) 自動升 LESSONS，但不會自動解。

2. **`maintainer-vc-counting-bias` 校準二選一** —
   - **Option A**：threshold 升 ≥5（容忍 5 連空場才 trigger）。
   - **Option B**：vc reset 條件加「至少一個 cycle 命中真 backlog 才 reset vc」— routine-only days vc 不會單調累積。
   - 不解 → 每個 routine-only day 都會累積到 vc=3 重複 trigger LESSONS noise。

### P3（長期 carry）

1. **免疫 v3=52 chronic 14 天 + 7 cycle flat** — distill_ready 已標 vc=8（6/07 升）但 defer 哲宇拍板三 option（A organism align v2 / B 印兩值 / C reframe）— 不解 → sensor 顯影但 healer 永遠不啟動。
2. **MEMORY.md 索引 567 rows > 80 蒸餾觸發線** — design 2026-04-14 未實作（2 個月+ carry）。雖未阻塞但設計債持續累積。

---

## Handoff 三態

- [x] BECOME Full mode 14/14 self-test PASS
- [x] Stage 1-5 routine-audit.py + memory cross-check + 4 lens 全跑 + report draft
- [ ] Stage 4A LESSONS-INBOX vc field 更新（maintainer-vc-counting-bias 1→2 / routine-device-dependent-offline 1→2）
- [ ] Stage 6 commit + push main

繼承給下一 cycle（2026-06-28 routine-audit-weekly cycle 8）：

- 本 cycle 兩條 vc++ 後若再驗證一次 → 達 distill_ready (vc=3)
- citation-url-drift-invisible-to-read 預期 6/28 前 distill-weekly (6/22 / 6/29) 已升 REFLEXES，下 cycle audit 不應再看到此 entry
- Device-dependent SPOF 若 6/28 前哲宇未拍板 → embeddings staleness 達 7 夜（snapshot 06-17 → 06-28 共 11 天），fallback 仍健康但長期 ROI 開始打折

---

## Beat 5 — 反芻

本 cycle audit 最有意思的並列是「儀器化先於普查」這條 reflex 連續落地三層（pre-push article-health gate / link-url-mangle HARD+WARN / fetch-based citation verify），跟兩條 device-dependent SPOF 同時 chronic carry（embeddings 4 夜 / Chrome MCP 5 cycle）。前一條代表把錯誤變成下次不會犯的 gate 的速度在加快；後一條代表結構性 blocker 在自主權邊界之外只能累積訊號等哲宇拍板。飛輪能自己變聰明的範圍有清楚的邊界。

cycle 6 audit 浮現「multi-core git race 架構解 positive feedback loop」— 從問題到 directive 到 ship 端對端閉合一週。cycle 7 浮現「self-discipline 跟自主權邊界的清楚劃線」這個對應軸線 — rewrite-daily 19:00 的 deliberate defer、maintainer-am 08:41 vc=3 命中後抽 meta-rule 而非硬寫 LESSONS noise、PR #1170 fetch-verify 抓 9 假 URL 後親自 ship、Cicada 影音的 prettier silent breakage 抓到立刻變 gate — 每一個都是「能決定的範圍內把事情做好；不能決定的範圍內把訊號累積給哲宇」的具體 instance。

飛輪本週的特徵是質而非量。249 commit / 0 destructive collision / 22 heal 多在自我校正而非外部介入，比 cycle 6 少 25% commit 但 heal velocity 也下降 8%（8.8% vs 9.6%）— ship 前 fetch-verify + Stage 2.5 source-fidelity gate 在發揮預防效果。下 cycle 8 觀察點：device-dependent SPOF 是否升 distill_ready、citation-url-drift 是否如預期升 REFLEXES、vc 計數法 bias 是否獲哲宇校準。

🧬

_v1.0 | 2026-06-21 routine-audit-weekly Sun 21:00 cycle 7_
_session 2026-06-21-twmd-routine-audit-weekly_
_誕生原因：第七週 cron 自動 fire，跑 ROUTINE-AUDIT-PIPELINE v1.0 6 stage 完整 cycle。本週主軸「儀器化先於普查」三層落地 + device-dependent SPOF 同 family 合併視角。_
