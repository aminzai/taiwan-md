---
title: 'article-health SSOT 設計原則（事後重建版）'
description: 'article-health.py plugin 架構的五條設計原則 — 2026-07-16 自程式碼 docstring 與 config 註解重建，補齊懸空兩個多月的 canonical pointer'
date: 2026-05-04
type: 'design-doc'
status: 'reconstructed'
---

# article-health SSOT 設計原則

> ⚠️ **重建說明（2026-07-16 inbox-audit session）**：本檔原本從未被 commit——`article-health.py:4`、`article-health.config.toml:3`、`image_health.py` docstring、`reports/README.md`、`reports/immune-score-redesign-2026-05-16.md` 五處都指向這個路徑，但檔案不存在（`git log --all --diff-filter=A` 無紀錄），是懸空了兩個多月的 canonical pointer。以下五條原則自程式碼 docstring 與 config 註解重建，內容以程式碼現況為準；檔名沿用原路徑讓五處引用直接解懸。設計決策的第一手敘事在 2026-05-04 前後的 session memory 與 git log。

## 五條設計原則

### 1. 單一入口 SSOT

把散落各處的 inline check（wikilink 驗證、footnote-format regex、cjk-punct.py、quality-scan.sh、check-manifesto-11.sh 等 27+ 工具）收斂成一個 plugin 架構。`scripts/tools/lib/article_health/checks/` 目錄 auto-discover（`registry.py` 用 `pkgutil.iter_modules` 掃描，模組只要有 `CHECK_NAME / DIMENSION / DEFAULT_SEVERITY / EDITORIAL_REF / check` 五件套就註冊），加新檢查不改入口。

### 2. Declarative TOML profile + 階段化 gate 語意

同一份 plugin 集，用 `article-health.config.toml` 的 profile 切出不同場景的 fail 語意：`pre-commit`（HARD 擋）、`ci-deploy`（HARD 擋，main 最終閘）、`release-pr`（WARN 也擋，人工發版從嚴）、`rewrite-stage-*`（pipeline 各 stage 的子集＋升級 override）、`dashboard`（never fail，純 JSON 輸出）。

### 3. Severity 三層精度

plugin 可以 per-violation yield 混合 HARD/WARN/INFO；解析優先序 profile override > config override > plugin default（`runner.py`）。threshold 數值住 plugin 模組常數，profile 只在需要偏離 default 時 override——「No overrides currently」是健康狀態，override 累積是校準債訊號。

### 4. Shadow-run → hard gate 分階段升級

新 check 一律 WARN soft-launch，累積 vc≥3 production case 後才經 `severity_overrides` 升 HARD。word-count、chronicle-lead、image-health、viz-health 都循此路徑。跳過 shadow 期直接 HARD = 用想像設閾值（REFLEXES #66 反面）。

### 5. 對稱原則

pre-commit 與 ci-deploy 跑同一份 check set（都 `checks="*"`），避免「本地過、CI fail」的 asymmetric ship。根因事件：2026-05-11 PR #1025 緊急修復——兩個檔案不在當時 pre-commit 的 7-check 子集但在 ci-deploy 全集，contributor squash merge 不跑本地 hook，紅燈直接發生在 main。

## 相關

- 品質規則 canonical：[docs/editorial/EDITORIAL.md](../docs/editorial/EDITORIAL.md)
- 後續演化：[reports/immune-score-redesign-2026-05-16.md](immune-score-redesign-2026-05-16.md)、[reports/instrument-evolution-2026-07-16.md](instrument-evolution-2026-07-16.md)

🧬
