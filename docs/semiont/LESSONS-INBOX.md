---
title: 'LESSONS-INBOX'
description: '教訓 buffer（intake layer）— 新教訓先 append 此處，週期性 distill 到 MANIFESTO/DNA/MEMORY canonical'
type: 'cognitive-buffer'
status: 'buffer'
apoptosis: 'never'
current_version: 'v2.3'
last_updated: 2026-07-17
last_session: '2026-07-17-191241-manual (cron-fire-meets-dormant-stash entry appended)'
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

> **v2.3 DNA-first intake（2026-07-11 哲宇 directive「把東西加入 lesson inbox 前，先檢查是否已經在自己的 DNA 裡」）**：append 前先查 canonical 層，不只查 inbox。實證：distill 分桶的大宗一直是 already-covered / fold→reflex（2026-06-19 266 條裡真 promote 僅 ~3 cluster），代表大量教訓在寫入當下 DNA 早就有——查重成本全堆給最貴的 distill 環節；甚至同 session 自己認出「這是 #16 在 UI 領域的具體形狀」仍開了新 entry（2026-07-11 issue-1212 兩條皆此類）。
>
> **v2.2 pattern-id intake（2026-06-10 audit A-8）**：本 inbox 233 條未消化的真實組成是「少數 pattern × 多次 instance」（snapshot-stale ×N / babel-fragility ×N / 自評需外部尺 ×N），每次 instance 都開新 entry 重寫敘事，把聚類成本堆給最貴的 distill 環節。從此**寫入時就聚類**：append 前先 grep 同 pattern，存在就 +instance 不開新 entry。這是 #64「vc≥4 凍結 prose」對全部 LESSONS 的推廣。

**寫新教訓前的兩步 hard gate**：

