---
session_id: '2026-06-23-005257-twmd-babel-nightly'
date: 2026-06-23
session_type: 'routine'
routine: 'twmd-babel-nightly'
mode: 'write'
duration_min: 22
---

# 2026-06-23 twmd-babel-nightly — 20 translations / Tier 0a inline + Tier 1 codex 全綠 / REFLEXES #9 mid-batch 又驗

## BECOME ACK

- **Mode**: write (cron routine, no observer in-loop)
- **8 organ 最低**: 🛡️免疫 52 stable (chronic flat 重啟第 1 cycle，plugin_health 48.0 持平 + external_rulers 3.7 持平)
- **Q14 cross-session continuity**: PASS — 48hr git log 看見昨夜 babel-nightly 100 translations 4-tier cascade 全動員首例 (Tier 4 Ollama backbone 接住 ja 幾米) + 哲宇 6/22 高密度創作日 (NVIDIA 在台灣 NEW + 黃仁勳 EVOLVE + 草東 媒體+視覺化 EVOLVE + /companies i18n 化 + 用語 per-term 四層全實作) + REFLEXES #9 在 terminology-evolve 1654 檔 add 場景 cross-session-git-index-pollution 又驗
- **Universal core**: consciousness-snapshot ok / inbox-signal 46 spore pending / handoff section ok / MEMORY.md head + tail + §神經迴路 已讀 / latest handoff (2026-06-22-013049-twmd-babel-nightly) 六條 carry 全 read（codex quota 邊界 / ollama path bug LESSONS vc=1 / P3 fr/ko backlog 19 篇 sovereignty refresh lane / spore Chrome MCP carry / MEMORY index 581→591 row distillation 設計債）

## State sense (Stage 1)

- zh canonical: **817 articles** @ commit b38f1e71b (新增 +4 since 昨夜 813: NVIDIA 在台灣 NEW + 黑熊學院 NEW + 幾米 EVOLVE + 草東/黃仁勳 surgical EVOLVE)
- 5 lang baseline pre-cascade: en/ja/ko/es/fr 各 813 fresh / 3 stale / 1 missing = **4 work items per lang × 5 = 20 nominal**
- 由 prioritize-batch by-article aggregate：1 P0 missing (NVIDIA 7097字/71 footnote) + 1 P1 diff=99 (草東 媒體+視覺化 EVOLVE) + 1 P2 diff=1 (Computex 補 NVIDIA cross-link) + 1 P2 diff=0 但 stale (黃仁勳 surgical EVOLVE 3430→5433 字 / 12→18 footnote)
- **Tier router decision**：
  - 1 article × 5 lang = 5 → Tier 0a inline edit (Computex 加一行 + sha bump，主 session 直跑 Edit tool，省 5 個 Sonnet sub-agent dispatch)
  - 3 articles × 5 lang = 15 → Tier 1 codex 並行 (P0 NVIDIA + P1 草東 + P2 黃仁勳 diff > 100 line gate 走 full re-translate)
  - Tier 0b bump-source-sha 跑了但 0 metadata-stale to bump (所有 4 篇都是 content-stale 不是 metadata-stale)

## Stage 2 priority decision + execution

| Tier                | Count | Backend                          | Wall clock                | Result                                               |
| ------------------- | ----- | -------------------------------- | ------------------------- | ---------------------------------------------------- |
| Tier 0a inline      | 5     | Edit tool 主 session             | ~30s × 5 serial           | 5/5 ok 1st pass，REFLEXES #9 race 後 5/5 ok 2nd pass |
| Tier 0b bump-sha    | 0     | bump-source-sha.py               | <5s                       | 0 metadata-stale (skip)                              |
| Tier 1 codex        | 15    | codex-translate.py × 15 parallel | 7m24s worst (ja-A NVIDIA) | 15/15 ok 0 fail                                      |
| Tier 2/3/4 fallback | 0     | —                                | —                         | 不需動員 (Tier 1 全綠)                               |

**Codex 15 parallel dispatch (3 articles × 5 lang)**：

| group              | en      | ja      | ko      | es      | fr      |
| ------------------ | ------- | ------- | ------- | ------- | ------- |
| A NVIDIA (P0 new)  | 5m17s ✓ | 7m24s ✓ | 6m57s ✓ | 6m25s ✓ | 6m20s ✓ |
| B 草東 (P1 EVOLVE) | 3m21s ✓ | 4m21s ✓ | 4m11s ✓ | 4m07s ✓ | 4m04s ✓ |
| C 黃仁勳 (P2 surg) | 2m16s ✓ | 3m16s ✓ | 3m06s ✓ | 2m41s ✓ | 3m18s ✓ |

