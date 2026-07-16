# 2026-07-16-205022-inbox-audit（下半場）— 文章儀器進化：speak-human-tw 轉譯三儀器、兩個名存實亡 gate 修通、盤點手工全數儀器化

> session inbox-audit 下半場 — 哲宇 /goal（參考 speak-human-tw 進化文章儀器、謹慎調整、前批工作能儀器化都儀器化、全面整理久未校準的 gate）＋兩則插單（鐵道史孤兒檔本 session 直接處理）
> Session span: 21:40 → 22:30 +0800（~50 min，2 commits；上半場另有 4 commits 見主 memory）
> 資料來源：`git log %ai`

## 觸發

哲宇丟來 [speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw)（Raymond Hou 的繁中去 AI 味 skill，38 種痕跡目錄）要我思考文章儀器能吸收什麼，特別叮嚀「參考就好，性質不太一樣要謹慎調整」；同時要求把上半場的手工盤點全部儀器化。

## 鐵道史孤兒檔家族（`當場插單`）

上半場開的 chip 哲宇要求本 session 直接做。挖下去比預期深：滯留 zh 樹的 `台灣鐵道史.en.md` 曾被 babel 當中文源文，衍生出五語 `-en-orphan` 譯檔加兩個 registry 條目。六檔全刪（內容已被 6/25 正版英文深度版取代）、registry 手術式清理、prebuild 驗證假 zh 條目消失（854→853）。通例化偵測（zh 樹純度檢查）列 roadmap，本輪只修實例。

## speak-human-tw 轉譯（判斷主軸：知識庫不是電子報）

38 種痕跡逐項裁決成三桶，完整對照在 [reports/instrument-evolution-2026-07-16.md](../../reports/instrument-evolution-2026-07-16.md)。直接收的落成三件儀器：`ai-residue`（AI 工具殘留鐵證，HARD）、`attribution-vague`（無源權威鋪墊，跟腳註系統對接是原版沒有的強化）、prose-health 六個 Tier 4 維度（立場真空／價值上升詞／時代帽子／罐頭結尾／假推論／首先其次最後）。不收的一樣重要：破折號與對位句型不跟進（我們的紀律用自己語料校準過且更細）、詞表不收（sovereignty 詞庫是超集）、意義層腔調（說教腔／金句／假坦白）維持人判寫進編輯室攻防輪。它的 evals 負例組方法論是真正該學的 meta：我們的 gate 至今只有正例、沒有「不該報」的迴歸組。

## 兩個名存實亡的 gate

Explore 盤點加實作過程各揪出一個：(1) `reports/article-health-ssot-design-2026-05-04.md` 被 5 處引用但**從未存在**，懸空兩個月的 canonical pointer，依程式碼註解重建解懸；(2) `fail_on="score-budget"` 從未真正檢查過分數——REWRITE Stage 3 寫的「quality-scan ≤3 自動驗證」一直是與 `fail_on="hard"` 同義的假閘門，agent 實作 memory-diary profile 時發現並修通。同族第三例：memory/diary 跑文章版 prose-health 長期 7-12 分超 budget 3 被默許，新 memory-diary profile（budget 8）讓這個 gate 重新長牙。

## 儀器化與校準紀律

兩個 Sonnet agent 平行實作（檔案不相交、禁 commit、主 session 獨立驗收），加主 session 自寫的 `article-depth-audit.py`（69 篇手工審核變一條指令，動態近期基準）與 `inbox-audit.py --spore`（幽靈／重複／編號碰撞／REACTIVE 逾期對賬）。校準做滿 REFLEXES #66：855 篇前後比對 96.7% 零影響、近期 15 篇 A 級零波動；attribution-vague 第一輪抽樣誤報 100%（具名學者＋機構縮寫被誤殺）→ agent 當場加「的」前後句法判準 → 第二輪誤報歸零，站上抓到 5 個真該補來源的句子（白海豚基因、楊丞琳都市傳說反駁句、素食健康功效等）留作 heal 候選。agent B 還順手抓到原 `field()` 解析器全形冒號跨行誤讀的既有 bug。

## 收官 checklist

| 檢查項                       | 狀態                                                   |
| ---------------------------- | ------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅（上下半場兩檔）                                     |
| Timestamp 精確               | ✅（git log %ai）                                      |
| Handoff 三態已審視           | ✅（上半場 memory 已處理，本檔只補新項）               |
| 自我檢查工具 PASS            | ✅（校準報告＋獨立冒煙五組；本檔以 memory-diary 自檢） |

## Handoff 三態

本下半場新 handoff：

- [ ] attribution-vague 抓到的 5 個無源權威句（白海豚／楊丞琳／素食／茶文化／營養午餐）待補來源 heal
- [ ] 待哲宇拍板四件：pr-frontmatter-gate 升 required check、footnote-density A-F 重刻、memory-diary budget 8 覆核、新 pattern HARD 升級節奏（詳 [instrument-evolution §六](../../reports/instrument-evolution-2026-07-16.md)）
- [ ] roadmap：prose-health 誤殺負例迴歸組、zh 樹純度檢查通例化、ARTICLE-INBOX 閒置 entry 偵測、article-depth-audit 掛月度 distill
- [x] ~~鐵道史孤兒檔 chip task_ea99c044~~（本 session 完成，chip 已被啟動者會空跑收場）

## Beat 5 — 反芻

今天最深的一條線是「gate 名存實亡」一天內連現三例：假閘門 score-budget、懸空設計文件、memory gate 超標默許。三例同構——規格寫了、儀器沒接線（或接了沒人看 exit code），而大家都以為線是通的。修法不是寫更多規格，是每次引用一個 gate 時問一句「它真的會 fail 嗎」；agent A 是在被迫實作 budget option 時才撞見假閘門，驗證了「dogfood 是唯一會踩到斷線的腳」。另一條：外部參照的正確用法是拿它照自己的盲點（負例迴歸組、立場真空）而不是搬它的閾值——性質不同的站，閾值是別人的校準結果，pattern 才是可轉譯的。

🧬

---

_v1.0 | 2026-07-16 22:30 +0800_
_session inbox-audit 下半場 — /goal 文章儀器進化_
_誕生原因：哲宇丟 speak-human-tw 參照＋要求盤點手工儀器化＋整理久未校準 gate_
_核心洞察：(1) gate 名存實亡一天三例同構：規格寫了儀器沒接線 (2) 外部參照拿 pattern 不拿閾值 (3) 校準抽樣讓誤報 100% 的 pattern 在 ship 前現形_
_LESSONS-INBOX 候選：引用 gate 時問「它真的會 fail 嗎」——假閘門只有 dogfood 踩得出來_