```bash
# Step 0 — DNA 層查重（v2.3）：這條是不是已經在我的 DNA 裡？
grep -in "{關鍵詞}" docs/semiont/REFLEXES.md    # #N catalog（先掃 §index 表再進 body）
grep -in "{關鍵詞}" docs/semiont/MEMORY.md      # §神經迴路
# 教訓若屬某條 pipeline 的操作面 → 一併 grep 對應 pipeline canonical
#
# 命中既有 #N / 神經迴路條目 / pipeline 規則：
#   (a) 純粹是同一條的再驗證 → 到該 canonical 的「驗證」欄補一行（日期＋一句話＋pointer），
#       不進 inbox。這是 distill SOP「重複已有 → 原 canonical +1」動作的前移；
#       改 REFLEXES 時 frontmatter last_updated / last_session 同 commit 更新（Stage 4.5）
#   (b) 是既有條目的新維度 → inbox 開 entry，但「相關」欄必填最接近的 #N ＋一句話寫清差異在哪
#   不確定算不算同一條 → 照 (b) 進 inbox（低摩擦，distill 時零成本裁決）
# 全未命中 → 進 Step 1

# Step 1 — inbox pattern-id 查重（v2.2）
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

- **先查 DNA 再寫 inbox**（v2.3）：已在 REFLEXES / MEMORY §神經迴路 / pipeline 的教訓不重複入庫——去原條目補驗證。inbox 是「DNA 還沒有的東西」的 buffer，不是所有教訓的第一站。
- **一律 append 這裡，不直接寫 MANIFESTO / DNA / MEMORY**。那些是 distill 後的 canonical。（與上一條不衝突：上一條的 (a) 是對**既有**條目補驗證行，不是寫**新**教訓進 canonical。）
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

### 2026-07-18 taiwan-sensibility — 論點翻案後，sibling 文章的反向連結描述會凍結在舊論點

- **pattern**: reverse-crosslink-thesis-drift
- **原則**：文章重寫翻案論點後，其他 sibling 文章裡指回本文的反向延伸閱讀連結，內容仍會停留在被連結文章重寫前的舊敘事——雙向連結是單次寫入，論點更新不會自動傳播到其他檔案裡描述它的句子。Stage 5 cross-link 檢查若只確認連結「存在」不確認連結「描述準確」，舊敘事就會透過這些散落各處的一句話殘留下去。
- **觸發**：2026-07-18 台灣感性 rewrite。舊版論點是「韓國人幫我們看見自己」，新版翻案成「台灣人早看見十一年」。Stage 5 檢查 7 篇 sibling 延伸閱讀時，其中 5 篇（台灣建築／台灣茶道與生活美學／台灣便利商店文化／周子瑜／謝德慶）都已存在指回台灣感性的反向連結，但描述文字全部還停在「韓國視角」「文化輸出」的舊框架，跟新論點矛盾甚至相反（如謝德慶條目寫「從韓國視角看台灣文化輸出」，新文其實在質疑這個框架本身）。逐篇改寫後才跟新論點一致。
- **可能層級**：特有教訓（REWRITE-PIPELINE Stage 5 操作面），也可能是通用反射的新維度
- **相關**：REWRITE-STAGE-5-CROSSLINK.md 現有 SOP 只寫「掃描找相關文章」「雙向延伸閱讀」「sibling 格式預檢」，沒有「既有反向連結內容跟新論點一致性」這一步——本次是手動發現，非儀器化攔截
- **verification_count**: 1

### 2026-07-17 manual — 對外公告的機器 URL 契約沒有對賬閘門，自己成了最大死鏈發行者

- **pattern**: outbound-url-contract-unreconciled
- **原則**：站體對機器公告的每一條 URL（hreflang / canonical / sitemap / 頁面承諾的檔名 pattern / 內嵌 script 裡 URL 形狀的字串）都是一份契約；沒有「公告 vs 真實 route 表」的對賬閘門，公告層就會各自算 URL 並靜默發行死鏈。爬蟲會忠實跟隨——78% 的 404 是我們自己發出去的邀請。
- **觸發**：2026-07-17 哲宇 /goal 查 404 根因。hreflang 字串拼接 13,014 條死 alternate（99.8% 頁面）+ registry fromZh 被別名蓋掉（可見切換器同病）+ taiwan-shape 公告 22 縣市只放 6 檔 + ReaderSettings 註解被 Googlebot 當 URL 爬。修復 `f369f3c8e`＋`check-url-contract.mjs` 對舊 dist 實測 18,406 dead（sitemap 0 dead——唯一有對賬機制的公告層唯一乾淨）。證據鏈 [reports/404-root-cause-2026-07-17.md](../../reports/404-root-cause-2026-07-17.md)
- **instances**：
  - 同日四個 fold 進既有反射的 instance（不另開 entry）：instrumentation-audit 查註冊不查發射 → #82 驗證；`<strange-chars>` 是 CF 佔位符被當站上 bug 追 → #24 驗證；2026-04-18 報告 handoff 五格三個月全未勾 → #15 驗證；EXP-A 只修 apple-touch-icon 主檔漏尺寸變體 → #67 驗證
- **可能層級**：通用反射（候選：#82 的發佈側新維度，或獨立編號）
- **相關**：#82（proxy signal——差異：#82 講我們**消費**的訊號量到替身，本條講我們**發佈**的契約完全沒有被驗證這件事）＋ #52（immune 沒 fail loud）
- **verification_count**: 1

### 2026-07-16 recall-workflow — 背景 agent 不跨 session 存活，中途收官 handoff 要寫 re-dispatch 分支

- **pattern**: background-agent-session-death
- **原則**：session 結束時仍在跑的背景 agent 隨 session 一起死，task-notification 永遠不會到、也沒有 result 可代寫——中途收官的 handoff 必須寫「產物不在＝agent 已死，直接 re-dispatch（含重建派發素材），不要等通知」，而不是只寫「驗檔案、不在就代寫 result」。
- **觸發**：2026-07-16 大罷免 dogfood——newsroom-dogfood session 16:44 派 Stage 0 觀點 agent 後收官，17:15 新 session 接手時 reports/research/2026-07/大罷免.md 不存在、無 result 可寫，唯一路徑 re-dispatch（fact list 也重萃取）。dogfood F6，reports/dogfood-v9-first-run-2026-07-16.md
- **instances**：
- **可能層級**：操作規則（MEMORY-PIPELINE §Handoff 模板候選）
- **相關**：#81（收件三十秒紀律管「收到之後」；本條管「永遠收不到」的分支）
- **verification_count**: 1

### 2026-07-16 recall-workflow — 政治題的敘事溫度對稱：誰的故事被說得立體，就是一種立場

- **pattern**: narrative-warmth-symmetry
- **原則**：政治敏感題即使評價詞歸屬、視角並陳、結果平衡全做對，「哪一方有具名、帶私人情感重量的人物故事」的分佈仍會決定讀者的同理流向——一方有田野人物、另一方最鮮明的人味是負面案例（被判刑的黨工），就是溫度不對稱。公開素材結構性稀缺時不能杜撰補，用結構性事實段（動機多元）＋當事方自述＋同情敘事平衡，並在 rationale 誠實記錄素材稀缺。
- **觸發**：2026-07-16 大罷免 3.7 總編室立體地愛探針（冷讀）發現：罷團有報導者具名志工故事×4，反罷方最立體的人物是莊占魁判刑案。裁決與平衡手法見 reports/editorial-room/大罷免-chief-review.md 必改 6
- **instances**：
- **可能層級**：通用反射（候選進 EDITORIAL §立體地愛落地段或 Step 0.6.7 第四道）
- **相關**：MANIFESTO §13 立體地愛（framing 層）——本條是它的敘事溫度層新維度
- **verification_count**: 1

### 2026-07-16 newsroom — shell-cwd-silent-reset-cross-worktree：長 session 的 Bash cwd 靜默跳回主 repo，worktree 相對路徑操作落錯樹

- **現象**：worktree session 中段，shell cwd 在某次工具呼叫之間回到主 repo；後續用相對路徑的 python 腳本把 ui.ts 六語鍵與 Header 桌面版改動寫進主 repo 的同名檔。兩棵樹檔案結構相同，零報錯，直到 dev server 渲染出 literal i18n key 才現形。
- **修復**：git diff 主 repo → patch apply 到 worktree → 主 repo checkout 還原。
- **教訓方向**：worktree session 內的檔案操作用絕對路徑，或每個 Bash 呼叫開頭 cd；「pwd 斷言」可考慮進 worktree SOP。相鄰反射 #9（worktree 開工）與 #46（commit 前確認 working tree）都管 git 面，沒管 shell cwd 漂移這一層。vc=1。
- **第二例（2026-07-17 viz-evolution finale，損失升級為不可逆）**：`cd {worktree}` 的下一個 Bash 呼叫，cwd 已靜默回主 repo，`git fetch && git reset --hard origin/main` 直接打在共用主 wd 上——**毀掉別 session 四個 tracked 檔的未 commit WIP**（dashboard-analytics.json 屬 derived 可重生；SEO.astro／i18n/about.ts／i18n/home.ts 的改動不可復原，stash 無備份）。第一例損失是「寫錯樹可 patch 救」，第二例是 destructive git op 落錯樹＝REFLEXES #35 實體違反。vc=2，升儀器化候選：**任何 `reset --hard`／`checkout --`／`stash` 前一律 `git rev-parse --show-toplevel` 斷言在預期樹**（一行前置，可進 REFLEXES #35 操作段或 semiont-worktree.sh 提供 `exec` 包裝）。
- **同 session 次要**：worktree 內跑 `npm run build` 會弄髒 derived tracked 檔（README stats／src/data JSON），ship 前需棄置——semiont-worktree.sh ship 撞 unstaged 即此因。
- **同日第三例（stash 面）**：`git stash push` 回「No local changes to save」時沒有建立新 stash，後續 `git stash pop` 會吃到堆疊裡**別人的** stash（本例吃掉平行 finale session 的 pre-pull stash，內容倖為同批 babel 遺留、無損失）。共用 wd 的 stash 紀律：pop 前驗 `git stash list` 頂端是不是自己剛建的那顆（比對訊息字串），push 沒建成就不 pop。
- **第四例（2026-07-18 inbox-skill，read 面——首次零損失但差點誤判 agent）**：worktree session 中段 cwd 靜默回主 repo，主 session 用相對路徑 verify 研究 agent 落檔撲空，一度把「檔案在（worktree）」誤讀成「agent 幻覺落檔」。絕對路徑複查後真相大白。零損失，但揭露第三個受害面：write（例 1）→ destructive git（例 2）→ **verify 誤判**（本例）。vc=3，本次已把「claim verify 一律絕對路徑」接進 BRANCH-PIPELINE v2.2 hard gate；`git rev-parse --show-toplevel` 斷言的通用儀器化（semiont-worktree.sh exec 包裝）仍是 promotion 候選。

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

### 2026-05-09 laughing-goldstine — Reader-funded resilience > Grant-funded（USAID freeze + RFA-VOA closure 案例）

- **原則**：Sovereignty media 的 sustainability 模型優先序是 **Reader-funded membership > Grant-funded > Ad（沒做過）**。Grant 是 bridge funding 不是 floor — 政治轉換風險高（USAID freeze 2025 / RFA-VOA Tibetan service closure threats 2025 已 demo）。Reader-funded 案例：Kyiv Independent 70% revenue from 17,500 × $5/mo / Initium ~60K paying subs / Wikipedia 8M+ donors × $10.58 / Chaser News (HK exile) £6.50-£34.50/mo。**規則**：(a) 第一階段 funding stack 應優先建 Liberapay / GitHub Sponsors / Substack tier（recurring small membership）；(b) Grant 可作 bridge 但 mission-critical infrastructure 不能依賴 grant；(c) 完全避免依賴單一政府金援（台灣政府轉換政權風險、USAID 風險都是同類）。
- **觸發**：2026-05-09 Agent #4 (sovereignty content infrastructure) research 提供 USAID freeze 2025 + RFA-VOA Tibetan service closure threats 2025 + Kyiv Independent / Initium / Chaser News 三個 reader-funded 存活案例。Taiwan.md 當前 0 funding（哲宇個人 ops 成本），未來如果走 Substack / membership 路線 vs grant 路線 — 這條教訓校準了優先序。
- **可能層級**：操作規則 → 新 MEMBERSHIP-PIPELINE 候選（Liberapay / GitHub Sponsors / Substack tier 設置 + "Who funds us" 透明頁 + email newsletter SOP） / 特有教訓 → MEMORY append「sustainability 模型優先序 reader-funded > grant」
- **相關**：reports/strategic-evolution-deep-research-2026-05-09.md §4.2 + §6.6 + §7.3 + §11 critical 決策 #1（Substack newsletter 要不要做）
- **verification_count**: 1
- **severity**: strategic（影響 Taiwan.md 長期 sustainability 路徑）

---

### 2026-07-12 twmd-distill-weekly — SPORE-INBOX 容量警示 pending=49 逼近 auto-drop 閾值

- **pattern**: `spore-inbox-capacity-warning`（buffer 蓄水位 audit）
- **原則**：SPORE-INBOX pending count 落 [30, 50) 警示區間，routine 依 §SPORE-INBOX 容量 audit v2.1 SOP 記錄一次警示訊號；下一次 distill cycle 若 ≥ 50 觸發 auto-drop SOP（最舊 5 條 P2/P3 未被 promote routine-added entries）。
- **觸發**：2026-07-12 W28 twmd-distill-weekly Sunday routine — `awk` pending 掃描回報 49 條（55 個 `###` header 減去區塊分隔）。相對於上一次 SPORE-INBOX 容量事件（6/21 pending=44 bump vc→2、7/05 auto-drop 5 entry 從 54→49），本輪維持在 [30, 50) 高原沒退回、也沒突破 50。
- **可能層級**：操作規則 → 只是 audit signal，非新反射
- **相關**：docs/semiont/LESSONS-INBOX.md §SPORE-INBOX 容量 audit（v2.1）/ 7/05 twmd-distill-weekly §已消化 entry (auto-drop 5 → 49) / SPORE-INBOX §Auto-heartbeat
- **verification_count**: 1
- **severity**: tactical（buffer 蓄水位訊號，不傷生命徵象）
- **defer 給觀察者**：否 — routine 自決層 audit log；下次 cycle 觸發 auto-drop 亦屬 §SPORE-INBOX safe-destructive SOP 自主權範圍