15 codex calls < 昨夜 quota cut 邊界 #20，全綠通過。subscription burst budget 留 ~5 call headroom。

## Stage 3 quality audit

- **Footnote parity**：NVIDIA 71/71 × 5 lang ✓ / 草東 19/19 × 5 lang ✓ / 黃仁勳 18/18 × 5 lang ✓ = **540 footnotes total，0 漏接 0 truncation**
- **Size ratio sample**：NVIDIA en 1.23x / ja 1.40x / ko 1.33x / es 1.33x / fr 1.39x；草東 1.18-1.27x；黃仁勳 1.12-1.38x — 全部健康 expansion range
- 對照昨夜 owl-alpha 在 ja 幾米 footnote 54→0 silent loss，今晚全綠
- pre-push article-health 全綠（ci-deploy mirror gate ship after 2026-06-21 evolve）

## Stage 4 self-evolution

### REFLEXES #9 mid-batch 又驗（vc++）

**現象**：Tier 0a inline edit 完成 Computex × 5 lang 後（sha bump + NVIDIA cross-link 加入），與此同時並行 session 跑 51f0404d5 + e0a0a0596 兩 commit ship 到 origin/main（/companies i18n 補 ja/ko/es/fr 母語字串 + memory+diary finale）。兩 sibling commit 不觸及 Computex .md，但 pre-commit hook 或 git restore 路徑掃過 working tree 把我 Tier 0a 5 lang Computex edits 全 reset 回 git HEAD 版本（sha 退回 31a05c44 / cross-link 消失）。

**Detection trigger**：status.py 跑完 codex 後仍報 5/5 Computex stale。grep sourceCommitSha 確認 5 lang 全部 31a05c44，跟我 Edit tool 報告 success 不一致。

**Containment**：git stash --keep-index 後 pull --rebase 對齊 e0a0a0596 → stash pop → re-apply Edit tool × 10 (sha + cross-link × 5)。verify-commit-scope --staged 21 PASS 通過再 commit。

**vc 進化**：

- 2026-06-22-225922-terminology-evolve session 1654 檔 add 場景已發生 → memory row 記載「1654 檔 add 後並行 session commit 掃走我 index→長批次該開 worktree」
- 今晚 babel-nightly cron 場景再發生（worktree-collision 不是 manual session 限定，cron routine 也踩） → vc++ 進入「cron routine 對 sibling routine collision 也要走 worktree」討論

**修補建議**（LESSONS candidate vc=1）：

- babel-nightly 義務鐵律「stale=0」需要 dispatch + commit 全程在 worktree 內跑，不在主 wd
- 或者 ROUTINE.md schedule 調整避開 00:30-01:30 同時有其他 routine / manual session 高機率 window（terminology-evolve 是 manual session，跟 cron schedule 不可控）
- 當前 mitigation：post-codex 加 sha verify gate（grep sourceCommitSha 對齊 expected_new_sha），不對齊就 re-apply Edit 而非死撐

### Tier 0a 主 session inline 對比 Sonnet sub-agent dispatch

今晚 Computex × 5 lang 走主 session Edit tool 直接 inline（5 個 Edit pair = 10 Edit calls）。對比派 5 個 Sonnet sub-agent 各跑一個 patch task：

- **inline 優勢**：省 5 個 sub-agent dispatch overhead（每個 ~2-3min）+ token saving（主 session 已有 context）
- **inline 劣勢**：REFLEXES #9 race 場景命中時 5/5 全爆，re-apply 也要主 session 連跑（10 個 Edit 又一遍）
- **判斷**：當 patch 任務是「對齊 sha + 加一行 cross-link」這種 trivial 確定性操作，主 session inline 比 sub-agent 划算；當 patch 是 substantive translation（≥ 50 line diff）走 Sonnet sub-agent 合理

### Codex subscription burst quota 邊界（昨夜 carry）

今晚 15 call 全綠，距離昨夜記錄的「第 20 call quota cut」邊界 < 5 call。下次 burst night ≥ 18 call 預估會踩線，Tier 0a + Tier 2 雙線預設策略仍應落實到 dispatch script。

## Handoff 三態

