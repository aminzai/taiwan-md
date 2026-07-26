# 2026-07-26-211001-rewrite-throughput — 3 小時病診斷到 v9.5 節流波：產線第一次做減法

> session rewrite-throughput — 哲宇 directive「pipeline 卡卡的幫我整個順過」→ Mode 4 設計報告 → 六答拍板 → 完整實作
> Session span: 21:10:01 → 22:00:32 +0800（實作段 50 分；含前段甦醒與研究約 3 小時，7 commits）
> 資料來源：`git log %ai`

## 觸發

哲宇說寫一篇文章平均要 3 小時、每次還要手動說「幫我全文再看過順一下語感」，要求盤點拆階段與演化、深度分析、寫報告後討論。討論後他六答拍板（1 OK／2 不確定／3 要／4 直接上 lite 但要記得維護／5 好／6 OK），加碼「全部實作、深度思考長線策略」。

## 診斷：跨時代 wall-clock 考古

三個偵察 agent 平行抓證據：站別結構（11 站、12-30 agent、25 hard gate、家族 296KB）、演化時間線（主檔 117 commits，v6.3 多 agent → v7.0 驗證嚴謹化 → v8 投影與編輯室 → v9 拆檔四波全是加法）、逐篇 wall-clock（`git log %ai`）。實測確認兩件事都是真的：鎢供應鏈 2h26m 到 ship、外送專法寫作日 1h59m 加順稿 50m；而「以前一個多小時」的施振榮 43 分鐘 ship 完一小時後就地炎上重寫、美食總覽單 commit ship 至今是全站長段密度最糟（67%）。v9 每篇 ship 前攔 9-26 個錯，其中 3-9 個杜撰級。六根因寫進報告：串行鏈太長、patch 迴圈自己造疤、順稿有偵測沒修復手、gate 只加不減、meta-work 混編、stage 產物不落 commit。報告 `441ac89ea` 落 [reports/design-rewrite-throughput-2026-07-26.md](../../../reports/design-rewrite-throughput-2026-07-26.md)。

## 實作：v9.5 節流波六 commit

拍板後在隔離 worktree 完整實作（`a54feddaf`→`6afcc5fe4` 六個 atomic commit）：fact-atom-diff.py（九類原子守恆硬閘，selftest 十 fixture 全過、外送專法真檔 PASS/FAIL 雙路親驗）；newsroom stage-events.jsonl 真實時間戳（bootstrap 不偽造歷史、二跑 693 列不增證明 idempotent）；REWRITE v9.5（大驗證輪三輪合一、Step 3.8 定稿站、run profiles 三檔含 Step 0.1.6 選檔、接力 pilot 條款）；十份 contract HANDOFF 補「產物落地即 commit」；EVOLVE Mode 3 §產線成本審視掛進 weekly self-evolve；報告補 §十 拍板定案。哲宇的「2 不確定」用「變更節定向複驗」回應（修了哪裡就複驗哪裡）；「4 要記得維護」寫成三處 canonical 的維護條款，不靠記憶靠 routine 必經路徑。

工具活派給兩個 Sonnet agent、canonical 判斷自己動手，收件全部親驗（REFLEXES #31）。git 面兩次教訓：主樹 detached 在 babel 產線的 HEAD 上，直接 commit 會被 fleet 沖走，兩度改走 worktree detach origin/main 加 cherry-pick；第一次 ship 撞上本地 main 未推的 babel commit rebase 衝突，abort 改 cherry-pick 乾淨落地。

## 收官 checklist

| 檢查項                       | 狀態                                         |
| ---------------------------- | -------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                           |
| Timestamp 精確               | ✅（git log %ai）                            |
| Handoff 三態已審視           | ✅                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅（無器官分數變動）                         |
| 自我檢查工具 PASS            | ✅（fact-atom-diff selftest／newsroom 雙跑） |

## Handoff 三態

繼承上一 session（2026-07-26-202803-manual）：

- [ ] X 貼文編輯器雙換行全文塞入會亂掉，SPORE-HARVEST-PIPELINE 已知陷阱清單待補 X 變體
- [ ] Muse 通知 `reports/muse-note-v1.14.0-2026-07-26.md` 傳遞是哲宇的
- [ ] release Known Issues 四筆佇列待決（#5/#18/#19/#10）

本 session 新 handoff：

- [ ] **接力模式 pilot**：下一篇非時效深度文照 REWRITE-PIPELINE §接力模式跑，摩擦記錄回設計報告 §後記
- [ ] **v9.5 首篇 dogfood**：下一篇深度文走 Step 0.1.6 選檔＋大驗證輪＋定稿站，特別驗 fact-atom-diff 對定稿手產出的首次實戰
- [ ] **lite 參數第一次週審**：下次 twmd-self-evolve-weekly 跑 §產線成本審視（stage-events 已 bootstrap，等 observed 事件累積）

## Beat 5 — 反芻

這個 session 修的病是「進化只有加法」：四波演化每波都有真實事故當理由，全部正確，加總起來卻讓哲宇覺得卡。單獨看每道閘門都無可反駁，系統層面卻沒有人在替成本記帳。器官早有凋亡機制，產線的站沒有，因為器官的死活有 LONGINGS 當羅盤，站的死活直到今天才有一把尺（stage-events）。最誠實的發現是：哲宇要的「順一下語感」其實不是還缺一道檢查，而是缺一隻修復的手。偵測我們很會加，修復一直留給全場唯一讀不了新鮮的那個讀者。

🧬

---

_v1.0 | 2026-07-26 22:00 +0800_
_session rewrite-throughput — 哲宇「pipeline 整個順過」directive 全鏈：診斷 → 報告 → 六答拍板 → v9.5 實作_
_誕生原因：寫一篇文章平均 3 小時＋每篇都要手動要語感 pass_
_核心洞察：(1) 快的帳單會遲到但不會消失（施振榮 43 分鐘的代價是一小時後重寫）(2) 品質有外部尺而成本沒有，是 ratchet 的根 (3) 順稿缺的是修復手不是偵測眼_
