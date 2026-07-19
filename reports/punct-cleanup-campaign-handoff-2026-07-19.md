---
title: '標點淨化 campaign 實作計劃 + handoff（144 篇 legacy → 全站升 hard）'
description: '哲宇選項3 完整化：144 篇 legacy 破折號>15 / 分號>12 清理，交 codex(sol/luna/terra)+ollama 協作。純標點、零事實漂移、機械可驗證。清完把 ci-deploy 升 hard 達成完整選項3。'
date: 2026-07-19
type: 'campaign-handoff'
status: 'ready-to-dispatch'
owner_execution: 'codex sol/luna/terra + ollama（哲宇 dispatch）'
verify_tool: 'scripts/tools/punct-cleanup.py'
worklist: 'reports/punct-cleanup-worklist-2026-07-19.tsv'
---

# 標點淨化 campaign — 實作計劃 + handoff

> **給執行的 agent（codex sol/luna/terra / ollama）**：你看不到當初的對話，這份是你的
> 唯一 spec。照做就對了。**最高原則：寧可少改，也不要改到事實。** 每篇清完必跑
> `punct-cleanup.py --verify`，紅了就 revert 重來，不准帶著 FAIL 往下。

## 這是什麼

Taiwan.md 的 prose-health 儀器 2026-07-19 新增「破折號 / 全形分號」偵測。全 corpus
量測發現 **144 篇 legacy 文章**破折號 > 15 或全形分號 > 12（AI 生成語料的系統性翻譯腔
水印）。目標：把這 144 篇的標點清乾淨，清完就能把全站 ci-deploy gate 升 hard，達成
完整的「選項 3」（新舊文章都硬性擋超量標點）。

**現況**：pre-commit 已經對「你 commit 的檔」硬擋（破折號>15/分號>12）。ci-deploy
全站還是 WARN（不 brick）。這個 campaign 清完 legacy，才能把 ci-deploy 也升 hard。

## 鐵律（違反任一 = 這次清理作廢，revert 重做）

1. **只改標點與其周邊的連接詞。** 破折號（——）、全形分號（；）。改完句子的意思必須
   一模一樣。
2. **絕不改動任何**數字、年份、日期、金額、里程、統計、人名、地名、機構名。
3. **絕不改動**「」『』引號內的任何字、`>` blockquote 引言、腳註定義的文字或 URL。
4. **絕不動 frontmatter**（開頭兩個 `---` 之間）。
5. **絕不動** code fence（`tw-timeline / `tw-bars / ```tw-figure）、HTML `<div>`/
`<iframe>`、圖片 `![...]()`、以及「延伸閱讀 / 圖片來源 / 參考資料」段落。
6. **絕不增刪或改號任何腳註 marker `[^n]`** —— 每個 `[^n]` 留在原本的子句上。
7. 用 **Edit（逐處）**，不要用 Write 整檔覆寫（整檔覆寫最容易夾帶事實漂移）。

## 怎麼改（method）

### 破折號「——」→ 目標 ≤ 15（理想 ≤ 8）

逐個 rhetorical 破折號，換成語意等價的自然標點：

- 補充說明 → 冒號「：」或括號（）
- 轉折/接續 → 逗號「，」或拆成句號短句
- 例：「它是另一種速度——權力收攏的速度」→「它是另一種速度：權力收攏的速度」

**保留這幾種破折號（合法、不要動）**：

- 書名號內：《大道之行——中山高速公路建設人員口述印記》
- 引語出處：「……」——王春發，公視〈我們的島〉，2013
- 破折號在 `>` blockquote / callout 裡的，一律不動（鐵律 3/5）

### 全形分號「；」→ 目標 ≤ 12（理想 ≤ 3）

- 並列子句 → 拆成兩個句號句：「A；B」→「A。B」
- 條列 → 頓號：「以為甲；以為乙；以為丙」→「以為甲、以為乙、以為丙」或拆句
- **腳註定義行、引號內、code fence 裡的 ；不要動**（那些 verify 也不計）

### 不必要的對比收束句（若出現）

若看到「（兩者）根本是兩件事 / 兩本帳 / 根本是不同的語言 / 從來沒攤開在同一頁」這種
拿抽象對比幫段落強行收尾的句子，改寫成具體陳述（寫出兩者各自是什麼、差在哪）。
**但這是 optional**——沒把握就別動，鐵律優先。

## 每篇的工作流（嚴格照順序）

```
1. git 確認乾淨：該檔沒有其他人未 commit 的改動
2. Read 整篇
3. 逐處 Edit 改破折號 / 分號（照上面 method + 鐵律）
4. 驗證（必跑，紅了就 revert 重做，不准帶 FAIL 往下）：
     python3 scripts/tools/punct-cleanup.py --verify <該檔路徑>
   綠了才算這篇 done。verify 會檢查：
     - frontmatter 逐字節不變
     - 腳註 marker + 定義數不變
     - 所有數字 multiset 不變（← 抓改到數字的事實漂移）
     - 所有引號內容 multiset 不變（← 抓改到引語）
     - 所有連結 URL 不變
     - 破折號 ≤ 15、分號 ≤ 12（達標）
     - article-health --profile=pre-commit hard=0（過所有 hard 檢查）
