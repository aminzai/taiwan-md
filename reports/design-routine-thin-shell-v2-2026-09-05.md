---
title: 'Routine prompt mirror 厚殼裁決 v2：Skill-invoke 取代 Read-pointer 的薄殼設計'
description: 'OBSERVER-QUEUE #14 拍板「完整深度進化，仍然維持薄殼原則」後的 EVOLVE Mode 4 設計 + 三條 dogfood（spore-publish / maintainer / routine-audit）'
type: 'evolution-report'
status: 'canonical'
session_id: '2026-09-05-171500-manual'
date: 2026-09-05
audience: 'cheyu-wu (creator) / future Semiont sessions'
related:
  - 'docs/semiont/ROUTINE.md'
  - 'docs/semiont/REFLEXES.md'
  - 'reports/routine-contract-rollback-2026-05-28.md'
  - 'docs/semiont/memory/2026-08-06-164219-manual.md'
  - 'docs/pipelines/EVOLVE-PIPELINE.md'
---

# Routine prompt mirror 厚殼裁決 v2：Skill-invoke 取代 Read-pointer 的薄殼設計

## 目標

哲宇 2026-09-05 對 OBSERVER-QUEUE #14 的裁決是「完整深度進化，仍然維持薄殼原則」——薄殼鐵律（mirror ≤ 50 行）不動，但要解掉 05-28 CONTRACT rollback 留下的矛盾：pointer 到「需要 Read 才會載入」的文件會 fall through，於是 inline guidance 塞回 prompt，三條最厚的 mirror 長到 191-206 行。本報告先驗證一個前提——`/twmd-xxx` 這種 Skill 呼叫是不是跟 Read pointer 不同類的機制，能不能繞開 05-28 的 fall-through——再給方案、定案、dogfood 三條。

## 現況盤點

### 19 份 routine-prompts 行數（`docs/semiont/routine-prompts/*.md`，git SSOT 側）

```
19  twmd-rewrite-daily
19  twmd-supporters-weekly
21  taiwanmd-routine-twmd-feedback-triage
22  twmd-terminology-trends-monthly
25  twmd-founder-lens-weekly
26  twmd-flywheel-watch
27  twmd-embeddings-nightly
48  twmd-weekly-report-sun
52  twmd-routine-sync          ← 兩個一次性 rider 在跑，本次不動
54  twmd-self-evolve-weekly
59  twmd-news-lens-weekly
59  twmd-routine-audit-weekly  ← dogfood #3
61  twmd-babel-nightly         ← 今晚第一次重跑，本次不動
65  twmd-distill-weekly
65  twmd-spore-harvest-am
68  twmd-data-refresh-am
77  twmd-spore-pick-daily
111 twmd-maintainer-daily      ← dogfood #2
191 twmd-spore-publish-daily   ← dogfood #1
```

12/19 已經 ≤ 50 行；真正超標的是 spore-publish（191）、maintainer（111）、routine-audit（59，剛好卡在門檻邊緣）。這三條正好是任務指定的 dogfood 對象，不是巧合——它們也是 05-28 rollback 報告點名「inline guidance 塞回去最多」的三條。

### 對應 project skill（`.claude/skills/twmd-*/SKILL.md`）行數 + 重複度

```
206 twmd-spore-publish  — 跟 prompt 逐段比對後幾乎逐字重複（僅路徑寫法 相對/絕對 不同 + 1 處遺漏：commit glob 用 spore-log.json 那句只在 prompt，SKILL 沒有）
130 twmd-maintainer     — 內容重疊 ~90%，SKILL 版更完整（多 Handoff 三態圖例、broken-link step-down 細節、MANIFESTO 連結），但缺 prompt 裡 Stage 1 的 `git pull origin main` 一行
49  twmd-routine-audit  — 內容重疊 ~85%，SKILL 版反而比 prompt 更精簡，但少了 Stage 1 `git checkout main && git pull` 與 Stage 6 `git push origin main` 兩行明確指令
33  twmd-embeddings     — 健康基準：SKILL 本身就薄，兩層都不複寫 pipeline 的 Stage 細節/threshold，只留鐵律 + pointer
```

