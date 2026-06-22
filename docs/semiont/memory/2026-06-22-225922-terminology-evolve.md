# 2026-06-22-225922-terminology-evolve — 用語頁面進化：GA/SC 觀察 → 四層全實作 ship

> **Session span**: 2026-06-22 22:59 → 2026-06-23 00:xx +0800 Asia/Taipei
> 資料來源: git log %ai
> Mode: Full BECOME（strategy → 觸碰 ~2,336 頁 page-type 進化，§自主權邊界 命中，哲宇「完整全部做」明確授權）
> 兩階段：先歸檔 report（哲宇 review）→ 哲宇「完整全部做跟進化」→ 全四層實作 ship

## 觸發

哲宇 manual directive：「最近很多用語頁面開始被搜尋引擎收錄。用語頁面有點陽春？上面有奇怪的 padding，
可以統一用 hero 元件。完整觀察 GA、SC，思考怎麼完整進化 terminology 頁面，先歸檔 report。」
per-term 頁（`/terminology/{詞}`）2026-06-13 上線，到今天約 9 天進入第一波索引。

## GA/SC 觀察（用 converter-analytics.py + sc-query.py + ga-query.py 直連）

per-term 頁**正在做被設計來做的事**：吃「{中國詞}台灣用語」長尾、被收錄、排得不差（很多 pos 1–5）。
但曝光沒轉點擊——demand class 96 詞 / 587 impr / 22 clk / **3.7% CTR**，而且 8+ 個詞**排到 pos 1.0 卻 0 點擊**
（優化 / 屏蔽 / 監控 / 頭像 / 乾貨 / 復盤 / 補丁）。pos 1 + 0 clk = SERP 標題/摘要沒打中意圖的鐵證，
是內容+snippet 問題，不是排名問題。第二種意圖「X 是支語嗎」（便利店/卸載/嘴替是支語嗎）完全沒接。
有需求但詞條不存在：出片(17)/內耗(17)/調研(11)/進度條(6)/打碟(6)。

## 三個 root cause（為什麼陽春）— data/terminology 全庫體檢 2,334 條

1. **77%（1,807）只有對照零內文** → 結構性陽春，不是版型問題。
2. **1,655 條把佔位垃圾「台灣用法/中國用法」當詞源 render**（`hasEtymology` 只判非空）→ 71% 頁有可見填充物。
3. **1,716 條 fork_type=B「1949 分流」是 import 預設值，93% 零佐證**，頁面卻把「1949 分流」當事實寫出來
   （很多是視頻/激活/內捲等網路詞，跟 1949 無關）→ 內容誠信問題，給錯比少給嚴重。
   根因：ThunderKO/1997 那批 import（B+佔位+署名 notes）vs caris-events/invade（E+有肉）兩批品質落差。
4. **hero padding**：三頁都已用 PageHero（「統一用 hero」其實做完了），per-term 用 `padding="default"`(py-16)
   對精簡 hero 太大，撐出哲宇看到的深色空帶。修法 = 改 `padding` 值，不是搬元件。

## 產出

[reports/terminology-page-evolution-2026-06-22.md](../../../reports/terminology-page-evolution-2026-06-22.md)：
四層策略（內容誠信 → 數據驅動加肉 → SERP 轉換 → 呈現層）+ P0–P5 分階段 ship 表 + 自主權邊界標注 + 6 個給哲宇的決策點。

## 執行（哲宇「完整全部做跟進化」後 — 全四層 ship）

逐 commit（全 preview 驗 + 逐階段 commit/push）：

