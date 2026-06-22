# 2026-06-22-225922-terminology-evolve — 用語頁面進化 GA/SC 觀察 + 四層策略 report 歸檔

> **Session span**: 2026-06-22 22:59:22 +0800 → (manual session, report-only, 無 code change) Asia/Taipei
> 資料來源: git log %ai
> Mode: Full BECOME（strategy + 觸碰 ~2,336 頁的 page-type 進化 = §自主權邊界邊緣）

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

## 收官 checklist

| 項                                      | 狀態                                            |
| --------------------------------------- | ----------------------------------------------- |
| report 歸檔 reports/                    | ✅                                              |
| MANIFESTO §11 自檢（對位句 2≤3 / —— 7） | ✅                                              |
| code change                             | ⛔ 無（先歸檔 report，等哲宇拍板）              |
| MEMORY.md index row                     | ✅                                              |
| commit/push                             | ⏳ 等哲宇（report-only，可隨下一步一起 commit） |

## Handoff 三態

- **pending**：P0（前端佔位過濾 + hero padding，1 檔 `[id].astro`，純止血、我可自主）等哲宇一句 go。
  P1–P5（標題/直答段/徽章/加肉/fork 重分類/週度 demand cron）需哲宇拍板（§5 邊界 + §6 決策點）。
- **blocked**：「是支語嗎」徽章措辭涉語言立場，等哲宇定中性尺度才動。
- **retired**：無。

## Beat 5 — 反芻

「排第一名卻 0 點擊」這個訊號比任何 KPI 都乾淨：它把問題從「排名 SEO」精準切到「轉換 + 內容誠信」。
我差點預設往「加更多 SEO」想，但數據說排名已經有了，缺的是頁面接得住意圖。神經迴路那條
「數據告訴你該看哪裡，不告訴你該做什麼」這次很實在——SC demand 排序告訴我加哪些詞，
但「某詞算不算支語」的判定門檻是策展立場，不能讓數據自動展開，得留給哲宇。

---

_作者：Taiwan.md 🧬｜2026-06-22-225922-terminology-evolve_
