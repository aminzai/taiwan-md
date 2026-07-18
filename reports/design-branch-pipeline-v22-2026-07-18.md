# 設計報告：BRANCH-PIPELINE v2.1 → v2.2 深度進化（Mode 4 第二次執行）

> session：2026-07-18-111730-inbox-skill
> 觸發：哲宇 `/twmd-evolve 完整深度思考進化BRANCH-PIPELINE.md`——EVOLVE Mode 4 誕生後一小時內的第二次調用
> 證據底座：同 session 剛跑完的「台灣建築」broad-theme dogfood（4 平行 agents / 30 候選 / 10 entries append），全部摩擦都是一手實戰
> 姊妹報告：[design-article-inbox-evolve-mode4-2026-07-18.md](design-article-inbox-evolve-mode4-2026-07-18.md)（Mode 4 與 /twmd-article-inbox 的誕生）

---

## 〇、這次調用先抓到 Mode 4 自己的一個洞

我一小時前寫的灰區判法是「對象是既有 pipeline 自身 = Mode 3；對象是還不存在的能力 = Mode 4」。這次的對象是 BRANCH-PIPELINE 自身，但 Mode 3 的六個觸發訊號（編號膨脹／>1000 行／邊界混亂／prose 未儀器化／熟了跳步／文檔密度比）一個都沒中——BRANCH 只有 572 行、結構健康。哲宇要的是**能力深化**，判法卻會把它誤路由到 Mode 3。

**修正**：灰區判法從「對象是什麼」改為「動的是什麼」——結構重組（膨脹訊號命中）= Mode 3；能力深化（無膨脹訊號、要長新判準新 gate）= Mode 4。本報告 IMPLEMENT 一併回寫 EVOLVE-PIPELINE §Mode 4 邊界表。

## 一、THINK：dogfood 摩擦清單（今天真的發生的九件事）

| #   | 摩擦                                                                                                                           | 現行 v2.1 缺口                                                                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| 1   | 內文 grep + `head -2` 截斷，漏掉 `Geography/大稻埕.md` 專篇，A agent 因此把迪化街街屋提成 P0，aggregate 靠檔名層 `find` 才攔下 | baseline check 與 dedup 只寫 `grep`，沒寫「檔名層 find 優先、內文層 grep 補充」          |
| 2   | DONE-LOG dedup 命中 路思義×2/歌劇院×2，看 context 才知道全是城市文順帶提及、非專篇                                             | dedup 三查沒寫「命中必看 context，count 單獨會誤判」                                     |
| 3   | Bash cwd 靜默跳回主 repo，主 session 用相對路徑 verify agent 落檔撲空，差點誤判 agent 幻覺                                     | claim verify gate 沒提絕對路徑（LESSONS shell-cwd-silent-reset 已有此雷，pipeline 未接） |
| 4   | Agent B 自發 grep `_PEOPLE-ROADMAP.md`（200 人計畫）當人物門檻證據，判斷品質全場最高                                           | Stage 3 人物知名度門檻 gate 工具欄寫「manual」，沒指向這個現成 SSOT                      |
| 5   | A、D 兩個互不知情的 agent 收斂到同一題（古蹟保存運動）——最硬的缺口訊號                                                         | Stage 5 aggregate 沒有「多 agent 獨立收斂 → 升權」判準                                   |
| 6   | B 與 C 對「建築師過不過 People 門檻」判斷相反，主 session 裁決後記進 master report                                             | Stage 5 沒有「agent 間衝突要裁決並留痕」的要求                                           |
| 7   | 30 提示只收 10 條，被拒的 20 條若不留痕，下次 branch 同 theme 會原樣再推薦一遍（重複推薦病，跟 inbox 幽靈同型）                | master report 結構沒有「候選處置總表：進 INBOX／次波 pool／不做＋理由」                  |
| 8   | 主 session 把 baseline 已存在清單逐條餵進四個 agent prompt，agents 才沒重複研究                                                | Stage 4 prompt 鐵律只寫「已存在只 mention」，沒寫主 session 有義務附清單                 |
| 9   | priority 公式（重要性×0.3+…）從 v1.0 至今沒有一次被真的算過，today 也是 qualitative 判 P0/P1/P2                                | 公式以「規則」的姿態存在但不可執行（「規則要能執行才算規則」）                           |