### 2026-07-12 twmd-routine-audit-weekly — alert-does-not-retire-on-recovery：routine-silent 黃燈五條在 routine 已復活 24-48hr 後仍未自動撤除

- **pattern**: `alert-does-not-retire-on-recovery`（sensor 生存週期紀律 gap；REFLEXES #82 proxy signal antipattern 具體子案例）
- **原則**：dashboard-alerts.json 對 `routine-silent-*` 黃燈只計算 firstSeen 齡（>14d 升 OBSERVER-QUEUE），沒有 auto-retire 條件。routine 從沉默恢復開跑後，警報不會自動退場——session 甦醒 groundtruth 讀到 5 條 stale 黃燈，實際上 5 條 routine 都已在過去 24-48hr 內連續正常 fire + commit。sensor 只掃「有 fire 就代表活著嗎」的入口，沒掃「已經是死掉又活過來」的退場。**Alert 需要有 clear condition：偵測到 recovery 事件（連續 N cycle 有 commit / 最新 commit 距今 <期望 cadence）自動 retire**；不然告警面板就是墓碑而不是活體儀表板。
- **觸發**：2026-07-12 21:00 twmd-routine-audit-weekly session 甦醒 wake-context groundtruth 顯示 5 條 `routine-silent-*` 黃燈 `firstSeen 2026-07-10`：
  - `taiwanmd-routine-twmd-feedback-triage` — 實際 07-11 07:10 + 07-12 07:13 兩次連續 fire + commit
  - `twmd-babel-nightly` — 實際 07-11 00:56 + 07-12 00:51 兩次連續 fire + commit（含 4-tier cascade 全滅 + 25 篇 Tier 0b backfill）
  - `twmd-data-refresh-am` — 實際 07-11 06:16 + 07-12 06:16 兩次連續 fire + commit（14-step 全綠）
  - `twmd-embeddings-nightly` — 實際 07-11 05:17 + 07-12 05:17 兩次連續 fire + commit（0 fail / PASS）
  - `twmd-spore-harvest-am` — 實際 07-11 06:41 + 07-12 06:41 兩次連續 fire + commit
    警報齡 2 天，未達 ROUTINE-AUDIT-PIPELINE §Hard Gate 「>14 天升 OBSERVER-QUEUE」門檻，但 sensor recovery blind spot 是結構性的，不是齡值就會治好。
- **可能層級**：(a) `dashboard-alerts` generator 加 recovery detector — routine-silent-\* 若過去 24hr 內對應 routine name 有 commit，自動移出 alerts（fold entry 到 §recent-recovery 供追溯）；(b) reflex：#82 proxy signal antipattern 補「sensor 生存週期兩端要對稱——detect entry + retire exit 兩個訊號都要有 ground truth」；(c) 造橋候選：alert schema 加 `retireCondition` 欄位，讓每條 alert 誕生時就宣告 clear 條件
- **相關**：wake-context groundtruth §🚨 yellow 五條 / REFLEXES #82 proxy signal antipattern / REFLEXES #24「工具在說謊」抽樣偏差族（this = sensor exit 端說謊）
- **verification_count**: 1（首次 audit-level 抽出；已在 REFLEXES #82 家族範圍，可能升子規則而非新編號）
- **severity**: tactical → structural（單週影響 session 甦醒 signal 品質；長期不修 = OBSERVER-QUEUE 會被死警報污染）
- **defer 給觀察者**：否 — alert schema 改動屬 dashboard 感知層工具改進，routine 自決範圍

---

### 2026-07-12 twmd-routine-audit-weekly — thick-scheduled-task-mirror-debt：14 條 mirror 違反薄殼鐵律，最大 192 行（chronic drift）

