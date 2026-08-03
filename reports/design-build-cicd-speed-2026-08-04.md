---
title: 'Build / CI / CD 加速深度研究 2026-08-04'
description: 'EVOLVE Mode 4 設計報告：push→上線 9.3 分鐘的完整拆帳（166 run/7 天實測）、三重健檢掃描與逐檔 cp 等重複工診斷、三波加速方案（管線瘦身 → runner A/B → 部署平台）與 trade-off。'
type: 'roadmap'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-08-04
last_session: '2026-08-04-build-cicd-research'
related:
  - 'build-pipeline-audit-findings-2026-06-10.md'
  - 'git-info-prebuild-2026-06-13.md'
---

# Build / CI / CD 加速深度研究 — 2026-08-04

> 哲宇的問題：「build / ci / cd 流程還有沒有可能更快」。
> 走 EVOLVE Mode 4（THINK → DIVERGE → REPORT），本檔是 REPORT。實作等拍板，
> 除了明確標「自主權內」的第一波項目。
>
> 前情：這是第二輪手術。第一輪是 2026-06-10 審計（[findings](build-pipeline-audit-findings-2026-06-10.md)）
> ＋ 6-13 手術（[EVO-A4](git-info-prebuild-2026-06-13.md)），Build step 從 1,125s 降到 122s。
> 兩個月後的今天它回到 264s——不是退化，是身體長大了（頁數 8.4k → 12.9k、語言 6 → 12）。

---

## 一、現況量測（全部來自 CI log 與 GitHub API，2026-08-02〜08-03 窗口）

### push → 上線的完整拆帳

成功 run 中位數 **559s（9.3 分鐘）**，p90 573s（n=12）。以 run 30832814503（583s）逐段：

| 段                       | 秒數    | 備註                                               |
| ------------------------ | ------- | -------------------------------------------------- |
| queue + setup            | ~5      |                                                    |
| Checkout                 | 38      | `fetch-depth: 0` 全歷史（pack ~330MiB）            |
| npm ci                   | 31      | npm cache 有中，剩 node_modules 解壓本體           |
| frontmatter + 健檢 step  | 21      | 含 article-health 全站掃描 **第 1 遍**（17s）      |
| caches + Playwright deps | ~20     | OG 增量正常（本次只產 1 張）                       |
| **Build step**           | **264** | ↓ 下表拆開                                         |
| Upload artifact          | 73      | **每次全量上傳 1.14GB**（GitHub Pages 無增量部署） |
| deploy job               | 90      | actions/deploy-pages 固定開銷                      |

### Build step 264s 內部

| 段          | 秒數 | 內容                                                                     |
| ----------- | ---- | ------------------------------------------------------------------------ |
| prebuild    | 82   | sync 26 ＋ status 11 ＋ run-p 關鍵路徑 41 ＋ latest/redirects/aliases ~4 |
| astro build | 178  | vite 14 ＋ 靜態生成 161（12,895 頁）                                     |
| postbuild   | 4    | check-url-contract（六月的 verify-internal-links 64s 已不在 CI 鏈上 ✓）  |

run-p 41s 的關鍵路徑整條是 `prebuild:dashboard` 串行鏈：
article-health baseline **第 2 遍**（17s）→ `generate-dashboard-immune.py`（18s，**內部又跑一次
`article-health.py --all` = 第 3 遍**）→ data/forks/alerts/newsroom/status（~6s）。

astro 靜態生成的頁群拆帳（per-page 加總 548s CPU，wall 161s，有效平行度 3.4 / 4 vCPU——
`concurrency: 8` 已到頂，CPU 飽和）：

| 頁群             | 頁數   | CPU 加總 | 平均  | 佔比 |
| ---------------- | ------ | -------- | ----- | ---- |
| 文章頁（12 語）  | 10,047 | 438s     | 44ms  | 80%  |
| 其他站頁         | 284    | 36s      | 127ms | 7%   |
| terminology 條目 | 2,284  | 32s      | 14ms  | 6%   |
| raw md endpoints | 3,463  | 27s      | 8ms   | 5%   |
| semiont/diary    | 477    | 15s      | 31ms  | 3%   |

文章頁 44ms/頁是六月手術（554ms → 44ms，-92%）的成果仍然在——這輪**沒有** render 層的病，
剩的是頁數與 CPU 上限。

### 頻率與浪費（7 天）

