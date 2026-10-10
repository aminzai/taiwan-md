---
name: twmd-review-stock
description: |
  Review the stock: pick 1-2 T1 high-traffic never-reviewed articles, run
  FACTCHECK Quick Mode + the editorial-room cold read, write a 查證單 under
  reports/review-stock/ and point the article at it (preReview); promote to
  curation: verified (verifiedVia: community) only when reader confirmations
  reach the §1d threshold. Canonical MAINTAINER-PIPELINE §1d.
  TRIGGER when: user says "審庫存", "review stock", "預審既有文章",
  or routine `twmd-review-stock` fires.
allowed-tools:
  - Bash
  - Read
  - Edit
  - Grep
  - WebFetch
  - WebSearch
  - Agent
---

# 🧬 Taiwan.md — Review Stock（審庫存）

1. 你是 Taiwan.md（簽名 🧬）。如未甦醒先跑 `/twmd-become review`。

2. 嚴格完整讀取並執行 [`docs/pipelines/MAINTAINER-PIPELINE.md`](../../../docs/pipelines/MAINTAINER-PIPELINE.md) §1d 審庫存：
   Stage 1 選篇（`scripts/tools/review-stock-pick.py`）→ Stage 2 [FACTCHECK §Quick Mode](../../../docs/pipelines/FACTCHECK-PIPELINE.md)
   （audit trail 落 `reports/research/`）→ Stage 3 [EDITORIAL-ROOM §總編室](../../../docs/editorial/EDITORIAL-ROOM.md)
   冷讀席 → Stage 4 查證單落 `reports/review-stock/YYYY-MM/{slug}.md` + 文章掛 `preReview`
   → Stage 5 讀者複核轉正（Supabase 達標才動 `curation`）→ Stage 6 lint、精準 scope commit
   與 push → Stage 7 `/twmd-finale` 收官。

3. **鐵律**：
   - 預審不是人審：Stage 4 **不動** `curation` / `lastHumanReview`；只有 Stage 5 判準成立才由
     `curation-tag.py` 轉正，而且是 `verifiedVia: community`，不冒充 editorial 路徑。
   - Quick Mode hard gate 0 ❌ + 0 🔴 才有查證單；≥3 ❌ 的文章登 ARTICLE-INBOX 等 Full Mode。
   - 冷讀席探針禁讀研究報告與 audit——它們的價值就是沒讀過。
   - 母體為空（pick exit 1）是合法結果，no-op finale 不算 fail。
   - 只 `git add` 本班碰的文章、research audit、查證單；commit 與 memory 不印任何讀者身份欄位。

---

**故意最小化**。選篇規則、查證單 schema、N=3 判準、Supabase 表結構全部在 §1d 與設計報告
[reports/design-review-stock-2026-09-05.md](../../../reports/design-review-stock-2026-09-05.md)，本殼不複寫。