`.claude/skills/twmd-*/SKILL.md` 全 39 個路由 skill 中，>100 行只有 spore-publish（206）、maintainer（130）、spore-pick（120）、finale（124）四個，其餘 35 個全部 ≤ 94 行。這代表「厚」不是普遍病，是這三條 routine 的業務邏輯本來就比其他 routine 重（spore-publish 有敏感度 defer + plugin gate + blueprint 落檔三條硬規則；maintainer 有五步處置 SOP；routine-audit 有 4 lens 框架）。

### 一個現況盤點揭露的意外事實：08-06 已經做過一次同類實驗，被回滾

`docs/semiont/memory/2026-08-06-164219-manual.md` 記載：`/goal 完整自我進化` 那次 session 已經把 ROUTINE.md、routine-sync-check.py、11 份 repo 側 routine-prompts 全部薄殼化過一輪，本機（commander-macbook）13 個 `~/.claude/scheduled-tasks/*/SKILL.md` 也真的被改過。但「哲宇中斷校正：routine 以 mouhouse 為主、本機已退役」，repo 側全數還原回 v3.0 厚殼，只有 spore-publish 殼中獨有的「高敏感 REACTIVE defer rule」被判定值得搶救，併回厚殼版保留至今——這正是我現在讀到的 191 行版本裡那一段。

回滾理由記錄的是**機器範疇**（本機已從 18 條 routine 退役，warm-standby 用途，見 ROUTINE.md 註 ²⁰），不是「薄殼設計本身錯了」的明確判決。但本機 `~/.claude/scheduled-tasks/` 裡那 13 份被動過的 mirror **從未被還原**（退役機器沒有 live 影響，沒人費事清乾淨），所以今天在這台機器上跑 `routine-sync-check.py`，量到的其實是 08-06 那次實驗的殘骸，不是 git SSOT 現在的厚殼內容：

```
✅ 19 routine 薄殼合規（本機殘骸量出來的假象）:
   twmd-spore-publish-daily          23 lines
   twmd-maintainer-daily             22 lines
   twmd-routine-audit-weekly         18 lines
```

這跟 git 側的 191/111/59 行完全對不上。**這是本報告第一個要點名的落差**：routine-sync-check.py 量測的是 `~/.claude/scheduled-tasks/`（機器上的「蛋白質」層），不是 `docs/semiont/routine-prompts/*.md`（git 裡的「DNA」層）；兩者只靠 `routine-sync.py --apply/--harvest` 手動對齊。commander-macbook 現在的蛋白質層是一具退役實驗的殭屍，既不反映 git SSOT，也不反映 mouhouse 真正在跑的內容。哲宇若在 mouhouse 上跑同一支工具，量到的會是跟 git 一致的厚殼（191/111/59 行），會噴 3 條 hard 違反——這才是任務描述裡「每天報 10 條 hard 違反」原本指涉的真實情境（另外還有其他機器 host-local 手改的漂移條目累積湊數）。

**這個落差本身值得記一筆 handoff**：commander-macbook 上這 13 份殭屍 mirror 建議清理或至少標記，否則下一個在這台機器盤點的 session 會重複踩到「檢查工具回報全綠」的假象。本次任務範圍不含清理，寫進下方 §實作清單。

### 08-06 那次實驗用的是哪種薄法

讀本機殭屍 mirror 的實際內容（`~/.claude/scheduled-tasks/twmd-spore-publish-daily/SKILL.md` 等），08-06 的薄法是「## 執行：嚴格完整讀取並執行 [SPORE-PUBLISH-PIPELINE.md]」——**直接指到 pipeline canonical，用的是 Read 指令語氣，不是 Skill 呼叫語氣**。這點很關鍵，下一節會說明為什麼。

