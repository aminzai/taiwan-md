---
title: 'LESSONS-INBOX'
description: '教訓 buffer（intake layer）— 新教訓先 append 此處，週期性 distill 到 MANIFESTO/DNA/MEMORY canonical'
type: 'cognitive-buffer'
status: 'buffer'
apoptosis: 'never'
current_version: 'v2.5'
last_updated: 2026-08-03
last_session: '2026-08-03-140210-manual（黃崇仁 REWRITE，+3 未消化：中立管語氣不管份量、數字具體但無象徵重量、後台洩漏；後二者已 instantiate 為 EDITORIAL v6.14 Title 第 5 原則 + v6.15 §後台洩漏＋prose-health §backstage 儀器）'
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

### 2026-08-03 manual（黃崇仁 REWRITE）— backstage-leak-in-prose：作者的工作痕跡跑進正文，每句單獨看都過關

- **pattern**: `backstage-leak-in-prose`
- **原則**：pipeline 給寫手的每一份規格（投影藍圖的「全局功能」、研究報告的護欄、查證表的分歧欄）都是**用來指導寫作的語言**。寫手在 context 裡讀了一整輪，下筆時很自然把那套語言帶進正文——而且它覺得自己很盡責（「我有交代清楚」「我有誠實標註分歧」）。**盡責的地方是後台，不是正文。** 這個病特別難自檢，因為每一句單獨看都有內容、不空洞、不歐化，**過得了既有的所有關卡**；它壞在說話對象錯了——這些句子是說給編輯／查核者／作者自己聽的，不是說給讀者聽的。一句判準：這句話在跟誰說話？
- **觸發**：2026-08-03 黃崇仁 Stage 2 寫手成品，自評 `article-health --profile=rewrite-stage-4` hard=0 warn=0 全綠，哲宇讀完逐條 callout 四處：(1)「兩件事的動詞不一樣，判斷是同一套」——「這也聽起來很AI，誰會在看這個時候想到動詞XDDDD」(2)「要說清楚回來的是什麼樣的公司。」——「是段落寫作動機，不該是段落的一部分」(3)「這一段誠實的空白值得留著。」——「語感怪」(4)「這句話有兩個版本在流傳，另一家媒體的版本沒有…」——「所以你要採用完整的內容，不是在裡面分析媒體」。四處分屬四種形狀：分析框架洩漏／寫作動機洩漏／自我評價洩漏／查證過程洩漏。
- **可能層級**：通用反射候選（不限本篇——任何走 pipeline 的寫作都會被規格語言 prime），但目前 1 instance（雖然同一篇內四種形狀齊發）。已 instantiate 為 EDITORIAL 規則 + 儀器，先觀察其他文章是否復發
- **相關**：harness memory `feedback_red_line_anxiety_leak`（別把「逐字」「原封不動」這類來源焦慮標籤漏進正文）是本條第三、四類的一個特例——本條把它從「來源焦慮」擴大到整個後台家族（分析鷹架／寫作指令／自我表揚／查證過程）。另與 REFLEXES #69「每層自評都需要外部尺」同族：寫手 warn=0 的自評不是說謊，是**它的尺量不到這一維**——後台洩漏對寫手而言是「盡責的證據」不是「該刪的東西」，同一顆腦不會把自己的盡責當缺陷。
- **六種形狀**（哲宇分三輪 callout 補齊）：分析框架洩漏（用「動詞」描述人生）／寫作動機洩漏（藍圖指令照抄）／自我評價洩漏（稱讚自己誠實）／查證過程洩漏（攤開媒體版本分歧）／**指揮讀者注意力**（「這裡有一個細節值得停下來看」）／**論述鷹架洩漏**（「這兩件事完全不同：前者可以等，後者必須動手」）
- **round 2（2026-08-03 深夜〜08-04，vc 1→2）**：D+0 上線版哲宇再貼 13+ 段殘留，聚類出兩個新形狀升 EDITORIAL v6.16 八形狀——**查無聲明**（查證的「查無」用研究者語言進正文，5 例最大宗，兩例腳註早有同句話）與**懸念預告鷹架**（匿名名詞＋延遲揭曉）。三個元教訓：(1) **尺只量得到已見過的形狀**——第一輪六形狀與五組偵測器全來自第一輪 callout，查無聲明沒被踩到就沒長那維 (2) **一處 callout 應觸發全文同族重掃**（第一輪逐 callout 修六處、第二輪被抓 13 處多數當時就在文裡）——已立 REWRITE-STAGE-3 修復單鐵律 (3) **頭銜考證三輪收斂揭「合法的家有容量與層級」**：第一輪修語氣、第二輪壓縮筆記仍被打回、第三輪哲宇裁決「連比較都不需要寫」——查證內容層級表（正文零痕跡／腳註一句／筆記只收得上洞察的勘誤）進 EDITORIAL。附帶發現：修病時的**病種替換**（修英式段首滑進「是⋯的」cleft，哲宇當場抓）＋兩個跨篇簽名檔（「真正的轉折發生在」9 篇→擴無前綴型 32 篇、「不在X，在Y」9 篇）。完整診斷 [reports/backstage-leak-round2-2026-08-03.md](../../reports/backstage-leak-round2-2026-08-03.md)。儀器 5→7 組＋cleft＋段首雙帶，全 WARN 意識層
- **已 instantiate（規則 + 儀器雙軌）**：
  - [EDITORIAL v6.15](../editorial/EDITORIAL.md) §六 新增 §後台洩漏（廚房的聲音跑到餐廳）：六種形狀 × 六個真實反例 × 改法對照表 + 「這句話在跟誰說話」判準
  - `prose-health` plugin §backstage 五組偵測（WARN-only soft-launch）。**878 篇 zh corpus 三輪校準**：初版 43 hits → 收緊 8 hits；加第五六類後 83 hits（9.45%）→ 再收緊 **29 hits（3.30%），零誤報**
