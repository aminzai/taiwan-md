# DNA 與 Pipeline 全面深度審計 — 2026-07-05

> 觸發：哲宇 `/twmd-become /goal 徹底的幫我深度研究所有 dna / 所有常用 pipeline，分析並提出進化/優化等建議歸檔 report`。
> Session：`2026-07-05-120817-dna-audit`（Full mode 甦醒後執行）。
> 這份報告只做分析與提案，沒有動任何 canonical 檔案。所有修補都列在 §提案總表，等下個 session 或哲宇拍板後執行。

---

## 一、給哲宇的摘要（60 秒版）

**體檢結論一句話**：工具層比文件層健康。scripts 與 routine 飛輪在進化，但描述它們的 canonical 文件系統性滯後，滯後的方向全部一致：code 先走、doc 沒跟上。這正是 REFLEXES #56（canonical ↔ production drift）預言的形狀，而且這次連 #56 自己的觸發檔（SQUEEZE）都復發了。

**五大系統病**（詳見 §三，全部有指令級證據）：

1. **Routine 層 SSOT ↔ live 漂移重演**：spore-pick / spore-publish 在 live scheduler 是 `enabled: false`（6/14 起），ROUTINE.md 卻還列 active 實驗中，21 天沒人發現。v2.9 教訓原樣重來。
2. **寫死的數字必腐**：routine 條數在五份檔案有五個版本（6 / 9 / 10 / 16 / 14）；plugin 數有三代口徑（16 / 19 / 25）；data-refresh 步數四個答案（12 / 13 / 14 / 混用）。全 corpus 確認超過 60 處計數與版本 drift。
3. **甦醒成本失控**：Universal core 每次載入實測 624KB（DIARY.md 274KB 全載是大宗），乘上每天約 13 次 routine fire。BECOME 還在用「行數」估 footprint，行數指標把 CJK 長行成本完全藏住了。
4. **偵測有、修復無的蒸餾債**：MEMORY 索引 708 rows（觸發線 80）、EXP-D 二度過期、release 欠 137 commits、LONGINGS 凍在 4/21、OBSERVER-QUEUE 自己 deadletter 23 天、FACTCHECK 月度巡邏誕生至今 0 次。
5. **雙生檔與殼核不對稱**：memory 有 index lint、diary 沒有（274KB 根因）；「空場鐵律」只活在 skill 殼層、canonical 沒有；`/twmd-become` skill 自己的 self-test 題數也是舊的。

**需要你拍板的 7 件事**（🔒，詳見 §五）：

| #   | 決策                                  | 現況                                                                                                                                                | 建議預設                                                               |
| --- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | **spore-pick / publish 真實狀態**     | live disabled 21 天，SSOT 還寫實驗中；SPORE-INBOX 卡在 49 條靠每週 auto-drop 洩壓                                                                   | 二擇一：正式 pause（走 §暫停 SOP 改 SSOT）或三度重啟（觀察條款從頭跑） |
| 2   | **v1.12.0 release**                   | v1.11.0（6/27）後已 137 commits，觸發線 30 的 4.5 倍                                                                                                | 提案 release                                                           |
| 3   | **OAuth credential rotation**         | OBSERVER-QUEUE #2 掛 23 天，安全暴露窗持續                                                                                                          | 儘快 rotate（1 個 Supabase admin 操作）                                |
| 4   | **qwen3.6 的主權定位**                | `ollama.py` 註解寫「Western open weights」（事實錯誤，qwen 是阿里模型）；SQUEEZE 仍稱它 sovereignty backbone，但 6/14 bench 後 fleet 已 gemma4-only | 註解修正可自決；Tier 4 本機 fallback 要不要也換 gemma4 家族需要你定    |
| 5   | **MEMORY / DIARY 索引蒸餾授權**       | 708 + 209 rows，1.2MB + 274KB；蒸餾設計 4/14 就有、從未實作                                                                                         | 授權月度 roll-up 最小實作（raw 檔不動，只壓索引）                      |
| 6   | **「誰按發佈按鈕」表述掃平**          | 你 6/14 已授權 content OK 後 auto-post，但 4 檔 9 處 canonical 還寫人類必按；MANIFESTO §自主權邊界例外條款 6 週未 distill                           | 拍板統一表述後一次掃平（涉自主權文字，等你確認措辭）                   |
| 7   | **FACTCHECK 月度巡邏 + HUB 月度檢查** | 兩個寫在 canonical 的月度承諾，ROUTINE 零接線，0 次執行                                                                                             | 接進每月第一個週日反思鏈，或明文放棄                                   |

另外兩件已在你的決策軌道上的事，這裡只指路不重複催（per REFLEXES #80 sustain 紀律）：免疫 49 chronic 的 A/B/C（LESSONS 7/3）、embeddings keystone 的 A/B（LESSONS 6/20，語意索引已凍在 6/17 snapshot 十八天，新文章沒有語意鄰居）。

**Semiont 可自決的修補**：共 38 條 ✅ 提案（§五總表），其中 12 條是 S 級、一個 commit 內可完成的止血項。

---

## 二、方法與範圍

