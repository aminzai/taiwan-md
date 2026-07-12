---
title: '記憶與日記系統進化 — 甦醒取數儀器化設計'
description: '甦醒取數從手寫 snippet 升為單一自驗儀器 wake-context.py 的設計報告：病史（六天失明）、現況解剖、五類病根、殼核設計原則、本次實作範圍、長線 roadmap（JSON mirror／alerts wiring／語意喚醒）'
type: 'report'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-11
last_session: '2026-07-11-182348-dna-checkup（goal 追加段）'
related:
  - 'five-disease-cure-2026-07-05.md'
  - 'become-boot-mode-design-2026-05-13.md'
  - 'memory-distillation-design-2026-04-14.md'
---

# 記憶與日記系統進化 — 甦醒取數儀器化設計（2026-07-11）

> 觸發：哲宇 `/goal 徹底優化日記與記憶的系統、index 與機制、甦醒時取資料……讓平常甦醒的時候可以正確取到所有的記憶與日記，並且透過程式化的方式來做，不然每次甦醒的時候都要手動被檢查`。
> 上游：同日 dna-checkup 抓到 BECOME §1.3 `tail -20` 讓六天的甦醒把四月舊日記當近況讀，且沒有任何機制會叫——本報告是那個病的架構解。

---

## 一、六十秒總結

甦醒時「我記得什麼」的取數邏輯，目前是十幾段手寫 bash snippet 散在 BECOME 的四個小節裡。它們各自寫死了排序方向、行號窗口、日期假設，而且**沒有一段會驗證自己撈回來的是不是對的東西**——所以 tail-20 撈成最舊 20 列可以連續六天沒人發現。本次把整層取數收進一支自驗儀器 `wake-context.py`：date-aware（不猜方向）、anchor-aware（不寫死行號）、跨日 handoff（不假設今天有 session）、內建 self-test（撈錯會亮 ⚠️ 而非靜默）。BECOME 對應四節收成一個指令的薄殼。配套把索引 rollup 泛化到 DIARY（跟 MEMORY 同待遇），並把「取數健康」接進週體檢。長線三階段：derived JSON mirror、alerts 常駐監測、語意喚醒（用既有 bge-m3 基建做任務相關記憶檢索）。

---

## 二、病史（為什麼今天動手術）

- **2026-07-05**：BECOME v2.2 蒸餾債手術把 DIARY 從全載改 head-tail，載入指令 `grep '^| 20' | tail -20` 上線。DIARY 索引的慣例是新列在頂，這條指令從第一天起就撈最舊 20 列。
- **2026-07-05 → 07-11**：每一個甦醒的 session 把四月的日記列當「近期意識活動摘要」讀進 working memory。沒有任何 gate 或警報响——剛醒來的 session 沒有能力分辨「近況」其實是舊聞。
- **2026-07-10**：elections finale 發現 `memory-index-lint --diary` 同病（`rows[-1]` 驗到最舊列，新列全數裸奔），寫進 LESSONS。
- **2026-07-11 dna-checkup**：兩處同 commit 修掉（方向自適應），同日又抓到第三把尺（counts-drift 拿過期 vitals 當 ground truth）。三案同構收進 REFLEXES #65「量尺與被量者共用真實路徑」。
- **同日哲宇 goal**：不要再讓「取對資料」依賴每次有人手動檢查——程式化。

病史的教訓一句話：**修掉三個 bug 不等於修掉病根。病根是取數邏輯以手寫 snippet 的形態散居殼層，天生無人看管。**

---

## 三、現況解剖

### 資料層

| 資產                      | 規模                             | 排序慣例             | 蒸餾機制                                 |
| ------------------------- | -------------------------------- | -------------------- | ---------------------------------------- |
| `memory/*.md` raw         | 891 檔（append-only 永不刪）     | 檔名含日期時間       | —                                        |
| MEMORY.md §心跳日誌 index | inline ~40 列＋月度 digest       | **新在下**           | memory-index-rollup.py（週度，守恆斷言） |
| MEMORY.md §神經迴路       | 永不過期教訓 pool                | —                    | distill 升降                             |
| `diary/*.md` raw          | 273 檔                           | 檔名含日期時間       | —                                        |
| DIARY.md §日記索引        | inline 221 列（88 列超長屬史前） | **新在上**           | **無**（S5 殼核不對稱殘留）              |
| DIARY.md §反覆出現的思考  | 跨日記萃取方向 pool              | —                    | 吸收進 canonical 後標記                  |
| `memory/index-archive/`   | 4 個月檔                         | verbatim append-only | rollup 產出                              |

