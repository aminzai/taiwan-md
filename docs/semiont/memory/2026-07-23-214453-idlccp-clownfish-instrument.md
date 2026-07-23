# 2026-07-23-214453-idlccp-clownfish-instrument — 小丑魚 9 PR + 儀器進化

✅ BECOME ack: mode=full（PR triage ≥5 + 新 workflow/threshold）/ wake-context selftest 全綠 / Q14 observer=哲宇

> session manual — 觀察者 `/twmd-become` + idlccp1984 全 PR 小丑魚 + 儀器 warn+lint+auto-heal + `/twmd-finale`
> Session span: 21:44:53 → 21:57:28 +0800
> 資料來源：gh pr list/diff、article-health、footnote-format-fix、contributor-pr-heal、taxonomy_subcat

## 觸發

哲宇要求 Full 甦醒後審 idlccp1984 全部 open PR，以小丑魚原則代修，並把「關聯文是否存在 / max match / 子分類 / 腳註」從純 warn 升到 warn + lint + auto-heal + advanced-review-required。先寫深度研究報告與實作計劃，再完整執行，最後 finale。

## 儀器進化（Wave A）

先造橋再收 PR。研究報告落在 `reports/idlccp1984-pr-batch-instrument-evolution-2026-07-23.md`。

link-target 先 unquote percent-encoded 路徑再做存在性檢查。台灣迷因四條延伸閱讀（PTT批踢踢、馬英九迷因、長輩圖、台灣VTuber）本來全活，卻被報 broken。補上 difflib max-match 與 ratio，唯一 top 且 ratio≥0.90 可 `--fix` auto-heal。

subcategory 由 `taxonomy_subcat.py` 從 taxonomy 與 keyword boost 推 top match。高信心寫入 frontmatter，中信心 HARD 訊息帶 candidates 與 advanced-review-required。中元節因「節慶與禮俗 0.86 vs 宗教與民俗 0.83」margin 不足，改人手指定。

footnote-format-fix 把 GitHub `[display](#user-content-fn-REALID)` 轉成 `[^REALID]`（必須用真實 id，不是 display 編號）。NET 的 `[1](#user-content-fn-19)` 曾被錯轉成 `[^1]`，這次根治。編號列表用 fnref-N 當真 id，yaml code fence frontmatter 拆成 `---`。

`contributor-pr-heal.py` 一鍵串起 footnote、article-health --fix、recheck。儀器 commit：`2a583ad30`。

## 九篇 PR 代修（Wave B）

idlccp1984 共 9 個 open PR，內容級多為 B+ 到 A-，阻塞幾乎全在格式。紅旗 0/10。Decision matrix 全部走 merge + heal。

#1236 台灣迷因重寫合入並 decode 延伸閱讀。#1233 萊爾富、#1232 NET、#1229 紡織業進 Economy（企業列傳或經濟發展）。#1231 農曆七月與 #1230 中元節進 Culture 節慶與禮俗。#1227 當兵進 Society 社會制度。#1226 牡丹社事件進 History 殖民與帝國。#1225 台灣與北朝鮮關係進民主與治理，並做 advanced review：刪 Google 搜尋頁 source，hedge 無來源的「前法官走私煤炭」主張。

九檔 pre-commit hard=0。內容 commit `96bf8d193`（Co-authored-by: idlccp1984）。main push 後 9/9 `gh pr close` 並用中文感謝，說明不必再改 GitHub 格式。

## Beat 5 — 反芻

純 warn 把格式稅轉嫁給最不會 GitHub 的貢獻者。小丑魚原則若不連儀器一起進化，每次 batch 都要重發明同一套 regex。真正的繁殖友善是他專心寫故事、格式由 `--fix` 接住，只有 source 錯配與品味判斷才進 advanced-review。

## Handoff 三態

繼承（來自 214147-pr-review-refresh-finale）仍 pending：

- [ ] hi 剩 12 篇 P0 待譯。
- [ ] 68 檔英文假翻譯待重譯。
- [ ] person-fidelity 仍缺 file-level occurrence-count。
- [ ] `codex/recover-kmt-projection` 續寫。
- [ ] 42 個保留 worktree 救援盤點。
- [ ] #1228 draft 等作者 ready（或哲宇授權）。
- [ ] scheduled-tasks rider / routine-live-state dump。
- [ ] 兩個保護 stash 未 pop。

本 session 新 handoff：

- ~~[x] #1236 等作者修~~ → **retired**：小丑魚代修已合 main（`96bf8d193`）。
- [ ] 九篇新文缺 media / rationale / 深度 <4500：排 EVOLVE polish backlog（非擋 ship）。
- [ ] contributor-pr-heal dogfood 下一批 external PR；收集 fuzzy auto-heal vc。
- [ ] 中元節類 ambiguous subcategory：考慮降 margin 或分 category 權重。

🧬
