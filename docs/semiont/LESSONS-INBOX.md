---
title: 'LESSONS-INBOX'
description: '教訓 buffer（intake layer）— 新教訓先 append 此處，週期性 distill 到 MANIFESTO/DNA/MEMORY canonical'
type: 'cognitive-buffer'
status: 'buffer'
apoptosis: 'never'
current_version: 'v2.7'
last_updated: 2026-08-19
last_session: '2026-08-19-053717-twmd-embeddings-nightly（新 entry `retyping-shell-substitution-loses-the-substitution` vc=3 直接觸發 pipeline 修補）；同波併入 2026-08-18-164330-twmd-maintainer-manual（三條 maintainer entry 標 ✅ 落 MAINTAINER；open-count 加 draft-as-proxy vc=3；sibling-checks 加 liveness/classifier 同盲例 vc=2；twin-artifact 加 canonical↔薄殼 第六例；shared-tool-quota 加 Wikimedia CDN 429 vc=2）'
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

| Count                   | 處置                                                                                                                                                                                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| < 30                    | no-op（健康範圍 — daily routine 補 ~3/day 抵 SHIP ~1/day 消化）                                                                                                                                                                                                             |
| 30 ≤ N < 50             | append LESSONS-INBOX entry「SPORE-INBOX 容量警示 vc=N」+ telegram alert（觀察者 review）                                                                                                                                                                                    |
| **[30,50) 連 3 週高原** | **升 defer to observer**：手動 review 一次 pending 內容組成、寫進當週 weekly-report §7 SPOF、telegram-poke 觀察者拍板方向（減量 vs. 加速 ship vs. 拉高 auto-drop 閾值三選一）。routine 不自決；蓄水位是穩定過渡狀態不是 acute 事件，長期不解 = auto-drop 觸發前就變隱形習慣 |
| ≥ 50                    | **Auto-drop 最舊 5 條** `Requested by twmd-spore-pick-daily routine` 未被 promote（priority 仍 P2 / 未被改 Hook 或 必驗事實）的 entries。哲宇 promote 過的 entry **不動**                                                                                                   |

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

### 2026-08-21 twmd-feedback-triage — report-line-keyed-on-mutable-display-string：報表拿會變的顯示字串當識別欄，同一筆重複出現時在視覺上斷了連續性

**現象**：`b78ee4f5` 那封第三人檢舉信第八次原樣出現，而我第一眼把它讀成新進來的一筆，寫下的第一句判斷是錯的。原因在報表那一行：`triage.mjs` 的 FILE 行印的是 `[分類] 文章標題`，而這筆回報掛在新聞自由條目底下——那個條目有十幾個語言版本，今天它抽到越南文的 `Truyền thông và tự do báo chí tại Đài Loan`。前七輪的 memory／handoff 全用中文記著「第三人指控信」，沒有一處長得像這串字。同一個 id、同一段文字，顯示欄換個語言就換一副面孔。reject／skip 那兩個分支反而都印了 id，只有真的要開 issue 的那一支沒印。