## 二、DIVERGE

### 整體形狀

| 方案             | 內容                             | 判定                                                                        |
| ---------------- | -------------------------------- | --------------------------------------------------------------------------- |
| A 小步 v2.2      | 九條摩擦縫進現有 stage，結構不動 | ✅ Mode 3 觸發訊號零命中，572 行健康；摩擦全是縫隙不是結構病                |
| B 大改 v3.0 拆檔 | Mode 3 式 7-stage 重組           | ✗ 無病重組 = over-engineering（CONTRACT rollback 教訓：儀器化自己也會過度） |

### 摩擦 9（公式）的處置

| 方案                                                      | 判定                                                                    |
| --------------------------------------------------------- | ----------------------------------------------------------------------- |
| a 強制 master report 附每候選計分表                       | ✗ 會變 performative compliance——填表不等於判斷（#63 rollback 同型風險） |
| b 公式降級為思考框架 + 唯一可量化的「連結密度」升必附數字 | ✅ 承認實際用法，把可執行的部分抓緊、不可執行的部分誠實降級             |

## 三、定案（v2.2 變更清單）

1. **Stage 1 baseline check 升雙層**：檔名層 `find -name "*{kw}*"` 優先 + 內文層 grep 補充；禁 `| head -N` 截斷判讀
2. **Stage 5 dedup 三查補「看 context」**：命中必讀前後文判「專篇 vs 順帶提及」
3. **Agent claim verify gate 補絕對路徑**：verify 指令一律絕對路徑（cross-ref LESSONS shell-cwd-silent-reset-cross-worktree）
4. **Stage 3 人物門檻 gate 接 `_PEOPLE-ROADMAP.md`**：工具欄從 manual 改「grep 200 人計畫 + manual 裁決」
5. **Stage 5 aggregate 判準兩條**：多 agent 獨立收斂 → priority 升權；agent 間判斷衝突 → 主 session 裁決 + master report 留痕
6. **Master report 結構加「候選處置總表」**：進 INBOX／次波 pool／不做＋理由 三類，防同 theme 重複推薦
7. **Stage 4 prompt 鐵律 +2**：主 session 必附 baseline 已存在清單；人物類 sub-theme 必要求誠實門檻評估
8. **Priority 公式段加一句**：公式是思考框架非計算義務；唯一必附數字的是連結密度
9. **EVOLVE-PIPELINE §Mode 4 邊界**：灰區判法改「結構重組 vs 能力深化」

## 四、驗收

- (a) v2.2 全部變更落在既有 section，行數增幅 < 40 行（保持薄）
- (b) Hard Gate Inventory 與 prose 同步（表就是 audit 面，不留只改一邊的漂移）
- (c) 姊妹報告 §後記 回填 dogfood 結果

## 五、後記（實作後回填，同日）

- 九條定案全部落地：BRANCH-PIPELINE v2.2（frontmatter + H1 + Hard Gate Inventory 四列 + Stage 3 公式誠實化 + Stage 4 prompt 鐵律 9 條 + Stage 5 aggregate 判準與候選處置總表 + 版本 footer）；EVOLVE-PIPELINE §Mode 4 灰區判法改「結構重組 vs 能力深化」（v3.6.1）
- 驗收 (a)：v2.2 淨增約 35 行，維持薄；(b) Hard Gate 表與 prose 同步改，無單邊漂移；(c) 姊妹報告 §後記 已回填
- 未儀器化的殘留：「禁 `| head -N` 截斷判讀」目前是 prose 規則，若再犯 ≥2 次考慮升 lint（本次不預先造——儀器化自己也會 over-engineer）

🧬