- **校準過程本身的三個發現（比規則更有價值）**：
  1. **「值得停下來看／想」是跨 22 篇的招牌慣性**（「很值得停下來想的話」／「最值得停下來想一秒的地方」／「這一段值得停下來想一秒」），「誠實的空白」跨 3 篇。這種口頭禪**每篇單獨看都只是一句過場，要把全站攤開才看得見它已經變成簽名檔**——人眼結構上抓不到，只有儀器能。REFLEXES #15 最強的一次驗證
  2. **兩種形狀 regex 結構上做不到，誠實不做**：指涉語法回指（「前者可以等，後者必須動手」，38 hits 絕大多數是正當對比——「前者是壓制，後者是收編」指涉文中已存在的真實事物，病的那種指涉作者剛造出來的抽象對比，**句法完全一樣**）與對稱宣告（「這兩件事完全不同」）。硬收會複製 PUA／媒體焦慮偵測器 92-100% 假陽性被移除的錯誤。寫進 EDITORIAL 當人眼判準並在 plugin 註解記錄為什麼不做
  3. **誤報的共同結構**：三輪被砍掉的 pattern（「值得一提的是」25／「有兩個版本」9／裸「值得停下來」17／「前者後者」38）全部是「**病的形狀跟正當用法共用同一個字串**」。真正可儀器化的是那些**只有在後台語境才會出現的字串**（「誠實的空白」「另一家媒體的版本」「先說清楚 X 是什麼」）
- **verification_count**: 2（round 2 於 D+0 復發即驗證）

### 2026-08-03 manual（黃崇仁 REWRITE）— concrete-number-mistaken-for-symbolic-weight：數字通過了「不抽象」那關，卻沒通過「有意義」那關