1. **template P0-P2** `0dbc2fc08`：placeholder render-filter + fork 誠信閘（無佐證不顯示「1949 分流」）+ hero padding compact + 直答 lead 段 + 常見問題 FAQ（中性回答「算中國用語嗎」）+ FAQPage JSON-LD。
2. **demand-rank tool** `a83b51669`：`scripts/tools/terminology-demand-rank.py` — SC 需求 join 詞條豐富度 → enrich 排序（MISSING/MAPPING/RICH），self-contained 最小 YAML reader（venv 無 pyyaml）。candidate cron。
3. **P3 加肉** `1425e0e83`：usage.example 模組「台灣人會這樣說」+ lead/FAQ 改 fork-aware（E 詞不再被斷言純中國用語）+ enrich 9 詞（啟用/網際網路/解除安裝/修補程式/頭貼/代碼/關注 fork→C，復盤 fork→E 圍棋 origin web 查證）+ 新建 調研。
4. **notes 誠信** `a061300c8`：補充段過濾屬名 notes（辣眼睛等 ~230 caris 詞條不再把「來源：caris」當內容）。
5. **placeholder 全庫清除** `8b01ab81e`(混入並行 commit, 見下)：1654 檔移除佔位 etymology，逐檔 parse 前後結構驗證等價 0 corruption。
6. **高畫質 heal** `d33d1b0e0`：修 pre-existing YAML 語法錯（未跳脫引號）→ 復活 per-term 頁 + 加肉。全庫 2336 檔 0 parse failure。

**未做（flag 哲宇）**：fork_type 1716 個 B 預設的全量重分類 — 非可安全自動化（逐詞語言學判斷），template 誠信閘已解 render 層，enrich 漸進修正。fuzzy mapping MISSING 詞（內耗/出片/打碟/維度/高光時刻/進度條/質地）需哲宇定 Taiwan 對應（怕造錯映射）。

## 收官 checklist

| 項                                      | 狀態               |
| --------------------------------------- | ------------------ |
| report 歸檔 reports/                    | ✅                 |
| 四層全實作 ship（6 commit 全 push）     | ✅                 |
| preview 逐頁驗（啟用/復盤/調研/辣眼睛） | ✅ 0 console error |
| 全庫 2336 檔 0 parse failure            | ✅                 |
| MANIFESTO §11 自檢                      | ✅                 |
| MEMORY.md index row                     | ✅                 |
| commit/push                             | ✅ d33d1b0e0       |

## Handoff 三態

- **pending（給哲宇決策）**：fuzzy mapping MISSING 詞（內耗/出片/打碟/維度/高光時刻/進度條/質地）的 Taiwan 對應；fork 1716 B 全量重分類要不要做（template 閘已護 render，非急）。
- **pending（可接續）**：demand-rank tool 排 cron（twmd-terminology-demand-weekly）；index 頁 1321 impr/0.2% CTR 止血（report §L3d）；觀察 7-14 天 SC 看 CTR 有沒有從 0 動起來。
- **blocked**：無。
- **retired**：report-only handoff（已全做完）。

## Beat 5 — 反芻

「排第一名卻 0 點擊」這個訊號比任何 KPI 都乾淨：它把問題從「排名 SEO」精準切到「轉換 + 內容誠信」。
我差點預設往「加更多 SEO」想，但數據說排名已經有了，缺的是頁面接得住意圖。神經迴路那條
「數據告訴你該看哪裡，不告訴你該做什麼」這次很實在——SC demand 排序告訴我加哪些詞，
但「某詞算不算支語」的判定門檻是策展立場，不能讓數據自動展開，得留給哲宇（fork 全量重分類也同理沒硬做）。

**多核心碰撞實例（REFLEXES #9 又一次驗證）**：1654 檔 placeholder cleanup 我 `git add` 後，並行的
黃仁勳-evolve session 同刻 `git commit`，把我 staged 的 index 一起掃進它的 memory commit `8b01ab81e`
推上去——我的 commit message 沒了、檔案沒丟（全在 HEAD）。長批次任務第一動作該開 worktree
（semiont-worktree.sh）讓 commit 污染結構性不可能；我貪快直接在主 wd 跑 → 踩中。資料零損失因為
有逐檔結構驗證 + push 後 ground-truth 重核，但 git 歷史被混進不相干 commit 是真實代價。

---

_作者：Taiwan.md 🧬｜2026-06-22-225922-terminology-evolve_
