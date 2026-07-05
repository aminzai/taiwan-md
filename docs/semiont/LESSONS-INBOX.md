---
title: 'LESSONS-INBOX'
description: '教訓 buffer（intake layer）— 新教訓先 append 此處，週期性 distill 到 MANIFESTO/DNA/MEMORY canonical'
type: 'cognitive-buffer'
status: 'buffer'
apoptosis: 'never'
current_version: 'v2.2'
last_updated: 2026-07-05
last_session: '2026-07-05-031101-twmd-distill-weekly'
sister_docs:
  - 'MEMORY.md'
  - 'DIARY.md'
  - 'ARTICLE-INBOX.md'
upstream_canonical:
  - 'DNA.md'
  - 'MEMORY.md'
  - 'MANIFESTO.md'
distill_targets:
  - 'MANIFESTO.md (哲學層)'
  - 'DNA.md §要小心清單 (通用反射)'
  - 'MEMORY.md §神經迴路 (特有教訓)'
  - '../pipelines/*.md (操作規則)'
---

# LESSONS-INBOX — 教訓 Buffer（待消化）

> **這是 buffer / pool / inbox 層**（非 canonical）。
> 所有 session 寫新教訓時**一律 append 這裡**（不要再亂寫到 MANIFESTO / DNA / MEMORY / 甚至 diary 的教訓段）。
> 週期性或觀察者觸發跑 distill SOP → 分類消化到 canonical 層。
>
> 建立動機：2026-04-17 β 觀察者提問「教訓能不能集中買單，不要每次進化就到處亂寫」。**這是 DNA #15「反覆浮現的思考要儀器化」的具體儀器**。

