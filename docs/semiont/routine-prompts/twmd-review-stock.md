---
name: twmd-review-stock
description: TWMD review stock (wed @ 22:00) — 審庫存：挑 1-2 篇 T1 高流量、從沒人審過的既有文章，FACTCHECK Quick + 冷讀席預審，落查證單並在文章掛 preReview 指標；讀者複核達標時機械轉 verified（via community）。Canonical MAINTAINER-PIPELINE §1d, thin shell, sonnet.
---

🧬 Taiwan.md routine: twmd-review-stock（每週三 22:00）。庫存從來沒有人巡邏過：maintainer 審進料口、rewrite 審要重寫的、feedback 審讀者回報的，沒有一條 routine 拿一篇已經在站上的文章逐條查證後蓋章。本 routine 就是那條。

🚨 STRICT BECOME GATE — 第一動作不可省略：跑 /twmd-become review 完整走 BECOME_TAIWANMD.md Step 0-9，Review mode self-test 全過才動。ACK 一行寫 memory 頂部：`✅ BECOME ack: mode=review / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`。

業務邏輯 canonical：docs/pipelines/MAINTAINER-PIPELINE.md §1d 審庫存（**完整 Read 不憑記憶**；它只 pointer 到 FACTCHECK-PIPELINE §Quick Mode 與 EDITORIAL-ROOM §總編室，兩邊 SOP 都要讀原檔）+ 薄殼 skill .claude/skills/twmd-review-stock/SKILL.md。執行：

1. `git checkout main && git pull origin main`。
2. Stage 1 選篇：`python3 scripts/tools/review-stock-pick.py --top 2 --json`（T1 ∧ 未人審 ∧ 非 verified，GA 流量排序，跳過近 14 天已預審與在 open PR 裡的）。exit 1 = 母體為空 → no-op finale，不算 fail。第一篇若是 FACTCHECK A 級（≥50 腳註／≥3000 字／引語 ≥10 句）本班只做它一篇。
3. Stage 2 FACTCHECK §Quick Mode：audit trail 落 `reports/research/YYYY-MM/{slug}.md` § audit（沒有就建，`type: 'research'` / `status: 'audit'`——月度巡邏抽樣靠這個檔排除已巡過的）。Hard gate 0 ❌ + 0 🔴 才進 Stage 3；⚠️ SOFT-FIX 當班修。發現 ≥3 個 ❌ → 不進查證單、登 ARTICLE-INBOX 待 Full Mode、換下一篇。
4. Stage 3 冷讀席：EDITORIAL-ROOM §總編室規格，3-4 支平行 Sonnet 探針（門面兌現／逐段主軸／H2 載體還原／閱讀節奏），各自乾淨 context，**禁讀研究報告與 audit，只拿成品＋標題**。
5. Stage 4 查證單：落 `reports/review-stock/YYYY-MM/{slug}.md`（frontmatter HARD schema 見 §1d：slug / checkedAt / factcheckVerdict / coldReadVerdict），文章 frontmatter 加 `preReview: reports/review-stock/YYYY-MM/{slug}.md`。**不動 `curation` / `lastHumanReview`**——預審不是人審。
6. Stage 5 讀者複核轉正：§1d 判準（preReview 存在 ∧ Supabase `article_confirmations` 獨立 user_id ≥ 3）。表尚未建立時本步 no-op，memory 寫明「Stage 5 skipped: article_confirmations 未建」。
7. Stage 6 lint + commit：每篇 `python3 scripts/tools/article-health.py <article> --check=curation-consistency`（preReview 指標必須指向存在的檔）。只 `git add` 本班碰的文章、research audit、查證單 → commit 標 `🧬 [routine] twmd-review-stock: {N} 篇預審（{slugs}）— YYYY-MM-DD` → `git push origin main`（main-direct；origin 領先先 rebase）。commit message 只印篇數，不印任何讀者身份欄位。
8. Stage 7 `/twmd-finale`：memory 必含 BECOME ACK + pick 輸出（母體數／picked／skip 數）+ 每篇 atoms／❌／⚠️／🔴 數 + 冷讀席必改數 + 查證單路徑 + Stage 5 狀態 + commit hash + Handoff 三態。

ROUTINE.md §排程表 + footnote ²⁷ 是本 routine 的 SSOT 登記，本檔是 mirror。設計：reports/design-review-stock-2026-09-05.md。
