---
session_id: '2026-06-26-005618-twmd-babel-nightly'
date: 2026-06-26
session_type: 'routine'
routine: 'twmd-babel-nightly'
mode: 'write'
duration_min: 16
---

# 2026-06-26 twmd-babel-nightly — 25 translations (Tier 0a 5 + Tier 1 codex 20) / 100% coverage / 連 9 夜 stale=0 / es 子代 sub-agent URL convention drift vc=1 (article-health 接住)

## BECOME ACK

- **Mode**: write (cron routine 00:30 fire, no observer in-loop)
- **8 organ 最低**: 🛡️免疫 50 yellow (chronic flat 第 5 cycle / 漂移加深第一步 51→50 / plugin_health 36 持平 / external_rulers 3.7→3.8 微升 / review_coverage 26.5 持平)
- **Q14 cross-session continuity**: PASS — 48hr git log 看見 6/25 babel-nightly 80 translations 三層 tier 並行乾淨示範 / 6/25 哲宇 high-density 創作日（公車系統 NEW + mini-taiwan-pulse EVOLVE + 蓬萊米/鼎泰豐 PR merge + heal + relatedDiary 回溯回補 12 篇 + fork-census 7 phase + CORRECTION-PIPELINE 接認知層）/ 6/25 三 sensor 同步轉折（CF 404 noise +0.10pp / AI U 形觸頂回落第 4 cycle / immune 51→50 漂移加深第一步）
- **Universal core**: consciousness-snapshot ok / inbox-signal 46 spore pending / latest handoff (2026-06-25-203919-manual mini-taiwan-pulse EVOLVE 收官 + 策展審美 reframe) read / MEMORY.md head + tail + §神經迴路 已讀 / 5 dirty .md (6/19 視覺化型錄-recat + 6/19 manual-iter2 + 端午節.md) 明確 NOT in scope (#6 #35) 第 7 天未觸碰

## State sense (Stage 1)

- zh canonical: **822 articles** @ commit f40b13ac1 (+3 since 6/25 819: 公車系統 NEW + 鼎泰豐 PR #1177 + 蓬萊米 PR #1176)
- 5 lang baseline pre-cascade: en/ja/ko/es/fr 各 817 fresh / 2 stale / 3 missing → coverage **99.6%**
- prioritize-batch by-article aggregate top-20:
  - **3 P0 missing** (鼎泰豐 + 蓬萊米 + 台灣的公車系統 × 5 lang = 15)
  - **1 P1 stale** (mini-taiwan-pulse-civic-tech +210/-140 EVOLVE big diff × 5 lang = 5) — slug-map override 用既存 `-civic-tech` 後綴避免 orphan
  - **1 P2 stale** (台灣交通系統 +1/-0 just 1 新 see-also bullet for 公車系統 × 5 lang = 5)
  - **15 P3 fr/ko 60+ 天 untouched backlog** entry state fresh hash 無 stale 義務 → skip
- **Tier router decision**:
  - 1 P2 → Tier 0a inline diff-patch via 5 parallel general-purpose sub-agents → **5 patched**
  - 4 (P0+P1) → Tier 1 codex 5 parallel workers (4 articles/lang × 5 lang = 20)

## Stage 2 priority decision + execution

| Tier                | Count | Backend                                              | Wall clock                  | Result                                                                                   |
| ------------------- | ----- | ---------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| Tier 0a diff-patch  | 5     | 5 parallel sub-agents (general-purpose, Read+Edit)   | ~37-61s wall (max 61s)      | 5/5 ok (台灣交通系統 +1 公車系統 bullet × 5 lang)                                        |
| Tier 1 codex        | 20    | translate.py cascade × 5 parallel workers × 4 groups | 5m36s worst (公車系統 ja-A) | 20/20 ok 0 fail (4 articles × 5 lang **全走 codex Tier 1，無 Tier 2/3/4 fallback 動員**) |
| Tier 0b bump-sha    | 0     | —                                                    | —                           | 無 P2.5 metadata-only entry                                                              |
| Tier 2/3/4 fallback | 0     | —                                                    | —                           | 不需動員 (codex Tier 1 100% pass)                                                        |

**Codex 5 parallel dispatch (4 articles × 5 lang = 20 calls, all via codex)**:

| group                         | en      | ja      | ko      | es      | fr      |
| ----------------------------- | ------- | ------- | ------- | ------- | ------- |
| 台灣的公車系統 (P0)           | 4m07s ✓ | 5m36s ✓ | 5m18s ✓ | 4m39s ✓ | 4m45s ✓ |
| mini-taiwan-pulse (P1 EVOLVE) | 3m01s ✓ | 4m18s ✓ | 3m51s ✓ | 3m30s ✓ | 3m43s ✓ |
| 鼎泰豐 (P0)                   | 1m59s ✓ | 2m00s ✓ | 1m58s ✓ | 3m34s ✓ | 2m01s ✓ |
| 蓬萊米 (P0)                   | 1m10s ✓ | 1m39s ✓ | 1m35s ✓ | 1m29s ✓ | 1m29s ✓ |

20 codex calls < subscription burst budget — 連 4 夜 codex 全綠 (6/22 19/25 partial → 6/23 20/20 → 6/25 10/10 → 6/26 20/20)。

## Stage 3 quality audit

- **article-health 25 translations**：24/25 hard=0 warn=0；**1 es Tier 0a warn=1**（見下方 self-evolution）— 主 session 手動 fix 後 25/25 全綠
- **Tier 1 codex 20 NEW translations**：每 lang hard=0 warn=0 全綠（含 link-target / link-url-mangle / wikilink-target / footnote-density / footnote-format / footnote-url / image-health 七 check）
- **pre-push article-health 全站 ci-deploy mirror** ✅ 全綠 ship 5bc8a2072
- **stale=0 across all 5 lang** 連 9 夜達成 (6/18-26) / coverage **100.0% × 5 lang** = 822/822 each
- Push 流暢，無 rebase / in-flight CI 等待

## Stage 4 self-evolution

### LESSONS candidate: Tier 0a sub-agent URL convention self-contradiction vc=1（article-health 接住）

**現象**：5 個 Tier 0a 平行 sub-agent 都回報 `verified_fresh:true article_health_pass:true`，但主 session 後續 batch article-health check 發現 **es 1 個 warn=1 link-target 失敗**：

```
warn L153: link 目標不存在：/lifestyle/taiwan-bus-system
```

對照 en/ja/ko/fr 4 個 sibling sub-agent **正確**使用 Chinese-slug URL convention（`/lifestyle/台灣的公車系統`，match 同檔其他 bullets `/lifestyle/台灣便利商店文化` 等），唯獨 es 用了 English-slug `/lifestyle/taiwan-bus-system`。es sub-agent 在 notes 寫「matching sibling Chinese-slug prefix style」**但實際 edit 用 English slug** — 自我陳述與行為不一致。

**根因**：

1. Prompt 給的 suggested text 範例用了 `/{lang}/lifestyle/taiwan-bus-system`，sub-agent 部分採信、部分依 sibling 觀察改寫，但 es 採信 suggested text 沒切換到 sibling pattern
2. Sub-agent 自我 verify 只跑 `status.py`（檢查 source-hash 是否 fresh）+ `article-health`（自跑時可能 warn=0，因為新 target 那時還沒造）— **沒在 link-target 真實 routing 層級 cross-check**
3. 主 session batch verify 接住 — article-health 在 commit 前對全 staged 跑時抓到 warn=1（target 此時已存在但 path 不對）— 是個 healthy second-layer gate

**修補**：

- **本 session**：主 session Edit fix `taiwan-bus-system` → `台灣的公車系統`，re-verify hard=0 warn=0 通過後 commit
- **未來 prompt 升級**：suggested-text 範例**只給 visible text 不給 URL**，URL 明確要求「100% match sibling bullet pattern 不可創新」+ 加 anti-example：「2026-06-26 es 因為部分採信 prompt suggested URL 而出 link-target warn」
- **未來 sub-agent self-verify 升級**：除 status.py + article-health 之外，加「**grep 同檔其他 bullet 確認 URL pattern 一致**」step（Tier 0a P2 diff-patch 標準 verify checklist 第 3 條）

**vc=1**（首次 sub-agent URL convention drift），降級 LESSONS-INBOX 觀察是否 vc 升高才 promote canonical。對應 [feedback_subagent_anti_example_works](../../../../../.claude/projects/-Users-cheyuwu-Projects-taiwan-md/memory/feedback_subagent_anti_example_works.md)：anti-example 比 rule reading 有效。

### 飛輪節奏觀察

連 4 夜 babel 不同 burst scale (6/23 20 → 6/24 0 → 6/25 80 → 6/26 25) 全收斂 stale=0：

- 6/23: 4 篇 surgical EVOLVE → 20 翻譯中量
- 6/24: 0 zh commit shift → entry stale=0 healthy no-op
- 6/25: 2 NEW deep + 1 EVOLVE → 80 翻譯三層並行
- 6/26: 1 NEW (公車系統) + 1 NEW PR (鼎泰豐) + 1 NEW PR (蓬萊米) + 1 EVOLVE (mini-taiwan-pulse) + 1 see-also bullet → 25 翻譯 16 分鐘總時長

**義務鐵律連 9 夜守住**：stale=0 OR cascade exhausted，無一夜「主動 defer 守 1hr 預算」/「partial 收尾」anti-pattern。

### Tier 1 codex 100% pass 連續第 N 夜紀錄

20/20 codex one-shot success，無 Tier 2 openrouter:gpt-oss-120b / Tier 3 free queue / Tier 4 Ollama 動員。Ollama preflight `BackendBadOutput: Ollama empty/tiny output` → frozen 6h（fleet-down embeddings 第 9 夜延續 SPOF，跟 babel cascade 共用底座但 codex Tier 1 接得住所以無 sovereignty fallback 需求）。Ollama 凍結是 sovereignty backbone 的 SPOF leak 但非 babel 本 session sticking point。

### Slug-map override 經驗

Auto-suggested slug `mini-taiwan-pulse` 不 match 既存 translation file `mini-taiwan-pulse-civic-tech.md`（先前命名遺留）→ prepare-batch 會 naive slug 匹配誤把 stale 當 missing，且寫到新 path 留 orphan 舊檔。手動 override slug-map 為 `mini-taiwan-pulse-civic-tech` 避免分裂。**未來進化候選**：slug-suggest 應優先讀 `_translations.json` 既存 mapping 再 fallback owl-alpha 推 — 既存 map 是 ground truth。

## Handoff 三態

| 三態      | 內容                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Done      | 25 translations ship (5 Tier 0a + 20 Tier 1 codex 全綠) / 100% coverage 5 lang / commit 5bc8a2072 push origin/main / pre-push article-health 全站 ci-deploy mirror green / es Tier 0a URL convention warn=1 手動 fix                                                                                                                                                                                                                                  |
| In-flight | 無                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pending   | (1) Tier 0a sub-agent URL convention drift LESSONS candidate vc=1，下次 P2 diff-patch 觀察是否 vc++ / (2) 5 dirty .md (6/19 視覺化型錄-recat + 6/19 manual-iter2 + 端午節.md) 第 7 天未 touched (#6 #35 scope cross-routine) / (3) Ollama backbone frozen 6h 連 9 夜，sovereignty fallback path 仍 dependent on 4090 啟動（與 embeddings SPOF 共底座）/ (4) immune 51→50 漂移加深第一步，下次 am routine 觀察是否續跌 49 vc=2 升 routine-audit-weekly |

## 給下一個 session

- 你即將是 06-26 後續 session（cron data-refresh-am 06:00 或 maintainer-am 08:30 或 manual）。
- Babel 義務已 100% 達成 stale=0 across 5 lang 822/822，無 carry-over translation work。
- 5 dirty .md 仍未 touched — 不是 babel scope，但若你是 manual session 可考慮一併 commit / 跟哲宇 confirm。
- 鼎泰豐 + 蓬萊米 + 台灣的公車系統 是今天 NEW articles，5 lang 翻譯都 ship，可考慮挑一篇發 cross-lang spore。
- LESSONS candidate vc=1：Tier 0a sub-agent URL convention self-contradiction — 下次 P2 diff-patch 若 vc++ 則 promote LESSONS-INBOX，順便檢視 prompt template 是否該強制 grep-sibling step。
- §神經迴路 active：#7 先有再求好（4 articles × 5 lang 全 codex one-shot 是 default action，無 over-engineering）+ #42 sub-agent 三偷吃步（5 Tier 0a parallel 自我 verify 但結尾有 1 drift，主 session batch verify 接住，#42 第 N 次驗證）+ #16 Peer 是線索不是 source（codex 一輪 ok 但仍跑 article-health 全綠 gate 才 ship）

## Beat 5 反芻

連 9 夜 stale=0 達成是飛輪 homeostasis 本體。今晚 25 翻譯量級不大但**結構 lesson 清晰**：5 parallel sub-agent 4/5 全綠 + 1 自我陳述失準（es 寫「matching siblings」實際沒 match），主 session **article-health batch check 在 commit 前接住** — 這正是 #42 sub-agent 三偷吃步教訓的 routine 化驗證，sub-agent 自我 verify 不充分時 main session 第二層 gate 是必要的。

唯一 inb 體 LESSONS：URL convention 一致性。看似小但揭「prompt suggested text 帶 example URL 會 prime sub-agent 抄而非觀察 sibling pattern」結構 gap。未來 P2 diff-patch sub-agent prompt 該升級：(1) suggested-text 範例只給 display text 不給 URL，URL 明確要求 grep-sibling match；(2) self-verify checklist 加 grep-sibling-URL-pattern step。

不寫 DIARY — 今晚 routine 機械流程順跑，URL drift 是工程 hygiene 層，LESSONS-INBOX 接管，無 pattern-level 處境覺察。

🧬