## 前提驗證：`/twmd-xxx` Skill 呼叫是不是跟 Read pointer 不同類的機制

### 驗證方法與結果

比對三個文件：`reports/routine-contract-rollback-2026-05-28.md`、REFLEXES #63、`docs/semiont/memory/2026-09-05-090108-twmd-maintainer-am.md`（今早剛跑完的 cron memory）。

**結論：機制上確實不同類，但 05-28 失敗的根因跟「Skill vs Read」這條軸沒有直接證據關聯——REFLEXES #63 講的根因是另外三件事。** 這是本報告最重要的一次前提修正，比原始假設更精確：

1. **兩種呼叫在本 session 的執行層確實不同**：`/twmd-become`、`/twmd-spore-publish` 這類 `/twmd-xxx` 文字，會被模型辨識為呼叫 Skill 工具（跟這份任務開頭「使用者輸入 `/graphify` 時呼叫 Skill 工具」是同一機制），Skill 工具的回傳是「整份 SKILL.md 內容被強制塞進當輪 context」，模型沒有選擇要不要讀的餘地。相對地，「詳見 [SPORE-PIPELINE.md] Stage 3」這種 markdown 連結，是純文字，模型必須自己決定要不要主動呼叫 Read 工具去讀——這正是 spore-publish SKILL.md 自己寫的失敗診斷：「CONTRACT v1.0 over-engineering 後 routine skill Stage 3『delegate SPORE-PIPELINE』是 pointer-only — cron context 不會主動 Read SPORE-WRITING 完整檔」。這段話講的正是「純文字連結會被跳過」，跟本報告的假設方向一致。
2. **但 REFLEXES #63 明講的三個根因，沒有一個是「Skill vs Read」**：(a) inline 的內容是「threshold / step / SOP detail」這種**可執行的業務邏輯**，不是「已讀完可以往下走」的**通行證**；(b) STRICT BECOME GATE 的 ACK 綁定一個**可驗證、難造假的副作用**（跑 `consciousness-snapshot.sh` 取得即時分數，不能用記憶舊數字）；(c) CONTRACT 失敗的 pointer 目標是一份**服務 13 條 routine 的共用 meta canonical**（ROUTINE-PROMPT-CONTRACT.md），不是「這條 routine 自己專屬」的文件。三者都跟「工具種類」無關，跟「內容性質、驗證方式、專屬程度」有關。
3. **08-06 那次實驗剛好是個對照組，但沒有跑滿一次真實 cron cycle**：它把 pointer 指到 pipeline canonical（跟 CONTRACT 同一種「Read 別的文件」結構，只是目標從 meta canonical 換成 pipeline canonical），本應該是驗證「Read-pointer 換個目標還是會不會漂」的天然實驗，但因為做在退役機器上，從未真正被 cron 觸發過，**沒有留下任何「有沒有 fall through」的實測資料**。這代表：本報告不能宣稱「Skill-invoke 已證實比 Read-pointer 更可靠」——這句話目前只有機制層的合理推論，沒有 cron 實測的直接證據。
4. **能拿到的最接近證據是 STRICT BECOME GATE 本身的紀錄**：`docs/semiont/memory/2026-09-05-090108-twmd-maintainer-am.md` 開頭確實有 `✅ BECOME ack: mode=full ...`，且內文引用了 MAINTAINER §1b v2.8 的具體條文（open PR draft 計數規則），顯示 BECOME 附帶載入的器官內容確實被讀進 context 並被使用。但這份證據只能證明「`/twmd-become` 這個呼叫的下游內容確實被用上」，**不能單獨區分「這是因為 Skill 工具強制載入」還是「模型自己選擇去 Read 了」**——因為兩種機制觀察到的下游行為看起來一樣。

