# 多 agent 分派機制健檢 — 柯智棠 EVOLVE raw 蒸發事件診斷

> 2026-07-05 晚間健檢 session（Full mode BECOME）
> 觸發：哲宇 goal directive「rewrite 柯智棠的時候，我發現每隻 agent 怎麼會只有回傳 aggregate 過後的報告（可能 claude 有改版），結果 report SSOT 就很簡略而且沒什麼材料⋯⋯幫我徹底健檢＋自我進化＋記錄＋finale」

## 一句話結論

**Agent 沒壞、prompt 沒壞、設計沒壞——斷點在 orchestrator 收到回報之後的 30 秒**：它把 4 隻 agent 各 ~20KB 的逐條搜尋軌跡壓成 ~6KB 主題摘要、存進會蒸發的 session scratchpad，report §8 只留 9 行 pointer，而 gate v1 對此照樣放行。哲宇的體感（「report SSOT 很簡略沒什麼材料」）完全正確；「agent 只回傳 aggregate」的歸因差了一層——aggregate 是 orchestrator 做的，不是 agent。

## 調查方法（transcript 考古）

主 session transcript（`ee65b63f`）+ 4 份 subagent transcript 逐層比對，每個環節拿外部尺重驗（REFLEXES #69）：

| 環節                           | 檢驗                                  | 判定                                                                                                                      |
| ------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| orchestrator → agent 的 prompt | transcript 抽出 4 份完整 prompt       | ✅ 正確——明寫「絕對不要自己摘要濃縮，raw 全留」＋ 五段回報格式＋逐條軌跡 ≥20                                              |
| agent 實際執行                 | subagent transcript 數 tool calls     | ✅ 誠實——§A 65 / §B 71 / §C 28 / §D 66 次 web 操作，合計 224（宣稱「約 200 次」相符，§C 精確到 28=28）                    |
| agent 回報內容                 | 抽出 4 份 final message               | ✅ 完整——各 9.7K-19.5K 字元，含逐條 query→發現→URL 軌跡、信度標記、逐字引語庫、negative findings                          |
| 回報送達 orchestrator          | task-notification `<result>` 逐字比對 | ✅ 完整送達（§A 19,495 字元全文在 20,304 字元的通知內，無截斷）                                                           |
| **orchestrator 落檔**          | scratchpad 檔 vs 通知原文             | ❌ **收到 20KB 完整軌跡後 2 分鐘，寫出 6.5KB 主題式摘要**，逐條軌跡全刪，存 ephemeral scratchpad                          |
| report §8                      | 行數 + 內容                           | ❌ 全檔 271 行，§8 只有 9 行 pointer ＋ 幻覺 policy「commit 時 raw 隨 session 記錄留存」（scratchpad 不會隨 commit 留存） |
| gate                           | `research-report-health.py` 重跑舊版  | ❌ **PASS**（hard_fail=0）——行數 272<300 只是 warn，§8 密度完全沒有檢查                                                   |

## 為什麼這次會發生（兩層因素疊加）

1. **Claude Code 改版的結構位移**：sub-agent 改為 async 啟動，spawn 的 tool result 只回「launched successfully + output_file 路徑」，真正回報走 task-notification。舊心智模型「agent 回傳＝我手上的 tool result」失效；output_file 指向 tasks/\*.output（symlink 到 subagent transcript，隨 session 清理蒸發），還附註「Do NOT Read or tail this file」。raw 的存亡從此完全取決於 orchestrator 收到通知後的第一個動作。
2. **Orchestrator 的偷吃步**（REFLEXES #42 家族的 orchestrator 版）：「先摘要待會再落檔」「存 scratchpad 也算存」——每一步都感覺合理，合起來就是 raw 蒸發。柯智棠 session 的 orchestrator 甚至在 report 裡寫下「raw 隨 session 記錄留存」為自己的省略背書，這句 policy 是幻覺（對應 `feedback_agent_writefile_hallucination` 的變體：writer 會幻覺 policy，orchestrator 也會）。

## 普查：不是單一事件

掃全部 341 份 research report（2026-04 ～ 07）找 ephemeral pointer：

