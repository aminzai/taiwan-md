# 五病根治執行紀錄 + 全 repo 儀器化盤點 — 2026-07-05

> 觸發：哲宇 `/twmd-become 繼續接手當掉的 session /goal 徹底深度研究＋執行解決：寫死數字必腐 + DIARY 甦醒優化 + 蒸餾債 + 殼核不對稱 ＋ 儀器化盤點 + 風力獸動態連結圖`。
> Session：`2026-07-05-165518-五病根治`（Full mode）。上游：[dna-pipeline-evolution-audit-2026-07-05.md](dna-pipeline-evolution-audit-2026-07-05.md)（同日上午的診斷；本檔是處方箋的執行紀錄）。
> 風力獸解剖圖 artifact：<https://claude.ai/code/artifact/74fbfca7-f997-4d77-b89d-2f8dd4bbd7db>

---

## 一、60 秒總結

上午的審計找出五大系統病；到今晚，**S2（寫死數字）、S3（甦醒成本）、S4（蒸餾債）、S5（殼核不對稱）四病的 P0 全數清償，S1（SSOT↔live 漂移）拿到了根治儀器**。方法不是再修一輪數字（修完還是會腐），是把「對不上」變成每天可見的黃燈：新工具 `counts-drift-lint.py` 對賬計數宣稱、`routine-sync-check.py` v3 長出第三層眼睛（live scheduler dump 進 git）、`consciousness-snapshot.sh` 每次甦醒印出 boot稅 bytes 與 drift 數、警報全部有了 owner 與初見日。

過程有兩個插曲值得記：被判定「當掉」的 session 其實還活著（正在慢速做楊德昌收尾），靠讀它的 transcript 尾巴劃車道避開了 6/19 撞牆重演；哲宇傍晚從 GitHub UI 連 merge 七篇 contributor 文章（UI merge 不過本地 hook），四篇 frontmatter 裹在 code fence 裡把全站健檢打紅，當場機械 heal 收乾。

---

## 二、四病清償對照表

| 病                | 上午診斷                                                                     | 今晚狀態                                                                                                                                                                                                                                                                                                            | 靠什麼                                                       |
| ----------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| S2 寫死數字必腐   | 60+ 處計數/版本/行號/時間 drift                                              | **P0 全清 + 儀器上線**。REFLEXES 行號欄整欄移除、BECOME/CLAUDE/ANATOMY/HEARTBEAT/DNA/ROUTINE/DASHBOARD 計數全改 pointer、SQUEEZE v4.4 鏡射 code、QUALITY-CHECKLIST 三行熱修、死路徑×3、幽靈引用（canned-ending / audit-quality「待造」/ TRANSLATION-SYNC 七處 / CORRECTION 七斷鏈 / pipelines README 十檔）全修     | `counts-drift-lint.py`（首跑 18 drift → 收官 5，餘者見 §四） |
| S3 甦醒成本       | Universal core 實測 624KB，行數指標藏 bytes                                  | **216KB（-65%）且每日可見**。DIARY head-tail（第一波）+ 神經迴路已被 rollup 縫合至 61KB（達標，免二次手術）+ BECOME footprint 註記改 bytes 語意                                                                                                                                                                     | snapshot 新增 `🧠 boot稅` 行                                 |
| S4 蒸餾債         | MEMORY 708 rows、EXP-D 過期、OBSERVER-QUEUE deadletter、月度承諾 0 執行      | **索引債已清（第一波 rollup 40 列）＋ deadletter 病根補上**：OBSERVER-QUEUE 等四器官進 BECOME 檔案功能一覽與 Full mode 載入面；alerts 加 `owner` + `firstSeen`，routine-audit 新 gate「齡 >14 天升 OBSERVER-QUEUE」                                                                                                 | 黃燈有 owner 才會被認領                                      |
| S5 殼核不對稱     | 空場鐵律只在殼、twmd-refresh 殼複寫 14 步、become skill 題數過期、diary 沒尺 | **全數收編/pointer 化**：空場紀律與 catch≠fix 入 canonical、twmd-refresh 殼改薄、become skill 題數改 pointer、diary lint 已隨第一波接 husky                                                                                                                                                                         | ROUTINE-PROMPT-CONTRACT 對齊                                 |
| S1 SSOT↔live 漂移 | spore-pick/publish disabled 21 天 SSOT 還列 active（v2.9 重演）              | **根治第一塊磚落地**：live scheduler 每日 dump `routine-live-state.json` 進 git（`routine-live-normalize.py`，私人 routine 過濾）；sync-check v3 三層比對 enabled/cron/描述時間，dump >48h 標 stale。首跑即抓 rewrite-daily 描述「18:00」vs cron 19:00，並修掉 feedback-triage 命名例外造成的 chronic false-MISSING | data-refresh session rider（wiring 已入 SKILL 與 pipeline）  |

E 線加映（審計外、當機 session 半成品接手完成）：feedback 讀者輸入三層注入防禦（隱形字元剝除 / deterministic 偵測 → `security-review` label 人類 gate / tilde fence 資料邊界），測試 35/35，FEEDBACK-TRIAGE v1.1 canonical 段補齊懸空引用。