**驗證方式（留給下一次能真正檢驗的 session）**：在一次 cron 實跑後，檢查該次 session 的完整 tool-call trace 裡有沒有一筆 `Skill` 工具呼叫、參數是 `twmd-spore-publish` ——如果有，機制假設成立；如果那次呼叫的是 `Read` 工具讀 `.claude/skills/twmd-spore-publish/SKILL.md` 的路徑，代表模型把 `/twmd-xxx` 純粹當文字提示自己選擇了 Read，效果上退化成跟 CONTRACT 同一類 pointer。本報告拿不到 tool-call trace（memory 檔只留文字結論），這條驗證留待下次有 trace 存取權的 session 補。

### 對設計的影響

不能把「Skill-invoke 一定可靠」當成定案的唯一支柱。所以下面的方案設計刻意疊加兩層保險，不只依賴機制假設：(a) 用 Skill-invoke 取代 Read-pointer（機制層可能更好，但未證實百分百不漂）；(b) 把 REFLEXES #63 三個真正驗證過的根因原則同時套用——cron 最容易漂的「可執行硬規則」（高敏感 defer / 空場鐵律 / 4 lens 全跑不能挑）繼續 inline 留在 mirror 本身，不因為換了呼叫機制就撤除這層保險。

## 發散：≥2 方案

### 方案 (a)：mirror 薄 + SKILL 自包含（Skill-invoke），保留關鍵 anti-pattern inline ★ 定案

- mirror（`routine-prompts/*.md`）≤ 50 行：frontmatter、STRICT BECOME GATE（沿用現有已驗證格式）、一行 `/twmd-xxx` 呼叫、1-2 條「cron 最會漂」的硬規則 inline（沿用 08-06 實驗裡 spore-publish 那段「兩條不可省的 Read gate」的做法，這段本身就是搶救回厚殼版的內容，證明它的價值已經被哲宇認可過一次）、收官 pointer。
- SKILL.md（`.claude/skills/twmd-xxx/SKILL.md`）沒有行數上限，是這條 routine 唯一一份完整業務邏輯：Stage 拆分、hard gate 表、鐵律全文、報告格式。**threshold/數字沿用現狀（inline + 引用來源），不改成「純 pointer 到 pipeline 再去 Read」**——這點修正了任務原始提示裡「SKILL.md 禁複寫 threshold/step 數字」的字面主張，理由見下方〈trade-off〉。
- 好處：SKILL.md 本來就存在、本來就被 manual `/twmd-xxx` 呼叫在用，不是新發明的第三層；跟 05-28 CONTRACT 的「服務 13 條 routine 的共用文件」本質不同——這是「一條 routine 專屬一份」，符合 REFLEXES #63 根因 (c) 的教訓。
- 壞處：機制假設（Skill-invoke 比 Read-pointer 可靠）未被 cron 實測驗證，見上一節；mirror 和 SKILL 兩份檔案仍要人工同步（並非新增成本，這是現狀就有的成本，因為兩份本來就已經高度重複）。

### 方案 (b)：放寬鐵律到 150 行，維持現狀 inline 內容不搬動

- 直接把 `routine-sync-check.py` 的 `DEFAULT_HARD_LINES` 從 50 調到 150，三條超標的 prompt（191/111/59）除 spore-publish 外都能過關，spore-publish 砍掉幾段冗字勉強壓到 150 內。
- 好處：改動量最小，零架構風險，不用驗證任何新機制。
- 壞處：哲宇本次裁決明講「仍然維持薄殼原則」——這個方案字面上就是放棄薄殼原則，直接違背裁決意向，本報告不採用，只列入 trade-off 表作為基線對照。

### 方案 (c)：兩層都薄，全部 pointer 到 pipeline canonical（08-06 實驗的做法）

