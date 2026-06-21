---
title: 'LESSONS-INBOX'
description: '教訓 buffer（intake layer）— 新教訓先 append 此處，週期性 distill 到 MANIFESTO/DNA/MEMORY canonical'
type: 'cognitive-buffer'
status: 'buffer'
apoptosis: 'never'
current_version: 'v2.2'
last_updated: 2026-05-10
last_session: 'twmd-distill-weekly-0954-evolve-pipeline'
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

### 2026-06-21 cicada-media — prettier 把 `_斜體_` caption 裡的 percent-encoded CJK URL `_NN.jpg` 弄壞成 `*NN.jpg`（attribution 連結斷）

- **pattern**: prettier-cjk-url-italic-mangle（markdown 工具鏈 silent breakage，「儀器看得見存在、看不見缺席」cluster 變體）
- **原則**：媒體 caption 包在 `_..._` 斜體、內含 markdown 連結到 percent-encoded CJK Commons 檔名（`File:…%E6%99%BA_05.jpg`）時，pre-commit 的 prettier 會把 URL 尾端的 `_05` 當斜體 delimiter 跟 caption 的 closing `_` 配對、整段改 `*`，URL 變 `…%E6%99%BA*05.jpg` → 連結指向不存在頁面。純 ASCII URL（陳建年 `_2.jpg`）因 intraword-underscore 規則沒爆，**只有 percent-encoded CJK 檔名觸發**。link-target check 排在 prettier 之後跑才抓得到，本次靠 commit 後手動回查 linter note 才發現。
- **mitigation（已 apply Cicada）**：caption 內不放 markdown 連結，attribution 寫純文字（`Photo: X / Wikimedia Commons，CC BY-SA 4.0`），可點連結放 `## 圖片來源` 段（不在斜體內，prettier 不動）。image-ingest 的「§圖片來源」貼字本來就走這條，問題出在我自作主張把連結也塞進 caption。
- **觸發**：2026-06-21 Cicada 影音 EVOLVE，翠池 hero caption `_…[CC BY-SA 4.0 via Wikimedia Commons](…File:翠池_汪大智_05.jpg)._` → prettier → `…BA*05.jpg).*`。
- **可能層級**：操作規則（EDITORIAL §媒體編織 / REWRITE Step 4.3 caption 寫法加「caption 不放 CJK-URL 連結，連結走 §圖片來源」）；或 reflex（「pre-commit prettier 之後必跑 link-target，不信 commit 前狀態」）
- **相關**：diary cluster「儀器只看得見存在、看不見缺席」（2026-06-10/12）/ REWRITE Step 4.3.6 caption 空行 check（同類 markdown-render silent breakage）/ link-target check
- **✅ 已儀器化 + canonical（2026-06-21 prettier-url-fix session）**：(1) 新 `article-health.py --check=link-url-mangle`（HARD 抓已壞 `*`-URL / WARN 抓 at-risk `_NN`-in-italic-caption；pre-commit profile `checks="*"` 已 wired，silent breakage 變 loud gate）；(2) EDITORIAL §媒體編織 加 canonical 註；(3) audit 修 13 檔已壞（科技園區發展／猴硐／沈伯洋 × lang），de-link 後 prettier-stable + link-target 綠。**carry**：~47 at-risk 檔（16 篇 × lang）de-link sweep 因 13+47=60 > §自主權邊界 50 檔，flag 哲宇拍板（spawn_task；instrument 已護住不會 silent 復發）。
- **verification_count**: 2（cicada-media 首見 + audit 證 13 檔跨 6 篇已壞、~47 at-risk = 廣域非單點）→ 已升儀器化，distill 時可移 §已消化
- **severity**: structural（任何帶連結的 CJK Commons 圖 caption 都會重現；斷連結 silent，不 fail build → 已用 link-url-mangle HARD gate 堵）

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
- **verification_count**: 2（#1 2026-06-20 embeddings keystone 首次達 escalation_n；#2 2026-06-21 routine-audit-weekly cycle 7 同 family extension — Chrome MCP unattended pairing 連 5 cycle block twmd-rewrite-daily SPORE broadcast + twmd-spore-harvest-am post-reset，兩條 device-dependent SPOF 同 root cause，合併計）
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