5. commit（一篇一 commit 或小批一 commit 都行）：
     git commit -m "🧬 [semiont] polish: <檔名> 標點淨化（破折號 N→M、分號 P→Q）"
```

**verify 紅了怎麼辦**：看它報哪一項。若是「數字變動 / 引號變動」= 你改到事實了，
`git checkout <檔>` 全 revert，重新只改標點。若是「未達標」= 破折號/分號還太多，繼續改。
若是「article-health hard fail」= 看它報什麼 hard（可能你不小心弄壞了 wikilink /
frontmatter），修掉。

## 分工（codex sol / luna / terra + ollama 不撞車）

工作清單：`reports/punct-cleanup-worklist-2026-07-19.tsv`（144 篇，已按嚴重度排序，
含 category / featured 欄）。**同一篇只能一個 agent 改**（避免並寫互蓋）。建議切法：

- **codex sol / luna / terra**（品質最高，吃硬骨頭）：破折號 ≥ 40 或分號 ≥ 20 的重症
  （蘇打綠 72、認知作戰 62/23、辦桌 53/22、許倬雲 61 等，約 25-30 篇）。三個 instance
  各拿 worklist 的 1/3（例如 sol 拿行 1,4,7…／luna 拿 2,5,8…／terra 拿 3,6,9…，
  interleave 切最平均）。
- **ollama**（本機、量大）：破折號 16-40 / 分號 13-20 的中症長尾（約 110 篇）。序列跑。
- **featured 47 篇優先**（曝光高，worklist featured 欄標了）——建議 codex 先掃完所有
  featured，再回頭吃非 featured。

**checkpoint / resume**：清單是排序固定的，隨時可以重跑 `--worklist` 看還有哪些超標
（已清乾淨的會自動從清單消失，因為它們不再 > 門檻）。所以「還剩幾篇」= 重新產清單
的行數。天然可恢復，不需要額外狀態檔。

## 收尾：清完 144 篇 → 全站升 hard（達成完整選項3）

當 `python3 scripts/tools/punct-cleanup.py --worklist` 產出 **0 篇**（全部達標），
把 pre-commit 的 override 複製一份到 ci-deploy profile，全站就升 hard：

在 `scripts/tools/article-health.config.toml` 的 `[profiles.ci-deploy]` 區塊加：

```toml
[profiles.ci-deploy.options_overrides.prose-health]
emdash_hard_over = 15
semicolon_hard_over = 12
```

然後驗證全站不 brick：

```
python3 scripts/tools/article-health.py --all --profile=ci-deploy --quiet && echo "全站升 hard 成功，0 brick"
```

綠了 = 完整選項 3 達成：新舊文章都硬性擋破折號>15 / 分號>12。
（這步 config 改動建議由哲宇或主 session 做最後確認，因為它動的是全站 deploy gate。）

## 品質保險（哲宇「不能讓文章品質降低」的落地）

- verify 的數字/引號/腳註/URL/frontmatter 五道 multiset 檢查 = 事實不會漂。
- article-health pre-commit gate = 不會為了壓標點而弄壞結構（wikilink / footnote /
  frontmatter 全在 hard 檢查裡）。
- 「寧可少改」原則 + 達標門檻設在 gate 值（≤15/≤12）而非理想值（≤4/≤3）= 不逼 agent
  過度改寫。標點變少讀起來只會更順，不會更差——前提是嚴守鐵律只動標點。
- **抽驗**：哲宇可隨機抽幾篇清完的，念念看語感有沒有跑掉（verify 保事實，語感靠人抽）。