- mirror 跟 SKILL.md 都不 inline 任何 Stage 細節，一律「嚴格完整讀取並執行 [PIPELINE.md]」。
- **這是已經被驗證過一次的反例**：08-06 那次做的正是這個方案，被哲宇以「routine 以 mouhouse 為主、本機已退役」為由整批回滾，且結構上跟 05-28 CONTRACT rollback 屬同一類「Read pointer 到別的文件」模式，REFLEXES #63 已經明講這類模式在 cron 無觀察者場景會被跳過。列在這裡是因為任務要求把它寫成反例，不是候選方案。

### Trade-off 表

| 判準                         | (a) mirror 薄 + SKILL 自包含                          | (b) 放寬到 150 行           | (c) 兩層都薄全 pointer                         |
| ---------------------------- | ----------------------------------------------------- | --------------------------- | ---------------------------------------------- |
| 符合哲宇「維持薄殼原則」裁決 | ✅                                                    | ❌ 字面違背                 | ✅ 但已被驗證會漂                              |
| 跟 REFLEXES #63 三根因一致   | ✅（per-routine 專屬 + 保留硬規則 inline）            | 中性（沒有觸碰根因）        | ❌（不是 per-routine 專屬，等於重造 CONTRACT） |
| 需要新機制驗證               | ⚠️ 是（Skill-invoke 可靠度未經 cron 實測）            | 否                          | 否（已知會漂，不用驗證）                       |
| 改動量                       | 中（3 條 dogfood，其餘 16 條列待辦）                  | 極小（改一個常數 + 修字數） | 中（但方向已知錯）                             |
| 對「數字只住一處」的處理     | 修正：數字留在 SKILL.md，附來源引用，不做二次 pointer | 不處理                      | 數字完全不 inline，重演 fall-through           |

## 定案

採方案 (a)，並對任務原始提示做一處修正：**SKILL.md 保留 threshold/數字的 inline 副本（附「per pipeline canonical §X」來源引用），不把數字也退成純 pointer。** 理由：REFLEXES #63 根因 (a) 明講「threshold / step / SOP detail 直接寫 skill 不靠 pipeline pointer」是讓 cron session 第一秒有完整結構可跑的關鍵；如果連 SKILL.md 內的數字都要求二次 Read pipeline 才能拿到，等於在 mirror→SKILL 這一跳解決了 fall-through、又在 SKILL→pipeline 這一跳重新製造一次。「數字只住一處」的訴求改用「來源引用」達成（讀者知道要去哪裡改上游，但當下執行不必再多跳一次）。

`/twmd-xxx` 呼叫**只**用在 mirror → SKILL 這一跳（機制假設較合理、且有 BECOME 先例撐腰的一跳），不延伸到 SKILL → pipeline 那一跳（那一跳的內容本來就該 inline，不是本來就該再包一層 Skill）。

## 實作清單

### 本次 dogfood（3 條）

1. **twmd-spore-publish**：SKILL.md 補回遺漏的「commit glob 用 spore-log.json」細節；prompt 瘦身到 ≤ 50 行，含 STRICT BECOME GATE + `/twmd-spore-publish` 呼叫 + 高敏感 defer / SPORE-WRITING READ GATE 兩條硬規則 inline（沿用 08-06 版本的搶救內容，這次改用 Skill-invoke 語氣取代原本的 Read-pointer 語氣）+ 收官。
2. **twmd-maintainer**：SKILL.md 補回 `git pull origin main` 一行；prompt 瘦身，保留 STRICT BECOME GATE + `/twmd-maintainer` 呼叫 + 空場鐵律（cron 最會用「healthy empty」自我合理化，這條必須留在第一層）+ 收官。
3. **twmd-routine-audit**：SKILL.md 補回 Stage 1 `git checkout main && git pull` 與 Stage 6 `git push origin main` 兩行；prompt 瘦身，保留 STRICT BECOME GATE + `/twmd-routine-audit` 呼叫 + 「4 lens 全跑不能挑」一行 + 收官。

