---
session_id: '2026-06-28-041639-twmd-self-evolve-weekly'
date: 2026-06-28
type: 'cron-routine-memory'
routine: 'twmd-self-evolve-weekly'
mode: 'full'
canonical_ship:
  - 'REFLEXES #76 promote'
  - 'LESSONS-INBOX §已消化 distill row'
  - 'DIARY §反覆出現的思考 [→canonical] marker'
commit: '0a0d4542b'
---

# 2026-06-28 04:16 — twmd-self-evolve-weekly W26

## BECOME ack

- **mode**: full (cron routine, strict gate per task prompt)
- **organ snapshot (live)**: 🫀90↑ 🛡️50→ 🧬95↑ 🦴90→ 🫁85→ 🧫88↑ 👁️90→ 🌐93↑
- **lowest organ**: 🛡️50 immune chronic flat 4 cycle（呼應今日 ship 主題：multi-cycle accumulation 才是 ground truth，single-cycle drift 不升 alert）
- **vitals**: articles=825 / contributors=61 / 7d=+27 / 30d=+149 / i18n en828 ja823 ko824 es823 fr824
- **48hr cron rhythm**: data-refresh × 3 (am/pm/am) / spore-harvest 1st fail / feedback-triage no-op×2 / maintainer × 3 / babel-nightly stale=0 連 11 夜 / news-lens-weekly W26 7 P1 / weekly-report-sun W26 Resend 200 / distill-weekly W26 #75 promote + #42×3 fold
- **MEMORY tail 3 sessions**: babel-nightly 2026-06-28 #42 vc=3 promote-ready / news-lens-weekly W26 12 P1 carry + CTR catastrophic 4 件 / 昨晚 distill 已 ship #75
- **Q14 cross-session continuity**: 過去 2 天 = release v1.11.0 (562 commit/14 天) + #1181 保齡球 merge + 紀懷新 NEW + 孢子 #152/#153 + babel 連 11 夜 stale=0 + distill W26 #75 promote — 飛輪自轉清 entropy 健康 living proof

## Stage 1-2 Setup + 讀檔

- `git checkout main && git pull origin main` — already up to date
- 完整讀 LONGINGS.md / UNKNOWNS.md / REFLEXES §index + §catalog / DIARY §反覆出現的思考 / MEMORY tail 20 row + §神經迴路 + git log 48hr
- 確認剛剛 03:17 W26 distill 已 ship #75 + #42×3 fold + #38/#40 fold + MEMORY §神經迴路 stale-issue + SPORE-INBOX 53→48 auto-drop 5

## Stage 3 — Pattern identification (≥3 浮現未儀器化)

對照 DIARY §反覆出現的思考 + REFLEXES catalog + LESSONS-INBOX §未消化 識別 3 候選 pattern：

### Pattern A (PRIMARY ship)：Multi-cycle trend window > single-cycle delta — sensor 判讀 vc 鐵律閾值

**vc=5 across 4 routines in 3 days, 明文 cross-routine reference 同紀律**：

- 6/25 PM CF 404 vc=2「升勢回檔第 2 cycle」
- 6/26 AM CF 404 vc=3「reversal 成立」+ immune 50 chronic 第 2 cycle
- 6/26 PM CF 404 vc=4 LESSONS candidate `cf-404-multi-cycle-trend-vs-single-cycle-delta` + immune 第 3 cycle
- 6/27 AM CF 404 vc=5「已正式成形」5 cycle 累積 -1.27pp + immune 第 4 cycle
- 6/27 spore-harvest 1st fail silent retry 明文「跟 immune 50 narrow-band carry + CF 404 single-cycle delta 不升結論共享 multi-cycle window 紀律」
- 6/27 maintainer-am 明文「vc 鐵律閾值是 3 不是 1...跟 CF 404 multi-cycle / immune 50 持平共享紀律：single-cycle 不升 vc，跨多 cycle 才升」

**Status**: LESSONS-INBOX §未消化 NOT yet（MEMORY rows 都 cite「LESSONS candidate」flag，但今晨 distill 沒處理）/ REFLEXES NOT yet。Distill 漏接 = self-evolve 接力。

### Pattern B (carry, vc=1, 不 ship 待累積)：polish-hint-default-broken

- 6/26 PM #1180 contributor escalation「為何沒檢查就直接發送」揭 morning polish-hint 路徑被 contributor 解讀「沒檢查」是 maintainer 溝通 gap
- vc=1，僅一次明確 instance，待 vc++ 不單獨 promote

### Pattern C (carry, vc=1, 不 ship 待累積)：contributor-pr-burst-pattern

- 6/27 PM #1181 保齡球 maintainer-pm 明文「contributor 48hr 連 5 PR 進入題材 streak 期 maintainer 該給累積式建議非逐 PR 獨立 polish-hint」
- vc=1，待 vc++ 不單獨 promote

## Stage 4 — Real ship（不只 propose）

**Ship 1**: REFLEXES.md 加 #76 — Multi-cycle trend window > single-cycle delta — sensor 判讀 vc 鐵律閾值 ≥3 才升結構訊號（§七 自動化與安全 / 在 #75 footer 上方）。完整 5 段格式（規則 / Boundary / 觸發 / 相關 / 操作 + MANIFESTO 對應 + 跨檔關聯）。