- **pattern**: `concrete-number-mistaken-for-symbolic-weight`
- **原則**：EDITORIAL §抽象聰明句不是標題 的自檢是「每個關鍵詞能不能指出具體的東西」，數字天然通過這關——可查證、可指認、絕不抽象。於是寫手（跟 AI）容易把「堆三個數字」誤當成「夠具體了」。但**具體 ≠ 有象徵重量**：讀者心裡對「四十三家銀行」「一千兩百億」沒有一把尺，不知道算多算少、代表什麼；而「說好三年，放了四十年」同樣是數字，卻自帶對照物（承諾 vs 現實），落差本身就是意義。判準是遮住主題名後，副標剩下的東西還能不能讓人猜到這是誰的人生——規格表遮掉人名後可以套用在任何一間欠債重整的公司。
- **觸發**：2026-08-03 黃崇仁 REWRITE，寫手產出標題「黃崇仁：一千兩百億債務、四十三家銀行，和一條沒有停下來的產線」，哲宇 callout「有數字，但是象徵意義不足，只看標題一點真實意義都沒有，也沒辦法代表他的人生」。三個數字全部可查證、全部具體、全部通過既有的 reverse-abstraction test，但串起來讀是規格表不是人生。
- **可能層級**：操作規則（已 instantiate 為 EDITORIAL v6.14 Title 第 5 原則），但底下的認知 pattern 可能更廣——「通過了某一關的檢查，就以為通過了它真正要防的東西」這個形狀，跟 REFLEXES #82 proxy signal antipattern 同族（具體度是象徵重量的 proxy，不是象徵重量本身）
- **相關**：REFLEXES #82（proxy signal antipattern：訊號要摸到 ground truth，不是量它的替身）——本條是 #82 在編輯判斷層的具體形狀，「可查證的具體性」是「讀者感受得到的意義」的替身。若 distill 判定可 fold，最可能落點是 #82 新增子規則。也跟 EDITORIAL §四 reverse-abstraction test 相關——本條補的是：那個 test 只擋得住抽象詞，擋不住具體但無意義的數字。
- **已 instantiate**：[EDITORIAL v6.14](../editorial/EDITORIAL.md) §Title 四原則 → 五原則，新增第 5 條「數字要有象徵重量，不是規格表」含正反例與「數字旁邊有沒有對照物」判準
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

### 2026-08-02 twmd-routine-audit-weekly — babel-delegation-commit-convention-drift：委派層產生的 commit 脫離格式，讓自己的一部分工作對儀器隱形

- **pattern**: `babel-delegation-commit-convention-drift`
- **原則**：babel 渦流／Claude 委派層產生的 commit，有部分不遵循 [MANIFESTO §Commit 標記規則](MANIFESTO.md) canonical 格式（`🧬 [semiont] <type>: <描述>` / `🧬 [routine] <type>: <描述>`）——本週窗口內 10 條用「🧬 babel: ...」（缺 `[semiont]` 方括號），32 條直接用英文 conventional-commits 風格（`fix(babel): ...` / `chore(babel): ...` / `feat(i18n): ...` / `docs: ...`），完全跳出中文「🧬」簽名慣例。這些 commit 內容本身多半可讀（具體英文短句描述修復），但因為不含 `[semiont]` 或 `[routine]` 方括號，任何 keyed off 這個格式的儀器都看不到它們——本次 routine-audit.py 的 unclassified 桶（64 條 / 7.9%）裡有 42 條（65.6%）是這個成因，而非真正的「分類器沒見過的新 routine」。
- **觸發**：2026-08-02 twmd-routine-audit-weekly Stage 1 跑 `routine-audit.py --last-week`，unclassified=64。細查後 22 條是 git merge 自動訊息（正常，非漂移）、10 條是「🧬 babel:」缺方括號、32 條是純 conventional-commits 風格。樣本：`fix(babel): heal italic caption URL mangling`、`chore(babel): refresh translation indexes after integration`、`feat(i18n): rescue Arabic and Portuguese egg tart`（皆 2026-07-30，babel 渦流連續自我修復日）。
- **可能層級**：(a) 通用反射候選——任何長跑自動化子系統，若讓委派層 / sub-agent 自訂 commit message 格式而非強制套用 repo canonical template，遲早會漂出 grep-based 儀器的可視範圍，不是 Taiwan.md 特有；(b) 操作規則——babel vortex dispatcher 的 commit 產生邏輯（含委派給 Claude sub-agent / codex 的路徑）應統一套用 `🧬 [semiont] babel: <desc>` 模板，不論是哪一層產生的
- **相關**：REFLEXES #24 工具在說謊（新形狀：commit 來源格式漂移讓下游偵測工具靜默失明，不是工具本身說謊，是輸入源不再說儀器聽得懂的話）；MANIFESTO §11.4 電報腔紀律（本條方向相反——這批 commit 反而比較「人話」，但犧牲了格式一致性，兩種毛病不同軸，不能用其中一條的修法解另一條）
- **verification_count**: 1
- **severity**: structural（第一次出現，但影響是「儀器看不見自己一部分工作」的結構性缺口，不只是本次審計數字失真——未來任何依賴 `[semiont]`/`[routine]` 格式的自動化都會踩到同一個盲區）

### 2026-08-02 twmd-routine-audit-weekly — routine-audit-classifier-memory-commit-misattribution：新 routine 的 action commit 跟 memory commit 落進不同桶，count 半失真