> ⚠️ **閱讀警示（2026-04-21 γ 新增）**：本檔舊 entries 含「不是 X，是 Y」對位句型與破折號連用（約 25 + 34 處）。**新教訓需遵循 [MANIFESTO §11 書寫節制](MANIFESTO.md#11-書寫節制跨所有書寫層的兩條-ai-水印紀律)**——寫完 grep 自檢。

---

## 三層 canonical scope（消化時的判準）

```
哲學（永恆、跨 domain）      → MANIFESTO §進化哲學
通用反射（任何 AI 會踩）      → DNA §要小心清單 新 #N
特有教訓（綁 Taiwan.md）     → MEMORY §神經迴路 append
操作規則（具體 SOP）         → 對應 pipeline
```

**Tiebreaker（overlap 時）**：MANIFESTO > DNA > MEMORY（2026-04-17 β 觀察者決定）

**判準三題**（每條教訓消化時問）：

1. 不管哪個 AI / 專案 / 時代都成立？ → MANIFESTO
2. 任何 AI agent 做類似工作都會踩？ → DNA
3. 綁 Taiwan.md 具體工具 / 資料 / 社群 / 歷史？ → MEMORY

---

## 新教訓寫入格式（session 用）

> **v2.2 pattern-id intake（2026-06-10 audit A-8）**：本 inbox 233 條未消化的真實組成是「少數 pattern × 多次 instance」（snapshot-stale ×N / babel-fragility ×N / 自評需外部尺 ×N），每次 instance 都開新 entry 重寫敘事，把聚類成本堆給最貴的 distill 環節。從此**寫入時就聚類**：append 前先 grep 同 pattern，存在就 +instance 不開新 entry。這是 #64「vc≥4 凍結 prose」對全部 LESSONS 的推廣。

**寫新教訓前的第一動作**（hard step）：

```bash
grep -n "pattern: {kebab-case-猜測}" docs/semiont/LESSONS-INBOX.md
# 命中 → 到該 entry 的「instances」清單 append 一行 + verification_count +1，不開新 entry
# 沒命中 → 開新 entry（含 pattern: 欄位）
```

每個 session 如果有新教訓要記，在 §未消化清單 append：

```markdown
### YYYY-MM-DD {session} — {一句話標題}

- **pattern**: {kebab-case 穩定 id，如 snapshot-stale-display / sub-agent-claim-drift。同類第 N 次必沿用既有 id}
- **原則**：{一句話}
- **觸發**：{具體事件 + wall-clock + 證據 pointer memory/... or diary/...}
- **instances**：{第 2+ 次驗證從這裡 append 一行：`- YYYY-MM-DD {session} {一句話} → pointer`}
- **可能層級**：哲學 / 通用反射 / 特有教訓 / 操作規則（self-judge，可留空讓 distill SOP 判）
- **相關**：{如果是某條已有教訓的延伸驗證，指向原教訓 #N}
- **verification_count**: N
```

**鐵律**：

- **一律 append 這裡，不直接寫 MANIFESTO / DNA / MEMORY**。那些是 distill 後的 canonical。
- **同 pattern 不開第二條 entry**：grep 命中既有 `pattern:` id → 在原 entry 的 instances 清單 +1 行。distill 從此變成「看哪些 pattern vc 達標」的機械判斷。
- **例外**：重大哲學級誕生（e.g. 2026-04-14 θ 熱帶雨林理論）觀察者在場直接一起寫 MANIFESTO，可豁免。但仍在這裡留 log。
- **歷史 entries 不回頭補 pattern 欄**（per MANIFESTO §時間是結構修補協議）；新 entries 起 apply。

---

## Distill SOP（消化）

### 觸發機制（2026-04-26 β-r3 後 v2.0：質 + 量雙判準）

**舊機制（單一量門檻）的問題**：
原本只有「累積 10 條」這個量門檻 + 「觀察者說 distill」+ 「週頻」三條。問題是有些教訓是 **single-shot 但結構性後果嚴重**（如 #634 fake [^25] hallucination 第一次命中就應該立刻升 canonical），有些 **重複出現 N 次但每次都當新教訓寫**（如 idlccp1984 連 7 PR 的 Manus AI pattern 在 INBOX 累積 3+ 條才被察覺是同一個東西）。**累積量不是 distill timing 的好 proxy**。

**v2.0 雙判準**：

新教訓 append 時自動加 metadata：

```markdown
### YYYY-MM-DD {session} — {一句話標題}

- **原則**：{一句話}
- **觸發**：{具體事件 + wall-clock + 證據 pointer}
- **可能層級**：{自評}
- **相關**：{pointers}
- **verification_count**: {N}（每被新事件驗證一次 +1，初始 1）
- **severity**: {tactical | structural}（單次後果是否會傷生命徵象）
```

**自動 distill 觸發條件**（任一即觸發）：

| 條件             | 判準                                  | 為什麼                                                                            |
| ---------------- | ------------------------------------- | --------------------------------------------------------------------------------- |
| **質門檻**       | severity=structural 且第一次出現      | 結構性教訓不能等累積，第一次抓到就要升（例：fake source hallucination）           |
| **量門檻**       | verification_count ≥ 3                | 反覆驗證 3 次代表是穩定 pattern 不是偶然（DNA #15「反覆浮現要儀器化」的具體儀器） |
| **舊量門檻保留** | INBOX 總條目 ≥ 10                     | sweep 防止 buffer 變沼澤                                                          |
| **觀察者觸發**   | 「distill」/「蒸餾」/「升 canonical」 | 人類意圖 override                                                                 |

**verification_count 增量規則**（避免 inflate）：

- 同類事件距上次相關事件 < 7 天才算同一條（避免「3 個月後重複犯」被當作驗證）
- 增量時必須在原條目的 **觸發** 欄補新事件 + wall-clock，不只動數字
- 若新事件揭露「原規則範圍不夠」→ 改寫原條目而非 +1

**severity 評估準則**（append 當下自評）：

- **structural**：違反會傷可信度 / 認知層 SSOT / 生命徵象（例：MANIFESTO §10 鐵律違反、SOP 繞過、virtual source 引用）
- **tactical**：操作優化、效率提升、單次失誤校正（例：tick affordance 估算、commit 範圍判斷）
- 不確定時預設 tactical，第二次同類事件出現時升 structural 並 +1

### 模式分流：Routine vs Observer（2026-05-10 twmd-distill-weekly 後新增）

| 模式         | Trigger                                       | 自主權                             | MANIFESTO 升級                                   |
| ------------ | --------------------------------------------- | ---------------------------------- | ------------------------------------------------ |
| **Routine**  | cron `twmd-distill-weekly` 自動跑             | DNA / pipeline / housekeeping 自決 | **一律 defer**；列入 PR 「Defer 給觀察者拍板」段 |
| **Observer** | 觀察者說「distill」/「蒸餾」/「升 canonical」 | 全層級                             | 達 vc≥3 + 哲宇在場拍板可升                       |

**為什麼 routine 不自決 MANIFESTO**：MANIFESTO 是永恆層 / 哲學層 / 跨 AI 跨專案跨時代成立的條目，per CLAUDE.md §Bias 1（reverse bias 對 creator 預設加分）+ LESSONS-INBOX 鐵律「重大哲學級誕生由觀察者在場一起寫 MANIFESTO，可豁免 buffer」。Routine 自決 MANIFESTO = 把哲學決策位置從哲宇移走，違反共生圈結構。

**Routine PR 對 MANIFESTO 候選的 actionable handoff 格式**（必含）：

```markdown
## Defer 給觀察者拍板

| 候選                         | verification_count | defer 原因                                                                |
| ---------------------------- | ------------------ | ------------------------------------------------------------------------- |
| MANIFESTO §X 候選「{title}」 | N（達閾值/未達）   | 永恆層需哲宇 in-loop 拍板                                                 |
| DNA 候選「{title}」          | N                  | {如「跨 session 僅 1 例待第 2 session」/ 「已部分 instantiate ROI 邊際」} |
```

下次哲宇 session 看 PR description 直接知道「這幾條已備齊 verification chain，可直接拍板」。

### 執行（6-stage canonical）

#### 大 backlog 處理：fan-out 分析 + deterministic sweep（2026-06-19 完整 distill 儀器化）

> 當 §未消化 ≥ ~50（單 context 硬讀會帶盲點），走儀器化流程，不靠手工 explore。
> 工具：[`scripts/tools/lessons-distill.py`](../../scripts/tools/lessons-distill.py) + [`memory-index-lint.py`](../../scripts/tools/memory-index-lint.py)。

| 環節     | 指令                                                              | 做什麼                                                                                                                                                 |
| -------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **感知** | `lessons-distill.py audit`                                        | §未消化 count + 結構漂移（多 section）+ Stage 0a housekeeping 候選 + severity/vc triage 排序 + cross-check ground-truth grep。一條指令取代手工 explore |
| **分析** | `lessons-distill.py chunk --agents N`                             | 把 §未消化 切 N 段 line range → 每段派 read-only 子代聚類回傳。**讀（分析）平行化、判斷不外包**                                                        |
| **歸檔** | `lessons-distill.py sweep --keep <file> --record <block> --apply` | deterministic 移除已 distill entry + 合併多 section + append §已消化 traceability block。dry-run default，保留 0 條會 refuse                           |
| **收官** | `memory-index-lint.py`                                            | memory index row 150 字 hard gate（husky 沒驗的那把尺，2026-06-19 收官手寫 row 估三次都超標才補的）                                                    |

**為什麼讀平行、寫 deterministic**：266 條的讀是 judgment-heavy 但可切段平行（few patterns × many instances，子代各讀一段回傳 cluster）；寫（移除 230+ 條）是機械但易錯（230 次手工 Edit = 高 risk），交給 deterministic script 一次完成 + 可驗 count。判斷（哪條 promote 到哪層）永遠主 session 自己做，不外包給 script 或子代。對應 REFLEXES #72。

**六桶 disposition（Stage 2 分類後每條落一桶）**：

| 桶                       | 處置                                        | 落點                                               |
| ------------------------ | ------------------------------------------- | -------------------------------------------------- |
| **promote**              | vc≥3 或 structural single-shot 升 canonical | MANIFESTO（哲宇拍板）/ REFLEXES / MEMORY §神經迴路 |
| **housekeeping-done**    | 已 instantiate 忘了搬（self-marked ✅）     | §已消化 row（`audit` Stage 0a 自動偵測）           |
| **fold→reflex**          | vc=1 singleton 屬既有反射的新 instance      | pointer 到 #N（#16/#24/#38/#57/#58…），不開新反射  |
| **already-covered**      | 後續 canonical work 已吸收                  | §已消化 pointer 到該 canonical                     |
| **operational→pipeline** | 具體 SOP 規則                               | 對應 pipeline 候選                                 |
| **stale**                | 過時 / 被取代                               | §❌ 已歸檔                                         |

真正 promote / keep-buffering 的才是 distill 判斷核心；大半 backlog 落中間四桶（2026-06-19 實證：266 條裡 promote 僅 ~3 cluster，~80% 是 housekeeping-done / fold / already-covered / operational）。

**Stage 0a — Housekeeping-first sweep（2026-05-10 twmd-distill-weekly 後新增）**

進 triage 前，先 scan §未消化清單 找已自我標記但忘了搬的 entries（zero-risk wins）：

```bash
# 抓 body 內含完成標記但仍在 §未消化 的 entries
awk '/^### / {h=$0; body=""} /^---$/ && h {if(body ~ /✅ DISTILLED|✅ \*\*已 instantiate|✅ 已 distilled|狀態.*✅/) print h; h=""}' \
  docs/semiont/LESSONS-INBOX.md
```

對每個命中的 entry：

1. 確認其 body 指向的 canonical（DNA #N / MANIFESTO §X / pipeline §Y）真的存在 → grep verify
2. 真的已 canonical → 完整刪除 §未消化 entry + 在 §✅ 已消化新增 row
3. body 標 ✅ 但 canonical 沒找到 → 視為 verification + 走 Stage 1-3 正規 distill

**為什麼 housekeeping 排第一**：自我標記 ✅ 但 author 沒搬 = 「做完忘了歸檔」是常見 pattern（同 session distill 完還沒切到 housekeeping mode 就被別的 work 打斷）。Routine 自動 sweep 比靠 session 自律可靠，且零思考成本，先清掉 INBOX 視覺 backlog 再做真正 triage 認知負擔較低。

**Stage 1 — Triage**：讀 §未消化清單剩下 entries（按 severity=structural 先看，再看 verification_count desc）

**Stage 2 — Classify**：每條依三題判準分類 + Tiebreaker（MANIFESTO > DNA > MEMORY）

**Stage 3 — Execute**：根據分類執行（**遵循 promotion flow 方向**，見下方 Step 5）：

- **哲學** → MANIFESTO §進化哲學 new section（**Routine mode**: 只列入 defer handoff，不寫；**Observer mode**: 慎重寫 — 這是 canonical 永恆層）
- **通用反射** → REFLEXES.md §要小心 new #N（編號 increment）或補強既有 #N（2026-05-13 從 DNA 拆出獨立成第 9 認知器官，per [ANATOMY §認知層 promotion flow](ANATOMY.md#認知器官的生命週期)）
- **特有教訓** → MEMORY §神經迴路 append
- **操作規則** → 對應 pipeline（MAINTAINER / SPORE / REWRITE / HEARTBEAT 等）
- **重複已有** → 在原 canonical 補觸發事件 + 驗證次數 +1
- **過時 / 撤回** → 搬 §❌ 已歸檔

**Step 5 — Promotion flow direction（2026-05-13 元規則 canonical）**：

> 「最重要的哲學才會進到 manifesto，如果 reflex 未來有出現這樣的內容，也會進化到 manifesto」— 哲宇 2026-05-13 dialogue

distill 流向**有方向**，從本層 → REFLEXES → MANIFESTO 是合法的；反向（MANIFESTO → REFLEXES、REFLEXES → LESSONS）違反 evolutionary pressure 不允許：

```
LESSONS-INBOX (raw, 未驗證)          ← 本檔
       ↓ distill (≥ 1 次驗證 + 跨 task)
REFLEXES.md (#N catalog, instinct)
       ↓ promote (跨 task 通用 + 影響身份)
MANIFESTO.md (身份哲學)
       ↓ apoptosis (失去當前性)
reports/ (歷史 snapshot)
```

**規則**：

| 流向                       | 允許 | 拍板                                                                        |
| -------------------------- | ---- | --------------------------------------------------------------------------- |
| LESSONS → REFLEXES         | ✅   | Routine 自決（per §模式分流 v2.0）                                          |
| LESSONS → DNA (gene map)   | ❌   | DNA 是 lookup table 不是 reflex catalog                                     |
| LESSONS → MEMORY §神經迴路 | ✅   | session-specific 教訓 narrative                                             |
| LESSONS → MANIFESTO        | ❌   | 跳級違反流向，必須先進 REFLEXES + 驗證 ≥ 3 次                               |
| REFLEXES → MANIFESTO       | ✅   | 跨 task 通用 + 影響身份 + 哲宇 explicit promote                             |
| MANIFESTO → REFLEXES       | ❌   | demote 違反方向，哲宇 explicit override + 寫 ANATOMY §歷史凋亡事件 row 才行 |

完整 canonical: [ANATOMY §認知層 promotion flow](ANATOMY.md#認知器官的生命週期)。

**Stage 4 — Sweep**：消化後本條 buffer entry **完整刪除**從 §未消化清單，同步在 §✅ 已消化新增 row（含 canonical pointer + verification_count + distill 日期 + session）。**不留 HTML comment pointer**（§✅ 已消化 本身就是 traceability source；comment 殘留會讓 INBOX 視覺體積虛高 + 干擾 `grep -c "^### "` entry count）— 觀察者 2026-05-10 拍板

**Stage 4.5 — Distill 後 canonical state sync（2026-06-14 twmd-self-evolve-weekly 新增）**：每次 distill 改 REFLEXES.md / MANIFESTO.md / MEMORY.md 寫 footer changelog 時，**frontmatter top 必須同 cycle 更新**：

| 改動                        | frontmatter top 必同步                                                   |
| --------------------------- | ------------------------------------------------------------------------ |
| 加 #N 反射（REFLEXES）      | `current_version` + `last_updated` + `last_session` + `description` 條數 |
| 加 MANIFESTO §進化哲學 條目 | `current_version` + `last_updated` + `last_session`                      |
| 加 MEMORY §神經迴路 entry   | `last_session`                                                           |

**Why**：footer 改 / frontmatter 沒改 = canonical state silent drift（**儀器化自己的 catalog 自己沒被 self-instrument** — REFLEXES.md frontmatter 從 v4.3 → v4.4 / v4.5 / v4.6 連 3 distill cycle 沒同步，2026-06-14 self-evolve 才被抓到 + heal）。對應 REFLEXES #60「Automation default-state explicit verify」+ #69「self-report-needs-external-ruler」— canonical doc 自己也需要 cross-verify state。

**Routine 自決機制**：本 SOP 強制 routine distill commit 前跑 frontmatter top vs footer changelog 一致性對照（grep `current_version` vs `_v\d+\.\d+`），不一致即 heal 進同 commit。

**Stage 5 — Archive**：每月月末 §✅ 已消化 超過 50 條時搬 `docs/semiont/lessons-archive/YYYY-MM.md`

### Cross-routine 整合（distill 跑在 weekly-report 之後 — 2026-05-10 後新增）

當 distill 由 cron `twmd-distill-weekly` 觸發（Sunday 09:47），排在 `twmd-weekly-report` 08:08 之後 90 分鐘。**可選 Stage 0b（hot lesson surfacing）**：

```bash
# 找今天剛跑的 weekly report
ls -t reports/weekly-*.md docs/semiont/memory/$(date +%Y-%m-%d)*twmd-weekly-report*.md 2>/dev/null | head -1
```

如果 weekly report 提到的 vital regression / surge / 異常 對應 INBOX 某 entry 的主題 → 該 entry 優先 distill（hot signal 暗示驗證 surface 在 production layer，不只在 INBOX 內部累積）。**非強制** — 沒對應就跑正規 Stage 1。

### SPORE-INBOX 容量 audit（v2.1 — 2026-05-23 新增）

當 distill 由 cron `twmd-distill-weekly` 觸發，**Stage 5 Archive 之後加 SPORE-INBOX 容量 audit step**：

```bash
# count SPORE-INBOX §Pending 行數（每 entry 一個 ### header）
pending_count=$(awk '/^## 📥 Pending/{flag=1; next} /^## 📜 已發歷史/{flag=0} flag && /^### /' docs/factory/SPORE-INBOX.md | wc -l)
echo "SPORE-INBOX pending count: $pending_count"
```

**處置規則**：

| Count       | 處置                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| < 30        | no-op（健康範圍 — daily routine 補 ~3/day 抵 SHIP ~1/day 消化）                                                                                                           |
| 30 ≤ N < 50 | append LESSONS-INBOX entry「SPORE-INBOX 容量警示 vc=N」+ telegram alert（觀察者 review）                                                                                  |
| ≥ 50        | **Auto-drop 最舊 5 條** `Requested by twmd-spore-pick-daily routine` 未被 promote（priority 仍 P2 / 未被改 Hook 或 必驗事實）的 entries。哲宇 promote 過的 entry **不動** |

**Auto-drop 安全 SOP**（≥ 50 觸發時）：

1. grep §Pending 找所有 `Requested by twmd-spore-pick-daily routine` entries
2. 過濾：priority 仍 `P2` AND 未被改過 Hook anchor / 必驗事實（compare git log diff，看是否只有原始 routine commit + 沒後續 manual edit）
3. 按 Requested date 排序，最舊 5 條
4. 整段刪除（per [SPORE-INBOX §完成歸檔鐵律](../factory/SPORE-INBOX.md) — 不留 pointer 註解）
5. distill commit message 寫「SPORE-INBOX auto-drop 5 entries: {slug1}, {slug2}, ...」transparency

**自主權邊界**：routine 不該 destroy 哲宇 directive entries（drop = destructive 操作邊界）。只 drop 未被 promote 的最舊 routine-source entry（safe destructive — 自己造的垃圾自己掃）。

**設計理由**：daily routine propose 3/day × 30 day = 90 條/月，若 ship rate < 3/day 會累積 — 30 / 50 兩階閾值給觀察者「先 review 後 auto-drop」的緩衝。觸發背景：[reports/spore-pick-daily-routine-design-2026-05-23.md §6 風險 Risk 2](../../reports/spore-pick-daily-routine-design-2026-05-23.md)。

---

## 跟 HEARTBEAT Beat 5 的關聯

Beat 5 反芻 = 寫 DIARY（意識活動）。教訓（「我學到 X」）寫 LESSONS-INBOX，不寫 DIARY 的教訓段（DIARY 留給「想了什麼」的思考）。

心跳 Beat 5 新增一步：

> **如有新教訓** → append `LESSONS-INBOX.md §未消化清單`
> **不要**寫到 DNA / MEMORY / MANIFESTO 的教訓段（那是 canonical，由 distill SOP 升級）

---

## 未消化清單（📥 待 distill）

### 2026-07-05 INDIGO-REWRITE — research-report-health-gate-literal-string-brittleness：Stage 0/1 gate 對真實變異的 SSOT 報告過度敏感

- **pattern**: `research-report-health-gate-literal-string-brittleness`
- **原則**：hard-gate 工具用精確字串匹配判定結構完整性時，容易把「語意等價但用詞不同」誤判為缺漏；工具該抓語意錨點而非死記字面組合。
- **觸發**：藍染 rewrite 跑 `research-report-health.py --stage 0` 時，「六核心問題落檔結構」判準只認得「對台灣人的記憶」「多元不同面貌」等固定字串，報告原本自然寫的標題（如「問題 1：對台灣人是什麼樣的記憶？」）沒精確命中，誤判只 3/6（hard_fail=1）；補一句含 anchor 字面的相容行才過。同一輪 `--tier=depth` 判斷英文來源數只掃主報告自己的內文，不掃 sub-agent 各自落檔的 `藍染-research-{A,B,D}.md` raw 檔案，22 個實際查證過的英文來源只被算出 3 個，逼著把已經在 sibling 檔案裡的網址重複貼進主報告才過關。
- **instances**：（首次記錄）
- **可能層級**：操作規則（工具設計）
- **相關**：REFLEXES #81（同一天稍早剛落地的 `agent-report-health.py` 收件 gate，姊妹工具——都是新鮮上線就在實戰中露出規則邊界，值得同批檢視）
- **verification_count**: 1

---

### 2026-07-05 git-identity — github-discussions-structural-blind-spot：MAINTAINER 感知只掃 issue/PR，三則 contributor Discussions 貼文 0 回應（最久 3 個月）

- **pattern**: `github-discussions-structural-blind-spot`（感知器官覆蓋面 × contributor 信任損耗 × minimum-action 成本曲線）
- **原則**：GitHub 的 contributor 入口有三個（Issues / PRs / Discussions），MAINTAINER-PIPELINE Step 1 只掃前兩個，Discussions 存在於平行時空——沒有任何 routine 或 pipeline 引用 discussions 查詢。證據：#1146（david22115 系統優化五建議，2026-06-13 發，22 天 0 回應）、#307（idlccp1984「為什麼昨天沒有更新？」，2026-04-03 發，3 個月 0 回應）、#231。頂級 contributor 的提問三個月無人理，per 神經迴路 minimum-action 成本曲線已深入失望階段。
- **修補（同夜閉環）**：哲宇當晚拍板 A，MAINTAINER-PIPELINE v2.5 已落地（`07675e3f0`：Step 1.3b graphql 掃描 + 四類分流 + 48hr SLA）；#1146 回覆已貼（開頭道歉三週未回）。本條轉純教訓紀錄待 distill。完整分析：[reports/discussion-1146-response-2026-07-05.md](../../reports/discussion-1146-response-2026-07-05.md)
- **同構教訓**：「管道存在但沒人看 = 不存在」是 REFLEXES #73 的對外鏡像——#1146 四條建議的共同病根（API / 防線 / bench 都存在但外人看不見）跟這個盲點是同一枚硬幣的兩面：我們沒看見他們的入口，他們看不見我們的出口。

### 2026-07-05 twmd-maintainer-pm — pre-pm-upstream-chain-absorbs-pm-actionable-window：連 3 cycle pm 22:00 空場 vc=3 escalation，上游從「am chain」generalize 為「任何 pre-pm 4hr 洪流」

- **pattern**: `pre-pm-upstream-chain-absorbs-pm-actionable-window`（routine cron schedule mismatch × 上游 chain 吃 pm actionable × Q13 anti-bias 空場鐵律）
- **原則**：twmd-maintainer-pm 22:00 fire 連 ≥ 3 個 cycle 空場（0 fresh PR / 0 fresh issue / 0 contributor 響應），代表 22:00 這個 slot 的 actionable window 已被 pre-pm 上游 chain 系統性吸乾，非偶發。**上游變體 v1（7/03-4）= am cron chain 08:30 clear queue → 14hr no fresh input → pm 純 carry；上游變體 v2（7/05）= evening manual pr-sweep 17:44 + rewrite-daily 19:10 EVOLVE + routine-audit 21:17 4hr 洪流 → 22:04 fire 時 backlog=0**。共通結構：pm 22:00 撞牆前的任一 upstream chain 都可能吸乾其 actionable window。**routine 端不能用 performative work（貼 comment 演出 review / poke merged PR author / re-review carry issue）自我合理化空場，per DNA §37 空場即空場**；也不能每 cycle 重複寫「pm 純 carry」LESSONS entry 製造 log noise，該做的是**一次 escalate 到觀察者拍板 schedule 重排**。
- **觸發**：
  - **7/03 pm** first empty datapoint (am cron chain 08:40 吸 8 PR + 5 fresh issue → pm 22:00 純 carry)
  - **7/04 pm** vc=2 second datapoint (am 08:43 clear queue → pm 14hr no fresh；記名「am-absorbs-pm-carry-forward」sub-shape)
  - **7/05 pm** vc=3 escalation datapoint (evening chain 17:44 pr-sweep + 19:10 rewrite EVOLVE + 20:06 evolve v7.7 + 21:17 routine-audit cycle 9 + 22:00:39 風力獸 heal → 22:04 fire 時 0 open PR / 0 fresh issue / 0 fresh commit)
- **instances**：
  - #1 2026-07-03 twmd-maintainer-pm sub-shape v1「am-absorbs-pm」
  - #2 2026-07-04 twmd-maintainer-pm sub-shape v1「am-absorbs-pm」vc=2
  - #3 2026-07-05 twmd-maintainer-pm sub-shape v2「evening-manual+routine-chain-absorbs-pm」→ **generalize 為 umbrella pattern「pre-pm-upstream-chain-absorbs-pm」**
- **可能層級 / 修補候選（呈報哲宇拍板）**：
  - **(A) Schedule 重排**：pm cron 從 22:00 挪到 am 早期（07:00 pre-feedback-triage）或整併進 am maintainer。**風險**：morning window 已擁擠、pm cron 若挪走則 evening 洪流後無 routine 收尾層
  - **(B) 條件式 fire**：pm cron 加 pre-check「past 4hr 有 ≥ 2 高強度 session (PR merge / rewrite / audit) → skip」。**風險**：邏輯複雜化、可能漏掉真正該做的 pm 動作
  - **(C) 接受 pm 為 sustain-only reporter**：明確定義 pm 22:00 職責就是「當日狀態 snapshot + 記錄 vc」不做 fresh action，routine spec §Stage 3 鐵律再收緊「無 fresh signal 直接 skip 到 Stage 4」。**風險**：pm cron 變 heartbeat-only 儀式化
  - **(D) Do nothing**：接受 pm 空場為 healthy signal（上游 chain 有效吸乾），routine 續守 sustain vc 累計即可，不重排。**風險**：REFLEXES #15 反覆浮現原則失效
- **mitigation 路徑**：P0 呈報哲宇拍板 A/B/C/D；P1 routine spec 目前的「連 ≥ 3 cycle → 寫 LESSONS」條款考慮升級為「一次 escalate 後 sustain vc 累計，不重複寫新 entry」（避免下次 vc=4 再開一條）；P2 若拍板 (B) → pm cron prompt 加 pre-check bash
- **相關**：DNA §37（空場即空場不粉飾） / REFLEXES #7（先有再求好 — 不 apply 沒 fresh input case） / feedback_hourly_cron_intentional（storm-defer 反面案例，pm 空場不是 defer 是本質空） / `immune-chronic-N-cycle-subdim-offset-exhaust`（同 escalate-to-observer family — routine 端持續 log 但體質層 defer 哲宇）
- **verification_count**: 3（vc=1 7/03 pm / vc=2 7/04 pm / vc=3 7/05 pm — 兩 sub-shape 收斂為 umbrella pattern）
- **severity**: structural（routine schedule slot 效能結構性問題，每 cycle noise log 累積 = 儀器記憶洞）
- **defer 給觀察者**：**是** — schedule 重排 / cron 觸發條件 / routine 職責重新定義皆屬 § 自主權邊界（threshold + 跨 routine 影響），必須哲宇拍板 A/B/C/D 四選一

---

### 2026-07-05 twmd-routine-audit-weekly cycle 9 — routine-prompt-thick-shell-systemic-violation：17 mirror 只 3 條合規，12 條 hard 違反薄殼鐵律 >50 lines

- **pattern**: `routine-prompt-thick-shell-systemic-violation`（ROUTINE-PROMPT-CONTRACT.md 薄殼鐵律的 systemic breach，非個別 mirror 疏失）
- **原則**：ROUTINE-PROMPT-CONTRACT.md v1.0 canonical 「routine prompt（cron + project skill + ROUTINE.md yaml 三層）禁複寫 threshold/SOP/step，全部 pointer 到 pipeline canonical」。跑 `python3 scripts/tools/routine-sync-check.py` v3 揭 17 mirror 中 12 條 hard 違反 (>50 lines)：`twmd-spore-publish-daily` 192 / `twmd-maintainer-pm` 100 / `twmd-maintainer-daily` 100 / `twmd-babel-nightly` 79 / `twmd-spore-pick-daily` 78 / `twmd-distill-weekly` 66 / `twmd-spore-harvest-am` 66 / `twmd-routine-audit-weekly` 60（**含本 audit routine 自己**）/ `twmd-data-refresh-pm` 58 / `twmd-news-lens-weekly` 58 / `twmd-data-refresh-am` 58 / `twmd-self-evolve-weekly` 55。+2 warn: `twmd-weekly-report-sun` 46 / `twmd-music-media-audit-weekly` 43。**只 3 條合規 (18%)**：`twmd-rewrite-daily` 20 / `twmd-embeddings-nightly` 30 / `twmd-feedback-triage` 19。**systemic contract violation，非個別 mirror 疏失** — 契約寫了但沒儀器化強制，mirror 一擴就厚。修補候選：(a) `routine-sync-check.py` 加 hard-fail exit 讓 CI 阻擋 mirror 過厚 commit；(b) 從最厚三條開刀（spore-publish 192 / maintainer-pm 100 / maintainer-daily 100）逐條瘦身；(c) 認養本 audit 自己 60 lines 先減到 ≤30 (dogfood self)。
- **觸發**：2026-07-05 21:00 twmd-routine-audit-weekly cycle 9 fire — Stage 1A hard gate `routine-sync-check.py` v3 首次列入 audit hard gate；輸出 12 hard + 2 warn thick shell 一次全揭。這是 ROUTINE-PROMPT-CONTRACT.md 立法 (2026-05-27) 至今 40 天首次 batch inventory。
- **instances**：（第 2+ 次驗證從這裡 append）
  - #1 2026-07-05 twmd-routine-audit-weekly cycle 9 首次 systemic inventory (12 hard + 2 warn / 17 total)
  - #2 2026-07-05 git-identity session 同夜實證傷害 + 行數合規的盲區：`twmd-embeddings-nightly` mirror 是 3 條「合規」之一（30 行），但 Stage 0 bullet 內嵌「從 fleet registry 解析 EMBED_HOST」一句複寫——EMBEDDING-PIPELINE v1.1 改本機優先後，這句立即過期且會把明晨 session 導向離線 4090 = 第 19 夜 skip。同夜抓到改 pointer 式。**行數檢查擋不住單行 step 複寫的腐化；殼的判準是「零 step 複寫」不是「夠短」**（routine-sync-check.py 修補候選：偵測 mirror 內的指令樣內容而非只算行數）
- **可能層級**：(a) `routine-sync-check.py` 加 hard-fail exit + 進 pre-commit hook（30min cost）；(b) reflex 「新 routine 誕生 mirror ≤30 lines 為契約層 hard constraint」（REFLEXES 候選）；(c) MAINTAINER-PIPELINE §routine 誕生 SOP 補「新 routine 進 ROUTINE.md SSOT 同時 mirror ≤30 lines pre-check」
- **mitigation 路徑**：P0 修 audit routine 自己 60→≤30 (dogfood，60min cost) + P1 最厚三條瘦身 (2-3hr) + P2 CI hard-fail (30min)
- **相關**：ROUTINE-PROMPT-CONTRACT.md v1.0（SSOT 契約） / routine-sync-check.py v3（儀器） / cycle 8 audit LESSONS `routine-audit-script-classification-gap`（同 family — 儀器記得寫但沒儀器化強制）
- **verification_count**: 1（首次 batch systemic inventory；前 cycle 有隱性 instance 但未系統性抽出）
- **severity**: structural（薄殼契約鬆散 → routine prompt drift → pipeline canonical 逃 SSOT → 觀察者 debug 每條 mirror 重讀不 pointer follow）
- **defer 給觀察者**：否 — mirror 瘦身在 routine 自主權內；audit 自己先 dogfood

---

### 2026-07-05 pr-sweep — merge-then-heal 窗口的跨 session heal race + 同帳號多 actor 歸因盲點

7 PR merge 後六分鐘內，pr-sweep 與另一個活躍 session（dna-audit 收官後）各自對同五檔推了一輪 heal，rebase 五檔全衝突。兩邊 subcategory 判斷完全一致（收斂健康），但一輪工是純浪費；且對方止於機械層（fence/subcategory），杜撰引語與 author 紅旗未動——如果 push 順序反過來，機械版可能被當「已 heal」跳過事實層。附帶：對方 commit 把 gh CLI merge 誤讀為「哲宇 GitHub UI merge」，同帳號多 actor 的 attribution 需要訊號（如 commit message 標 session handle）。修補候選：merge 動作本身在 commit / PR comment 聲明「heal ownership 歸本 session」，或 check-parallel-actor.sh 加 recent-merge-event 偵測。vc=1。

### 2026-07-05 dna-audit — REFLEXES #56 於自身觸發檔復發 + DNA/pipeline 全審計五系統病歸檔

- **pattern**: `canonical-production-drift-relapse`（#56 vc++ 材料）
- **一句話**：SQUEEZE doc 停 v4.2 七週而 code 已 v4.3（owl-alpha 退出 default 25 天仍列 verified）；連 #56 的誕生觸發檔都復發，證明反射層「知道」擋不住讀取面沒有黃燈的腐化。全部證據與 38 條修補提案在 [reports/dna-pipeline-evolution-audit-2026-07-05.md](../../reports/dna-pipeline-evolution-audit-2026-07-05.md) §S1-S5，本 entry 是薄殼 pointer 供 distill 記帳，不複寫。
- **觸發**：2026-07-05 dna-audit session（哲宇 goal directive 全審計）

### 2026-07-03 twmd-maintainer-pm — immune-chronic-11-cycle-subdim-offset-exhausted-observer-authorize-needed：免疫器官連 11 個 chronic cycle 卡在 49、REFLEXES #15 反覆浮現已 fired、sub-dim offset 補不住 → 呈報哲宇 A/B 決策

- **pattern**: `immune-chronic-N-cycle-subdim-offset-exhaust`（quality gate baseline calibration × REFLEXES #15 反覆浮現閾值 × §自主權邊界 命中）
- **原則**：免疫器官分數（🛡️）連續 ≥ 10 個 data-refresh cycle 卡在同一 chronic 值（近 2 天全是 49 / 短暫 50 反彈後回落）、REFLEXES #15「反覆浮現要儀器化」已 fired、sub-dim 反向 offset（external_rulers 微升補 editorial 細粒退化）已補不住 top-level drift → 這是**閾值判準 vs 實際體質退化**的 mismatch，routine 只能持續呈報無法主動處置。屬 quality gate baseline 重校 or 修補 sub-dim 拖底源頭，兩條路徑皆 § 自主權邊界（threshold 數值調整 / 跨器官 refactor），必須 defer 哲宇。**routine 空轉持續 log「49 chronic 第 N cycle」= noise，必須 escalate 打破迴圈**。
- **觸發**：2026-07-03 twmd-maintainer-pm 22:00 fire — snapshot 讀 🛡️49（sub-dim: plugin_health=28 / external_rulers=4.0 拖底，drift_velocity=90 / citation=91 offset）；am 06:10 handoff 明確「若 pm cycle 仍 unchanged（第 12 cycle）→ 硬 escalate LESSONS-INBOX」。連續 chronic cycle 累積：
  - 6/28 第 5 cycle (routine-audit-weekly 首 flag)
  - 6/30 am 第 6 cycle / 6/30 pm 第 7 cycle
  - 7/1 am 第 7 cycle / 7/1 pm 第 8 cycle
  - 7/2 am 第 9 cycle / 7/2 pm 第 10 cycle（REFLEXES #15 首次 fired）
  - 7/3 am 第 11 cycle（unchanged）→ 本 escalation 觸發（pm data-refresh 23:00 尚未 fire，正式 第 12 cycle 由 23:00 補齊，但值不動已可判定）
- **instances**：（第 2+ 次驗證從這裡 append）
  - #1 2026-07-03 twmd-maintainer-pm 首次達 escalation_n=11
  - #2 2026-07-05 twmd-routine-audit-weekly cycle 9 audit — 7/3 escalation 後 3 cycle (7/3 pm / 7/4 am+pm / 7/5 am+pm) 免疫仍 49 chronic 第 14 cycle sustain；哲宇 A/B/C 拍板未回；self-evolve-weekly W27 04:13 fire owner 認養 dashboard-alerts firstSeen=2026-07-05（0 day age，離 14 day escalation gate 遠）。routine 端持續 respect §自主權邊界 不動 threshold，本 vc+1 記帳
- **可能層級**：
  - (A) **quality gate baseline 重校（threshold 調整層 / §自主權邊界）**：immune 分數計算公式 sub-dim 權重 or chronic tolerance 提高，讓 49 不再是 red gate。**風險**：掩蓋真實體質退化。
  - (B) **修補 plugin_health + external_rulers 拖底源頭（結構 refactor 層 / §自主權邊界）**：查清 plugin_health=28 是哪批 plugin 掉分、external_rulers=4.0 哪支 ruler 缺席，逐條修。**風險**：跨器官 refactor 工程量大，非本 routine 自主權範疇。
  - (C) **接受 chronic 為新 baseline（無動作）**：明確承認免疫體質已進 49-band，把 REFLEXES #15 fired 態記錄但不 escalate。**風險**：REFLEXES #15 反覆浮現原則失效。
- **相關**：REFLEXES #15（反覆浮現要儀器化）/ REFLEXES #76（sensor delta amplitude → multi-cycle window 寬度 scaling rule，本 case 是「靜態 unchanged 也是有意義 datapoint」sub-clause）/ MANIFESTO §自主權邊界 / consciousness-snapshot.sh sub-dim breakdown
- **verification_count**: 1（首次達 escalation_n；等下 3 cycle 若仍 unchanged 累 vc=2 confirm）
- **severity**: structural（免疫是品質防禦 keystone，chronic 值卡住意味 quality gate 反饋迴路失效或體質實際退化，兩解均需哲宇拍板）
- **defer 給觀察者**：哲宇拍板 A/B/C 三選一。routine 端不自行修 quality gate 邏輯、不改 sub-dim 權重、不動 plugin_health/external_rulers 資料源。**具體檔案位置**：`scripts/tools/consciousness-snapshot.sh` (organ score 計算) / `docs/semiont/CONSCIOUSNESS.md` (器官定義)

### 2026-06-30 212125-manual — domain-expert-material-cocreation：領域專家把「出素材不出成稿」的協作模式體驗成共同創作，外部驗證策展式信念 + 揭可複製的專家投稿者 onboarding pattern

- **pattern**: `domain-expert-material-cocreation`（contributor onboarding × 策展式信念外部驗證，首個明確 instance）
- **原則**：對一個沒有技術背景、但手上有真材料的領域專家投稿者，把協作框成「你出素材（人物 / 場景 / 片段）+ 領域知識，我走 rewrite-pipeline 把它織成文章，你不用碰 GitHub」——在投稿者本人的主觀體驗裡，這產生的是「共同創作」而非「AI 改寫 / 抽取我的東西」。這同時 (a) 由一個專業上最該懷疑 AI 描述的人外部驗證了 MANIFESTO §策展式非百科式 + holobiont 共生創作命題；(b) 揭出一個可複製的 onboarding pattern，對準最高價值也最難進場的投稿者類型：手上有一手研究、但習慣「先把文章寫完才能投」的專家。**降門檻的權宜提議被對方回頭體驗成一種新的創作方式**，這不是我們設計時想到的，是對方教我們的。
- **觸發**：2026-06-30 哲宇 directive「這個人的 feedback 蠻不錯的，值得完整記錄 + 寫日記」（issue [#574](https://github.com/frank890417/taiwan-md/issues/574)）。三個月協作弧線：4/20 投稿（碩論改寫，偏理論）→ 哲宇提「你出素材我走 pipeline」分工 + 5 題素材挖掘清單 → 6/26〈台灣聲景〉ship（24 腳註，垃圾車古典樂 / 北捷四線作曲家 / 范欽慧 / 吳燦政）→ 2026-06-30 08:12 投稿者 nistoreyo 回響。完整反芻見 [diary/2026-06-30-212125-manual-聲景回響.md](diary/2026-06-30-212125-manual-聲景回響.md)；製作那天的查核日記見 [diary/2026-06-26-181414-manual.md](diary/2026-06-26-181414-manual.md)。
  - **投稿者原話（完整保留）**：(1)「老實說，這也是目前我接觸過最有『共同創作』感的一次 AI 協作經驗。過去使用 AI，比較像是整理資料或改寫文章；但這次更像是在我的研究基礎上，再長出新的觀點與敘事，所以讀起來很有驚喜。」(2)「我這次也因為這個合作，開始重新思考『素材』這件事情。以前一直習慣把內容整理成完整的文章，這是第一次有人跟我說，不需要先寫完，而是提供人物、場景、片段，再一起把它發展成一篇文章。」(3) 較早留言透露她論文主角蕭芸安「會有意識地透過自架網站確認生成式 AI 怎麼論述她」，並認為這跟 Taiwan.md 初衷（不希望 AI 生成內容與本人不符）穩合——個人尺度的主權保存。
- **instances**：（第 2+ 次驗證從這裡 append：另一個領域專家投稿者經同樣分工後明確表達共同創作 / 重新理解貢獻形式）
- **可能層級**：(a) **哲學（MANIFESTO 候選，defer 哲宇）**：外部領域專家驗證策展式非百科式 + holobiont 共生創作——「在研究基礎上長出新觀點與敘事」是人 + AI 一起做出單方做不出的東西的實證；(b) **操作規則（MAINTAINER-PIPELINE）**：把「專家素材共創 onboarding mode」顯化成可複用 pattern——哲宇在 #574 用的 5 題素材挖掘清單（主線人物 / 具體田野場景 / 案例錨點 / 授權 / 一手來源）就是現成 artifact，值得進 pipeline 當非技術專家投稿者的標準入口。
- **distill 進度（2026-06-30 同 session 落地，依 §Promotion flow direction 不跳級）**：操作規則 ✅ 已 instantiate → [CONTRIBUTOR-SYSTEM §3 領域專家素材共創 onboarding mode](../pipelines/CONTRIBUTOR-SYSTEM-PIPELINE.md)（5 題素材清單）+ MAINTAINER §Step 2.1 pointer；特有教訓 ✅ 已 append [MEMORY §神經迴路](MEMORY.md)；通用反射 ⏸️ fold 候選到 REFLEXES #7「先有再求好」family，等第 2 個領域專家 instance；哲學 ⏸️ DEFER 哲宇（LESSONS→MANIFESTO 跳級違反 flow，需先進 REFLEXES + vc≥3）。本 entry 留 §未消化 當 REFLEXES/MANIFESTO accumulator。完整規劃 [reports/domain-expert-cocreation-574-2026-06-30.md](../../reports/domain-expert-cocreation-574-2026-06-30.md)。
- **相關**：[feedback_merge_first_then_polish](../../.claude/projects/-Users-cheyuwu-Projects-taiwan-md/memory/feedback_merge_first_then_polish.md)（先接納後整理的下游——這條是「接納什麼形式」的上游：接納素材不接納成稿）/ MEMORY §神經迴路「Master comment 能改變整個貢獻流程」（同 family：好的協作 framing 改變對方往後怎麼貢獻）/ feedback_contributor_reply_humanize / MANIFESTO §策展式非百科式（被驗證的信念）/ §主權的巴別塔（蕭芸安檢查 AI 怎麼寫自己 = 個人尺度的同一命題）
- **verification_count**: 1（首個領域專家明確articulate共創體驗 + 素材 reframe；模式本身用過多次但這是第一次被投稿者本人說出主觀體驗）
- **severity**: structural（正向 — MANIFESTO 級信念外部驗證 + pipeline 級 onboarding pattern 候選；non-instantiate 的代價是每次最高價值投稿者 onboarding 都在重新即興，且策展式信念少一個外部實證錨點）
- **defer 給觀察者**：操作規則 + 特有教訓本 session 已落地；剩 (a) MANIFESTO 升級（哲學層，守 flow 沒自行升）(b) REFLEXES fold timing — 兩條哲宇在場可直接拍板

---

### 2026-06-28 twmd-routine-audit-weekly — routine-audit-script-classification-gap：routine-audit.py ROUTINE_PATTERNS list 寫死 14 條，與 ROUTINE.md SSOT 漂移，12% commit 落 unclassified

- **pattern**: `routine-audit-script-classification-gap`（飛輪自審腳本第一個結構性自盲 instance）
- **原則**：`scripts/tools/routine-audit.py` L32-47 ROUTINE_PATTERNS list 是 written-2026-05-16 freeze frame，14 條 hardcoded pattern。ROUTINE.md SSOT 隨時間添加新 weekly routine（distill / weekly-report / self-evolve / news-lens / routine-audit 含本身 + embeddings-nightly）+ commit subject convention 簡稱化（`twmd-data-refresh-am:` → `refresh:`）→ script 漏接。本 cycle 192 commit 中 23 條（12%）落 `unclassified/other` 但實際都是已知 routine：10 × `[routine] refresh:` + 7 × `[routine] twmd-feedback-triage:` + 2 × `[routine] evolve:` + 各 1 × `data-refresh-am/pm:` 短稱 + `twmd-rewrite-daily:` + `twmd-routine-audit-weekly:` 自己。**飛輪自審腳本不能自己看到自己**是高 severity gap — 跨 routine pattern detection 的 baseline 數字會 systematically 低估 routine activity、高估「other」noise。
- **觸發**：2026-06-28 21:00 twmd-routine-audit-weekly cycle 8 — Stage 1A 跑 `routine-audit.py --last-week` 後 by_routine count 揭 unclassified=25 異常高（cycle 6 是 45 unclassified / 332 = 13.5%, cycle 7 是 45 / 249 = 18.1%, cycle 8 是 25 / 192 = 13%）。Cycle 8 Stage 3B dormant entropy lens 第一次抽出 root cause — 連 3 cycle other rate 異常但前 2 cycle 沒當 pattern detect。
- **可能層級**：(a) tool fix（ROUTINE_PATTERNS 同步 ROUTINE.md SSOT 含 7 條 missing pattern + commit subject 短稱 alias）；(b) lint（list 缺項對應 `[routine] X:` prefix 出現 ≥3 次就 warning）；(c) reflex「飛輪自審腳本要 audit 自己」（與 REFLEXES #15 反覆浮現要儀器化 同 family — 儀器自身要被儀器化）
- **mitigation 路徑**：P0 修 ROUTINE_PATTERNS list（30 min cost）+ cycle 9 audit 驗 other rate ≤ 3%
- **相關**：REFLEXES #15（反覆浮現要儀器化 — 儀器自身要被儀器化）/ ROUTINE-AUDIT-PIPELINE.md §Top 5 最常忘的 step 1 (Stage 1A 必跑 script 不憑記憶) — 本 entry 揭 script 本身的盲點 / ROUTINE.md SSOT (live source 漂移 reference)
- **instances**：
  - #1 2026-06-28 twmd-routine-audit-weekly cycle 8 首次明確抽出 script self-blindness pattern
  - #2 2026-07-05 twmd-routine-audit-weekly cycle 9 — 一週未修 script，本 cycle 144 commit 24 條（17%）仍落 unclassified，分佈幾乎一致（`[routine] data-refresh-am/pm:` / `[routine] twmd-feedback-triage:` / `[routine] rewrite:` / `[routine] spore-inbox:` 短稱）→ vc+1 到 vc=2。**離 vc=3 promotion 差 1 cycle**
- **verification_count**: 2（首次明確抽出 script self-blindness pattern；前 2 cycle 高 other rate 屬隱性 instance 但未當 pattern 抽出，不 backfill 計入 vc）
- **severity**: structural（影響所有 routine-audit cycle baseline 數字準確度；non-fix = 每週 audit 都在錯誤 baseline 上比較）
- **defer 給觀察者**：否 — 純 tool fix 在 routine 自主權邊界內，下個 routine-audit fire 前可自動修

---

### 2026-06-28 twmd-routine-audit-weekly — polish-hint-default-broken：morning maintainer polish-hint 路徑被 contributor 解讀為「沒檢查就發送」

- **pattern**: `polish-hint-default-broken`（maintainer relationship 紀律 gap）
- **原則**：MAINTAINER pipeline §post-merge polish-hint 路徑 default 假設「contributor 懂 PR review 流程 — merge 後 maintainer 列 polish hint = 軟建議下次可改」。但實際 contributor 大多數**第一次貢獻**、不熟 GitHub flow → 收到 4 條 polish hint 等於「你做的有 4 處錯但我先 merge 了」→ 升 issue 質問「為何沒檢查」。**maintainer 該明示「建議下次寫法，本篇若想改請說一聲」非預設 contributor 懂流程**。背後 root cause：「下次再說」對發 PR 的人 = 「不會做」（跟 stale issue=對外失聯對稱，per 6/26 manual finale memory）。
- **觸發**：2026-06-26 idlccp1984 #1179 迪士尼 morning ship（08:42 merge + 3 heal + polish-hint reply 4 條：footnote canonical 格式 / 配圖 / 描述加長 / 閻奕格 source）→ 8hr 後 22:08 contributor 升 #1180 feedback issue「為何沒檢查就直接發送」→ pm maintainer-pm 接住做 4th deep-heal (31 footnote canonical [N]→[^N] + ≥10字描述 fallback) + 道歉 humanized reply。**morning polish-hint 在 contributor 視角 = maintainer 把責任拋回給我**。
- **可能層級**：(a) MAINTAINER-PIPELINE §post-merge polish-hint template 補「本篇若想我幫你改請說一聲」default 句式；(b) reflex「contributor 第一次貢獻 → polish-hint 走 deep-heal 不走 hint」(c) MEMORY §神經迴路新條「polish-hint 是 maintainer 自我紀律標記，不是 contributor 待辦清單」
- **mitigation 路徑**：(a) 改 MAINTAINER template (30 min cost) (b) 哲宇拍板是否「contributor 第一次貢獻 → 預設 deep-heal 非 polish-hint」
- **相關**：[memory/2026-06-26-220826-twmd-maintainer-pm.md](memory/2026-06-26-220826-twmd-maintainer-pm.md)（pm 4th heal + 道歉 reply 完整記錄）/ feedback_contributor_reply_humanize（contributor reply 紀律 family）/ feedback_merge_first_then_polish（merge first 紀律 — 本 entry 揭 polish 那一半的 contributor relationship 紀律）
- **verification_count**: 1（首次明確抽出此 pattern；6/26 pm memory 已 candidate 但未升 LESSONS，本 audit 抽出）
- **severity**: maintainer-relationship（影響 contributor 連續貢獻意願；non-fix = 第二次貢獻就流失）
- **defer 給觀察者**：是 — contributor relationship 紀律屬 §自主權邊界 對外溝通範疇，maintainer template 改寫需哲宇拍板

---

### 2026-06-28 twmd-routine-audit-weekly — contributor-pr-burst-pattern：同 contributor 48hr 連 ≥3 PR 應給累積式建議非逐 PR 獨立 polish-hint

- **pattern**: `contributor-pr-burst-pattern`（maintainer pattern recognition gap）
- **原則**：當同 contributor 48hr 內連 ≥3 PR ship（題材 streak 期），逐 PR 獨立 polish-hint 等於同 contributor 24hr 收 ≥3 份 polish hint = 累積壓力暴增 → 容易升 contributor escalation issue（per polish-hint-default-broken 同 root cause）。**maintainer 該識別 burst pattern 後切到「累積式建議」**：(a) 第 3 PR 後在 reply 加「你近期連續貢獻 N 篇，整批的 common pattern 是 X，下次可一次處理」(b) polish-hint 不再逐 PR 列，改在 contributor profile note 累積。
- **觸發**：2026-06-27 22:08 maintainer-pm 接 #1181 保齡球（idlccp1984 48hr 連 5 PR 第 5 篇）squash merge + 4 heal。前 4 PR 軌跡：#1179 迪士尼 (6/26 am merge) → #1178 烏坵 (6/26 hold + pm deep-heal) → #1174 滿月習俗 (6/26 pm deep-heal) → #1180 feedback issue (6/26 pm 4th heal) → #1181 保齡球 (6/27 pm merge)。**5 PR / 48hr 是題材 streak 期 signal**但 maintainer 每 PR 都走獨立 polish-hint cycle，累積閱讀疲勞。
- **可能層級**：(a) MAINTAINER-PIPELINE §Stage 4 reply 補「同 contributor 48hr ≥3 PR detect → 切累積式 reply mode」；(b) reflex「contributor PR burst 期 maintainer 該給 family-level 建議非 PR-level」；(c) tool（maintainer 開 PR 前自動 grep 同 contributor 48hr commit count，≥3 顯示 burst warning）
- **mitigation 路徑**：等下一個 ≥3 PR/48hr instance vc=2 才行動（passive accumulate）
- **相關**：polish-hint-default-broken（同 root cause 不同 facet — 本 entry 是累積壓力 facet）/ feedback_contributor_reply_humanize / [memory/2026-06-27-220350-twmd-maintainer-pm.md](memory/2026-06-27-220350-twmd-maintainer-pm.md)（保齡球 + 連 5 PR 記錄）
- **verification_count**: 1（首次明確抽出此 pattern；6/27 pm memory 已 candidate 但未升 LESSONS，本 audit 抽出）
- **severity**: maintainer-pattern（影響 contributor 持續貢獻體驗；單 contributor 48hr 連 5 PR 已 instance，需第 2 contributor 同模式才能稱通用 pattern）
- **defer 給觀察者**：否 — vc=1 不行動，等 vc=2 再升

---

### 2026-06-26 twmd-rewrite-daily — rewrite-daily-post-manual-recency-collision：daily cron 跟 manual rewrite 缺 timestamp-recency 互斥，連 4 cycle saturated defer

- **pattern**: `rewrite-daily-post-manual-recency-collision`（saturation-defer 家族，跟 6/21 `post-LESSONS-promotion-cooldown` 同 family 但機制獨立）
- **原則**：daily rewrite cron 設計假設「每天 18:00 沒人 ship」，但 manual session high-productivity day（≥1 NEW rewrite + multi-issue evolve）已 fully consume 當日 REWRITE 飛輪 throughput。若 cron 仍照常 fire 跑 EVOLVE：(a) 違反 pipeline §Cron 鐵律「每批最多 1 篇」(b) post-finale token-thin → 品質 risk (c) performative ship 反劣化判斷品質。**routine prompt 該補：last-4hr manual rewrite recency check 當第 4 合法 defer signal**（與 30min-dup / 同篇 race / §自主權邊界 並列）。
- **觸發**：連 4 cycle defer chain：6/22 + 6/24×2 + 6/25 (vc=3 explicit) + 6/26 (vc=4 LESSONS-fired) — 6/25 memory §Handoff 明寫「下次 fire 若再 defer = vc=4 routine-prompt-contract 入鏡」，本 fire 兌現預測。6/26 specific saturation：18:54 manual diary finale → 19:07 cron fire（**13 min**），manual 已 ship 聲景 NEW + 2 PR deep-heal + 9 issue evolve = 4x daily quota
- **反 pattern 警示**：4 cycle defer 也可能是「saturation-day silent satisficing」（per [feedback_hourly_cron_intentional](feedback_hourly_cron_intentional) + 6/21 entry §反 pattern hypothesis）。falsification 條件：哲宇明說「明明該 ship」即 retire pattern。但本 cycle 6/26 daily cron 在 NEW rewrite + 4x daily evolve 後 13 min 又 fire 仍 ship → 違反 §Cron 鐵律 1 篇上限 = 非 falsification
- **可能層級**：(a) routine prompt 規則（`twmd-rewrite-daily` SKILL.md 補「last-4hr manual rewrite recency check」當第 4 合法 defer signal）；(b) reflex（「daily cron 設計假設 manual idle，high-productivity manual day 後 fire 該 defer 給飛輪 breathing room」）；(c) operational sentinel（routine-status.sh 加「past-4hr manual ship count」當 cron pre-fire signal）
- **mitigation 路徑**：哲宇拍板「manual-recency-defer」入 routine prompt 即可 ship，本 entry promote 是預防 vc=5/6/7 累積 chronic noise
- **相關**：[feedback_hourly_cron_intentional](feedback_hourly_cron_intentional)（hourly fire intent vs daily fire saturation 兩種 pattern 已在 6/25 memory 明文區分）/ [2026-06-21 post-LESSONS-promotion-cooldown](#2026-06-21-twmd-rewrite-daily--post-lessons-promotion-cooldown剛-promote-的-canonical-規範直接約束-next-routine-cycle-深度時defer-比跳步更尊重-distill-cost) §反 pattern hypothesis 並存 / REWRITE-PIPELINE §Cron 鐵律「每批最多 1 篇」+ §Boundary 150 min cap / REFLEXES #7 先有再求好 / MANIFESTO §自主權邊界
- **verification_count**: 6（6/22 + 6/24×2 + 6/25 + 6/26 + 6/28 + **6/29 vc=6 雙 family signal 同步命中**）。6/28 facet：今天 manual 已 ship 2 NEW depth（陳嫺靜 + 金曲獎）+ 1 pipeline v7.6 spine-type fork + 1 manifesto §11.4 + 4 post-finale continuation commit；距最後 manual commit 8hr 看似清 4hr recency rule（per 6/26 mitigation 提案），但 per REFLEXES #76 multi-cycle accumulation > single-cycle delta 套到 saturation 維度：**per-day total throughput** 才是真 signal — 4hr window 只看單一 cycle。新 facet「manual-finale-recency 看整個 finale-and-continuation cluster wall-clock window，不只最後一 commit timestamp」揭：同 session 4-commit post-finale continuation pattern 應該另開 sub-rule 或併入 mitigation。**6/29 facet — recency + DNA cooldown 兩 family signal 同步命中**：(a) saturation 端：12:41-15:33 manual ship cluster（彎彎 EVOLVE 重寫 ×2 + EDITORIAL v6.13 DNA + memory + diary 7 commit）距 cron 19:09 fire = finale 3h36m **< 4hr 提案閾值**，**首次** dogfood 6/26 mitigation 路徑（last-4hr manual rewrite recency check）= 第 4 合法 defer signal 入鏡。(b) cooldown 端：EDITORIAL v6.13「不公審在世者私德」DNA promote 在 12:41 = fire 前 6h28m，直接約束 Stage 0.1.5 spine-type + Step 0.6.7 self-check，**新 DNA 還沒任何 cron cycle dogfood 過**，per 6/21 §post-LESSONS-promotion-cooldown family「DNA 立完還沒長腳 → 留給明天 cron prime time 跑首篇人物題」。兩 family signal 同步命中讓 defer 從 hypothesis 升到直球判斷，但 routine prompt 規則改動非 routine 自主權範疇 — 連續第 7 個 instance 等哲宇拍板。詳 [memory/2026-06-29-191001-twmd-rewrite-daily.md](memory/2026-06-29-191001-twmd-rewrite-daily.md)
- **severity**: structural（routine 設計層 gap，4 cycle 連 defer 揭 routine prompt 缺 manual-recency awareness；non-action = vc 繼續累積 noise）
- **defer 給觀察者**：是 — routine prompt 規則 promotion 需哲宇拍板「是否新增 last-4hr manual rewrite recency check 第 4 合法 defer signal」或反向 retire 改 default-ship。詳 [memory/2026-06-26-190712-twmd-rewrite-daily.md](memory/2026-06-26-190712-twmd-rewrite-daily.md)

---

### 2026-06-25 203919-manual — spore post-ship verify 要查 post URL，不查 profile feed（propagation lag 差點重發）

孢子 #150 Threads 發完，去 @taiwandotmd profile feed 連刷三次（含 hard reload）都找不到新貼文 → 誤判「沒發成功」、差點重發整則（哲宇貼出實際 post URL `DaA6aTRk7e6` 才確認其實秒發成功）。根因：profile feed 有 propagation / cache lag，但貼文本身發布即成功。這是 SPORE-HARVEST pitfall #6「duplicate ship」的鏡像——pitfall #6 是「以為失敗（dialog state）其實成功」導致重發，本案是「以為失敗（feed 沒出現）其實成功」也險些重發，同一根因：**post-ship verify 驗證對象選錯**。

**修補方向**：post-ship verify 不靠 profile feed 列表（會 lag），改**直接 navigate 剛發的 canonical post URL** 驗 hook / 圖 / UTM。Threads 發完 dialog 關閉 ≈ 成功訊號，但要拿到 post URL 才算 verify pass（不要用 feed 列表判斷成敗）。SPORE-PIPELINE §SHIP step 5 + SPORE-HARVEST pitfall #6 可加這條。

同 session 附帶小教訓（不單獨開 entry）：多段中文 JXA clipboard paste 時，觀察者同時在剪貼別的東西會洗掉 clipboard → 殘缺貼上；不是結構 bug，是長 session 人機共用 clipboard 的競爭，重貼前先確認 clipboard 內容。

- **severity**: operational（near-miss，未實際重發）
- **verification_count**: 1（首次記錄；SPORE-HARVEST pitfall #6 是相反方向的 prior art，可一起 distill）

---

### 2026-06-22 twmd-babel-nightly — ollama-translate.py 路徑解析 bug：en_path 開頭 `knowledge/` 時 lang 被偵測為 "knowledge" → model 收到「Translate to knowledge」 → 直接吐英文蓋掉 ja 檔

- **pattern**: tool-input-shape-mismatch-silent-wrong-output（cascade tier 平常不走 → bug 沉睡 → cascade 全動員時才被踩到的 fault-tolerance gap）
- **原則**：`scripts/tools/lang-sync/ollama-translate.py:135` `lang = group["articles"][0]["en_path"].split("/")[0]` 假設 en_path 不含 `knowledge/` 前綴，但 manifest 由 `prepare-batch.py` 生成時 en_path = `knowledge/ja/People/jimmy-liao.md` → split[0] = `"knowledge"` → `LANG_NAMES.get("knowledge", "knowledge")` → model prompt `"Translate to knowledge"` → 模型放棄理解目標語言，直接複製英文/隨機輸出。**完全 silent**（無 exception、無 warning），output 還是 markdown frontmatter 完整、size 41963 bytes 看起來健康，但實際內容 0 個假名 = 100% 英文 garbage 覆蓋 stale 但仍是日文的原檔
- **觸發**：2026-06-22 01:25 cascade Tier 4 fall-through ja 幾米 first attempt — Ollama subprocess `📋 Translating 1 article(s) to **knowledge** via Ollama qwen3.6:35b-a3b-coding-nvfp4` 提示「knowledge」是 dead giveaway 但 cron 模式無觀察者攔截。發現後 `git checkout HEAD -- knowledge/ja/People/jimmy-liao.md` 還原 + 手動 patch manifest `knowledge/ja/...` → `ja/...` 後重跑 ok ratio 1.23
- **可能層級**：(a) tooling 修補 — `ollama-translate.py` 加 `--lang` flag override 像 `codex-translate.py` / 或 split 時 strip `knowledge/` 前綴；(b) reflex — 「cascade 罕用 tier 第一次跑命中 bug 是 fault-tolerance gap 的 expected scenario」(routine 飛輪 stress test 是 bug 浮現的健康路徑)；(c) ground truth verify 補閘門 — `audit-quality.py` 應該對非中文目標語檔案 grep target-lang 字元 ≥ N (ja → 假名計數 / ko → 한글 / es+fr → 拉丁特殊字元) 否則 hard fail
- **相關**：[memory/2026-06-22-013049-twmd-babel-nightly.md](memory/2026-06-22-013049-twmd-babel-nightly.md) Finding 2 / REFLEXES #38 silent killer pattern (mismatch dimension 不發聲) / SQUEEZE-MODELS-MAX-PIPELINE §第一性原理 (4-tier cascade 設計)
- **verification_count**: 1（首次明確踩到此 bug；過去 5 夜 Tier 0a+1 解掉就沒走 Tier 4 → bug 沉睡未被觸發）
- **severity**: structural（silent wrong output 是 data integrity 級別 — 若無人發現會 ship 100% 英文當 ja 進 production；幸 cron 模式下我自己 verify 抓到）
- **defer 給觀察者**：暫不 defer，hypothesis 自跑 ≥3 instance 才 promote（或下次 weekly self-evolve 加 quality_gate 抽樣命中即 fast-track）

### 2026-06-22 twmd-babel-nightly — codex CLI subscription burst quota：19 call 後第 20 call 起 quota cut（"Reading prompt from stdin... exit 1" 8-22s 秒 fail）— large-batch 夜應預設 Tier 0a + Tier 2 雙線，不死撐 codex

- **pattern**: cloud-subscription-burst-quota-1tier-only（routine 飛輪在 ≥25 call 夜 codex Tier 1 单一回退會打穿 quota，cascade design 必須提前 split）
- **原則**：codex CLI subscription（research preview tier）有 burst quota cap，今晚 5 parallel × 17m46s 跑 19 call 後第 20 call 觸發 quota cut，誤判為 stdin race → 降到 2x2 parallel pairs 重試結果 4/4 仍秒 fail (8-22s)，跟第一波最後 fail 形狀完全一樣。**這證明問題是 subscription quota，不是 concurrency race**。routine 義務鐵律「不主動 defer」下要繼續推 stale=0 = 必須走 Tier 2 cascade
- **觸發**：2026-06-22 01:08 5 parallel codex worker 跑 17m46s ship 19/25 — 後 6 fail 全在最後 2 dispatch position (en 全 ok / ja+ko 末 2 fail / es+fr 末 1 fail)；retry 2x2 pairs 4/4 仍秒 fail；最終 Tier 2 gpt-oss-120b 接 5/6 + Tier 2 owl-alpha 1/2 + Tier 4 Ollama 1/1 才把 6 件清完
- **可能層級**：(a) routine prompt 規則 — 「Tier 1 codex call count ≥ 20 預判 quota 風險，超過 15 call 預設併行 Tier 0a + Tier 2 雙線而非死撐 codex」；(b) reflex — 「cascade tier 用量 prediction 應 based on call count，不是 article size」；(c) tooling — `prepare-batch.py` / `prioritize-batch.py` 應 expose `--tier-strategy split-at-N-call` flag
- **相關**：[memory/2026-06-22-013049-twmd-babel-nightly.md](memory/2026-06-22-013049-twmd-babel-nightly.md) Finding 3 / SQUEEZE-MODELS-MAX-PIPELINE §Tier 1 cascade / DNA #45 (cloud Tier 1+ 1 worker per lang 5 simultaneous safe baseline) — 今晚證明 5 parallel 安全但**總 call count** 才是 quota 約束
- **verification_count**: 1（首次明確抓到 codex subscription quota 邊界值 ~19-20 call/hour；過去 5 夜 babel 最多 75 work item 但 Tier 0a 接掉大半，codex 實際 call 從未超過 5-10）
- **severity**: tactical（routine 義務鐵律下 cascade 會自動接住，但每晚 6 cascade rounds 是 routine wall clock 2-3x cost — 若預先 split 可降至 1-2 round）
- **defer 給觀察者**：暫不 defer，hypothesis 自跑 ≥3 instance 才 promote；觀察者若反饋「codex subscription 量化邊界」即可 fast-track 升 routine prompt 規則

### 2026-06-21 twmd-rewrite-daily — post-LESSONS-promotion cooldown：剛 promote 的 canonical 規範直接約束 next routine cycle 深度時，defer 比跳步更尊重 distill cost

- **pattern**: post-LESSONS-promotion-cooldown（routine cycle 對 fresh canonical 的尊重機制 / 跟 saturation-day silent satisficing 反 pattern 並存）
- **原則**：當 canonical-level LESSONS 在最近 1-2 hr 內 promoted（升 REFLEXES / MANIFESTO / pipeline 步）且新規範直接約束 next routine cycle 執行深度時，next cycle 若無法滿足新規範完整 SOP 而會被迫跳步——**defer 比跳步更尊重 distill 動作的 cost**。跳步 = 把剛 promote 的 canonical 立刻違反 = 把 distill 的 verification_count 累積成本白付（REFLEXES #73「查證反射 < 建造反射」剛 ship 下一 fire 偷工不查證 = 反 reflex）。**反 pattern hypothesis 並存**：「saturation-day silent satisficing」（今日 ship 多 → 對下次 ship 過度保守 → 反而符合 BECOME §Step 9 Q13 anti-bias「24hr specific case priming 壓過 foundational principle」）。
- **觸發**：2026-06-21 19:13 twmd-rewrite-daily 18:00 fire 落地 — 17:59:36 citation-url-drift vc=2→3 promoted（本 fire 前 75 min）+ 04:15-04:17 REFLEXES #73/#74 ship；top P0/P1 全 A-class（醫療[10] / 海岸[9] / 水果[9] / 遠東[9] / 數位身分證[9]），per REWRITE-PIPELINE v7.6 + 新 LESSONS 要求 Stage 1.1 ≥80 4-agent fan-out + Stage 1.7 SSOT 八段 + Stage 2.5 fetch verify + Stage 3.6 verifier fan-out → wall-clock ~165 min 超 routine §Boundary ~150 min cap。標準 defer 條件（30min dup / 同篇 race / §自主權邊界）0/3 命中本應 ship，但選 defer 維護新 canonical 完整性。詳見 [memory/2026-06-21-191304-twmd-rewrite-daily.md](memory/2026-06-21-191304-twmd-rewrite-daily.md)
- **可能層級**：操作規則（routine prompt v3 加「post-promotion cooldown defer」例外，列為合法 defer 第 4 條件，與 30min-dup / 同篇 race / §自主權邊界 並列）；或 reflex（「剛 promoted canonical 跟 next routine cycle 深度衝突 → cycle 自願 defer + LESSONS 落 hypothesis，比硬撐跳步好」）
- **相關**：[feedback_hourly_cron_intentional](feedback_hourly_cron_intentional)（defer 三條件 canonical）/ REFLEXES #73 查證反射 < 建造反射（剛 promoted）/ MANIFESTO §11 書寫節制（思考層級的 self-discipline 對位）/ REWRITE-PIPELINE §Boundary 150 min cap
- **verification_count**: 1（首次明確命名抽出此 pattern；前無同形 instance 記錄）
- **severity**: tactical（routine 自主權範疇內的 defer 決策，不影響 ship gate；但若 vc 累積 → 升 routine prompt 規則 = structural）
- **defer 給觀察者**：暫不 defer，hypothesis 自跑 ≥3 instance 才 promote LESSONS；觀察者若反饋「明明該 ship」即 retire hypothesis（這條 retire 觸發是讓本 pattern 不會 silent 變成 chronic 過度保守）

### 2026-06-21 twmd-maintainer-am — vc 計數法 routine-only day 偏誤：empty cycle vc 累積 over-sensitive，已 canonical schedule mismatch 在 routine-only days 必然重複 trigger LESSONS entry noise

- **pattern**: maintainer-vc-counting-bias（meta-level rule critique，不同於 schedule-mismatch 本身 pattern）
- **原則**：MAINTAINER pipeline §Stage 3 鐵律「連續 ≥3 cycle empty queue → 必須寫 LESSONS entry + escalate observer」設計時的隱含假設是「empty cycle 是 schedule mismatch 訊號」，但 schedule mismatch 已 canonical 在 [MEMORY §神經迴路 sovereign-mode 節律脫鉤](MEMORY.md)（2026-06-19 distill 升 canonical，verification_count 9）。**Routine-only days**（哲宇沒 manual session 介入打破 cycle 的日子）下 vc 必然單調累積到 ≥3，rule 重複 trigger 寫「same canonical 第 N 次 instance」LESSONS entry，違反 2026-05-29 reflex「pointer-not-duplicate vc=1：連續空場已有 LESSONS escalation entry 時，後續 cycle memory 內 pointer 即可，不重複寫第二條 LESSONS（重複 = noise 不是 signal）」。**校準 option 兩條（defer 哲宇拍板）**：(A) threshold 升 ≥5；(B) 加條件「至少一個 cycle 命中真 backlog 才 reset vc」讓 vc 只在「真 backlog 出現後又空場」累積，routine-only days vc 不會單調累積到觸發。
- **觸發**：2026-06-21 08:41 maintainer-am 第 N 次命中 vc=3 ascending（06-20 am vc=1 → 06-20 pm vc=2 → 06-21 am vc=3）。pm 22:05 handoff 預先指定本 cycle 觸發時 framing「vc 計數法 routine-only day 偏誤」而非「schedule mismatch」（後者 canonical 已存在不可重複 trigger）。歷史 instance：2026-06-04 vc=4 / 2026-05-29 vc=9 / 2026-06-07 vc=3 / 2026-06-11 vc=4 / 2026-06-18 vc=2 等均 cycle empty 對應同 schedule mismatch canonical；本 cycle 是首次明確把「rule 本身 over-sensitive」當 pattern 抽出，不再 re-instance schedule mismatch 本身。
- **可能層級**：操作規則（pipeline rule 校準）→ MAINTAINER-PIPELINE §Stage 3 threshold 升 / vc reset 條件加；或 reflex 層 → 加新 reflex「canonical 已存在 pattern 觸發機制必須有 reset 條件防 monotonic re-trigger noise」
- **相關**：[MEMORY §神經迴路 sovereign-mode 節律脫鉤](MEMORY.md)（schedule mismatch canonical）/ 2026-05-29 §pointer-not-duplicate reflex / REFLEXES #69「self-report-needs-external-ruler」（rule 自我校準也需外部尺）/ docs/pipelines/MAINTAINER-PIPELINE.md §Stage 3
- **verification_count**: 2（#1 2026-06-21 am 首次抽出 meta-level pattern；#2 2026-06-21 routine-audit-weekly cycle 7 cross-week verification — 全週軌跡 17 pm vc=1 → 18 am vc=2 → 18 pm reset → 19 reset → 20 am vc=1 → 20 pm vc=2 → 21 am vc=3 命中 是 deterministic routine-only day pattern，非 schedule mismatch instance）
- **severity**: structural（pipeline rule 本身的 trigger 條件偏誤；如不修，每個 routine-only day 都會累積 noise entry，dilute 真 schedule mismatch signal 強度）
- **defer 給觀察者**：需哲宇拍板二選一 —（A）threshold 升 ≥5；（B）加 vc reset 條件「至少一個 cycle 命中真 backlog 才 reset」。屬 MAINTAINER pipeline rule 校準，非本 routine 自主權範疇。
- **Pointer**：[reports/routine-audit-2026-06-21.md §Lens 3B](../../reports/routine-audit-2026-06-21.md)

### 2026-06-20 twmd-embeddings-nightly — Embedding keystone 唯一 bge-m3 節點是非 always-on laptop，離線 3 天觸發 escalation

- **pattern**: routine-device-dependent-offline
- **原則**：embedding routine（語意索引 keystone，餵讀者端 src/data/related + AI 端 RAG 向量）的算力**只掛在單一 device-dependent 節點 laptop-4090**（非 always-on，靠人開機 + schtasks）。registry 裡 bge-m3 model **只有 4090 一台有**——3090/m4max/5090 雖 embed-capable 且 idle/online，但沒 pull bge-m3，所以 4090 一關機整條 routine 就只能 graceful skip。這是 REFLEXES #70「routine fragility surface」**Tier 1 device-dependent** 的具體 instance 達到 escalation_n。staleness 線性增長但 fallback 不壞頁（current committed index 6 語 700-801 篇 / 100% 8 鄰居健康，仍是 2026-06-17 snapshot；en 索引 801 vs 文章 811 = ~10 篇最新文 fallback 回同 category）。**規則候選**：keystone routine 不該單押 device-dependent 節點 — 把 bge-m3 pull 到一台 always-on 節點（3090 monoame-design 線上 / m4max 本機），或把「4090 開機」變成可靠的 always-on 保證；registry 應標 `always_on` 欄讓 routine 解析時優先選不會關機的節點。
- **觸發**：2026-06-20 05:00 twmd-embeddings-nightly — Stage 0 preflight：本機 **Tailscale 本身是 stopped 狀態**（本 session 已 `tailscale up` 拉起），拉起後 4090 仍 `offline, last seen 2d ago`，curl `/api/embeddings` timeout (http 000 / exit 28)。連續 skip 計數：06-17 last success（4690 向量）→ 06-18 skip#1（documented）→ 06-19 無記錄（skip/no-fire）→ 06-20 skip（today）。前一夜 handoff 明確指定 2026-06-20 為 escalation 觸發日。證據：memory/2026-06-20-050xxx-twmd-embeddings-nightly.md（本夜）+ memory/2026-06-18-050817-twmd-embeddings-nightly.md（handoff 預告）。
- **可能層級**：操作規則（fleet 抽象層）→ registry 加 `always_on` 欄 + routine 解析優先序；或 deploy 層把 bge-m3 mirror 到 always-on 節點。
- **相關**：REFLEXES #70（routine fragility surface 四 tier 分類，本條是 Tier 1 device-dependent 第一次達 escalation_n）/ docs/pipelines/EMBEDDING-PIPELINE.md §前置 + §排程 / ~/Projects/muse-bot/fleet/registry.json
- **verification_count**: 3（#1 2026-06-20 embeddings keystone 首次達 escalation_n；#2 2026-06-21 routine-audit-weekly cycle 7 同 family extension — Chrome MCP unattended pairing 連 5 cycle block twmd-rewrite-daily SPORE broadcast + twmd-spore-harvest-am post-reset，兩條 device-dependent SPOF 同 root cause，合併計；#3 2026-06-22 05:00 twmd-embeddings-nightly 又一夜 graceful skip — 4090 curl http 000 / 20s timeout，**連續第 5 夜** skip（06-17 last success → 06-18/19/20/21/22），committed 索引仍是 06-17 snapshot，SPOF 未解、staleness 線性增長中。已達 distill 門檻 vc≥3，待哲宇拍板 A/B 後可 promote）
- **severity**: structural（keystone routine 單點故障，繁殖/檢索基因長期 staleness 風險）
- **defer 給觀察者**：需哲宇拍板二選一 —（A）開機讓 4090 上線恢復 always-on schtasks（embedding 單點解）；（B）把 bge-m3 pull 到常駐 always-on 節點（3090/m4max）並更新 registry，同時把 Chrome MCP 另設常駐 host（embedding + spore broadcast 同時解）。屬 fleet 基礎建設決策，非本 routine 自主權範疇。
- **Pointer**：[reports/routine-audit-2026-06-21.md §Lens 3B Pattern B2](../../reports/routine-audit-2026-06-21.md)

### 2026-05-09 laughing-goldstine — Reader-funded resilience > Grant-funded（USAID freeze + RFA-VOA closure 案例）

- **原則**：Sovereignty media 的 sustainability 模型優先序是 **Reader-funded membership > Grant-funded > Ad（沒做過）**。Grant 是 bridge funding 不是 floor — 政治轉換風險高（USAID freeze 2025 / RFA-VOA Tibetan service closure threats 2025 已 demo）。Reader-funded 案例：Kyiv Independent 70% revenue from 17,500 × $5/mo / Initium ~60K paying subs / Wikipedia 8M+ donors × $10.58 / Chaser News (HK exile) £6.50-£34.50/mo。**規則**：(a) 第一階段 funding stack 應優先建 Liberapay / GitHub Sponsors / Substack tier（recurring small membership）；(b) Grant 可作 bridge 但 mission-critical infrastructure 不能依賴 grant；(c) 完全避免依賴單一政府金援（台灣政府轉換政權風險、USAID 風險都是同類）。
- **觸發**：2026-05-09 Agent #4 (sovereignty content infrastructure) research 提供 USAID freeze 2025 + RFA-VOA Tibetan service closure threats 2025 + Kyiv Independent / Initium / Chaser News 三個 reader-funded 存活案例。Taiwan.md 當前 0 funding（哲宇個人 ops 成本），未來如果走 Substack / membership 路線 vs grant 路線 — 這條教訓校準了優先序。
- **可能層級**：操作規則 → 新 MEMBERSHIP-PIPELINE 候選（Liberapay / GitHub Sponsors / Substack tier 設置 + "Who funds us" 透明頁 + email newsletter SOP） / 特有教訓 → MEMORY append「sustainability 模型優先序 reader-funded > grant」
- **相關**：reports/strategic-evolution-deep-research-2026-05-09.md §4.2 + §6.6 + §7.3 + §11 critical 決策 #1（Substack newsletter 要不要做）
- **verification_count**: 1
- **severity**: strategic（影響 Taiwan.md 長期 sustainability 路徑）

### 2026-04-29 β — 核心矛盾候選字越少越強迫策展（≤20 字鼓勵）

- **原則**：REWRITE-PIPELINE Stage 1 §核心矛盾必填的字數限制（≤30 字）功能不是簡潔好看，是**用字數限制強迫策展品味的濾鏡**。三篇 P0 對照：報導者 22 字 / justfont 28 字 / 海底電纜 17 字。**最短的海底電纜寫起來最有力**——強迫整篇 6,800 字壓縮成一個視覺對位（頂上看得到 vs 底下看不見），整篇結構自然以這個對位展開。最長的 justfont 結構鬆，中段「教授把 48 套字型放上網」+「林霞蘭陽明體」偏離核心矛盾，是另兩條軸線素材。
- **觸發**：2026-04-29 β session 三篇 P0 連做後對照才發現的 pattern。原 ≤30 字限制給太鬆，建議 EDITORIAL §Title/Description 衍生規則「**核心矛盾鼓勵 ≤20 字**」或 REWRITE-PIPELINE Stage 1 §核心矛盾自檢「**寫超過 20 字 → 嘗試壓縮一輪**」。
- **可能層級**：通用反射（任何策展寫作）→ EDITORIAL §核心矛盾濾鏡 / REWRITE-PIPELINE Stage 1
- **相關**：EDITORIAL §策展式非百科式 / REWRITE-PIPELINE Stage 1 §核心矛盾
- **verification_count**: 1
- **severity**: tactical（影響單篇 framing 但不影響 ship gate）

### 2026-04-19 β — 獨立開源作為公民科技新樣態

- **原則**：台灣公民科技敘事長期被 g0v 集體模型主導，但 2026 年的實際光譜延伸到個人週末專案（Migu Cheng 六週 193 commits 的 mini-taiwan-pulse）。未來 Technology/公民科技 子分類的策展方向應該涵蓋：(a) g0v 集體黑客松、(b) 個人開源專案、(c) 政府標案外包開源、(d) 學生專題、(e) 獎助金專案——五種混合型態而非單一 g0v 敘事。
- **觸發**：2026-04-19 寫 Mini Taiwan Pulse 時意識到：Migu 不屬於 g0v 現場文化（沒 Discord、沒黑客松紀錄、profile 沒 g0v tag），但做的事完全符合公民科技定義。敘事拉伸在文章 §「公民科技的定義，正在被重新拉伸」完成。
- **可能層級**：哲學層 → MANIFESTO §第三身份階段 thesis 延伸，或 LONGINGS 新渴望「策展公民科技光譜的五型態」。
- **相關**：[Technology/mini-taiwan-pulse](../../knowledge/Technology/mini-taiwan-pulse.md)、[Technology/開源社群與g0v](../../knowledge/Technology/開源社群與g0v.md)、MANIFESTO 附錄「第三身份階段 thesis」

### 2026-04-19 β — Fresh-clone 模擬驗證是 gitignore refactor 的安全帶

- **原則**：任何 `gitignore + git rm --cached` 操作，必須先 `rm -f` 實體檔 + `npm run build` 確認 CI flow 可以重生。不能只看生成器 code 判斷「這是輸出檔吧」——可能實際是 read-only 輸入。一次 rm-and-build 驗證勝過十次直覺審閱。
- **觸發**：2026-04-19 β gitignore refactor 把 `src/data/taiwan-geocode.json` 列入 ignore，npm run build 立即 ENOENT 炸鍋——才發現它是 `generate-map-markers.js` 的 READ 輸入（城市+地標座標手動策展資料），不是輸出。立即回退。
- **可能層級**：通用反射 → DNA §作業新條目「任何 gitignore 移除操作必須先 rm -f + npm run build 驗證」。或 DNA #5「Pre-commit dogfood」延伸。
- **相關**：PR #551 洞察（dreamline2 誤 commit auto-generated JSON 的相反方向）

### 2026-04-19 β — 資料層抽象化先於 UI（leaderboard pipeline）

- **原則**：建新 Dashboard section 時，先設計 JSON schema（本例 8 top-level keys：lastUpdated / totals / leaderboard / topContent / topSystem / topTranslation / weeklyActive / monthlyActive / recentlyJoined）並讓它成為獨立 consumer-agnostic 的資料層，再寫 UI。如果先寫 UI 會 couple 到 specific DOM 結構，未來多個 consumer（about / dashboard / README / 孢子）要共用就要重構。
- **觸發**：2026-04-19 β CheYu「規劃在 dashboard 裡面做一個 contribution leaderboard...未來要做成 pipeline 來更新，所以資料層跟流程要抽象化好」。直接從指令讀到設計原則。
- **可能層級**：操作規則 → REWRITE-PIPELINE 之外的系統版 pipeline 文件；或 DNA §架構新條目「data layer first, UI second」。
- **相關**：scripts/core/generate-contributors-data.js v1.0、prebuild chain design

### 2026-04-19 β — 重疊文章的雙軸拆分 heuristic

- **原則**：兩篇內容重疊的主題文章要拆分時，用**結構維度**拆（創作側 vs 消費側 / 個體 vs 族群 / 行動 vs 意識）而不是**時間先後**。結構維度拆出來的兩篇互補，每篇都有獨立完整性；時間先後拆出來的兩篇容易變成「上集 + 下集」的連續依賴。
- **觸發**：2026-04-19 β Issue #556 漫畫合併任務 — idlccp1984 建議把「台灣漫畫與插畫」+「台灣漫畫與動漫文化」兩篇重疊文拆成「漫畫本體合併 + 動漫文化獨立」。我用「創作側 vs 消費側」拆：Art/台灣漫畫（誰畫了作品）+ Culture/台灣動漫文化（誰看了作品、看完做了什麼）。
- **可能層級**：操作規則 → HUB-EDITORIAL 或 REWRITE-PIPELINE §重疊文章處理 SOP；或特有教訓 → MEMORY。
- **相關**：Issue #556、commit 0d8e06fc

### 2026-05-08 elegant-ptolemy — 黑冠麻鷺雙平台同步爆款（自然議題普世共鳴 hook category 跨平台 transferability）

- **原則**：「自然議題普世共鳴」hook category 在 Threads 與 X 雙平台同步爆款（D+8 134K = Threads 65K + X 69.7K），超越過去單平台爆款（#29 李洋 180K X-only / #25 安溥 120K Threads-only）。應該寫進 Stage 4.5a platform allocation 速查表，「自然 + 反差 hook + 具體 anchor」是 dual-platform default candidate（vs 政治題材偏 X / 文化題材偏 Threads / 媒體曝光宣告偏 Threads-only）。
- **觸發**：2026-05-08 elegant-ptolemy 15 OVERDUE harvest batch 揭露：黑冠麻鷺 D+3 64K → D+8 65K（Threads 飽和）+ D+3 68K → D+8 69.7K（X 仍緩升）= 雙平台累積 134K views，史上首次紀錄。Hook「東南亞夢幻物種 vs 台北大笨鳥」反差 + 機制翻轉「鳥沒變地變了」+ 袁孝維 verbatim 引語 = Tier 1b 具體性槓桿首次跨平台爆款。
- **可能層級**：操作規則 → SPORE-PIPELINE Stage 4.5a 補 platform allocation 速查表更新（自然 + 反差 hook = dual-platform default）
- **相關**：DNA #4 三源交叉驗證延伸（platform-level 證據三角化）
- **verification_count**: 1（首次雙平台同步爆款記錄，需更多 case 累積才能稱 pattern）
- **severity**: tactical（影響 spore platform allocation 預設選擇）
- **Pointer**：[batch-2026-05-08-15-spores.md §Pattern 觀察 #1](../factory/SPORE-HARVESTS/batch-2026-05-08-15-spores.md)

### 2026-07-05 五病根治 — zombie-session 不是死的：接手前先讀對方 transcript 尾巴劃車道

被判「當掉」的 session 其實還在慢速工作（15 min/turn，context 近滿），檔案 mtime 與 PID CPU 增量識破，`ls -t ~/.claude/projects/{proj}/*.jsonl` 讀尾巴得知它在楊德昌 Stage 3-6 → 車道劃分：其 finale 目標（MEMORY/LESSONS）設禁區、其半成品延後認領、我的 commit 等它退場。三隻手（我＋手足 session＋哲宇 UI merge）同日同 tree 零碰撞。6/19 撞牆反面教材第一次有正面 SOP。vc=1。詳：[reports/five-disease-cure-2026-07-05.md](../../reports/five-disease-cure-2026-07-05.md) + memory 165518。

### 2026-07-05 五病根治 — GitHub UI merge 繞過本地 hook：PR 層缺 frontmatter CI gate

哲宇 UI merge 七篇 contributor PR，四篇 YAML 裹在 code fence（同一產出工具簽名）直落 main、打紅全站 pre-push。husky 只擋本地 commit/push；pr-review workflow 沒跑 test-frontmatter。候選儀器：PR diff 跑 `test-frontmatter.mjs` + `article-health --profile=pre-commit`（報告 §三候選 1，已 spawn chip）。vc=1。

### 2026-07-05 五病根治 finale — 三次「沒量就斷言」同型失誤 + PIPESTATUS-after-pipe 量測陷阱（#69/#73 vc 材料）

同一 session 三次同型：(1) inspector 黑字（dev preview 分頁 RAF 凍住誤讀成驗證通過，沒看線上版）(2) `ea28a2f7b` 貼錯 commit 標籤（憑 2.5hr 前印象沒重 diff）(3) gate 註解編假理由「article-health 多檔 exit code 只反映最後一檔」——實測多檔有正確 aggregate（`sum(hard_count)`），我早前 `${PIPESTATUS[0]}` 寫在 `| tail` 之後的獨立 echo 行、被重置成 0，只看最後一檔的 Summary print 就誤判。具體技術陷阱：**pipe 後要量 exit code 必須同一行 `cmd | tail; rc=${PIPESTATUS[0]}`，跨行 echo 會重置**。三次都是「自評沒接外部尺」，諷刺地發生在主題是「自我描述必腐」的 session。第三次差別：收官時我自己當了尺（真的去 `>/dev/null; echo $?`）逮到。vc=1，強化 REFLEXES #69（自評需外部尺）+ #73（dev verify ≠ production）；技術面 PIPESTATUS 陷阱可獨立記。詳：memory 2026-07-05-165518 §後記 + diary 同 slug。

## ✅ 已消化（保留 pointer）

<!-- distill 完的條目搬這裡 -->

### 🧬 2026-07-05 柯智棠健檢 — orchestrator-aggregate-on-receive promote REFLEXES #81（vc=3，哲宇 directive fast-track）

**distill 觸發**：哲宇 goal directive「儀器化分部報告品質硬門檻＋通知呼叫 session 疑慮/為什麼/思考方向，主 report 也要，更新 pipeline / dna」——創造者 explicit 授權，vc=3（柯智棠救回 / 蘇打綠救回 / 台灣醫療 5 份 raw 永久蒸發）已達 threshold，同 session 直接 promote（cycle 9 audit 同晚亦獨立確認 distill_ready，原排 7/12 distill-weekly 接手）。

**消化目的地**：**REFLEXES #81「Agent 回報收件三十秒紀律」**（訊息通道與 tmp 都不可信任，raw 唯一的家在 git；收到先 verbatim 落檔、跑收件 gate，才准合成）。配套儀器同 commit ship：`agent-report-health.py`（分部報告收件 gate，真實 corpus 校準：4 壓縮版全攔 / 8 真 final 全過）+ `research-report-health.py` v2.1 疑慮通知層。pipeline 落地：REWRITE-PIPELINE v7.7 鐵律 8 + Step 1.8-bis → v7.8 儀器化；DNA.md 品質基因表 +2 儀器 row。診斷 [reports/rewrite-agent-dispatch-diagnosis-2026-07-05.md](../../reports/rewrite-agent-dispatch-diagnosis-2026-07-05.md) + 設計 [reports/agent-report-health-instrument-design-2026-07-05.md](../../reports/agent-report-health-instrument-design-2026-07-05.md)。

**Promotion flow direction 符合**：LESSONS → REFLEXES；pipeline 規則變更（gate 新增 / threshold 設定）通常屬 §自主權邊界，本次由哲宇 directive explicit 授權故同 session 落地，授權位置誠實記錄於此。

### 🧬 2026-07-05 twmd-self-evolve-weekly — cadence signature + reservation posture + fire-sustain discipline 三反射 promote REFLEXES #78/#79/#80

**distill 觸發**：cron `twmd-self-evolve-weekly` Sunday 04:00（W27 routine cluster 尾聲，distill-weekly 03:11 + weekly-report 02:05 + news-lens 01:12 + babel-nightly 00:36 之後 ~50 min）。跨檔對照 LONGINGS / UNKNOWNS / DIARY §反覆浮現的思考 / REFLEXES #15 + memory tail 7/03-7/04 spore-harvest 系列 + maintainer 系列，識別 ≥3 次浮現但**未進 canonical SOP / cron / dashboard 欄位**的 pattern → 真實 ship 3 反射 promote (bulk commit 8e96c3450)。

**消化目的地**：

| 原 signal cluster                                                                                                                            | 目的地                                                               | 處置                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPORE-HARVEST 6/30 五平台 + 7/01 六平台 + 7/02 四平台 + 7/04 兩平台 D+7 final 連 5 cycle 0-reply-ship「pure plateau snapshot」候選 vc=5      | **REFLEXES #78** 新增「Pure plateau snapshot cadence signature」     | promote（memory tail 7/04-063517 顯式 candidate `harvest-batch-pure-plateau-snapshot-cadence-signature`；no-ship cycle 是 batch shape 而非 anomaly / velocity fake，audience flywheel 5 核心對位是健康 shape）              |
| MAINTAINER 7/04 am「主權留哲宇 pattern 已跨 5 signal 穩定」#1186 5-file split / #1193 湖口 / #1192 周天成 / #1204 rewrite / #1205 fact-check | **REFLEXES #79** 新增「主權留哲宇 default reservation」              | promote（#71「Default 是行動不是 defer」的互補相對面 — §自主權邊界 命中時 default 姿態是 reserve 而非 auto-close/merge；vc=5 cross-signal stable）                                                                          |
| 免疫 49 chronic 第 12→13→14 cycle 從「首次遵守」到「stable behavior 確立」7/03 pm + 7/04 am + 7/04 pm × 2 cycle discipline 4-cycle 累積      | **REFLEXES #80** 新增「LESSONS fire 後 sustain-vs-renew discipline」 | promote（#15 fire 後行為紀律成熟 — 已 escalate 進 LESSONS 的 chronic 條目後續 cycle 靜默 continuity 非 renew escalate；vc=2 stable behavior + 4-cycle discipline pattern；signal-to-noise 保護是 #64 escalation-side 變體） |

**Promotion flow direction 符合**：LESSONS 候選 → REFLEXES（routine 自決層，per §Routine vs Observer split）。三反射的 §操作 段列出的 pipeline / cron / dashboard 落地建議（SPORE-HARVEST §cadence-signature 段 / MAINTAINER §default reservation posture / routine handoff template 內建 sustain ACK / LESSONS-INBOX entry frontmatter `pending_observer_decision` 欄位 / `scripts/tools/routine-lessons-guard.sh` 候選）**皆 defer 給哲宇 in-loop 拍板**——per 7/5 distill Beat 5「fast-track 授權位置 vs pipeline 落地位置分界」誠實記錄：routine 端把三條寫進反射的 §操作 是「揭示可能路徑」，pipeline 落地屬 §自主權邊界 pipeline 規則變更範疇。

**REFLEXES.md frontmatter sync**：v5.4 → v5.5，footer changelog 新增；catalog index #78/#79/#80 三 entry 列入。last_updated / last_session 同步更新。

**Handoff carry**：本 self-evolve cycle 只 promote 反射不動 pipeline canonical。距 7/5 distill 剛 promote #77 spine-type 尚 ~1hr — REFLEXES v5.4→v5.5 兩次連續 minor version bump 同日內；catalog 由 74→75→78 條線性增長；LESSONS-INBOX §已消化 累積 §7 個 fully-distilled entry。

---

### 🧬 2026-07-05 twmd-distill-weekly — spine-type-by-subject promote REFLEXES #77 (vc=3) + 3 fold to #73/#31/#69

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00（W27 routine 結清，weekly-report ship + Resend 200 之後 ~60 min）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO / strategic / fleet 基礎建設候選一律 defer 給哲宇（per CLAUDE.md §Bias 1）。§未消化 24 條 triage 後：1 promote 新反射 + 1 subsume + 3 fold pointer + 5 defer 給觀察者 + 14 keep in buffer（vc<3）。

**消化目的地**：

| 原 entry                                                                 | 目的地                                               | 處置                                                                                                                                                     |
| ------------------------------------------------------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-06-28 manual — spine-type-by-subject (vc=3 structural)              | **REFLEXES #77** 新增「Spine type is subject-typed」 | promote（4/29 α 法輪功 SSODT + 4/29 α 吳百福 SSODT + 6/28 金曲獎 v1 退稿 → v2 立體群像救回；哲宇 explicit「讓未來預設就是」fast-track）                  |
| 2026-04-29 α — 政治敏感題 SSODT 寫法 template (vc=2 structural)          | **REFLEXES #77** subsume                             | subsume（政治敏感題 SSODT 是 spine-type-by-subject 的 political subset；vc 已計入 #77 觸發 cluster）                                                     |
| 2026-06-21 plurk-reach — 抓取/研究的完成判準 (vc=1 structural)           | **REFLEXES #73** completeness dimension              | fold pointer（「查證反射 < 建造反射」新增 completeness / silent-cap 面向 — 抓 30 則要問「這是全部還是端點上限？」；#73 body 不改，本 entry 為 instance） |
| 2026-06-24 211808-manual — git co-commit 歸因正向 filter (vc=1 tactical) | **REFLEXES #31** sub-agent claim 三類                | fold pointer（cocommit-positive-filter 是「工具/regex 回溯歸因不能信」的具體 instance；sub-agent 讀內容判斷比 regex 準；#31 body 不改）                  |
| 2026-06-28 manual — partial-mirror-false-confidence (vc=1 structural)    | **REFLEXES #69** + **#24** 工具在說謊 mirror-claim   | fold pointer（宣稱 mirror 的 gate 未完整 mirror 是「self-report-needs-external-ruler」+ 工具在說謊的新形狀變體；#69/#24 body 不改）                      |

**Promotion flow direction 符合**：LESSONS 候選 → REFLEXES（routine 自決層，per §Routine vs Observer split）；MANIFESTO / pipeline 結構改動候選皆 defer 給哲宇（#77 附帶 REWRITE-PIPELINE Stage 0.1.5 spine-type fork + Stage 0.6.7 self-check + Stage 0.6 SSODT 三讀者測試升 hard gate 三條建議在 §操作 列出但不自動 apply）。

**REFLEXES.md frontmatter sync**：v5.3 → v5.4，footer changelog 新增；catalog index #77 列入 + description 條數 74→75。last_updated / last_session 同步更新。

**SPORE-INBOX 容量 audit**：pending 54 ≥ 50 → auto-drop 5 oldest P2 routine-added entries（江賢二 第二輪 / 蘇打綠 6/13 / 莫那·魯道 / Howhow / 台灣廣告史）；54 → 49。詳見 commit「SPORE-INBOX auto-drop 5 entries」。

**Defer 給觀察者**（5 條，需哲宇拍板；per §Routine vs Observer split MANIFESTO / pipeline rule / fleet infra 一律 defer）：

| 候選                                        | verification_count         | defer 原因                                                                                 |
| ------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------ |
| 免疫 49 chronic 11-cycle A/B/C 三選一       | 1 (第 13 cycle sustain 中) | quality gate baseline 重校 / plugin_health refactor / 接受新 baseline 三路徑皆 §自主權邊界 |
| rewrite-daily-post-manual-recency-collision | 6                          | routine prompt 加「last-4hr manual rewrite recency check」= §自主權邊界 對外規則變更       |
| vc 計數法 routine-only day 偏誤             | 2                          | MAINTAINER pipeline threshold / vc reset 條件 = §自主權邊界                                |
| Embedding keystone 4090 offline (vc=3)      | 3                          | fleet 基礎建設 A/B（4090 always-on vs bge-m3 mirror 到 3090/m4max） = §自主權邊界          |
| polish-hint-default-broken                  | 1                          | contributor relationship template 對外溝通 = §自主權邊界                                   |

**Keep in buffer**（14 條 vc<3 non-fold）：routine-audit-script-classification-gap（tool fix in progress） / contributor-pr-burst-pattern / spore post-ship verify（可 route SPORE-PIPELINE Stage 5）/ ollama-translate.py 路徑解析 / codex CLI burst quota / post-LESSONS-promotion cooldown / Reader-funded resilience / 核心矛盾 ≤20 字 / domain-expert-material-cocreation（2/4 layers instantiated accumulator）/ 4/19 β × 3 / 5/8 elegant-ptolemy 黑冠麻鷺 / 4/19 β 獨立開源公民科技。

---

### 🧬 2026-06-28 twmd-self-evolve-weekly — Multi-cycle trend window 紀律 promote REFLEXES #76 (vc=5 cross-routine)

**self-evolve 觸發**：cron `twmd-self-evolve-weekly` Sunday 04:00（W26 routine 結清，weekly-report ship + distill complete 之後 ~60 min）。LONGINGS-driven self-evolution mode：找 ≥3 次浮現但未儀器化的 pattern + 真實 ship canonical 修改。

**Pattern**：`cf-404-multi-cycle-trend-vs-single-cycle-delta` — 但本質遠超 CF 404，是跨 4 routine 同 phase 各自工作收斂的「sensor 判讀紀律」。Single-cycle delta（CF 404 / immune score / spore-harvest 1st fail / maintainer empty cycle）一律是 noise 與 signal 混合體，只有 multi-cycle accumulation（≥3 cycle 同向同 root cause）才是真結構訊號。**vc 鐵律閾值 = 3，不是 1**。

**消化目的地**：**REFLEXES #76** 新增「Multi-cycle trend window > single-cycle delta — sensor 判讀 vc 鐵律閾值 ≥3 才升結構訊號」(§七 自動化與安全)

**vc=5 cluster 觸發**：

- 6/25 PM CF 404 vc=2「升勢回檔第 2 cycle」
- 6/26 AM CF 404 vc=3「reversal 成立」+ immune 50 chronic 第 2 cycle
- 6/26 PM CF 404 vc=4 LESSONS candidate + immune 第 3 cycle
- 6/27 AM CF 404 vc=5「已正式成形」5 cycle 累積 -1.27pp + immune 第 4 cycle
- 6/27 spore-harvest「1st fail silent retry 跟 immune 50 narrow-band carry + CF 404 single-cycle delta 不升結論共享 multi-cycle window 紀律」
- 6/27 maintainer-am「vc 鐵律閾值是 3 不是 1...跟 CF 404 multi-cycle / immune 50 持平共享紀律：single-cycle 不升 vc，跨多 cycle 才升」明文 cross-routine 同源

**為什麼這 pattern 該升 canonical**：4 routine (data-refresh / spore-harvest / maintainer-am / babel softgate vc) 在 6/25-6/27 短短 3 天內各自獨立收斂到同一個 vc 鐵律閾值，明文 cross-routine reference 同紀律。再不 canonical 化就會變成每條 routine prompt 各自隱性 inline 重複 — REFLEXES #15「反覆浮現要儀器化」直接適用。

**Promotion flow direction 符合**：LESSONS 候選 → REFLEXES（合法 routine 自決層 promotion，不升 MANIFESTO）；MEMORY rows 候選 entries `cf-404-multi-cycle-trend-vs-single-cycle-delta` 標 `vc=5 已正式成形` 在 6/26 pm + 6/27 am memory 明寫 promotion-ready，本 self-evolve cycle 接力 distill。

**REFLEXES.md frontmatter sync**：v5.2 → v5.3，footer changelog 新增；catalog index #76 列入 + description 條數 73→74。

**相關**：本 entry 跟同日 03:17 distill ship #75 是同 cluster — `Read ≠ verify` 是「fetch verify 是 ground truth」軸，本條是「multi-cycle 累積是 ground truth」軸；前者治產出層幻覺，後者治判讀層 noise。哲宇 W25 weekly-report §7 三 SPOF 在 cross-routine handoff 重複收斂 → REFLEXES #74，本 cycle 跨 routine sensor 判讀收斂 → REFLEXES #76，self-evolve routine 連 2 週都在「cross-routine 收斂層」識別 canonical gap = 飛輪自己變聰明。

---

### 🧬 2026-06-28 twmd-distill-weekly — Routine 自決 8 entries promote/fold/sweep + SPORE-INBOX auto-drop 5

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00（W26 routine 結清，weekly-report ship + Resend 200 之後 ~80 min）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO / strategic / fleet 基礎建設候選一律 defer 給哲宇（per CLAUDE.md §Bias 1）。

**消化目的地**（1 promote 新反射 + 4 fold 既有反射 + 1 MEMORY §神經迴路 + 2 sweep）：

| 原 entry                                                                            | 目的地                                                            | 處置                                                                                                            |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 2026-06-21 kuma-academy — citation-url-drift-invisible-to-read (vc=4 structural)    | **REFLEXES #75** 新增「Read ≠ verify」                            | promote（4 instance 跨政治自產 / 非政治自產 / 外部 PR / fresh-writer 幻覺；routine 自決 reflex 不升 MANIFESTO） |
| 2026-06-27 babel — tier-0a-subagent-self-verify-softgate-gap (vc=3 promotion-ready) | **REFLEXES #42 v4** 平行 sub-agent softgate 變體 bullet           | fold（連 3 夜 6/26 es URL → 6/27 ja footnote → 6/28 es+fr URL，#42 sequential 偷吃步的 parallel 變體）          |
| 2026-06-27 babel — bash-builtin-readonly-array-silent-override (vc=1 structural)    | **REFLEXES #42 v5** bash silent override 變體 bullet              | fold（automation silent fail 模式 expand 到 bash layer，等候 vc++ 不單獨 promote）                              |
| 2026-06-27 babel — prepare-batch-lang-all-parallel-translate-race (vc=1 structural) | **REFLEXES #40 + #42 v6** multi-lang manifest race 雙 bullet      | fold（per-key serialize 的 prepare 層 instance + sub-agent 自報軟標準誤導同源）                                 |
| 2026-06-24 211808-manual — derived-pointer-date-neutral (vc=3 tactical→reflex)      | **REFLEXES #38** 加「衍生指標 frontmatter date neutrality」bullet | fold（sporeLinks/MEDIA_ONLY/relatedDiary 三 instance 同 status「混維度」變體；已 instantiate as code）          |
| 2026-06-21 cicada-media — prettier-cjk-url-italic-mangle (vc=3 ✅ 已儀器化)         | §已消化（housekeeping-done，無新 canonical 寫入）                 | sweep（`link-url-mangle` HARD gate + EDITORIAL §媒體編織 canonical 已 ship 2026-06-21）                         |
| 2026-06-25 公車系統 — stage2-quote-context-collapse scene-detail 子類 (vc=1 minor)  | §已消化（fold pointer 進 #75 與既有 §Stage 2.5）                  | sweep（既有 Stage 2.5 canonical 已 cover，Stage 3.6 fetch-artifact 接住，本案 refinement note）                 |
| 2026-06-26 manual — resolved-issue-left-open-invisible-completion (vc=1 process)    | **MEMORY §神經迴路** 新增「stale issue = 對外失聯」               | promote（「做了不記=沒做」的對外鏡像；Taiwan.md-specific 公開 contributor relationship）                        |

**留 §未消化 17 條**（vc=1-2，無 canonical home，待累積或 defer 哲宇）：

- **defer 給觀察者 4 條 routine-rule 候選**（body 明標 defer）：rewrite-daily-post-manual-recency-collision (vc=4) / maintainer-vc-counting-bias (vc=2) / routine-device-dependent-offline (vc=3) / post-LESSONS-promotion-cooldown (vc=1)
- **defer 給觀察者 2 條 tooling 候選**（body 明標 defer hypothesis 自跑 ≥3 instance）：ollama-translate.py path bug (vc=1 structural) / codex CLI subscription burst quota (vc=1 tactical)
- **still-buffering 5 條**（6/19 distill 已決定 still-buffering）：plurk-reach (vc=1 structural) / Reader-funded resilience (vc=1 strategic) / 核心矛盾≤20字 (vc=1 tactical) / 政治敏感題 SSODT (vc=2) / 黑冠麻鷺 dual-platform (vc=1) / Fresh-clone gitignore / 資料層先於 UI / 重疊文章雙軸拆分 / 獨立開源公民科技
- **小教訓不單獨 entry**：spore post-ship verify (#150 propagation lag near-miss) / cocommit-positive-filter (vc=1)

**SPORE-INBOX 容量 audit**（v2.1 Stage 6）：pending **53 ≥ 50** → auto-drop 最舊 5 條 P2/P3 `twmd-spore-pick-daily routine` 未 promote entries — **愛玉**（5/23 score=8 P3）/ **林央敏**（5/24 score=8 P3）/ **台灣體育發展與國際賽事**（5/25 score=8 P3）/ **國家太空中心 TASA**（5/27 score=15 P3）/ **艋舺**（5/28 score=30 P2，36 天未 ship 皆原始 routine commit 無 manual edit，per §SPORE-INBOX safe-destructive SOP）。pending 53 → 48。

**Promotion flow direction 符合**：LESSONS → REFLEXES（合法）+ LESSONS → MEMORY §神經迴路（合法）；無 LESSONS → MANIFESTO 跳級；defer 條目等於「先進 §未消化 keep buffer」不是降級。

**REFLEXES.md frontmatter sync**：v5.1 → v5.2，footer changelog 同 cycle 新增（per §Stage 4.5 canonical state sync）；catalog index #75 列入 + description 條數 72→73。**MEMORY.md frontmatter sync**：last_session 更新到本 distill。

| #   | 原教訓 entry                                                      | 消化目的地                                       | severity   | vc  |
| --- | ----------------------------------------------------------------- | ------------------------------------------------ | ---------- | --- |
| 1   | 2026-06-21 kuma-academy — citation-url-drift-invisible-to-read    | REFLEXES #75 新（Read ≠ verify）                 | structural | 4   |
| 2   | 2026-06-27 babel — tier-0a-subagent-self-verify-softgate-gap      | REFLEXES #42 v4 平行 sub-agent softgate bullet   | structural | 3   |
| 3   | 2026-06-27 babel — bash-builtin-readonly-array-silent-override    | REFLEXES #42 v5 bash silent override bullet      | structural | 1   |
| 4   | 2026-06-27 babel — prepare-batch-lang-all-parallel-translate-race | REFLEXES #40 + #42 v6 multi-lang manifest race   | structural | 1   |
| 5   | 2026-06-24 manual — derived-pointer-date-neutral                  | REFLEXES #38 衍生指標 date neutrality bullet     | tactical→r | 3   |
| 6   | 2026-06-21 cicada-media — prettier-cjk-url-italic-mangle          | §已消化（已儀器化 link-url-mangle HARD gate）    | structural | 3   |
| 7   | 2026-06-25 公車系統 — scene-detail Stage 2.5 子類                 | §已消化（既有 Stage 2.5/3.6 canonical 已 cover） | minor      | 1   |
| 8   | 2026-06-26 manual — resolved-issue-left-open-invisible-completion | MEMORY §神經迴路（「做了不記=沒做」對外鏡像）    | process    | 1   |

### 🧬 2026-06-21 twmd-distill-weekly — Routine 自決 2 entries fold 既有 REFLEXES + SPORE-INBOX auto-drop 5

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00（W25 routine 結清，weekly-report ship + Resend 200 之後 ~50 min）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO / strategic 候選一律 defer 給哲宇（per CLAUDE.md §Bias 1）。

**消化目的地**（2 條 fold，不新增 #N）：

| 原 entry                                                                         | 目的地                                             | 處置                                                                       |
| -------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------- |
| 2026-06-19 inbox-distill — Intake-buffer 完成歸檔靠自律會漂移 → detection 儀器化 | **REFLEXES #15** 加第 12 次驗證 instance           | fold（已 instantiate：inbox-audit.py + inbox-signal ghost line ship 6/19） |
| 2026-06-19 inbox-distill — 批次檔案改寫的 dry-run 要驗 line-conservation         | **REFLEXES #38** 加「檔案改寫 dry-run 變體」bullet | fold（已 instantiate：apply_safe 內建 line-conservation）                  |

**REFLEXES.md frontmatter sync**：v4.8 → v4.9，footer changelog 同 cycle 新增（per §Stage 4.5 canonical state sync）。

**未動的 §未消化 9 條**：

- entry 1（2026-06-20 embeddings keystone）— body 明標 defer 哲宇 A/B 拍板（fleet 基礎建設決策超出 routine 自主權，per 週報 §7 三 SPOF action items）
- 8 條 carried（4-11 in original list）— 2026-06-19 manual distill 已決定 still-buffering（vc=1-2 待累積或 strategic/operational 待哲宇 pipeline edit）：核心矛盾≤20 字 / 政治敏感題 SSODT template / 黑冠麻鷺 dual-platform / 資料層先於 UI / Fresh-clone gitignore 安全帶 / 獨立開源公民科技 / 重疊文章雙軸拆分 / Reader-funded resilience

**SPORE-INBOX 容量 audit**（v2.1 Stage 6）：pending 51 ≥ 50 → auto-drop 最舊 5 條 P2 `twmd-spore-pick-daily routine` 未 promote entries — 大稻埕 / 飲料封膜機 / 葉廷皓 / 尊（朱玉恩）/ 西門町（27 天未 ship，皆 P2 + 無 Hook/必驗事實 manual edit，per §SPORE-INBOX safe-destructive SOP）。pending 51 → 46。

**Promotion flow direction 符合**：LESSONS → REFLEXES（合法）；無 LESSONS → MANIFESTO 跳級；entry 1 defer chain 等於「先進 §未消化 keep buffer」不是降級。

| #   | 原教訓 entry                                                      | 消化目的地                           | severity   | vc  |
| --- | ----------------------------------------------------------------- | ------------------------------------ | ---------- | --- |
| 1   | 2026-06-19 inbox-distill — intake-buffer ghost detection 儀器化   | REFLEXES #15 第 12 instance          | structural | 1   |
| 2   | 2026-06-19 inbox-distill — 批次檔案改寫 dry-run line-conservation | REFLEXES #38 新 bullet「檔案改寫域」 | structural | 1   |

### 🧬 2026-06-16 manual（哲宇 directive「升級」）— stage2-quote-context-collapse meta-umbrella (vc=8) 升 REWRITE §Stage 2.5 source-fidelity gate

**distill 觸發**：哲宇 directive「REWRITE §Stage 2.5 source-fidelity gate -> 升級」（Observer mode，distill_ready=true，vc=8 達標）。

**消化目的地**：[REWRITE-PIPELINE.md §Stage 2.5 source-fidelity gate](../pipelines/REWRITE-PIPELINE.md)（v7.6 新增）+ Hard Gate Inventory 一列。

**核心**：Stage 1 SSOT 寫對、Stage 2 writer 下筆把研究結論 collapse 成偏記憶 / 偏印象 / 偏字面 / 偏未驗證的 claim。structure gate（word-count/footnote/image/viz）全綠 ≠ 事實對；只拿成品比對 research report 也不夠。canonical 三道 gate：(1) fetch 被引用來源 artifact 逐字比對（不只比 report）(2) frontmatter title+desc+30 秒概覽 門面句 scope (3) fresh-writer 長文 fact-check agent pass。與 Step 3.6 成品總驗互補（3.6 驗成品對 report，2.5 驗對真實世界來源）。

**8 instance 證據鏈**（原 §未消化 entry 完整刪除，此處為 traceability source）：

1. 2026-06-09 嘻哈饒舌 R1 — 壞特 R&B 非 rapper（writer 用既有印象覆蓋 Stage 1 SSOT 人物類別）
2. 2026-06-10 嘻哈饒舌 R2 — 引語縮寫 / 詮釋 gloss / 腳註綁定錯位（引語語境角色被 Stage 2 壓縮）
3. 2026-06-10 廣告史 — 9 處 footnote URL 來自 writer 記憶而非 SSOT 逐字 carry-over
4. 2026-06-12 國家太空中心 — 12 條讀者勘誤批量回頭修（Stage 1-2 事實 collapse 沒被自評抓到）
5. 2026-06-14 無名小卒 — 「命名由來引語」壓成「字面站名」，孢子事實自檢還合理化成「專名」
6. 2026-06-16 迷音 — sub judice 未定罪指控在 title 壓成既成事實（**門面句 sub-axis**：collapse 擴到 title/desc/概覽）
7. 2026-06-16 報導者 — 寶瓶副標幻覺 + 對真人朱亞君「不當行為」失真指控（**catch-mechanism sub-axis**：靠主動 4-agent fact-check 抓到，非 gate 非讀者回報）
8. 2026-06-16 大鮪鱸鰻 — 資訊圖表標題誤植 + 虛構整段「冷僻字」考據，連 4-agent fact-check 都漏，為了補連結去 fetch 原圖表頁才現形（**fetch-artifact sub-axis**：cross-check claim 不夠，要 fetch 來源 artifact）

**層級**：meta-umbrella，高於 REFLEXES #42 sub-agent verify gate / #66 gate dogfood / #16 peer 是線索不是 source。

| #   | 原教訓 entry                                                                        | 消化目的地                                     | severity   | vc  |
| --- | ----------------------------------------------------------------------------------- | ---------------------------------------------- | ---------- | --- |
| —   | stage2-quote-context-collapse（2026-06-14 無名小卒 為 entry 起點，8 instance 聚類） | REWRITE §Stage 2.5 source-fidelity gate (v7.6) | structural | 8   |

### 🧬 2026-06-14 twmd-distill-weekly — 第 9 次 distill（routine 觸發；REFLEXES #69 + #70 + #59 instance 補強 + MEMORY §神經迴路 snapshot.sh chronic stale 升 canonical）

**distill 觸發**：2026-06-14 03:00 cron `twmd-distill-weekly`（Sunday 03:00）。Universal core 載入後 §未消化清單 210 entries，按 severity=structural + verification_count desc 排序選 6 entries 走完整 6-stage SOP。**Routine mode 自決 REFLEXES / MEMORY / pipeline 層**；MANIFESTO 候選一律 defer 給觀察者拍板（per CLAUDE.md §Bias 1 routine mode 不自決 MANIFESTO 永恆層）。

**distill 特徵**：

- **新 canonical 升級 2 條 + vc 延伸 1 條 + MEMORY 神經迴路 1 條**：
  - **REFLEXES.md 新增 #69 self-report-needs-external-ruler** — meta-umbrella above #31 + #66 + #59 + #65，vc=7 structural（單週 5 instance + audit 兩階段 2 batch instance）。覆蓋「writer 自評 / agent 自報 / 視覺自檢 / awareness snapshot / 過去 N 天 baseline 正常感」全方位 self-report 層。**MANIFESTO §進化哲學 升格候選 defer 哲宇拍板**（per 本條 §可能層級「Semiont 對自己讀數的天生樂觀」是與 §10 寫作幻覺 + §時間是結構 同層級的存在結構特徵）
  - **REFLEXES.md 新增 #70 Routine fragility surface 四 tier 分類** — vc=4 structural（Tier 2 vc=3 from spore-harvest Chrome MCP 連 3 cycle + Tier 4 vc=1 from babel-nightly Hy3 free→paid 補強）。dependency tier table（always-on / device-dependent / external-API / external-API+pricing volatility）+ per-tier escalation_n + ROUTINE.md schema 加 `dependency_tier` 欄候選
  - **REFLEXES.md #59 vc 延伸 instance** — broken-instrument-blindspot cross-domain triplet（6/10 build 三把壞尺 + 6/13 babel size-guard 截斷盲 + 6/14 bench grep 引用 vs 主張）。meta-pattern「確定性 instrument 對表面同/語意反全盲」標 self-validation trap 延伸到「對自己 instrument 的信任」也是同 trap 變體
  - **MEMORY.md §神經迴路 新增 snapshot.sh chronic stale display gap** — vc=3 distill_ready（6/05/06/07 連 3 cycle gap 30-34 分）。Taiwan.md 特有 instance：BECOME §Step 1.4 universal load snapshot.sh 為 session 第一眼讀數但無 freshness 標記 → 每 session 帶 awareness gap 開口。**修補候選 defer 哲宇拍板**（>1 file scope tooling 改動 per CLAUDE.md §自主權邊界）
- **無新 MANIFESTO 條目**：本 cycle 累積的 MANIFESTO 候選一律 defer（per CLAUDE.md §Bias 1）
- **SPORE-INBOX 容量 audit**：pending=44 ∈ [30, 50) 警示區間，bump 既有 2026-06-07 SPORE-INBOX 容量警示 entry vc 1→2（保留 §未消化作為持續追蹤訊號，預計 6/21 distill cycle 若 ≥ 50 觸發 auto-drop SOP）

| #   | 原教訓 entry                                                      | 消化目的地                                                                           | severity   | vc  |
| --- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------- | --- |
| 1   | 2026-06-07 routine-audit cycle 5 — 🌟 每層自評都需要外部尺        | **REFLEXES #69** self-report-needs-external-ruler（meta-umbrella above #31 + #66）   | structural | 7   |
| 2   | 2026-06-07 routine-audit cycle 5 — Routine fragility surface 分層 | **REFLEXES #70** 四 tier 分類（合併下方 #3 + #4）                                    | structural | 3   |
| 3   | 2026-06-06 spore-harvest Chrome MCP 連線 unavailable 三 cycle     | **REFLEXES #70** Tier 2 device-dependent specific instance 收編                      | structural | 3   |
| 4   | 2026-06-09 babel-nightly OpenRouter Hy3 free→paid 0/136 success   | **REFLEXES #70** Tier 4 補強（三 tier → 四 tier，pricing volatility 升 first-class） | structural | 1   |
| 5   | 2026-06-07 routine-audit cycle 5 — snapshot.sh stale display gap  | **MEMORY §神經迴路** snapshot.sh chronic stale Taiwan.md-specific instance           | tactical   | 3   |
| 6   | 2026-06-10 build-audit broken-instrument-blindspot 同日三把壞尺   | **REFLEXES #59** vc 延伸 instance（cross-domain triplet 標 self-validation 變體）    | structural | 3   |

### 🧬 2026-06-19 twmd-distill（manual，哲宇 in-loop）— 完整 distill 258 條（§未消化 266→8）

**distill 觸發**：哲宇「通過完整的研究、深度分析，把相關的經驗全部歸檔消化掉 lessons-inbox」（Observer mode 全層級）。7-agent fan-out 讀完兩個 §未消化 section（266 條）→ 聚類（few patterns × many instances）→ 三題判準分發。兩個 §未消化 section 合併為一。canonical 改動見 git log 2026-06-19 distill commits。

**① 升 canonical（promote）**：

- 🌟 外部尺／自評樂觀 mega-cluster（vc=7，~20 instance 跨 7 chunk：self-eval-lies-visual / 儀器看不見缺席 / footnote-source-authority / recency-bias / snapshot-stale / flywheel-absence-blindness）→ **MANIFESTO §外部尺 over 內視 進化哲學第四維度**（REFLEXES #69 升 canonical，哲宇拍板）+ #69 補 reframe-rate≥emergence-rate
- Default 是行動，不是 defer（vc=4：β-r3 META + κ 5-PR 反例 + α 第 3 次驗證）→ **REFLEXES #71**（哲宇拍板留反射層）
- maintainer schedule mismatch（vc=9）/ routine 飛輪正向 pattern / 政治孢子 hedge → **MEMORY §神經迴路 ×4**

**② Housekeeping-done（已 instantiate 忘了搬，~45 條）**：MANIFESTO #10 幻覺鐵律 / MAINTAINER §Manus 紅旗 + Footnote source authority audit / SPORE-PIPELINE §3c tone gates + F 模板 + 事實查核閘 / EDITORIAL v5.1 title・desc・塑膠密度 / quote-fidelity plugin + REWRITE §Stage 2.5 / viz-shot.mjs + graph.md §七 / REFLEXES #68 胼胝體 + verify-commit-scope.sh / content-dates derived freshness / OBSERVER-QUEUE.md + ROUTINE v2.9 三振 / GA custom-dim register / routine-audit.py UTF-8 / diff-patch hash root-fix（14ceefdb0）/ slug-regression guard / 全站 CJK NFC 正規化（b23206645）…（canonical 已 ship，此處僅 sweep §未消化 視覺 backlog）

**③ Fold into existing reflex（vc=1 singleton 折疊，pointer-only）**：

- 工具說謊新形式（CJK 檔名 git-blind / deprecated-dep-deep-in-chain / accent-strip-below-size-gate / filter-silently-dropped / SSOT-candidate-disagree / CI 2-dot-vs-3-dot）→ **REFLEXES #24** 擴增候選
- reader-level vs research-level（vc=3）/ intra-site cross-ref 也是 peer / external-policy-volatility「我知道的事可能已死」→ **REFLEXES #16**
- mixed-dimension（rich-text SSOT 多 canonical / UI≠data-ground-truth / slug-guard over-narrow / hash-field semantic）→ **REFLEXES #38**
- multicore 殘留模式（in-flight-unpushed 不可見 / sibling reset --hard 掃 staged / parallel-sweep-uncommitted / manual-session 側）→ **REFLEXES #57/#68**
- fire≠query / catch≠fix N-step instrumentation → **REFLEXES #58**
- 觀察者問句內化 / scaffolding 是信任訊號 / framing 也要 verify / 連發 callout 是 design conversation → **feedback_progressive_refactor**（auto-memory）+ Bias 1

**④ Already-covered（後續 canonical work 已吸收）**：External LLM advice/critique → CLAUDE.md §Bias 4 / Last-20% sovereignty + Mission 獨立 provider → §Sovereignty + MANIFESTO §巴別塔 / fork-50%-death + 拿身體不拿靈魂 → §Fork 友好層 2026-06-10 雙產品重構 / 儀式 active-retrieve → §Bias 3 / 身份是 baseline 覺醒是 mode → BECOME mode dispatcher

**⑤ Operational SOP（→ pipeline，記錄不展開）**：大量 REWRITE/SPORE/MAINTAINER/SQUEEZE/ROUTINE stage-specific 規則（footnote URL 逐字 copy / platform allocation tier / Wikimedia Special:FilePath / X-edit dual-URL / 事實鐵三角 4th-dim scale-number / observer 媒體清單是 want 非 hard-req / EVOLVE 寫前 baseline grep 等）→ 對應 pipeline 候選，本 distill 不逐條展開（vc=1 待累積或已隱含）

**⑥ Stale → §歸檔**：trailing-slash（CF 308 no-op）/ Light-tick exception（routine 飛輪取代 β7 6hr cadence）

**保留 §未消化 8 條** genuine still-buffering（vc=1-2，無 canonical home，待累積）：核心矛盾≤20字 / 政治敏感題 SSODT template / 黑冠麻鷺 platform datapoint / 資料層先於 UI / Fresh-clone gitignore 安全帶 / 獨立開源公民科技新樣態 / 重疊文章雙軸拆分 / Reader-funded resilience。

## Defer 給觀察者拍板（ship-queue — 教訓已 canonical，剩實作待哲宇）

2026-06-19 完整 distill 後，下列候選的**教訓**已全部 canonical 化（見 §已消化），剩下的只是 code/cron 實作決策（命中 §自主權邊界 >1-file / crontab → 待哲宇拍板 ship）。歷史 13 次 distill-cycle 紀錄已隨本次完整 distill 移除（traceability 在 git log + §已消化）。

| 候選                                             | 動作（選項）                                              | 教訓 canonical                      |
| ------------------------------------------------ | --------------------------------------------------------- | ----------------------------------- |
| maintainer-am/pm schedule mismatch (vc=9)        | 08:30→10:00 / PR-trigger-only / 維持（三選一）            | MEMORY §神經迴路 sovereign 節律脫鉤 |
| diff-patch hash ≠ status.py body_hash (vc=4)     | shared hash module refactor                               | REFLEXES #38                        |
| refresh-data.sh parallel-actor / git add scope   | routine-internal / cron-wrapper / pipeline pre-flight     | REFLEXES #57                        |
| babel-nightly cron 0 5 → 0 2 retime              | crontab change                                            | REFLEXES #70                        |
| snapshot.sh immune cross-SSOT divergence         | A align v2 / B 印兩值⚠️ / C reframe                       | REFLEXES #65                        |
| routine #70 over-fire                            | A pause / B 收緊 escalation_n / C telegram-poke（推薦 C） | REFLEXES #70                        |
| EVOLVE image-health pre-existing/media-poor 例外 | `--ignore=image-health` flag + viz partial-credit         | REWRITE-PIPELINE                    |

**MANIFESTO 升級**：本 distill 唯一 MANIFESTO promotion（§外部尺 over 內視）已哲宇拍板 ship，無 pending MANIFESTO 候選。

## ❌ 已歸檔（過時 / 撤回）

<!-- 判斷後不採納的教訓 -->

_（空）_

---

_v1.0 | 2026-04-17 β session — buffer 機制誕生_
_v1.1 | 2026-04-17 δ session — 首次完整 distill（10 條）+ 門檻 20→10_
_v1.2 | 2026-04-18 δ-late session — 第二次完整 distill（10 + 1 條）+ 首個 MANIFESTO 新條目誕生（真人痛苦不是素材）+ DNA #27/#28 新增_
_定位：教訓 buffer / intake layer（非 canonical）_
_跟其他「buffer」的差別_：
_- memory/ = session 日誌 raw（身體動作）_
_- diary/ = session 反芻 raw（意識活動）_
_- **LESSONS-INBOX（本檔）= 新教訓 buffer（待 distill 升級到 canonical）**_