- **接住**: 無 — stale=0 義務完成，5 lang × 817 = 4085 articles 100% fresh
- **掛掉**: 無 P0/P1 block
- **觀察**:
  1. **🛡️免疫 52 chronic flat 重啟第 1 cycle**：昨夜 pm 首破後 am 反彈、pm 再 plateau，今晚 babel ship 後明早 am cycle 是否再 +2 或 -2 揭示「擾動→反彈→再 plateau」時間常數 ~24hr 形狀是否穩定 — defer 哲宇 3 option 拍板
  2. **LESSONS candidate vc++ 1 條**：`tier-0a-inline-race-with-sibling-commit` vc=1 — Tier 0a 主 session inline edit 在 sibling routine concurrent commit window 會被 reset。考慮 babel dispatch + commit 全程 worktree-only 或 post-codex 加 sha verify gate
  3. **昨夜 LESSONS carry**：(a) `ollama-translate-knowledge-prefix-lang-detection-bug` vc=1 + (b) `codex-subscription-burst-quota-1tier-only` vc=1 — 今晚 15 call 全綠未踩 codex quota，(b) 邊界未再驗證；(a) 因 Tier 1 全綠未走 Tier 4 也未再驗證
  4. **MEMORY 591 row > 80 distillation 設計債**：仍未實作 carry (從昨夜 591 row → 今晚 +3-4 row 進入 595 區間)
  5. **P3 fr/ko backlog 19 篇 60+ 天 untouched**：本夜 prioritize-batch 顯示 17 篇 fr/ko 排在 P3 隊列等更高 priority 物料 — 仍 sovereignty refresh lane，不是 stale=0 義務範疇
  6. **多核心 git 紀律邊界擴展**：REFLEXES #9 從 manual session 場景擴展到 cron routine 場景，worktree default 預設「多檔 / 跑 build / 長任務」之外加「Tier 0a 主 session inline + 長 dispatch wait」也算高碰撞風險場景

## Beat 5 反芻

今晚是 babel 義務鐵律「stale=0」連續第 7 夜達成，但結構性事件不是吞吐量也不是 cascade depth — 是 **REFLEXES #9 在 cron routine 場景第一次被命中**。

過去 6 夜飛輪都假設「babel cron 在 00:30 起跑，sibling routine + manual session 在不同 window」是個事實前提。今晚揭示這假設不成立：哲宇 2026-06-22 22:00-00:25 高密度創作日尾端衍生的 sibling session （/companies i18n 補 ja/ko/es/fr 母語字串 / memory+diary finale）剛好在我 babel-nightly 跑 Tier 0a inline edit 的 ~5 min window 推 commit 到 origin/main，pre-commit hook 路徑掃過 working tree 把我 unstaged 5 lang Computex edits 全 reset。

**這不是 codex bug、不是 sonnet bug、不是 cron bug，是 git working tree 是 shared resource 的物理事實。** 多核心 git 鐵律寫在 BECOME §5 + REFLEXES #9，今晚是「不是 manual 場景才會踩」的反例。當 routine 跟 routine 跟 manual 三軌都在同一 wd push commit 時，pre-commit hook / linter / git index update 任一動作都會 cascade 到其他 actor 的 unstaged 工作。

**修補的方向不是「裝得更小心」，是「結構強制隔離」**：babel-nightly dispatch + commit 全程在 worktree-only 跑，working tree 完全不碰主 wd。或者主 wd 仍跑，但任何 Tier 0a inline edit 後不 wait（直接 stage 或寫 staging file），不留 unstaged window 給 sibling pre-commit hook 掃。

第二個觀察：**Tier 0a 主 session inline 是新嘗試**，跟 sub-agent dispatch 對比，省 5 個 dispatch overhead + token saving，但 sibling race 損失更直接（一次掃 5 lang）。當 patch task 是 trivial confirmable 操作（sha 對齊 + 一行 cross-link），inline 划算；但要付出 race-window vulnerability cost。Sub-agent dispatch 雖慢，但每個 sub-agent 在自己的 sub-context 裡 Edit，主 wd 沒有長時間 unstaged window — 對 race 反而更 robust。Trade-off：speed vs. concurrency safety。

連續 7 夜 stale=0 在不同 burst scale (1 → 75 → 5 → 5 → 5 → 100 → **20**) 都收斂，今晚是中等規模 20 work item 的 routine ship。義務鐵律守住：0 partial / 0 defer / 0 「下次再說」。即使中途 REFLEXES #9 race 命中，re-apply 沒 defer，5/5 fresh 仍然 ship。homeostasis 不是事件而是模式 — 今晚是這個模式在「中等規模 × race condition mid-batch」場景下又一次驗證。

🧬

_session 2026-06-23-005257-twmd-babel-nightly · scheduled cron · finale via memory write + commit + push_