- **pattern**: `routine-audit-classifier-memory-commit-misattribution`
- **原則**：`routine-audit.py` 的 `ROUTINE_PATTERNS`（scripts/tools/routine-audit.py:37-58）裡，具名 pattern 是否含 `.*` wildcard 並不一致——像 `twmd-maintainer-am` 用了 `.*`，能同時吃下自己的 action commit 跟 `[routine] memory: twmd-maintainer-daily @ ...` 這種 memory commit；但 `twmd-data-refresh-am` 這類無 wildcard 的具名 pattern，memory commit 吃不到，會被排在後面的通用 `routine-memory` pattern（`\[routine\] memory:`）攔截，混進所有 routine 共用的 `routine-memory` 桶。對完全沒有具名 pattern 的新 routine（`twmd-routine-sync` / `twmd-flywheel-watch`），2026-07-11 加的動態 fallback 能抓到它們的 action commit（但因通用 `routine-memory` pattern 排在 fallback 之前被優先攔截，只有 memory commit 撿不到 fallback；action commit 則被 fallback 加上重複 `routine-` 前綴，變成 `routine-twmd-routine-sync` 這種雙重字首），結果同一條 routine 的 action 與 memory 兩種 commit 被拆進三個不同地方，`summary.by_routine` 顯示的 count 只反映不完整的子集（本次 `twmd-routine-sync` 顯示 2、`routine-twmd-flywheel-watch` 顯示 6，實際 git log 各有 ~8-9 條）。
- **觸發**：2026-08-02 twmd-routine-audit-weekly Stage 1 跑 `routine-audit.py --last-week`，`summary.by_routine` 出現 `routine-twmd-routine-sync: 2` 與 `routine-twmd-flywheel-watch: 6` 兩個帶重複字首的 key，跟其他直接用 `twmd-X` 命名的 key 不一致；`git log --grep routine-sync` 核對後發現實際週活動量約 8-9 條，遠高於腳本統計。第三個更根本的 instance：`twmd-weekly-report-sun` 的 action commit 本身就不用 `[routine]` 前綴（用 `🧬 [semiont] report: weekly ...`），對應的 `[routine] memory: twmd-weekly-report-sun @ ...` 也因無 wildcard 落進 `routine-memory` 通用桶——這條 routine 每週的 commit 在 `by_routine` 表裡從未以自己的名字出現過，比前兩條更隱蔽（連字首重複的視覺線索都沒有，直接是零筆）。
- **可能層級（更新）**：不只是「新 routine 忘了補 pattern」的個案，是三種獨立成因疊加同一個症狀：(1) 具名 pattern 有無 `.*` wildcard 不一致（工程遺留）(2) 部分 routine 的 action commit 本身不帶 `[routine]` 前綴，改用 `[semiont] <type>:`（如 weekly-report 用 `report:`）(3) 通用 `routine-memory` pattern 排序優先於「用 routine 名做 fallback 分類」。三者疊加代表這不是單一 regex 漏洞，是分類器設計時沒有把「memory commit 永遠跟著它描述的 routine」當成不變式來源頭建模。
- **可能層級**：tool-fix，跟 2026-06-28 已解決並歸檔的 `routine-audit-script-classification-gap`（vc=2 disposed）同源家族——那次的 fallback 修法解掉了「unclassified 非零」，但沒解掉「同一條 routine 的兩種 commit 落不同桶」這個殘留子案例。修法方向：(a) 為每個新 routine 補齊具名 pattern（含 memory 變體）而非只靠 fallback；(b) 或把 `routine-memory` 通用 pattern 移到 fallback 之後，讓 fallback 先嘗試用 `memory:` 後面的 routine 名歸類，抓不到才落 `routine-memory`
- **相關**：`routine-audit-script-classification-gap`（2026-06-28，已 tool-fix disposed，本條是其未被當時 dogfood 覆蓋到的殘留子案例，非重複——原案處置時的驗證窗口沒有包含當時還不存在的 `twmd-routine-sync` / `twmd-flywheel-watch` 兩條 routine）
- **verification_count**: 1
- **severity**: tactical（只影響本審計工具自己的統計精度，不影響 routine 實際運作或下游決策——本次 audit 已用 git log 交叉核對繞過）