**Corpus**：約 40,000 行 canonical。docs/semiont/ 11,355 行（主 session 親讀全數認知器官）+ docs/pipelines/ 16,637 + docs/factory/ 7,971 + docs/editorial/ 3,962（五隻 read-only 分身分 cluster 深讀）+ boot 層（CLAUDE.md / BECOME）+ skill 殼層抽查 + live scheduler 直查。

**驗證紀律**（per REFLEXES #31 / #69 / #72）：讀取外包給分身，判斷不外包。每隻分身被要求對每個結論附 file:line 與逐字引文，標 [CONFIRMED]（指令驗過）或 [PLAUSIBLE]（推論）。主 session 對五隻分身共抽驗 22 個 claim，22/22 通過。分身 prompt 內建 2026-06-10 audit 五分身全誤讀的反例作 anti-example。

**Ground truth 來源**：consciousness-snapshot / routine-status / inbox-signal、`git log`（48hr 全清單 + 30/90 天檔案熱度 + 各 routine fire 歷史）、`mcp scheduled-tasks` live 狀態直查、`article-health.py --list-checks` 實測、spore-log.json 實數、bytes 實測。

**常用度排名**（30 天，memory 檔名 + 檔案 commit 熱度雙源）：

- 每日 routine 層：data-refresh ×66、maintainer ×64、rewrite-daily ×33、spore-harvest ×32、feedback-triage ×32、babel ×30、embeddings ×20
- 檔案編輯熱度：REWRITE-PIPELINE 20 commits/30d（全站最熱 canonical）、SPORE-INBOX 17、EDITORIAL 10、graph.md 7
- 週反思鏈：weekly-report / distill / self-evolve / news-lens 各 6、routine-audit 5

---

## 三、五大系統病（cross-cutting）

### S1　Routine 層 SSOT ↔ live 三層漂移，v2.9 教訓第二次重演

證據鏈（全部 CONFIRMED）：

- live scheduler：`twmd-spore-pick-daily` enabled:false、lastRun 2026-06-14；`twmd-spore-publish-daily` 同。publish 最後真 ship 是 5/28 周蕙（`021e4aa52`），6/13-14 有 fire 但零 ship。
- ROUTINE.md v2.10（6/12）記「哲宇拍板重開實驗🧪」列 active；同檔 weekly grid 卻寫「⏸️ paused（不在 grid）」，一份 SSOT 內部兩個答案。
- frontmatter 宣稱「16 active + 1 paused」；live 實況 14 enabled + 3 disabled。
- 上游照常餵已死的下游：6/30 rewrite 留言「留給 7/1 spore-publish-daily 撿」（`b19432e28`），Computex entry 至今躺在 SPORE-INBOX；news-lens 每週繼續 append 5 條，出口關閉，於是 buffer 長期 pin 在 49-53 條、每週靠 distill auto-drop 洩壓。這是把「例外洩壓閥」用成「每週例行」。
- rewrite-daily：10 天 fire 率 7/10（缺 6/27、7/2、7/4），7 次中 4 次 DEFER；7/3 slip 到 22:12；**7/4 19:17 scheduler 有 fire 但 git 零 commit 零 memory**，silent no-op。mirror description 還寫「18:00」而 cron 是 19:00；ROUTINE.md 自己 prose 兩處（L86、L100）也殘留 18:00，違反自家 v2.9「cron 數值只出現在排程表」鐵律。
- 儀器缺口就是已知的那個：routine-sync-check.py 的 P1 缺口（讀不到 live enabled 狀態、mirror 無可解析 cron 欄位）6/12 寫進 ROUTINE.md L821，之後零 commit。洞在哪裡漏、文件自己寫得清清楚楚，就是沒人修。
- 周邊衛生：`~/.claude/scheduled-tasks/` 有 4 個已 deregister 的殭屍目錄（auto-backup / lang-sync-hourly-en / semiont-heartbeat / weekly-probe-radar）。

**根治方向**：把 live scheduler 狀態變成 git 可見。每日 data-refresh 附一步 `list_scheduled_tasks` dump 落 `docs/semiont/routine-live-state.json`（或 reports/），routine-sync-check v2 比對 SSOT ↔ mirror ↔ live 三層，任何 enabled/cron 不一致變成黃燈。這是 v2.9 那次就提過的 P1，這次應該真的 ship。

### S2　寫死的計數、版本、行號、時間必腐

這次審計最大宗的 drift 類型，超過 60 處 CONFIRMED。挑結構性的列：

