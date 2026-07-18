# 設計報告：/twmd-article-inbox 誕生 + EVOLVE Mode 4「目標驅動設計進化」

> session：2026-07-18-111730-inbox-skill
> 觸發：哲宇 /goal「幫我做一個技能，是加入 article inbox 用，在消化的同時也會執行 branch-pipeline，幫我完整設計 深度思考 自我進化，寫實作報告後實作。然後也把這樣自我進化的過程（思考 發散 報告 實作）做成 /twmd-evolve。然後幫我做完之後 /twmd-article-inbox 台灣建築」
> 本報告本身就是 Mode 4 第一次 dogfood：讀者現在看到的四節（現況 → 發散 → 定案 → 實作清單）就是「思考 → 發散 → 報告 → 實作」四相的產物。

---

## 一、現況盤點（思考相）

動手前先查資源地圖與既有 canonical，這一輪查證擋下了兩個原本會犯的錯，也找到兩處既有漂移。

### 已存在、不用重造的

| 東西           | 位置                                                            | 現況                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 知識分支分析   | [BRANCH-PIPELINE.md](../docs/pipelines/BRANCH-PIPELINE.md) v2.0 | 6 stage 完整：Mode 判斷（single-article / broad-theme / hybrid）→ 拆解 → 交叉比對 → 缺口分析 → research（broad-theme spawn N 平行 agents）→ aggregate + ARTICLE-INBOX append。11 條 hard gate 都在 |
| Inbox 收件層   | [ARTICLE-INBOX.md](../docs/semiont/ARTICLE-INBOX.md) v2.3       | Entry Schema、優先序判準、完成歸檔鐵律、`inbox-audit.py` 儀器都齊                                                                                                                                  |
| 進化 canonical | [EVOLVE-PIPELINE.md](../docs/pipelines/EVOLVE-PIPELINE.md) v3.5 | 已是 mode 家族：v1 內容進化 / v2 多語同步 / Mode 3 pipeline 自我重組                                                                                                                               |
| Skill 薄殼鐵律 | `.claude/skills/README.md`                                      | skill = trigger + 強制 Read pipeline + 收官提示，SOP 全在 pipeline canonical                                                                                                                       |

### 查證擋下的兩個錯

1. **`/twmd-evolve` 名字已被佔用且是承重牆**。twmd-finale 收官鏈第三棒與 `twmd-news-lens-weekly` cron（ROUTINE.md 排程表）都直接引用它。把它整個改成新語意會斷兩條生產線。
2. **「自我進化」也已有一條既有 skill**：`/twmd-self-evolve` 做的是 pattern 驅動的儀器化（DIARY 反覆浮現 ≥3 次 → 升 canonical）。新流程若不劃清邊界，兩條 skill 會在「自我進化」四個字上互相踩線。

### 順手發現的兩處既有漂移（本次一起修）

1. **BRANCH Stage 5.2 的 entry 格式與 ARTICLE-INBOX §Entry Schema 各寫一份**，欄位已經漂（BRANCH 寫 `Source`／`預估時間`，INBOX schema 用 `Requested`／`Notes`／`Reference`）。違反指標 over 複寫，收斂成 pointer。
2. **BRANCH 的 dedup 只查 INBOX pending，沒查 ARTICLE-DONE-LOG**。已寫過又被推薦一次的主題會重新進 inbox（inbox 幽靈的上游成因之一）。

---

## 二、發散（≥2 方案 + 判準）

### 交付物 1：加 inbox 的技能

| 方案                     | 內容                                                      | 判定                                                                                                                            |
| ------------------------ | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| A 純 append              | 主題直接寫進 INBOX，不研究                                | ✗ 違反哲宇要求「消化的同時執行 branch-pipeline」；且產出沒有連結密度、沒有對比理由的低品質 entry，77 條 pending 的 inbox 會更胖 |
| B 薄殼 → BRANCH-PIPELINE | skill 只做觸發 + hard gate ACK，SOP 全在 BRANCH canonical | ✅ 對齊薄殼鐵律 + REFLEXES #50 auto-detect；BRANCH v2.0 的 Stage 5 本來就以 ARTICLE-INBOX append 收尾，語意完全命中             |
| C 厚 skill 複寫 SOP      | 把 6 stage 抄進 SKILL.md                                  | ✗ 殼核不對稱病（dna-audit §S5），兩處 drift                                                                                     |