### 2026-08-02 twmd-routine-audit-weekly — session-id-handle-silent-fallback：跑了 12 週都對的 routine handle，這週悄悄變成 `manual`

- **pattern**: `session-id-handle-silent-fallback`
- **原則**：`twmd-self-evolve-weekly` 從 2026-05-10 起連續 12 週都正確產出 `memory/YYYY-MM-DD-HHMMSS-twmd-self-evolve-weekly.md` 檔名，2026-08-02 這次卻產出 `memory/2026-08-02-041706-manual.md`——commit message 本身正確寫著「🧬 [semiont] memory: twmd-self-evolve-weekly @ 2026-08-02 04:17」，但檔名 handle 落成通用的 `manual`，代表 `scripts/tools/session-id.sh` 這次是被無參數呼叫（auto-detect 落 default）而非顯式傳入 `twmd-self-evolve-weekly`。這個落差只在檔名層，commit message 是對的，MEMORY.md 索引行的敘述文字也是對的，唯獨實體檔名跟兩者不一致——**沒有任何現成儀器會比對「commit message 講的 routine 名」跟「它建立的 memory 檔名 handle」是否一致**，本次是 audit 為了核對本週各 routine 的實際活動量、直接用檔名 pattern 找檔案時才意外發現（`find *twmd-self-evolve-weekly*` 少一筆，git log 找到多一筆，兩個尺不一致才浮現）。
- **觸發**：2026-08-02 twmd-routine-audit-weekly Stage 1 核對本週各 routine 的 memory 檔案數時，`twmd-self-evolve-weekly` 用檔名 glob 找到 0 筆（正常應 1 筆），但 `git log --grep` 找到 1 筆對應 commit（`72251fdb7`）。追蹤到實體檔案是 `2026-08-02-041706-manual.md`，內文 session header 明寫「session twmd-self-evolve-weekly（cron routine，Sunday 04:00）」，是同一個 session 只是檔名沒跟上。
- **可能層級**：通用反射候選——任何靠「呼叫時傳入 handle 參數」決定產物命名的自動化，若呼叫路徑存在無參數的 fallback（auto-detect），遲早會有一次呼叫漏了參數，產物命名跟內容本身的敘述（commit message／內文 header）不一致，而且因為內容本身讀起來完全正確，人工複閱不會發現——只有靠「檔名 vs 內容」交叉比對的第三方稽核才抓得到，跟 REFLEXES #65 (f) 存活≠生產是同一個「訊號要摸到 ground truth，不能只信自己一種讀法」的家族，這次的「訊號」換成檔案命名系統本身
- **相關**：REFLEXES #82 Proxy signal antipattern（訊號要摸到 ground truth）、REFLEXES #51 Session ID schema（filename collision 有解、content collision 不解——本條是第三種：filename **drift**，不是撞名也不是內容衝突，是這次命名本身選錯了 handle）
- **verification_count**: 1
- **severity**: tactical（單次事件，未造成資料遺失或決策錯誤，僅讓下游任何靠檔名 pattern 找特定 routine 記憶的工具這一週漏看一筆——包括本審計自己，若非另外用 git log 交叉核對就會誤判「self-evolve-weekly 這週沒跑」）

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
- **可能層級**：通用反射（REFLEXES #45 OpenRouter hourly budget 同族——「共享額度池進 dispatch 預算」的 WebSearch instance）
- **相關**：#45
- **verification_count**: 1
- **severity**: tactical

### 2026-08-04 支語研究 — dedup-layer-silent-degradation：入庫查重的對照層會靜默退化

- **pattern**: dedup-layer-silent-degradation
- **原則**：資料入庫查重不能靠單一對照層——opencc import 失敗時正規化靜默退化成 identity、known 集合漏抓既有條目；必須有第二道「新資料值對全庫值」的 deterministic 掃描＋檔名存在檢查
- **觸發**：同 session 充電寶／老鐵／學渣本已在庫但 gap 對照誤判為缺口，靠 test -f＋china 值全庫掃接住 4 個潛在重複（創可貼／外賣／發貨／掃碼），0 誤入庫
- **可能層級**：通用反射（#65 awareness instrument 自身要 cross-verify 家族——查重器也是 instrument）
- **相關**：#65 #24
- **verification_count**: 1
- **severity**: tactical

## ✅ 已消化（保留 pointer）

<!-- distill 完的條目搬這裡 -->

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