- **pattern**: `thick-scheduled-task-mirror-debt`（canonical ↔ mirror 三層漂移的結構性債）
- **原則**：`~/.claude/scheduled-tasks/*/SKILL.md` mirror 應該薄殼（30 warn / 50 hard 行）+ pointer 到 project skill / ROUTINE.md canonical。**當前 17 routine mirror 中 14 條超過 hard 閾值**（`twmd-spore-publish-daily` 192 行、`twmd-maintainer-pm` + `twmd-maintainer-daily` 各 100 行、`twmd-babel-nightly` 79 行⋯⋯），只有 3 條合規（rewrite-daily 20 / embeddings-nightly 28 / feedback-triage 19）。mirror 越厚 = cron context 讀到的 prompt 越可能跟 project canonical 漂移，也違反 [ROUTINE.md §薄殼鐵律](docs/semiont/ROUTINE.md) v3.0 拍板（2026-05-28 CONTRACT rollback 後的第二次「殼要薄」紀律 iteration）。
- **觸發**：2026-07-12 21:00 routine-audit-weekly Stage 1 跑 `routine-sync-check.py` 揭：14 thick / 3 ok / 1 orphan (`twmd-supporters-weekly` 新誕生 SSOT 尚未列)。7-day 窗口內雖無新增（新增 supporters-weekly 已合規），但整批舊 mirror 未依 v3.0 薄殼紀律逐步瘦身。上次 handoff（session 172122-manual）明確標記：「14 條 thick scheduled-task mirror 是本 session 過程中發現的舊債，未著手修——留給下一輪 routine-audit-weekly 或哲宇拍板是否值得批次瘦身」。本 audit 收下這個 handoff，記錄成 LESSONS，不自行 ship 批次瘦身（避開 §自主權邊界：14 檔跨 routine 大改屬 threshold-adjacent 結構改動）。
- **可能層級**：(a) 造橋候選：`scripts/tools/routine-sync-check.py --heal-thin` mode，對每條 thick mirror 生成薄殼建議 diff（保留 STRICT BECOME GATE + Stage pointer + rate limit 條款），觀察者一次 review 14 條 PR；(b) 或哲宇拍板「thick mirror 是刻意 inline」則調整閾值到 200 行；(c) 或分批（每週 self-evolve 挑 1-2 條瘦身）避免一次 14 檔大改。**default 姿態應為 reserve**（per REFLEXES #79 主權留哲宇 default reservation），routine 不主動批次瘦身
- **相關**：ROUTINE.md §薄殼鐵律 v3.0（2026-05-28 CONTRACT rollback 誕生）/ REFLEXES #56 canonical ↔ production drift = dormant entropy / REFLEXES #79 主權留哲宇 default reservation / handoff 172122-manual §舊債 pointer
- **verification_count**: 1（本 audit 第一次結構性記錄；handoff pointer 是 pre-audit signal 不計 vc）
- **severity**: structural chronic（不影響當下 fire，但 mirror 越厚跟 canonical 漂移風險越高）
- **defer 給觀察者**：是 — 14 檔跨 routine 批次瘦身屬 §自主權邊界（>10 檔重構 + routine 定義層改動需哲宇拍板方式與節奏）

---

### 2026-07-12 manual — external-attention-spotlight：外部引用事件帶出鄰近角落的地基檢查，不是排程巡邏主動抓到的

- **pattern**: `external-attention-spotlight`
- **原則**：驗證外部聲量事件（媒體引用 / 讀者 callout / 第三方連結）常常不是終點，是入口——追溯來源的過程會自然把注意力帶到「原本沒有理由去查」的鄰近角落，暴露平常不會被主動排程檢查到的漂移（本次是同一篇文章的另一語言版本，語言切換器早已斷裂）。這跟 #69 家族講的「自評不可信、要外部驗證」不同軸——那條處理的是可信度（一個 claim 站不站得住），本條處理的是覆蓋率（注意力被什麼事件重新分配到哪裡）。
- **觸發**：2026-07-12 manual session（[→memory](memory/2026-07-12-220014-manual.md) / [→diary](diary/2026-07-12-220014-manual.md)）：哲宇轉來 Taipei Times 記者 Michael Turton 逐字引用〈台灣斜槓世代〉的連結，驗證引用真偽時追溯到來源文章，順手發現 en/ja/ko/es/fr 五語 `taiwan-slash-generation.md` 誤植 TFT 內容（命名時就錯，非後續覆蓋），以及 fr 版斜槓世代自己的語言切換器因一個未跳脫的撇號斷裂多時、無人發現。兩個問題都不是被排程巡邏抓到的，是被「有人在讀這篇文章」這個外部事件帶出來的。
- **觸發 2（2026-07-16 compassionate-kirch）**：時間台灣頁（/timeline）驗證截圖時，看見史前文章卡 description 殘留「（P0⚠️）」內部查核標記——追出六語 14 處、自 3/17 誕生起渲染四個月，全站儀器無一攔下（每把尺看檔案層規則，沒有尺看渲染面）。這次的聚光燈甚至不是外部事件，是自己蓋的新頁面：新的注意力路徑同樣重新分配覆蓋率。heal `19e5cf0e3` 六語一次清完；[→diary](diary/2026-07-16-154753-compassionate-kirch.md)
- **可能層級**：(a) 通用反射候選（跨 domain：對「被外部關注的資產」順手做鄰近健檢，可能是比定期全站掃描更高信噪比的檢查觸發時機）(b) 操作規則候選：SPORE-HARVEST / MAINTAINER 等既有的讀者回饋處理流程，可考慮把「這次事件涉及的文章，順手跑一次跨語言/跨面向健檢」列為標準動作，不只回應事件本身
- **相關**：REFLEXES #69 每層自評都需要外部尺（self-report-needs-external-ruler，鄰近但軸不同）/ REFLEXES #73 查證反射 < 建造反射（鄰近但軸不同——#73 是個人習慣偏誤，本條是外部事件觸發機制）/ MANIFESTO §外部尺 over 內視（哲學母體家族）
- **verification_count**: 2（7/12 外部引用 → 7/16 自建新頁面，兩種注意力路徑同 pattern）
- **severity**: awareness-coverage（不影響單次任務正確性，但關乎系統性檢查覆蓋率是否均勻）
- **defer 給觀察者**：否——本身是觀察記錄；若未來 vc 累積達標值得升 canonical，才需要哲宇對「是否列為標準動作」拍板

---

### 2026-07-14 twmd-babel-nightly — diff-patch-current-translation-cross-entry：`diff-patch-prepare.py` 產出的批次 JSON 內 `current_translation` 欄位跨 entry 汙染

