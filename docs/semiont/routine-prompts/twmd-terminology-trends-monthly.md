---
name: twmd-terminology-trends-monthly
description: TWMD terminology trends (monthly @ 每月 5 日 10:30) — 用語保存計劃月度趨勢觀察：SC 需求 → 多切面搜索 → 缺口對照 → 高信心入庫 ≤20 條 → 月度趨勢報告。Canonical TERMINOLOGY-TRENDS-PIPELINE, thin shell, opus.
---

🧬 Taiwan.md routine: twmd-terminology-trends-monthly（每月 5 日 10:30）。用語保存計劃的月度趨勢觀察：看這個月哪些中國用語在進來、哪些被收編、哪些誤判被翻案，高信心缺口入庫，累積台灣視角的語言滲透時間序列。

🚨 STRICT BECOME GATE — 第一動作不可省略：跑 /twmd-become write 完整走 BECOME_TAIWANMD.md Step 0-9，Write mode self-test 全過才動。ACK 一行寫 memory 頂部：`✅ BECOME ack: mode=write / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`。

業務邏輯 canonical：docs/pipelines/TERMINOLOGY-TRENDS-PIPELINE.md（7 stage + 6 hard gate，**完整 Read 不憑記憶**）。執行：

1. `git checkout main && git pull origin main`。
2. Stage 1 DEMAND：`python3 scripts/tools/terminology-demand-rank.py --days 28` ＋ `--state MISSING`——MISSING 清單是入庫第一優先。
3. Stage 2 SWEEP：6-8 切面、每切面 10-15 次搜索（固定四切面：Threads 支語現場／PTT 近月新串／中國年度流行語榜單／誤判鑑定討論；機動切面看上輪報告）。⚠️ 「台灣怎麼說」引台灣網友原話，不憑模型語感——模型預設中國語料，會把台灣名洗向中國名。
4. Stage 3 GAP 雙防線查重 HARD gate：檔名 `test -f` ＋ 新詞值對全庫 china/taiwan 值掃描（含簡繁形），兩道都跑。
5. Stage 4 INGEST：≤20 條/輪 HARD 上限；每條必帶 etymology.origin 詞源敘事＋sources 證據 URL（薄殼進不了長尾，GA4 實證）；日源／方言／港澳／台灣本有四型誤判逐條查、命中即 notes 誠信標註。QA 四件套：yaml parse＋`node scripts/tools/terminology-charcheck.js`＋重複掃＋`python3 scripts/core/extract-china-terms.py`。
6. Stage 5 REPORT：`reports/terminology-trends/YYYY-MM.md` 短報告（新進詞／收編動態／誤判翻案／需求變化，1-2 頁）。
7. Stage 6 QUEUE：刪除類／政治敏感判定（「是支語嗎」徽章類）／大批重分類一律進 OBSERVER-QUEUE 不自主施作。
8. commit 標 `🧬 [routine] twmd-terminology-trends: {N} 詞入庫＋{月份}趨勢報告 — YYYY-MM-DD` → `git push origin main`（origin 領先先 rebase）。
9. Stage 7 `/twmd-finale`：memory 必含 BECOME ACK＋搜索切面數與次數＋入庫數／查重攔截數＋QA 結果＋commit hash＋Handoff 三態。

ROUTINE.md §排程表 + footnote ²⁴ 是本 routine 的 SSOT 登記，本檔是 mirror。範本：首輪 reports/terminology-zhiyu-deep-research-2026-08-04.md。
