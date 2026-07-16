---
title: '文章儀器進化：speak-human-tw 轉譯 + 盤點工作儀器化 + gate 整理'
description: '2026-07-16 哲宇 /goal — 參照 Raymondhou0917/speak-human-tw（38 種 AI 痕跡目錄）進化文章儀器，同日把 inbox 盤點與品質審核的手工方法儀器化，並整理久未校準的 gate'
date: 2026-07-16
type: 'evolution-report'
session: '2026-07-16-205022-inbox-audit（下半場 /goal）'
---

# 文章儀器進化 — 2026-07-16

哲宇 directive 三件事：(1) 參考 [speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw)（Raymond Hou，MIT，v1.4.0）思考文章儀器可以吸收什麼——「參考就好，我們站跟文章的性質不太一樣，要謹慎調整」；(2) 把今天上半場 inbox 盤點與品質審核的手工工作儀器化；(3) 全面進化久未整理的文章 gate 與儀器。

## 一、speak-human-tw 是什麼、跟我們差在哪

它是針對**行銷與辦公文字**（電子報、社群貼文、銷售頁、客服信）的去 AI 味改寫 skill：38 種 AI 痕跡目錄（整理自中文維基 WikiProject AI Cleanup、朱宥勳 AI 腔分析、英文維基 Signs of AI writing）、保護清單、五情境力度表、正向人味目標、40 條 benchmark（含「不該改」的誤殺防護負例組）。

性質差異決定了轉譯邊界：

| 維度      | speak-human-tw             | Taiwan.md                                             |
| --------- | -------------------------- | ----------------------------------------------------- |
| 對象文體  | 行銷/辦公短文              | 策展式知識庫深度文（中位 6,556 字/22 腳註）           |
| 運作模式  | 互動式改寫服務（兩輪確認） | pipeline gate（寫作端守門，不是改寫端）               |
| 事實層    | 「不代查、標記交作者」     | FACTCHECK/Stage 3.5-3.6 自己查到底                    |
| 詞語主權  | 6 行中國用語替換表         | 2,300+ per-term sovereignty 詞庫 + terminology plugin |
| 表格/粗體 | 降格式（貼文場景）         | tw-\* viz 與對照表是策展特色                          |

## 二、收／改造收／不收（逐項裁決）

### 直接收（儀器級，本日 ship，全部 soft-launch）

| 來源 pattern                                                                | 我們的落地                                                                                                          | 等級                 |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------- |
| #37 AI 工具殘留（utm_source=chatgpt / turn0search / citeturn / 私有區字元） | 新 plugin `ai-residue`                                                                                              | hard（鐵證級零誤殺） |
| #30 協作交流殘留（「以下是修改後的版本」）                                  | 併入 `ai-residue`                                                                                                   | hard                 |
| #5 模糊歸屬（研究顯示/專家認為 無出處）                                     | 新 plugin `attribution-vague`——知識庫特化：命中後查同段有無 `[^N]` 腳註，有就放行。比原版強（我們有腳註系統可對接） | warn                 |
| #9 立場真空（各有優缺點/見仁見智/因人而異）                                 | prose-health Tier 4——與「策展式非百科式」信念直接對齊：維基追求的中立正是我們拒絕的                                 | 計分                 |
| #1/#3 價值上升詞（標誌著/見證了/體現了/彰顯了）                             | prose-health Tier 4，**密度計分**非逐 hit（史觀文有合法單次使用）；「轉捩點/里程碑」刻意不列（歷史文合法高頻）      | 計分                 |
| #21 時代帽子開場（在當今⋯的時代）                                           | prose-health Tier 4——EDITORIAL 已要求具體人物/時刻開場、chronicle-lead 抓編年開場，這補宏觀帽子這一族               | 計分                 |
| #32 罐頭結尾起手式（總的來說/綜上所述）                                     | prose-health Tier 4——EDITORIAL「不做罐頭總結」第一次有儀器                                                          | 計分                 |
| #15 假推論（這意味著）密度                                                  | prose-health Tier 4                                                                                                 | 計分                 |
| #26 首先/其次/最後 三件套                                                   | prose-health Tier 4                                                                                                 | 計分                 |
| evals 方法論（SF 該改 26 條 + SNF 誤殺防護負例組）                          | roadmap：prose-health 建誤殺防護測試組（我們的 gate 至今只有正例、沒有「不該報」的負例迴歸組）                      | 待造                 |