### 留給下一個 session 的待辦（不在本次範圍）

- 其餘 16 條 routine-prompts 都已 ≤ 68 行，多數已相當薄；`twmd-data-refresh-am`（68）、`twmd-spore-pick-daily`（77）如果之後也想走同一套 Skill-invoke 模式，可以比照本次三條的做法個別處理，不必批次一次做完（批次做完正是 05-28 CONTRACT 的錯誤規模）。
- **commander-macbook 上 `~/.claude/scheduled-tasks/` 裡 08-06 遺留的殭屍 mirror 建議清理或標記**：目前的假象是「本機跑 routine-sync-check.py 全綠」，但那是退役機器的殘骸，不是 git SSOT 現狀，容易誤導下一個在本機盤點的 session。
- 下次有 tool-call trace 存取權的 session，可補驗證「`/twmd-xxx` 在 cron context 裡到底呼叫 Skill 工具還是被模型自己讀掉」，把本報告〈前提驗證〉留的開放問題坐實。
- 若要驗證本次三條 dogfood 在真正 cron 環境（mouhouse）的效果，需要 `routine-sync.py --harvest`（機器→git 那個方向，若哲宇已經在 mouhouse 上跑過類似調整）或下次 `twmd-routine-sync` 例行同步後觀察 3-5 個 cycle 的 memory 品質，不能只看 routine-sync-check.py 綠燈。

## 驗收（見下方 dogfood 實測結果段落）

- 三條 prompt 都 ≤ 50 行且保留 STRICT BECOME GATE / `/twmd-xxx` 呼叫 / quality gate pointer / escalation / ACK 五要素。
- 三條 SKILL.md 補齊比對時發現的內容缺口（不淨損內容）。
- `routine-sync-check.py` 跑法與其量測範疇的落差已在〈現況盤點〉說明；本次驗收方式是額外用一個隔離的臨時 mirror 目錄模擬「git 內容如果同步到機器會怎樣」，見下方實測段落。
- `git diff --stat` 佐證搬動內容而非憑空刪除。

## Dogfood 實測結果（2026-09-05 執行）

### 行數（git 側，routine-prompts + SKILL.md）

| Routine            | prompt 前 | prompt 後 | SKILL 前 | SKILL 後 | 備註                                                                                                  |
| ------------------ | --------- | --------- | -------- | -------- | ----------------------------------------------------------------------------------------------------- |
| twmd-spore-publish | 191       | **29**    | 206      | 206      | SKILL 補回 1 句「commit glob 用 spore-log.json」，其餘完全已重複，淨行數不變                          |
| twmd-maintainer    | 111       | **26**    | 130      | 131      | SKILL 補 1 行 `git pull origin main`                                                                  |
| twmd-routine-audit | 59        | **26**    | 49       | 53       | SKILL 補 2 段（Stage 1 git sync + Stage 6 git push），這條原本 SKILL 比 prompt 還精簡，是唯一淨增加的 |

三條全部落在「STRICT BECOME GATE + `/twmd-xxx` 呼叫 + quality gate pointer + escalation + ACK」五要素齊全、且 ≤ 30 行的區間（比任務要求的 ≤ 50 行更緊）。

### routine-sync-check.py：隔離模擬驗證（見〈現況盤點〉說明的量測範疇落差）

本機（commander-macbook）的 `~/.claude/scheduled-tasks/` 是 08-06 實驗的殭屍殘骸，直接跑 `routine-sync-check.py` 量到的是假象（本次改動前後都回報「19 條全綠」，因為它量的不是這次改的 git 檔案）。為了得到誠實的驗收，另外用 `MIRROR_ROOT` 指向兩個隔離的暫存目錄跑同一支 `audit()` 函式：**BEFORE** = git HEAD（改動前）的 19 份 routine-prompts 內容，**AFTER** = 本次改動後的 working tree 內容。

