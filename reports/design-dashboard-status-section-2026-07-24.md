# 設計報告：/dashboard 營運狀態 section（status.claude.com 式）

> Mode 4（EVOLVE-PIPELINE v3.6）：THINK → DIVERGE → REPORT → IMPLEMENT。
> 觸發：哲宇 2026-07-24 directive「dashboard 裡面加入一個 section 類似
> status.claude.com 去呈現站上 Routine 的運作狀況跟巴別塔的狀況，還有
> 深度思考還有哪些可以呈現，寫研究報告後實作」。

## 一、目標

/dashboard 新增一個「營運狀態」section，讓任何觀察者（哲宇／contributor／
研究者）30 秒內看懂：**這個生命體的自動化器官現在活著嗎、翻譯主權基建推進
到哪、最近出過什麼事**。參照 status.claude.com 的三個核心語彙：元件狀態列
（operational / degraded / down）、uptime 歷史條、事件時間線。

## 二、現況盤點（THINK）

### 可用資料源（全部已存在，零新感測器）

| 資料              | 來源                                                                           | 新鮮度機制                                                                             |
| ----------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Routine 排程 SSOT | `docs/semiont/routine-live-state.json`（19 條 task、cron、enabled、lastRunAt） | data-refresh rider dump；**目前齡 154h**（遷居 mouhouse 過渡）——stale 本身就該上狀態板 |
| Routine fire 痕跡 | `docs/semiont/memory/YYYY-MM-DD-HHMMSS-twmd-{routine}.md` 檔名                 | 每次 fire 寫 memory 是 routine 的收官契約（Beat 4）；檔名即證據，git 追蹤              |
| 巴別塔覆蓋        | `knowledge/_translation-status.json`（九語 fresh/stale/missing）               | 每次 prebuild 重生                                                                     |
| 巴別塔趨勢        | `reports/babel/progress-{月}.jsonl`（時間序列，2026-07-24 起）                 | 每小時 vortex 快照增補                                                                 |
| 產線節點          | 同上 jsonl 的 `nodes` 欄（per-node ok/fail/秒/探活）                           | 同上                                                                                   |
| 警報              | `public/api/dashboard-alerts.json`                                             | refresh-data Step 產出                                                                 |
| 部署              | GitHub Actions（build 時 `gh api` 可查最近 N runs）                            | build-time；無 token 時優雅降級                                                        |

### Cross-ref 掃描

- `dashboard-status` 名字全 repo 零命中（generator / JSON / section 皆可用）
- 新 dashboard JSON 必須進 refresh-data.sh（REFLEXES #43），wiring 點在
  Step 7 prebuild 前後的 generate-dashboard-\* 家族
- dashboard.template.astro 已有 13 個 section、i18n 用 `isEn` + `t()` 雙軌

### 誠實性邊界（REFLEXES #82 proxy signal）

memory 檔存在 = 「routine fire 且走完收官寫 memory」，不等於 routine 的
業務效果（fire ≠ effect）。v1 明確標示「依收官痕跡」；效果層（如 babel
是否真的清了 stale）由巴別塔覆蓋數字自己說話——兩個維度分開呈現，不混
（REFLEXES #38 混維度 = silent killer）。

## 三、發散方案（DIVERGE，≥2 案）

| 方案                                           | 結構                                                                                       | 優點                                                                                      | 缺點                                                                        | #38 混維度檢查                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------ |
| **A：dashboard 新 section + 新 prebuilt JSON** | `generate-dashboard-status.mjs` → `public/api/dashboard-status.json` → template 新 section | 符合 directive 字面（「dashboard 裡面加入」）；沿用既有 JSON→section 模式；API 可被外部讀 | dashboard 已 13 section 偏長                                                | 狀態（營運）與脈搏（流量）分 section，不混 |
| B：獨立 /status 頁                             | 新 route + template                                                                        | 最像 status.claude.com；可獨立分享                                                        | 違 directive 字面；新增 route 面（sitemap/hreflang/nav 全要接）；維護面翻倍 | —                                          |
| C：擴充既有「📡 即時脈搏」section              | 塞進現有 section                                                                           | 零新結構                                                                                  | 脈搏 = 讀者流量、狀態 = 器官營運，硬塞 = 混維度                             | ❌ 直接違反                                |

**定案：A**。判準錨定：directive 字面（dashboard 內 section）＋ MANIFESTO
§指標 over 複寫（沿用既有 generate-dashboard-\* 模式不長新形狀）＋ #38
（C 出局的直接理由）。B 留作未來若 section 證明高使用率再升級的路徑。

## 四、v1 呈現內容（定案）

