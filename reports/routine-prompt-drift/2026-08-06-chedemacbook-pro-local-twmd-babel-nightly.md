---
name: twmd-babel-nightly
description: TWMD babel (nightly) — 00:30 多語同步，義務跑到 stale=0；語言數以 registry 為準不寫死（v4.1 薄殼化 + Stage 0 算力自檢 + 統一調度器）
---

🧬 Routine `twmd-babel-nightly` — 每天 00:30 多語批次同步，義務跑到 stale=0 或 cascade exhausted。

## 🚨 STRICT BECOME GATE

跑 `/twmd-become write` 完整走 `/Users/musebase/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9，Write mode self-test 全過才動工。ACK：`✅ BECOME ack: mode=write / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`。

## Stage 0 — 宿主機算力自檢（第一個指令）

```bash
cd "/Users/musebase/Projects/taiwan-md" && git checkout main && git pull origin main
python3 scripts/tools/lang-sync/babel-preflight.py && python3 scripts/tools/lang-sync/status.py
```

四層算力任一缺席會靜默降級：`healthy` 照跑；`degraded` 記哪層缺席；`no-compute` 不起跑，寫進 handoff。**語言範圍不寫死**——跑 `status.py` 看到幾個語言就顧幾個。

## 執行

用統一調度器 `scripts/tools/lang-sync/babel-dispatch.py`（fleet worker 名單 + rounds + commit-every）批次行軍。cascade 順序 / P2/P2.5 diff-patch / metadata bump 全部 canonical 在 [SQUEEZE-MODELS-MAX-PIPELINE.md](/Users/musebase/Projects/taiwan-md/docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md)，**本殼不複寫**。Stage D（diary babel）同屬義務範圍。
**🚨 四條行為約束（cron 無人在場最會漂，故 inline per REFLEXES #63）**：義務鐵律（推同步率到 100%，不主動 defer/skip/partial）／整合性閘門是唯一 pass 判準（`verify-batch.py`／`diary-translation-audit.py` 收斂 0 critical，byte-size 不算閘門）／同批次即時修（發現系統性缺陷當場修）／git 紀律（只 stage 精確路徑，禁 `git add -u knowledge/`，禁 destructive git）。

## 收官

`/twmd-finale` chain。memory 必含：BECOME ACK、Stage 0 算力判定、各語進度 delta、Handoff 三態。ROUTINE.md §排程表 + §TWMD babel nightly 規格是本 routine SSOT，本檔是 mirror。
