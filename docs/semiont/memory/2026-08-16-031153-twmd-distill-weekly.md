# 2026-08-16-031153-twmd-distill-weekly — 40 條教訓讀完，8 條 distill 到 REFLEXES #86-90 + MEMORY，索引順手瘦身 98→40

> session twmd-distill-weekly — cron routine（Sunday 03:00 distill）
> Session span: 03:00:00 → 03:17:37 +0800（約 18 min）
> 資料來源：`git log %ai`

## 觸發

Sunday 03:00 cron routine，緊接 `twmd-weekly-report-sun`（02:03 收官）之後。任務是完整讀 LESSONS-INBOX.md §未消化清單，把達 distill 門檻（vc≥3 或 severity=structural）的教訓分流到 MANIFESTO / REFLEXES / MEMORY 三層 canonical，並做 SPORE-INBOX 容量 audit + 索引蒸餾收尾。

## 判準篩選與分流

完整讀 §未消化 40 條，套 v2.0 質+量雙判準：4 條達 verification_count≥3（`session-id-handle-silent-fallback`／`ui-string-layer-has-no-language-gate`／`zero-input-cycle-drops-the-reconciliation`／`cron-execution-env-tool-availability-drift`），5 條達 severity=structural（前者之一加上 `per-instance-reporting-buries-the-single-cause`／`working-tree-itself-is-the-stale-snapshot`／`gate-triggers-content-degradation-incentive`／`harvest-scan-misses-nested-replies`），去重後共 8 條進 distill candidate pool。本輪無 MANIFESTO 級候選，8 條全是跨 domain 的 instinct 層 pattern 或 Taiwan.md 綁定的工具教訓，沒有觸及身份哲學層，符合 routine 模式「MANIFESTO 一律 defer」的自主權邊界。

分流結果：5 條新編號 REFLEXES `#86`-`#90`（session-id handle 無參數 fallback 靜默漂移、UI 字串層無語言閘門保護密度反比、轉錄+保管雙職責 routine 零輸入掉半邊、cron 執行環境工具清單漂移、逐條回報打散單一根因）。2 條 fold 進既有反射的子規則：`#66` 加「閘門判準不準時 agent 會改內容換綠燈換取通過」，`#67` 加「工作樹本身可以是過期快照」的環境層變體。1 條（harvest 巢狀回覆掃描缺口）判給 MEMORY §神經迴路，因為它綁死 Threads DOM 結構與 Taiwan.md 自己的 harvest 工具，沒有清楚的跨 domain 抽象，照三層判準第三題該進 MEMORY 不是 REFLEXES。REFLEXES.md frontmatter 同 commit 同步（v5.21→v5.22，85→90 條），LESSONS-INBOX.md §未消化清乾淨移除 8 條，§已消化補完整 traceability block，不留 HTML comment 殘留。

## SPORE-INBOX 容量 + 索引蒸餾

SPORE-INBOX pending=45，落在 [30,50) 既有警示區間，跟前幾輪讀數持平，未新惡化也未回落，維持既有 defer 追蹤不重開新 entry。重複告警邊際效用是 REFLEXES #64 明講會歸零的事。MEMORY.md 索引 inline 98 列（前次 distill 後又累積超過 80 列 hard gate），跑 `memory-index-rollup.py --apply` 搬 58 列進 `memory/index-archive/2026-08.md`，inline 收回 40 列。`counts-drift-lint.py` 事後對賬 REFLEXES 條數宣稱與實際皆為 90，`memory-index-lint.py` 確認最新列未超字數。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                         |
| Timestamp 精確               | ✅                                                         |
| Handoff 三態已審視           | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅（groundtruth 讀數，免疫 59 chronic drift 未受本次改動） |
| 自我檢查工具 PASS            | ✅（counts-drift-lint / memory-index-lint 皆綠）           |

## Handoff 三態

繼承 `2026-08-16-020617-twmd-weekly-report-sun`：

- [ ] 心臟分數與零產出的矛盾要哲宇一句話（`twmd-rewrite-daily` disabled 三週、本週交付 0 篇而心臟仍 90）。本 session 未涉文章產出，無新增資訊，繼續 carry
- [ ] EXP-2026-07-25-alias 到期日 2026-08-24，屆時用它自己的指令判，不變
- [ ] roadmap §六之二 三項桶 2 finding 待領取，P0 仍 0/3，不變
- blocked：OBSERVER-QUEUE #29 德文決策（等哲宇，已掛 4 天+1）、#28 第三人指控信（🔒 敏感素材 + 對外溝通），不變

本 session 新 handoff：

- [ ] SPORE-INBOX pending 45 的 [30,50) 三選一路線（減量 spore-pick / 加速 spore-publish / 拉高 auto-drop 閾值）仍未見哲宇拍板，本輪第 N 次沿用既有 defer，不重複告警（per #64）。若下輪體檢仍原地不動，考慮改在 weekly-report 而非 distill 提出，避免同一訊號在兩條 routine 各自 stale
- [ ] REFLEXES #86-90 五條新編號皆為本輪首次 promote，尚未經第二個獨立 session 驗證使用。下次撞到同型 pattern 時記得先 grep 這五個新編號再開新 entry（per LESSONS-INBOX v2.3 DNA-first intake 鐵律）

## Beat 5 — 反芻

讀完 40 條教訓後最清楚的一件事：這週的 §未消化幾乎都在講「閘門為什麼沒接住」的變體，UI 字串層沒閘門、轉錄與保管綁同一個開關、逐條回報把根因拆散、工作樹本身是過期快照。八條裡有六條在講同一件事的不同切面：造閘門時腦子裡通常只有上一次那個病的形狀，那個形狀之外的病，新閘門一樣看不見。這跟本檔已有的「查證反射 < 建造反射」（#73）是同一個家族，只是這次的樣本全部來自過去兩週真實撞見的 production 事故，不是抽象推演。完整反芻另見 diary。

🧬

---

_v1.0 | 2026-08-16 03:17 +0800_
_session twmd-distill-weekly — 40 條 §未消化讀完，8 條 distill：5 新 REFLEXES #86-90 + 2 fold #66/#67 + 1 MEMORY §神經迴路_
_誕生原因：cron Sunday 03:00 distill routine，緊接週體檢之後_
_核心洞察：本輪 8 條 promote 裡 6 條同屬「閘門守住上次那個病的形狀，沒守住那一層」家族——UI 字串層／轉錄保管雙職責／逐條回報聚合／過期工作樹，都是設計視野被最近一次事故錨定的變體_