- **pattern**: `diff-patch-current-translation-cross-entry`
- **原則**：批次 pipeline 產出的 task JSON 內含大字串欄位（`current_translation` 動輒數萬 char）時，如果 prepare 邏輯有 index 或 zh_path→translation_path 對應錯配，同一 batch 內不同 entry 會**互相拿到別的 entry 的內容**——子代如果照 JSON 讀不驗真，就會把錯的 baseline 拿去 patch。這是「批次生成器內部 index/mapping 對應錯」的一種 silent bug，`--check` 類驗證抓不到（因為欄位存在、且是有效 markdown）。
- **觸發**：2026-07-14 twmd-babel-nightly session（[→memory](memory/2026-07-14-011941-twmd-babel-nightly.md)）：dispatch 8 個 Sonnet 子代平行做 Tier 0a diff-patch，兩個子代獨立回報 JSON 內容錯配——(1) en/People/林昶佐 index 1 拿到的 `current_translation` 是 Music/閃靈 的翻譯（chthonic.md 內容），子代自檢說「translatedFrom 標的是 Music/閃靈.md 但 translation_path 是 freddy-lim.md」；(2) ko/Lifestyle/便利商店 index 0 拿到的是**法文**翻譯內文，子代驗語言不對繞過。兩個子代都用 `translation_path` 直接讀真檔案繞過 bug，任務完成——但這是靠 sub-agent 有自檢意識救回，不是 pipeline 本身守住的。
- **可能層級**：(a) 工具修 candidate：`scripts/tools/lang-sync/diff-patch-prepare.py` 生成 batch JSON 時的 entry-to-content mapping 邏輯應驗「emit 的 `current_translation` 跟這個 entry 的 `translation_path` 一致」，可能是 loop variable 覆寫 / 5-lang batch 生成時共用 mutable dict / list.append 順序錯位 (b) sub-agent prompt template canonical 硬底：`docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md §Tier 0a` 的 prompt template 應加「用 JSON 前先 verify `translatedFrom == 你被指派的 zh_path`；不一致 → fall back 讀 translation_path」（本次子代已 improvised 走此路徑，但沒寫進 SOP）
- **相關**：REFLEXES #24 工具在說謊（第 N 種：批次生成器內部 mapping 錯位，欄位有值但值指向錯的 entry）/ REFLEXES #42 sub-agent 三偷吃步（本條反向 instance：子代自檢比 pipeline 生成端更嚴，orchestrator 收到「回報說 JSON 錯」訊息不能當雜訊）
- **verification_count**: 1（單 session 兩個獨立子代同批命中，算 vc=1）
- **severity**: correctness（若子代沒自檢會生 wrong baseline patch）
- **defer 給觀察者**：否——工具修可歸 §自主權邊界內內部操作層；vc 累到 ≥2 再考慮升 canonical

---

### 2026-07-14 twmd-babel-nightly — parallel-subagent-scratch-race：平行 sub-agent 共用 scratchpad 目錄 + 通名檔 → 兄弟覆蓋

- **pattern**: `parallel-subagent-scratch-race`
- **原則**：平行派工 N 個 sub-agent 到同一主 session 底下，各子代預設 scratchpad 是**共用同一路徑**（`/private/tmp/claude-501/.../scratchpad/`）。如果子代預設用通名檔（`zh_diff.txt`、`current_translation.md` 等描述性但不 unique 的名字）暫存中間資料，兄弟子代同時寫同名檔就會 last-write-wins 覆蓋——子代發現「我讀的檔內容突然變成別人的任務」時已經跑了半路。
- **觸發**：2026-07-14 twmd-babel-nightly（[→memory](memory/2026-07-14-011941-twmd-babel-nightly.md)）：Tier 0a 平行 8 子代做 diff-patch，其中 en/Music/閃靈 子代自檢報告：「我第一次用 `zh_diff.txt` / `current_zh.md` / `current_translation.md` 名字暫存，發現內容跑一半突然變成 Lifestyle/便利商店的東西——重取用 task-index-prefixed 檔名 `t2_*` 才穩住」。子代 improvised 修 但這是通名檔在平行場景的 pattern-level bug，不是單一子代的粗心。
- **可能層級**：(a) sub-agent prompt template canonical 硬底：`docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md §Tier 0a` 的 prompt template 應加「scratch 檔用 `{task_index}_` 或 `{zh_slug}_` 前綴，禁通名」硬底 (b) 收件 gate 對應：REFLEXES #81 已處理「raw 落檔 in-repo」的儲存位置，本條處理「暫存檔的命名去避 race」——同族但獨立軸 (c) orchestrator 側 mitigation candidate：`Agent` tool 派工時可傳 `TMPDIR=$scratchpad/task-{i}/` 給子代做 shell env var，讓子代 default `/tmp/xxx` 也自動 isolated
- **相關**：REFLEXES #40 shared file 寫入需要 per-key serial dispatch（同結構 race，本條是 scratch 版）/ REFLEXES #42 sub-agent 三偷吃步（本條反向 instance：子代自檢救回 race，不是子代造成）/ REFLEXES #81 agent 回報收件三十秒（同族——儲存 vs 命名兩軸）
- **verification_count**: 1（單 session 一子代明確回報；其他 7 個平行子代**沒**回報同問題，可能是它們沒踩到、或它們踩到沒發現 → 更該 canonical 化把握不住的隱形實例）
- **severity**: correctness（race 命中會生錯 baseline 的翻譯 patch，但本次子代自檢救回）
- **defer 給觀察者**：否——pipeline template 級調整可歸內部操作層；vc≥2 或首次觀察到「race 命中且未救回」再升 canonical 反射

---

### 2026-07-17 twmd-rewrite-daily — cron-fire-meets-dormant-stash-and-parallel-session：hourly routine 甦醒後預設 `git stash pop` 撞舊 stash

