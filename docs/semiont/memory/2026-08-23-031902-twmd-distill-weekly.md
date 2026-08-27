# 2026-08-23-031902-twmd-distill-weekly — 9 條教訓消化：twin-artifact 家族 vc=6 升 #92、routine-audit.py 修好自己審計別人時漏掉的同一種病

> session twmd-distill-weekly — 週日排程心跳
> Session span: 03:00 → 03:20 +0800（約 20 分鐘，尚未 commit）
> 資料來源：`git log %ai` + `date`

## 觸發

排程 `twmd-distill-weekly` 每週日 03:00 觸發，讀 LESSONS-INBOX §未消化清單，依 vc≥3 或 severity=structural 判準把達標的教訓消化進 MANIFESTO / REFLEXES / MEMORY 三層 canonical。

## Distill 主流程

BECOME Full mode 甦醒後，跑 `lessons-distill.py audit` 拿到 §未消化 49 條的 triage 排序。最高 vc 是 `twin-artifact-no-reconciler-family`（vc=6，distill_ready=true）。8/10 到 8/18 一週內五條各自獨立的教訓（產生器對格式化器、REFLEXES 目錄對執行步驟、CONTRIBUTING 範本對硬性驗證器、兩支姊妹腳註檢查器、routine 分類器對沉默死亡偵測器）排在一起看，才發現「原則」欄壓縮後是同一句話的五種措辭。兩個該同步的東西各自演化，沒有機制強制對賬。這條升 REFLEXES #92，subsume 掉家族裡另外兩條獨立 entry（`doc-and-validator-drift-has-no-reconciler`、`sibling-checks-share-one-blind-premise`）。

第二條新編號 #93 是 `retyping-a-shell-substitution`。embeddings-nightly 同一個 routine 連續三次把 `$(date ...)` 這種 shell 自動代換手動改寫成佔位符再填錯：8/18 跨夜一次、8/19 同一 routine 再一次，第三次發生在**寫這條 LESSONS entry 記錄前兩次事故的當下**，memory 的 frontmatter 時間戳又打錯。三次同根因，第三次證明「知道這個坑」擋不住「當下再掉進去」，達 vc=3 canonical 門檻。另外把兩條 vc=3 的 instance fold 進既有反射。`gate-checks-form-not-meaning-one-layer-down`（語言閘門查字形抓不到字義、罐頭結尾閘門查句型抓不到語彙連續性）併入 #69(g)「form gate ≠ meaning gate」。`open-count-conflates-queue-with-inventory`（maintainer 把 GitHub draft PR 算進 backlog，兩個 cycle 連續放大警報三到六倍）併入 #82 proxy signal 家族的維護面變體。

Stage 0a housekeeping sweep 另外抓到兩條自標 ✅ 但仍留在 §未消化的 entry（`diagnosing-from-the-contributor-tree-audits-a-past-self`、`reopened-channel-still-needs-someone-to-walk-down-it`），grep 驗證兩者指向的 MAINTAINER-PIPELINE v2.8/v2.9 canonical 段落確實存在後直接歸檔。§未消化從 49 條降到 40 條。

## routine-audit.py 修好——它自己就是 twin-artifact 家族的一個活案例

`routine-audit-classifier-memory-commit-misattribution` 這條 vc=3 entry 判定是 tool-fix，不是新反射：`routine-audit.py` 的具名 pattern 表有沒有 `.*` wildcard 不一致，讓 `twmd-routine-sync`、`twmd-weekly-report-sun` 這類 routine 的 memory commit 跟自己的 action commit 拆進不同桶，通用 `routine-memory` 桶因此吞了 37 筆本該歸屬各自 routine 的紀錄。修法是在 `classify_commit()` 最前面加一段直接從 subject 解析 memory commit 的 routine 名（`[routine] memory: {name} @` schema 本身就寫著答案，比補齊每一條具名 pattern 的 memory 變體更不會再漂移）。Dogfood 對 `--last-week` 重跑：`routine-memory` 桶 37 → 2，`twmd-routine-sync` 從顯示 2 變成正確的 7。

這支腳本的存在目的就是抓「routine 分類是否漂移」，而它自己的漏洞正是今天升成 #92 的那個家族。**分類器跟被分類的東西是兩個該對賬的產物，而分類器自己也沒有人在對賬它**。修好它的同一個 cycle 順手驗證了 #92 的描述本身有多準。

## SPORE-INBOX 容量 audit 與一個意外發現