- deploy run **166 個（~24/天）**；抽樣 100 個：47 成功 / 50 取消 / 3 失敗。
- 取消是 `cancel-in-progress` 對消（babel 批次 push 密集期），浪費 141 分鐘 runner 算力——
  公開 repo 免費，不是錢的問題，但代表**一半的 build 是白跑的**。
- 巴別塔脈搏 commit **從不單獨觸發 deploy**（0/100，都被批次 push 一起帶走）✓——
  6 月擔心的「儀器自己灌 deploy」不存在。
- dist：21,561 檔（13,204 HTML）；大頭 og-images 252MB、terminology 頁 243MB、
  article-images 131MB、carousel 68MB。

### 兩個月的成長軌跡（給「為什麼又慢回來」一個誠實答案）

| 時點       | Build step | 頁數   | 語言 | 每頁全含成本 |
| ---------- | ---------- | ------ | ---- | ------------ |
| 2026-06-10 | 1,125s     | 8,436  | 6    | 133ms        |
| 2026-06-13 | 122s       | ~8,500 | 6    | 14ms         |
| 2026-08-03 | 264s       | 12,895 | 12   | 22ms         |

頁數 +52%、每頁 +57%（新視覺模組、語意 related、12 語 hreflang 面）。斜率會繼續：
vi/id/pt/hi/ar/ru 六個新語系補完後文章頁還會再 +2k 頁以上。**單點手術會被成長吃掉，
這輪要挑的是結構位置。**

---

## 二、診斷：時間花在哪四類

1. **重複工（純浪費，~55s/build）**：article-health 全站掃三遍（17+17+15s）；
   sync.sh 用 bash 迴圈逐檔 `cp`（10k+ 次 process spawn，26s）。
2. **固定稅（~232s/build）**：checkout 全歷史 38s、npm ci 31s、artifact 全量上傳 73s、
   deploy job 90s。前兩項有便宜解；後兩項是 **GitHub Pages 架構稅**（無增量部署，
   1.14GB 每次重傳）。
3. **成長驅動（178s 且持續漲）**：astro 靜態生成，CPU 飽和在 4 vCPU。
4. **頻率（不影響單次延遲）**：24 deploy/天、50% 對消。行為正確（後推蓋前推），
   單純是活動量大。

---

## 三、方案發散與 trade-off

### 方案 A：管線瘦身（自主權內，工程半天）

| 項                                                                                                                            | 預估省   | 風險                                                            |
| ----------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------- |
| A1 健檢三掃合一：CI step 加 `--baseline-out`，`prebuild:dashboard` 與 immune 改吃現成 baseline JSON                           | **-32s** | 低。immune 需加 `--baseline-in` 參數（讀檔取代重掃）            |
| A2 sync.sh 逐檔 cp → `rsync -a --delete`（保留 resources/ 分流語意）                                                          | **-22s** | 低。本機 `npm run dev` 啟動同賺 ~20s（每天所有 session 都受益） |
| A4 node_modules 整包 cache（key = lock hash）                                                                                 | **-23s** | 低。lock 變更時 fallback npm ci，六月審計已點名                 |
| A5 `prebuild:buildperf`（30 次 serial gh api）移出 CI（`CI=true` 時 skip，交 data-refresh routine）＋ status 三支 python 平行 | **-8s**  | 低                                                              |

小計 **-85s**：job 583 → ~500s，Build 264 → ~210s。

### 方案 B：runner 與 astro 本體

| 項                                                                                                                                   | 預估省       | 風險                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------- |
| B1 ARM runner 重試（`ubuntu-24.04-arm`，Node/Sharp 官方稱 1.3-1.7×）                                                                 | **-40〜70s** | 中。6/01 因 pool 不穩回退，已兩個月；一行改回，帶觀察條款（連 5 綠轉正、紅一次即 hotfix 回退，同上次劇本） |
| B2 raw md endpoints（3,463 頁）移出 astro，prebuild 直接寫進 dist                                                                    | -8s          | 低，但收益小，列順手項                                                                                     |
| B3 文章頁 render 再 profile                                                                                                          | 邊際低       | 44ms/頁已是瘦過的數字，不建議這輪動                                                                        |
| A3 checkout `filter: blob:none`（歸這組一起 A/B）：三個吃 git log 的 prebuild 步驟已驗證只用 commit graph + tree diff，blobless 可行 | **-15〜20s** | 低-中。需一次 CI 真環境驗證 restore-mtime ratio guard 仍過                                                 |

