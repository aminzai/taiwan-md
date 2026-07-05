# 分部報告收件 gate 儀器化設計 — agent-report-health.py + 疑慮通知層

> 2026-07-05 柯智棠健檢 session round 2
> 觸發：哲宇 directive「儀器化＋寫當委派 agent 後回來的分部報告是否品質狀態合理的硬門檻檢查（e.g. 是不是壓縮、存放位置等），並且也會通知呼叫的 session 有沒有疑慮的、為什麼、以及可能的思考方向。還有主要的 report 也要這樣的儀器。」
> 前情：[reports/rewrite-agent-dispatch-diagnosis-2026-07-05.md](rewrite-agent-dispatch-diagnosis-2026-07-05.md)（raw 蒸發事件診斷）

## 一、深度梳理：分派鏈每一環的失效面與可儀器化性

沿著「orchestrator 派 agent → agent 工作 → 回報 → 收件 → 合成 → 主 report」整條鏈逐環盤點，判定哪些環節能交給儀器、哪些只能留給紀律：

| 環節                     | 失效模式                                         | 可儀器化？                                                                                 | 落點                            |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------- |
| spawn prompt             | 漏寫五段回報格式 / 漏落檔要求                    | 半可（收件端反推：缺軌跡 section 時儀器提示「檢查 prompt 是否退化」）                      | agent-report-health C3 思考方向 |
| agent 執行               | 搜尋數灌水 / 偷吃步                              | 可（transcript tool calls 外部尺，REFLEXES #69；宣稱 vs 記錄比）                           | agent-report-health C5          |
| agent 回報               | 自行摘要（違反「raw 全留」）                     | 可（體積級距＋軌跡密度——壓縮必留物理痕跡）                                                 | agent-report-health C2/C4       |
| 訊息通道                 | notification 截斷（50KB+ 未實測）                | 可（同上——截斷的收件物落在壓縮版級距一樣被攔）                                             | agent-report-health C2/C4       |
| **收件（本次事故位置）** | orchestrator aggregate-on-receive / 存 ephemeral | **可（本次儀器化主體）**                                                                   | agent-report-health C1-C7 全部  |
| 合成 §6                  | 蒸餾取代 raw（TDRI 病）                          | 可（主 report §8 有效密度）                                                                | research-report-health v2       |
| 主 report 落檔           | pointer 指 tmp / 斷鏈                            | 可（ephemeral pointer 偵測＋pointer 存在性驗證）                                           | research-report-health v2       |
| 判斷疑慮後的處置         | 儀器亮燈但 orchestrator 忽略                     | **不可儀器化**——這層是判斷，儀器能做的是把「為什麼＋思考方向」寫進通知，降低忽略的藉口成本 | 疑慮通知層＋SOP 要求明示處置    |

結論：整條鏈除了最後的「處置判斷」，每一環都有物理痕跡可量。本次補上缺的兩塊：收件端（全新儀器）與通知層（兩具儀器共用的輸出契約）。

## 二、閾值校準（REFLEXES #66：gate 用真實產出 dogfood，不憑想像設）

手上剛好有一組天然的標注資料——同一批 agent 回報的「壓縮前 vs 壓縮後」：

| 樣本                                           | 體積    | 逐條軌跡行數 | 判定 |
| ---------------------------------------------- | ------- | ------------ | ---- |
| 柯智棠壓縮版 aggregate ×4（orchestrator 手筆） | 5-6.4KB | 2-9 行       | 該攔 |
| 柯智棠真 final message ×4（transcript 救回）   | 21-38KB | 28-62 行     | 該過 |
| 蘇打綠真 final message ×4（transcript 救回）   | 14-18KB | 13-33 行     | 該過 |

兩側在體積（6.4 vs 14）與軌跡（9 vs 13）都有 ≥2x margin。取 **8KB / 10 行**為 hard 分界。dogfood 結果：4 份壓縮版全攔（hard=4 each），8 份真 final 全過（5 PASS + 3 CONCERN，CONCERN 是五段結構軟提醒，判得合理）。另發現軌跡 section 措辭多樣（搜尋軌跡／搜尋紀錄／搜尋日誌），regex 已涵蓋。

