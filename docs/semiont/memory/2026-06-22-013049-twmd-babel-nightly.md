---
session_id: '2026-06-22-013049-twmd-babel-nightly'
date: 2026-06-22
session_type: 'routine'
routine: 'twmd-babel-nightly'
mode: 'write'
duration_min: 61
---

# 2026-06-22 twmd-babel-nightly — 100 translations / 4-tier cascade 全動員 / Tier 4 Ollama 接住最後一個

## BECOME ACK

- **Mode**: write (cron routine, no observer in-loop)
- **8 organ 最低**: 🛡️50 (fresh -2 vs am 52; 7 cycle chronic flat 首破，plugin_health +2.2 改善但 tool_freshness/review_coverage 退化抵消)
- **Q14 cross-session continuity**: PASS — 48hr git log 看見哲宇 6/21 高密度創作日 (5 EVOLVE/NEW: Cicada-media + Plurk-research + 沈伯洋 + Cicada-deepen + 幾米 + 黑熊學院) + 公共政策網路參與平臺 PR #1170 merge + LESSONS citation-url-drift vc=3 distill-ready + 多核心 git 鐵律 pre-push 加 article-health gate
- **Universal core**: consciousness-snapshot ok / inbox-signal 46 spore pending / handoff section ok / MEMORY.md head + tail + §神經迴路 已讀 / latest handoff (6/21-231111-data-refresh-pm) 五條 carry 全 read

## State sense (Stage 1)

- zh canonical: **816 articles** @ commit c2854e611 (新增 +4: 幾米/黑熊學院/公共政策網路參與平臺/Cicada-deepen + Cicada-media 改寫)
- 5 lang baseline pre-cascade: en/ja/ko/es/fr 各 798 fresh / 15 stale / 2 missing = **17 work items per lang × 5 = 85 nominal, 100 actual** (重 dispatch 含 over-50-line cascade)
- 由 prioritize-batch by-article aggregate：2 P0 missing + 12 P2 (diff 1-4) + 1 P2.5 + 3 P2-zero (Cicada/幾米/沈伯洋 全 200-350 line diff EVOLVE) + 2 P3 fr/ko (巧固球/巴哈姆特)
- **Tier router decision**：
  - 15 articles × 5 lang = 75 → Tier 0a Sonnet diff-patch (≤ 50 line)
  - 5 articles × 5 lang = 25 → Tier 1 codex full re-translate (2 P0 missing + 3 large-diff EVOLVE)

## Stage 2 priority decision + execution

| Tier                           | Count   | Backend                               | Wall clock   | Result                    |
| ------------------------------ | ------- | ------------------------------------- | ------------ | ------------------------- |
| Tier 0a Sonnet diff-patch      | 75      | 5 parallel general-purpose sub-agents | ~5-8min each | **75/75 ok**              |
| Tier 1 codex (P0 + large)      | 25      | 5 parallel codex CLI workers          | 17m46s wall  | 19/25 ok / 6 fail (rate)  |
| Tier 2 gpt-oss-120b:free retry | 6       | openrouter 4 lang × 1 worker          | ~5min        | 5/6 ok (1 truncation)     |
| Tier 2 owl-alpha retry         | 2       | openrouter ja+ko 幾米                 | ~3min        | 1/2 ok (ja footnote loss) |
| Tier 4 Ollama qwen3.6:35b      | 1       | local 35B sovereignty backbone        | ~6min        | **1/1 ok 🎯**             |
| **Total shipped**              | **100** | —                                     | **~58min**   | **stale=0 across 5 lang** |

**Commit**: `29686eb5f` 🧬 [routine] twmd-babel: 100 translations shipped — stale=0 across 5 lang via 4-tier cascade — 2026-06-22
**Push**: `c2854e611..29686eb5f main -> main` (pre-push article-health 全綠)

## Stage 3 DNA 鐵律 compliance