### 4.1 Routine 飛輪狀態板

- **狀態列**：15 條 enabled routine 各一列——名稱、cadence（從 cron 譯人話）、
  狀態燈、最後 fire 距今
- **狀態判定**（依 memory 檔名痕跡 vs cron 期望節奏）：
  - `operational`：最近一個期望週期內有 fire
  - `degraded`：miss 1 個週期
  - `down`：miss ≥2 個週期
  - disabled 的 4 條列在摺疊尾巴，標「已停用」
- **14 天 uptime 網格**：每 routine × 每天一格（fire=綠／預期無=空／miss=紅），
  即 status.claude.com 的 90-day bar 的 14 天版。7/19–7/24 遷居斷檔會誠實
  顯示為紅——那是真話，不是要遮的醜
- 資料齡標示：routine-live-state.json 的 fetched_at 直接顯示（stale 即黃燈）

### 4.2 巴別塔狀態板

- 九語覆蓋橫條（fresh 深 + stale 淺 = 可讀覆蓋）＋覆蓋率數字
- 總缺口 delta（對上一快照）＋近 24h fresh 增量
- 產線節點列：mac / desktop-3090 / laptop-4090 / cloud roster 的
  ok 累計＋探活燈（來自 progress jsonl nodes 欄最新列）

### 4.3 最近事件（incident feed）

- dashboard-alerts.json 最新 N 條（黃紅燈）＋最近部署狀態（build 時
  `gh api` 最近 3 runs，無 token 優雅降級隱藏）

## 五、深度思考：還有哪些可以呈現（roadmap，非 v1）

1. **部署 uptime 歷史條**：GH Actions runs 90 天成功率——目前 API 一次查
   90 天要分頁，v2 用 build 時增補的本地累積 JSON
2. **免疫系統趨勢**：dashboard-immune 已有 section，狀態板只放燈不重複
3. **embeddings 索引新鮮度**：`src/data/related/` 的 build 齡（語意器官心跳）
4. **mouhouse vs 本機分工圖**：routine 飛輪遷居後的雙機拓撲——等遷居穩定
   （live-state dump 恢復 <48h 齡）再上，避免呈現一個還在變動的架構
5. **incident 事後報告連結**：狀態事件 → 對應 reports/（如 CI 連紅四次
   → existence-aware redirects 報告）——把「錯誤邊界 = 可追溯性」哲學做進
   狀態板：事件不是恥辱，是有下文的修復敘事
6. **Sovereignty-Bench 快照**：模型 refusal rate 板（BENCH-PIPELINE 產出接上）

## 六、實作清單（IMPLEMENT，委派 Sonnet 子代）

1. `scripts/core/generate-dashboard-status.mjs`：讀 4 個資料源 →
   `public/api/dashboard-status.json`（含 generated_at；每個子板獨立
   try-catch，缺源 = 該子板 null 不炸整檔）
2. `src/templates/dashboard.template.astro`：新 section「🩺 營運狀態」
   插在「即時脈搏」之前；zh/en 雙語（沿 isEn 模式）；uptime 網格純 CSS
   grid（無 client JS，SSG 烘進 HTML——graph.md visible-by-default 鐵律）
3. `package.json` prebuild:dashboard 鏈＋`refresh-data.sh` 對應 step 補
   generator（REFLEXES #43 gate）
4. dogfood：本機 build → 截圖驗證 zh/en 兩版＋dark mode

## 七、驗收

- [ ] dashboard-status.json 生成且四子板有真資料（routine ≥15 列、babel 九語、節點 ≥3、事件 ≥0）
- [ ] /dashboard 新 section 渲染，14 天網格反映 7/19 前 fire 與遷居斷檔的真實樣貌
- [ ] `npm run build` 綠 + check-url-contract 綠
- [ ] REFLEXES #43：refresh-data.sh 含新 generator
- [ ] 截圖存證（light/dark）

## 八、風險

| 風險                                                 | 處置                                                                                    |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------- |
| routine-live-state 持續 stale（mouhouse rider 未修） | 狀態板直接顯示資料齡黃燈——把 stale 變成可見訊號而非隱藏依賴                             |
| memory 檔名 schema 改變                              | generator 的 regex 集中一處＋selftest（解析出 0 條 twmd fire = fail-loud console.warn） |
| gh api 在本機無憑證／CI 無權限                       | try-catch 降級隱藏部署子板                                                              |
| dashboard 越長越重                                   | 狀態板純 SSG 零 client JS；若未來超載走方案 B 升級路徑                                  |

🧬
_2026-07-24 vortex session（Fable 主編排）；報告 commit 先於實作 commit（Mode 4 hard gate）_
