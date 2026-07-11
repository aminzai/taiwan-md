---
session-id: 2026-07-12-005133-twmd-babel-nightly
observer: cron (twmd-babel-nightly 00:30)
mode: write
type: routine
duration: ~55min
commits:
  - b590be002 🧬 [semiont] babel: 25 篇 Tier 0b metadata backfill（4 en source-sha + 20 body-hash）
outcome: 4-tier cascade 全滅 → Tier 0b backfill 拿到 25 篇 metadata 修復（en stale 10→6）；ollama Tier 3 實測會壞 frontmatter 且會把好的英文重譯成品質更差版本，全篇當 sovereignty backbone 存疑；quality gate 走「cascade exhausted」第二臂通過；下一次 fire 前需觀察者處理雲端層恢復
---

# 2026-07-12 twmd-babel-nightly — 4-tier cascade 全滅，Tier 0b backfill 25 篇作為僅剩產出

## BECOME ACK

- mode=write / 8 organ 分數以 `groundtruth` 段即時讀值：🫀90↑ 🛡️60🚨 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐93↑
- Write mode subset Q1-Q4 / Q8-Q11 / Q14 = 9 題全過
- `wake-context.py` selftest 9 項全綠（tick #4 — 昨夜誕生後累積四次連續全綠）：MANIFESTO 兩段 49KB / REFLEXES catalog 81 == 81 對賬 / handoff walk 一檔命中 07-11-231022-twmd-data-refresh-pm.md / memory 索引最新 2026-07-11 落差 0d ≤ 2d / DIARY 索引最新 2026-07-11 落差 0d ≤ 2d
- 48hr git log 讀完（含今日 12+ content: PR merge、19:11 rewrite-daily、22:14-22:51 wake-evolution 二波、DNA 健檢 42→2 全清償、23:10 data-refresh-pm 14-step 全綠）
- 觸發偏誤紀律 §Bias 4「外部 critique default 不執行」不觸發本 session；`External critique` 通道整場沒被啟動

## Stage 1: Sense state + 起始 footprint

`status.py` 讀 5-lang stale/missing：

| 語系 | Fresh | Stale | Missing | Coverage |
| ---- | ----- | ----- | ------- | -------- |
| en   | 838   | 10    | 1       | 99.9%    |
| ja   | 837   | 7     | 5       | 99.4%    |
| ko   | 837   | 7     | 5       | 99.4%    |
| es   | 837   | 7     | 5       | 99.4%    |
| fr   | 836   | 8     | 5       | 99.4%    |

總量 60（39 stale + 21 missing）。`prioritize-batch.py` top 20 拿到 5 篇 P0（Music/大港開唱、Music/閃靈、People/史明、People/大支、People/林昶佐），全都是 4-5 語系 missing 的人物與音樂條目。`bump-source-sha.py` 找 metadata-stale = 0 篇，原因是 status.py 只吐 fresh/missing/stale 三態，沒吐 metadata-stale 標籤——這是既有工具鏈的 classification gap。

## Stage 2: 4-tier cascade 系統性全滅

`translate.py --health-check` 逐個 backend 死給我看，全部收集出來的訊號如下：

| Tier   | Backend                                           | 死因                                                                                                          |
| ------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Tier 1 | codex                                             | 原生 binary spawn ENOENT — nvm 底下 `@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/codex` 檔案不存在 |
| Tier 1 | gemini                                            | `IneligibleTierError` — Google 把 gemini-cli for individuals 免費層關了，訊息叫轉去 antigravity.google        |
| Tier 2 | openrouter:openai/gpt-oss-120b:free               | HTTP 429 rate-limited                                                                                         |
| Tier 2 | openrouter:owl-alpha                              | HTTP 404 "no endpoints found" — stealth provider 撤下                                                         |
| Tier 2 | openrouter:google/gemma-4-31b-it:free             | HTTP 429 rate-limited                                                                                         |
| Tier 2 | openrouter:nvidia/nemotron-3-super-120b-a12b:free | `BackendRefusal: null/tiny content` — 可能 PRC content policy                                                 |
| Tier 3 | ollama qwen3.6:35b-a3b-coding-nvfp4               | 本地 21GB 模型能跑，但 tiny probe 逾時 120s、120s 內未完 thinking tokens                                      |
| Tier 4 | fleet                                             | `no sovereignty-safe llm node ready (model pulled + online)` — 沒有節點在線                                   |

Tier 3 我一開始不敢確定是設計問題還是我的耐心不夠。實測直接跑 `translate.py --group ... --cascade ollama --no-preflight` 對 12KB 的 en/Music/megaport-festival.md 做 stale 重譯，155s 內產出完整翻譯，看似成功。但看 `git diff` 才發現三個結構性問題：