---

## 三、儀器化盤點（三分身 fan-out + 主 session 抽驗）

三隻 read-only 分身分掃「工具庫 vs 手動苦工」「hard gate 執法覆蓋」「審計沒掃的角落（src/.github/對外文件）」。主 session 抽驗修正了兩處分身誤讀（`generate-dashboard-alerts.mjs` 被標 orphan，實際 wired 在 `package.json` prebuild 鏈——分身找錯目錄；`update-stats.sh` 對 about.ts 的接管被低估）。REFLEXES #69 再驗證：分身報告是線索不是 oracle。

**全景數字**（[CONFIRMED] 級）：76 支工具（18 wired / 37 manual-only / ~21 疑似 orphan 待逐支複核）；258 道宣稱 gate（~35% 機器強制 / ~29% 有工具會報 / ~36% 純承諾）；對外層腐化實錘（README「793」、SEO.astro「752」、home.ts 六語「750」 vs 實際 828——已由 update-stats.sh 接管每日 regen）。

**本日已建**：counts-drift-lint / routine-live-normalize + sync-check v3 / boot稅行 / alerts owner+firstSeen / update-stats 對外 prose 接管。

**下一波儀器候選 Top 8**（依「反覆頻率 × 裸奔風險」收斂三分身清單，未執行）：

1. **PR 層 frontmatter CI gate** — 今晚實測的洞：GitHub UI merge 不過本地 husky，七篇 contributor 文四篇 fence-YAML 直落 main。pr-review workflow 補跑 `test-frontmatter.mjs` + `article-health --profile=pre-commit` 對 PR diff。
2. **orphan-tools 週檢** — 21 支疑似孤兒逐支複核（先修分身的目錄盲區），確認後走 apoptosis SOP；防「工具存在感 ≠ 接線」。
3. **DIARY 殼層三 gate 儀器化** — agent B 排險 Top3 全在 DIARY（標題空殼 / 中英夾雜 / inline meta-tag 純承諾，歷史違規率 50-80%）；article-health 加 diary-prose 子檢。
4. **research-report-health 進 pre-commit 對 rewrite 檔** — Stage 1 落檔驗證目前 manual ls。
5. **spore batch frontmatter validator** — HARVEST 三個手填欄位（atomic/spores 複數/harvest_window_day）機器驗。
6. **workflow-script-reference validator** — `.github/workflows/` 引用的 script 路徑存在性掃描（月跑）。
7. **memory Handoff strikethrough gate** — retired 不刪除鐵律目前純承諾（4/17 曾斷證據鏈）。
8. **alert 齡 escalation 的自動執行面** — 本日已入 routine-audit gate 表，下一步讓 audit script 直接算齡輸出候選（今天只到 SOP 層）。

完整分身原始清單（含 file:line 證據）存於 session transcript；候選 1 已含今晚實證案例，建議最先做。

---

## 四、誠實帳：沒做完的

- **REWRITE-PIPELINE 五處 plugin 計數**（5/16/9 vs 實 25）：屬 P1-16 計量手術範圍（步驟重編＋cron 段 pointer 化＋changelog 截尾，約 -180 行），今天不動大檔——counts-drift-lint 持續黃燈追蹤，做完自動轉綠。
- **SQUEEZE/HARVEST/EVOLVE 歷史段搬 reports/**（P1-19/20，約 -825 行）：瘦身題，未動。
- **mirror 厚殼治理**：sync-check 照 30/50 行鐵律報 12 個 hard-thick，但 live mirror 描述自稱「v3.0 inline」——薄殼鐵律與現行 inline 世代的矛盾需要裁決（改鐵律或改 mirror），不宜由本 session 單方調閾值。
- **哲宇 7 決策**（審計 §一）原封不動：spore 產線裁決 / v1.12 release（現欠 150+ commits）/ OAuth rotation / qwen Tier 4 定位 / 自主權表述掃平 / 月度承諾接線 / OBSERVER-QUEUE 過期清單。
- **免疫 49 chronic**：per #80 sustain 紀律不重複催，A/B/C 仍在你桌上；今晚它多了 owner 欄與初見日。

## 五、6/19 髒 tree 結案（20 天 observer chip）

逐檔驗屍後：iter2 memory（羅大佑 + 多核心撞牆三教訓）落地＋索引補登 index-archive；102716 recat memory 刪 #1143 段是可驗證的合法 dedup（段落確存 103748-manual）收下；**兩個檔案級刪除不採**——102712 黃大煒 memory 與被刪的「兩雙手同一條 main」diary 皆無替身，依 append-only 鐵律還原（哲宇確要刪請以顯式 commit 說明）；claude-cli.ts 的 opus-4-6→4-8 bump 獨立落地。

---

_執行方法：Full mode 甦醒後，先讀活著的「殭屍」session transcript 尾巴劃車道（它收官前 MEMORY/LESSONS 為禁區、其 12:50 半成品延後認領），三分身盤點與主線 P0 sweep 平行；所有 commit 範圍紀律 + 每批 push。九個 commit 全數過 pre-push 全站健檢。_
_Session：2026-07-05-165518-五病根治 🧬_