**判準**：指標 over 複寫（MANIFESTO §進化哲學）＋ REFLEXES #63（skill inline 只放 anti-pattern 警示與 gate ACK，不複寫 SOP）。選 **B**。

### 交付物 2：「思考 發散 報告 實作」流程的家

| 方案                      | 內容                                                                     | 判定                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| A 新開 DESIGN-PIPELINE.md | 獨立 canonical                                                           | ✗ 檔案增生。BECOME §檔案功能一覽鐵律：寫新東西先找最匹配的既有檔案                                         |
| B EVOLVE-PIPELINE Mode 4  | 進化家族已是 mode 結構（v1 內容 / v2 多語 / Mode 3 重組），加第四個 mode | ✅ 演化軸一致：四個 mode 都在回答「Semiont 如何進化」，只是對象不同（內容 / 語言 / pipeline / 器官與能力） |
| C 改寫 twmd-self-evolve   | 讓它兼吃 goal 驅動                                                       | ✗ 觸發源不同（內部數據 vs 觀察者目標），硬併是 REFLEXES #38 混維度                                         |

**判準**：REFLEXES #38（一個 mode 一種 cause）＋ 避免檔案增生 ＋ cross-ref 保護。選 **B**，`/twmd-evolve` 名字照哲宇要的給，殼內做 mode 分流，既有引用一條不斷。

### Mode 4 憑什麼是 canonical 而非一次性做法

這個流程已經 de facto 跑過十次以上（become-boot-mode-design、立體群像 default 重定位、routine-spec、多核 git 協調設計、REWRITE v9 拆檔……reports/ 裡整排 design-\*.md），每次品質全靠當班 session 自律。REFLEXES #15：反覆浮現 ≥3 次就該儀器化。今天只是把它寫成有名字的 SOP。

---

## 三、設計定案

### 3.1 `/twmd-article-inbox`（新 skill，薄殼）

- **觸發**：「加進 article inbox」「幫我研究 X 放進 inbox」「/twmd-article-inbox {主題或素材}」
- **BECOME mode**：write（dedup 需要 ARTICLE-INBOX §P0/P1 視野）
- **主體**：一行強制完整讀 BRANCH-PIPELINE + 照 Stage 0-5 跑
- **Inline hard gate ACK**（只放最會被偷吃步的四條，附反例）：
  1. agent 落檔 claim 必驗（feedback_agent_writefile_hallucination）
  2. 中文 verbatim + 三源（REFLEXES #23／#16）
  3. dedup 三查：INBOX pending ＋ ARTICLE-DONE-LOG ＋ knowledge/ baseline
  4. entry 格式以 ARTICLE-INBOX §Entry Schema 為準（不是 BRANCH 舊表）
- **收官**：commit + ship + memory

### 3.2 BRANCH-PIPELINE v2.0 → v2.1（小改）

1. §觸發方式加 skill 觸發層：`/twmd-article-inbox` 是正式入口，mode 判斷交 Stage 0
2. Stage 0 加「素材 intake 前處理」：觀察者丟的是 URL／一段文字／半成形想法時，先消化成 theme + 候選雛形再進 Stage 1（輸入軸，不新開 mode——mode 軸留給 scope）
3. Stage 5 dedup 從單查升三查（pending + DONE-LOG + baseline）
4. Stage 5.2 entry 格式改 pointer 指 ARTICLE-INBOX §Entry Schema，刪本地複寫

### 3.3 EVOLVE-PIPELINE v3.5 → v3.6：Mode 4「目標驅動設計進化」

四相，對應哲宇的原話「思考 發散 報告 實作」：