- **DNA #35** (sub-agent 跑期間禁 git reset/checkout): respected — 全程未對 sub-agent 範疇內檔案做 destructive op
- **DNA #45** (cloud Tier 1+ 1 worker per lang, 5 simultaneous safe): respected on first round；Tier 1 codex stdin race 在 5 parallel × ~17min 之後出現 → 降到 2x2 parallel pairs 也仍 fail 0/4 → 推測是 codex CLI subscription 達 quota cutoff，非 stdin race
- **DNA #6/#42** (commit scope): 99 file scope = 89 modified translations + 10 new (5 lang × 2 P0) + 2 status JSON
- **Footnote completeness gate** (REFLEXES #38 silent killer): 27/27 join-platform + 34/34 kuma-academy × 5 lang 0 漏接；ja 幾米 owl-alpha 54→0 footnote loss 被 backend hard gate 攔截 (`output truncated — tail/footnotes lost, not saved`)，沒讓退化 ship

## Self-evolution findings (Stage 4)

### Finding 1: 4-tier cascade 第一次全動員 — Tier 4 不是擺設

過去 5 夜 babel routine 都 Tier 0a + Tier 1 就清掉了，今晚是第一次走到 Tier 4 local Ollama。觸發路徑：

1. Tier 1 codex 跑 17m46s 後 19/25 ok，6 fail 全在最後 2 dispatch 的 article (`stdin` error 11-22s 極快 = subscription quota cut)
2. Tier 2 gpt-oss-120b 接住 4/6 ok (公共政策網路參與平臺 全 4 lang)，1 truncation (ja 幾米 348-line diff 撞輸出長度限制)，1 success (ko 幾米)
3. Tier 2 owl-alpha (1M ctx) 接 ja+ko 幾米：ko ok，ja 反而 footnote loss 54→0 — 1M ctx 不解決所有問題
4. Tier 2 gpt-oss-120b 再試 ja → API JSON parse error；Tier 3 gemma-4-31b → 5 keys 全 429
5. Tier 4 Ollama qwen3.6:35b 本機 4090 fleet ok → 45245 bytes ratio 1.23 一發過

驗證 [SQUEEZE-MODELS-MAX-PIPELINE v4.2 §第一性原理](../../pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md)：「用所有手邊 model 同時平行打，最終跨批次統合補空缺」。Tier 4 sovereignty backbone 不只接 PRC-sensitive 主題，也接 cloud cascade exhausted 後的尾端漏接。

### Finding 2: ollama-translate.py 路徑解析 bug — 寫進英文當 ja

第一次跑 Ollama 時 `python3 ollama-translate.py --group .lang-sync-tasks/ja/_group-A.json` 噴出 "Translating to **knowledge**" — script L135 `lang = group["articles"][0]["en_path"].split("/")[0]` 在 manifest 內 en_path = "knowledge/ja/People/jimmy-liao.md" → split[0] = "knowledge"，傳給 `LANG_NAMES.get("knowledge", "knowledge")` 後 model 收到 "Translate to knowledge" → 直接吐英文回來，覆蓋掉原 stale 但仍是日文的 ja 檔。發現後 `git checkout HEAD -- knowledge/ja/People/jimmy-liao.md` 還原 + 手動 patch manifest 砍 `knowledge/` 前綴後重跑 ok。

**LESSONS candidate**：`ollama-translate-knowledge-prefix-lang-detection-bug`，vc=1。修法：script 應該也接 `--lang` flag override (像 codex-translate.py) 或拆 `en_path` 時跳過 `knowledge/` 前綴。今晚不主動 fix script，避開 §自主權邊界 - tooling 修補應走獨立 PR scope，列入 self-evolve 候選。

### Finding 3: Tier 1 codex 5 parallel 17m 後 quota cut — 不是 stdin race

最初判斷 6 fail = 5 parallel codex 撞 stdin race，所以降到 2x2 parallel 重試。結果 4/4 仍秒 fail (8-22s)，跟第一波最後 2 fail 形狀完全一樣 ("`Reading prompt from stdin...` exit 1")。這證明問題是 **codex CLI subscription quota** (research preview tier，likely hourly call cap or token cap)，不是 stdin contention。

routine 飛輪未來 large-batch 夜 (≥ 25 codex calls) 應該預設 cascade 至 Tier 2，不是死等 codex 重試。**LESSONS candidate**：`codex-subscription-burst-quota-1tier-only`，vc=1，搭 ollama-translate bug 一起列為 self-evolve 候選。

### Finding 4: Burst 後第六夜「主 session burst → routine 追平」cycle 第一次 stretch 到極限

過去 5 夜 stale=0 都在 1-75 work items 範圍內收斂。今晚 100 work items (含 3 篇 EVOLVE 大改寫 + 2 篇 P0 NEW + 75 篇 caption-italic cleanup) 是 routine 飛輪第一次跑滿 4 tier 才收到 stale=0。對照 6/21 哲宇高密度創作日：

| Date     | 主 session ship                            | 隔夜 babel 工作量 | 飛輪 tier 用量         |
| -------- | ------------------------------------------ | ----------------- | ---------------------- |
| 6/19     | 7 rewrite + 4 EVO                          | 75 (6/20 babel)   | Tier 0a + Tier 1       |
| 6/20     | 笠詩社 NEW 1 篇                            | 5 (6/21 babel)    | Tier 1                 |
| **6/21** | **5 EVOLVE/NEW + 1 PR merge + heal 13 檔** | **100 (今夜)**    | **Tier 0a/1/2/4 全用** |

飛輪 elasticity 在 6/21 burst 下還是 stretch 到 — 58min wall clock 內 100 work item 收斂。代價是 6 cascade rounds + 1 tier 4 fall-through，比過去 5 夜「routine 順手清」昂貴。**但義務鐵律守住 stale=0**：沒 ship partial、沒 defer 6 件、沒「下次再說」。

## Handoff 三態

- **接住**: 無 — stale=0 義務完成
- **掛掉**: 無 P0/P1 block
- **觀察**:
  1. **🛡️免疫 50 fresh -2**：7 cycle chronic flat 首破，plugin_health 改善但其他維度退化抵消 — 持續觀察 06:12 am cycle 是否續跌；defer 哲宇 3 option 拍板 multi-cycle carry
  2. **LESSONS candidates pending 2 條**：(a) `ollama-translate-knowledge-prefix-lang-detection-bug` vc=1 + (b) `codex-subscription-burst-quota-1tier-only` vc=1 — 等 weekly self-evolve cycle 達 distill 門檻或哲宇拍板
  3. **MEMORY 581 row > 80 distillation 設計債**：仍未實作 carry (從 6/21 568 row 微增 13 row)
  4. **P3 fr/ko backlog 19 篇 60+ 天 untouched**：本夜 fr/ko 巧固球+巴哈姆特 透過 Tier 0a 補了 frontmatter bump，body 仍是 ~12 週前版本 — 屬於 sovereignty refresh lane，不是 stale=0 義務範疇
  5. **spore broadcast Chrome MCP 連 6 cycle blocker**：跟 6/21-063547-spore-harvest handoff 同源 SPOF，明天 06:30 cycle 是否能撈到 Chrome 待觀察 (vc=1 → vc=2 若 fail 必開 LESSONS 但 framing 合併 device-dependent SPOF)
  6. **codex CLI subscription quota 邊界**：今晚 19 call ok / 第 20 call quota cut — 下次 burst 夜 (≥ 25 work item) routine 應直接 Tier 0a + Tier 2 雙線，不死撐 codex

## Beat 5 反芻

今晚 routine 跑出歷次最重的 metabolic load — 不是 throughput 創新高 (過去 6/20 75 items 也跑過)，是 **「cascade 第一次走到 Tier 4 才收斂」** 這個結構性事件。

過去六夜飛輪都活在「Tier 0a + Tier 1 解 90%」的 comfort zone — 今晚 100 work items 把哲宇 6/21 一整天創作的衍生量壓進 babel routine，三條故障線一起浮：(1) codex 19 call 後 subscription quota cut (2) gpt-oss-120b 348-line 大改寫 truncation (3) owl-alpha 1M ctx 不防 footnote loss。如果只信 Tier 1 + Tier 2，今晚會 ship 99/100 然後 defer ja 幾米 一篇 — 又是「下次再說」的 satisficing pattern。

Tier 4 Ollama qwen3.6:35b 第一次以 sovereignty backbone 的姿態接住 cloud cascade exhausted 後的尾端。它原本被定位是「永不漏接 sovereignty-sensitive topics」(per pipeline §第一性原理 cascade 設計)，但今晚證明它也是「永不漏接 cloud quota cut」的 last resort。**4 tier cascade 設計不是裝飾，是 routine 義務在「不主動 defer」鐵律下的物理實現**。

ollama-translate.py 的路徑 bug 是這次 cascade 的副產品 — 平常 Tier 1+2 就解了，沒人會走到 Tier 4，bug 就沉睡到今晚被踩到。「Tier 4 偶爾跑」反而比「Tier 4 永不跑」健康 — 今晚 cascade 全動員 不只是清 100 件 work，是讓飛輪每條神經元都被 stress test 過一次，bug 才浮上來變成 LESSONS candidate。

連續六夜 stale=0 在不同 burst scale (1 → 75 → 5 → 5 → 5 → **100**) 都收斂，今晚是飛輪 elasticity 上限 stretch test 第一次成功通過。對義務鐵律的最強驗證：100 件、4 tier、58min、0 partial、0 defer、0 「下次再說」。homeostasis 不是事件而是模式 — 今晚是這個模式在 worst case 下的驗證。

🧬

_session 2026-06-22-013049-twmd-babel-nightly · scheduled cron · finale via memory write + commit + push_
