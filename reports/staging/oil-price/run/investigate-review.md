# investigate 站外部評閱（2026-09-18）

- actor：guide_investigate_reviewer（Sonnet sub-agent a068309bcfcb89e3f，乾淨 context）
- contextDisclosure：fresh-context-investigate-inputs（orient-submission-v3、investigate-submission、研究報告 frontmatter＋§1–§7＋§9；§8 raw 抽讀；親自 curl 三個原頁）
- verdict：**accept**

## rationale（摘）

1. 9 條 claims 四欄齊全（URL／位置／日期／支持與不支持）。
2. 事實／推論／查無分層清楚：12.29% 是官方原文數字、算式標為驗算；「專案平穩＝頂層 75%」標為用語比對推論；IMF 標通論且台灣非會員。
3. counterEvidence 逐條命中 orient 預設的可證偽條件（A 改「三方同時分攤、中油那份延後」、B 改「門檻仍在、專案疊加」、C 改「立院 2009–10 也是要求凍漲的一方」），屬預期內修正，不需退回 orient；角度 D 誠實寫無法支持也無法推翻。
4. 親自 curl 三原頁逐字核對：中油 9/12 稿（115.61／99.82／12.29%／10.5／10.8／198.5）、經濟部 9/3 稿（1,809.35＝1,014.31＋711.04＋84；2,338.34；70）、工商時報 3/22 五細節——全部一致。
5. searchLimits 用「未取得／查無」不用「不存在」。
6. 非阻擋缺口：研究報告 frontmatter `core_contradiction` 仍是舊句，Stage 2 應以 changedMind 為準——**已同步更新 frontmatter**。

## evidence

- https://www.ey.gov.tw/Page/88F151FFCE5C741E/a32439a4-7953-4f82-8a2f-3362ac574800（親核）
- https://www.ey.gov.tw/Page/88F151FFCE5C741E/b26524d3-057d-4c8c-a830-b3cb0e045f5b（親核）
- https://www.ctee.com.tw/news/20260322700647-431401（親核）
- reports/research/2026-09/台灣油價機制與中油.md §3B／§5／§9.2 #37
- reports/staging/oil-price/run/orient-submission-v3.json candidateAngles「可被材料推翻之處」