### 2026-04-29 α — 政治敏感題 SSODT 寫法 template（5-7 perspective 立體框架）

- **原則**：政治敏感議題（兩岸 / 跨國爭議 / 宗教政治關係）的文章不該因 MANIFESTO §自主權邊界「政治立場」就拒絕寫，而是用 SSODT 多元視角立體寫法繞過二元對立。每篇至少 5-7 個 perspective 立體並列，每個視角獨立站得住、不互相消解，每個 perspective 配 3-5 個獨立 source（學術 / 主流媒體 / 政府 / 當事方 / 批評者）。**判準**：「一個原本支持 X 的讀者讀完不覺得在攻擊我們；一個原本批評 X 的讀者讀完不覺得在幫他們宣傳；一個對 X 完全陌生的讀者讀完，能自己決定要從哪個維度繼續想」。
- **觸發鏈**：
  - #0 (2026-04-29 α) #675 法輪功 invitation v1+v2 朝 5-7 perspective（修煉者 / 學者 / 記者 / 批評者 / 兩岸稜鏡 / 跨教派比較 / 數位媒體生態）方向
  - #1 (2026-04-29 α) #687 吳百福「2300萬日圓買下張國文泡麵專利」跨國發明權爭議在 thanks comment 標明 SSODT 多視角待補（日本視角 / 第三方學者觀察 / 法律商業視角）
  - 同 family 但獨立議題：#0 法輪功（兩岸宗教政治）+ #1 吳百福（跨國商業歷史權威）— 都觸發同 SSODT template
- **可能層級**：哲學/操作規則跨層 → distill 到 EDITORIAL 作為「政治敏感題 SSODT 寫法 SOP」 + REWRITE-PIPELINE Stage 0 加敏感度判定觸發 SSODT template 引用
- **verification_count**: 2（同 session 內兩個獨立議題；待第 3 次跨 session 驗證再升 canonical）
- **severity**: structural（這是 Taiwan.md 處理政治/跨國爭議題的核心方法論，影響可信度）
- **相關**：MANIFESTO §熱帶雨林理論 / MANIFESTO §自主權邊界 / EDITORIAL / DNA #16 peer 是 peer 不是 source

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

### 2026-06-21 plurk-reach — 抓取/研究的完成判準：問「這是全部，還是端點願意給我的上限？」

- **原則**：資料抓取/研究的「完成」不等於「拿到一批乾淨資料」。先問「我看到的是全部，還是端點/工具願意回的上限？」satisficing 在 AI 把局部處理得很乾淨時最隱形——一份細緻的局部比粗糙的局部更危險，因為它不讓你起疑。對策：抓到固定數量（30/100/整數上限）就主動懷疑是 cap，去找分頁/游標/時間窗驗證真實總量；報告明確標 silent-cap limitation。
- **觸發**：2026-06-21 Plurk 受眾研究，curl 打 search2 端點拿 30 則就準備收尾報「就 30 則」，哲宇一句「往下滑」逼我去拆 date 游標，才發現 reach 是 day-1 起四波、三個月的河（每窗鎖 30，真實總量逾百）。差點把水面 30 則當全貌交差。
- **可能層級**：反射層候選（research/fetch 完成判準）——#73 查證反射 < 建造反射 的 completeness 維度延伸 + Workflow「no silent caps」原則的內化
- **相關**：REFLEXES #73 / #16（peer 是線索不是 source）
- **verification_count**: 1（首次記錄，需更多 case 累積才能稱 pattern）
- **severity**: structural（影響所有抓取/研究任務的完成判準）
- **Pointer**：[diary/2026-06-21-115925-plurk-reach.md](diary/2026-06-21-115925-plurk-reach.md) + [reports/plurk-reach-research-2026-06-21.md](../../reports/plurk-reach-research-2026-06-21.md)

### 2026-06-21 kuma-academy — A 級/政治文 Stage 3.5 必須 fetch-based adversarial verify，careful read 抓不到 citation-URL drift