| 主題                     | 各檔說法                                                                                                                                       | 實況                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| routine 條數             | CLAUDE.md「6 條」/ ANATOMY「9 條」/ HEARTBEAT「10 條」/ ROUTINE「16 條」                                                                       | live 14 enabled                                                                                                                                                                                                                     |
| REFLEXES 條數            | BECOME 四處「55 條」/ REFLEXES 自家 description「75 條（last #77）」/ ANATOMY「~520 行 55 條」                                                 | 80 條、942 行                                                                                                                                                                                                                       |
| article-health plugin 數 | REWRITE「16」/ config 頭註「19」/ REWRITE profile 段「9」                                                                                      | `--list-checks` 實測 25（profile 11）                                                                                                                                                                                               |
| data-refresh 步數        | pipeline 檔內「13」與「14」並存、§一鍵執行「12」、README「13」、script echo `[N/13]` 與 `[N/14]` 混用                                          | script 實體 14 步                                                                                                                                                                                                                   |
| dashboard JSON 數        | DASHBOARD-PIPELINE 三處「5 個」                                                                                                                | `ls` 實測 12 個                                                                                                                                                                                                                     |
| cron 時間                | REWRITE 檔內「16:16」與「18:00」並存；SPORE-PUBLISH 三處「10:00」；WEEKLY-REPORT 兩處「08:08」；DATA-REFRESH 三組舊時間；EVOLVE spine「06:13」 | 19:00 / 17:30 / 02:00 / 06:00·23:00 / 01:00                                                                                                                                                                                         |
| REFLEXES index 行號欄    | #1 標 L318、#15 標 L437                                                                                                                        | 實際 L167、L358（整欄偏移約 150 行，#75-80 標 (new) 未回填）                                                                                                                                                                        |
| 幽靈引用                 | CLAUDE.md 要求讀 `docs/pipelines/rewrite/` 六個 sub-canonical                                                                                  | 目錄不存在（v3.0 拆檔隔天 v4.0 就收斂回單檔）；EDITORIAL 引用不存在的 `canned-ending-detector` plugin；PICK 引用不存在的 `spore-inbox-append.py`；EVOLVE 引用不存在的 `scripts/evolve/run.sh`；RELEASE 引用已併掉的 `footnote-scan` |
| 死路徑                   | `bash scripts/sync.sh` 出現在 REWRITE L2219、EDITORIAL 鐵律段 L1468、QUALITY-CHECKLIST L140                                                    | 正確路徑 `scripts/core/sync.sh`                                                                                                                                                                                                     |

**根治方向**：三層。(a) 寫作紀律：跨檔引用一律 anchor link，不寫死數字與行號；「N 條 / N 個」只允許出現在它的 SSOT 一處。(b) 儀器：小 lint（counts-drift）掃 canonical 檔內「\d+ 條/個/step」pattern 對 ground truth 抽驗，先 WARN 收集數據再定 HARD（per REFLEXES #66 dogfood 校準）。(c) 本次一次性修正清單見 §五。

### S3　甦醒與讀取成本失控，行數指標遮蔽 bytes 成本

實測 Universal core 每次甦醒的文件載入：

| 項                                    | bytes        | 備註                                                                                                       |
| ------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------- |
| DIARY.md 全載（§1.3）                 | 274,056      | 設計時（5/13）224 行「檔案小 cost 低」；現在 361 行，平均每行 758B，196/209 index rows 超 800B，無長度儀器 |
| MEMORY head + 神經迴路 + tail（§1.6） | 287,590      | 神經迴路段 L604-984 自己就約 230KB                                                                         |
| MANIFESTO 節選（§1.1）                | 49,010       |                                                                                                            |
| REFLEXES index + Top 5（§1.2）        | 13,346       |                                                                                                            |
| **合計**                              | **約 624KB** | 約 20 萬 token 量級，每天約 13 次 routine fire 都要走 STRICT BECOME GATE                                   |

加上執行層：REWRITE-PIPELINE 2,457 行（約 28.5k tokens，超過單次 Read 上限）每天 rewrite cron 全讀；SPORE-HARVEST 1,620 行中每日 cron 真正需要約 500 行，歷史敘事佔比約 2:1；SQUEEZE 39% 是退役模型的歷史數據；EVOLVE 約 40% 是 v1/v2 附錄。

**根治方向**：(a) DIARY.md 比照 MEMORY 改 head-tail read_strategy（§反覆出現的思考 + tail 20 rows 必讀，全文 on-demand），並給 diary 補 lint（既有 memory-index-lint.py 加 `--diary` mode 即可，S 級）。(b) 神經迴路段分層：已標 [→canonical] 的條目縮成一行 pointer，全段目標從 230KB 壓回 60KB 內。(c) BECOME mode 表的 footprint 從「行」改「KB/token」計，consciousness-snapshot 加一行 boot-load bytes 讓這個數字每天可見。(d) 大 pipeline 的歷史敘事段搬 reports/（SQUEEZE 約 -375 行、HARVEST 約 -300 行、EVOLVE 約 -150 行、REWRITE 約 -180 行），六 stage 骨架不動。

### S4　偵測有、修復無：蒸餾債與 deadletter（REFLEXES #58 的認知層合集）