### 改造後收

- **五情境力度表 → doc-type profiles**。它按「發布場景」調力度；我們按「文件類型」——今天實測 memory/diary/reports 跑文章版 prose-health 長期 7-12 分超 3 分 budget 被默許，gate 名存實亡。新 `memory-diary` profile（budget 8，排除引用類維度誤傷），MEMORY/DIARY pipeline 指過去。
- **保護清單概念**。quote-fidelity 已保引語、terminology 有例外表；補進 roadmap 的是 `--fix` 類 plugin 的引語/code-fence 保護稽核。

### 不收（性質不合，明確記錄避免未來重議）

- **#23 破折號「每 300-500 字最多 1 次」**：遠嚴於我們 15/1500 字現行紀律；MANIFESTO §11 已用自己語料校準過，不跟進。
- **#12 對位句型「整篇最多一次」**：我們已有 ≤3/1500 + 三題判準，比它細；收緊會誤殺史觀對比（「不是碳基的，是資訊基的」是定義不是套話）。
- **#24/#25/#28 粗體/列表/表格降格式**：為貼文平台設計；我們的對照表與 tw-\* viz 是策展特色。
- **taiwan-localization 詞表**：我們的 sovereignty 詞庫是它的超集。
- **#13 換詞循環、#29 句長過勻、#17-20 說教腔/金句/假坦白/短句轟炸**：意義層，regex 必然大量誤殺——per OBSERVER-QUEUE #15 決策精神（意義層維持人判＋編輯室分席），這幾種寫進 EDITORIAL-ROOM 攻防輪的參考彈藥即可，不硬造 plugin。
- **兩輪確認互動模式**：我們是 gate 模型不是改寫服務；但它的「非互動環境跳過確認、事後摘要」設計跟我們 routine 的 defer 哲學互相印證。

## 三、盤點工作儀器化（上半場手工 → 常備儀器）

1. **`article-depth-audit.py`**（新，本 session 主寫）：把 69 篇審核的方法論固化——動態近期基準（45 天窗口 p25/中位）＋ severe/next 雙門檻＋首作者歸因。第二輪審核（+190 篇）從此一條指令。
2. **`inbox-audit.py --spore`**（Sonnet agent 實作）：SPORE-INBOX 對賬——幽靈（已發未刪，天燈案）/重複/blueprint 編號碰撞（#148/#149 案）/REACTIVE 逾 21 天過期，report-only（孢子裁決一律人工）。`inbox-signal.sh` 補 ghost/dup 訊號行。
3. **`ai-residue` / `attribution-vague` / prose-health Tier 4**（Sonnet agent 實作）：見上表。

## 四、gate 整理（久未校準部分——全儀器盤點結果）

完整現況地圖由 Explore agent 盤點（26 個 plugin + husky 雙 hook + 3 條 CI workflow + 10 個 standalone 儀器，含每檔最後實質修改日期）。要害與處置：

1. **懸空 canonical pointer（已修）**：`reports/article-health-ssot-design-2026-05-04.md` 被 5 處引用但從未存在。已依程式碼 docstring 與 config 註解重建五條設計原則（單一入口 SSOT／declarative profile／severity 三層／shadow-run 升級／對稱原則），檔名沿用原路徑直接解懸，標明 reconstructed。
2. **prose-health 的結構性不對稱（已修）**：word-count／image-health／media-richness／paragraph-rhythm／quote-fidelity 五個 plugin 都在內部 skip `memory/ diary/ reports/`，唯獨 prose-health 沒有——但 MEMORY／DIARY pipeline 又明文要求對 memory 檔跑它，budget 3 分對必填 checklist 結構必然超標，近期 memory 實測 7-12 分＝gate 名存實亡。處置：新 `memory-diary` profile（budget 8）＋ prose-health 支援 per-profile budget option，pipeline 指過去。
3. **9 個 2026-05-04 出廠後未回頭的 plugin**：cjk-punct／cross-reference／footnote-density／footnote-url／format-structure／link-target／terminology／wikilink-target（＋`__init__`）。判讀：多數是穩定的機械檢查（半形標點、連結存在性），停在出廠日是健康不是債；真正要留意兩個——**terminology plugin vs 7/11 詞庫深度進化的同步**（536 flag 還在 OBSERVER-QUEUE #11 等哲宇，plugin 先不動）與 **footnote-density A-F 分級從未用真實語料回頭校準**（A 級=≥3 腳註+密度≤300 字/註，以近期中位 22 腳註看已偏鬆，列第二輪校準候選）。
4. **pr-frontmatter-gate 紅 X 不是 required check**：workflow 自己註明要真擋 merge 需在 branch protection 設定，留哲宇拍板（見 §七）。
5. **核心 lib（runner/config/registry）自 5/04 未動**：架構穩定的訊號；本輪擴充幾乎全走 plugin/config 層，驗證了原設計的擴充性。
6. **`fail_on="score-budget"` 是休眠 no-op（已修）**：實作 memory-diary profile 時發現這個 fail 模式從未真正檢查過 score——舊碼跟 `fail_on="hard"` 完全同義，REWRITE Stage 3 文件寫的「quality-scan ≤3 自動驗證」從未在程式碼層生效過（跟本節 #2 同族：規格債偽裝成品債）。已在 article-health.py 接上真閘門（profile override > config > 預設 3），只影響 rewrite-stage-3 與新 memory-diary 兩條路徑，pre-commit/ci-deploy 邏輯不變，前後行為以合成文章驗證（score 7 在 budget 3 fail、budget 8 pass）。