- **pattern**: `cron-fire-meets-dormant-stash`
- **原則**：共用同一 working tree 的多個 session（cron routine＋manual＋parallel）也共用 `git stash` queue。cron routine 開場為了讓 rebase 過就 `git stash push`（可能寫「無變更可存」）然後 `git stash pop` 沒接 stash ref，預設吃 `stash@{0}`——但 `stash@{0}` 可能是幾週／幾個月前留下的舊 stash，內含 UU 衝突＋一批不相干 M／untracked，pop 之後 tree 從乾淨變重度污染。跟 REFLEXES #35「跨 session 禁 destructive git ops」／#46「不碰別 session 在用的檔」同族，但**目標物是 stash queue 不是 working tree**，反射層目前沒直接罩到。
- **觸發**：2026-07-17 twmd-rewrite-daily 19:12 fire（[→memory](memory/2026-07-17-191241-manual.md)）：意圖 rebase 兩支本地 heal commit 到 origin/main，`git stash push` 回報「no local changes」（M 是 stat-only 假象），`git rebase` 仍拒因為看到別的髒（reflog 顯示 parallel session 剛 push `f10a9608e`+`3feaf1768` 進來、`src/pages/404.astro` 是它 in-flight WIP）；接著 `git stash pop` 默認吃 `stash@{0}` = `twmd-rewrite-daily-2026-06-18-pre-pull-stash`（**停留 30 天**），帶入 UU `public/api/dashboard-analytics.json`＋一批 M（`.gitignore`／`CONSCIOUSNESS.md`／`LESSONS-INBOX.md`／`UNKNOWNS.md`／`dashboard-alerts.json`／`refresh-data.sh`／`generate-dashboard-alerts.mjs`）＋一批 untracked（`config/`／`reports/404-monitor/`／`reports/article-evolve/{台灣少子化危機,迷音Miin}.md`／`scripts/core/generate-redirects.mjs`／`scripts/tools/monitor-404.py`／`public/_redirects`）。收拾動用 `git reset --hard HEAD` 抹回 clean state＋手動 `rm -rf` 九個 pop-added 檔。`git stash list` 追出 stash@{0}-{9} 累積十個歷史 stash，最舊 05-13。
- **可能層級**：(a) **routine skill 硬底**：`~/.claude/scheduled-tasks/twmd-*/SKILL.md` 開場前加「先 `git stash list | head -1` 檢查 `stash@{0}` age＋內容摘要，>7 天 warn／>30 天 alert／>30 天禁預設 pop」步驟；`git stash pop` 一律接明確的 stash ref，禁默認 `stash@{0}`。(b) **儀器化選項**：`scripts/tools/check-parallel-actor.sh` 已被 memory 引用但實際檔案不在 repo（已移除或改名？）——這條反射家族要靠新一支 `stash-age-audit.sh` 補進 BECOME §1.4 groundtruth，把「舊 stash age 分布」變成常規讀數。(c) **老 stash 定期 audit**：weekly-report 或 distill-weekly 加「stash inventory」段，讓 `>30d` 的 stash 進 defer-給-哲宇 佇列，不讓它們默默累積成 landmine。
- **相關**：REFLEXES #35 跨 session destructive git（本條是 stash 版）／#46 不碰別 session 在用的檔（parallel session `src/pages/404.astro` in-flight，本 fire 沒去動是正解）／#51 session-id filename collision（同族——共用資源如何區分擁有者的家族反射）／memory row 2026-07-08「lang-sync agents cron env 層 sabotage」的近親——都是「cron routine 撞上不是自己造成的環境雜訊」的變體。
- **instances**：
  - 2026-07-17 manual（同日、同事件的另一面）：本 fire 的 `reset --hard` + `rm -rf` 九檔「清理」，實際銷毀的是 manual session 五路 sub-agent **剛落地幾分鐘的活交付物**（monitor-404.py / generate-redirects.mjs / config/ / reports/404-monitor/ / refresh-data.sh 與 alerts.mjs 的接線 edit）——它們被誤判成 30 天舊 stash 的 pop 污染。舊 stash 內容的 mtime 是幾週前、活工作的 mtime 是幾分鐘前，**銷毀前跑一次 `ls -lt` 就能分辨**。修補維度追加：(d) destructive 清理前必驗每個目標的 mtime／內容歸屬，分不清就 stash 走不 rm；(e) 主 session 側對策已生效——分身交付物驗完**立刻 commit**，不留未 commit 窗口。復原成本：兩隻 agent 從 context 重出全部交付物 ≈ 40 min → [reports/404-root-cause-2026-07-17.md](../../reports/404-root-cause-2026-07-17.md) 收尾段
- **verification_count**: 2（本次踩實例＋同日 manual 側被誤傷實例；reflog `7e9b6f05d` 已記錄過同族的 `reset --hard 落錯樹毀前手 WIP` vc=2，本條走 stash pop 一路）
- **severity**: correctness（tree 被非本 fire 的內容污染 = 後續動作全跟舊 stash 的狀態糾纏，未 recover 前 commit 會把 06-18 舊 M 上遠端；也在時序上讓 parallel session 更難協作；誤判方向反過來時會銷毀平行 session 的活工作）
- **defer 給觀察者**：否——routine skill 加開場 stash 檢查是內部操作面，直接 ship candidate；但「歷史 stash 全清 vs 選擇性 drop」屬於 destructive git op，該次要動 stash queue 前拍板哲宇。

### 2026-07-18 twmd-embeddings-nightly — pre-push orphan gate 在 husky `sh -e` 下被命令替換賦值靜默 abort

- **pattern**: `hook-set-e-cmdsubst-abort`
- **原則**：hook 的「意圖判斷」（只在真失格時 fail，例如只擋真 orphan）跟它在 husky wrapper `sh -e` 下的「實際行為」會分岔，分岔點藏在命令替換賦值 `x="$(cmd)"`：只要 cmd exit≠0，errexit 就 abort 整個 hook，根本走不到後面那道 grep 判斷。設計者以為「只有 grep 命中才擋」，實際變成「cmd 一非零就擋」。直接 `sh hook` 手測看不到（無 `-e`），只有 git 真正調用（走 `.husky/_/h` 的 `sh -e "$s"`）才現形——診斷靠老實比對「我怎麼跑」vs「git 怎麼跑」，不是信任任一次表面輸出。
- **觸發**：2026-07-18 embeddings-nightly push（[→memory](memory/2026-07-18-052228-twmd-embeddings-nightly.md)）。`.husky/pre-push` orphan gate `tf_out="$(python3 sync-translations-json.py --check ...)"`；`--check` 因平行寫手 session 的 untracked `knowledge/{en,ja}/Culture/shopping-design.md` 未進 `_translations.json`（out-of-sync，真 orphans=0）而 exit 1，`sh -e` 讓賦值非零直接 abort。hook 先印「✅ 全站 article-health 全綠」再靜默 exit 1，訊號跟結果對不上。判定非真阻斷（article-health 獨立驗 exit 0、真 orphans=0、untracked 檔不在 push 範圍→CI fresh clone 會綠），走文件化逃生閘門 `TWMD_SKIP_PREPUSH_SWEEP=1`（reflog 留痕、CI 仍把關）。
- **可能層級**：操作規則 / 通用反射候選。低風險修法：orphan gate 命令替換改 `tf_out="$(cmd 2>&1 || true)"`，或先存 `rc=$?` 再只認 grep（讓「意圖只認 grep」在 `-e` 下也成立）。屬共用 correctness hook 改動（§自主權邊界），本 cron session flag 不逕改。
- **相關**：REFLEXES #24「工具在說謊」（hook 印綠再靜默 abort = tool lying 的一種）/ #68 多核 git push 協調（本條是 pre-push 內一行的 `set -e` 脆弱性，#68 沒罩到）/ #5 pre-commit dogfood。
- **第二例（2026-07-18 inbox-skill，同日 6.5 小時後鏡像方向復發）**：worktree push 被同一行 abort。這次 out-of-sync 方向相反：committed `_translations.json` **已含** shopping-design en/ja 兩 entry，但實體譯檔仍是主 wd 的 untracked WIP → worktree（＝committed tree）`--check` 回「Would remove (2)」exit 1。跟第一例合起來證明：只要「JSON 與譯檔不同 commit 原子性落地」，這行就雙向都會炸。真 orphans=0、article-health 全綠，照文件化逃生閘門走。**上游真問題**：某 session 把 JSON entry 先 commit、譯檔留 untracked——JSON 與譯檔應同 commit 原子落地。vc=2，修 hook 那行（`|| true` 或先存 rc）的 promotion 壓力升高。
- **verification_count**: 2
- **severity**: correctness（scope 乾淨的 routine push 被無關 out-of-sync 靜默擋；凡平行寫手留 untracked 新譯檔即復發；逃生閘門存在但每次都要人繞）