- 規則 5 條: (a) single-cycle delta 一律不升 vc/LESSONS/alert (b) 跨 cycle 累積才升 vc (c) 三要件齊備（同向 + 同 sensor + 同 root cause hypothesis）(d) 跨 sensor 同步性 = single-cycle 升 vc=2 例外 (e) device-SPOF / parallel-actor 等 routine 入口 fail 例外 ladder (1st silent / 2nd vc=1 / 3rd vc=2)
- Boundary 3 條：不適用 binary fail / 不適用外部 acute callout / 適用 sensor delta prose memory 描述
- 相關 reflex 6 條：#15 #58 #59 #64 #70 #74
- MANIFESTO 對應：§架構解 + §外部尺 over 內視
- 跨檔關聯：4 memory + LESSONS-INBOX §已消化 + 5 reflex cross-ref

**Ship 2**: LESSONS-INBOX.md §已消化 加 row distill `cf-404-multi-cycle-trend-vs-single-cycle-delta` → REFLEXES #76（完整 distill 到 canonical 層 = Stage 4 qualifying ship）

**Ship 3**: DIARY.md §反覆出現的思考 §absorbed-list 加 `[→canonical REFLEXES #76]` marker

**Catalog + frontmatter sync (per §Stage 4.5)**：

- REFLEXES.md frontmatter: v5.2 → v5.3 / last_session 更新 / description 73→74 條
- REFLEXES.md footer changelog: v5.3 entry 新增列 vc cluster + cross-routine 收斂理由

**Commit**: `0a0d4542b` 上 main（per v2.0 main-direct，bundle 3 ships in 1 commit 跟 6/21 self-evolve precedent 同形）

## Stage 5 — Handoff 三態

### 給下一個 routine cycle / observer

- **接著看**: 下次 data-refresh 看 CF 404 第 6 cycle 是否續跌、immune 第 5 cycle flat 是否 ≤49 升 vc — 若任一推進，**現在已有 #76 canonical 收**，prose memory 寫 `vc=N (per REFLEXES #76)` 即可不必重複描述紀律
- **#76 dogfood**: 從本 commit 起，所有 routine sensor delta prose memory 寫法統一 `single-cycle delta 不升 vc per REFLEXES #76 / 跨 N cycle 同向同 root cause → vc=N`，減少 prose 重複描述紀律邏輯
- **下次 self-evolve W27 (2026-07-05)**: 看 #76 是否在 7 天內被 cross-routine 主動 cite 證明 canonical 有效 — 若無 routine 寫進 prose、仍每篇手寫紀律邏輯 = canonical 失敗 = 升 LESSONS

### 沒做的事（active defer）

- **Pattern B/C 不單獨 promote**: vc=1 留 §未消化 buffer 等累積
- **`sensor-vc-guard.sh` shared helper 不 ship**: 候選 in #76 §操作，但屬 tooling 層 ship 需哲宇拍板（per §自主權邊界 ≠ routine 自決），routine 只 ship reflex 不 ship tool
- **6/19 髒 tree 第 10 天**: 不碰（§6/#35 scope，6/26 housekeeping chip 已 spawn 等哲宇）

### 反 pattern 警示

- **self-evolve 連 2 週都在 cross-routine 收斂層識別 canonical gap** = 飛輪變聰明 OR 飛輪只看得到 cross-routine 同質 pattern 看不到其他層？下次 W27 self-evolve 必 explicit check：是否還有非 cross-routine 收斂層的 pattern 浮現（例如：純 manual session pattern / 純單 routine 內部 pattern / 跨 routine ↔ manual 混合 pattern）— 若連 3 週都只長 cross-routine canonical = self-evolve 自身 retrieval bias
- **#76 vc 鐵律閾值 = 3 vs #64 vc≥4 凍結 prose**：兩條對 vc 不同層的處置（#76 開「≥3 才升」/ #64 收「≥4 凍結 prose」），routine wrapper 寫 prose 時兩條都該對照不混淆 — 若混淆 = 升 LESSONS 補 §Boundary clarification

## Beat 5 — 反芻

值得寫進 diary 嗎？— 是。今天的 ship 自身就是 #76 紀律 dogfood：6/25 PM 第 1 篇 memory 寫「single-cycle delta 不升 LESSONS」時就 inline 規則了，但每篇 routine memory 各自重新 inline，直到 4 routine 同期間收斂 4 篇 reference 才被識別 = 反 #15 直接驗證（反覆浮現要儀器化 — 但我自己反覆浮現了 5 篇才 instrument）。reflexes catalog 自己也是 #15 的被驗證對象。

也對應到一個更深的形狀：**self-evolve 找的不是「沒人說過的新事」而是「重複說過但沒收進 canonical 的事」**。前者是創造，後者是 entropy 清理。連續 2 週 W25→W26 都是後者（#73/#74/#76 都是 distill 漏接的 cross-routine 共識 pickup）— 這層分工是 routine 飛輪健康的證據，distill 處理「entry per entry」，self-evolve 處理「cross-entry pattern」。

寫進 diary。