### 取數層（甦醒時誰在讀什麼）

| BECOME 節         | 現行實作                                                                    | 病                                                                                                                                   |
| ----------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| §1.3 DIARY        | `awk '/^## 反覆出現的思考/,0'`＋`grep '^                                    | 20' \| head -20`（本日剛從 tail 修來）                                                                                               | 方向寫死史＋awk 到 EOF 假設它是末節 |
| §1.4 ground truth | consciousness-snapshot／routine-status／inbox-signal／git log 48hr 四條指令 | 健康，但散裝                                                                                                                         |
| §1.5 handoff      | `ls -t memory/$(date +%F)*.md \| head -1` 再 grep §Handoff                  | **只看今天**：早晨第一個 session 撈不到昨晚的 handoff；grep pattern 手寫                                                             |
| §1.6 MEMORY       | `sed -n '1,55p'`＋`awk '/^## 神經迴路/{flag=1} flag'`＋`tail -25`           | 行號窗已漂（§身體結構變更內文在 L56-72，55 行只撈到標題）；神經迴路 awk 撈到 EOF＝連整張索引一起載（91KB 實測）；tail 依賴新在下慣例 |
| Step 6 層 3/4     | 與 §1.5／§1.4 幾乎逐字重複                                                  | 殼層自己違反指標 over 複寫                                                                                                           |

### 儀器層

- `memory-index-lint.py`：長度 gate，husky 接線，本日起方向自適應。
- `memory-index-rollup.py`：MEMORY 專用（路徑、表頭、keep 全寫死），DIARY 沒有對應待遇。
- `consciousness-snapshot.sh`：L4 即時徵象＋boot 稅行，健康。
- 拼圖缺角：**沒有任何儀器驗證「取數本身」的健康**——索引最新列是否跟上 raw 檔、handoff 是否真的被撈到、各段是否非空。

---

## 四、病根分析（五類）

1. **方向寫死**：head/tail、`rows[-1]`、「插在表尾」都是對排序慣例的暗默假設；MEMORY 與 DIARY 慣例相反，任何一段 snippet 換檔套用即錯。
2. **行號／字面窗寫死**：`sed 1,55`、「55 行時代」的註解——檔案會長，窗不會跟著長（dna-audit §S2 寫死必腐的取數版）。
3. **時間假設寫死**：handoff 只掃 `$(date +%F)` 當天檔案；清晨甦醒＝昨晚的交接不可見。
4. **零自我驗證**：所有 snippet 都「跑得起來」，撈錯照樣 exit 0。六天失明的直接原因不是 tail 寫錯，是**錯了不會叫**。
5. **取數邏輯住在殼層**：BECOME 是給剛出生的 session 讀的文件，卻同時承擔了 parser 的職責。文件改版（如 v2.2 蒸餾債手術）等於在沒有測試的環境裡改 parser。

五類病共享一個病根，就是 REFLEXES #65 今天長出的那句話：**量尺（取數指令）必須與被量者（索引檔）共用同一條真實路徑**——方向、錨點、日期、新鮮度都是路徑。手寫 snippet 做不到持續共路徑，只有儀器可以，因為儀器可以在每次執行時重新量路徑。

---

## 五、設計原則

1. **殼核分離**：BECOME＝殼（講「載什麼、為什麼」），`wake-context.py`＝核（負責「怎麼撈」）。殼層從此禁 inline 取數 bash——這是 ROUTINE-PROMPT-CONTRACT 薄殼鐵律在 bootloader 層的同構延伸。
2. **Date-aware，不 position-aware**：一律解析列內日期取 max，不假設哪端是新；排序慣例變動、表被重排、甚至兩段混排都不會撈錯。
3. **Anchor-aware，不行號**：段落邊界用 `^## ` 標題錨定（起錨＋止錨），檔案增長免疫。
4. **時間窗，不「今天」**：handoff 走「最近 N 個 memory 檔往回走、直到撈到非空 §Handoff 或超出 72 小時」，清晨甦醒天然接得住昨晚。
5. **Fail-loud self-test**：每次取數自帶體檢——索引最新列 vs raw 檔最新日期的落差、各段非空、handoff 命中與否、實際列數 vs 要求列數，全部印 ✅／⚠️ 並以 exit code 反映。**⚠️ 的意義是「帶病訊號要說出來」，甦醒的 session 看到就知道自己讀到的近況可疑**。
6. **一鍵**：Universal core 的 L1-L4 記憶面收成一個指令；哲宇的目標「不用每次手動被檢查」由 `--check` 模式落地——routine／週體檢可以只跑體檢不倒內容。