### 方案 C：部署平台（🔒 命中 §自主權邊界：基建＋經費，等哲宇）

現況 GitHub Pages 的結構稅 = upload 73s ＋ deploy 90s = **163s，且隨 dist 長大**。

| 項                                                                                                     | 預估省         | 代價與風險                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C1 遷 Cloudflare Workers 靜態資產（wrangler 增量上傳，只傳變更檔；babel 批次典型只動幾十頁）           | **-120〜140s** | **dist 21,561 檔超過免費層 20,000 檔上限**，需 Workers Paid（US$5/月，上限 100,000 檔）[^cf1][^cf2]。CF 已是站前 DNS/CDN，origin 切換對讀者透明；redirects 現制（meta-refresh stub）不受影響。遷移工程 1-2 天＋雙軌驗證期。經費＋基建 → 哲宇拍板 |
| C2 保 GH Pages，大資產出走（og-images 252MB ＋ article-images 131MB ＋ carousel 68MB → R2/自有資產域） | -30s           | og:image 絕對網址要改（SEO 面）、多一條資產發佈鏈。收益比 C1 小、工程不小——只在不想動平台時才考慮                                                                                                                                                |

[^cf1]: [Workers static assets — Billing and limitations](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/)（20,000 free / 100,000 paid，單檔 25MiB）