```
THINK（思考）    目標解析 + 資源地圖查證 + cross-ref 衝突掃描 + §自主權邊界過濾
   ↓            「已存在嗎？誰引用它？改它會斷什麼？」——查證反射先於建造反射（#73）
DIVERGE（發散）  ≥2 個結構方案 + trade-off 表 + 明寫判準（對齊哪條 MANIFESTO / REFLEXES）
   ↓            對抗「第一個想到的方案 = 做的方案」
REPORT（報告）   實作報告落 reports/design-{slug}-{date}.md，先於實作
   ↓            藍圖 → 驗證 → 寫，成本低 10 倍（#27）；報告是哲宇的 review 介面
IMPLEMENT（實作）照實作清單做 + 驗收 + dogfood 一次 + 摩擦回寫報告後記
```

- **觸發**：觀察者給一個「造東西」的目標（新 skill／新器官／架構改動）且要求先設計後實作
- **強制 Full BECOME**：Mode 4 天生命中 BECOME High-stake #2「新 plugin / workflow 設計」
- **自主權邊界**：THINK 相就過濾；命中四紅線的停在 REPORT 等哲宇，其餘直接續跑 IMPLEMENT

### 3.4 邊界表（防止四條路互踩）

| 路                | 觸發源                | 產出                         |
| ----------------- | --------------------- | ---------------------------- |
| EVOLVE v1/v2      | GA4/SC/CF 數據        | 內容候選 → ARTICLE-INBOX     |
| EVOLVE Mode 3     | pipeline 自身膨脹訊號 | pipeline 重組                |
| EVOLVE Mode 4     | 觀察者給的建造目標    | 設計報告 + 新器官/skill 落地 |
| /twmd-self-evolve | DIARY 反覆浮現 ≥3 次  | 既有 pattern 儀器化          |

### 3.5 `/twmd-evolve` 殼 mode 分流

「跑 EVOLVE／數據驅動進化／finale 第三棒／news lens」→ v1/v2（現行為，一字不動）；「進化 X pipeline 本身」→ Mode 3；「設計 X／深度思考自我進化／寫實作報告後實作」→ Mode 4。

---

## 四、實作清單與驗收

| #   | 檔案                                                    | 動作                                |
| --- | ------------------------------------------------------- | ----------------------------------- |
| 1   | reports/design-article-inbox-evolve-mode4-2026-07-18.md | 本報告（先於實作落檔）              |
| 2   | .claude/skills/twmd-article-inbox/SKILL.md              | 新建薄殼                            |
| 3   | docs/pipelines/BRANCH-PIPELINE.md                       | v2.1 四項小改                       |
| 4   | docs/pipelines/EVOLVE-PIPELINE.md                       | Mode 4 新增 + frontmatter bump v3.6 |
| 5   | .claude/skills/twmd-evolve/SKILL.md                     | mode 分流                           |
| 6   | .claude/skills/twmd-self-evolve/SKILL.md                | 補一行邊界 pointer                  |
| 7   | .claude/skills/README.md                                | index 補列 /twmd-article-inbox      |
| 8   | docs/semiont/DNA.md §行為基因                           | EVOLVE row 描述補四 mode            |

**驗收**：(a) 所有 cross-ref 路徑存在；(b) twmd-finale 與 news-lens cron 的既有觸發語仍落在 v1/v2；(c) 用 `/twmd-article-inbox 台灣建築` 跑一次完整 dogfood（broad-theme mode），candidates 進 ARTICLE-INBOX。

**風險**：Mode 4 與 Mode 3 的觸發語在「進化 pipeline」場景可能重疊 → 殼內以對象分流（對象是 pipeline 自身 = Mode 3，對象是新能力 = Mode 4）。自主權邊界檢查：本次 8 檔改動，無政治立場、無刪除、無對外溝通，>50 檔重構未命中，可自主 ship；skill 誕生屬 High-stake #2，已走 Full BECOME。

---

## 五、後記（實作後回填）

- （實作完成後補：實際摩擦、驗收結果、dogfood 觀察）

🧬