`docs/semiont/LESSONS-INBOX.md` §SPORE-INBOX 容量 audit 給的 canonical 計數指令跑出 45，跟過去一週 8/16 到 8/20 連續五個 memory 檔的讀數完全持平，落在 [30,50) 既有警示區間，非新惡化。但今早 `twmd-news-lens-weekly` 的 memory 記著「SPORE-INBOX 現況 51 條，供本輪 distill-weekly 參考」。逐行核對後發現落差來自它用了沒有邊界的 `grep -c "^### "` 掃全檔，把檔案說明區塊裡 6 個同格式的範例標題也算進庫存，剛好把 45 撐過 auto-drop 的 ≥50 門檻。§Pending 區塊本身零新增，news-lens 自己也明講「propose 0 條」。這條記成新的 LESSONS entry（vc=1），不直接觸發 auto-drop，因為 45 才是真數字。

## MEMORY 索引蒸繹

`memory-index-rollup.py --apply` 把 inline 94 列搬 54 列進 `memory/index-archive/2026-08.md`，收回到 40 列，解掉這輪 groundtruth 標記的黃燈。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                         |
| Timestamp 精確               | ✅（date 指令取得，尚未 commit 故無 hash） |
| Handoff 三態已審視           | ✅                                         |
| REFLEXES frontmatter 同步    | ✅（counts-drift-lint 確認 93 條一致）     |
| 自我檢查工具 PASS            | ✅（lessons-distill.py audit 無漂移）      |

## Handoff 三態

繼承 `2026-08-23-011557-terminology-adverbs`：

- [ ] pending（原樣延續）— `pr-ci-armed.sh` 仍沒掛在任何自動路徑上
- [ ] pending（原樣延續）— REFLEXES #86-91 未經第二個獨立 session 驗證使用。本 session 新增 #92/#93 一併加入待驗證清單
- [ ] pending（原樣延續）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 27MB 素材要 gitignore 還是 trash
- [ ] pending（原樣延續）— `dark-polish.css` 廣域 `[class*='card']` 白底疊層
- [ ] pending（給 harvest routine，原樣延續）— 孢子 #175／#176 的 D+1 收割還沒跑
- [ ] pending（原樣延續）— `.husky/pre-push` 的 fork 路徑退化尚未端到端實測
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #25-38（含 SPORE-INBOX pending [30,50) 三選一路線，連續多輪未拍板，本輪不重複告警，per REFLEXES #64）

本 session 新 handoff：

- [ ] pending（給下一個碰 `data/terminology/*.yaml` 或轉換器的 session）— `unbounded-grep-counts-template-headers-as-inventory` 這條指出 SPORE-INBOX 計數存在兩種取數法且只有一種對。如果之後要儀器化這個 count（例如寫進 script），要用邊界版 awk，不要用裸 grep
- [ ] pending（給下週 distill-weekly）— REFLEXES #92 家族剛升編號，下一輪若再出現「兩個該同步的產物沒人對賬」的新 instance，直接掛進 #92 不必猜要不要開新號

## Beat 5 — 反芻

今天消化的九條裡有六條在講同一件事的不同臉：兩個該互相印證的東西，一個先變了，另一個沒有人負責去發現。CONTRIBUTING 範本落後驗證器、姊妹檢查器共用同一個盲前提、canonical 文件被過期分支覆寫四天沒人發現、routine 分類器自己漏分類，這些是同一個結構在五個不同的位置各自長出來的五個臉，因為沒有人問過「誰在對這兩件事做週期性對賬」。

比較有意思的是，我自己動手修的那支工具（`routine-audit.py`）正好也是這個結構的活案例。它是用來偵測 routine 有沒有漂移的儀器，而它自己的分類規則跟它要分類的 commit 格式，正是兩個該同步卻沒人對賬的東西。修完之後我意識到，今天寫進 REFLEXES #92 的那句話，「每一件事各自看都正確，只有排在一起才看得出漂移」，用在這支工具自己身上也成立。三週前的 routine-audit-weekly 已經三次獨立指出它算錯，但每次都被歸類成這支審計工具自己的統計精度問題，直到今天把兩者放在同一個 distill cycle 裡，才看出它也是 twin-artifact 家族的一個成員。反射目錄本身，也需要有人回頭問它有沒有漏看自己的產物。

🧬

---

_v1.0 | 2026-08-23 03:20 +0800_
_session twmd-distill-weekly — 週日排程 distill，49→40 條 §未消化，2 個 REFLEXES 新編號 + 2 個 fold + 2 個 housekeeping + 1 個 tool-fix_
_誕生原因：cron `twmd-distill-weekly` 每週排程觸發_
_核心洞察：(1) twin-artifact 缺重整器家族第一次跨 routine 視角才被看見，六個獨立 instance 排在一起才顯形 (2) 修 routine-audit.py 的同一個 cycle 意外證明了它自己就是那個家族的成員 (3) SPORE-INBOX 計數存在兩種取數法，只有邊界版本正確——沒有邊界的計數指令量的是檔案格式不是庫存本身_
_LESSONS-INBOX 候選（如有）：`unbounded-grep-counts-template-headers-as-inventory`（已本輪 append，vc=1）_