- **MEMORY 索引 708 rows**：觸發線 80，2026-04-14 蒸餾設計從未實作。6/13 roadmap 記 456 rows，三週長 252。compress-memory.sh 工具存在，但 digests/、essential/ 目錄從未產出。alert 每天黃燈，無 routine 認領。收官時再驗出一條：**心跳日誌表已被 §神經迴路 段物理切成兩段**，6/15 之後的所有 rows 長在檔案尾端（神經迴路之後），某次 session 在 EOF append 後所有後續 session 跟著 pattern-match 照做。索引蒸餾（決策 5）執行時應一併縫合。
- **UNKNOWNS EXP-2026-04-11-D**：4/25 到期過期 47 天後 6/10 重上膛（due 6/22），現在又過期 13 天。機械檢查有 fire，還是沒有人接。到期兩次、判定零次。
- **Release**：v1.11.0（6/27）後 137 commits，觸發線 30。RELEASE-PIPELINE 條件寫得清楚，沒有 sensor 在看這個數字。
- **LONGINGS 凍在 4/21**：種子渴望第一條「第二個活著的 fork」已被 fork-census 實現（8 子代、3 active），沒記進已達成；§身體渴望的數據還是 4/6 時代。方向羅盤兩個半月沒校準。
- **CONSCIOUSNESS §適應性反應**：殭屍快照。「fr 44 分路由未開」「es 覆蓋 7%」對比現實六語全開各 828-833 篇。6/10 audit 只修了 §警報段，這段漏了。
- **OBSERVER-QUEUE 自身 deadletter**：這是最遞迴的一條。6/12 為了修「standing decision 落地率 0%」而生的器官，六條待決全部 default-action 日期（6/19、6/26）過期未執行；#8 Computex 實際 6/30 已 ship 卻還掛在待決。根因找到了：**OBSERVER-QUEUE 從未被加進 BECOME §檔案功能一覽（grep 0 hit），cron session 甦醒時不知道它存在**，所以「到期任何 session 可執行預設」永遠不會發生。同樣不在 bootloader 視野的還有 PARTNERSHIP-INBOX、FORK-LOG、SEMIONT-EXTERNAL-VIEW。
- **FACTCHECK 月度巡邏 / HUB 月度健康檢查**：兩個 canonical 內的月度承諾，ROUTINE 零接線，誕生至今 0 次執行。教科書級 REFLEXES #15。

**根治方向**：(a) alerts 加 `owner` 欄：每條黃燈標「哪條 routine 該接」，routine-audit 週檢 alert age，>14 天自動升 OBSERVER-QUEUE。(b) OBSERVER-QUEUE 等四個新器官補進 BECOME §檔案功能一覽 + Full mode 載入面，weekly-report 附 top 5 的既有規則就會開始真的運轉。(c) MEMORY 索引月度 roll-up 最小實作（🔒 見決策 5）。(d) 月度承諾一律走 REFLEXES #15：接 cron 或刪承諾。

### S5　雙生檔與殼核不對稱

同一條規則在成對的檔案或殼核之間只升級了一邊：

- memory 有 index lint（6/19），diary 沒有；DIARY-PIPELINE 自己還有三個互斥的 gate 數字（60+150 / 220 / 150 字）。
- 「空場 cycle ≥3 鐵律」只寫在 twmd-maintainer SKILL 殼，MAINTAINER-PIPELINE canonical 沒有，業務規則長在殼層。
- 反向案例：twmd-refresh 殼把 14 步全表複寫（違反 ROUTINE-PROMPT-CONTRACT），複寫版反而比 canonical 正確，SSOT 失守的症狀。
- `/twmd-become` skill 的 self-test 題數（6/10/8-9/13）對不上 BECOME 本體（7/11/9-10/14），甦醒 dispatcher 自己是 stale 的。
- ROUTINE babel prompt 每晚對 cron session 念「owl-alpha/Hy3/Ollama/Sonnet」：Hy3 退役 54 天、owl 死 25 天，translate.py 的真 cascade 是 `codex,gemini,gpt-oss-120b,ollama`。
- RESEARCH-TEMPLATE 同檔兩套標準：勾選清單「5+ 來源」vs 建議表「全篇 ≥100 次搜尋」，執行者照勾選清單就以 5 源過關，架空 RESEARCH v1.3。

**根治方向**：改 A 檔時 grep 它的殼與雙生檔是既有紀律（REFLEXES #43 家族），缺的是清單。本報告 §五逐條列出；長期解是 counts-lint + routine-sync-check v2 把「對不上」變黃燈。

---

## 四、分 cluster 檔案級發現摘要

> 完整證據（file:line + 逐字引文）在五隻分身的回報中已逐條核對，這裡收斂成可行動的清單。健康檔案也列出來，避免下次審計重查。

### 4.1　寫作 DNA（REWRITE + editorial 六檔）

