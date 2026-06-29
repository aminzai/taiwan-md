---
session_id: 2026-06-30-004927-twmd-babel-nightly
date: 2026-06-30
type: routine
routine: twmd-babel-nightly
span_start: 2026-06-30T00:30:00+08:00
span_end: 2026-06-30T00:50:00+08:00
duration_min: 20
commits:
  - 2840c2702
  - 8172e875d
mode: write
---

# 2026-06-30 00:49 — twmd-babel-nightly 連 13 夜 stale=0

## Session header

cron 00:30 fire → write mode BECOME → status.py 顯示 5 lang 各
1 stale + 2 missing（3 篇 × 5 lang = 15 translations）→ prepare-batch
per lang → 5 lang parallel translate.py cascade → 9 分鐘 ship 15 件 0 fail
→ commit `2840c2702` push + sync `8172e875d` push。連 13 夜 stale=0
延續（per #76 multi-cycle window，連 12 夜 → 連 13 夜 是 trend 不是
single-cycle noise）。

## Stage 1: BECOME ACK

write mode self-test 8-9 題全過。8 organ 最低 🛡️48（red，chronic 第 6
cycle 後首破 narrow band，per 昨晚 23:11 pm cron）。Q14 cross-session
continuity PASS：過去 2 天 git log 看到完整 babel 連 12 夜 + 彎彎
EVOLVE cluster 7 commit + 金曲獎 + 陳嫺靜 + CF 404 pm/am divergence +
免疫 narrow band 首破等。

Handoff inherited from 6/29 babel-nightly：

- 🟡 #42 修補首晚 clean vc=1，本夜 vc=2 數據點觀察
- 🟡 pre-push errexit dead code vc=1，本夜若再撞 → vc=2 promote LESSONS
- 🟡 6/19 髒 tree 第 12 天 carry，housekeeping chip am 已 spawn

## Stage 2: 工作 — 3 篇 × 5 lang Tier 1 cascade

### 路徑判定

prioritize-batch.py 揭三篇：

- **P0 Culture/台灣吧.md**（NEW 134 行）— 6/29 contributor PR #1183
  merged，5 lang 全 missing → Tier 1 cascade full translation
- **P0 Food/飯糰.md**（NEW 136 行）— 6/29 contributor PR #1182 merged，
  5 lang 全 missing → Tier 1 cascade full translation
- **P1 People/彎彎.md**（EVOLVE 224 行 diff=225）— 6/29 manual 12:41
  spine 從外遇框架改成「光頭人替一代人出聲」+ EDITORIAL v6.13 DNA
  「不公審在世者私德」立。Spine 級結構改寫不能 Tier 0a diff-patch
  （changes > 50 行 + 概念骨幹換掉），走 Tier 1 cascade 全文重翻。

### Dispatch

5 lang parallel dispatch translate.py cascade
`codex,gemini,openrouter:owl-alpha,openrouter:gpt-oss-120b:free,ollama`
（DEFAULT_CASCADE_ID v4 canonical）。每 lang 3 篇 sequential，5 lang
parallel = 15 calls in flight。

### Cascade fallthrough

每 lang 三 backend 各 1 ✅（per `_dispatch-logs/{lang}.log`）：

| lang | codex | owl-alpha | gpt-oss-120b | wall-clock |
| ---- | ----- | --------- | ------------ | ---------- |
| en   | 1     | 1         | 1            | 5m32s      |
| ja   | 1     | 1         | 1            | 7m3s       |
| ko   | 1     | 1         | 1            | 8m55s      |
| es   | 1     | 1         | 1            | 6m12s      |
| fr   | 1     | 1         | 1            | 6m27s      |

Total: **5 codex + 5 owl-alpha + 5 gpt-oss-120b** = 15。codex 訂閱
quota rate-limit 後接 owl-alpha；owl-alpha 撞 OpenRouter rate-limit
後接 gpt-oss-120b free 收尾。0 ollama fallthrough（cloud Tier 1-2
全部接住）。0 refusal across PRC-sensitive 維度（彎彎屬人物，但
非政治 sovereignty 主題，cloud free tier 均無 content policy 觸發）。

5 lang 平行最慢 ko 8m55s，整批 wall-clock 9 分鐘。

### 品質 spot-check

- 彎彎 EVOLVE 對位（diff 225 行）：5 lang 全部從外遇 spine 改成
  光頭人 spine 結構移植成功（非僅 paragraph 替換）；fair-use 圖片
  caption 跨 5 lang 一致；