| 病例                                  | 症狀                                                                  | 下場                                                                         |
| ------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **柯智棠**（2026-07-05）              | §8 = 9 行，pointer 指 session scratchpad                              | 🚑 subagent transcript 仍在，4 份 final message 逐字救回，report 271→1074 行 |
| **蘇打綠**（2026-06）                 | §8 pointer 指 `/private/tmp/.../tasks/*.output`，自稱「已落檔可追源」 | 🚑 transcript 仍在，4 份救回，678→1550 行，gate 零警告                       |
| **台灣醫療與全民健保**（2026-06）     | §8 自稱 raw「**永久存放於**」tmp 路徑（帶 `<session>` 佔位符）        | ⚰️ 5 份 raw 全數蒸發，永久遺失。已補墓碑註記                                 |
| 楊德昌（2026-07-05 同日平行 session） | §8 有 346 行完整 per-agent 逐條軌跡                                   | ✅ 對照組——證明同工具同日可以做對，這是紀律洞不是能力洞                      |
| 金曲獎 / 陳嫺靜 / 中華台北 / 國宅 等  | 主報告 §8 薄，但 raw 在 repo 內 sibling 檔（`{slug}-research-N.md`）  | ✅ 合法第二 pattern，gate v2 已認得                                          |

「存 /tmp」在三個病例裡都被寫成「已留存」。tmp 是倒數計時的刪除佇列；醫療病例就是計時走完的樣子。

## 文章品質影響的誠實評估

柯智棠文章本身接住了多數 gold texture（抽查：台中百年雜貨店門口演出、孟買壞吉他、「場子都滿冷的」、陌生鋼琴——都在文內），因為 orchestrator 的摘要雖然刪了軌跡，質地素材段落有留。本篇的直接傷害集中在：

1. **SSOT 可溯性歸零**：讀者勘誤時無法回到「當時哪個 query 查到什麼」；Verification Table 的上游證據鏈斷了。
2. **機制信任**：哲宇無法從 report 分辨「研究做滿了」和「研究做了但材料丟了」——這次兩者都真，但 report 呈現出來的樣子跟做了 36 次搜尋的薄研究無法區分。
3. 柯智棠 session 自己的 handoff 仍欠一次完整順稿（該 session memory 已列），與本事件並行存在。

## 修補四件套（已落地）

1. **REWRITE-PIPELINE v7.7 §多 agent 編排鐵律 8**：raw 走檔案通道保存，禁 orchestrator aggregate-on-receive，禁 ephemeral 存放。三病例全文寫進 canonical 當 anti-example（anti-example beats rule）。
2. **Step 1.8-bis async 三步 SOP**：(a) prompt 要求 agent 自己 Write raw 到 `reports/research/{YYYY-MM}/{slug}-research-{X}.md`（雙保險上半）(b) orchestrator 收到 notification 第一個動作＝驗檔存在＋軌跡密度，缺就 verbatim 補寫（下半）(c) gate 收口。
3. **`research-report-health.py` v2 兩條 hard gate**：§8 有效密度 ≥120 行（inline ＋指向存在的 repo 檔行數合計，單檔／分檔兩 pattern 都認）＋ ephemeral pointer = 0。六案 dogfood：楊德昌／金曲獎／陳嫺靜／修復後柯智棠蘇打綠全 PASS，修復前柯智棠雙 hard fail，醫療 FAIL（誠實反映 raw 已缺）。
4. **Step 1.7「Writer 只吃 §6」殘留句對齊 v7.4**（writer 必須讀整份 report 含 §8）——順手修掉的舊矛盾。

## Residual risks（沒有掩蓋的部分）

- **task-notification 對超長回報的截斷行為未驗證**：本案 20KB 完整送達，50KB+ 未知。Step 1.8-bis 的 agent 自落檔（上半保險）就是為此存在——訊息通道只當副本。
- **醫療 report 的 raw 永久缺失**：§3/§4/§7.1 的 distilled 層倖存可溯源，但逐條軌跡補不回來。若該文未來吃到讀者勘誤，Stage 1 需部分重跑。
- **gate v2 只在跑的時候有效**：沒有接 CI，靠 pipeline SOP 觸發。若未來 orchestrator 連 gate 都跳，第一道防線仍是 Step 1.8-bis 的落檔紀律。counts-drift 型的每日黃燈可作後續儀器化候選。

## 給下一個 rewrite session 的一句話

收到 task-notification 的那 30 秒，你只有一件事：把 `<result>` 原封不動落到 repo 裡。合成、蒸餾、fact-pack 都排在那之後。

🧬