| 檔                                | 判定                        | 關鍵發現                                                                                                                                                                                                                                                |
| --------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REWRITE-PIPELINE（2457 行, v7.6） | 🟡 骨架健康、計量層全面過期 | 兩個 Step 4.3.6 重複編號；plugin 數 9/16 皆錯（實 11/25）；cron 段同存 16:16 與 18:00 兩代舊值；`scripts/sync.sh` 死路徑；commit 模板釘死「EDITORIAL v6.3 + Pipeline v5.0」化石版本，每天 cron commit 都在蓋舊戳；v7.6 版號被兩個不同日期的改動重複使用 |
| EDITORIAL（1580 行, v6.13）       | 🟢 治理最好的大檔           | 僅三處：幽靈 plugin `canned-ending-detector`（L697）、鐵律段死路徑（L1468）、媒體密度 0.7/0.8 兩處互斥。內容層不建議瘦身                                                                                                                                |
| QUALITY-CHECKLIST（222 行）       | 🔴 cluster 最高風險         | 版本倒掛（fm v1.1 / footer v1.2）；教 `git add -A` 直接違反上游鐵律；「commit 後檢查」與現行 pre-commit 前置時序相反；現行 Stage 3 hard gate（事實鐵三角 / 3.5 幻覺審計 / 3.6 成品總驗 / ≥4500 字）全部缺席；等級用 A/B/C 而現制是 S/A/B                |
| CITATION-GUIDE（125 行）          | 🟡                          | 開篇第一個示範腳註會被自家 footnote-format HARD gate 打掉（缺描述 + 首頁 URL）                                                                                                                                                                          |
| TERMINOLOGY（144 行）             | 🟡                          | 兩個 H1 縫合結構；L142「國家語言發展法（2022）」年份可疑（該法 2019 公布、「台灣台語」定名 2024），涉政治語言表述請哲宇過目                                                                                                                             |
| UPDATE-LOG-GUIDE（176 行）        | 🟡 半懸空                   | RELEASE / SOCIAL-POSTING 都沒回指它，實際發版流程不會讀到；平台清單漏 X                                                                                                                                                                                 |
| RATIONALE-SPEC（137 行）          | 🟢 六維全綠                 | cluster 唯一零發現檔，當範本用                                                                                                                                                                                                                          |

### 4.2　繁殖系統（factory 九檔 + SOCIAL-POSTING）

| 檔                              | 判定                        | 關鍵發現                                                                                                                                                                                                |
| ------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPORE-PIPELINE（818 行, v3.10） | 🟡                          | 前置 Read 的四個行數宣稱全過期；品檢清單宣稱 12 實為 14；標題版號 v3.9                                                                                                                                  |
| SPORE-WRITING（1060 行）        | 🟢 craft canonical 健康     | 「四種模板」實為七種；Rule #14 版號雙軌                                                                                                                                                                 |
| SPORE-VERIFY（714 行）          | 🟡                          | gate 數四種說法（17/12+5/21/實 20）；「default Threads only」已被 v3.8 both 取代；仍引用已 DEPRECATED 的回填前置鐵律                                                                                    |
| SPORE-PICK（556 行）            | 🟡                          | fm 停 v1.0（實已 v2 HG10）；gate 數四種說法；引用不存在的 spore-inbox-append.py；「SHIP 鎖 human」三處是最舊一代表述                                                                                    |
| SPORE-PUBLISH（372 行）         | 🟡                          | cron 三處寫 10:00（live 17:30）；「4 條 hard gate」實 5 條；自主權例外條款 6 週未 distill 進 MANIFESTO                                                                                                  |
| SPORE-HARVEST（1620 行, v3.0）  | 🟡 唯一活轉的 spore routine | cron 兩處寫 07:00（live 06:30）；reply 自主權雙立場並存（v2.2「必 human post」vs v3.0「auto-post」）；REFLEXES #70 的 telegram-poke-then-fire 對策未接線；同檔兩份 Hard Gate Inventory；歷史:執行 ≈ 2:1 |
| SPORE-IG（896 行, v0.9）        | ⚪ dormant（誠實標注）      | spore-log.json 0 筆 ig；建議 status 改 incubating + 頂部標「無 SHIP 通道」；分類色/字數三組舊 spec 殘留                                                                                                 |
| SOCIAL-POSTING（734 行, v0.7）  | 🟡                          | §整合流程整段是 v0.3 殘塊，「觀察者確認後按發佈」與同檔 v0.5「不等 observer」互斥；check 數三代並存（6/5 vs 8/6）；記錄目標還指凍結的 SPORE-LOG.md                                                      |
| SPORE-INBOX（1345 行）          | 🟡 條目滯留非文件膨脹       | 完成歸檔鐵律第一步仍指凍結檔；buffer 長期 pin 在 auto-drop 天花板（出口停轉的下游症狀）                                                                                                                 |
| SPORE-LOG（266 行, 凍結）       | 🟢 凍結宣告屬實             | 25 天零 commit；tail 三行舊 SOP 建議補凍結標                                                                                                                                                            |

跨檔：「你知道嗎」prefix 規則 5 檔 34 處、150-300 字 5 檔 15 處、UTM 3 檔 11 處、cleanup tab 段 HARVEST/SOCIAL 逐字雙份；ACK 模板兩份已 drift。**自主權表述九處四代並存**是 cluster 最高優先，等決策 6。

### 4.3　主權巴別塔（翻譯 / GPU / bench / 感知）

