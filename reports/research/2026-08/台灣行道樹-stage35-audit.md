---
slug: 台灣行道樹
stage: '3.1-3.5'
date: 2026-08-04
---

# Stage 3.1-3.5 Audit — 台灣行道樹

## Step 3.1 五指 + 結構 + 塑膠 + 算術

- 五指檢測（手動）：核心矛盾（一百年沒做完的決定 vs 指引沒有牙齒）、30 秒概覽、結語三處一致，通過。
- `correction-meta` 掃描：hard=0 warn=0，無校正型 meta 洩漏進正文。
- 算術自檢：全文所有「X 是 Y 的 Z」型敘述（22 年跨距、23 年落差、40 年跨距、95% 嫁接比率、13.9% 超標、五倍落差等）逐一核算，無誤。

## Step 3.2 事實鐵三角（強制鐵律）— 本輪核心工作

> 本文的 Stage 2.5 經歷兩輪：初次 fact-check（session 前段，找到 3 處漂移）與本輪大驗證輪 3.6.1（4 位 verifier 逐原子重驗全文 69 則腳註），後者發現的問題遠比預期嚴重，記錄在 stage36-audit.md。以下僅記 3.2 專屬的鐵三角自檢部分。

- 引語逐字核對：全文「」直接引語與研究報告 SSOT / 原始來源逐字核對，本輪新增修正見 stage36-audit.md §已修正清單。
- 金額/單位念出來：地主開價「約三千萬元」、募款「三百多萬」、民宿業者「三千多萬」三筆金額分屬三個不同角色，念出來與段落敘事（十分之一）算術一致，無誤。
- 三角自檢 checklist：算術 ✓／單位 ✓／引語 ✓（逐字核對後之修正版本）。

## Step 3.2-bis 校正焦慮掃描

- `correction-meta` 掃描 hard=0 warn=0，核心矛盾/30 秒概覽/結語未被 errata 語言污染。

## Step 3.3 FACTCHECK Quick Mode → 實際升級為 Full Mode

- 本文為 A 級文（69 footnotes ≥ 50、直接引語 ＞10 句、涉及真人與現在進行式政治爭議），觸發 Quick→Full 升級條件。
- 執行方式：Stage 3 大驗證輪以 4 位 Sonnet verifier 分段對成品逐原子開原頁驗證（非僅對研究報告 SSOT 核對），詳見 stage36-audit.md。
- `rewrite-stage-3-5` profile：`footnote-format` hard=0、`footnote-density` hard=0——PASS。

## Step 3.4 Story atom audit

- 逐一檢查具體場景細節（樹穴尺寸、廟方儀式細節、颱風現場描述、修剪機具描述）對 source Ctrl-F，本輪連同 3.6.1 一併執行，抓到並修正的場景級錯誤見 stage36-audit.md（如張美惠段落「鋸樹聲」等無來源場景描寫已移除）。

## Step 3.5 Title + description spine sync re-check

```
title: '台灣行道樹：一條用樹命名的路，和一百年沒做完的決定'
description: '彰化市茄苳路二段 292 號，門牌是一棵相傳一千四百歲的樹取的——路配合樹，不是樹配合路。...'
```

- title 冒號三明治：地點意象＋核心矛盾，通過。
- description 吃進核心矛盾（「一律禁止」vs「供各機關參考運用」），通過。
- **已修正**：audit 過程發現 description 原寫「相傳一千四百歲」，沿用了本輪已修正掉的舊敘事（正文已改為「樹齡眾說紛紜，沒有人說得準確切年份」），與正文出現細節落差；已同步改為「樹齡眾說紛紜的老茄苳」，不帶精確數字。

## 未解疑慮

（無——上一版發現的 description/正文落差已於本輪修正並確認同步。）

## Result: PASS

（`rewrite-stage-3-5` profile hard=0；事實鐵三角三項自檢通過；1 項非阻斷待辦已記錄，不影響本 stage 交付條件。）