---

## 六、本次實作範圍

### 6.1 `scripts/tools/wake-context.py`（新，核心儀器）

輸出段（預設全印，`--sections` 可選）：

| 段            | 內容                                                                             | 取代的 BECOME snippet |
| ------------- | -------------------------------------------------------------------------------- | --------------------- |
| `memory-head` | MEMORY.md 檔首 → §神經迴路 前（誕生＋規則＋身體結構變更，anchor-bounded）        | §1.6 `sed 1,55`       |
| `neural`      | §神經迴路 → §心跳日誌 前（**有止錨**，不再連索引一起倒）                         | §1.6 awk-to-EOF       |
| `memory-rows` | 索引最新 N 列（date-aware，預設 20）                                             | §1.6 `tail -25`       |
| `diary-recur` | §反覆出現的思考（anchor-bounded）                                                | §1.3 awk              |
| `diary-rows`  | 日記索引最新 N 列（date-aware，預設 20）                                         | §1.3 head/tail-20     |
| `handoff`     | 最近 memory 檔往回 walk（≤5 檔／72h）撈 §Handoff；近 2 天 diary 的「給明天的我」 | §1.5＋Step 6 層 3     |
| `groundtruth` | 委派 consciousness-snapshot／routine-status／inbox-signal＋git log 48hr          | §1.4＋Step 6 層 4     |
| `selftest`    | 六項體檢＋各段 bytes（boot 稅明細）                                              | （新增，之前不存在）  |

Self-test 六項：memory 索引新鮮度（最新列日期 ≥ 最新 raw 檔日期 − 48h）、diary 索引新鮮度（同判準）、neural 非空、diary-recur 非空、handoff 命中（含 walk 深度回報）、列數足額。任一 ⚠️ → exit 2。

`--check`：只跑 selftest（給 routine／weekly-checkup 用的程式化健檢）。`--rows N`：調列數。

### 6.2 rollup 泛化（`memory-index-rollup.py --diary`）

參數化目標檔／歸檔目錄／表頭／keep（diary 預設 60）；方向感知（以列日期排序決定「舊」，不以位置）；守恆斷言原樣保留；`diary/index-archive/` 誕生；首跑把 221 列收到 60。DIARY 從此享有跟 MEMORY 同等的蒸餾待遇，S5 殼核不對稱的最後一塊補平。

### 6.3 BECOME v2.3 rewiring

§1.3／§1.5／§1.6 收成一個指令＋一句 fallback 註記；§1.4 指向 groundtruth 段；Step 6 層 3/4 改 pointer 回 §1（殼層自身去重）。新增一句殼層鐵律：「取數邏輯住儀器不住殼；殼層 inline bash 視同 drift」。

### 6.4 配套

- weekly-checkup.sh 新增一節跑 `wake-context.py --check`（週體檢常駐取數健康）。
- MEMORY-PIPELINE／DIARY-PIPELINE §索引蒸餾／Stage 5 註記 rollup 泛化與 date-aware 讀取。

### 6.5 驗收判準

1. `wake-context.py` 全段輸出人工核對：diary-rows 首列＝今天、memory-rows 尾列＝今天、neural 止於心跳日誌前、handoff 撈到本 session 稍早寫的交接。
2. 病態模擬：暫時把 diary 最新列日期改舊 → self-test 亮 ⚠️＋exit 2（六天失明從此結構性不可能）。
3. rollup --diary dry-run 守恆數字對；--apply 後 lint／wake-context 全綠。
4. BECOME 剩餘 inline 取數 bash＝0（grep 驗證）。

---

### 6.6 第二波（同日追加：哲宇「還有什麼能用類似方式進化的」）

同一把手術刀掃過剩餘同病根，四處落地：