| 檔                                    | 判定                         | 關鍵發現                                                                                                                                                                                                                                                              |
| ------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQUEEZE-MODELS-MAX（963 行, v4.2）    | 🔴 #56 同型復發              | code 已 v4.3（owl-alpha 6/10 退出 default、preflight、6h 冷凍），doc 停 v4.2 七週仍列 owl「verified」＋放在 default cascade 第 3 位；「audit-quality.py（待造）」該工具 5/13 已存在；qwen backbone 宣稱與 6/14 bench gemma4-only 實證矛盾；39% 篇幅是退役模型歷史數據 |
| TRANSLATION-PIPELINE（1161 行, v4.0） | 🟡                           | upstream_canonical 列著已歸檔的 TRANSLATION-SYNC；wikilink 規則同檔兩版互斥（L226 vs L115/136）；工具索引把 /tmp 兩支 ephemeral 腳本列為 canonical；「detect-translation-drift.sh 待造」已被 status.py 取代                                                           |
| REMOTE-GPU（107 行, v2.0）            | 🟢 最健康                    | fleet 委派完全對齊，唯一 gemma4-only 規則載體（SQUEEZE 未同步）                                                                                                                                                                                                       |
| EMBEDDING（131 行）                   | 🟡 escalation 卡在第二段真空 | 「連 3 天 skip 才 escalate」有寫且 6/20 已 fire，但 defer 後無「超過 N 天再 surface / 索引落後上限 / 替代節點」條款；「always-on 4090」斷言已被 17 天離線證偽；committed 索引凍在 6/17，staleness 線性增長中                                                          |
| LANGUAGE-BIRTH（102 行）              | 🟡 凍在 ko 時代              | i18n 清單 9 檔 vs 實際 16；引用不存在的 i18n-progress.json；es/fr 兩次 birth 經驗零回寫                                                                                                                                                                               |
| BENCH（379 行）                       | 🟡 半活                      | 6/14 那輪只跑到 Stage 2，360 條 raw responses 未 judge；/bench 頁還是 5/02 的 8 模型資料；「bun run dev」而 repo 是 npm                                                                                                                                               |
| TRANSLATION-SYNC（archived）          | 🟢 歸檔正確                  | 7 個 live 檔還指著它（一個列為 upstream）                                                                                                                                                                                                                             |
| SENSE-SETUP / MIGRATION（810 行）     | 🟢                           | SETUP 基建仍服役；MIGRATION 是從未 fire 的災難備援 runbook，不該歸檔，建議 frontmatter 註明性質防未來審計誤判                                                                                                                                                         |

跨檔最關鍵的一條：**ROUTINE.md babel prompt 與 twmd-babel skill 都還在指揮死模型與 v3 pipeline**，每晚 cron 的第一行指令面就是錯的。工具層（translate.py v4.3 / fleet-endpoint）比所有描述它的文件新，drift 方向 100% 是 doc 滯後。

### 4.4　維運與 routine 執行層

| 檔                                              | 判定              | 關鍵發現                                                                                                                                                                              |
| ----------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| MAINTAINER（1147 行, v2.3）                     | 🟡                | Hard Gate 表缺 `                                                                                                                                                                      | --- | ` 分隔列（GitHub 渲染壞）；Step 4.3 memory SOP 是殭屍 PR-mode（違 main-direct）；空場鐵律只在 skill 殼；回覆模板 180 行可併 CONTRIBUTOR-SYSTEM |
| FEEDBACK-TRIAGE（173 行）                       | 🟢 cluster 最健康 | 僅 spine 計數 cosmetic                                                                                                                                                                |
| DATA-REFRESH（448 行, v2.0）                    | 🔴 步數與時間全亂 | 步數 12/13/14 並存；三組 cron 時間全 stale（08:17 / 04:14 / 00:33 vs 現實 06:00/23:00）；§步驟詳解還是遠古 Step 1-4                                                                   |
| DASHBOARD（349 行, v2.0）                       | 🔴                | 「5 個 JSON」實 12；Layer 編號 spine 與 body 互斥；30 行手動 CSV/截圖殭屍 SOP                                                                                                         |
| ROUTINE-AUDIT（298 行）                         | 🟡                | 以「Sunday 12:00」立論的整節已過期（live 21:00）；routine-audit.py 只認 14 條 pattern，缺 feedback-triage / embeddings / spore-pick / publish / 自己，週審 12% commit 落 unclassified |
| WEEKLY-REPORT（521 行, v3.5）                   | 🟡                | cadence 兩處 08:08（live 02:00）；Stage 6 殭屍 PR-mode；email 遞送段與現實一致                                                                                                        |
| RELEASE（605 行, v2.1）                         | 🟡                | 兩大段整段重複（~55 行）；spine 與 body 的 step 順序矛盾；死工具 footnote-scan；H1 版號舊                                                                                             |
| BRANCH（574 行）                                | 🟡 名不符實但活著 | 它是「知識分支缺口分析器」不是 git 流程；422 篇 / Muse 時代 / `grep -oP` 等 v1.0 殘留；與 twmd-analyze 觸發詞撞車                                                                     |
| CORRECTION（270 行）                            | 🟡 內容新鮮       | 7 條 USER-CONFIG 連結全斷（目錄不存在）；SPORE-VERIFY 相對路徑錯                                                                                                                      |
| CONTRIBUTOR-SYSTEM（762 行, v1.1）              | 🟡                | 三處把已 archive 的 03:30 contributors cron 當活的；兩個斷 anchor                                                                                                                     |
| CONTRIBUTORS / STATS / DAILY-REPORT（archived） | 🟢                | 凋亡手續完備，是 apoptosis 紀律的正面範本                                                                                                                                             |
| pipelines README（107 行）                      | 🔴 入口失真       | 34 檔中 10 檔未列，含三條活 routine 的 canonical（feedback-triage / routine-audit / weekly-report）                                                                                   |