[^cf2]: [Changelog 2025-09-02 — Increased static asset limits](https://developers.cloudflare.com/changelog/2025-09-02-increased-static-asset-limits/)；[Pages limits](https://developers.cloudflare.com/pages/platform/limits) 同為 20k/100k

### 方案 D：deploy 頻率治理 — **建議不動**

cancel-in-progress 是正確設計；pulse 不單獨觸發；50% 對消的成本是免費 runner 分鐘。
曾考慮 paths-ignore（memory/reports-only push 跳過 deploy），但 docs/semiont 有站上投影
（/semiont、newsroom），白名單易錯難維護，省的又只是免費算力。不做。

---

## 四、定案建議：三波

```
第一波（自主權內，半天工程）      A1 + A2 + A4 + A5           583s → ~500s
第二波（兩個一行 A/B，各觀察一次） A3 blobless + B1 ARM        ~500s → ~390-420s（6.5-7 分）
第三波（🔒 哲宇拍板）             C1 Workers 增量部署          ~390s → ~250-270s（4.2-4.5 分）
```

第三波做完，push→上線從 9.3 分鐘到 ~4.3 分鐘（-54%），且 babel 高頻期的 1.14GB×24/天
上傳流量降到 MB 級。長期天花板（另案）：astro 無原生增量 build，頁數破 2 萬後
真正的結構解是增量生成或部署單元拆分，屆時再開設計輪。

## 五、驗收判準

- 第一波：Build step ≤ 215s（dashboard-build-perf.json trend 連 5 run）；
  article-health 每 build 只掃一遍（log 佐證）；本機 `npm run dev` 起動 sync 段 ≤ 6s。
- 第二波：A/B 各觀察 5 個成功 run，job 中位數下降且零新 failure；ARM 紅一次即回退。
- 第三波：push→上線 ≤ 4.5 分鐘；增量 deploy 上傳量 ≤ 50MB（典型 babel 批次）。

## 六、風險與回退

全部方案可單獨回退（各自一個 commit / 一行 config）。ARM 有 6/01 前科，觀察條款寫死。
C1 遷移期間 GH Pages 與 Workers 雙軌並跑，DNS 切換是最後一步、可即時切回。

## 七、誠實備註

- 本機 prebuild 逐步計時**沒有跑**：量測時 babel 渦流 6 個 writer 在本機活動
  （check-parallel-actor ACTOR_BUSY），避免搶檔案。所有數字取自 CI log 與 GitHub API，
  是 ground truth 而非本機模擬。
- dashboard-build-perf 儀器（六月時自己壞掉那顆）現在數字正確（22ms/頁 ✓），
  本報告與它互相印證。

---

_作者：Taiwan.md 🧬（2026-08-04 Full mode session，EVOLVE Mode 4 REPORT 相）_
_方法：gh API run/job/step 級拆帳 ＋ CI log 時間戳解析 ＋ 7 天 166 run 統計 ＋ 兩份歷史審計對讀_

---

## 後記：第一＋第二波執行與驗收（2026-08-04 01:26〜02:26，同日）

哲宇拍板「完整執行一波跟測試驗收 1+2」。五個 CI run 的實測全紀錄如下，
含一次歸因錯誤與更正——照實記，這段比成功的部分更有教學價值。

### 驗收終態（run 30840499884，ARM＋blobless＋全部優化）

| 段                  | 基線     | 終態              | Δ         | 靠什麼                                          |
| ------------------- | -------- | ----------------- | --------- | ----------------------------------------------- |
| Checkout            | 38s      | 22s               | -16s      | `filter: blob:none`                             |
| npm ci              | 31s      | 1s（cache hit）   | -30s      | node_modules 整包 cache（key 含 arch）          |
| Build step          | 264s     | 230s              | -34s      | sync 批次化＋健檢三掃合一＋ARM astro            |
| — prebuild sync     | 26s      | ~4s               | -22s      | 逐檔 cp → 每目錄一次多檔 cp                     |
| — astro 靜態生成    | 177s     | 155s              | -22s      | ARM（Node workload 穩定快 ~10%）                |
| Upload artifact     | 73s      | 58s               | -15s      | ARM                                             |
| build job 合計      | ~446s    | **~339s**         | **-107s** |                                                 |
| deploy job          | 90s      | 81-133s（波動）   | ~0        | GitHub Pages 端，五個 run 實測 81/107/111/133/281 |

push→上線：基線中位 559s → 終態約 **420-470s（-20% 上下）**，deploy job 的
平台端波動（±50s）現在是最大的不可控項——這正是方案 C 的論據。

### 歸因錯誤與更正（值得留給下一輪的部分）

第二波把 ARM 與 blobless 同 run 上線，prebuild 從 52s 掉到 84/122s，當時
歸給「ARM 上 python 慢」並回退 ARM。下一個 x86＋blobless 的 run prebuild
同樣 81s，歸因被推翻：真兇是 `status.py` 對每條 stale 翻譯跑
`git diff --shortstat`（要讀 blob 內容），blobless 下變成上千次逐 blob 網路
lazy fetch，84/122/81 的大變異正是網路特徵。修法 `LANG_SYNC_SKIP_DIFFSTAT`
（CI 設 1；diffSummary 是資訊欄，判定與 dashboard 都不吃）。同型第二例是
`og-rename-sync` 的 `-M` 相似度偵測（12s lazy fetch，改 `-M100%` 歸零）。
教訓：**兩個變因同 run 上線，慢的那筆帳會記到比較顯眼的變因頭上**——
7/30「兩個都算對的缺口帶到一個錯的故事」的重演，已進 LESSONS-INBOX。

### 驗收判準對照（§五）

- Build step ≤ 215s：**未全達**（230s）。殘餘缺口在 sync→sweep 段：ARM＋
  blobless 58s vs x86＋full-clone 37s，還有 ~20s 來源未定（候選：殘餘
  lazy fetch 消費者或 run-p 併發下的 ARM python），交 dashboard-build-perf
  trend 觀察，flag_slow 會叫。
- 健檢每 build 只掃一遍 prebuild 側：**達成**（immune reuse 訊息 ×5 run）；
  CI gate step 刻意保留獨立（severity 語意不同）。
- 本機 dev sync ≤ 6s：**達成**（29.3 → 5.0s，parity 三層全同）。
- ARM 觀察條款：**進行中**，3/5 連綠（run 2/3/5），SIGTERM(143) 零次；
  紅一次即回退，條款寫在 deploy.yml 註解。

### 流程自省

status.py 的 flag 修補犯了「驗證指令失敗但 ship 已出」：本機驗證跟 commit
之間不是 && 鏈，驗證炸了（測試方法問題：/tmp 下 import 不到同目錄模組）
ship 照跑，事後才在 repo 內補驗通過。CI 的 prebuild 鏈是最後接住的外部尺。
下次的正確形：驗證與 ship 寫成同一條 && 鏈，驗證不過 ship 物理上不會跑。

### 第三波維持待決

C1（Workers 增量部署，需 Workers Paid US$5/月）仍 🔒 等哲宇——本輪驗收後
deploy job 波動（81-281s）取代 Upload 成為最大單段不可控項，C1 的預期收益
從 -120s 上修為 -120〜180s。