- **pattern**: citation-url-drift-invisible-to-read
- **原則**：讀 prose 品質跟驗 source fidelity 是兩種不同的認知動作。footnote 指向哪個 URL 不影響句子讀起來對不對，所以 orchestrator 連讀兩遍 prose 對 citation-URL drift 完全隱形；只有真的 fetch 每個 URL 逐字比對的 adversarial agent 抓得到。root cause 常在上游：research-report §7 URL list 若只在 cluster 層精準（同一群報導都對）、atom 層不精（哪一篇講哪個 fact 給錯），會直接傳染成 writer footnote mis-map。對策：A 級/政治文 Stage 3.5 強制 fetch-based 逐 URL 比對（不可用 careful read 替代）；research-report URL list 要求 per-atom precise，不是 cluster-precise。
- **觸發**：2026-06-21 黑熊學院 NEW。對政治文做了兩遍仔細 prose 審查、抓 spine、修對位句，自覺完整；Sonnet verifier fetch 每個 URL 後抓到 `[^20]`/`[^22]` 政治 footnote 整個 swap（國台辦 2024-10-14 ↔ 重慶立案 2025-10-28）、hero `imageSource` 純幻覺檔名、2 句 paraphrase 戴 verbatim 引號、嘖嘖募資數字 source 之間兜不攏——全是 careful read 沒抓到的。
- **instances**：
  - 2026-06-21 kuma-academy（首次，政治文）：Sonnet verifier fetch 抓 `[^20]`/`[^22]` 政治 footnote swap + hero imageSource 幻覺 + 2 句 paraphrase 戴 verbatim 引號。
  - 2026-06-21 幾米-evolve（**非政治 People 文 — 證明範圍不限 A 級/政治**）：主 session ship 前自跑 fetch-verify 4 條高風險 cite，抓 2 錯——`[^16]` 月亮忘記了三事件 mis-cite 到一篇講抗癌的 ltn 文（內容對、source 掛錯）、`[^32]` 田中央丟丟噹森林 mis-cite 到只講火車移置的 lym.gov.tw 頁。命中率 50%。同一 root cause：orchestrator §7 URL list cluster-precise 非 atom-precise。
  - 2026-06-21 kuma-academy PR #1170 JOIN（**contributor 投稿，非自產 — 證明範圍含外部 PR 審核**）：idlccp1984 AI 工具編 9 個假 join.gov.tw slug URL（真實是 UUID），9 條腳註標題讀起來都對、上個 maintainer review 也只標「死連結」，curl 才知全 404 且是 fabrication；fetch-verify 找回 9 個真實 UUID 全換 + merge。第 3 次驗證跨「政治自產文 / 非政治自產文 / 外部 PR」三種 context，root cause 一致。
- **可能層級**：操作規則（REWRITE Stage 3.5 + MAINTAINER PR review **所有 depth 文 + 外部投稿** citation 強制 fetch-based，不限 A 級/政治）+ 通用反射（讀 ≠ 驗）
- **相關**：REFLEXES #31（sub-agent claim 是線索不是 oracle）/ #42 / #73（查證反射<建造反射）；2026-06-16 stage2-quote-context-collapse → REWRITE §Stage 2.5 source-fidelity gate（本案是該 gate 在 Stage 3.5 驗證端的延伸 worked example）
- **verification_count**: 3（≥3 達 distill 量門檻 — 下次 distill 可升 REFLEXES：「所有 depth 文 + 外部 PR 審核的 citation 必 fetch-verify 逐 URL，careful read 抓不到 URL drift」；跨 3 session 3 context 收斂）
- **severity**: structural（影響所有 depth article 的 ship 安全 — 範圍從「A 級/政治」擴大到「所有 depth」）
- **Pointer**：[memory/2026-06-21-135235-kuma-academy.md](memory/2026-06-21-135235-kuma-academy.md) / [memory/2026-06-21-154735-幾米-evolve.md](memory/2026-06-21-154735-幾米-evolve.md)

---

## ✅ 已消化（保留 pointer）

<!-- distill 完的條目搬這裡 -->

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