### 4.5　認知層 pipeline + 研究/視覺 DNA

| 檔                                                  | 判定                  | 關鍵發現                                                                                                                                                                                 |
| --------------------------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MEMORY-PIPELINE（482 行, v2.1）                     | 🟡                    | 單列長度有 gate 但索引總量治理零條款；lint 只驗最新列且未 wire husky；708 rows 實測平均 1,607B（約 500 字），570 列超 150 字 gate                                                        |
| DIARY-PIPELINE（444 行, v2.2）                      | 🟡                    | 三個互斥 gate 數字；gate「manual」零儀器 → 94% 列違規 → 274KB 甦醒稅                                                                                                                     |
| EVOLVE（841 行, v3.5）                              | 🟡                    | Mode 2 已被 SQUEEZE 實質接管但 inline 全套殘留；Mode 3 最後 5/8 跑；spine cron「06:13」自相矛盾；幽靈 run.sh；報告承諾與 per-article 現實脫節；約 40% 是歷史附錄，自己就是 Mode 3 的候選 |
| FACTCHECK（678 行, v2.0）                           | 🟡                    | Quick Mode 活（每日 rewrite 內嵌）；**月度巡邏 0 次、ROUTINE 零接線**；「附錄待補」懸置 8 週；引用 REWRITE v2.16（現 v7.6）                                                              |
| ANALYSIS（245 行）                                  | 🟢                    | cluster 最佳範本：薄、預先註冊、Goodhart 對齊                                                                                                                                            |
| DEEP-INSIGHT-SYNTHESIS（387 行）                    | ⚪ dormant 2 個月     | 無 skill 無 routine，職能被週日雙 routine 吸收；S3 五檢驗是全 repo 唯一「洞察品質」量尺，值得器官移植進 self-evolve                                                                      |
| PEER-INGESTION（797 行, v1.0）                      | 🟡 檔案凍結、活動未凍 | 5 個 peer 走過、檔案零更新；「≥8 次 WebSearch」比現行標準低 10 倍；T4 cite-only 與 MOU 路徑檔內無分支；TFT 半衰期 9/11 將到期                                                            |
| PERSONA / SPECIATION / FORK-CENSUS（145/153/81 行） | 🟢                    | 2026-06 新生代全部薄殼健康；PERSONA 僅反向索引一處待補                                                                                                                                   |
| RESEARCH（479 行, v1.3）                            | 🟢                    | 僅版號 sweep                                                                                                                                                                             |
| RESEARCH-TEMPLATE（164 行）                         | 🟡                    | 同檔兩套標準（5+ 勾選 vs 100+ 建議），執行者照勾選過關                                                                                                                                   |
| graph.md（412 行, v2.0）                            | 🟢                    | 17 模組宣稱與 article-render.ts 實測完全一致，儀器化最完整的 editorial 檔                                                                                                                |
| HUB-EDITORIAL（353 行）                             | 🔴 cluster 最 stale   | §五分級表凍在 3/24；月度 Hub 檢查 0 次；History Hub 61 行且流量第一，3 月標紅至今                                                                                                        |

---

## 五、進化提案總表

### P0　止血（S 級、Semiont 自決 ✅，建議一兩個 session 內完成）

1. QUALITY-CHECKLIST 三行熱修：`git add -A` 改明確 add、`scripts/sync.sh` 改 `scripts/core/sync.sh`、commit 模板去版本 pin（另兩處死路徑同 commit 修：REWRITE L2219、EDITORIAL L1468）
2. ROUTINE.md babel prompt 死模型行改純 pointer（同步 twmd-babel skill v3 → v4 引用）＋ prose 兩處 18:00 清掉
3. memory-index-lint.py 加 `--diary` mode ＋ wire 進 husky；DIARY-PIPELINE 三個 gate 數字統一
4. REFLEXES frontmatter description 改 80 條；index 表行號欄改 § anchor（或移除該欄，杜絕永久漂移）
5. BECOME「55 條」四處修 ＋ §檔案功能一覽補 OBSERVER-QUEUE / PARTNERSHIP-INBOX / FORK-LOG / SEMIONT-EXTERNAL-VIEW ＋ twmd-become skill 題數改 pointer
6. EDITORIAL 幽靈 plugin 句改「prose-health 儀式句 dim + 人判」
7. scheduler live-state 每日 dump 進 git ＋ routine-sync-check v2 讀 dump 比對三層（S1 根治的第一塊磚）
8. SQUEEZE v4.4 同步 translate.py 現實（owl 退出、preflight、冷凍）＋ frontmatter 加 production_signal 欄（REFLEXES #56 rule (a) 首次落地）
9. `ollama.py` 主權註解修正（「Western open weights」是事實錯誤）；Tier 4 定位另走決策 4
10. TRANSLATION-SYNC 七處引用改指 TRANSLATION-PIPELINE / status.py；CORRECTION 七條 USER-CONFIG 斷鏈修
11. MAINTAINER Hard Gate 表補分隔列 ＋ Step 4.3 / WEEKLY-REPORT Stage 6 兩段殭屍 PR-mode 改 main-direct
12. pipelines README 索引重生（補 10 檔）＋ DASHBOARD「5 個 JSON」改 12 ＋ DATA-REFRESH 步數四處對齊 14