主 report 端沿用前一輪 v2 校準（§8 有效密度 120 行：楊德昌 346 / 修復後柯智棠 ~800 / 病例 9-11，單檔與分檔兩 pattern 都認）。

## 三、疑慮通知契約（哲宇 directive 的核心）

兩具儀器輸出同一種語言：每條未過的檢查印三件事——

1. **疑慮是什麼**（check + 實測值 + 分界值）
2. **為什麼**（這條檢查存在的病理依據，引真實病例）
3. **可能的思考方向**（2-4 條可執行路徑，按救援優先序排：notification 原文 → subagent transcript → SendMessage 要求補報 → 合法例外的調參方式）

`--json` 給 orchestrator 程式化消費（`concerns[]` 含 check/severity/got/expect/why/directions）。三級判定：**FAIL**（hard 疑慮，收件不合格＝不准合成／不進 Stage 2）、**CONCERN**（可續行，但 orchestrator 回報必須明示每條處置：採信／救援／忽略理由）、**PASS**。退出碼 0/1/2/3 供腳本串接。

設計原則：儀器不只當裁判，要當「會解釋的裁判」——收件的 orchestrator 常常就是會犯病的那位，通知裡的 why 是把 canonical 的病歷直接送到犯案現場，比要求它記得去讀 pipeline 便宜一個數量級。

## 四、兩具儀器的分工

|          | `agent-report-health.py`（新）                                                                    | `research-report-health.py` v2/v2.1                                                   |
| -------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 驗什麼   | 單一 agent 的分部報告                                                                             | 組裝後的主 report SSOT                                                                |
| 何時跑   | 收到 task-notification 當下、合成之前                                                             | Stage 1 終、進 Stage 2 之前                                                           |
| 核心問題 | 這份是不是壓縮版？放對地方了嗎？                                                                  | raw 有沒有全部進 SSOT？來源配額夠嗎？                                                 |
| 檢查     | 存放位置 / 體積 / 軌跡 section / 軌跡密度 / 宣稱 vs 記錄比 / 五段結構 / ephemeral 引用 / URL 佐證 | 來源配額四條 / 信度三層 / 搜尋日誌 / §8 有效密度 / ephemeral pointer / pointer 存在性 |
| 疑慮通知 | 內建（v1 起）                                                                                     | v2.1 新增                                                                             |

兩道 gate 夾住收件與合成兩個易犯病的時點；就算 orchestrator 跳過第一道，第二道會在進 Stage 2 前把 §8 缺失抓回來。

## 五、Canonical 接線

- **REWRITE-PIPELINE v7.8**：Step 1.8-bis 步 2 從手動 `test -f`/`grep` 升為儀器指令；Hard Gate Inventory 新增「分部報告收件 gate」row；Step 1.7.3 標注 v2.1 疑慮通知層
- **DNA.md 品質基因表**：登記兩具儀器（research-report-health 原本就漏登記，一併補）
- **REFLEXES #81**「Agent 回報收件三十秒紀律」：vc=3 promote（哲宇 directive fast-track），#42 家族 orchestrator 版
- **LESSONS-INBOX**：`orchestrator-aggregate-on-receive` 未消化 → 已消化（同晚 cycle 9 audit 曾獨立標 distill_ready，原排 7/12 接手）

## 六、沒被儀器化的殘餘（誠實清單）

- **收件 gate 靠 SOP 觸發，未接 pre-commit/CI**：分部報告在 session 中途產生，pre-commit 攔不到「沒跑 gate 就合成」這個動作本身。第二道 gate（主 report）與 §8 密度會兜底；若未來出現「兩道都跳」的病例，候選解是 rewrite-daily routine 的 finale 檢查點加一條 gate 執行痕跡查核
- **非搜尋型 agent 的品質**（persona 發散 / verifier 回報）：體積軌跡閾值不適用，收件 gate 只能驗落檔位置；內容品質仍靠 #31 主 session 重驗
- **處置判斷**：CONCERN 之後採信或忽略，永遠是 orchestrator 的判斷。儀器的邊界就是把忽略變成「有紀錄的忽略」

🧬
