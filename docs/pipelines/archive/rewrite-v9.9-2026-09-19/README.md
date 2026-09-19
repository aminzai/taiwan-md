# REWRITE v9.9 多檔型 — 退場歸檔（2026-09-19）

**最後活著的 commit**：`7d3b6d4b06`（2026-09-19 09:50，`025d356a6f` 切換 commit 的 parent）。這個目錄是 `git mv` 搬進來的，歷史連續，`git log --follow` 追得到每一檔。

**內容**：薄索引本體 `REWRITE-PIPELINE-v9.9-index.md`、十一個 `REWRITE-STAGE-*.md` contract、互動式協議 `REWRITE-GUIDE.md` 與 `scripts/{cli,engine,prompts,view}.mjs`、工具生成的單檔閱讀版 `REWRITE-PIPELINE-單檔案型完整流程.md`（最後一次生成結果，當證據）、生成器 `scripts/build-rewrite-single-file.py` 與兩份測試。

**為什麼退場**：v6.7（2026-06-04）到 v9.9（2026-09-07）之間 87 個 commit，每一段都是一次錯誤換來的，沒有一段是一次「悶」換來的。2026-09-18 三篇（誰算低薪／台灣油價機制與中油／金鐘獎）走完互動式六站、十五位冷讀者、三輪 release 全綠上線，哲宇讀後「文謅謅、沒人味、像堆砌不像有主見的分析、過度強調數字」。隔天同三篇用 v6.7 單檔版重做，閱讀感明顯好轉。根因：第三型「不收束」規則給了「不主張」的合法出口、研究 lane 沒有一條去找人、冷讀者每問一次困惑寫手就多塞一個限定詞。完整紀錄：`docs/semiont/LESSONS-INBOX.md` 的 `third-type-thesis-defaults-to-meta-observation`、`docs/semiont/diary/2026-09-19-003000-news-radar.md`、整併工單 `reports/staging/rewrite-consolidation-brief-2026-09-19.md`。

**現行 canonical**：`docs/pipelines/REWRITE-PIPELINE-SINGLE.md`（v6.8）。行數帽 2,300，只走 v6.x patch；不設冷讀站、不設多席編輯室、不加後設論點形態。

**怎麼復活**：`git mv docs/pipelines/archive/rewrite-v9.9-2026-09-19/REWRITE-STAGE-*.md docs/pipelines/`，index 搬回 `REWRITE-PIPELINE.md`，`scripts/*.mjs` 搬回 `scripts/rewrite/`，`scripts/twmd.mjs` 把 `rewrite` 子命令加回 COMMANDS，測試搬回 `tests/`。不建議：先問這次要復活的是哪一段，那一段當初是為了哪一次錯誤長出來的。