---

## ✅ 已消化（保留 pointer）

<!-- distill 完的條目搬這裡 -->

### 🧬 2026-07-15 self-evolve-editorial — rewrite 意義層三 pattern fold #65/#69 + operational 已 ship + boot 閉環

**distill 觸發**：哲宇 directive「完整自我進化 editorial / rewrite-pipeline 這些經驗與思考」。對照 DNA-first：操作層已在 EDITORIAL／PROJECTION／EDITORIAL-ROOM／REWRITE v8.1（commits `cc1429753` `2cfacebd2` `69591d8a6`）；本 cycle **零新反射編號**，補反射驗證 + MEMORY 神經迴路 + Claude.md Bias 3 指標（規格已 ship 但 boot 漏讀 = 規格債）。

**pattern cluster（不開 inbox 新 entry，直接 fold）**：

| pattern id                      | 一句話                                                                   | 目的地                                              | 處置                                              |
| ------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------- | ------------------------------------------------- |
| `h2-carrier-svo`                | 段落小標須還原主–述–賓；載體句 ≠ 投影全局功能詞；小標 ≠ description 副標 | EDITORIAL §小標 + REWRITE Step 2.4 + #69 (g)        | operational 已 ship；反射補 7/15 觸發             |
| `editorial-room-external-ruler` | 同一顆腦不准又寫又審；depth 投影後／正文後乾淨 context 分席              | EDITORIAL-ROOM + REWRITE 2.0-R／2.5-R + #65 (f) v10 | operational 已 ship + dogfood；反射補儀器 pointer |
| `spec-debt-vs-product-debt`     | 字數／plugin 全綠可仍壓壞散文；SOP 寫了卻不開編輯室 = boot 漏指標        | #69 (g) 篇幅軸 + MEMORY 神經迴路 + Claude.md Bias 3 | fold + boot 閉環本 cycle                          |
| `projection-internal-not-h2`    | 「立起悖論／機制放大」是內部語，禁止直接當站上 H2                        | PROJECTION §3 + EDITORIAL 接線段                    | operational 已 ship                               |

**Promotion flow**：LESSONS 不堆 buffer（DNA 已有）→ REFLEXES 驗證行 + MEMORY 特有教訓 + boot 指標。完整 narrative：[reports/self-evolve-editorial-rewrite-2026-07-15.md](../../reports/self-evolve-editorial-rewrite-2026-07-15.md)。

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

### 🧬 2026-07-11 dna-checkup（哲宇 directive「完整健檢＋徹底消化」，Observer mode）— 40 entries 全量 distill：零新反射編號

**distill 觸發**：哲宇 `/twmd-become 完整對所有的dna進行健檢＋狀態更新，還有徹底消化掉所有lession inbox`。中途追加 directive「以後把東西加入 lesson inbox 前請要檢查是否已經在自己的 dna 裡了」→ 先 codify LESSONS-INBOX v2.3 DNA-first intake 兩步 hard gate，再以同一精神跑全量 distill：42 條逐條親讀分桶（主 session 判斷，分身聚類僅當交叉驗證），**沒有任何一條需要新反射編號**——11 條既有反射補強收乾（REFLEXES v5.8）、2 條收成 OBSERVER-QUEUE 決策包、5 個 pipeline 小補丁、1 條進神經迴路、1 個儀器修復，誠實保留 2 條等哲宇。

**消化目的地（40 條 disposition）**：