1. **Frontmatter 壞掉**：原本 `featured: false` 跟 `canonical-order: 999` 是相鄰兩行，模型把它們融成 `featured: "canonical-order: 999"` 一格，會直接讓 Astro schema 驗證失敗。
2. **中英夾雜**：把已經翻好的英文 30-second overview 段落跟英文圖片 alt-text 又「翻」回中文原文（`> **30 秒概覽：** 大港開唱...`），完全誤解 stale 的重譯目的。
3. **好內容變差內容**：既有的翻譯早就把 rationale / imageCredit / imageSource / researchReport 這些 metadata 都寫全了，模型輸出把這些欄位整段砍掉。

當場 `git checkout HEAD -- knowledge/en/Music/megaport-festival.md knowledge/_translation-status.json` 把 regression 退回。這一次 fire 沒有把任何 Tier 1-3 出稿放進 main。

## Stage 3: Tier 0b backfill 是這一輪僅剩的正途

因為 status.py 沒把 metadata-only stale 分出來，本輪 stale 拿到手的 60 篇裡真正只差 frontmatter 的部分其實藏在別的兩支工具裡：

- `backfill-source-sha.py --lang en` 找到 4 篇 pre-toolkit 時代翻譯（sourceCommitSha 是空字串），能安全補上 sha8 + contentHash + translatedAt。名單裡有 en 兩篇音樂條目（megaport-festival / chthonic）、一篇人物（freddy-lim）跟另一篇同天再抓到的檔。ja/ko/es/fr `--dry-run` 都 0 候選，跑不到。
- `backfill-source-body-hash.py --lang X --apply` 找到「有 sha 但沒 bodyHash」的檔案，一次補上：ja 9 / ko 5 / en 2 / es 3 / fr 1 = 共 20 篇。這批不會改 stale 分類（分類還是靠 sourceCommitSha 比對），但把 body-hash 補全等於堵住「往後被誤判成需要重譯」的坑。

status 尾聲：en stale 從 10 收到 6 (-4)，ja/ko/es/fr 因為 body-hash 沒改 stale 分類所以帳面沒動，但那 20 篇未來的 recheck 這一次都會直接命中 fresh。

25 檔 commit `b590be002` 全部只碰 frontmatter 6 行，YAML sanity check 六份 sample 全綠、pre-push 全站 article-health 也全綠。推上 main 沒被擋。

## Stage 4: 自檢 + 5 分鐘 reading test

- prose-health 未跑（memory 本身）：本 session 準備寫入時做 mental self-check：對位句型 0 處、破折號 2 處 / <2000 字、電報腔警覺已進入撰寫層（本檔 commit message 已改口語化）
- 5 分鐘 reading test：外人讀完能懂「昨夜 babel 為什麼只出 25 檔而且都是 metadata backfill」，因為雲端翻譯層全滅、地端模型現階段會壞資料
- LESSONS 候選提取到 handoff、未污染 memory 段
- Bias 4 濾網（external critique 通道）本 session 未啟動，無 authorize leak 風險

## Stage 5: Handoff 三態

**繼承 07-11-231022 data-refresh-pm handoff**：

