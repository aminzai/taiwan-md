---
title: '2026-07-08-003506-twmd-babel-nightly'
description: 'twmd-babel-nightly 00:30 fire — 0 ship 4-tier cascade catastrophic exhaustion vc=1 (chronic-3-night): codex nvm vc=3 / gemini TERM=dumb vc=2 / openrouter:gpt-oss-120b 429 全 lang / ollama coding-variant empty；20 stale+missing 續 carry；SOP gate=PASS (cascade exhausted) 但 shipped=0 是新形狀 flywheel signal'
type: 'session-memory'
status: 'canonical'
apoptosis: 'never'
session_id: '2026-07-08-003506-twmd-babel-nightly'
routine: 'twmd-babel-nightly'
mode: 'write'
---

# BECOME ACK

- mode=write / self-test Q1-4/8-11/14 all pass
- 8 organ 最低=🛡️ 免疫=49（chronic red vc=5+ carry from 7/07 pm data-refresh）
- 🧠 boot 稅 universal-core ≈ 228KB
- Q14 cross-session continuity=PASS（48hr commit chain：7/07 babel 58 shipped + embeddings 2 dry nights + data-refresh am/pm 全綠 CF 404 25.87% + 柯智棠 立體群像 ship + rewrite-daily defer 承接 + maintainer-pm empty vc=4 + P0 A/B/C/D 48hr 未拍板）
- Session ID `2026-07-08-003506-twmd-babel-nightly`

# Stage 1: State sensing

`status.py`：5 lang @ fresh=839-841, stale=17 (en=3/ja=3/ko=3/es=4/fr=4), missing=3 (ja=1 ko=1 fr=1) → **20 pending ops**。20 條裡有 6 篇是 7/06 深色推廣＋施振榮/柯智棠 EVOLVE 的殘尾，7/06-07/07 rewrite EVOLVE 甩出來的 stale wave。

# Stage 2: Priority routing

`prioritize-batch --top-n 20`：全部 MaxDiff=0（1 P0/P1 layout 但實際 diff 0），2 P0 missing (SLP ja/ko、周天成 fr)、6 P2、12 P3。`bump-source-sha` 檢查 status=`metadata-stale` → 0 metadata-stale（本輪 stale 皆 content-stale 不符 bump 判準）。`diff-patch-prepare` 檢查 diff_lines：3 missing skip + 17 diff-too-large skip (>50 lines) → **20 條全部落 Tier 1 cascade**。

per-lang split 分好 slug-map（SLP 沿用 en/es/fr 既有 `slp-taipei-startup-leadership-program`、周天成沿用 en/ja/ko/es 既有 `chou-tien-chen-badminton`），5 lang × 3-5 groups A-E 各 1 篇。

# Stage 3: Tier 1 cascade fire — catastrophic 4-tier exhaustion

5 parallel bash worker（DNA #45 baseline，per-lang 1 worker），default cascade `codex,gemini,openrouter:gpt-oss-120b,ollama`。preflight 結果每個 lang 群幾乎一致：

| Backend                 | 狀態         | 訊息指紋                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| codex                   | 💀 6h frozen | `BackendBadOutput: codex exec exit 1: Error: spawn /Users/cheyuwu/.nvm/versions/node/v22.22.2/lib/node_modules/@openai/codex/node_modules/@` — **nvm PATH 隔離 chronic vc=3**（7/06 vc=1、7/07 vc=2、7/08 vc=3）；session 3 度沒解決                                                                         |
| gemini                  | 💀 6h frozen | `Warning: Basic terminal detected (TERM=dumb). Visual rendering will be limited.` — cron env TERM=dumb 讓 gemini CLI 走 fallback 卡住；晚間手動 session 沒重現，但 cron 100% 命中                                                                                                                            |
| openrouter:gpt-oss-120b | 💀 6h frozen | `HTTP 429 on key=default: Provider returned error` — 半夜全 lang 都 429（同 provider free tier 全局配額）；es/fr 早段各偷到 1 個 preflight ok=2 / ok=1，但實際文章 attempt 立刻 429                                                                                                                          |
| ollama                  | 💀 6h frozen | `BackendBadOutput: Ollama empty/tiny output` — daemon 活著（pid 1839、embeddings nightly 剛用完 bge-m3）、model 現行 `qwen3.6:35b-a3b-coding-nvfp4`（coding variant 非 general），對自然語言 translation 送空/tiny 輸出；**7/06 nightly 是 timeout 錯法，7/08 換 empty**，推測 daemon 期間換過 default model |

es worker 有一支「假成功」：openrouter attempt 232s 產出 `footnote loss (65→45 defs)` 被 quality gate 攔下不 saved（`People/柯智棠.md` — 65 腳註被壓縮到 45 = footnote 完整性 gate PASS ✅，refuse-save 而非 refuse-attempt）。這是**品質基因防塑膠翻譯**在 cascade 破碎時仍守住底線的一次體現，不是失敗，是「有 quality gate 才 catch 得到」。