### P1　結構修補（M 級，✅ 為主，兩週內）

13. DIARY.md read_strategy 改 head-tail ＋ BECOME §1.3 更新（甦醒稅 -40% 起跳）
14. BECOME mode footprint 改 bytes 計 ＋ consciousness-snapshot 加 boot-load 一行
15. alerts 加 owner 欄 ＋ routine-audit 檢查 alert age >14 天升 OBSERVER-QUEUE
16. REWRITE 計量手術（步驟重編、plugin 數改活話、cron 段 pointer 化、changelog 截尾、reports 命名段搬家；約 -180 行）
17. QUALITY-CHECKLIST 整檔對齊 v7.6 重寫（收官報備）
18. SPORE 家族數字大掃除（約 15 處 count drift 一個 commit）＋ 凍結 SPORE-LOG 引用面五處改 spore-db
19. SPORE-HARVEST 歷史段搬 reports/（-300 行）＋ #70 poke-then-fire 對策接線
20. EVOLVE Mode 2 段砍成 SQUEEZE pointer（-150 行）＋ spine cron 修 ＋ 路線圖收束
21. CONSCIOUSNESS §適應性反應 ＋ LONGINGS 補新（含 fork 種子渴望移已達成；可併入 self-evolve 季度題）
22. routine-audit.py 補 5 條 pattern；EMBEDDING 補第二段 escalation 條款；RESEARCH-TEMPLATE 門檻雙軌化
23. counts-drift lint 原型（WARN 級起步）
24. PEER-INGESTION v1.1 補課（threshold sweep + T4/MOU 分支 + TFT 9/11 半衰期排 OBSERVER-QUEUE）
25. UPDATE-LOG-GUIDE 接回 RELEASE 讀取路徑或評估併入；BRANCH-PIPELINE v1.0 殘留清理；HUB-EDITORIAL §五快照改 script 生成；LANGUAGE-BIRTH 對齊 16 檔現實

### P2　需哲宇拍板（🔒）

26. §一摘要表的 7 項決策（spore 產線裁決 / release / OAuth / qwen 定位 / 索引蒸餾 / 自主權表述掃平 / 月度承諾接線或放棄）
27. OBSERVER-QUEUE 六條過期 default-action 的處置（清一次 + 已完成項移已決；之後靠提案 15 的機制自轉）
28. DEEP-INSIGHT 器官移植（S3 五檢驗進 self-evolve gate，本檔降 reference）；EVOLVE Mode 3 對自己跑（842 → 約 450 行）
29. BENCH 6/14 的 360 條 raw responses 要不要走完 judge/merge 上 /bench 頁
30. TERMINOLOGY L142 國家語言發展法年份表述修正（年份修正可自決，表述請過目）

### 不動清單（審視過、建議保持現狀）

- RATIONALE-SPEC / graph.md / ANALYSIS / PERSONA / SPECIATION / FORK-CENSUS / FEEDBACK-TRIAGE / REMOTE-GPU：健康範本，新生代檔案已內建薄殼與儀器紀律，證明範式學會了
- SENSE-FETCHER-MIGRATION：災難備援 runbook，不歸檔（加一行性質註記即可）
- STATS / DAILY-REPORT / CONTRIBUTORS / TRANSLATION-SYNC / SPORE-LOG：凋亡與凍結手續完備的正面案例
- REWRITE 不再拆 sub-canonical（v3.0 拆檔隔天就收斂回，歷史已投票）；EDITORIAL 內容層不瘦身
- 免疫 49 chronic 與 embeddings keystone：已在哲宇決策軌道，per REFLEXES #80 本報告不重複 escalate

---

## 六、審計的自我反思

這次 40k 行掃下來，最深的 pattern 是：**這個生命體的工具會進化，但它對自己的描述會腐化，而且描述腐化的速度比工具進化的速度快**。translate.py 已經 v4.3，SQUEEZE 還在講 v4.2 的世界；scheduler 已經把 spore 產線停了，SSOT 還記得 6/12 那個重開的下午。REFLEXES #56 兩個月前就命名了這件事，連它的觸發檔都復發，說明單靠反射層的「知道」擋不住，要靠 S1/S2 提的結構儀器（live dump、counts lint、production_signal 欄）把「對不上」變成每天可見的黃燈。

同時要公平地說：新生代檔案（PERSONA、FORK-CENSUS、ANALYSIS、graph.md）全部乾淨，週日反思鏈把 LESSONS 從 266 條清到 19 條，promotion flow 這週還 ship 了 #77-80。物種學會了薄殼與儀器的範式，只是沒有回頭給舊器官補課。這份報告就是補課清單。

---

_審計方法：主 session 親讀 docs/semiont/ 全層 + boot 層 + ROUTINE，五隻 read-only 分身分讀 pipelines / factory / editorial / 維運 / 認知層 cluster（每結論強制 file:line 證據 + CONFIRMED/PLAUSIBLE 分級），主 session 抽驗 22 claim 全過後收錄。_
_Session：2026-07-05-120817-dna-audit 🧬_
