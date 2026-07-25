---
name: twmd-embeddings-nightly
description: TWMD embeddings (nightly @ 05:00) — bge-m3 semantic index rebuild → src/data/related (reader related-articles) + public/api/rag (RAG vectors). Local mac-m4max primary + fleet fallback (v1.1 2026-07-05). Sovereignty-preserving, graceful-skip if embed host down. Canonical EMBEDDING-PIPELINE, thin shell, sonnet.
---

🧬 Routine `twmd-embeddings-nightly` — 每天 05:00 用 bge-m3 重建全站語意索引（keystone：一次產出讀者端 src/data/related「你可能也想讀」8 鄰居 + AI 端 public/api/rag 向量）。意思的座標在地端算、不出境。主節點 = 本機 mac-m4max（v1.1 2026-07-05 遷回，4090 離線 18 夜後哲宇拍板）。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become micro` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9。Micro mode self-test 7 題全過才能進 Stage 0。不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

```
✅ BECOME ack: mode=micro / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

## 執行：嚴格讀 + 跑 canonical pipeline

完整 SOP 在 `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/EMBEDDING-PIPELINE.md`（v1.1），**嚴格 Read 全檔再執行**，不憑記憶複寫 step。Stage 0-4 的 endpoint 解析、preflight、rebuild、verify threshold、commit 規則全部以 pipeline canonical 為準——**本殼不複寫任何 step 細節**（ROUTINE-PROMPT-CONTRACT：殼是 pointer，不是第二份 SOP）。

執行後 ACK 需 cite：`EMBEDDING-PIPELINE.md §前置`（實際解析到的 EMBED_HOST）+ `§Stage 2`（verify 結果）。

## 鐵律

- endpoint 解析走 pipeline §前置（本機 127.0.0.1 優先 + fleet registry 備援），不 hardcode IP、不憑舊記憶找 4090。
- 只 commit `src/data/related/`（public/api/rag + public/api/related 是 gitignored 產出）。內容無 diff → skip commit。
- embed host 不可達 → graceful skip 非 fail；連 3 天 skip 才 escalate LESSONS。
- Stage 4 `/twmd-finale`：memory 必含 BECOME ACK + 實際 EMBED_HOST + 6 語向量數 + fail rate + verify PASS/FAIL + commit hash（或 skip 原因）+ Handoff 三態。
- ROUTINE.md §排程表 + footnote ¹² 是本 routine 的 SSOT 登記。