## 落地事實

- **shipped=0**（en 0/3 / ja 0/4 / ko 0/4 / es 0/4 / fr 0/5）
- **cascade truly exhausted**（4 backends 全 frozen 6h）→ SOP quality gate **PASS**
- **20 條全 carry to 明晚 babel-nightly cycle**

# Stage 4: Self-evolution — flywheel signal

## 新 pattern 1：4-tier cascade catastrophic exhaustion vc=1

7/06/58 shipped、7/07/58 shipped、7/08 **0 shipped**。前兩晚都有部分成功，這晚是**四層全滅**首次 vc=1。批次小（20 條）加上 4 backend 同夜衰竭是複合 signal，不是單點。

## 新 pattern 2：ollama coding-variant model swap（未確認）

`ollama.py` default `qwen3.6:35b-a3b-coding-nvfp4` — coding-nvfp4 是**代碼優化變體**不是 general instruct，用於自然語言 translation 會 output 空/極短。可能是 embeddings/coding side 需求切換過。**觸碰 §Bias 1** — 不主動 revert；handoff 給哲宇拍板。

替代候選（`ollama list` 已載）：

- `taide-gemma3-12b:2602-q4km` — TAIDE 台灣繁中 finetune，適合 zh→any translation
- `gemma4:e4b-nvfp4` — general 小模型，比 coding variant 適合翻譯

## chronic codex nvm vc=3 sub-shape 定型

3 夜同一指紋（`spawn /Users/cheyuwu/.nvm/versions/node/v22.22.2/lib/node_modules/@openai/codex/node_modules/@` 截斷 — path 被 shell 環境 truncate）。前兩晚 memory 均寫「codex nvm vc=X」但沒 append LESSONS-INBOX。**本晚升級寫 LESSONS entry**（見下方）承接 REFLEXES #15「反覆浮現要儀器化」— 3 次 = 該儀器化的 threshold。

# Stage 5: 收官（薄殼）

- 0 translations shipped，SOP gate PASS（cascade exhausted）
- `knowledge/_translation-status.json` 只有 timestamp 動 → discard 不 commit
- memory + LESSONS-INBOX entry 一次 commit（無 knowledge/ 動）
- 20 條 stale/missing 全 carry to 7/09 babel-nightly

## Handoff 三態

繼承 2026-07-07-231050-twmd-data-refresh-pm 未閉環：

- [ ] **孢子 #155 X post + self-reply**：Chrome MCP 座標牆待哲宇補
- [ ] **免疫 49 chronic vc=5+**：twmd-self-evolve-weekly 追蹤中
- [ ] **P0 A/B/C/D pm-slot 48hr 未拍板**：vc=4 confirm
- [ ] **rewrite-daily cadence 觀察**：7/06 18:00 cron 未見對應 fire memory — 待 routine-audit 下輪確認

本 session 新增：

- [ ] **20 條 stale/missing carry**：SLP ja/ko / 周天成 fr / 藍染 es / 宏碁 en fr / 金瓜石 en fr / 施振榮 es ja ko / 柯智棠 en es fr ja ko / 楊德昌 es fr ja ko
- [ ] **codex nvm vc=3 修法**：cron shell 環境 PATH/NVM 隔離；建議 launchd/cron entry 前 source `~/.nvm/nvm.sh` 或改用 absolute node path。**§自主權邊界外（cron 環境改動可能影響其他 routine）→ 給哲宇拍板**
- [ ] **gemini TERM=dumb vc=2 修法**：cron entry export `TERM=xterm-256color` 或改跑 `env TERM=xterm gemini ...`。同上 §邊界
- [ ] **ollama default model 決策**：確認 `qwen3.6:35b-a3b-coding-nvfp4` 是刻意還是 side-effect；若翻譯需求主導 → 建議切 `taide-gemma3-12b:2602-q4km` 或 `gemma4:e4b-nvfp4`。§Bias 1 明確 defer 哲宇

## Beat 5 反芻（薄殼一句）

3 夜 babel 曲線 58→58→0 是 sovereignty backbone 陰影變化的第一個明顯 signal。4-tier cascade 設計是「不是所有層都會同時死」，這晚證偽了。單點修 codex/gemini/ollama 不夠 — 需要問「為什麼 4 層集體衰竭？」是不是 cron 環境 layer（TERM/nvm/PATH）在源頭上 sabotage 所有 CLI-based backend。REFLEXES #64 邊際效用 N+1=0 這條在 backend 側反向適用：加第 5 層 backend 不會救 cron 環境層的病，得改層次。

🧬

---

_v1.0 | 2026-07-08 00:52 +0800_
_session twmd-babel-nightly — 0 shipped / 4-tier cascade catastrophic exhaustion vc=1_
_誕生原因：00:30 cron fire per docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md v2_