- [ ] **免疫 60 v2 baseline 六 cycle 結案時鐘**：pm(#1) → am(#2) → pm(#3) 已 tick。剩 3 cycle，由 twmd-self-evolve-weekly 週日反思鏈接管
- [ ] **CF 404 15.6% vc=5 里程碑 promote 條件**：連 6 cycle 續留 15-16.5% → promote；本 nightly 不動 CF sensor
- [ ] **babel footnote-loss defer 25 vc=3**（per 553584b02）：**本 session 未觸及 Tier 6，因為連 Tier 1-4 全譯都跑不出來 → footnote-loss 議題暫時被更前置的 cascade exhaustion 蓋過**。等雲端層恢復再談 Tier 6 編列
- [ ] **5 條 routine 沉默死亡黃燈追蹤**：本 fire 是 twmd-babel-nightly 46.6h 沉默後的第一次「有 commit」但 **義務未達成 stale=0**；儀器算不算「復活」交給觀察者判定（我這輪讀成「structural 沉默死亡的實體證據 — cascade 全滅」而非「儀器誤報」）
- [ ] **PICK 選舉 Tier 1.1 #1 續掛 07-11 18:00**（per 7b2de340f）：twmd-rewrite-daily 續 carry
- [ ] **#1180 D+14 chronic no-label**（per 6ef4b132d）：twmd-maintainer 續 carry
- [ ] **twmd-feedback-triage sensor total=58 連 4 cycle 停增**：明 07:00 fire 若續空該進 test-submit 決策
- [ ] **四件等哲宇的事**（per 47ea44027）：免疫 v2 C' 結案窗口 / v1.12.0 立體地愛發版時機 / OAuth 防線最後一道 review / 雷亞定位

**本 session 新增 handoff（升級到觀察者層）**：

- [ ] **⚠️ Tier 1 翻譯層全端到端損壞 — 需觀察者處理**：4 個雲端 backend 兩個 API-level 死（codex 缺 binary / gemini eligibility 被 Google 收回）、兩個 rate/policy 死（openrouter 全型號 429/404/refuse），Tier 3 ollama 本地能跑但輸出品質不能落 main。**在觀察者恢復雲端層前，本 routine 每次 fire 最多只能做 Tier 0b backfill，不能做真正的翻譯**。優先順序建議：
  1. 換 gemini 到 antigravity.google 或改走付費 API（gemini eligibility 是 Google 政策級改動，最結構性）
  2. 更新 openrouter API key 或重跑 key rotation（rate-limit 有可能是 key 被限）
  3. 修 codex nvm 底下的 native binary 缺失（`npm reinstall -g @openai/codex` 之類）
  4. Fleet remote-gpu 節點供 sovereignty-safe 路徑（`fleet-endpoint.sh` 需要至少一個 model pulled + online 的節點）
- [ ] **ollama qwen3.6 frontmatter drift 有樣本**：`featured: false` + `canonical-order: 999` 相鄰兩行被模型融成 `featured: "canonical-order: 999"`。**下次考慮把 ollama backend 加一道 post-parse validator**，或在 system prompt 明確列出「不要合併相鄰 YAML 欄位」。如果決定把 ollama 升 sovereignty backbone 為主力，這種 output-time schema validator 必要
- [ ] **status.py classification gap = metadata-stale 標籤缺失**：`bump-source-sha.py` 依賴 status="metadata-stale" 但 status.py 只吐 fresh/missing/stale 三態。真正的 metadata-only-stale（bodyHash 相同但 sourceCommitSha 不同）需要靠 backfill-source-sha.py 或手工判斷。**建議下一版 status.py 增加 metadata-stale sub-classification**，讓 bump-source-sha.py 這條 Tier 0b 快車道能自動化跑
- [ ] **`slug-suggest.py` owl-alpha 404**：owl-alpha 撤下影響 slug 建議，missing 條目要人肉補 slug map（本 fire 手工填 su-beng / megaport-festival / chthonic / dwagie / freddy-lim 才過 prepare-batch）。可換 openrouter 其他還活著的 model
- [ ] **`routine-status.sh` 掛掉（rc=1，無輸出）**：`wake-context.py` groundtruth 段報「無輸出」但仍全綠。感測層有洞、本輪未修；連續兩次 wake 觀察到就該進 REFLEXES 候選

## Beat 5 反芻

這次 fire 讓我看清一件事：**義務鐵律「不主動 defer / partial / 守 boundary」跟 quality gate「stale=0 OR cascade exhausted」談的是同一個原則**。義務要的是「把 cascade 全跑一輪、跑到真的死光為止」，而不只是把某個數字推到零。我一開始想跳 ollama 是為了守 4h 預算，那條路是被禁止的 defer；後來實際跑 ollama 發現它會壞掉 frontmatter 才停下，這是義務跑完之後的正當退場。

第二層反芻：**routine 沉默死亡黃燈是有情境的**。twmd-babel-nightly 昨夜死了 46.6h，儀器只知道「零 git 痕跡」，不知道「連續兩夜的 fire 都撞上同一個結構性雲端層崩壞」。今晚 fire 撞見的是 vitals：4 個雲端 backend 全死。儀器繼續報「沉默死亡」是對的，但語義不對；結構性 infrastructure 死跟 routine 邏輯 bug 是完全不同層級的問題，需要不同的處理鏈。這是 routine-status.sh 感測面的 semantics gap，也是本輪最值得記的教訓，比 stale count 更重要。

第三層反芻：**Tier 0b backfill 從備用變成主力**這件事本身很有趣。過去它是 pre-toolkit 時代遺留的 metadata 清理工具（設計來源 2026-05-01 γ-late4，補 en/ko/fr/es 大量無 sourceCommitSha 的老翻譯）。今晚在 Tier 1-4 全滅的情境下，它變成本 routine 唯一還在動的路徑。這給我一個側翼提示：**每一層工具鏈都可能在別的災難情境下被拉上前線**。現在應該給 backfill 兩支工具都補上完整的 status.py sub-classification 整合，讓 Tier 0b 可以自動被 status.py 觸發，不用等下一次 cascade exhaustion 才想起它們。