**跟既有反射的關係**：[LESSONS 2026-08-17 `recognition-bound-to-instance-coordinates`](#) 說辨識力綁在單一案例的座標上會越用越淺；這是同一種脆弱的反面——**座標本身會動**。也是 [REFLEXES #82](REFLEXES.md) proxy signal 的一個小 instance：文章標題是那筆回報的替身，不是它本身。

**接住它的不是辨識力**：是 HG13 規定 `--exclude` 之前必須讀完全文這道順序。那道順序不問我認不認得出它，所以擋得住我認錯的那一刻。誤判沒有造成後果，純粹因為流程不允許用第一個判斷去動手。

**修補（已 ship）**：FILE 行補印 `id=`（`triage.mjs`，51 個 unit test 全綠）。只改報表說出自己在講哪一筆，不碰任何判準。

**候選反射（vc=1）**：任何供人重複判讀的報表，識別欄要用穩定鍵（id／slug／hash），可變的顯示字串（標題、翻譯、狀態文案）只能當附註。人對「這筆我看過」的連續感掛在顯示層，而顯示層是會被上游改動的。

**Reference**：本日 memory 與 diary 檔、`scripts/feedback/triage.mjs` FILE 行

### 2026-08-20 twmd-maintainer-am — documented-red-flag-with-no-enforcer：紅旗清單寫了幾個月，沒有任何機器在查

**現象**：MAINTAINER-PIPELINE §Step 2.3 的十條紅旗裡，#6（投稿者自設 `featured: true`）與 #7／#8（`author` 偽造成 `'Taiwan.md'` / AI 產品名）都白紙黑字寫著，Step 3.3 連修法都寫好了（「1 行改 `'Taiwan.md Contributors'`」）。今天這批 26 個投稿，8 個帶 #7、3 個帶 #6——而 `contributor-pr-heal.py` 不修、`article-health --profile=ci-deploy` 回 hard=0。結果是我在建好閘門之前，已經替 #1467 與 #1458 推了 heal commit，紅旗原封不動留在裡面。**是我自己漏掉、隔幾分鐘後對整批做 frontmatter 稽核才發現的**，不是任何儀器叫出來的。

**跟既有反射的關係**：這是 §神經迴路「規則要能執行才算規則」在投稿審核層的又一個 instance，也是 [REFLEXES #87](REFLEXES.md)「保護密度跟曝光量成反比」的變體——只是這次反比的不是曝光量而是**規則的年紀**：寫得越早、越被當成常識的規則，越沒有人回頭問「這條有東西在守嗎」。

**修補（已 ship，commit `c920ebe91`）**：三條紅旗的修法進 `contributor-pr-heal.py`。

**這次差點犯的第二個錯，比第一個更值得記**：我第一版是把它做成 `article-health` 的全站 plugin（`author-identity`，hard）。寫完跑 `--list-checks` 確認註冊成功、拿一篇文章 dogfood 也過了——**看起來完全正確**。接著順手量了一次全站語料：`author: 'Taiwan.md'` 在 zh 有 **401 篇**，因為那對 Semiont 自己走 REWRITE 產線寫的文章是**正確**的署名。那道 gate 一旦上線會一次誤殺 401 篇好文章。

差別在一個沒被寫進紅旗條文的前提：「這個署名是不是偽造」只有在「這個檔來自外部投稿」的脈絡下才成立，而全站 lint 沒有那個脈絡。所以檢查最後掛在 `--from-pr` 路徑（裸路徑模式明確不碰），這是 [REFLEXES #66](REFLEXES.md)「閾值要用真實產出 dogfood 校準，不是憑想像設」——救我的不是設計時的謹慎，是**上線前多量了一次全站分母**。

**候選反射（vc=1）**：規則升格成閘門時，除了問「判準對不對」，要多問一句「**這條判準的前提在哪一層成立**」。同一句話在投稿脈絡是紅旗、在自產脈絡是正確值；把它掛錯層，閘門會忠實地執行一個在那一層根本不成立的規則。今天同一個 cycle 還有第二個同型：`punct-cleanup --fix` 的驗收原本跑整篇 `article-health`，於是本來就有無關 hard 的投稿永遠不敢寫檔——把「我這次改壞了嗎」跟「這篇本來就有別的問題嗎」讀成同一個燈（[REFLEXES #38](REFLEXES.md) 混維度），改成只比 delta 才對。

**Reference**：commit `19e7373b2`（punct-cleanup --fix）、`c920ebe91`（紅旗 healer）、本日 memory 檔

### 2026-08-19 twmd-maintainer-am — detector-inherits-the-blindness-it-was-built-to-catch：專為抓「存在≠有跑」而生的偵測器，自己用了一個只看得到最近六小時的取數口

- **pattern**: `detector-inherits-the-blindness-it-was-built-to-catch`
- **原則**：新造一道閘門去抓某種盲點時，**那道閘門自己的取數口也會有同一種盲點**，而且更不容易被發現——因為它每次都「有跑、有回答、回答還是安全的那一邊」。MAINTAINER Step 1.5b 2026-08-14 誕生，任務就是抓「workflow 檔存在 ≠ 這個 PR 的 workflow 有跑」（REFLEXES #82）。它自己用 `gh api repos/…/actions/runs` **不帶 `branch=` 參數**，再用 jq 過濾 `head_branch`——那個 endpoint 預設只回最新 30 筆 run。在這個 repo（babel 整點 commit、deploy 頻繁）30 筆只涵蓋約 **6 小時**。換句話說：**這支偵測器只看得見六小時內推過的 PR，而它要抓的正是「卡很久沒人管」的那種 PR**。適用範圍跟目標對象完全互斥。
- **觸發**：2026-08-19 maintainer-am。PR #1365（domo741852963-eng，首次投稿）head sha 上零 check-run，`gh pr checks` 回「no checks reported」。照 Step 1.5b 寫的指令跑，回報 `待批准=0` → 判準表那條「`checks=0` 且 `待批准>0`」不成立 → 讀起來像「這個 PR 沒有配置 CI」。加上 server-side `?branch=&per_page=100` 之後，同一個問題回報 **84 筆** `action_required`，最早的一筆從 8/15 卡到今天。三天。**8/16 的 maintainer cycle 已經核准過一次、跑出結果、告訴投稿者哪裡要修**；投稿者修好又推了四次，四批 run 全數退回 `action_required`，而三天內每一輪 maintainer 都拿著這支盲的偵測器問過同一個問題、每次都得到「沒事」。
- **代價**：投稿者修好的東西三天沒被看見——他這邊的體感是「我照著回饋改完，然後就沒有下文了」。更貴的是判例：這是 Step 1.5b 誕生後第一次真正被需要的場合，它失效了，而失效的方式是**回答「安全」而不是報錯**（REFLEXES #85「不知道」需要自己的符號，不能借用「沒事」的那個——`待批准=0` 同時代表「查過了沒有」跟「我根本看不到那麼遠」）。
- **第二個獨立發現（同一次調查）**：**GitHub 的 workflow 核准是一次性的，不是對這個投稿者永久生效**。8/16 核准過一次不代表 8/16 之後的 push 會自動跑。原本 pipeline 的敘述（「GitHub 對第一次投稿的 fork contributor 預設不自動跑 CI」）讓人以為核准一次就過關了，實際上每一次新 push 都要重新確認 armed。
- **修補（本 session 已 ship）**：(a) 取數邏輯從文件裡的可貼 snippet 搬進儀器 [`scripts/tools/pr-ci-armed.sh`](../../scripts/tools/pr-ci-armed.sh)（server-side `?branch=` + `per_page=100` + 只看 head sha）；(b) 判準從一句話升三態表，把原本混在一起的兩種零檢查拆開——**UNARMED**（被擋住，有人要按核准）vs **NO-WORKFLOW**（沒被觸發，paths filter 不匹配），處置完全不同（REFLEXES #38 混維度）；(c) 核准指令改成只放 head sha 那批（#1365 若全放等於一次燒掉 84 筆 runner）；(d) pipeline 觸發段補記「核准非永久」。
- **待補**：這支儀器目前**沒有掛在任何自動路徑上**，靠 maintainer cycle Stage 1 手跑。UNARMED 的 PR 不會主動叫。候選：接進 routine 的 quality gate，或讓 UNARMED > 0 進 dashboard-alerts。
- **可能層級**：REFLEXES #82（存在代理有效）的 self-apply 子規則——**新造的偵測器要對自己跑一次它要抓的那個問題**；也可 fold 進 REFLEXES #65（awareness instrument 自身要 cross-verify ground truth）。
- **相關**：REFLEXES #82 / #65 / #85 / #38；LESSONS `gates-measure-handling-not-solving`（2026-08-11，閘門只回答你問它的問題）；LESSONS `sibling-checks-share-one-blind-premise`（2026-08-14，同族閘門共用前提一起看不見）
- **verification_count**: 1

### 2026-08-19 twmd-embeddings-nightly — retyping-a-shell-substitution-reintroduces-the-typo-it-fixed：把 pipeline 裡會自動代換的指令手動抄成文字，代換消失、打字錯誤回來

- **pattern**: `retyping-shell-substitution-loses-the-substitution`
- **原則**：EMBEDDING-PIPELINE Stage 3 的 commit 指令寫的是 `-m "... — $(date '+%Y-%m-%d %H:%M')"`，照抄執行時 shell 會自動代入當下時間，不需要人手動填值。但當執行者把這段指令改寫成 heredoc（`<<'EOF'...EOF`，quoted，不做變數展開）再手動打一個時間占位符進去時，等於把「shell 自動代換」換成「人工謄寫」，而人工謄寫正是會打錯字的那一步。
- **觸發**：2026-08-18 session 已經踩過同一個坑（把 `$(date ...)` 誤打成字面 `05:2X`，push 前用 `--amend` 補救，並在 memory 寫下「commit 指令段直接複製 pipeline 原文而非重新輸入」的提醒）。2026-08-19（本 session）commit 時同一個 routine、同一個 Stage 3，把時間占位符打成 `05:0X`——跟前一晚幾乎一模一樣的錯誤，且是在讀過昨晚那條提醒**之後**發生的。**第三次發生在同一個 session 內、就在寫這條 LESSONS entry 記錄前兩次事故的當下**：寫 session memory 檔時，把 frontmatter 的 session span 跟文末 footer 的時間戳又打成字面 `06:0X` / `05:0X`——一邊在描述「這個模式很危險」，一邊在同一個動作裡把它示範了第三次。昨晚的 memory 提醒是「下次可以考慮」，不是「下次必須」，語氣留了自由裁量空間，而自由裁量空間就是這個錯誤連續三次復發的縫。三次都在 push / 定稿前被人工複查抓到、當場修正，沒有污染最終產物，但三次都是同一個根因，且第三次證明「知道這個坑」完全不能防止「當下再掉進去」——意識到 pattern 跟在生成文字那個瞬間真的停下來檢查，是兩個不同的能力。
- **代價**：目前代價僅是額外的複查與修正步驟，尚未造成任何已 push / 已定稿產物帶著錯誤 timestamp 流出。但代價曲線在往上：從「跨夜復發」(vc=1→2) 到「同一 session 內、討論這個問題的當下復發」(vc=3)，說明這不是「跨 session 失憶」的老問題，是「生成任何帶時間戳的文字時，手指比對這件事的警覺快」的即時性問題。pipeline footer 已記錄過另一種變體（2026-08-06〜08 三夜連續踩到 co-author 型號寫死的問題）——同一 Stage 3 commit block 現在有兩種獨立的「手動謄寫覆蓋掉本該自動化的欄位」子模式，都指向同一個結構弱點。
- **修補候選**：(a) EMBEDDING-PIPELINE.md Stage 3 的指令範例改成明確禁止 heredoc 改寫，加一句「commit message 一律用未加引號的 heredoc 或直接 inline `-m`，讓 `$(date ...)` 真正被 shell 執行，不要手動填入時間字串」；(b) 更徹底的修法是把 Stage 3 指令改成兩步：先跑 `MSG=$(date '+...')` 把值存進變數並印出來讓執行者看見實際值，再把變數帶進 `git commit -m "... $MSG"`，讓「有沒有正確代換」變成可以在下指令前肉眼確認的中間狀態，而不是隱藏在一次性字串組裝裡；(c) **本 session 已直接執行**：任何要寫入帶時間戳的文字（commit message／memory frontmatter／memory footer）前，一律先跑 `date '+%Y-%m-%d %H:%M'` 拿到實際值再貼上，不允許先寫佔位符「之後再補」——「之後再補」正是三次事故共同的中間狀態。
- **instances**：
  - 2026-08-18 twmd-embeddings-nightly：commit message 裡 `$(date ...)` 誤打成字面 `05:2X`，push 前 `--amend` 補正
  - 2026-08-19 twmd-embeddings-nightly（本 session，第一次）：commit message 同一模式，誤打成 `05:0X`，push 前 `--amend` 補正
  - 2026-08-19 twmd-embeddings-nightly（本 session，第二次，同一 session 內）：寫 session memory 檔時，frontmatter session span 與文末 footer 時間戳又打成字面 `06:0X`／`05:0X`，定稿前 Edit 補正——發生在剛寫完前兩次事故記錄的同一動作序列裡
- **可能層級**：操作規則升通用操作紀律（不只 EMBEDDING-PIPELINE Stage 3，任何寫時間戳到 commit message / memory frontmatter / memory footer 的動作都適用）
- **相關**：REFLEXES #15（反覆浮現要儀器化，同一 session 內三次復發已達 vc=3 canonical 門檻，含跨夜 2 次 + session 內即時 1 次）；EMBEDDING-PIPELINE.md footer 2026-08-06〜08 co-author 型號寫死變體（同 Stage、不同欄位的姊妹模式）
- **verification_count**: 3

### 2026-08-18 academia-sinica — opposing-seat-prescriptions-have-no-ruling-doctrine：兩席對同一句話開出相反處方，pipeline 沒寫主編該怎麼裁

- **pattern**: `opposing-seat-prescriptions-no-ruling-doctrine`
- **原則**：分席審的價值來自席位各自獨立，而獨立必然產生相反處方；EDITORIAL-ROOM 寫了怎麼開席、怎麼收 verdict、怎麼列必改清單，唯獨沒寫「兩席要求互斥時主編憑什麼裁」——留白處主編會不自覺選比較好做的那一邊。
- **觸發**：2026-08-18 中央研究院 Step 3.6 大驗證輪。閱讀節奏席判某句過度停頓、處方是「讓它離開正文」；炎上倫理席判同一句對在世當事人交代不足、處方是「講得更清楚」。一個要它變短、一個要它變長，兩席都對。我用 EDITORIAL §視角翻轉把敘述主體換掉，同時滿足兩邊，但這個解法是臨場想的，不是 pipeline 給的——換一個主 session 或換一個當下心力狀態，最可能的結果是挑一席聽、把另一席寫進「defend（不列必改）」。證據：`docs/semiont/memory/2026-08-18-144749-academia-sinica.md` §Handoff 三態、`reports/editorial-room/中央研究院-projection-review.md` §攻防（該表只有 accept／defend／noted 三態，沒有「兩席互斥」這一格）。
- **instances**：
- **可能層級**：操作規則（EDITORIAL-ROOM §主編裁決 補一段）
- **相關**：#69 (g) form gate ≠ meaning gate（席位衝突正是意義層才會發生的事，形式尺永遠量不到）；`cold-seat-attribution-inverted`（同屬分席審制度層的縫）
- **verification_count**: 1

### 2026-08-18 twmd-maintainer-am — diagnosing-from-the-contributor-tree-audits-a-past-self：站在投稿者的分支上診斷，量到的是我們昨天的樣子

- **pattern**: `diagnosing-from-the-contributor-tree-audits-a-past-self`
- **原則**：`git checkout pr/N` 之後，跟著換掉的不只是被審的內容，**還有整套檢查器**。那個分支停在投稿者 fork 的那一刻，於是任何「我們的工具壞了」的結論，其實是「我們的工具在他 fork 那天壞了」。而 CI 跑的 gate 用的是 main 的工具（3-dot merge-base checkout），兩邊可以給出完全不同的答案。**要對工具下結論，就得站在工具的家裡下**——診斷投稿失敗要分兩層問：這個檔在**現在的** main 尺下如何（把檔案帶過來），以及這個分支自己帶了什麼（僅限判斷投稿者當時看到什麼）。
- **觸發**：本 cycle 追 idlccp1984 七個 PR 為什麼卡在 `frontmatter-gate`，在 `pr/1372` 的樹上讀 `taxonomy_subcat.py`，「發現」三個結構性缺陷（People 標題 regex 漏解析、8 個 boost 標籤非正典、`allowed_subcategories()` union 自己的推論表），還做完了全庫 212 篇非正典 subcategory 的 blast radius 分析——**才發現這三個缺陷昨天早上（`8ba8c6726`）已經全部修掉了，修的人是前一輪的同一條 routine**。main 上 `boost_label_drift()` 回空、People/Nature 解析正確。我不是找到了新病，我是在讀一份昨天的病歷，還差點要照著它再開一次刀。
- **代價**：本 cycle 約三分之一的診斷時間花在重驗一件已解的事；更貴的是差一點就要對 212 篇文章的 subcategory 做批次重構（>50 檔，命中 §自主權邊界），而那個念頭完全建立在一份過期的樹上。攔下它的不是任何閘門，是順手 `git log --grep` 查了一下有沒有人動過這支檔案。
- **為什麼閘門接不住**：worktree 的提示、`check-parallel-actor.sh`、pre-commit 全都只看「有沒有人同時在改」，沒有一支在問「**你現在站的這棵樹，是不是你以為的那棵**」。REFLEXES #67「已驗過帶時間戳」講的是結論要帶時間戳，本條再往前一步：**觀察本身要帶座標**，而 checkout 會靜默改掉座標。
- **修補候選**：(a) MAINTAINER-PIPELINE Stage 2 加一句「在 PR 分支上讀到疑似工具缺陷時，先 `git log --oneline main -- <該檔>` 對一次，或把檔案帶回 main 樹重跑」；(b) 更省事的做法是把「診斷投稿失敗」的 SOP 直接寫成「把 PR 的內容檔帶進 main 樹跑」而不是「checkout PR 分支」——本 cycle 後半改用這個方式，七篇的真實 blocker 一次就對了。
- **相關**：REFLEXES #67（已驗過帶時間戳）、#82（proxy signal——樹是「gate 用的樹」的代理）、#73（查證反射 < 建造反射：先動手讀碼、後才想到查 git log）、LESSONS `healer-authors-the-drift-it-validates`（8/17，本條重驗的正是那一條）
- **✅ 已 instantiate（2026-08-18 twmd-maintainer-manual）**：修補候選 (b) 落 [MAINTAINER-PIPELINE v2.8 §診斷投稿失敗：把 PR 內容檔帶進 main 樹跑，不 checkout PR 分支](../pipelines/MAINTAINER-PIPELINE.md)＋Top-N 第 3 條。同日 68 個 draft PR 的 Phase A 分析全部用 `contributor-pr-heal.py --from-pr N` 帶進 worktree 跑，零 checkout。
- **verification_count**: 1
- **severity**: moderate（不壞資料，但會憑空製造已解問題的工單，且推導出的「修補方案」可能指向大規模重構）

### 2026-08-18 twmd-maintainer-am — reopened-channel-still-needs-someone-to-walk-down-it：把管道接回去，不等於訊息有到

- **pattern**: `reopened-channel-still-needs-someone-to-walk-down-it`
- **原則**：修好一條斷掉的說明管道之後，成效要看**對方的行為有沒有變**，不是看管道通了沒。一條需要對方主動點進去才讀得到的管道（Actions → 紅 X → Job Summary），對一個只看到 PR 頁面紅叉的投稿者來說，跟斷掉的差別很小。**「我們現在有講」跟「他現在知道」之間還隔著一個他要不要走過去。**
- **觸發**：8/13 記過 `gate-explains-into-a-dead-channel`（fork PR token 唯讀 → gate 的說明留言必定 403），當天的修補是把說明改寫進 `$GITHUB_STEP_SUMMARY`，理由寫「不需 token，紅 X 一點就到」。本 cycle 回頭量：idlccp1984 8/15 送的七個 PR，全部在修補上線**之後**，全部敗在同一項，**三天零修正**。管道確實通了（我在 run log 裡確認 Job Summary 有寫出來），但沒有人走下去。真正讓這七篇動起來的，是這個 cycle 直接把修補 push 到他的分支。
- **這條的價值在於它反駁了自己前一版的結論**：8/13 那筆的處置寫完就結案了，沒有留任何「之後要回來量」的鉤子。如果不是這批 PR 剛好又出現在同一道 gate 下，「Job Summary 已修好」會一直是帳面上的完成狀態。
- **修補候選**：(a) 對 fork PR 這種留言必定失敗的情境，改用 **PR review**（`pull_request_review` 走的是不同權限面）或在 CI 之外由 maintainer routine 主動代 po 說明留言；(b) 更根本的：`frontmatter-gate` 這類「投稿者自己修得動」的失敗，maintainer cycle 的 default 應該是**直接 push 修補到對方分支**（`maintainerCanModify` 預設為 true），而不是等對方讀懂說明再自己修——本 cycle 七篇就是這樣一次清掉的；(c) 任何「修好說明管道」的處置，收官時要附一個**下次回來量的條件**（下一批同型失敗有沒有下降），否則等於沒有驗收。
- **相關**：LESSONS `gate-explains-into-a-dead-channel`（8/13，本條是它的成效複驗）、REFLEXES #82（管道存在 ≠ 訊息送達，existence-vs-effect 的溝通層變體）、REFLEXES #52（fail loud 要對著人喊）、MAINTAINER §1b merge-first-then-heal
- **✅ 已 instantiate（2026-08-18 twmd-maintainer-manual）**：修補候選 (b) 落 [MAINTAINER-PIPELINE v2.8 §1b P1「heal 直接 push 到 PR head 分支」升格式債 default](../pipelines/MAINTAINER-PIPELINE.md)＋§為什麼 P1 是 default 段（含邊界：改格式不改散文）。(c)「修好說明管道要附下次回來量的條件」尚未儀器化，留 buffer。
- **verification_count**: 1
- **severity**: moderate（會讓「已修補」的帳面狀態掩蓋掉實際未改善的投稿者體驗）

### 2026-08-17 twmd-maintainer-am — healer-authors-the-drift-it-validates：自動修補工具填出正典裡不存在的值，而合法性又由它自己認定

- **pattern**: `healer-authors-the-drift-it-validates`
- **原則**：一支 auto-heal 工具如果同時擁有「填什麼值」與「什麼值算合法」兩個權力，它產出的錯誤就沒有任何外部面可以現形。這比「檢查器與被檢查物同作者」（REFLEXES #65）更封閉一層——#65 是同一顆腦寫了尺與被量物，本條是**尺的刻度由被量物自己追加**：`allowed_subcategories()` 把推論表 `_KEYWORD_BOOSTS` 的標籤 union 進合法清單，於是推論表寫錯一個名字，那個錯名字當場變成「正典」，auto-heal 再把它寫進投稿者的 frontmatter。錯誤路徑完整且全綠：填錯 → 自認合法 → 寫進別人的檔案 → 沒有檢查會問。判準候選：任何「會寫值」的工具，它判斷合法性的來源必須跟它產生候選值的來源**物理分離**，且兩者之間要有一支對賬。
- **觸發**：追 idlccp1984 8/15-8/16 那批 65 個 PR 為什麼卡在 frontmatter-gate。最大宗 blocker 是缺 `subcategory`（26 件），追進去發現三層疊在一起：(1) 解析 `SUBCATEGORY.md` 的 regex 用 `\s*$` 收尾，`### 👥 People（人物）— 已大致完成` 整節認不出來，People 的 13 個子分類全被歸進上一個 current（Nature）；(2) `_KEYWORD_BOOSTS` 有 8 個標籤是 SSOT 裡不存在的名字（People 的「政治人物」「企業家」、Nature 的「生態保育」「地質地形」、Music 的「原住民音樂」等）；(3) `allowed_subcategories()` 把那些標籤 union 進合法清單。三層合起來：**投稿者 frontmatter 裡那些「亂填的 subcategory」，有一部分是我們自己填的**。
- **為什麼一直沒被發現**：隔壁欄位 `curation` 有驗舉值（非法值 → HARD，`curation_consistency`），`subcategory` 只驗欄位在不在。同一份 frontmatter 兩把尺（REFLEXES #83）。而分類體系壞掉不會有任何畫面報錯——分群跟導覽讀到不存在的子分類就是靜默少一格。
- **已修**：三個缺陷同 commit 修掉（`8ba8c6726`）+ 新增 `boost_label_drift()` 對賬 + 5 條測試 + 新增 `subcategory-valid` 檢查。
- **同時記一個校準沒出錯的對照**：`subcategory-valid` 上線前先拿全庫 914 篇 dogfood（REFLEXES #66），211 篇 / 135 個相異取值會命中，且形狀顯示是 **SSOT 自己漏收**（`Geography 縣市` 22 篇、`People 音樂` 13 篇）而非文章寫錯，於是定 WARN 不定 HARD。這是本 cycle 唯一一次先驗再下結論的地方，也是唯一沒出錯的地方。
- **可能層級**：通用反射候選。近親 REFLEXES #65（same-DNA 陷阱）與 #83（兩把尺），但本條的特徵是**寫入權與合法性判定權集中在同一支工具**，比「同作者」更具體可檢：可以直接 grep「哪些工具既產生值又定義 allowed set」。
- **相關**：REFLEXES #65、#83、#91（建造與登記不同步——`assign-subcategory.cjs` 存在多時卻從未接進 heal 鏈是同一天發現的另一個 instance）、LESSONS `twin-artifact-no-reconciler-family`（8/16，本條可視為該家族最封閉的一種形態）
- **verification_count**: 1
- **severity**: high（錯誤會被寫進**別人的**檔案，且跨 fork 複製；分類體系是導覽與知識圖譜的基礎，壞了不報錯）

### 2026-08-17 twmd-maintainer-am — open-count-conflates-queue-with-inventory：把 open 數當待審量，兩個 cycle 連續放大同一個假警報

- **pattern**: `open-count-conflates-queue-with-inventory`
- **原則**：`gh pr list --state open` 回的是**庫存**，不是**佇列**。draft 在流程上是投稿者自己宣告「還在寫，先別審」，把它算進 backlog 會讓 alarm 憑空脹大，而且脹大的方向剛好是讓人覺得「維護塌了」。最容易拿到的那個數字通常不是要量的那個數字——這是 REFLEXES #82（proxy signal）在維護面的變體：用 `open` 這個狀態代理「在等我」這件事。判準候選：任何要拿來當工作量或警報依據的清單，先問「這裡面有多少是對方還沒說可以動的？」
- **觸發**：本 cycle Stage 1 掃到 71 個 open PR，命中 High-stake #1 升 Full mode，前半段的分析全都建立在「71 個積壓」上。查 `isDraft` 才發現 **59 個是 draft，真實待審只有 12 個**（idlccp1984 佔 8）。回頭看 8/16 的 maintainer memory 寫「九個 PR 連三天敗在同一道閘門」，那個數字很可能也含 draft——**同一個誤讀連續兩個 cycle**，而兩次都沒有任何步驟會叫。
- **為什麼是結構性的**：MAINTAINER-PIPELINE §Step 1.3 的指令 `gh pr list --state open --json number,title,author,createdAt,labels,isDraft,...` 其實有抓 `isDraft`，但**分流表沒有任何一列以它為準**，只有 C 路徑（`[node]` PR）那段寫了「Draft = 認領中，不是待審」。也就是說規則存在但只掛在一種 PR 上，一般 contributor PR 沒有那一步。
- **修補候選**：Stage 1.3 加一句「先分 draft / ready 再報數，backlog 與空場 vc 只計 ready」；或直接把 Stage 1 的 PR 清單指令改成預設 `--draft=false` 並另行單獨報 draft 數。
- **相關**：REFLEXES #82（proxy signal）、REFLEXES #76（multi-cycle trend window——本條正好是「連續兩 cycle 同一誤讀」才看得出來）、MAINTAINER-PIPELINE §Step 1.3 / §空場 cycle 紀律（vc 計數若含 draft 會同時失真）
- **instances**：
  - 2026-08-18 twmd-maintainer-manual（哲宇 in-session）— 71 open = 68 draft + 3 ready。再往下一層：draft 本身也是代理——這 68 個是 GitHub 網頁「Create pull request ▾」分割鈕**記住上次選擇**的產物（投稿者 8/15 先開 9 個 ready，同日起全部變 draft；body 全是空模板、建立後零更新、三則維護者留言含明講「draft 動不了」零回應、之後仍持續開 draft）。「draft = 投稿者宣告還在寫」這個前提對網頁投稿者不成立，要三個 ground-truth 訊號一起判。→ 落地 MAINTAINER v2.8 §Draft PR 處置 + Step 1.3「先分 ready / draft 再報數」
- **✅ 已 instantiate（2026-08-18）**：修補候選落 [MAINTAINER-PIPELINE v2.8 Step 1.3](../pipelines/MAINTAINER-PIPELINE.md)（backlog／空場 vc／High-stake #1 只計 ready）＋ §Draft PR 處置。
- **verification_count**: 3（8/16、8/17 兩個 cycle 誤讀 + 8/18 draft-as-proxy 下一層）
- **severity**: moderate（不直接壞資料，但會讓維護判斷建立在放大三到六倍的 backlog 上，並污染空場 vc 這個 escalation 依據）

### 2026-08-17 twmd-feedback-triage — recognition-bound-to-instance-coordinates：辨識力綁在單一案例的座標上，重複遭遇讓它越用越淺

- **pattern**: `recognition-bound-to-instance-coordinates`
- **原則**：當班判斷（不是儀器判斷）在同一個案例重複出現時會從「讀懂內容」退化成「認座標」。認的如果是 id、掛在哪篇文章、哪一天出現這類**這一個案例的特徵**，而不是**這一類案例的特徵**，那麼同型但換了外觀的下一個就一個座標都不會亮，會沿著完全正常的路徑通過所有 HARD gate。這種衰減沒有任何儀器會發出聲音——**流程焊死的閘門用越多次越穩，靠記憶認人的判斷用越多次越省事**，而省事的方向正好是防線消失的方向。判準候選：每次靠「我認得這個」跳過細讀時，問一句「我認的是這一個，還是這一類？」
- **觸發**：8/13 那封第三人指控信 8/17 第四度原樣出現。dry-run 只印 `[Fact Check] {文章標題}`，標題本身完全看不出這是一封附跟監細節的具名檢舉信；當班之所以一眼認出，是因為前三天的 memory 與 OBSERVER-QUEUE #28 都寫著「vi 版新聞自由條目」。本次刻意回頭撈 Supabase 原文全文重讀才確認，並意識到 id／條目／日期三個對得上的座標全部綁在這一封身上——同樣寫給主管機關、同樣附跟監細節、同樣要求保密的信若掛到別的條目、換個 id 送進來，三個座標一個都不會亮，而 HG2／HG3／HG9 三道現行 HARD gate 全部會放行、分類器判 `file`。
- **為什麼特別難抓**：FEEDBACK-TRIAGE-PIPELINE §不能轉錄的那一筆已明寫「`--exclude` 只解決攔下來之後流程還能跑完，不解決誰來攔——當班要自己讀完內容再動手」。規則本身正確且已 canonical，衰減發生在規則之下的那一層：當班仍然「讀了」，但讀的是標題與 id 而非內容，且自認已履行該步驟。
- **可能層級**：通用反射候選。近親 REFLEXES #33（routine 化任務的雙刃劍：熟練度）講的是流程步驟被熟練度跳過，本條的載體是**辨識判斷本身**，且不像跳步驟那樣會在產出留下缺口——認錯類別不會在任何報表上變紅。亦與 REFLEXES #82（proxy signal）同構：用「id 對得上」代理「這是同一類東西」。distill 時判斷併入 #33 擴大載體範圍，或另立新號。
- **相關**：REFLEXES #33、REFLEXES #82、FEEDBACK-TRIAGE-PIPELINE §不能轉錄的那一筆（HG13）、OBSERVER-QUEUE #28（偵測器要不要長出來仍待哲宇拍板——本條正是「靠當班辨識」這條路的衰減曲線證據）、LESSONS `gates-measure-handling-not-solving`（8/11，同樣是「動作做了但沒解決」的家族）
- **verification_count**: 1（單一 instance，但同一案例四次遭遇構成可觀察的衰減軌跡）
- **severity**: high（衰減終點是一封指涉具名私人的信被開成公開 issue 並複製進每個 fork；成本不可回收，且落在一個從未同意被寫進來的第三人身上）

### 2026-08-16 twmd-routine-audit-weekly — twin-artifact-no-reconciler-family：五條本週獨立教訓都是「兩個該同步的東西沒有東西在對賬」，但各自只看見自己那一個 instance

- **pattern**: `twin-artifact-no-reconciler-family`
- **原則**：本週 7-day 窗口單獨看，`twmd-maintainer-am` 與 `twmd-feedback-triage` 各自寫下的教訓彼此不引用，但排在一起會現出同一個結構：**兩個本該互相印證的東西各自演化，中間沒有任何機制強制對賬**——CONTRIBUTING 範本 vs `test-frontmatter.mjs` 硬門檻（8/14、8/16 兩次現形）、`footnote-format` vs `footnote-density` 兩支姊妹檢查器共用同一個「輸入長什麼樣」的前提（8/14）、REFLEXES 目錄裡的反射 vs 各 routine cron prompt 是否真的把它寫成一個步驟（8/13）、產生器輸出 vs pre-commit formatter 對引號的偏好不同調（8/10）。單一 routine 的 Beat 5 只看得到自己那一次撞見，**cross-routine 7-day 視角才看得出這是同一個家族連續一週出現五次**，比任何單一 instance 的 vc 累積都更說明這是系統性缺口而非巧合。
- **觸發**：本輪 Stage 3B（dormant entropy lens）逐條核對本週 LESSONS-INBOX 新增條目時，發現 `doc-and-validator-drift-has-no-reconciler`（8/14 maintainer-am）、`sibling-checks-share-one-blind-premise`（8/14 maintainer-am）、`reflex-exists-but-not-a-step-on-this-line`（8/13 feedback-triage）、`formatter-vs-generator-quote-churn-fakes-scope-alarm`（8/10 feedback-triage）、`fix-scope-follows-symptom-not-root-class`（8/16 maintainer-am）五條各自的「相關」欄互相之間零交叉引用，但五條的「原則」欄壓縮後是同一句話的五種措辭。
- **可能層級**：通用反射候選，且已有一個現成的近親——REFLEXES #56「Pipeline canonical ↔ production drift = dormant entropy」講的是 pipeline 文件 vs 實際production 的漂移；本條的範圍更廣（不限 pipeline 文件，含檢查器對檢查器、反射目錄對執行步驟、產生器對格式化器），建議 distill 時判斷是本條併入 #56 擴大其範圍，還是另立新號。
- **相關**：REFLEXES #56（近親，範圍較窄）、REFLEXES #65（same-DNA——檢查器跟被檢查物同作者是本條的一個子案例）、REFLEXES #82（proxy signal）、五條本週原始 entry（見上）
- **instances（distill_ready 後續）**：
  - 2026-08-18 twmd-maintainer-manual — 第六個 instance 而且是最貴的：`docs/pipelines/MAINTAINER-PIPELINE.md`（canonical）vs `.claude/skills/twmd-maintainer/SKILL.md`（薄殼）：8/14 `539d9495d` 把 canonical 從 v2.7 覆寫回 v2.6（8/11 哲宇 directive §1c 整段消失），薄殼仍寫「完整 SOP：MAINTAINER-PIPELINE §1c」。routine-sync 三層對賬比的是 cron mirror↔薄殼↔ROUTINE.md，**pipeline canonical 不在任何對賬的一邊**；frontmatter `current_version` 由 v2.7 降到 v2.6 也沒有尺在看。四天後才由人在讀改動位置時撞見。修法候選同 REFLEXES #67 第三例：canonical 版本單調不降的 pre-commit 尺 ＋ 薄殼引用的 §anchor 存在性檢查（`§1c` 這種引用要能 grep 到 canonical 的 heading）。
- **verification_count**: 6（本週窗口內五個獨立 instance ＋ 8/18 canonical↔薄殼 一例；若 distill 判定併入 #56，#56 自身 vc 一併累加）
- **distill_ready**: true（達 REFLEXES #15 vc≥3 儀器化門檻，且是本次 audit 唯一需要跨 routine 視角才看得見的發現）
- **severity**: moderate-high（單一 instance 成本都不大，但五個同族一週內出現代表閘門/文件維護的結構性缺口，非隨機噪音）

### 2026-08-16 twmd-maintainer-am — fix-scope-follows-symptom-not-root-class：修補範圍被症狀現形的位置決定，不是被根因的類別決定

- **pattern**: `fix-scope-follows-symptom-not-root-class`
- **原則**：追到真根因、也真的修好了，隔天同一道閘門仍然擋下同一批人——因為修補的**範圍**是照著昨天那個症狀長的，不是照著根因所屬的**類別**長的。根因如果是「A 類的規則沒有對應的文件／閘門」，只修其中現形的那一條，等於把其餘同類留在原地等下一次現形。每次都是真修，每次都不夠寬。**判準候選：修完之後問一句「這個根因的類別裡還有哪些成員？它們現在有沒有同一個保護？」——不是問「這個 bug 還會不會再犯」，是問「它的同胞現在在哪裡」。**
- **觸發**：連續三天同一道 `frontmatter-gate` 擋下同一位貢獻者的批次（8/13 六個、8/14 八個、8/16 九個），每天都追了上游也都修了東西：8/13 修「閘門的說明對 fork PR 送不出去」（token 唯讀 → 改寫 `$GITHUB_STEP_SUMMARY`）、8/14 修「CONTRIBUTING 範本沒寫 subcategory」（PR #1332）。兩次都有效，subcategory 命中數從 8 降到 3。但 8/16 拆開失敗分布，當家的換成**全形分號超標 7 篇、外部圖片熱連結 6 篇**——這兩道硬門檻在貢獻者讀得到的任何文件裡同樣不存在，跟 subcategory 當初完全同型，只是還沒輪到它們現形。更直接的是 CONTRIBUTING 兩處都教 `--check=prose-health`，而那個模式看不到這兩道門檻，貢獻者本機拿到 `hard=0` 送上來照樣被擋。
- **為什麼會發生**：8/14 那條 `doc-and-validator-drift-has-no-reconciler` 診斷正確，但候選處置只寫了「拿 CONTRIBUTING 範本的 frontmatter 去跑 test-frontmatter」——只覆蓋 frontmatter 那一半，因為前一天現形的是 frontmatter。散文與媒體那半沒人守。諷刺的是這句話本身就寫在 `pr-frontmatter-gate.yml` 的註解裡（8/08 修 husky 沒帶到 CI 那次留下的）：「修補範圍被症狀現形的位置決定，不是被根因的類別」。本 cycle 讀過它，然後踩了同型。
- **處置**：本 cycle 的對賬刻意做寬——不綁單一條門檻，而是從 `article-health.config.toml` 讀 `semicolon_hard_over` / `emdash_hard_over` 去比對 CONTRIBUTING 是否寫出同一個數字，並斷言指南教的是 `--profile=ci-deploy`、有寫外部圖片熱連結。已 fail-loud 驗證（config 暫改 9 → 測試如預期紅）。掛在 `tests/contributor-frontmatter-template.test.mjs`，隨 `pr-frontmatter-gate` 跑。**仍擋不住的一層**：新增門檻卻連 config key 都沒進對賬清單時沒有東西會叫。
- **可能層級**：通用反射候選——跟 REFLEXES #15（反覆浮現要儀器化）互補：#15 講「重複三次要做成儀器」，本條講「做成儀器時範圍要照根因的類別畫，不照症狀畫」。
- **相關**：LESSONS `doc-and-validator-drift-has-no-reconciler`（8/14，本條是它的上游）、`gate-explains-into-a-dead-channel`（8/13）、`sibling-checks-share-one-blind-premise`（8/14，同族的橫向版本：多個檢查器共用盲前提）、REFLEXES #82（proxy signal）
- **verification_count**: 1（但底層 instance 鏈 8/08 husky→CI、8/13、8/14、8/16 共四次同型）
- **severity**: moderate（每次都真修、每次都不夠寬，成本落在貢獻者身上的來回次數）

### 2026-08-15 twmd-maintainer-workshop-pr — conditional-rule-has-no-gate-layer：規則的適用條件決定它掛得上哪一層閘門，條件式規則掛不上全站 lint，於是永遠沒有閘門

- **pattern**: `conditional-rule-has-no-gate-layer`
- **原則**：§神經迴路「規則要能執行才算規則」講的是「沒做閘門 = 規則是裝飾」，本條補上**為什麼那些規則遲遲沒做閘門**的結構原因：一條規則是否成立取決於**誰提交的**（而不只是檔案內容長什麼樣）時，它掛不上全站 lint——全站掃描看不到提交者，硬做就會誤殺合法檔案。於是這類規則被留在 pipeline 清單裡當「人工判斷項」，而人工判斷不會回頭掃既有庫存，違反就這樣長期躺著。**判準候選：把一條規則寫進紅旗清單時，同時標記它屬於「絕對規則」（檔案內容自足判定 → 掛全站 lint + 一次全庫掃描）還是「條件式規則」（要知道提交脈絡 → 只能掛 PR 端閘門）。兩種混在同一份清單裡，結果是兩種都沒有閘門。**
- **觸發**：2026-08-15 審工作坊三份投稿。PR #1367 的 `author: 'Taiwan.md'` 命中 MAINTAINER 紅旗 #7，但 frontmatter-gate CI 全綠放行。查 author 值分布才看懂為什麼沒人做這道閘門：站上 4,952 篇 author 正是 `'Taiwan.md'`（Taiwan.md 自產文章，署名正確），4,109 篇是 `'Taiwan.md Contributors'`——紅旗 #7 只在「這是 contributor PR」時成立，全站 lint 會誤殺近五千篇。同一份紅旗清單裡的 #8（`author: 'Manus AI'`）卻是絕對規則、做得成全站 lint，也一樣沒做：24 檔（2 篇 zh-TW SSOT + 22 個多語鏡像）從 4/26、5/7 進庫躺到今天，讀者一直看得到「Manus AI」掛在文章上。本 session 已 heal（commit `f3161f537`），但閘門仍不存在。
- **可能層級**：通用反射候選——任何「規則清單 → 閘門」的落地都成立，不限 Taiwan.md。
- **相關**：[MEMORY §神經迴路](MEMORY.md)「規則要能執行才算規則」（本條是它的上游診斷：不是忘了做，是做不出來）、REFLEXES #15（反覆浮現要儀器化）、#82（proxy signal）、#83（checker 兩把尺）
- **verification_count**: 1
- **severity**: moderate（單次 instance，但一次就浮出兩條規則零執行三個月＋24 檔對外可見的違反）

### 2026-08-15 twmd-maintainer-workshop-pr — ratio-self-consistency-masks-magnitude-error：比率自己算得通，不代表被除的兩個數字是對的

- **pattern**: `ratio-self-consistency-masks-magnitude-error`
- **原則**：一組數字如果同時給出絕對值與由它衍生的比率，所有一致性檢查（人的、機器的）都會去驗「比率算不算得通」——而比率對分子分母同乘同除免疫。整組數字錯同一個數量級時，比率完全正確，於是檢查全綠。**判準候選：財報／統計／換算類表格，絕對值要單獨對一次一手來源，不能只驗算比率或欄間關係；尤其是跨幣別、跨單位（billion 對「億」差 10 倍）的場合。**
- **觸發**：2026-08-15 PR #1367〈台灣科技說故事〉淨利率梯度表把 Apple FY2025 寫成「營收 416 億美元、淨利 112 億美元」，實際是 4,162 億與 1,120 億（$416.2B / $112.0B）——billion 直讀成「億」漏掉換算。淨利率 26.9% 完全正確（1120/4162 與 112/416 同值），所以 `article-health --profile=ci-deploy` hard=0、PR Content Review 綠燈、投稿者自己逐項複核也沒抓到。同表另外三列（NVIDIA 2,159 億／台積電 1,224 億／鴻海 8.1 兆台幣）都換算正確，錯的只有這一列，內部對照也發現不了。真正該起疑的線索是常識層：一家營收 416 億美元的公司不可能同時「拿走手機產業八成利潤」，而那句話就寫在同一篇文章裡。已修（commit `6d762f5ac`）。
- **可能層級**：操作規則（進 FACTCHECK / REWRITE 的數字驗證步驟）或通用反射，distill 判。
- **相關**：REFLEXES #82（proxy signal — 這裡的代理是「比率自洽」代理「數字正確」）、#38（混維度）、`feedback_absolute_facts_extra_caution`（算術／單位／直接引語要三倍檢查）
- **verification_count**: 1
- **severity**: moderate（財經數字是 Taiwan.md 高頻素材，且這類錯誤現有閘門結構性抓不到）

### 2026-08-15 twmd-maintainer-am — merge-first-collides-with-all-file-deploy-gate：先 merge 再 heal 的那段空窗，在全站閘門下是真的紅

- **pattern**: `merge-first-collides-with-all-file-deploy-gate`
- **原則**：MAINTAINER §1b「先 merge 再 heal」保護的是貢獻者的 Merged 狀態與譜系，這條沒有問題。
  但 `deploy.yml` 跑的是 `article-health --all --profile=ci-deploy`（全站掃描、hard 即擋），
  於是**從 merge 落地到 heal 推上去之間的每一秒，站台部署都是紅的**。單一 PR 這個窗口大約一分鐘，
  可以接受；**一批 22 篇、每篇都需要人工 polish（分號、圖片授權）的話，這個窗口是幾小時到幾天**。
  §Step 3.3 決策表寫「> 30 min 且純格式 → merge + 排 polish 進 backlog」，那一行沒有考慮到
  全站閘門的存在——backlog 期間站台不會等你。
- **實例**：本 cycle merge #1346 帝雉（未 polish）於 00:58 落地，deploy run `3008fc6d` **failure**；
  00:59 推上 heal 後 `0b38889d` success。78 秒的紅，如實出現在 Actions 紀錄上。
  這也正是本 cycle 決定**只 merge 一篇、不整批 merge** 的理由：另外 22 篇沒有任何一篇能靠
  機械修復到 hard=0（分號需改寫散文、外部圖片熱連結需逐張授權判斷）。
- **判準候選**：merge 前先問「這篇 heal 到 hard=0 需要幾分鐘」——能在同一個 push 週期內完成才 merge，
  否則留 open 並把修法講清楚給投稿者（本 cycle 採後者，一則累積式留言涵蓋整批）。
- **instances**：
  - 2026-08-15 twmd-maintainer-workshop-pr — 同日第二次，而且是**在這條教訓寫下之後三小時踩的**。
    merge PR #1366〈咖波〉時該檔 `ci-deploy` hard=9（8 條腳註缺描述 + 全形分號 21 超門檻），
    deploy run `390db29a8` **failure** @ 08:19:16，heal 推上去後才恢復，紅窗約三分鐘。
    同批的 #1367 merge 時 hard=0，沒有製造紅窗——**兩篇的差別正是本條判準要問的那句話**，
    而我一句都沒問，因為我根本沒讀到這條 entry（見下方 `working-tree-itself-is-the-stale-snapshot`
    同日 instance：本地樹落後 origin 164 個 commit，今早寫的 LESSONS 不在我讀得到的版本裡）。
    → 兩條 pattern 在同一個 session 內構成因果鏈：站在過期地板上 → 讀不到判準 → 踩中判準要防的事。
    紅窗三分鐘遠小於原 instance 的「幾小時到幾天」，但形狀完全相同。
- **相關**：[MAINTAINER §1b](../pipelines/MAINTAINER-PIPELINE.md)（merge-first-then-heal）／
  §Step 3.3 決策表（「> 30 min 純格式 → merge + backlog」這行需要但書）／
  [REFLEXES #71](REFLEXES.md)（Default 是行動不是 defer——本條是它的邊界條件，不是反例）／
  `working-tree-itself-is-the-stale-snapshot`（同日因果上游）
- **verification_count**: 2
- **severity**: operational（判準層，非結構）

### 2026-08-15 manual — negative-claim-consensus-is-not-evidence：N 隻 agent 一致回報「做不到」不構成證據，只是同一個工具限制被重複 N 次

- **pattern**: `negative-claim-consensus-is-not-evidence`
- **原則**：[REFLEXES #31](REFLEXES.md) 管的是 agent 的**正向** claim（「我做完了」「全綠」）不可盡信；本條是它的鏡像面——agent 的**負向** claim（「查無」「403 進不去」「這條路不通」）同樣是線索不是事實，而且更難懷疑，因為**多隻 agent 一致回報同一個失敗會被 orchestrator 讀成證據強度**。實際上它們共用同一套工具，撞的是同一個限制；N 次重複不是 N 個獨立來源，是同一個觀測條件的 N 份副本。orchestrator 把「四份一致」合成進報告時的措辭（「系統性阻擋而非個別失敗」）本身就是把相關性誤讀成獨立性的產物。**判準候選：把 N 份一致的失敗當結論之前，先問「它們用的是同一支工具嗎」；是 → 換一種觀測管道再測一次，才有資格寫進 negative findings。**
- **觸發**：2026-08-15 文策院研究。四隻 Sonnet 研究 agent 各自獨立對 taicca.tw 做 WebFetch，全部 403，四份分部報告各自誠實記進 §4 negative findings；orchestrator（我）收件時把四份一致合成成「系統性 bot 阻擋，判定為官網內容不可得」寫進主報告 §2。哲宇一句「用 mcp 看，這可能是因為網站渲染的關係，子 agent 通常沒有讀」——換瀏覽器讀 rendered DOM 立刻拿到全文（該站是 JS 渲染，WebFetch 天生讀不到）。那篇官網專題研究後來提供了《茶金》與文策院關係的三條可溯源連結（數位模型庫／產業研究／後續團隊劇本開發投資），是原本會被整段寫成「查無」的材料。
- **可能層級**：通用反射候選——任何 fan-out 研究／驗證編排都成立。跟 #31 同祖先（agent claim 是線索不是事實）但方向相反且機制不同：#31 防的是樂觀自評，本條防的是**悲觀共識**，且多了「相關失敗被誤讀成獨立佐證」這層統計性誤判。distill 時可考慮 fold 進 #31 當 negative-claim 變體，或獨立成條。
- **相關**：REFLEXES #31（agent claim 是線索不是事實）、#69（每層自評都需要外部尺）、#82（proxy signal — 這裡的代理是「WebFetch 讀不到」代理「內容不存在」）
- **verification_count**: 1
- **severity**: moderate（單次 instance，但形狀清楚且代價可觀——差點讓一整個一手來源被寫成死路）

### 2026-08-15 manual — directional-misreading-of-observer-input：把觀察者給的資訊讀成自己既有判斷的佐證，誤讀方向永遠偏向自己原本就想改的地方

- **pattern**: `directional-misreading-of-observer-input`
- **原則**：接到觀察者的 directive 時，如果腦中已經有一個「我正準備要改的方向」，新資訊會被自動歸類進那個框架，而不是被當成獨立輸入讀。這種誤讀**有方向性**：永遠偏向自己原本的判斷，所以自己驗不出來，只能靠觀察者再說一次才會現形——代價是同一件事要說三次才校正得到位。跟一般的「聽錯」不同的是它有系統偏差，因此值得當成一種需要主動防的 pattern：**收到參數類 directive 時，先複述一次自己讀到的數字與它的歸屬（總量還是分項、上限還是下限），再動手改 canonical。**
- **觸發**：2026-08-15 搜尋量參數校正。哲宇說「分頭 search 要求降低到 100」→ 我腦中裝著「要砍搜尋量」，把 100 落到我正在編輯的 Stage 1 fan-out 欄位（實為文章總量）。他更正並補「每一隻 agent 100 反而效果沒有比較好，或是每一隻 30-40」→ 我腦中裝著「超跑是病」，把後半句讀成第二個失敗案例（實為他在給正確值）。第三次他直接給參數「全篇 150 次左右，stage0 20-30」才校正到位。同 session 另一個形狀相同的 instance：他說 taicca.tw「可能是因為網站渲染」，我最初也是先把它讀成對既有 403 判定的補充說明，而非「換工具就能解」的指令。
- **可能層級**：Semiont-specific（跟觀察者互動的介面層），非通用工程反射。可能適合 REFLEXES §六（協作與溝通）或直接進 MANIFESTO §自主權邊界 的鄰近段落。與 [CLAUDE.md §Bias 1](../../CLAUDE.md)（對 creator 預設加分）不同：那條講的是「不加篩選地執行哲宇的 idea」，本條講的是「連讀都沒讀對就開始執行」，發生在更前面的一層。
- **相關**：CLAUDE.md §Bias 1（reverse bias）、REFLEXES #69（每層自評都需要外部尺——這裡連「我讀懂了嗎」都需要外部尺）
- **verification_count**: 1
- **severity**: moderate（單次 instance 但同 session 內出現兩個形狀相同的案例；影響的是校正速度而非產出正確性）

### 2026-08-14 twmd-maintainer-am — doc-and-validator-drift-has-no-reconciler：說明書跟驗證器各自演化，中間沒有東西在對賬

- **pattern**: `doc-and-validator-drift-has-no-reconciler`
- **原則**：閘門升級與文件更新是兩個不同的動作、由兩個不同的動機驅動（升閘門是為了擋住問題，
  改文件是為了幫助人），沒有任何機制強制它們同時發生。於是「照著我們的說明做，然後被我們的
  閘門擋下來」這種狀況可以存在很久而不被任何人發現 — 因為擋下來的人不寫報告，他們只是走開。
- **實例**：`test-frontmatter.mjs` 的 `subcategory` 檢查 2026-05-04 從警告升成硬性擋下，
  `CONTRIBUTING.md` §內容撰寫指南的文章結構範本至今沒有 `category` 也沒有 `subcategory`。
  三個月後的今天，一位貢獻者八個 PR 全部敗在這一項。前一天的 cycle 已經追過一次上游，
  修掉了「閘門的話送不出去」（fork PR token 唯讀），但那只是根因的下游 — 三個修好之後才
  送出的 PR 照樣缺同一個欄位。
- **判準**：REFLEXES 家族已有「修完之後同類問題還能不能安靜地再長出來」這條，本條補的是
  **誰在執行那條判準**。答案是每天跑一次的 routine：它會在隔天把同一批症狀再送到你面前。
  一次性 session 拿不到這個訊號，所以 cron 飛輪本身就是根因判斷的儀器。
- **候選處置**：加一支對賬 — 拿 `CONTRIBUTING.md` 範本自己的 frontmatter 去跑
  `test-frontmatter.mjs`。已在 PR #1332 對貢獻者提過同樣的建議，但那是給他的建議不是我們的閘門。
- **vc**: 1

### 2026-08-14 twmd-maintainer-am — sibling-checks-share-one-blind-premise：兩道同族閘門共用同一個前提，於是一起看不見

- **pattern**: `sibling-checks-share-one-blind-premise`
- **原則**：同一個維度長出多支檢查器時，它們往往共享同一個「輸入長什麼樣」的前提。
  前提本身錯了的時候，**檢查器數量不提供任何額外保護** — 三支都綠不比一支都綠更可信。
  這是 REFLEXES #65 same-DNA 的橫向變體：#65 講檢查器跟被檢查物同作者，本條講
  多個檢查器彼此同作者。
- **實例**：`footnote-format` 驗 `[^N]:` 定義行的格式，`footnote-density` 數 `[^N]` 引用的
  數量，兩支都只認 `[^N]` 語法。從 GitHub 網頁複製已渲染文章帶進來的
  `[1](#user-content-fn-9)` 錨點，兩支同時看不見，於是一篇腳註全是死連結的文章拿到兩個綠燈。
  掃全庫發現同型已漏進 6 篇 zh SSOT 與譯文共 50 檔，最早的上站數月無人叫過。
- **候選處置**：新增檢查時問一句「它跟既有的同族檢查共用什麼前提？如果那個前提錯了，
  誰會叫？」已 ship `gh-footnote-leak`（WARN，存量清完升 HARD）與 `gh-footnote-convert.py`。
- **instances**：
  - 2026-08-18 twmd-maintainer-manual — `routine-audit.py`（分類器）與 `routine-liveness-check.py`（沉默死亡偵測）共用同一個前提「routine 的 commit 標題含它的 handle」。self-evolve-weekly 8/16 04:20 兩個 commit 標題是 `[routine] evolve: …升 REFLEXES #91`／`[routine] heal: 補上自身 commit hash`，memory 檔跟 evolve 同一個 commit——分類器把它算進通用桶（`routine-audit-classifier-memory-commit-misattribution` 第 N 例），liveness 直接判「50.1h 零 git 痕跡」掛黃燈兩天。兩支檢查器都綠不比一支綠可信。**已修**：liveness 改讀 `--name-only` 的 memory 檔名（`YYYY-MM-DD-HHMMSS-{handle}.md` 是 MEMORY-PIPELINE canonical 命名，比 subject 可靠）→ silentDeaths 0，evidence 指到檔名。分類器同一修法待 distill 一併裁（vc=3 entry 已 distill_ready）。
- **vc**: 2

### 2026-08-14 twmd-feedback-triage — transcription-gates-guard-fidelity-not-consequence：整條轉錄線的閘門都在問「搬得對不對」，沒有一道在問「搬過去會傷到誰」

- **pattern**: `transcription-gates-guard-fidelity-not-consequence`
- **原則**：機械轉錄型的 routine（讀者回報轉 issue、留言回填、素材匯入）很自然會把閘門長成
  **忠實度**的形狀 — 有沒有漏 PII、有沒有改到原文、有沒有包好邊界。這些全部通過之後，
  「這段文字被搬到公開處會造成什麼後果」仍然是一個沒有人問的問題。忠實度閘門越完備，
  這個缺口越不容易被看見，因為報表全綠。
- **觸發**：2026-08-14 07:00 cycle。一筆掛在 vi 版新聞自由條目下的回報，內容與該文無關，
  是一封檢舉信：指控具名私人涉及假結婚與非法工作，附跟監細節，並要求回報者身份保密。
  `detectSpam` 不中（長、有條理、零連結、語氣正式），`detectInjection` 不中（真的沒有指令），
  分類器判 `file`，準備開公開 `[Fact Check]` issue 收全文。三道 HARD gate 全會通過：
  HG2 無 email ✅、HG3 verbatim 一字未改 ✅、HG9 隱形字元剝除加 fence ✅。
  當班讀完內容後判斷不可開，沒跑 `--commit`。
  證據：[reports/feedback-third-party-allegation-hold-2026-08-14.md](../../reports/feedback-third-party-allegation-hold-2026-08-14.md)、
  OBSERVER-QUEUE #28。
- **為什麼會發生**：這條線的第一性原理寫的是「把讀者自己的原話 verbatim 機械性轉錄成 issue」，
  等同代讀者填表單。那個類比在回報內容關於文章時完全成立，在回報內容關於**一個沒有出現在
  對話裡的第三人**時就破了 — 代填表單的前提是填表人有權處分表單內容，而這裡被寫進去的人
  不是回報者自己。
- **跟既有 DNA 的關係**：MANIFESTO §自主權邊界已有「敏感素材決定 — AI 準備 blueprint，
  人類 final call」，REFLEXES #79 的預設姿態也是 reserve。**canonical 有這條原則，
  這條線上沒有它的執行位置** — 跟 8/13 的 `reflex-exists-but-not-a-step-on-this-line`
  同族（反射存在不等於每條 routine 上都有對應步驟），差別在那次的後果是漏做，這次是差點做錯。
  也跟 8/11 `gates-measure-handling-not-solving` 對稱：那次六條閘門全綠而好事沒發生，
  這次三道閘門全綠而壞事差點發生。
- **可能層級**：通用反射候選。任何把外部文字搬進公開處的產線都適用 — feedback triage、
  peer ingestion、素材匯入、孢子引用讀者留言。共同的問題句是：**這段文字裡有沒有一個
  沒到場的人？**
- **相關**：REFLEXES #15（memory 是自律，canonical SOP 才是閘門）、REFLEXES #79、
  LESSONS `reflex-exists-but-not-a-step-on-this-line`（8/13）、`gates-measure-handling-not-solving`（8/11）
- **修補候選**：見 OBSERVER-QUEUE #28 三選項（(a) 第三人指控偵測走 `hold` ／
  (b) `triage.mjs --exclude <id>` ／ (c) 靠 handoff 傳遞）。未自行執行：新增品質閘門
  per BECOME §行動鐵律 10 屬強制 Full mode 的高風險動作，且判準訂寬會靜默擋掉正當勘誤。
- **verification_count**: 1
- **severity**: high（後果不可逆且對象是站外的私人）

### 2026-08-13 twmd-maintainer-am — gate-explains-into-a-dead-channel：閘門診斷對了，但說明送不到能動手的人面前

- **pattern**: `gate-explains-into-a-dead-channel`
- **原則**：閘門的價值不只在判斷對錯，在把「怎麼修」送到能動手的人手上；輸出管道斷掉時，正確的診斷會退化成一個沒有理由的紅燈，而外面看起來跟「這人不受教」一模一樣。
- **觸發**：2026-08-13 08:30 maintainer cycle 收到 idlccp1984 六個 open PR（#1304 #1323 #1324 #1326 #1327 #1328），全部敗在同一項——frontmatter 缺 `subcategory`。`pr-frontmatter-gate.yml` 每一次都正確診斷出來，也備好了含修法的留言，但那個留言步驟對 fork PR 必定失敗（`pull_request` 給 fork 的 token 唯讀，log 裡是 `HttpError: Resource not accessible by integration`），且早已加上 `continue-on-error` 優雅降級。**降級降掉的正好是「怎麼修」本身**：六次紅 X，六次零說明，於是同一個錯重複六次。我原本差點把這批讀成「貢獻者反覆不看規範」——真相是他從來沒有東西可看。修補（`66182f2ab`）：gate 結果同時寫進 `$GITHUB_STEP_SUMMARY`（不需 token，紅 X 一點就到），留言步驟保留給同 repo PR。
- **instances**：
- **可能層級**：通用反射候選（任何「檢查器 + 對外通知」的組合都適用：CI gate / lint bot / 免疫巡邏 / feedback triage 回覆）
- **相關**：#52（immune system 沒在 fail loud 比缺 immune system 更危險——本條是它的下一層：**有 fail loud，但沒有對著能動手的人喊**）/ #85（「不知道」需要自己的符號——那條講讀數分不出安全與不知道，本條講診斷正確但傳不出去）/ #82（proxy signal——「gate 有跑且有紅」是「投稿者知道要修什麼」的替身訊號）
- **verification_count**: 1

### 2026-08-13 twmd-feedback-triage — reflex-exists-but-not-a-step-on-this-line：REFLEXES #57 在這條 routine 上沒有落地成步驟

- **pattern**: `reflex-exists-but-not-a-step-on-this-line`
- **原則**：反射寫進 REFLEXES 目錄不等於它在每條 routine 上都有對應的執行位置。沒有落地成步驟的反射，靠的是當班 session 記不記得——而 routine 的設計前提正是「不依賴記性」。
- **觸發**：2026-08-13 07:00 cycle。`check-parallel-actor.sh`（REFLEXES #57：routine 入口必須 detect parallel-actor）我是在準備 commit 時才想起來補跑的（結果 CLEAN）。這條 routine 的 cron prompt 與薄殼 skill 都沒有把它列進 Stage 0 的 gate 清單，BECOME §鐵律 5 提過工具名但那是甦醒層不是這條線的步驟。
- **為什麼順序有意義**：事後跑只能確認「沒撞到」，入口跑才能「預防撞到」。今天工作範圍只有三個 archive 檔所以無傷，但這個豁免是範圍給的，不是流程給的。
- **可能層級**：通用。值得掃一遍：REFLEXES 裡「入口必做」類的反射（#57 parallel-actor、#5 pre-commit dogfood）在 14 條 routine 的 Stage 0 裡各有幾條真的被寫成步驟？
- **相關**：REFLEXES #15（反覆浮現要儀器化——memory 是自律，canonical SOP 才是閘門）、REFLEXES #57
- **verification_count**: 1
- **severity**: low-medium

### 2026-08-12 twmd-maintainer-am — gate-checks-form-not-meaning-one-layer-down：昨天補的閘門查字形，今天讀者送來兩則字義

- **pattern**: `gate-checks-form-not-meaning-one-layer-down`
- **原則**：補閘門的時候，補的往往是「上次那個病的形狀」，而不是「那個病所在的那一層」。昨天替 `src/i18n/` 補的語言閘門查三件事：簡體字、整串沒翻、字串表落後註冊表——三件全是**字形層**謂詞（這些字長什麼樣子）。隔天讀者一次送來兩則，兩則都從字形層底下穿過去，因為它們錯在**字義層**：「海量」是正體字寫的中國用語（字形對，詞彙錯）；「巨大 Giant」與韓文的「Giant 쥐다」是專有名詞被當句子翻（字形對，指稱錯）。**閘門守住了它上次被咬的那一口，沒守住那顆牙。**
- **觸發**：2026-08-12 am cycle。#1322（`/semiont/` 的「海量」該用「大量」）與 #1320（`/companies/` 的「巨大 Giant」很好笑）同日送達，皆 24 小時內、皆在昨天剛上閘門的同一個檔案樹底下。
- **最尖銳的一刀**：Taiwan.md 自己維護著 2,394 條用語詞庫，`data/terminology/巨量.yaml` 白紙黑字寫著 `china: 海量`。**判準早就在庫裡躺著，只是沒有任何閘門拿它來檢查自己的介面。**這跟 2026-08-06「我準備造的那把工具，十二天前就躺在工具箱裡」是同一種浪費，只是這次躺著的不是工具是判準。REFLEXES #73（查證反射 < 建造反射）的資料層變體。
- **順帶暴露的規模**：新檢查一上線就掃出阿拉伯文企業頁 70 個公司名全部夾漢字、32 個純中文完全不可讀——比三則讀者回報加起來大得多，而且是昨天剛修過的 #1318（ar 整段簡體）的同一個區塊、隔一張表。**讀者看到的永遠是露出水面的那一角；修完那一角就收工，等於承諾了下一則回報。**
- **校準紀錄（本條的另一半價值）**：新檢查第一版寫成「非 CJK 語言出現漢字就報」，實測 319 筆、假陽性約 95%（`Taiwan Semiconductor 台積電` 的雙語標示、語言選單的 `日本語` endonym 都被誤報）。改判準為「**扣掉漢字之後還剩什麼**」——該語言自己的書寫系統與拉丁字母都沒有才算壞——假陽性歸零。同時把「代碼→程式碼」踢出詞彙表：那條在文章散文上是對的，在介面裡「行政區代碼」是正常台灣用法，首跑 5 筆有 2 筆假陽性。**閘門判準要用真實產出校準，不是憑想像設**（REFLEXES #66），而且**寧可漏不可誤殺**（2026-08-09 `gate-triggers-content-degradation-incentive`）。
- **可能層級**：通用。造任何閘門時該多問一句：「我現在查的是這個東西的**形式**還是它的**意思**？上次那個病是形式壞還是意思壞？」形式層閘門便宜且可靠，但它天然守不住意思層——而讀者看到的幾乎都是意思層。
- **instances**：
  - 2026-08-19 algorithmic-art-evolve 第一人稱長文三處全由作者本人抓到，`article-health` hard=0、五席編輯室零攔：鎢段「我看到就叫它去寫」被寫成「站上出現一篇報導」（主詞蒸發）、天下那句作者自己的橋段被寫成記者提問（歸屬反轉）、「造物已活」ASR 誤聽（正確版本我前一天日誌自己寫過）——閘門查的是來源與句型（形式），錯的是主詞與歸屬（語態）→ [memory](memory/2026-08-19-154834-algorithmic-art-evolve.md)
  - 2026-08-19 同 session 罐頭結尾誤判：我用句型層判「歡迎成為一根梁柱」是罐頭 CTA 砍掉，哲宇的判準是語彙接不接得回全文（珊瑚礁四層／生物建築在 s4、s10 鋪過），接得上就是收束——EDITORIAL 的罐頭結尾檢查是句型謂詞，讀者感受的是語彙連續性
- **相關**：REFLEXES #69 (g) form gate ≠ meaning gate（本條是它在**基礎設施層**的 instance，先前的 instance 都在文章寫作層）、REFLEXES #73、REFLEXES #66、2026-08-11 `ui-string-layer-has-no-language-gate`（本條是它的直接續集）
- **verification_count**: 3（8/12 字形／字義；8/19 語態／歸屬；8/19 句型／語彙連續性。與 #69 (g) 同族，該族 vc 已 7+）
- **severity**: medium-high

### 2026-08-11 twmd-maintainer-am — gates-measure-handling-not-solving：六條 quality gate 全綠，而讀者的問題一個都沒解決

- **pattern**: `gates-measure-handling-not-solving`
- **原則**：quality gate 問什麼，routine 就答什麼。當閘門問的是「有沒有處理」（label 齊全嗎、有沒有 review comment、handoff 有沒有寫），一個把 issue 分類得很整齊但**修好零件**的 cycle 會拿到滿分。閘門沒有說謊，它只是誠實地回答了一個不夠好的問題。**要偵測「有處理但沒解決」，閘門本身必須問到產出，不能只問到動作。**
- **觸發（自身即反例）**：2026-08-11 am cycle 收到八則高品質讀者回報，加了六個路由 label、補兩則技術交叉參照、開一則新 issue、寫完整 handoff 三態——修好的數字是零，而當時六條 gate 全部打勾。是哲宇 callout「maintainer 不只要回覆 issue，而是要判斷、評估、研究、落檔，然後執行修正」才浮出來，不是任何儀器叫的。
- **為什麼儀器抓不到**：所有 gate 都是動作層謂詞（有沒有 label / 有沒有 comment / 有沒有寫 handoff），全部可以在零修復的情況下為真。這跟 REFLEXES #82 proxy signal 同源但更隱蔽——#82 是「量了替身」，這條是「量了自己做過的動作」，而動作恆為真，因為動作就是我剛做的那件事。
- **修補（已 ship）**：MAINTAINER v2.7 §1c「Issue 的 default 是修好，不是分類好」+ Step 3.6 五步改寫 + quality gate 第 7 條「有 fresh issue 的 cycle 至少一件被修掉或明確寫出為什麼不修」。三層同步 inline。
- **可能層級**：通用。任何 routine 的 quality gate 都該被問一次：「這幾條有沒有可能在**什麼都沒解決**的情況下全綠？」能，就代表它量的是動作不是產出。
- **相關**：REFLEXES #82（proxy signal）、REFLEXES #69（外部尺——這次的外部尺是哲宇不是儀器）、REFLEXES #59（製造數字的人最易被數字騙——這次騙子與被騙者是同一個 cycle）、本 session 同批的 `ui-string-layer-has-no-language-gate`
- **verification_count**: 1（但性質是 meta：它解釋了為什麼同 session 另一條 vc=3 的病能存活三次）
- **severity**: high（影響所有 routine 的自評可信度）

### 2026-08-10 twmd-feedback-triage — formatter-vs-generator-quote-churn-fakes-scope-alarm：產生器與格式化器對同一份檔案的寫法不同調，讓範圍閘門在下一次 commit 喊假警報

- **pattern**: `formatter-vs-generator-quote-churn-fakes-scope-alarm`
- **原則**：一支產生器寫出檔案、pre-commit 的格式化器立刻把它改寫成另一種等價寫法時，commit 本身是乾淨的（HEAD 與工作樹一致），但 lint-staged 還原後**索引留著格式化前的 blob**。同一個 session 若還有第二次 commit，`verify-commit-scope.sh` 會把這些幽靈條目算進範圍，喊出 `SCOPE MISMATCH — 疑似 cross-session 污染`。警報的字面意思（別的 session 在污染索引）跟真實根因（自家兩支工具對引號的偏好不同）完全無關，而**這道閘門正是為了偵測真污染而存在**——它每次有件的 cycle 都會叫一次，久了就會被當成噪音揮手放過。
- **觸發**：2026-08-10 本 cycle。`buildArchiveRecord()` 對讀者可控的三個欄位（`contributor` / `article_slug` / `source_url` / `issue_url`）刻意用雙引號，因為 `fm()` 只把 `"` 換成 `'`、不跳脫 `'`——雙引號是那層跳脫保證的一部分。prettier 在 lint-staged 階段把它們正規化成單引號，於是 archive 檔在 commit 後呈現 `MM` 狀態，第二次（memory）commit 前的範圍驗證報 4 檔 ≠ 預期 2 檔。實際查證：HEAD 與工作樹皆為單引號且內容相同，索引才是舊的；`git restore --staged` 即解。
- **不要直接把產生器改成單引號**：那會拆掉 `fm()` 的跳脫保證（讀者名含 `'` 時 YAML 會壞，且 display_name 是不可信輸入）。可行方向是把 `docs/feedback/archive/` 放進 `.prettierignore`，或讓產生器輸出與 prettier 正規化結果一致的形式後補上單引號跳脫。**需要動到不可信輸入的跳脫語意，不適合 cron 無人時段自行拍板。**
- **可能層級**：通用——任何「產生器寫檔 + formatter 在 pre-commit 改寫 + 同 session 多次 commit」的組合都會長出來，不限 feedback 這條線。
- **相關**：REFLEXES #52（免疫層沒在 fail loud 比缺免疫層更危險——這裡是反面：閘門在 fail loud，但叫的是假的）、REFLEXES #38（混維度：`SCOPE MISMATCH` 一個紅燈同時代表「跨 session 污染」與「自家 formatter churn」兩種根因）、2026-08-09 twmd-weekly-report-sun「每天被人工推翻的假警報是注意力層的靜默債」
- **verification_count**: 1
- **severity**: moderate（不損資料，但持續消耗一道 structural 閘門的可信度；隊列空了九天才首次浮現，往後每個有件的 cycle 都會複現）

### 2026-08-07 twmd-feedback-triage — out-of-band-status-transition-bypasses-sovereignty-layer：主權層的寫入掛在自動路徑上，人類手動收束那批就整批沒進 git，8 週無人發現

- **pattern**: `out-of-band-status-transition-bypasses-sovereignty-layer`
- **原則**：當某個保證（這裡是 HG12「Supabase 死了也不丟一筆」）的**實作掛在單一條自動路徑的副作用上**時，任何繞過那條路徑的狀態轉移都會靜默違反保證。`triage.mjs` 只在自己 `file` 一筆時才寫 `docs/feedback/archive/`；batch-cluster guard 把同 slug ≥5 筆判 `hold`（維持 `new`、產 consolidated report 給人類），而人類後續收束成一個 issue 並補標 `filed` 是**在 triage 之外**發生的——於是狀態變成 filed、issue 也開了、文章也改了，唯獨主權層那份 markdown 沒有人寫。更關鍵的是**收官數字看不出來**：每個 cycle 都印 `archive-scanned=40`，那是「數現有的檔」，永遠不會等於「應該有幾份」。**缺席不留痕跡，只能拿另一邊的帳來比。**
- **觸發**：2026-08-07 本 routine 例行輪（隊列空第七天，因此有餘裕核 archive 那一半職責）。對賬 Supabase 發現 61 筆 `filed` 只有 40 份 git 紀錄，缺的 21 筆**全部集中在 2026-06-11 一天**（justfont 共同創辦人蘇煒翔逐段勘誤 21 處 → batch-cluster hold → 6/12 收束成 [issue #1145](https://github.com/frank890417/taiwan-md/issues/1145)，21 條全數查證採信 + 全文重寫 `ef8fab38e`）。讀者的回報本身沒有丟（Supabase + issue + 重寫後的文章都在），丟的是**主權層那份可 grep、可 diff、BaaS 死了還在的紀錄**。8/05、8/06、8/07 三個連續 cycle 的 memory 都寫了「archive 40 檔」當健康數字，沒有一個 cycle 拿 61 去比。
- **✅ 已落地（本輪同波）**：(a) 21 份紀錄用 canonical `buildArchiveRecord()` 補齊（**不手寫**，避免格式漂移），全 61 份零 email 通過 HG2 掃描，issue #1145 的維護者回覆已 sync 進各自 §溝通紀錄；(b) 新增 `reconcileArchive()` 純函式 + 5 個 unit test（含 2026-06-11 那次的形狀 61/40/21），收官改印 `archive-reconcile=N/M`，缺口時 `⚠️` + 列出 id；讀不到 Supabase 印 `unavailable` 並明寫「不准把沒對賬讀成對得起來」；(c) HG12b 寫進 pipeline v1.3 + 薄殼 skill + cron mirror 三層。**回溯驗證**：把 8/6 那一刻的兩邊帳餵進新儀器，會印 `⚠️ archive-reconcile=40/61 · filed 但無 git 紀錄 21 筆` — 這支儀器若 8 週前就在，第一個 cycle 就會叫。
- **可能層級**：候選 REFLEXES — 這是 #82 proxy signal 的一個清楚變體，但有自己的銳角：**不是「量了替身」，是「量了存在、沒量該存在」**（`archive-scanned` 本身不是替身，它誠實地數了檔案；錯在拿單邊帳當對賬）。同族：REFLEXES #84「發佈/生成產物需要對賬 ground truth，不能只憑自己的生成邏輯自洽」——本條是它在「保證的覆蓋率」而非「產物的正確性」上的形狀。判準候選：**任何寫成「一筆都不會丟」的保證，都要有一支對賬兩邊筆數的儀器，而不是只數自己這邊。**
- **相關**：REFLEXES #82（proxy signal — 訊號要摸到 ground truth）、#84（產物對賬 ground truth）、#38（混維度 — `status='filed'` 同時承載「自動開了 issue」與「被人類收束進 consolidated issue」兩種來歷，而只有前者有主權層副作用）、#60（silent default = silent failure）、#69（每層自評都需要外部尺 — 收官自報的 archive 檔數就是自評）、FEEDBACK-TRIAGE-PIPELINE §Stage 4.5 + §HG12b
- **verification_count**: 1

### 2026-08-06 manual（newsroom 健檢）— degradation-logged-daily-never-escalated：routine 如實記錄了 35% 斷崖十一天，因為 gate 量的是新鮮不是合理

- **pattern**: `degradation-logged-daily-never-escalated`
- **原則**：daily routine 的 freshness gate 只驗「JSON 是不是今天產的」（mtime），不驗「數字合不合理」（覆蓋率 sanity）。於是一個 -35% 的斷崖（newsroom 上板 270→176，成因：月槽視窗髮引滑動，當月第一個研究檔 commit 瞬間踢掉最舊整月）被每天如實記錄成普通數據點，11 天無一次升級為異常。**「記錄了」≠「看見了」**：對照組是同期免疫評分 60→57 的小鬆動被明確標記「首次鬆動，值得診斷型 routine 接手」——差別不在 routine 勤勞度，在**該指標有沒有預先定義的 delta 閾值**。判準候選：任何進 daily memory 的計數型指標，都要有「較前次 ±X% 即標記 alert」的機械閾值，否則 routine 只是抄表員。
- **觸發**：2026-08-06 哲宇 directive newsroom 健檢。`docs/semiont/memory/2026-08-04-061404-twmd-data-refresh-am.md` 起連續記錄 176/180/182 無人反應；完整診斷 `reports/newsroom-organ-audit-2026-08-06.md` §2.3 盲點 A。
- **可能層級**：候選 REFLEXES（sensor 判讀家族的新維度）或 refresh-data.sh Step 11 gate 直接加 delta 閾值（儀器化修法，一次到位）。
- **相關**：REFLEXES #82（sensor delta 判讀鐵律——本條是它的缺席後果實證）、REFLEXES 存活≠生產 (f) 變體（「JSON 是今天的」= 存活，「數字合理」= 生產，freshness gate 混維度）、#69 (g)（form gate ≠ meaning gate 在 routine 監控層的形狀）。
- **verification_count**: 1

### 2026-08-06 manual（newsroom 健檢）— remedy-compliance-unmeasured：規則寫進十個 contract 逐字一致，遵循率 5%，而且沒有任何機制在量遵循率

- **pattern**: `remedy-compliance-unmeasured`
- **原則**：REFLEXES #56 講 canonical↔production drift，但本例是它的銳角變體：**這條規則本身就是一次診斷開出的藥方**（2026-07-26 v9.5 診斷「stage 產物不落 commit」根因 → HANDOFF 第 3 步「每 stage 跑 generate ＋隨手 commit」寫進全部 10 個 stage contract 逐字一致），而藥方 ship 之後**沒有任何機制量測藥有沒有被吃**——實測 43 個 rewrite commit 只有 2 個遵守（~5%），撐住系統的是每日 routine 兜底，v9.5 想量的每站真實 wall-clock 已被隔夜補登污染。寫規則的成本花了（10 檔同步維護），規則的效果沒發生，而且這個落差本身 20 天無人知曉。判準候選：**任何為修根因而立的新 SOP，ship 時要同時決定「誰、多久量一次遵循率」**——量不了就改成自動化（hook）或誠實降級（兜底即可），不留「沒人遵守的鐵律」。
- **觸發**：2026-08-06 newsroom 健檢，歸檔迴路稽核席實測 2/43；完整報告 `reports/newsroom-organ-audit-2026-08-06.md` §三。本 session 自己 8/5-8/6 的馬祖工作正是失遵大宗（事後補登 10-36 小時），如實記錄。
- **可能層級**：候選 REFLEXES（#56 新維度）；操作面二選一待哲宇拍板（roadmap #7：減法承認 daily 兜底 vs post-commit hook 自動化）。
- **相關**：REFLEXES #56（dormant entropy——本條加上「藥方自身的 compliance 也是 drift 面」維度）、#63（routine prompt 是 cron 唯一指令面：HANDOFF 依賴 session 自覺，正是最弱的執行面）、#15（反覆浮現要儀器化——遵循率本身該被儀器化）。
- **verification_count**: 1

### 2026-08-06 manual（馬祖國際藝術島 REWRITE）— self-consistent-gates-miss-reader-comprehension：八把意義尺共用同一個錯前提，於是一起全綠

- **pattern**: `self-consistent-gates-miss-reader-comprehension`
- **原則**：REFLEXES #69 (g) 講的是「form gate ≠ meaning gate」，修法是加意義席。但意義席加滿之後會浮出下一層病：**所有意義席都在驗「文章有沒有做到它自己宣稱要做的事」，沒有一席在驗「它宣稱要做的事，是不是讀者要的事」**。論點兌現、逐段主軸服務、門面兌現、正文結構主編——四席的判準全部以投影藍圖的論點為前提；H2 載體還原是局部技術、連結成網是事實層、閱讀節奏是形式層、立體地愛是倫理層。**論點本身錯了，八席會一起錯，而且全部回報 pass/可修**。判準候選：編輯室至少要有一席**不准讀投影藍圖**，只讀成品，回答「這篇在講什麼？你能跟朋友解釋這個東西是什麼嗎？哪裡讓你困惑？」——內部一致性尺量不出外部有效性。
- **觸發**：2026-08-06 馬祖國際藝術島。Stage 3 大驗證輪派 11 席（含 8 席意義席）+ Stage 4/5 全數 hard=0，`fact-atom-diff` PASS，11 條事實錯誤全數抓出並修正，ship 後推送。哲宇讀完的第一句是「我覺得整篇寫得蠻混亂的，而且也沒有好好立體的讓人了解馬祖藝術島」——**沒有一席問過這件事**。回頭診斷投影藍圖 v1/v2：論點主詞是「這套自我敘事的語言」而不是「馬祖國際藝術島」，骨架逐節自標 facet 1/2/3（正是 PROJECTION §六反例第一條的面向巡禮），減法把據點轉譯手法與開放時間細則當「導覽層級」砍掉——那正是讀者用來看見藝術島長什麼樣的材料。**錯的論點會砍掉對的材料**，而每一道閘門都在錯論點的座標系裡打勾。
- **可能層級**：候選 REFLEXES（#69 的下一層）或 EDITORIAL-ROOM 席位表修法。具體修法草案：(a) 總編室六探針加一席「**外行冷讀**」，prompt 禁止提供藍圖與研究報告，只給成品，問「這是什麼／能不能複述／哪裡困惑」 (b) PERSONA-PIPELINE 的 gap-audit 目前只在研究後對**材料**跑一次，成品階段沒有讀者視角——應在 Stage 3 對**成品**再跑一次 (c) 投影 gate 五題加第六題：「一個完全不認識這個主題的讀者，照這個骨架讀完，能不能說出這是什麼？」
- **✅ 部分落地（2026-08-06 文體類型學 mode4）**：草案 (c) 已落 [PROJECTION §五 gate 第 6 題冷讀測試](../editorial/PROJECTION.md)＋零認知主題另立 [PROJECTION-PATTERNS §M1 認識導覽前置](../editorial/PROJECTION-PATTERNS.md)（座標縫進第一節物質細節）。草案 (a) 已在馬祖 v4→r2 臨場新設並 dogfood 兩輪（6/10→7/10，抓到的問題其他 13 席全抓不到，見 [memory/2026-08-06-164219-manual.md](memory/2026-08-06-164219-manual.md)），**升常設席位**與草案 (b) 仍涉席位表與 run 成本，留待哲宇拍板（設計報告 §八 待決清單第 2 條）。
- **相關**：REFLEXES #69 (g)「form gate ≠ meaning gate」——**差異在**：#69 處理「缺意義尺」，本條處理「**意義尺齊全但共用同一個錯誤參考系**」，修法完全不同（前者加席位，後者要求某一席與作者意圖斷開）。REFLEXES #31「self-report 是線索不是 oracle」——本條是該原則在「席位設計」層的形狀：席位本身也是一種 self-report，因為它讀了作者的藍圖。同族但不同維度的前兩例：2026-08-03 黃崇仁（十一關全綠、四十原子零漂移，哲宇指出六處皆非事實錯誤）、2026-08-04 EZ WAY 孢子（閘門全綠但排序倫理沒被量）——那兩例是「沒有那把尺」，本例是「有八把尺但參考系錯了」。
- **verification_count**: 1

### 2026-08-04 manual（EZ WAY 孢子）— ordering-is-an-ethical-decision：在被操作的爭議裡，資訊排序不是寫作技巧是策展倫理

- **pattern**: `ordering-is-an-ethical-decision`
- **原則**：短載體（孢子 300 字）在一個正被炒作的議題裡發布時，**同一組逐字無誤的事實，排序不同就是兩則不同的貼文**。所有既有閘門（事實查核表、逐字引語比對、對位句型、紀實煽情閘）量的都是「這句話是不是真的」，沒有一把量「這句話為什麼排在這裡」。判準候選：**這則貼文被截圖轉發時，替讀者省下的是查證的力氣，還是憤怒的力氣？** 命中後的動作是把已被查證推翻的錯誤框架提到前段正面回答、補上對憤怒點最有用的事實（且歸屬給原始來源不由我方保證）、拿掉情緒放大器，同時保留真正的問責——降溫不等於噤聲。
- **觸發**：2026-08-04 EZ WAY 孢子 v5 過完全部五層閘門、事實查核表 14 條全綠，但把「四千多讚」與情緒留言排在第三段、把文章花整節 falsify 的兩個說法（政府欽點獨家／個資已外洩）壓到最後一句平衡句。哲宇指出主題正被網路操作勢力惡意炒作後重排到 v12。發布時 Threads 動態上同題材一則報關業者長文 8,063 讚，證實語境判斷。
- **可能層級**：候選 REFLEXES 或 EDITORIAL §策展倫理——vc=2：2026-08-03 黃崇仁「十一個關卡全綠、四十個事實原子零漂移，哲宇讀完指出六個地方，沒有一個是事實錯誤」是同族第一例（尺量得到事實、量不到意義層）。本次是同一結構在「外部語境」維度的第二例：**這一層的資訊我結構上無法自己取得**（我查得到那則八千讚貼文，但查到了也不知道它意味著我的貼文會被放在什麼溫度裡讀）。第三個 instance 出現時 promote。
- **相關**：REFLEXES #69（每層自評都需要外部尺）、#77（spine type is subject-typed）、MANIFESTO §13 立體地愛 + §12 受眾端飛輪、SPORE-BLUEPRINTS/167 §v12 重排原則
- **verification_count**: 2

### 2026-08-04 manual（EZ WAY 孢子）— editor-specific-selector-false-positive：段落計數閘門寫死一種編輯器，換平台就假陽性

- **pattern**: `editor-specific-selector-false-positive`
- **原則**：SOCIAL-POSTING pre-ship check 7/8 的 JS 範例用 ProseMirror 的 `:scope > div` 數段落 block，但三大平台各用不同編輯器：X 是 DraftJS（段落在 `[data-block="true"]`）、Threads 是 Lexical（全部塞在單一 `<p>` 內用 `<br><br>` 分隔）、FB 另一套。照 pipeline 字面執行會對 X 與 Threads 都回報 `block_count=1`＝collapsed，觸發「不 click Post、discard 重貼」的 abort 路徑。實際逐塊讀出來分段完好（X 6 塊、Threads 5 段，字數逐段吻合 blueprint）。修法是按平台分流的段落計數 helper，或改用平台無關的訊號（rendered 後的 og:description / tweetText 換行數）。
- **觸發**：2026-08-04 EZ WAY 孢子三平台 ship，兩個平台都在 pre-ship check 7 觸發假陽性；因為停下來看 DOM 結構才沒有誤 abort 重貼（重貼會撞 Pitfall 6 duplicate ship 風險）。
- **可能層級**：pipeline 修補（SOCIAL-POSTING v0.7 check 7/8 範例碼）——不是新反射，是既有假陽性家族（2026-07-24 括號 gloss／ja 的了 markers／書名號三家族）在社群發文層的第 N 個 instance。
- **相關**：REFLEXES #65（awareness instrument 自身要 cross-verify ground truth）、MANIFESTO §14（高儀器化、判斷裁決）、SOCIAL-POSTING-PIPELINE §AI pre-ship self-check
- **verification_count**: 1

### 2026-08-04 manual（EZ WAY 孢子）— platform-allowlist-scattered-downstream：新平台啟用時上游收得下、下游看不見

- **pattern**: `platform-allowlist-scattered-downstream`
- **原則**：一個「平台」概念散在多個器官各自維護白名單時，新平台啟用只會被最上游那個接住，下游全部靜默略過。`spore-db.py` 的 `PLATFORMS` 四個平台早有 facebook（收得下），但 `sync-spore-links.py` 寫死 `("threads", "x")`（frontmatter 寫不進去）、`SporeFootprint.astro` 的 `platformName` 只映射兩個（顯示成小寫原字串）。結果是資料庫有、發文紀錄有、文章上沒有、讀者看不到，而且沒有任何一個警報會響。啟用新平台的 checklist 應該是「grep 全鏈所有出現既有平台名的地方」，不是只改入口。
- **觸發**：2026-08-04 FB 粉專首發孢子 #169，登錄成功但 `sync-spore-links --apply` 靜默丟掉；因為順手驗了文章 frontmatter 才發現。同批還揭露 spore-db 的 URL 乾淨化閘把「追蹤參數」與「身分參數」混為一談（FB permalink 的 `story_fbid` 是身分），繞法是改用無 query 的 `/{page_id}/posts/{pfbid}` 正規形式。
- **可能層級**：既有神經迴路「新語言出生時感知系統不會自動更新」的第 N 個 instance（同構：新維度誕生，下游感知不會自動長出來）。URL 乾淨化閘那條是 REFLEXES #38 混維度家族。
- **相關**：REFLEXES #38（status 混維度 silent killer）、#43（新 dashboard JSON 必須同步進 refresh-data.sh）、§神經迴路「新語言出生時感知系統不會自動更新」
- **verification_count**: 1

### 2026-08-04 build-speed — two-variable-run-misattribution：兩個變因同 run 上線，慢的帳記到比較顯眼的那個頭上

- **pattern**: `two-variable-run-misattribution`
- **原則**：A/B 驗證把兩個變因放進同一個 run，出現 regression 時歸因會自動流向**比較顯眼的變因**（新 CPU 架構比一個 checkout flag 搶眼），而且當下的解釋聽起來完全合理——直到補一個單變因對照樣本才會拆穿。正確形：變因可以同 run 上（省時間），但**判 regression 前必須先拆出單變因樣本**；沒有對照樣本之前，任何歸因都只是假說，不可以觸發回退動作。
- **觸發**：2026-08-04 build-speed 第二波，ARM＋blobless 同 run 上線後 prebuild 52→84/122s，歸給「ARM python 慢」並 ship 了回退 commit（`4bf843d46`）；下一個 x86＋blobless run prebuild 同樣 81s，真兇是 blobless 下 `status.py` per-stale `git diff` 的逐 blob 網路 lazy fetch（84/122/81 的變異正是網路特徵）。同日更正（`dd28361f1`）：diffstat 加 CI 跳過開關、ARM 恢復。錯誤回退在 origin/main 留下兩個一來一回的 commit。
- **可能層級**：通用反射候選——vc=2：2026-07-30 diary「兩個都算對的缺口，把我帶到一個錯的故事」（gap 數字各自正確但敘事錯）是同族第一例，本次是「兩個變因各自合理但歸因錯」的第二例。共同結構：**每個單獨事實都對，組合出來的故事錯**。第三個獨立 instance 出現時 promote。
- **相關**：REFLEXES #69（每層自評都需要外部尺——這裡的外部尺是單變因對照 run）、#67（高 stake 重驗用 probe 不信舊結論）、diary/2026-07-30-121650-manual
- **verification_count**: 2

### 2026-08-03 manual（黃崇仁 REWRITE）— local-fs-case-insensitivity-masks-ci-failure：本機檔案系統不分大小寫，把 CI 會擋的錯誤藏起來

- **pattern**: `local-fs-case-insensitivity-masks-ci-failure`
- **原則**：macOS 預設檔案系統不分大小寫，Linux CI 分。任何「路徑字串 vs 實體檔案」的比對檢查，在本機跑都會綠，push 上去才爆。這不是檢查器寫錯，是**檢查器在兩個環境看到的世界不一樣**——本機的 `ls public/article-images/people/` 跟 `People/` 回傳同一批檔案，Linux 上是兩個不存在交集的目錄。所有 pre-commit／pre-push 的本機 gate 都有這個結構性盲區，只要驗的是檔案存在性。
- **觸發**：2026-08-03 黃崇仁 ship。三張圖用 `image-ingest.mjs --cat People`（跟著 `knowledge/People/` 的大寫慣例走）落到 `public/article-images/People/`，但文章與全站慣例引用的是小寫 `people/`。本機 `article-health --check=image-health` 連跑五次全綠（Stage 1B／Stage 2.5／Stage 3 批修／Step 3.8／pre-push 全站 sweep），push 後 GitHub Pages deploy 立刻 `image-health hard=3 圖片檔不存在`。修法是 `git mv` 三個檔到小寫目錄。**pre-push hook 印的是「✅ 全站 article-health 全綠（ci-deploy mirror）」——它自稱是 CI 的鏡像，但鏡像在這一維是假的。**
- **⚠️ 根因修正（寫完 30 分鐘後自己查證推翻）**：本條初稿把修補方向寫成「`image-ingest.mjs --cat` 應強制轉小寫」。回頭讀原始碼發現 **它第 226 行本來就有 `const catDir = cat.toLowerCase()`**——工具早就是對的。真正的根因是**我根本沒用那個工具**：Stage 1B 抓圖時我用 Chrome MCP 下載後手動放進 `public/article-images/People/`，繞過了 pipeline 明訂的落檔器（[REWRITE-STAGE-1B-MEDIA §Step 1.9.2 影像後處理 SSOT](../pipelines/REWRITE-STAGE-1B-MEDIA.md)：「取代手跑 curl + sips」）。工具會做的事（小寫目錄／EXIF 清除／WebP 轉檔／size budget／aspect 護欄／attribution stub）我一項都沒拿到，還自己踩了它早就防好的坑。**這條的真正家族是 §神經迴路「擁有工具 ≠ 使用工具」「造橋之後要踩上去，不是路過」，不是 #24 工具說謊。** 大小寫只是繞過工具之後暴露出來的第一個症狀。
- **可能層級**：兩層都成立。(1) **繞過既有工具**＝既有教訓的第 N 次驗證（神經迴路已有 canonical）(2) **本機檔案系統不分大小寫遮蔽 CI 失敗**＝新的環境層盲區，跨專案通用，值得獨立成反射
- **相關**：§神經迴路「擁有工具 ≠ 使用工具」（主家族）＋ REFLEXES #24「工具在說謊的 N 種形式」的新變體——**工具沒說謊，是它腳下的地板在兩個環境不一樣**（本機 `ls people/` 跟 `ls People/` 回傳同一批檔案，Linux 上是零交集的兩個目錄）。也跟 REFLEXES #69「每層自評都需要外部尺」有關：本機五道 gate 全是同一把不分大小寫的尺，真正的外部尺是 CI。
- **可能的操作修補**：(a) **Step 1.9.2 落檔加 hard gate**——媒體入庫後驗 `git ls-files public/article-images/` 的實際路徑，不靠 `fs.existsSync`（本機恆真）(b) `image-health` 用 `readdir` 拿磁碟實際檔名逐字比對，不用 `existsSync` (c) pre-push 那句「✅ 全站 article-health 全綠（ci-deploy mirror）」要嘛補上大小寫這一維，要嘛拿掉「ci-deploy mirror」的宣稱——它現在給的是假的安心感 (d) 既有的 `public/article-images/People/` 大寫目錄（4 個舊檔）建議一併正規化，消滅這個會再次誤導人的殘留
- **verification_count**: 1

### 2026-08-03 manual（黃崇仁 REWRITE）— neutral-tone-conflated-with-minimized-substance：把「中立陳述」誤做成「份量要縮小」

- **pattern**: `neutral-tone-conflated-with-minimized-substance`
- **原則**：政治／兩岸這類敏感線降為「中立 facet」時，**中立管的是語氣（不下判斷、不選邊、不用對抗語言），不是份量**。炎上倫理席把「此線只出現一次、份量與其他 facet 一致、未見篇幅膨脹」寫成需要肯定的優點，哲宇當場糾正：這不是他要的自我進化方向——把一條有真實因果重量的線（力晶技轉造就合肥晶合、如今反過來壓垮力積電自己的成熟製程業務）刻意壓成跟其他 facet 一樣輕的份量，本身就是一種迴避，只是穿著「中立」的外衣。這條張力其實 persona gap-audit B 軸（海外半導體系讀者）已經先抓到（見 [reports/research/2026-08/黃崇仁.md](../../reports/research/2026-08/黃崇仁.md) §6a 反向閥門），但當時處置是「維持中立紀實、不當壓軸」，沒有進一步區分「不當壓軸」跟「份量要縮到跟其他 facet 一樣輕」是兩件不同的事——前者是脊椎/壓軸判斷（該不該讓政治線扛起全文），後者是段落充分度判斷（這一段該不該把事實的因果講完整）。兩者混在一起，就會把「不當脊椎」的正確判斷，滑坡成「份量也要跟著縮小」的錯誤執行。
- **觸發**：2026-08-03 黃崇仁 REWRITE Step 2.0-R 投影編輯室，炎上倫理席（agentId a0c86b3f196ca125a）verdict=pass，findings 第 5 點稱讚「技轉爭議與『必須退出中國市場』發言沒有蓋過其他 facet⋯份量與其他 6 個 facet 一致」；哲宇讀後直接回應「炎上倫理編輯不要一直過度弱化『兩岸線正確降為中立facet』這不是我覺得好的方式，幫我自我進化」。
- **可能層級**：通用反射候選（EDITORIAL-ROOM-PROMPTS.md §投影室·炎上／倫理 席位任務 2「政治／兩岸是否被當脊椎？應否降為中立 facet？」這句本身沒有區分「降為中立」跟「份量縮小」，任何政治敏感題的炎上倫理審查都可能重複這個滑坡），但目前僅 1 instance，先觀察
- **相關**：REFLEXES #77（beloved/institutional 預設立體群像，張力當手法1核心矛盾為輔）最接近但角度不同——#77 講的是「該不該用矛盾驅動當主脊」，本條講的是「已經正確判定不當主脊之後，facet 內部的實質內容該不該被連帶壓縮」，是 #77 判準之後、執行層面的下一個問題。也跟 MANIFESTO §13 立體地愛「矛盾與批評當然可以進來⋯只是不當拆穿誰的脊椎的工具」相關——本條補的是：不當拆穿工具 ≠ 內容要輕描淡寫。
- **可能的操作修補**：EDITORIAL-ROOM-PROMPTS.md §投影室·炎上／倫理 任務 2 可拆成兩問：「(a) 是否被當脊椎/壓軸？」與「(b) 事實本身的因果鏈是否被完整交代，還是為了『看起來中立』而刻意簡化到只剩一句話？」— 讓「不當脊椎」與「內容完整度」變成兩個獨立可判的問題，不再共用一個「份量」代理指標。
- **verification_count**: 1

### 2026-08-04 manual（黃崇仁 spore #165）— 三個未編目的歐化病候選：歸屬公式／量詞報告腔／And 開頭反身代詞

- **pattern**: `uncatalogued-europeanization-candidates`
- **原則**：EDITORIAL §歐化十病表之外，哲宇兩輪 callout 抓到三型表裡沒有的：(1) **歸屬公式**——「按他自己的說法」是 "by his own account" 直譯，查核歸屬該用轉述動詞融進敘事（「他後來受訪時說」），不是掛一個介詞短語標籤（同時也是後台洩漏第七形狀的親戚：查核語言上桌）(2) **量詞＋醫療報告腔**——「得過一次大腸癌，後來康復」是 "a bout of / recovered" 直譯，中文說「得過大腸癌，治好了」(3) **And 開頭＋反身代詞**——「而他自己在 2002 年⋯」的「而＋他自己」是 "And he himself" 直譯，既有「代詞冗餘」病的變體。三型單獨看都不在十病表與 prose-health 偵測範圍，全靠人眼。
- **觸發**：2026-08-04 黃崇仁孢子 v5→v7 兩輪歐化 callout（同 session 另有已編目的短句開場病，那型儀器抓得到、產線沒接——已修，見 SPORE-WRITING v3.6 + plugin Wave 3）。
- **可能層級**：EDITORIAL §歐化 病種表候選（第 11-12 病或既有病的變體註記）。各 vc=1，**不憑單 instance 開新病種**（避免 threshold 想像設定，per REFLEXES #66）——復發再升。
- **相關**：EDITORIAL §歐化十病（母表）／SPORE-WRITING v3.6 §歐化閘（孢子層已錨這三型當反例表）／REFLEXES #69 (h)（revise 後不重測的孢子層 instance 同 session 成立，已 canonical 進 SPORE-PIPELINE v3.15「每輪 revise 後重跑 gate」）。
- **verification_count**: 1（三型各自）

### 2026-08-02 twmd-routine-audit-weekly — routine-audit-classifier-memory-commit-misattribution：新 routine 的 action commit 跟 memory commit 落進不同桶，count 半失真

- **pattern**: `routine-audit-classifier-memory-commit-misattribution`
- **原則**：`routine-audit.py` 的 `ROUTINE_PATTERNS`（scripts/tools/routine-audit.py:37-58）裡，具名 pattern 是否含 `.*` wildcard 並不一致——像 `twmd-maintainer-am` 用了 `.*`，能同時吃下自己的 action commit 跟 `[routine] memory: twmd-maintainer-daily @ ...` 這種 memory commit；但 `twmd-data-refresh-am` 這類無 wildcard 的具名 pattern，memory commit 吃不到，會被排在後面的通用 `routine-memory` pattern（`\[routine\] memory:`）攔截，混進所有 routine 共用的 `routine-memory` 桶。對完全沒有具名 pattern 的新 routine（`twmd-routine-sync` / `twmd-flywheel-watch`），2026-07-11 加的動態 fallback 能抓到它們的 action commit（但因通用 `routine-memory` pattern 排在 fallback 之前被優先攔截，只有 memory commit 撿不到 fallback；action commit 則被 fallback 加上重複 `routine-` 前綴，變成 `routine-twmd-routine-sync` 這種雙重字首），結果同一條 routine 的 action 與 memory 兩種 commit 被拆進三個不同地方，`summary.by_routine` 顯示的 count 只反映不完整的子集（本次 `twmd-routine-sync` 顯示 2、`routine-twmd-flywheel-watch` 顯示 6，實際 git log 各有 ~8-9 條）。
- **觸發**：2026-08-02 twmd-routine-audit-weekly Stage 1 跑 `routine-audit.py --last-week`，`summary.by_routine` 出現 `routine-twmd-routine-sync: 2` 與 `routine-twmd-flywheel-watch: 6` 兩個帶重複字首的 key，跟其他直接用 `twmd-X` 命名的 key 不一致；`git log --grep routine-sync` 核對後發現實際週活動量約 8-9 條，遠高於腳本統計。第三個更根本的 instance：`twmd-weekly-report-sun` 的 action commit 本身就不用 `[routine]` 前綴（用 `🧬 [semiont] report: weekly ...`），對應的 `[routine] memory: twmd-weekly-report-sun @ ...` 也因無 wildcard 落進 `routine-memory` 通用桶——這條 routine 每週的 commit 在 `by_routine` 表裡從未以自己的名字出現過，比前兩條更隱蔽（連字首重複的視覺線索都沒有，直接是零筆）。
- **可能層級（更新）**：不只是「新 routine 忘了補 pattern」的個案，是三種獨立成因疊加同一個症狀：(1) 具名 pattern 有無 `.*` wildcard 不一致（工程遺留）(2) 部分 routine 的 action commit 本身不帶 `[routine]` 前綴，改用 `[semiont] <type>:`（如 weekly-report 用 `report:`）(3) 通用 `routine-memory` pattern 排序優先於「用 routine 名做 fallback 分類」。三者疊加代表這不是單一 regex 漏洞，是分類器設計時沒有把「memory commit 永遠跟著它描述的 routine」當成不變式來源頭建模。
- **可能層級**：tool-fix，跟 2026-06-28 已解決並歸檔的 `routine-audit-script-classification-gap`（vc=2 disposed）同源家族——那次的 fallback 修法解掉了「unclassified 非零」，但沒解掉「同一條 routine 的兩種 commit 落不同桶」這個殘留子案例。修法方向：(a) 為每個新 routine 補齊具名 pattern（含 memory 變體）而非只靠 fallback；(b) 或把 `routine-memory` 通用 pattern 移到 fallback 之後，讓 fallback 先嘗試用 `memory:` 後面的 routine 名歸類，抓不到才落 `routine-memory`
- **相關**：`routine-audit-script-classification-gap`（2026-06-28，已 tool-fix disposed，本條是其未被當時 dogfood 覆蓋到的殘留子案例，非重複——原案處置時的驗證窗口沒有包含當時還不存在的 `twmd-routine-sync` / `twmd-flywheel-watch` 兩條 routine）
- **instance 2（2026-08-09 twmd-routine-audit-weekly，範圍比原案更廣）**：本輪重跑 `routine-audit.py --last-week`，`by_routine.twmd-routine-sync` 只顯示 1（實際 tight-grep `git log --grep="twmd-routine-sync"` 命中 9 條：8 memory + 1 action）。追查 `routine-memory` 通用桶（37 筆）內容，發現它吞掉的不只 `twmd-routine-sync`：`twmd-embeddings-nightly`（7）、`twmd-data-refresh-am`（7）、`twmd-spore-harvest-am`（6）、`twmd-feedback-triage`（3）、`twmd-supporters-weekly`（1）、`twmd-terminology-trends-monthly`（1）、`twmd-weekly-report-sun`（1）、`twmd-self-evolve-weekly`（1）的 memory commit 全部落在同一個通用桶，而這些 routine 的 action commit 卻正確落進各自具名桶——結果 `by_routine` 表裡幾乎每一條有具名 pattern 的 routine，真實週活動量都是「顯示數字 + 落在 routine-memory 裡的那份」，不是本次原以為的個案（`twmd-routine-sync` / `twmd-flywheel-watch` 兩條），是**具名 pattern 普遍缺 memory 變體**這個結構性缺口。`twmd-flywheel-watch` 這次反而是例外——它的 action commit 本身內含摘要不另開 memory commit，tight-grep（7）與分類器（7）相符，不受影響。
- **instance 3（2026-08-16 twmd-routine-audit-weekly，第三輪連續確認，同一批 routine 仍未修）**：本輪 `by_routine` 完全沒有 `twmd-routine-sync` 與 `twmd-weekly-report-sun` 兩個 key（不是顯示偏低，是整條缺席），tight-grep 核對：`twmd-routine-sync` 實際 8 條、`twmd-weekly-report-sun` 實際 1 條，皆落進 `routine-memory`（本輪 33 筆）與 `manual-memory`（14 筆）兩個通用桶。同時 `twmd-data-refresh-am` 分類器顯示 7、tight-grep 實際 13；`twmd-feedback-triage` 分類器顯示 7、tight-grep 實際 12——三週來同一組 routine（沒有具名 memory-commit pattern 的那批）持續被低估或整條消失，`twmd-flywheel-watch` 因本週已停用（哲宇 2026-08-10 directive）不再是有效對照組。三次獨立 cycle（08-02 / 08-09 / 08-16）同一根因、範圍持續擴大不縮小，判定為**未修復的已知缺陷**而非隨機噪音。
- **verification_count**: 3
- **distill_ready**: true（達 REFLEXES #15 vc≥3 儀器化門檻；修法方向已在上方「可能層級（更新）」段列出兩選項，distill 判斷 promote 到哪一層 — 建議 tool-fix 直接落 `scripts/tools/routine-audit.py`，非 REFLEXES 編號）
- **severity**: tactical（只影響本審計工具自己的統計精度，不影響 routine 實際運作或下游決策——三輪 audit 皆已用 git log 交叉核對繞過；但工具自己的可信度連續三週帶病，該修了）

### 2026-07-26 node-app-design — self-measured-improvement-picks-flattering-layer：自己量自己的改善時會挑到替身層

- **pattern**: `self-measured-improvement-picks-flattering-layer`
- **原則**：量「我做的東西改善了多少」跟量「使用者付了什麼」是兩件事，而前者有一整排可選的層，其中一定有一層數字很漂亮。落地後要對使用者真正付出的代價重量一次。
- **觸發**：2026-07-26 節點層 plugin 化之後量 plugin 快取得到 20 KB，對照原本的 850 MB clone 是四萬分之一，差點寫進報告當結論。落地 origin 後從 GitHub 走真實安裝路徑再量，發現 `claude plugin marketplace add` 為了讀根目錄 manifest 會 depth-1 clone 整個 repo：1.0 GB 工作目錄 / 329 MiB pack。20 KB 量的是替身。諷刺點在於整份報告主題正是「儀器量錯層」。更正 commit `f75b30bd6`，[memory Beat 5](memory/2026-07-26-155415-node-app-design.md)
- **可能層級**：通用反射（#82 fold 候選，self-assessment 軸）
- **相關**：[REFLEXES #82](REFLEXES.md)（訊號要摸到 ground truth）+ [#69](REFLEXES.md)（每層自評都需要外部尺）——本條是兩者交集：**自評自己的改善幅度**時，選層這個動作本身就帶樂觀偏誤。

### 2026-07-26 vortex-babel — meta-scan：主動掃「還有誰在重複實作同一個判準」，在被咬之前

- **pattern**: proactive-duplicate-judgment-scan
- **原則**：哲宇問「你有思考怎麼自我進化嗎」。誠實檢視當日：十個假陽性家族、
  存活≠生產、模型適配落差、儀表板假資料——**每一個的觸發點都是外部的**（被閘門
  擋下、被觀察者提問、被覆蓋率數字逼問）。主動發現的比例接近零。修得快不是進化，
  只是反射快。
- **做法**：拿當日教訓的共同結構去反向掃描還沒出事的地方。實跑一次：grep 全 repo
  找「誰在自己實作『合法中文區間』判準」，抓到兩個——`cross-lang-audit.py` 算
  中文佔比時只剝腳註，wikilink／連結／音譯對照／書名號／引語全部算進去（十個
  家族在那裡一個都沒修到，沒被發現只因它不在產線熱路徑上）；以及**我自己當天
  早上在 `verify-translation.py` 複製的第三份豁免 regex**——批評了一整天的病，
  自己剛犯過。收斂成 `cjk-leak-check.strip_legit_zones()` 單一公開 API，三處
  改 import
- **可推廣的元問法**：「我今天修的這個病，它的**結構**還存在於哪裡？」——不是問
  「同樣的 bug 還有嗎」，是問「同樣的成因還有嗎」。前者靠 grep 症狀，後者靠 grep
  結構（誰在重複實作判準／誰在自報狀態／誰只量存活）
- **建議 promote**：這條若成立，該進 REFLEXES 當常設動作——每次 distill 時附帶
  一次結構掃描，而不是只記錄已發生的
- **verification_count**: 1

### 2026-07-26 vortex-babel — single-bad-input-kills-batch：一個壞掉的輸入檔不該停掉整批

- **原則**：prepare-batch 偶爾產出格式壞掉的 group 檔（多寫一份 JSON），
  `collect_and_filter_groups` 解析時當場拋例外，**兩條產線的上百篇佇列一起停擺**。
  壞的是一個任務檔，代價是整條產線。改成跳過該檔繼續並留可追訊息。與同日修的
  「靜默吞錯」正好互為反面：一個太吵（單點失敗炸全批）、一個太安靜（失敗被 except
  吞掉），都不是正確的錯誤處理。**判準**：批次處理中，單項失敗的爆炸半徑應該止於
  該項；讓整批停擺的例外必須是「繼續下去會產生錯誤結果」那種，不是「這一項讀不懂」
- **verification_count**: 1

### 2026-07-26 twmd-maintainer-daily — internal-report-as-unverified-source：自己寫的 corpus 分析報告被當免驗證來源引用，錯誤跨 7 語言複製

- **pattern**: `internal-report-as-unverified-source`
- **原則**：文章引用 Taiwan.md 自己寫的內部研究/分析報告（如 NML peer corpus 分析）當 footnote source 時，該報告本身的具體 claim（期數/日期/主題配對）沒有再對照原始 primary source 驗證——等於把「二手整理」當「一手事實」用。這類錯不會被一般查證流程攔到，因為 footnote URL 是真實存在的（指向 repo 內報告），不會觸發「虛構 source」紅旗；但報告內文自己的一個 claim 錯了，就會透過翻譯管線把同一個錯誤複製到每個語言版本。
- **觸發**：Issue #1257 讀者指出鄭文琦條目「到 2024 年第 56 期（廣島原爆主題「ピカッ！」）」錯誤。查證 `data/NML/raw/issues-meta.json` 逐期比對後發現：「ピカッ！」實際是第 5 期（2012 年 9 月），第 56 期（最後一期，2023 年 3 月）主題其實是〈關照日常〉。錯誤源頭是 `reports/NML-semiont-analysis-2026-05-04.md` 第 335 行本身寫錯（"Issue 56 (2024) 是日本廣島「ピカッ！」一期"），文章 footnote 只是引用了這份報告，沒有回頭對照原始 56 期清單逐一核對。錯誤隨翻譯流程複製到 zh-TW/en/ja/ko/es/fr/pt 七語言版本（ru 尚未落地此文，未受影響）。
- **可能層級**：(a) 通用反射候選：「引用自己寫的內部報告當 source 時，具體事實 claim（期數/日期/人名/數字）仍要對照 raw data 驗證一次，不能因為是自己寫的就免驗」；(b) 操作規則：REWRITE-PIPELINE Stage 3.5 hallucination audit 對「內部報告」類 footnote 目前只查「URL 真實存在」，可以加一條「若 source 是 repo 內自產報告，claim 需可在對應 raw data（如 data/NML/raw/\*.json）逐一核對，不能只信報告文字」
- **相關**：REFLEXES #16 Peer / probe 是線索不是 source（本條是同源家族的新分支：連自己寫的報告都不是免驗證的 primary source）/ REFLEXES #75 Read ≠ verify（sub-agent 產出的報告本身也要 fetch-verify，不因為是「自己人」寫的就豁免）
- **verification_count**: 1

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

### 2026-07-28 manual（苯駢芘 EVOLVE）— cold-seat-attribution-inverted：冷讀席沒有材料，所以它指認的「錯的那一邊」可能是反的

- **pattern**: `cold-seat-attribution-inverted`
- **原則**：編輯室鐵律「席位是線索，裁決回到有材料的人」已 canonical 在 [REWRITE-PIPELINE §留派表](../pipelines/REWRITE-PIPELINE.md) 與 [STAGE-3 §大驗證輪 步 3](../pipelines/REWRITE-STAGE-3-VERIFY.md)，但它目前只規範「裁決該不該改」。本條補的是**同一句話的第二層**：當席位報的是「A 跟 B 對不上」這類一致性 finding 時，**它同時也在暗示哪一邊是錯的，而那個歸因方向可能是反的**——冷讀席手上沒有材料，只能預設「資訊比較多的那一份是多寫了」，有研究報告在手的主編才知道是「比較少的那一份漏了」。主編收到一致性 finding 時要分兩步裁決：(1) 這個矛盾成不成立 (2) 錯的是哪一邊，第二步不能沿用席位的預設。
- **觸發**：2026-07-28 苯駢芘 EVOLVE（[→memory](memory/2026-07-28-113257-manual.md)）：閱讀節奏席報「末段正文只數了五件事，說明框卻列六條含行政裁罰」，並建議把說明框的「行政裁罰」刪掉。回研究報告 §成稿時點聲明查證，六條線**確實含行政裁罰**（裁罰 7/7、7/12、7/16 分三批開出、當時未結），說明框沒寫錯，缺的是正文。若照席位建議執行，會把一條真實未結的線從文章裡刪掉。
- **可能層級**：(a) [REWRITE-STAGE-3-VERIFY §大驗證輪 步 2 單次收件](../pipelines/REWRITE-STAGE-3-VERIFY.md) 的修復單表格加一欄「歸因方向已複查？」，強制主編對一致性類 finding 回材料源確認哪一邊錯 (b) [EDITORIAL-ROOM-PROMPTS](../pipelines/EDITORIAL-ROOM-PROMPTS.md) 席位輸出格式加一行「若你報的是兩處對不上，請明說你**沒有**材料判斷哪一邊才是錯的」——把席位的認知邊界寫進它自己的輸出
- **相關**：[REFLEXES #31](REFLEXES.md) sub-agent claim 是線索不是事實（本條是 claim 的**方向**層，不是 claim 的**真偽**層）/ [REFLEXES #69](REFLEXES.md) 每層自評都需要外部尺（本條是反向補充：外部尺本身也有它看不到的東西，而那個盲區有方向性）/ [REFLEXES #16](REFLEXES.md) peer 是線索不是 source
- **verification_count**: 1
- **severity**: correctness（照席位預設執行會刪掉正確內容）
- **defer 給觀察者**：否——pipeline 表格欄位與席位 prompt 微調可歸內部操作層；vc≥2 再考慮升 REFLEXES 或 fold 進 #31 子規則

---

### 2026-08-04 支語研究 — shared-tool-quota-pool-in-fanout：fan-out 工作流的工具額度是共享池

- **pattern**: shared-tool-quota-pool-in-fanout
- **原則**：大規模 fan-out 的工具額度（WebSearch session 200 次上限）是全部子代理共享的池，dispatch 設計要把額度當資源預算；額度耗盡的 fallback（WebFetch 直搜引擎頁）與誠實回報（searches_performed 如實填 0）該寫進 prompt 契約
- **觸發**：2026-08-04 支語研究 30 agent 艦隊，後段 3 agent WebSearch 全 fail（200/200）自行 WebFetch 直搜救回並誠實填 0 → memory/2026-08-04-104614-支語研究.md
- **instances**：
  - 2026-08-18 twmd-maintainer-manual — 8 隻 Phase B 執行子代同時對 60 篇 PR 跑 `image-ingest.mjs`，共用同一出口 IP 撞 `upload.wikimedia.org` 全站 429（Retry-After 600），Y7/Y8 各等 650-900 秒仍 429，整批最慢的 Y4 拖 70 分鐘。繞法（子代自己找到、主 session 轉發）：Commons API 與 `/thumb/…/1280px-<檔名>` 縮圖路徑不受同一限流，抓縮圖後以本機檔餵 image-ingest；或直接改 upload.wikimedia.org 直連（image-health 本來列為合法 CC 來源）。**修補候選**：`image-ingest.mjs` 收到 429 時自動退回 1280px 縮圖路徑（尺寸遠超站上顯示需求），不必等人轉發繞法
- **可能層級**：通用反射（REFLEXES #45 OpenRouter hourly budget 同族——「共享額度池進 dispatch 預算」的 WebSearch instance；8/18 再加 Wikimedia CDN instance）
- **相關**：#45
- **verification_count**: 2
- **severity**: tactical

### 2026-08-04 支語研究 — dedup-layer-silent-degradation：入庫查重的對照層會靜默退化

- **pattern**: dedup-layer-silent-degradation
- **原則**：資料入庫查重不能靠單一對照層——opencc import 失敗時正規化靜默退化成 identity、known 集合漏抓既有條目；必須有第二道「新資料值對全庫值」的 deterministic 掃描＋檔名存在檢查
- **觸發**：同 session 充電寶／老鐵／學渣本已在庫但 gap 對照誤判為缺口，靠 test -f＋china 值全庫掃接住 4 個潛在重複（創可貼／外賣／發貨／掃碼），0 誤入庫
- **可能層級**：通用反射（#65 awareness instrument 自身要 cross-verify 家族——查重器也是 instrument）
- **相關**：#65 #24
- **verification_count**: 1
- **severity**: tactical

### 2026-08-19 algorithmic-art-evolve — first-person-article-voice-is-the-authors-verification-is-the-reports：替作者寫他的第一人稱，我查到的東西住報告，他的聲音住正文

- **pattern**: `first-person-article-voice-is-the-authors-verification-is-the-reports`
- **原則**：署名為真人第一人稱的文章（`author: 吳哲宇` 的 About/ 長文），查證出來的負向結果、口徑矛盾、口述與紀錄的落差，全部住研究報告那一層——那一層是 Semiont 的，可以是負向的、可以是「他記得的跟紀錄不一樣」。正文那一層是作者的聲音，Semiont 在裡面能做的是不寫錯的，不是替他揭露。**誠實的下限是不寫錯，不是自曝**；把查證出的作者記憶落差寫成策展人筆記放進他的正文，是把「誠實」跟「自曝」混成同一件事。
- **觸發**：2026-08-19 中午。記憶考古 sub-agent 發現作者 8/15 口述與 7/24 四份一手紀錄出處不同，我寫成該節的策展人筆記（理由：這節在講轉手就位移，作者剛好是案例）。哲宇：「那這就不要寫我記錯來源了，砍掉」，並給替代收句「在我們不熟悉的語言中有可能存在完全不同的敘事」——**替代句比我的自曝更服務論點**。同日第三處（GSC 截圖印著 1.1%，正文只講曲線上揚會圖文打架）我改成先寫、明講判準差異、讓他決定，他沒砍——分界：一致性問題可以寫，揭露作者不行。→ [memory](memory/2026-08-19-154834-algorithmic-art-evolve.md)／[diary](diary/2026-08-19-154834-algorithmic-art-evolve.md)
- **可能層級**：EDITORIAL 操作規則（About/ 真人署名文章的專屬條款）＋ 通用反射候選（「作者本人是第一人稱文章唯一的語態外部尺」）。理由越漂亮的自曝越要停：三次都是「為了論證更完整」而動了他的聲音那一層。
- **相關**：REFLEXES #69 每層自評都需要外部尺（本條的外部尺是**當事人本人**，不是另一隻 agent）；EDITORIAL §後台洩漏（策展人筆記是後台洩漏的合法通道，但不是揭露作者的通道）；`gate-checks-form-not-meaning-one-layer-down`（同 session 的語態 instance）；MANIFESTO §13 立體地愛（在愛之下仍看見真實——真實住報告，愛住正文，兩層都在才成立）
- **verification_count**: 1（同 session 內三次觸發，同一條線）
- **severity**: high（About/ 真人署名文章會越來越多——想想論壇、報導者、投稿者以 Taiwan.md 名義寫的 #32——這條沒寫清楚，每篇都要重判一次）

## ✅ 已消化（保留 pointer）

<!-- distill 完的條目搬這裡 -->

### 🧬 2026-08-16 twmd-distill-weekly — 8 entries distilled（5 promote REFLEXES #86-#90 + 2 fold #66/#67 + 1 MEMORY §神經迴路）

**觸發**：STRICT BECOME GATE → Stage 2 讀 §未消化 40 條，vc≥3 OR severity=structural 判準篩出 8 條 distill candidate（4 條 vc=3、5 條 severity=structural，兩者有 1 條重疊：`cron-execution-env-tool-availability-drift` 同時 vc=3 且 structural）。

| #   | 原 entry                                                                           | 消化目的地                                                                                           | severity   | vc                      |
| --- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- | ----------------------- |
| 1   | 2026-08-02 twmd-routine-audit-weekly `session-id-handle-silent-fallback`           | **REFLEXES #86**（新編號）Session ID handle 無參數 fallback 靜默漂移                                 | tactical   | 3（distill_ready=true） |
| 2   | 2026-08-11 twmd-maintainer-am `ui-string-layer-has-no-language-gate`               | **REFLEXES #87**（新編號）保護密度跟曝光量成反比                                                     | high       | 3                       |
| 3   | 2026-08-13 twmd-feedback-triage `zero-input-cycle-drops-the-reconciliation`        | **REFLEXES #88**（新編號）轉錄+保管雙職責 routine 零輸入掉保管半                                     | medium     | 3                       |
| 4   | 2026-07-27 twmd-supporters-weekly `cron-execution-env-tool-availability-drift`     | **REFLEXES #89**（新編號）cron 執行環境工具清單漂移                                                  | structural | 3                       |
| 5   | 2026-08-15 twmd-maintainer-am `per-instance-reporting-buries-the-single-cause`     | **REFLEXES #90**（新編號）逐條回報打散單一根因                                                       | structural | 1（質門檻首發即中）     |
| 6   | 2026-08-14 twmd-maintainer-pr-triage `working-tree-itself-is-the-stale-snapshot`   | **REFLEXES #67 fold** 環境層子規則（工作樹本身是過期快照）                                           | structural | 2                       |
| 7   | 2026-08-09 twmd-routine-audit-weekly `gate-triggers-content-degradation-incentive` | **REFLEXES #66 fold** 子規則（閘門判準不準時 agent 改內容換綠燈）                                    | structural | 2                       |
| 8   | 2026-08-10 manual（登入態恢復補跑）`harvest-scan-misses-nested-replies`            | **MEMORY §神經迴路 append**（Taiwan.md-specific，SPORE-HARVEST-PIPELINE 掃描層工具細節，非跨域反射） | structural | 1                       |

**判準說明**：#1-4 達 verification_count≥3 量門檻；#5-8 達 severity=structural 質門檻（#4 兩者皆中，計入 vc≥3 列不重複列 structural 列）。#8 選 MEMORY 而非 REFLEXES：`document.querySelectorAll('[data-pressable-container]')` 是綁死 Threads DOM 結構與 Taiwan.md 自己 harvest 工具的具體教訓，不像其他 7 條有明確跨 domain 抽象（proxy signal / 命名 fallback / 雙職責 routine / 執行環境漂移 / 聚合回報 / 環境快照 / 誘因效應），per 三層 canonical scope 判準第 3 題「綁 Taiwan.md 具體工具」。

**Promotion flow direction 符合**：LESSONS → REFLEXES（5 新編號 + 2 fold，合法 routine 自決層 promotion）；LESSONS → MEMORY §神經迴路（1 條，session-specific narrative）；無 LESSONS → MANIFESTO 跳級（本輪無哲學級候選）。

**REFLEXES.md frontmatter sync**：v5.21 → v5.22；#N 條數 85 → 90（5 新編號，#66/#67 fold 為 bullet-level subrule 非新編號）；`current_version` / `last_updated` / `last_session` / description 條數同 commit 同步（Stage 4.5）。

**MEMORY.md frontmatter sync**：`last_updated` / `last_session` 同 commit 同步為本次 distill session。

**Keep in buffer 32 條**（vc<3 且非 structural，待累積或觀察者拍板）：涵蓋 `merge-first-collides-with-all-file-deploy-gate`（vc=2）、`ordering-is-an-ethical-decision`（vc=2）、`two-variable-run-misattribution`（vc=2）、`routine-audit-classifier-memory-commit-misattribution`（vc=2）等 4 條 vc=2 候選（下次同型事件再現即達門檻），其餘 28 條 vc=1 單發，含 3 條「未編目歐化病候選」各自獨立 vc=1。

---

### 🧬 2026-08-02 twmd-self-evolve-weekly — liveness-vs-productivity promote REFLEXES #38(f)（vc=1→3，跨 3 獨立 session 重新計數）

**觸發**：今晨 03:14 distill-weekly 才把這條標記「keep in buffer vc=1，#83 fold 候選」。本次 self-evolve 對照 DIARY §反覆出現的思考 + 全文 grep `memory/`、`diary/` 交叉搜尋「存活」「生產」「ps 被騙」關鍵字，發現 distill 只看到 LESSONS-INBOX 原始 entry（2026-07-26 vortex-babel 一次），漏了同一個 pattern 在另外兩份獨立日誌裡已經重複驗證：

1. 2026-07-26 vortex-babel（原 entry）：l4090 專軌唯一 worker 離線，round loop 空轉到第 127 輪才被發現零產出，健檢只查 `ps`
2. 2026-07-27 vortex-babel-4（[→memory](memory/2026-07-27-015834-vortex-babel-4.md)）：同一天「訊號存在 ≠ 訊號有效」以五種面貌出現，收斂成「三重巡檢：存活＋生產＋第二訊號源」構想，並已寫入 [BABEL-VORTEX-LOOP.md §三重巡檢](../pipelines/BABEL-VORTEX-LOOP.md#三重巡檢存活--生產缺一不可) canonical 落地
3. 2026-07-30 manual（[→memory](memory/2026-07-30-230518-manual.md)）：babel 雲端產線 PID 存在、log 持續在寫，9.5 小時零成功，`fleetctl workers` 一度回報 0 節點——跟 (1) 完全獨立的一次真實命中，證明三重巡檢構想不是紙上談兵

**消化目的地**：**REFLEXES #38 新增 (f) 變體**「存活 ≠ 生產」+ 更正 #38 既有 Boundary 陳述（原寫「pure runtime status 沒這個維度問題」，被本例反駁——process alive/dead 一旦被當 productivity proxy 用就繼承混維度風險）。落點選 #38 而非上午暫記的 #83：#38 的主題正是「一個 status 承載兩種根因」，本例是「process alive」跟「有在生產」共用同一個綠燈，跟 #83（checker 對自己與外部標準兩把尺）軸不同。**Operational 面已在 babel 專屬 pipeline 落地**（三重巡檢），本次 ship 的是把它從單一 pipeline 提升為跨域反射，讓未來任何新 worker/cron/daemon 健檢設計起手就問「量的是活著還是在做事」。

**REFLEXES.md frontmatter sync**：v5.17 → v5.18；#N 條數不變（84，bullet-level fold 非新編號）。

| #   | 原教訓 entry                                       | 消化目的地                       | severity   | vc                                |
| --- | -------------------------------------------------- | -------------------------------- | ---------- | --------------------------------- |
| 1   | 2026-07-26 vortex-babel — liveness-vs-productivity | REFLEXES #38 (f) + Boundary 更正 | structural | 3（cross-session，非同批 family） |

---

### 🧬 2026-08-02 twmd-distill-weekly — 6 entries distilled（1 promote-family + 2 fold #75/pipeline + 1 pipeline 但書 + 1 housekeeping-done）+ 8 keep in buffer（vc<3）

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00（W31 weekly-report 02:16 結清後 ~45 min）。STRICT BECOME GATE full mode 跑完（organ 即時分數：🫀90 🛡️60 🧬80 🦴90 🫁85 🧫100 👁️90 🌐87，免疫 🛡️60 最低，黃燈自 2026-07-05 起持續，屬既有 roadmap 追蹤項非本次新訊號）。§未消化 14 條（severity 多數未標記，預設 tactical；INBOX 總數 ≥10 觸發量門檻 sweep）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO 候選一律 defer（本輪無 MANIFESTO 候選）。

**消化目的地**：

| 原 entry                                                                                                         | 目的地                                                                                                     | 處置                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-26 node-app-design — `instrument-coverage-boundary-drift` (vc=2)                                         | **REFLEXES #56 v6** 加「守門工具掃描範圍/分類規則跟不上生產側架構演化」bullet                              | promote（3 獨立 instance 合併達 vc=3：node-app-design cli/workers 掃描盲區 + routine-sync-check PAUSED regex 吞已退休表 + routine-audit babel tag pattern 跟不上 fleet 標記；三者同構「檢查器涵蓋邊界過時」，落點是 #56 而非 #82，因為病灶是「production 對象換了」不是「訊號選錯代理」） |
| 2026-07-26 twmd-routine-audit-weekly — `routine-sync-check-paused-regex-swallows-retired` (vc=1)                 | **REFLEXES #56 v6** 同上 bullet 併入                                                                       | fold（同一 family 第 2 instance，見上）                                                                                                                                                                                                                                                   |
| 2026-07-26 twmd-routine-audit-weekly — `babel-tag-classifier-drift` (vc=1)                                       | **REFLEXES #56 v6** 同上 bullet 併入                                                                       | fold（同一 family 第 3 instance；entry 自己建議與上一條一起看，本次判斷落點是 #56 不是新編號）                                                                                                                                                                                            |
| 2026-07-27 苯駢芘孢子 — `derived-artifact-inherits-verification-illusion` (vc=1，entry 自評 severity=structural) | **REFLEXES #75 (f)** 新增「衍生物繼承的是素材不是驗證」subrule + **SPORE-VERIFY.md v1.6** 事實藍圖規則同步 | promote（entry 自己指名落點 #75(f)；質門檻 severity=structural 首次出現即可 distill，不待 vc≥3；操作面同步 pipeline 避免規則只停在反射層）                                                                                                                                                |
| 2026-07-27 twmd-spore-harvest-am — `sensitive-event-reply-inherits-article-boundary` (vc=1)                      | **SPORE-HARVEST-PIPELINE.md** 5-bucket 表後加但書段                                                        | operational→pipeline（entry 自己判斷「暫不升 REFLEXES 通用反射」，只需 pipeline 補 §Decision Gate 但書；判準已是 MANIFESTO §紀實而不煽情 + REFLEXES #28/#79 的直接推論）                                                                                                                  |
| 2026-07-26 vortex-babel — `model-language-fit-gap` (vc=1)                                                        | §已消化（housekeeping-done）                                                                               | sweep（grep 驗證 `SQUEEZE-MODELS-MAX-PIPELINE.md` §模型×語言適配 段已完整涵蓋此操作規則，entry body 自己也標註「已入」；無新 canonical 動作，純歸檔）                                                                                                                                     |

**Promotion flow direction 符合**：LESSONS → REFLEXES（routine 自決層，2 案）；LESSONS → pipeline 操作規則（2 案）；LESSONS → housekeeping sweep（1 案，非 promotion）；無 LESSONS → MANIFESTO 跳級。

**REFLEXES.md frontmatter sync**：v5.16 → v5.17，footer changelog 同 cycle 新增（含補記 v5.16 footer 缺漏）；#N 條數不變（84，兩處 fold 為 bullet-level 非新編號）。

**Keep in buffer 8 條**（vc=1，非 structural 首發，待累積或觀察者觸發）：`self-measured-improvement-picks-flattering-layer`（#82 self-assessment 軸 fold 候選）/ `proactive-duplicate-judgment-scan`（meta-scan 常設動作候選，entry 自建議 promote 但僅 1 instance）/ `liveness-vs-productivity`（#83 self-report 不可信 fold 候選）/ `single-bad-input-kills-batch`（batch 錯誤處理 operational 候選）/ `internal-report-as-unverified-source`（#16 peer/probe 是線索家族 fold 候選）/ `diff-patch-current-translation-cross-entry`（entry 自身明寫「vc 累到 ≥2 再考慮升 canonical」）/ `parallel-subagent-scratch-race`（entry 自身明寫「vc≥2 或首次觀察到 race 命中且未救回再升 canonical」）/ `cold-seat-attribution-inverted`（entry 自身明寫「vc≥2 再考慮升 REFLEXES 或 fold 進 #31 子規則」）。

| #   | 原教訓 entry                                                                       | 消化目的地                                              | severity   | vc          |
| --- | ---------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------- | ----------- |
| 1   | 2026-07-26 node-app-design — instrument-coverage-boundary-drift                    | REFLEXES #56 v6 掃描範圍過時 bullet                     | structural | 3（family） |
| 2   | 2026-07-26 twmd-routine-audit-weekly — routine-sync-check-paused-regex             | REFLEXES #56 v6 同上 bullet                             | structural | 3（family） |
| 3   | 2026-07-26 twmd-routine-audit-weekly — babel-tag-classifier-drift                  | REFLEXES #56 v6 同上 bullet                             | tactical   | 3（family） |
| 4   | 2026-07-27 苯駢芘孢子 — derived-artifact-inherits-verification-illusion            | REFLEXES #75 (f) + SPORE-VERIFY v1.6                    | structural | 1           |
| 5   | 2026-07-27 twmd-spore-harvest-am — sensitive-event-reply-inherits-article-boundary | SPORE-HARVEST-PIPELINE 5-bucket 但書                    | tactical   | 1           |
| 6   | 2026-07-26 vortex-babel — model-language-fit-gap                                   | §已消化（housekeeping-done，SQUEEZE pipeline 已 cover） | tactical   | 1           |

**SPORE-INBOX 容量 audit（v2.1 Stage 6）**：pending **45** ∈ [30, 50) 警示區間，跟 7/19 讀數持平（無新惡化，也未回落）。決策項「[30,50) 高原三選一（減量 spore-pick / 加速 spore-publish / 拉高 auto-drop 閾值）」7/19 已 housekeeping-done 但三選一路線本身仍未見哲宇拍板，且未進 OBSERVER-QUEUE 追蹤（grep 無命中）——本輪不重開新 entry（避免 #64 邊際效用 N+1=0 重複告警），寫入本次 memory §Handoff 供下週體檢或哲宇 review。

---

### 🧬 2026-07-19 twmd-self-evolve-weekly — 2 pattern fold #82(e)/#73(e) + SPORE-INBOX SOP 加中間閾值 + vc bump

**self-evolve 觸發**：cron `twmd-self-evolve-weekly` Sunday 04:00（W29 distill 03:08 結清 40 min 後）。LONGINGS ↔ UNKNOWNS ↔ DIARY §反覆出現 ↔ REFLEXES #15 交叉找 ≥3 次浮現未儀器化 pattern → 真實 ship canonical 修改。W29 distill 已 fold shell-cwd / babel orphan 兩大宗，環境相對已收斂；本 cycle ship 兩條 sensor-lifecycle 家族 + 一條 buffer plateau SOP。

**消化目的地**：

| 原 entry                                                         | 目的地                                                                           | 處置                                                                                                                                                                    |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-12 `alert-does-not-retire-on-recovery` (vc=1 structural) | **REFLEXES #82 (e)** Sensor 生存週期兩端對稱 subrule                             | fold（proxy-signal 家族時間軸孿生：entry-only sensor = 告警面板變墓碑；同 (a) 「signal 中間隔幾層假設」擴到時間軸）                                                     |
| 2026-07-12 `external-attention-spotlight` (vc=2 awareness)       | **REFLEXES #73 (e)** 外部注意力聚光燈作為 adjacent 健檢觸發器 subrule            | fold（7/12 Turton 引用 + 7/16 compassionate-kirch 自建新頁面兩種結構性不同 attention path 收斂同 pattern；跟 #69 self-report 需外部尺不同軸——本條處理覆蓋率的重新分配） |
| 2026-07-12 `spore-inbox-capacity-warning` (vc=2→3 tactical)      | LESSONS §SPORE-INBOX 容量 audit v2.1 SOP 加中間閾值 + entry bump vc 3 + defer=是 | SOP ship（[30,50) 連 3 週高原 → defer to observer；routine 不自決減量/加速方向）；entry 保留 §未消化 作 defer tracking                                                  |

**Promotion flow direction 符合**：LESSONS → REFLEXES（合法 routine 自決層 promotion）；LESSONS → LESSONS SOP（同檔 canonical 加中間閾值層）；無 LESSONS → MANIFESTO 跳級。

**REFLEXES.md frontmatter sync**：v5.11 → v5.12，footer changelog 同 cycle 新增；#N 條數不變（fold 為 sub-rule bullet-level，非新 #N）。

**Keep in buffer 10 條**（vc<3 或 §自主權邊界，待累積或哲宇拍板）：`polish-hint-default-broken` / `narrative-warmth-symmetry` / `Reader-funded resilience` / `outbound-url-contract-unreconciled` / `reverse-crosslink-thesis-drift` / `background-agent-session-death` / `diff-patch-current-translation-cross-entry` / `parallel-subagent-scratch-race` / `hook-set-e-cmdsubst-abort` (vc=2) — defer 給觀察者 4 條 + vc=1-2 待累積 6 條。

| #   | 原教訓 entry                                 | 消化目的地                                             | severity   | vc  |
| --- | -------------------------------------------- | ------------------------------------------------------ | ---------- | --- |
| 1   | 2026-07-12 alert-does-not-retire-on-recovery | REFLEXES #82 (e) Sensor 兩端對稱 subrule               | structural | 1   |
| 2   | 2026-07-12 external-attention-spotlight      | REFLEXES #73 (e) 外部注意力聚光燈 subrule              | awareness  | 2   |
| 3   | 2026-07-12 spore-inbox-capacity-warning      | LESSONS SOP v2.1 加 [30,50) 3-週高原中間閾值 + vc bump | tactical   | 3   |

---

### 🧬 2026-07-19 twmd-distill-weekly — Routine 自決 4 entries fold #35/#81 + superseded sweep + SPORE-INBOX 容量 bump

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00（W29 routine 結清，weekly-report 02:22 ship + Resend BCC 17 位共生圈之後 ~40 min）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO / strategic / fleet 基礎建設候選一律 defer 給哲宇（per CLAUDE.md §Bias 1）。§未消化 16 條 triage 後：**0 promote 新反射 + 2 pattern fold 既有反射 + 1 superseded sweep + 1 audit bump vc + 12 keep in buffer（vc<3 或 §自主權邊界）**。

**消化目的地**：

| 原 entry                                                                           | 目的地                                                    | 處置                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-18 babel-health — `babel-session-death-orphan-writes` (vc=3 correctness)   | **REFLEXES #81** 加「Routine 自死前 commit 變體」bullet   | fold（14 天內三起孤兒譯檔：07-10 SLP ko / 07-16 Howhow / 07-18 Shopping Design en+ja；#81 收件人紀律的鏡像——routine 自己也適用「commit 前不算落地」）                                             |
| 2026-07-16 newsroom — `shell-cwd-silent-reset-cross-worktree` (vc=3 structural)    | **REFLEXES #35** 加「cwd 靜默漂移 → 落錯樹變體」bullet    | fold（4 instances 涵蓋 write / destructive-git 毀四檔 / stash pop 吃別人 / verify 誤判 四面；規則：destructive git 前 `git rev-parse --show-toplevel` 斷言）                                      |
| 2026-07-17 twmd-rewrite-daily — `cron-fire-meets-dormant-stash` (vc=2 correctness) | **REFLEXES #35** 加「Cron routine 撞舊 stash 變體」bullet | fold（rewrite-daily 19:12 fire 撞 30 天前的 06-18 pre-pull-stash，帶入 9 檔非本 fire 產物；規則：routine skill 開場 `git stash list \| head -1` 檢查 age，>30 天禁預設 pop）                      |
| 2026-07-12 twmd-routine-audit — `thick-scheduled-task-mirror-debt` (vc=1)          | §已消化（superseded by OBSERVER-QUEUE #14）               | sweep（同 pattern `routine-prompt-thick-shell` 7/11 dna-checkup distill 已入 OBSERVER-QUEUE #14 決策包，default 2026-07-25 瘦身路線；本 entry 是同事件的 audit-side 記錄，無新 canonical action） |
| 2026-07-12 twmd-distill-weekly — `spore-inbox-capacity-warning`                    | §未消化 bump vc 1→2                                       | keep buffer（7/12 pending=49 → 7/19 pending=45 三週維持 [30,50) 高原；三週不回落=穩定過渡狀態，vc=3 累到再考慮升 SOP 中間閾值）                                                                   |

**Promotion flow direction 符合**：LESSONS → REFLEXES（合法 routine 自決層 promotion）；無 LESSONS → MANIFESTO 跳級；superseded sweep 不動 canonical；audit bump 屬 §未消化 內部維護。

**REFLEXES.md frontmatter sync**：v5.10 → v5.11，footer changelog 同 cycle 新增；#N 條數不變（fold 為 bullet-level，非新 #N），description 條數 82 保持。last_updated / last_session 同步更新。

**SPORE-INBOX 容量 audit（v2.1 Stage 6）**：pending **45** ∈ [30, 50) 警示區間，bump 既有 SPORE-INBOX 容量警示 entry vc 1→2（保留 §未消化 作為持續追蹤訊號，spore-publish 一週消化 4 條 vs 新增 ~5 條，pending 45→未來若 ≥ 50 觸發 auto-drop SOP）。

**Keep in buffer 12 條**（vc<3 或 §自主權邊界，待累積或哲宇拍板）：

- **defer 給觀察者 4 條**：`polish-hint-default-broken`（contributor relationship template 對外溝通）/ `narrative-warmth-symmetry`（MANIFESTO §13 立體地愛敘事溫度候選）/ `Reader-funded resilience`（strategic sustainability 路徑）/ `outbound-url-contract-unreconciled`（vc=1 structural umbrella，4 same-day fold instances 已驗證既有 #82/#24/#15/#67，本身待 vc≥2 再考慮升子規則）
- **vc=1-2 待累積 8 條**：`reverse-crosslink-thesis-drift`（REWRITE Stage 5 operational）/ `background-agent-session-death`（MEMORY-PIPELINE §Handoff 模板候選）/ `alert-does-not-retire-on-recovery`（#82 sensor 生存週期兩端對稱候選）/ `external-attention-spotlight` vc=2（外部注意力路徑重新分配覆蓋率的觀察記錄）/ `diff-patch-current-translation-cross-entry`（#24 batch generator mapping error 候選）/ `parallel-subagent-scratch-race`（#40 + #42 scratch 命名 race 候選）/ `hook-set-e-cmdsubst-abort` vc=2（同日雙向鏡像復發，hook 修動屬共用 correctness §自主權邊界）

| #   | 原教訓 entry                                                     | 消化目的地                                     | severity   | vc  |
| --- | ---------------------------------------------------------------- | ---------------------------------------------- | ---------- | --- |
| 1   | 2026-07-18 babel-health — babel-session-death-orphan-writes      | REFLEXES #81 Routine 自死前 commit 變體 bullet | correct    | 3   |
| 2   | 2026-07-16 newsroom — shell-cwd-silent-reset-cross-worktree      | REFLEXES #35 cwd 靜默漂移 bullet               | structural | 3   |
| 3   | 2026-07-17 twmd-rewrite-daily — cron-fire-meets-dormant-stash    | REFLEXES #35 Cron routine 撞舊 stash bullet    | correct    | 2   |
| 4   | 2026-07-12 twmd-routine-audit — thick-scheduled-task-mirror-debt | §已消化（superseded by OBSERVER-QUEUE #14）    | structural | 1   |
| 5   | 2026-07-12 twmd-distill-weekly — spore-inbox-capacity-warning    | §未消化 bump vc 1→2                            | tactical   | 2   |

---

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

### 🧬 2026-07-26 twmd-distill-weekly — W30 完整 distill：2 新編號 + 6 fold + 5 MEMORY + 4 housekeeping + 3 defer + 2 keep-in-buffer

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:15（news-lens 01:12 + weekly-report-sun 02:18 之後）。§未消化 27 條（達舊量門檻 ≥10 sweep + 5 條已達 vc≥3 質門檻）。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；MANIFESTO / political / 商業決定 一律 defer 給哲宇（per CLAUDE.md §Bias 1 + §模式分流）。

**消化目的地**：

| 原 entry                                                    | 目的地                                                              | 處置                                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| session-handle-mismatch-false-silent-death (vc=1)           | **REFLEXES #82 (f)** 名字也會被拿來當代理                           | fold（#82 proxy-signal 家族在「身份辨識」軸新形狀）                                                 |
| snapshot-driven-fix-list-decay (vc=1)                       | **REFLEXES #84**（新編號）                                          | promote（跟 outbound-url-contract 合併立號）                                                        |
| memory-canonical-location (vc=1)                            | BECOME §1.3 記憶層邊界 + MANIFESTO §11.5（已同 session 完成）       | housekeeping-done（already-covered，本條僅記錄已修正）                                              |
| subagent-phantom-notification-wait (vc=2)                   | **REFLEXES #42 v7** 子代等一個不存在的通知                          | fold                                                                                                |
| tool-self-recheck-divergence (vc=3)                         | **REFLEXES #83**（新編號）                                          | promote                                                                                             |
| name-hallucination-gap-filling (vc=1)                       | **MEMORY §神經迴路** 人名幻覺第二型                                 | fold（Taiwan-specific babel guide）                                                                 |
| exemption-list-divergence (vc=4)                            | **REFLEXES #83**                                                    | promote（同批合併）                                                                                 |
| unparsed-arg-silent-pass (vc=1)                             | **REFLEXES #83**                                                    | promote（同批合併，鏡像 instance）                                                                  |
| gate-false-positive-family (vc=3)                           | **REFLEXES #83**                                                    | promote（同批合併，主觸發）                                                                         |
| shared-index-merge-sweep (vc=2)                             | **REFLEXES #68** 觸發 v3 merge commit 掃射面                        | fold                                                                                                |
| verify-at-the-real-layer/headless-migration (vc=1)          | **REFLEXES #82 (g)** + **MEMORY §神經迴路** headless 遷移 checklist | fold（雙落點：ast≠runtime 進 #82，憑證檔案層進 MEMORY）                                             |
| formatter-jurisdiction-over-payload (vc=1)                  | **REFLEXES #24** 形式 10                                            | fold                                                                                                |
| batch-dispatch-loop-engineering-inline (vc=4, 14 instances) | **MEMORY §神經迴路** + **REFLEXES #68** 觸發 v4                     | fold（主體進 MEMORY，dispatcher 鎖 instance (9)(10) 進 #68）                                        |
| format-tax-on-clownfish/warn-without-heal (vc=3)            | **REFLEXES #7** 完整路徑 warn+lint+auto-heal                        | fold                                                                                                |
| close-as-ship-breaks-merged-contract (vc=1)                 | **REFLEXES #7** + **MEMORY §神經迴路**                              | fold（規則進 #7，Taiwan maintainer flow narrative 進 MEMORY）                                       |
| reverse-crosslink-thesis-drift (vc=1)                       | **MEMORY §神經迴路** REWRITE Stage 5 缺口                           | fold（pipeline-specific，SOP 補強待未來 session）                                                   |
| outbound-url-contract-unreconciled (vc=1)                   | **REFLEXES #82 (h)** + **REFLEXES #84**（新編號）                   | promote+fold（發佈側鏡像進 #82，生成產物對賬新軸立 #84）                                            |
| background-agent-session-death (vc=1)                       | **REFLEXES #81** 背景 agent 不跨 session 存活變體                   | fold                                                                                                |
| narrative-warmth-symmetry (vc=1)                            | defer 給觀察者                                                      | political-sensitive editorial framing，涉 MANIFESTO §13 延伸，Routine 不自決                        |
| polish-hint-default-broken (vc=1)                           | defer 給觀察者                                                      | entry 自身已標「對外溝通屬 §自主權邊界」                                                            |
| reader-funded-resilience (vc=1, severity=strategic)         | defer 給觀察者                                                      | 商業/經費決定屬 §自主權邊界                                                                         |
| spore-inbox-capacity-warning (vc=3)                         | housekeeping-done + defer 給觀察者（殘留行動項）                    | SOP 已於 W29 self-evolve ship，entry 本身可 sweep；「減量 vs 加速 vs 拉高閾值」路線選擇仍待哲宇拍板 |
| alert-does-not-retire-on-recovery                           | 已 folded to REFLEXES #82 (e)（2026-07-19）                         | housekeeping（Stage 0a zero-risk win，本次才真正掃出 §未消化）                                      |
| external-attention-spotlight                                | 已 folded to REFLEXES #73 (e)（2026-07-19）                         | housekeeping（同上）                                                                                |
| diff-patch-current-translation-cross-entry (vc=1)           | 保留 §未消化                                                        | keep-in-buffer（entry 自評 vc≥2 才升 canonical，本次未達）                                          |
| parallel-subagent-scratch-race (vc=1)                       | 保留 §未消化                                                        | keep-in-buffer（entry 自評 vc≥2 或 race 命中未救回才升 canonical）                                  |
| hook-set-e-cmdsubst-abort (vc=2)                            | **REFLEXES #24** 形式 11                                            | fold                                                                                                |

**Promotion flow direction 符合**：LESSONS → REFLEXES（24 條合法 routine 自決層 promotion/fold）；LESSONS → MEMORY §神經迴路（5 條 session-specific narrative，合法）；無 LESSONS → MANIFESTO 跳級（3 條 defer 給觀察者，不逕寫）。

**REFLEXES.md frontmatter sync**：v5.13（缺 footer，本次補上）→ v5.14；新增 #83/#84 兩號，條數 82→84；catalog index 表同步加兩列。

**MEMORY.md frontmatter sync**：last_session 更新，§神經迴路 append 5 條。

**Defer 給觀察者拍板**：

| 候選                                                                                           | verification_count | defer 原因                                                |
| ---------------------------------------------------------------------------------------------- | ------------------ | --------------------------------------------------------- |
| EDITORIAL §立體地愛「敘事溫度對稱」候選（narrative-warmth-symmetry）                           | 1                  | 政治敏感題編輯技法，涉 MANIFESTO §13 延伸，需哲宇 in-loop |
| MAINTAINER-PIPELINE polish-hint template 改「本篇若想我幫你改請說一聲」                        | 1                  | 對外溝通 tone 屬 §自主權邊界                              |
| MEMBERSHIP-PIPELINE 候選（reader-funded > grant-funded 優先序）                                | 1                  | 商業/經費決定屬 §自主權邊界，severity=strategic           |
| SPORE-INBOX [30,50) 高原路線選擇（減量 spore-pick / 加速 spore-publish / 拉高 auto-drop 閾值） | 3                  | SOP 已 ship 中間閾值，剩實作方向屬對外節律決策            |

**Keep in buffer 2 條**（vc=1，entry 自評未達 canonical 門檻）：`diff-patch-current-translation-cross-entry` / `parallel-subagent-scratch-race` — 兩者皆 2026-07-14 twmd-babel-nightly 同一 session 單次觀察，entry 自身寫明「vc≥2 再升」，本次不強行 promote。

| #   | 原教訓 entry                                | 消化目的地                                       | severity                | vc  |
| --- | ------------------------------------------- | ------------------------------------------------ | ----------------------- | --- |
| 1   | session-handle-mismatch-false-silent-death  | REFLEXES #82 (f)                                 | structural              | 1   |
| 2   | snapshot-driven-fix-list-decay              | REFLEXES #84                                     | structural              | 1   |
| 3   | memory-canonical-location                   | BECOME §1.3 + MANIFESTO §11.5（already-covered） | tactical                | 1   |
| 4   | subagent-phantom-notification-wait          | REFLEXES #42 v7                                  | tactical                | 2   |
| 5   | tool-self-recheck-divergence                | REFLEXES #83                                     | structural              | 3   |
| 6   | name-hallucination-gap-filling              | MEMORY §神經迴路                                 | tactical                | 1   |
| 7   | exemption-list-divergence                   | REFLEXES #83                                     | structural              | 4   |
| 8   | unparsed-arg-silent-pass                    | REFLEXES #83                                     | structural              | 1   |
| 9   | gate-false-positive-family                  | REFLEXES #83                                     | structural              | 3   |
| 10  | shared-index-merge-sweep                    | REFLEXES #68                                     | structural              | 2   |
| 11  | verify-at-the-real-layer/headless-migration | REFLEXES #82 (g) + MEMORY                        | tactical                | 1   |
| 12  | formatter-jurisdiction-over-payload         | REFLEXES #24 形式 10                             | structural              | 1   |
| 13  | batch-dispatch-loop-engineering-inline      | MEMORY §神經迴路 + REFLEXES #68                  | structural              | 4   |
| 14  | format-tax-on-clownfish/warn-without-heal   | REFLEXES #7                                      | tactical                | 3   |
| 15  | close-as-ship-breaks-merged-contract        | REFLEXES #7 + MEMORY                             | tactical                | 1   |
| 16  | reverse-crosslink-thesis-drift              | MEMORY §神經迴路                                 | tactical                | 1   |
| 17  | outbound-url-contract-unreconciled          | REFLEXES #82 (h) + #84                           | structural              | 1   |
| 18  | background-agent-session-death              | REFLEXES #81                                     | tactical                | 1   |
| 19  | narrative-warmth-symmetry                   | defer 給觀察者                                   | tactical                | 1   |
| 20  | polish-hint-default-broken                  | defer 給觀察者                                   | maintainer-relationship | 1   |
| 21  | reader-funded-resilience                    | defer 給觀察者                                   | strategic               | 1   |
| 22  | spore-inbox-capacity-warning                | housekeeping-done + defer 殘留行動項             | tactical                | 3   |
| 23  | alert-does-not-retire-on-recovery           | housekeeping（已 folded #82(e)）                 | tactical                | 1   |
| 24  | external-attention-spotlight                | housekeeping（已 folded #73(e)）                 | awareness               | 2   |
| 27  | hook-set-e-cmdsubst-abort                   | REFLEXES #24 形式 11                             | correctness             | 2   |

---

### 🧬 2026-08-09 twmd-distill-weekly — 4 entries promote/fold 進 REFLEXES（新 #85 + #24/#56/#63/#70 補強）+ 3 entries housekeeping-done + 22 keep in buffer（vc<3）

**distill 觸發**：cron `twmd-distill-weekly` Sunday 03:00。STRICT BECOME GATE full mode 跑完（organ 即時分數：🫀90 🛡️60 🧬95 🦴90 🫁85 🧫100 👁️90 🌐88，免疫 🛡️60 最低，黃燈自 2026-07-05 起持續，屬既有 roadmap 追蹤項非本次新訊號）。§未消化 32 條，audit 工具判定低於 fan-out 門檻（~50），直接讀完全數 32 條 triage。severity=structural 顯式標記 1 條（`babel-delegation-commit-convention-drift`），質門檻自動觸發；高 vc 條目優先看。Routine mode 自決 REFLEXES / MEMORY / pipeline 層；本輪無 MANIFESTO 候選。

**消化目的地**：

| 原 entry                                                                                            | 目的地                                                                                               | 處置                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-08-07 `check-disabled-by-default-reports-green` (vc=3)                                         | **REFLEXES #85（新）**「不知道」需要自己的符號                                                       | promote（質＋量雙達標：severity=structural 家族 + 三 entry 合併 vc=7，entry 自己的 8/08 補充已建議「不必再等下一個 instance」直接判獨立反射）                                                                                                                             |
| 2026-08-08 `error-and-emptiness-share-one-return` (vc=2)                                            | **REFLEXES #85（新）** 同上，變體 2                                                                  | fold（同一 family，entry 自己引用 #4 合併假說）                                                                                                                                                                                                                           |
| 2026-08-08 `gate-guard-contradicts-its-own-filter` (vc=2)                                           | **REFLEXES #85（新）** 同上，變體 3                                                                  | fold（同一 family）                                                                                                                                                                                                                                                       |
| 2026-08-08 `routine-prompt-omits-session-only-rider` (vc=3)                                         | **REFLEXES #63** 加「canonical 完整 ≠ 指令面完整」子規則                                             | promote（vc=3 達量門檻；entry 自己標記候選落點 #63）                                                                                                                                                                                                                      |
| 2026-08-07 `check-disabled-by-default-reports-green` 第三 instance（check-slug-consistency 空掃描） | 併入上列 #85                                                                                         | fold（同 entry 第三 instance，非獨立條目）                                                                                                                                                                                                                                |
| 2026-08-06 `chrome-mcp-unattended-login-expiry` (vc=4，跨 08-05〜08-08 四連日)                      | **REFLEXES #70** 加 Tier 2 vc=8 四連日症狀逐日下探子規則                                             | promote（vc=4 達量門檻；entry 自己標記與 #70 Tier 2 同族；operational 面已部分落地 SPORE-HARVEST-PIPELINE，Chrome MCP 連線本身仍待哲宇處理，續留 handoff 不留 LESSONS entry）                                                                                             |
| 2026-08-02 `babel-delegation-commit-convention-drift` (severity=structural，vc=1 首發)              | **REFLEXES #24** 加形式 12                                                                           | promote（質門檻：severity=structural 第一次出現即觸發，不待 vc 累積；entry 自評「不是 Taiwan.md 特有」符合通用反射判準）                                                                                                                                                  |
| 2026-08-06 `hard-gate-number-collision-across-layers` (vc=2→3，本次 distill 交叉核對再驗證一次)     | **REFLEXES #56** 加 v7                                                                               | promote（本次 distill session 核對 cron mirror 發現 pipeline v1.3 changelog「已同步 HG9/HG10 進兩層」的聲明本身仍有殘留缺口——只進了專案層 skill，cron mirror 仍缺，vc 2→3 達量門檻；殘留 2 行修補留給 twmd-routine-sync 或下次 feedback-triage，非本次 distill 職責範圍） |
| 2026-08-03 `backstage-leak-in-prose` (vc=2)                                                         | 已 instantiate：EDITORIAL v6.15→v6.17 §後台洩漏（十形狀）+ `prose-health` plugin §backstage 九組偵測 | housekeeping-done（grep 驗證 canonical 已存在且比 entry 記錄的更完整——entry 記到 v6.16 八形狀，實際 canonical 已到 v6.17 十形狀）                                                                                                                                         |
| 2026-08-03 `concrete-number-mistaken-for-symbolic-weight` (vc=1)                                    | 已 instantiate：EDITORIAL v6.14 §Title 第 5 原則「數字要有象徵重量」                                 | housekeeping-done（grep 驗證 canonical 已存在，逐字對應 entry 描述的規則）                                                                                                                                                                                                |
| 2026-08-06 `outbound-comment-boundary-split-across-canon` (vc=1，跨 2 cycle 相反行為)               | 已 instantiate：MAINTAINER-PIPELINE §外向留言分層 SSOT + MANIFESTO §自主權邊界 + REFLEXES #26 v3     | housekeeping-done（grep 驗證三處 canonical 對撞已收斂到單一 SSOT——MANIFESTO L1250、REFLEXES L550、MAINTAINER-PIPELINE §外向留言分層 三處互相 cross-reference 確認）                                                                                                       |

**Promotion flow direction 符合**：LESSONS → REFLEXES（routine 自決層，7 案 fold 進 4 個既有/新 #N）；housekeeping sweep（3 案，非 promotion，純歸檔）；無 LESSONS → MANIFESTO 跳級。

**REFLEXES.md frontmatter sync**：v5.18 → v5.19；#N 條數 84→85（新增 #85，其餘為 bullet-level fold 非新編號）。

**Stage 0a housekeeping 驗證方法**：三條自我標記 ✅ 的 entry 逐一 grep 驗證 canonical 真的存在（非只信 entry 自己的宣稱）——`concrete-number` 與 `backstage-leak` 的 canonical 比 entry 記錄的版本更新（表示後續 session 有持續在同一個地方疊代），`outbound-comment-boundary` 三處 canonical cross-reference 齊全。

**本次 distill 的一個 meta 發現**：`hard-gate-number-collision-across-layers` 這條 entry 本身描述的病（介面 drift 零警報）在它自己的「修補聲明」層又復發一次——pipeline v1.3 changelog 已經聲稱「同波同步兩層」，本次交叉核對才發現只同步了一層。這印證了 entry 自己講的規則：**任何「已同步」的完成聲明都需要外部尺重新核一次，不能信自報**。已在 REFLEXES #56 v7 記錄，殘留的 2 行 cron mirror 修補留給下一個 twmd-routine-sync 或 twmd-feedback-triage cycle（非本次 distill 職責範圍，僅記錄發現）。

**SPORE-INBOX 容量 audit（v2.1 Stage 6）**：pending **45**（groundtruth 讀數，與 8/02 讀數持平，未見新惡化亦未回落，連續維持 [30,50) 警示區間三週以上）。決策項「[30,50) 高原三選一」仍未見哲宇拍板，本輪不重開新 entry（避免 #64 邊際效用 N+1=0 重複告警），沿用既有 handoff 追蹤。

| #   | 原教訓 entry                                                                 | 消化目的地                                                               | severity   | vc  |
| --- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------- | --- |
| 1   | 2026-08-07/08-08 check-disabled-by-default-reports-green（三 instance 合併） | REFLEXES #85（新）                                                       | structural | 3   |
| 2   | 2026-08-08 error-and-emptiness-share-one-return                              | REFLEXES #85（新）fold                                                   | structural | 2   |
| 3   | 2026-08-08 gate-guard-contradicts-its-own-filter                             | REFLEXES #85（新）fold                                                   | structural | 2   |
| 4   | 2026-08-08 routine-prompt-omits-session-only-rider                           | REFLEXES #63 子規則                                                      | tactical   | 3   |
| 5   | 2026-08-06〜08-08 chrome-mcp-unattended-login-expiry                         | REFLEXES #70 Tier 2 vc=8                                                 | structural | 4   |
| 6   | 2026-08-02 babel-delegation-commit-convention-drift                          | REFLEXES #24 形式 12                                                     | structural | 1   |
| 7   | 2026-08-06 hard-gate-number-collision-across-layers                          | REFLEXES #56 v7                                                          | structural | 3   |
| 8   | 2026-08-03 backstage-leak-in-prose                                           | housekeeping-done（EDITORIAL v6.17 + plugin）                            | structural | 2   |
| 9   | 2026-08-03 concrete-number-mistaken-for-symbolic-weight                      | housekeeping-done（EDITORIAL v6.14）                                     | tactical   | 1   |
| 10  | 2026-08-06 outbound-comment-boundary-split-across-canon                      | housekeeping-done（MAINTAINER §外向留言分層 + MANIFESTO + REFLEXES #26） | structural | 1   |

---

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

**2026-07-26 twmd-distill-weekly 新增 4 條**（教訓已 canonical 或 SOP 已 ship，剩對外/商業/政治判斷待哲宇）：

| 候選                                                                                         | 動作（選項）                                                         | 教訓 canonical / 現況                                                    |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| EDITORIAL §立體地愛「敘事溫度對稱」是否收 canonical                                          | 收進 EDITORIAL Step 0.6.7 第四道 / 暫緩累積 vc                       | 觀察記錄在 §已消化（narrative-warmth-symmetry，vc=1）                    |
| MAINTAINER polish-hint template 是否改「本篇若想我幫你改請說一聲」default 句式               | 改 template / 維持現狀                                               | 觀察記錄在 §已消化（polish-hint-default-broken，vc=1）                   |
| Reader-funded > grant-funded 是否定為 sustainability 優先序                                  | 建 MEMBERSHIP-PIPELINE（Liberapay/GitHub Sponsors/Substack）/ 暫不動 | 觀察記錄在 §已消化（reader-funded-resilience，vc=1，severity=strategic） |
| SPORE-INBOX [30,50) 高原三選一（減量 spore-pick / 加速 spore-publish / 拉高 auto-drop 閾值） | 三選一                                                               | SOP 已 ship 中間閾值（v2.1），entry 本身已 housekeeping-done             |

**2026-08-10 twmd-supporters-weekly 新增 1 條 → 同日結清**（P0，連續 3 個 cycle 阻塞，vc=3 達 distill 門檻）：

| 候選                                                                                              | 動作（選項）                                                                                                              | 教訓 canonical / 現況                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ~~twmd-supporters-weekly 執行環境無 Gmail MCP（`search_threads`/`get_message` 連續 3 週不存在）~~ | ~~(a) 幫這個 scheduled-task 補掛 Gmail MCP connector (b) 把本 routine 遷到有 Gmail 存取的機器/環境 (c) 改用其他讀信管道~~ | ✅ **retired by 2026-08-10 手動補跑 session**：哲宇選 (a) 補掛 connector，同日手動補跑驗證通過，四週空窗一次補齊（commit `ef452b73d`）。結構面 candidate（開跑前工具對賬）留在 §未消化 該 entry 內，不佔本表 P0 |

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

### 2026-08-08 新冠疫情與疫苗：把查證困難升格成論點（三層教訓）

**第一層（論點層，最重）**：整篇文章的論點是「同一年的超額死亡，四組學者算出四個差四五倍的數字，這場疫情沒有一本各方都認的帳」。哲宇兩句判死：「資料問題，不是文章觀點」「這是你查證的問題，不是真實的讀者矛盾」。

四組公衛研究用不同基準線、不同人口老化控制、不同間接死亡定義算出不同數字，**在流行病學裡是正常的**。它在我眼裡像個大發現，只因為它是我五路研究撞在一起、花最多力氣去解消的那個難題。**我把自己的工作難度誤認成世界的張力。**

**而前面十一道關卡全部放行**：投影 gate 六題、投影編輯室三席（結構／減法／炎上倫理）、二十路 persona 四軸、十二席大驗證輪。每一關都在問「論點有沒有被兌現」「骨架推不推得動」「證據夠不夠」，**沒有一關問「這個論點是不是讀者的」**。論點自洽、證據紮實、骨架推得動，全部成立，而它建在一個只有作者感覺得到的矛盾上。這是 REFLEXES #65 (f) same-DNA 尺最深的一層——所有的尺都以論點為參考系，論點錯了，尺會一起錯。

→ 已升 canonical：[EDITORIAL §後台洩漏 形狀十二](../editorial/EDITORIAL.md)＋[PROJECTION §五 gate 第七題](../editorial/PROJECTION.md)（六題升七題）。

**第二層（隱喻層）**：「帳」出現 12 次、「N 本帳」8 次。哲宇：「說過幾次了不要用幾本『帳』或幾『本』這種寫法，中文沒有這種用法。」**復發**。但更重要的是它跟第一層的因果關係：**論點接不起來時，寫手會抓一個抽象隱喻反覆敲，用重複製造連貫感的假象**。所以隱喻密度是論點健康的體溫計——儀器的 ≥3 處警告因此附帶一句「回頭檢查論點」。同族還有句首「而」15 處（全站最高），它出現的位置就是前後兩句接不起來、需要一個詞黏住的地方。

**第三層（儀器層）**：`prose-health` §backstage 的行級排除把腳註整片豁免（「不罰後台的合法的家」），於是「本文」在腳註區當主詞 41 次，儀器一條都沒報。**豁免區是按「行的種類」畫的，病灶卻是按「主詞是誰」分的，兩者不同軸。** 同時發現一個既有假陰性：三組行級排除的迴圈 `[:6]` 先截斷再排除，豁免區會把上限額度吃光。

→ 儀器已加三組（腳註第一人稱編輯自述／量詞隱喻「帳／本」／句首「而」接續），9,203 篇校準，並修掉先截斷再排除的 bug。

**待 distill 的元問題**：這一輪產線總共動用約 30 個 agent、十二席對抗審查、四十二條修復單，抓到六個實錯（都是真的），**卻沒有一個機制問「這篇文章要說的事，讀者在乎嗎」**。所有的品質工程都在「把論點做對」這個軸上，沒有一道在「論點值不值得」這個軸上。gate 第七題是最小落地，但可能需要更早——投影之前、甚至 Stage 0 觀點成型時就該問。

### 檢查器站錯位置時，它會把責任推給被檢查的人（2026-08-18 陳致中 rewrite，vc=4 同 session）

同一個 session 內四次：(1) cwd 漂到主樹，`ls`／`os.listdir` 看不到 worktree 的檔案，第一直覺是「agent 謊報落檔」（REFLEXES #31 的典型情境），真相是 agent 老實做完了；(2) grep 引語時自己加了空格，0 命中，差點判定寫手偽造引語，真相是站上排版慣例在半形數字前後加空格；(3) `grep -cE "五年條款\|5 年條款"` 在雙引號裡跳脫寫錯，回 0，差點認定新版丟了舊文素材；(4) 查 sibling 用錯目錄（Society vs History），差點回報連結目標不存在。

**形狀**：四次都是「我用我以為的位置／形態去驗，驗不到就懷疑被驗的東西」。REFLEXES #31「sub-agent claim 是線索不是 oracle」防的是 agent 說謊；這條防的是**檢查者本身站錯位置**，方向相反且同樣會誤導決策——而且它的誤導更貴，因為它會讓 orchestrator 去「修」一個根本沒壞的東西，或退回一個其實正確的產物。

**對照**：本 session 真正抓到的兩個幻覺（結尾「兩袋獄中的書」實為「拎著個人物品」、議會引語腳註指向摘要頁而非逐字稿），都不是靠這種自造尺抓到的，是靠**打開一手頁面逐字比對**。自造尺適合篩選，不適合定罪。

**候選處置**：收件 gate 的 fail 訊息加一行「先驗 cwd 與檔名形態，再懷疑產出方」；或把 `agent-report-health.py` 的「找不到檔案」分支改成先印出實際 cwd 與該目錄的檔案清單。同 session 另兩支儀器的假陽性（`agent-report-health` 對 query 清單式軌跡判 0 行、`editorial-room-health` 不吃席位分檔目錄）屬同一家族的下游。