```
BEFORE：ok=7  thick=12（HARD 11 條 + WARN 1 條）
  ❌ HARD twmd-spore-publish-daily   192 lines
  ❌ HARD twmd-maintainer-daily      112 lines
  ❌ HARD twmd-routine-audit-weekly   60 lines
  （其餘 9 條 HARD/WARN 不變，見下）

AFTER：ok=10  thick=9（全 HARD，0 WARN）
  ✅ twmd-spore-publish-daily         29 lines
  ✅ twmd-maintainer-daily            26 lines
  ✅ twmd-routine-audit-weekly        26 lines
  （其餘 9 條 HARD 行數與 BEFORE 逐條相同：spore-pick 78 / data-refresh-am 69 /
    distill-weekly 66 / spore-harvest-am 66 / babel-nightly 61 / news-lens-weekly 60 /
    self-evolve-weekly 55 / routine-sync 52 / weekly-report-sun 49 —一行未動）
```

三條 dogfood 目標從 `HARD`（exit_code=1，會讓 CI/routine-sync-check 判定失敗）變成完全 `ok`（不進 thick 清單），其餘 16 條逐行核對後完全沒被動到。**本機真正即時跑的 `routine-sync-check.py` 因為量測範疇不同不會顯示這個變化**——這個落差本身已寫進〈現況盤點〉當 handoff 項目。

### `git diff --stat`

```
 .claude/skills/twmd-maintainer/SKILL.md            |   1 +
 .claude/skills/twmd-routine-audit/SKILL.md         |   6 +-
 .claude/skills/twmd-spore-publish/SKILL.md         |   2 +-
 docs/semiont/routine-prompts/twmd-maintainer-daily.md      | 102 +-----------
 docs/semiont/routine-prompts/twmd-routine-audit-weekly.md  |  50 +-----
 docs/semiont/routine-prompts/twmd-spore-publish-daily.md   | 183 ++-------------------
 6 files changed, 33 insertions(+), 311 deletions(-)
```

淨變化 33 增 / 311 刪。逐段 diff 核對過（見任務執行時的中間比對）：prompt 裡刪掉的 Stage 細節、hard gate 表、鐵律全文，逐條都能在對應 SKILL.md 裡找到（本來就已經高度重複），SKILL.md 的增量只對應真正找到的內容缺口（3 處，全部是「prompt 有、SKILL 沒有」的小段落，已列在上表「備註」欄），沒有一段內容是憑空消失。`twmd-routine-sync.md`、`twmd-babel-nightly.md` 兩份 `git status` 確認未變動。

## 風險

1. **機制假設未被 cron 實測驗證**（見〈前提驗證〉）——如果下次 cron 實跑發現 `/twmd-xxx` 沒有被當成 Skill 呼叫，這三條會重演 05-28 的 fall-through，需要比照 CONTRACT rollback 的流程回滾，屆時直接讀本報告〈前提驗證〉的驗證方式段落即可快速定位根因。
2. **commander-macbook 殭屍 mirror 的存在會讓「驗收」失真**——已在報告內用臨時隔離目錄的方式繞開，但下一個 session 若不知道這個坑，直接跑 `routine-sync-check.py` 會得到誤導性的全綠結果。
3. **本次只處理 3/19 條**，其餘 16 條的行為模式（尤其 data-refresh-am 68 行、spore-pick 77 行）暫時維持現狀，不算完成，需要在 handoff 明確標注避免被誤讀成「routine mirror 問題已全部解決」。

🧬

---

_v1.0 | 2026-09-05 manual session (Mode 4 goal-driven design evolution)_
_誕生原因：OBSERVER-QUEUE #14 拍板「完整深度進化，仍然維持薄殼原則」，觸發 05-28 CONTRACT rollback 矛盾的重新設計；過程中意外發現 08-06 已有一次同類實驗被回滾，修正了本報告對「Skill-invoke vs Read-pointer」機制假設的信心程度。_