## 五、校準結果（REFLEXES #66，完整數據見 [instrument-calibration-2026-07-16.md](instrument-calibration-2026-07-16.md)）

- **prose-health Tier 4**：855 篇全站前後比對——96.7% 分數完全不變、delta 中位 0、近期 15 篇 A 級樣本全部 delta 0 零翻轉；僅 4 篇壓線文章（0.5%）從 3 分過線到 4。通過「近期 A 級增量中位 ≤1」驗收線。
- **ai-residue**：全站 0 命中（鐵證級 pattern 本來低頻）＋合成 7 injection 測試 7/7 全中——留 HARD 上線不會擋任何現有 commit/CI。
- **attribution-vague**：第一輪 9 hits 抽 3 全誤報（具名學者＋機構縮寫被誤殺）→ 當場加兩條句法判準（「的」前後放行）→ 第二輪 5 hits 抽 3 全真陽性、0 誤報。**這 5 個真陽性是現成 heal 候選**：白海豚基因分化論斷、楊丞琳「研究顯示是都市傳說」反駁句、素食健康功效句、茶文化、營養午餐——全是該補來源的無源權威句。
- **迴歸**：article_health 測試 214 passed；4 個 fail 以 git stash 驗證為 pre-existing（frontmatter-title/image-health 既有 drift，未動該檔）。inbox-audit 原模式輸出 byte-for-byte 不變。
- threshold 升 HARD 走既有 staged promotion（vc≥3）慣例，由哲宇拍板。

## 六、待哲宇拍板

1. **pr-frontmatter-gate 升 required check**：workflow 紅 X 目前只是訊號，要真擋 merge 需在 GitHub branch protection 勾 required——一個設定動作，效果是 contributor PR 不過 gate 就不能 merge。
2. **新 pattern 的 HARD 升級節奏**：本輪全部 soft-launch；`ai-residue` 若全站校準零誤報，建議直接留 HARD（鐵證級）；其餘走 vc≥3 慣例。
3. **footnote-density A-F 分級重校準**：A 級門檻（≥3 腳註）以近期中位 22 腳註看已偏鬆，要不要按近期基準重刻（例如 A=≥15、B=≥8）？影響 dashboard 免疫分數組成，屬 threshold 調整。
4. **memory-diary budget=8**：從近期 memory 實測 7-12 校準的過渡值，用一兩週後回頭看要收緊還是維持。
5. **roadmap（不急）**：prose-health 誤殺防護負例測試組（借 speak-human-tw evals 的 SF/SNF 雙組方法論）；ARTICLE-INBOX 閒置 entry 偵測（Requested >60 天仍 pending → 降級候選訊號）；`--fix` 類 plugin 的引語/code-fence 保護稽核；article-depth-audit 掛進月度 distill 節奏；zh 樹純度檢查（非 zh 內容檔滯留 knowledge/{Category}/ 的結構性偵測——鐵道史 .en.md 案的通例化，本輪只修了實例）。

## 七、致謝與授權

speak-human-tw by Raymond Hou（雷蒙），MIT License。轉譯的 pattern 在 plugin 註解與本報告標明出處。其目錄上游（中文維基 WikiProject AI Cleanup、朱宥勳分析）一併致意。

🧬