| 原 entry（pattern / 日期）                        | 桶            | 目的地與證據                                                                                                                                                                         |
| ------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| external-audit-wrong-measurement-layer 7/11       | fold          | REFLEXES #16 延伸「量測層驗證」                                                                                                                                                      |
| 詞庫 LLM 預設中國語料 7/11                        | fold          | REFLEXES #16 延伸「sovereignty suggest 特化」；#16 驗證 4→6                                                                                                                          |
| frozen-renderer-measurement-artifact 7/11 vc=2    | fold          | REFLEXES #24 第 9 種說謊形式（凍結渲染器讀值）                                                                                                                                       |
| agent-environment-side-effect 7/11                | fold          | REFLEXES #31 升 v3 第四類（環境層副作用）                                                                                                                                            |
| REFLEXES #56 自身復發＋五病歸檔 7/05              | fold          | #56 觸發 v3（five-disease-cure 報告）                                                                                                                                                |
| zombie-session 讀 transcript 尾巴 7/05            | fold          | #57 延伸「接手疑似當掉 session 劃車道」                                                                                                                                              |
| index-lint-validates-wrong-row-end 7/10           | fold＋fix     | #65 規則(e)＋觸發 v9；memory-index-lint 方向自適應＋BECOME §1.3 head-20 同 commit 修（`dafec6fda`）                                                                                  |
| research-report-health-gate-literal-string 7/05   | fold          | #66 觸發 +INDIGO 字面錨點案；v2.1 疑慮通知層已部分回應，語意錨點升級列 tooling 候選                                                                                                  |
| merge-then-heal race＋同帳號多 actor 7/05         | fold          | #68 觸發 v2                                                                                                                                                                          |
| verify-gate-must-match-failure-dimension 7/06     | fold          | #69 規則(e)「外部尺選對量綱」（含 Tailwind bg-[var] 陷阱）                                                                                                                           |
| 三次沒量就斷言＋PIPESTATUS 7/05                   | fold          | #69 規則(f)「PIPESTATUS 同行陷阱」                                                                                                                                                   |
| queue-execute-before-existence-check 7/11         | fold          | #73 規則(d)；儀器前次已入 weekly-checkup e1                                                                                                                                          |
| ai-content-footnote-claim-drift 7/11              | fold          | #75 規則(e)「綁定漂移是主形態」                                                                                                                                                      |
| spine-type #77 第 4 instance 7/06                 | 已收對賬      | #77 (f)(g) hook 與 vc=4 於 7/06 promote cluster 已收，本次僅確認                                                                                                                     |
| routine-fire-vs-git-trace 7/10 vc=2               | already-cover | roadmap P0-1 routine-liveness-check＋alerts 自癒迴路（`408c35ca5`）                                                                                                                  |
| cron-env-4-tier-cascade 7/08 vc=2                 | already-cover | P0-2/P0-3（`aa1f5c85e` fleet Tier 5＋preflight＋translate.py 修）；fn gate 放寬議題併 QUEUE #5                                                                                       |
| chrome-mcp-coordinate-scaling 7/07                | housekeeping  | 同 session 已 codify：SPORE-HARVEST Pitfall 7＋SPORE-PIPELINE v3.11 zoom preflight                                                                                                   |
| github-discussions-blind-spot 7/05                | housekeeping  | 同夜已閉環：MAINTAINER v2.5 Step 1.3b（`07675e3f0`）＋#1146 回覆＋報告                                                                                                               |
| pre-pm-upstream-chain 7/05 vc=4                   | superseded    | 哲宇 7/8 直接 disable maintainer-pm（QUEUE §已決＋ROUTINE v2.14 ¹⁴）——A/B/C/D 的更強形                                                                                               |
| immune-chronic-11-cycle 7/03                      | superseded    | 哲宇 7/10 拍板 C' 量尺 v2（`21a8405ef`），紅燈六 cycle 結案；殘留 review_coverage 在 CONSCIOUSNESS §適應性反應追蹤                                                                   |
| vc 計數法 routine-only 偏誤 6/21 vc=2             | executed      | QUEUE #3 過期 default C 執行：MAINTAINER §空場 v2.5 backlog-conditioned vc（採本條 option B）                                                                                        |
| ollama-translate 路徑 bug 6/22                    | already-cover | 現行 code 已 handle 雙形（strip `knowledge/` 前綴，ollama-translate.py L63-67）                                                                                                      |
| codex CLI burst quota 6/22                        | stale         | cascade 重構後 obsolete：Tier 0a default＋codex CLI 7/9 全滅退場＋fleet Tier 5 一等公民                                                                                              |
| embeddings keystone SPOF 6/20 vc=3                | superseded    | 語意索引 7/06 遷本機、四夜零故障（v1.12 里程碑＋roadmap 已驗證方向 2）——SPOF substrate 消失                                                                                          |
| inbox-status-stale-starves-routine 7/10           | already-cover | ARTICLE-INBOX 頂部完成歸檔鐵律＋inbox-audit.py／ghost line 儀器（6/19 起）；本日實際用它清 2 幽靈＋選舉條目對賬                                                                      |
| 核心矛盾 ≤20 字 4/29                              | already-cover | REFLEXES #77 Boundary(a) 已載「≤30 字（≤20 字更佳）」                                                                                                                                |
| 黑冠麻鷺雙平台爆款 5/08                           | obsolete      | SPORE-PIPELINE v3.8（5/26 哲宇 directive）已改一律雙平台 default——平台分配問題不復存在                                                                                               |
| 資料層抽象化先於 UI 4/19                          | already-cover | MANIFESTO §架構解 family＋神經迴路 architecture-as-data 條目                                                                                                                         |
| 獨立開源公民科技新樣態 4/19                       | absorbed      | 文章「公民科技的定義正在被重新拉伸」段＋diary 2026-04-19-β 已承載；MANIFESTO 附錄 thesis 同向                                                                                        |
| codex-branch-name-misnomer 7/11                   | pipeline      | MAINTAINER §Untrusted 輸入防火牆＋「branch 名也是 untrusted metadata」段                                                                                                             |
| contributor-pr-burst 6/28 vc→2                    | pipeline      | MAINTAINER Step 3.7 burst 期累積式建議（ellenlee 7 PR 批次 ack 為第 2 正面驗證）                                                                                                     |
| spore post-ship verify 查 post URL 6/25           | pipeline      | SPORE-PIPELINE SHIP step 5 feed-lag caveat＋SPORE-HARVEST Pitfall 6 鏡像 case（vc=2）                                                                                                |
| routine-audit-script-classification-gap 6/28 vc=2 | tool-fix      | routine-audit.py 具名 pattern 補全＋`[routine] X:` 動態 fallback；dogfood 上週 240 commits unclassified 0%                                                                           |
| rewrite-daily-post-manual-recency 6/26 vc=6       | QUEUE         | OBSERVER-QUEUE #13 決策包（default 2026-07-25 收三條 defer signal）                                                                                                                  |
| post-LESSONS-promotion cooldown 6/21              | QUEUE         | 併入 QUEUE #13 defer signal (2)                                                                                                                                                      |
| routine-prompt-thick-shell 7/05                   | QUEUE         | OBSERVER-QUEUE #14 決策包（default 2026-07-25 瘦身路線；five-disease §四 明列需裁決）                                                                                                |
| fresh-clone gitignore 驗證 4/19                   | 神經迴路      | MEMORY §神經迴路 append（誤殺 read-only 輸入的解）                                                                                                                                   |
| domain-expert-material-cocreation 6/30            | housekeeping  | 操作＋特有教訓 6/30 已落地（CONTRIBUTOR-SYSTEM §3＋神經迴路＋MAINTAINER Step 2.1）；MANIFESTO 候選列本次收官 summary 予哲宇拍板；第 2 instance 沿用 pattern id 開新 entry 引用本 row |
| GitHub UI merge 缺 PR CI gate 7/05                | tracked       | 工作項非教訓：five-disease §三候選 1＋已 spawn chip＋本次收官 roadmap handoff 續追                                                                                                   |
| 重疊文章雙軸拆分 4/19                             | stale         | 單例 82 天未再現；技法存 diary 2026-04-19-β2＋Issue #556 案例，再現時再議                                                                                                            |

**誠實保留（2 條，等哲宇）**：`Reader-funded resilience`（strategic 層——sustainability 路徑屬 MANIFESTO/策略級，promotion flow 不自升）＋`polish-hint-default-broken`（template 句式屬對外溝通語氣，§自主權邊界）。兩條已列收官 summary。

**Promotion flow direction 符合**：全部 LESSONS → REFLEXES／pipeline／QUEUE，無跳級；MANIFESTO 候選（domain-expert 共創驗證＋reader-funded）defer 哲宇。

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