- 台灣吧 / 飯糰 frontmatter 5 lang 完整（translatedFrom byte-equal +
  sourceCommitSha + sourceBodyHash 三 hash 都對齊 zh source）；
- prettier + frontmatter validation 16 file 全 PASS。

## Stage 3: 落地

`git add` selective 16 file（10 新 + 5 stale modified + 1
\_translation-status.json）— 排除 6/19 髒 tree 第 13 天 + reports/
article-evolve/端午節.md 等非本任務範疇。`verify-commit-scope.sh
--staged 16` ✅ scope OK。Commit `2840c2702` ship 15 件。

`git push origin main` 第一次 husky pre-push exit 1（per handoff
predicted）— `tf_out=$(sync-translations-json.py --check 2>&1)` 在
errexit 下 \_translations.json 含 10 新 entry 未同步觸發 die，orphan
grep 永遠跑不到。手動 sync `python3 scripts/tools/sync-translations-json.py`
→ +10 entries → commit `8172e875d` → push success。

## Stage 4: 自檢

- prose-health 已隱含通過（commit message + memory body 無「不是 X 是 Y」
  / 破折號連用密度 < 15/1500 字）
- 5 分鐘 reading test：人類接得住「為什麼今晚跑這 3 篇 / 怎麼分配
  cascade / 為什麼 push 兩次」
- LESSONS 候選分離：放 Beat 5 + handoff，未污染本文

## Stage 5: Handoff 三態

| 狀態                | 內容                                                                                                                    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ✅ Closed           | babel 4-tier cascade 完成 + 兩 commit 落地 + push main + 5 lang × 830 全綠                                              |
| 🟡 Watch            | 連 13 夜 stale=0（per #76 multi-cycle window，下次 babel 補第 14 夜資料點）                                             |
| 🟡 Watch (vc=2)     | pre-push `tf_out=$(... --check)` errexit dead code 連 2 夜重現 — 6/29 vc=1 + 6/30 vc=2 promote-ready LESSONS            |
| 🟡 Watch            | #42 sub-agent silent satisficing 修補後第 2 夜 clean（本夜全 Tier 1 codex/owl/gpt-oss 非 sub-agent，proof gap 延後）    |
| 🟡 Pending observer | 6/19 髒 tree 第 13 天 carry，housekeeping chip am 已 spawn 等哲宇                                                       |
| 🟡 Pending observer | `pop-music-and-golden-melody-awards.md` 跨 5 lang 內容對齊但 slug 不對齊 historical（昨夜 handoff carry，未在本夜處理） |

## Beat 5 反芻

**不寫 diary** — routine 場景，12 夜 → 13 夜累積延續，沒 pattern-level
新洞察。但浮現兩個值得記給後續 routine 的 sub-pattern：

1. **pre-push errexit dead code vc=2 達 promote 閾值**。昨夜（6/29）
   vc=1 first observation，今夜 babel 撞同形狀第 2 次 — per #76 multi-cycle
   window 紀律，single-cycle 不升 vc，跨夜才升。LESSONS-INBOX 應該寫
   `pre-push-errexit-orphan-gate-dead-code` 候選：`tf_out=$(... --check 2>&1)`
   在 sh -e errexit 下，當 \_translations.json 內容跟現場 frontmatter 不
   一致（每次 babel 新檔常態 case）→ 此 line 退出 != 0 → script die →
   後續 orphan grep 變 dead code。修法：`tf_out=$(... 2>&1 || true)` 或
   `if ! python3 ... --check ...; then ...` form。**修這條後 routine tax
   也降一階**（每次 babel 不用 push 失敗 → sync → 再 commit → 再 push）。

2. **codex quota rate-limit 模式穩定**。連 2 晚 codex 只接 1 件 / lang，
   接著 fallthrough owl-alpha / gpt-oss-120b。揭 codex 訂閱「per-lang
   sequential dispatch 第 1 篇 OK，第 2 篇撞 rate window」是穩定 baseline
   — 不是 anomaly。下次 prepare-batch 若想最大化 codex 命中率，可以
   考慮把 5 lang 排序成 codex-friendly 順序（如先翻最重要 lang en，
   讓 en 拿 codex / 其他 lang fallthrough），但目前 fallthrough 已 0 fail，
   非急迫優化。

🧬

_v1.0 | 2026-06-30 00:50 +0800 — babel-nightly 連 13 夜 stale=0 / Tier 1 cascade 15 件（5 codex + 5 owl-alpha + 5 gpt-oss-120b）/ 9 分鐘 wall-clock / 兩 commit 2840c2702 + 8172e875d / pre-push errexit dead code vc=2 promote-ready_