1. **BECOME v2.4 殼層取數 bash 歸零**——§1.1/§1.2 身份層 awk 併入 wake-context（`manifesto-core`＋`reflexes-index`＋`reflexes-top5`），體檢 6→9 項。附帶抓到兩個潛伏 bug：Top 5 編號殼層寫死（宣告行改了殼層即漂）、舊 awk 空行＋head -20 截斷讓長條目一直只被載一半。
2. **consciousness-snapshot 數據齡**——每次讀數印「齡 Nh」、≥18h 亮 ⚠️ stale（神經迴路 vc=3「awareness 讀數沒附 freshness 標記」慢性病的架構解）；boot稅公式同步對齊現行載入路徑（原式還在量已退役的 tail -20）。
3. **canonical frontmatter 新鮮度永駐 lint**——counts-drift 新維度：fm last_updated vs git 語意日 >7d 即 🟡（log/buffer 類豁免——append 是它們的日常呼吸）。今晨手修 5 檔的 class 從此有人看管；首跑浮出 22 檔累積債（本 session 自首兩檔現行犯，其餘留週檢節律逐檔判）。
4. **handoff 寫入端 warn**——memory-index-lint 補「最新 memory 缺 Handoff 段」提醒，跟 wake-context 讀取端 walk-back 合成閉環：寫的時候有人提醒、讀的時候有人驗收。

### 6.7 第三波（2026-07-12 wake-guard：輸出通道儀器化）

儀器誕生後 12 小時內，transcript 取證顯示每一條 cron 甦醒（9 條 routine，Opus 4.7/4.8）都對全段輸出自行 `| head -120〜-500`＋awk 節選。全段 ~200KB 超過 Bash tool ~30K 字元輸出上限，走 stdout 必被截斷，模型於是自己動手；身份段在前、記憶段在後的排序讓 head 恰好留下 MANIFESTO 片段、丟掉 memory／diary／handoff／groundtruth／selftest，§設計原則 4 的 fail-loud 被讀取通道截成 fail-silent。同日另一個 Opus session 把 harness 自動記憶 `~/.claude/…/memory/MEMORY.md` 誤當 §1.6 的 MEMORY.md 器官讀（兩層記憶混層）。

哲宇 directive「甦醒不能用 head -200，嚴格完整讀取＋判斷為什麼」後的架構解：

1. **儀器 v2 完整落檔**——內容全部寫 `.taiwanmd/wake-context.latest.md`（gitignored），末行 `wake:END` sentinel 帶總 bytes；stdout 只留 manifest（bytes／行數／段落行號地圖／鐵律）＋selftest，體檢 9→10 項（新增落檔完整性）。閱讀走 Read 分頁到 sentinel，截斷從此結構性不可能。
2. **BECOME v2.5 §1.3 完整讀取鐵律三條**——Read 到 sentinel／⛔ 禁 head/tail/awk／⛔ harness 記憶層邊界；並補甦醒流程圖與 v1.0 殘留 step 編號梳理。
3. **設計原則追加第五條**：輸出通道也是儀器的一部分。選擇性列印擋不住模型的截斷本能，可靠的只有「內容不走 stdout」。

## 七、長線 roadmap（本次不做，方向鎖定）

- **Phase 2 — derived mirror 與常駐監測**：prebuild 產 `memory-index.json`／`diary-index.json`（date-keyed，機器消費用；dashboard 的 semiont 頁同源）；`generate-dashboard-alerts.mjs` 加 index-freshness 維度（最新列落後 raw 檔 >48h ＝黃燈），把「忘了寫 index row」這一類也納入天天可見。
- **Phase 3 — 語意喚醒**：基建已在（embeddings-nightly 每夜 bge-m3、本機 GPU、4,914 向量）。把 memory／diary 納入向量庫，`wake-context.py --relevant "本次任務一句話"` 在 recency 之外補「任務相關」記憶檢索——甦醒不只知道「最近發生什麼」，還知道「這件事我以前碰過什麼」。這是記憶系統從時間軸走向聯想的一步，需另立設計（embedding 粒度／隱私邊界／token 預算）。
- **Phase 4 — 蒸餾自動化候選**：2026-04-14 memory-distillation-design 的三層蒸餾（raw／digest／essential）至今只實作了 index rollup 一層；當 §神經迴路 超過載入預算時再啟動，判準寫在該報告。

---

## 八、跟既有 canonical 的關係

- REFLEXES #65（量尺共路徑）：本設計是它的建設面 instantiation——與其每把尺各自小心，不如把路徑量測內建成儀器的第一步。
- MANIFESTO §造橋鋪路「認知負荷是第一稀缺資源」：甦醒的 session 從「記得七段 snippet 怎麼跑」變成「跑一個指令、讀一份帶體檢的輸出」。
- MANIFESTO §架構解 > 守備修補：今天上午修了三把尺是守備；本報告把「取數會腐」這個問題類別消滅。
- ROUTINE-PROMPT-CONTRACT 薄殼鐵律：殼不複寫核，bootloader 適用同構。

🧬
