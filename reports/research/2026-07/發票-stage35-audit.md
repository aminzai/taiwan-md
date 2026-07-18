---
article: knowledge/Economy/發票.md
stage: 3.1-3.5-self-check
date: 2026-07-18
session: a5a84176-15fa-4c5e-b1ae-e4197b43353f
auditor: Taiwan.md session（主 session 親跑，未派 sub-agent）
---

# Stage 3.1-3.5 Self-Check Audit — 發票

依 QUALITY-CHECKLIST.md 逐步跑過 Step 3.1（五指/結構/塑膠/算術）、Step 3.2（事實鐵三角）、Step 3.2-bis（校正焦慮掃描）、Step 3.3（FACTCHECK Quick Mode citation gate）、Step 3.5（title/description spine sync）。Step 3.4（story atom audit）與更深入的逐原子查核併入 Step 3.6 fan-out（見 `發票-stage36-audit.md`），本檔記錄 Step 3.6 派工**之前**、主 session 親自完成的自檢與工具 gate。

## Step 3.1：五指 + 結構 + 塑膠 + 算術

- 五指檢測（手動）：開場場景／設計者命運轉折／制度借用擴張／演算法信任危機／收尾呼應開場——六 section 對應論點骨架六步，過關。
- 結構驗證：H2 對應藍圖動作序列，非可 shuffle 面向巡禮（Step 2.5-R 結構主編已驗證，見 `發票-prose-structure-review.md`）。
- 塑膠掃描（後半段重點）：手動通讀 section 4-6，未見罐頭句式；`prose-health` plugin score 2（≤3 通過）。
- 自動驗證：`article-health.py --check=prose-health` — hard=0 warn=3（對位句型 1 處、AI ritual 句 1 處累計、破折號 8 個均遠低於 15/1500字 閾值），對位句型該句就是全文核心反轉論點所在，判斷保留合理不修改。

## Step 3.2：事實鐵三角

### 3.2.1-3.2.2 算術＋單位自檢（主 session 手動逐條驗算）

- 稅收 2,900萬→5,100萬 +75%：(5100-2900)/2900=75.9%≈75%（史料原文自陳精確值），過關。
- 捐贈量 1.14 億→4,100 萬「降六成」：精算 64.0%，史料原文自己用語即為「驟減6成」，過關（見下方修正記錄，footnote 精確位數已修正為原文模糊值）。
- 千萬富翁 957+307=1,264：與 NOWnews 原文三數字內部一致，過關。
- 檢舉「7,000件/600件」600/7000=8.57%≈「不到一成」，過關。
- 「檢舉一筆百元漏開發票領一塊錢」：主 session 直接 curl TVBS 原文確認「假設單次消費100元，也只能拿到1元獎金」逐字成立，過關。

### 3.2.3 引語逐字核對（Ctrl-F 全文「」引語）

發現並修正 1 處：L58「四十年營業稅的收入共五千一百多萬元…」以「」直接引語呈現，但財政部史料原文用阿拉伯數字「5,100多萬元」，中文數字轉寫版本 Ctrl-F 對不上原頁——已改為間接轉述句式，移除引號。

## Step 3.2-bis：校正焦慮掃描（quality gate，非 callout-triggered EVOLVE 強制項，仍主動跑）

`article-health.py --check=correction-meta`：warn=1（「先把一件事分清楚」）。人工複核：此句是向讀者釐清集點樹活動與統一發票主開獎是兩個不同機制，屬讀者必要的範圍界定，非回應本文自身過去錯誤的校正焦慮句式，判斷保留。論點脊椎自檢：30 秒概覽／結語未見「歸屬要正確」類 meta 句，通過。

## Step 3.3：FACTCHECK Quick Mode — citation plugin gate

`article-health.py --profile=rewrite-stage-3-5`：

- 首輪跑出 2 個 hard footnote-format 違規（[^15][^23] URL 與 em-dash 之間夾帶額外括號文字破壞 canonical regex）——已修正，複跑 hard=0。
- footnote-density：hard=0 warn=0。
- `ARTICLE_HEALTH_NETWORK=1 --check=footnote-url`：14 個 warn，全部為 SSL 憑證錯誤（.gov.tw 站台常見）或 HTTP 403（bot 偵測），非真實 4xx/5xx 死鏈——主 session 已對其中多條同 URL 直接 WebFetch 成功驗證內容存在（例：footnote 1 的 museum.mof.gov.tw），判斷非 🔴 DEAD-LINK，不構成 hard gate 違反。

## Step 3.5：Title + description spine sync re-check

```
title: '發票：1951 年那張把全民變成稅務稽查員的紙'
description: '1951 年元旦，38 歲的財政廳長任顯群把抽獎號碼印上收據，讓消費者的貪念替國家看住了店家有沒有報稅，一年就把營業稅收拉高七成五。七十多年後，這套設計比它的發明人活得久、比它誕生時的威權統治都活得久——直到 2024 年一場程式碼風波，才第一次讓人問出口：這套系統憑什麼還值得相信？'
```

- title 冒號三明治：主體「發票」＋轉折「1951 年那張把全民變成稅務稽查員的紙」，過關。
- description 吃進核心矛盾：反射動作 vs 稽查恐嚇（Step 2.0 論點）、活得比發明人與威權統治都久、2024 年信任危機——過關；「主動」「威權政體」兩處用詞在 Step 3.7 總編室門面兌現探針發現與正文有落差，已回修（見 `發票-stage36-audit.md`／`發票-chief-review.md`）。

## Stage 3.1-3.5 Checklist

- [x] 五指檢測 + 結構驗證 + 塑膠掃描
- [x] 算術自檢（所有金額/百分比關係）
- [x] 單位念出來（無異常量級）
- [x] 引語逐字核對（1 處發現並修正）
- [x] 校正焦慮掃描（1 處複核判斷非違規）
- [x] citation plugin gate（`rewrite-stage-3-5` profile hard=0）
- [x] footnote-url 健康檢查（14 warn 均為存取方法artifacts，非真死鏈）
- [x] Title/description spine sync re-check（2 處用詞落差，於 Step 3.6 統一回修）

## Result

**PASS**（3 處修正：1 個直接引語降級為轉述、2 個 footnote-format hard violation 修正；其餘自檢無 blocking 發現，title/description 用詞落差併入 Step 3.6 總編室回修一次到位，不重複修改）
