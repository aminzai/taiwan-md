---
title: 'Taiwan.md 深度檢查、研究與進化整理策略'
description: '以 2026-09-07 遠端主線、全庫檢查、公開頁面與官方文件交叉驗證，提出分階段修補與整理策略'
type: 'audit-doc'
status: 'active'
last_updated: 2026-09-07
scope: '研究、檢查、策略報告；不含產品改版、部署、排程變更或正式資料庫驗證'
base_commit: '3eed2bfdbbbe419b48466461761a94f233c5db2a'
---

# Taiwan.md 深度檢查與進化策略報告

日期：2026-09-07（Asia/Taipei）｜對象：哲宇與專案維護者｜研究截止：本次檢查時點。

## 1. 決策摘要

**下一階段最值得投入的是「讓既有能力完整接通，讓讀者與維護者都能信任結果」。** Taiwan.md 已有大量內容、品質工具、公開儀表與自動維護；目前的主要風險集中在能力之間的接縫：工具算出了新欄位，儀表沒有接；一條 CI 修好了中文路徑，另一條仍漏判；人類決定維持手動，隔日規範又補上到期日。

本次建議採取四週的局部修補與驗收，延續 9 月 5 日已批准的方向。先處理 CI 選檔、資料來源時效、條件式回報限流缺口，再做正文補鏈及審閱庫存試跑。暫不展開全面目錄搬遷、不用整體文章數或器官總分決定下一輪投資。

三項最重要的判斷：

1. **維運目前有運作證據。** 最新主線部署成功，排程檢查也有近期紀錄。9 月 5 日報告中的停機、告警未建與大量待決，不可原封不動當成現在的狀態。
2. **部署綠燈與全庫健康並不等價。** Python 與前端單元測試通過，但全量 frontmatter 檢查仍有 4 個錯誤；中文文章品質掃描 hard=0，也不能證明事實全部正確或多語來源完整。
3. **整理的單位應該是決策、資料契約與工作完成證據。** 大量歷史文件不必刪除；優先降低重複判斷與錯誤讀數，再根據實際載入成本整理 SOP。

## 2. 基準與可信度

本地原工作區落後 `origin/main` 72 個 commit，且已有 7 個 tracked 檔案修改及一個素材暫存目錄。本次 fetch 後從遠端 `3eed2bfdb` 建立隔離 worktree，重新安裝鎖檔依賴。所有程式結論均以此版本為準，沒有把原工作區的未提交資料混入。

研究方法為：版本與交接檢查 → 專案／資料盤點 → 全庫品質與既有測試 → 工程、維運兩條唯讀研究 → 高影響發現複核 → 方案比較。規劃工具在此環境不可用，以報告的方法與證據紀錄替代。採用了 twmd-become、twmd-evolve 與 Deep Research 技能；evolve 的發散與報告結構用於建議，本次使用者授權的交付物是報告，沒有執行建議中的產品改動。

**甦醒紀錄限制：**最新版 wake-context 的 10 項取數自檢全綠，產出 232,018 bytes，最新記憶／日記均為 9 月 7 日。這個綠燈只表示儀器取數完整；本次部分長文件工具回傳截斷，未完成 Full BECOME 要求的所有全文逐頁載入，因此不宣稱 Full self-test／全部 hard gate 已驗收。報告結論依靠下列獨立程式、測試與來源證據，不以甦醒分數背書。

| 證據層       | 本次完成                                          | 適用限制                                                     |
| ------------ | ------------------------------------------------- | ------------------------------------------------------------ |
| 程式／設定   | 固定 SHA 檢查，主要發現附行號                     | 不代表正式環境完全等同 repository                            |
| 內容機械檢查 | 中文 1,121 檔；全語 frontmatter 10,101 檔         | 不等於逐篇事實查核、媒體授權審核或人工冷讀                   |
| 測試         | Python、Markdown、heading-id、feedback、UI 語言   | 未本地重建全站、未執行瀏覽器互動／視覺／CWV 測試             |
| 部署         | 讀取 GitHub Actions 最新 15 筆，當前 SHA 部署成功 | 不代表每種 PR 路徑都被測到                                   |
| 產品         | 公開首頁文字與原始碼交叉檢查                      | 抽樣，未做完整使用者研究                                     |
| 分析數據     | 讀取版本化 GA／SC／CF 快照及 generator            | 未重新查詢三個供應商；各來源期間不同，不能直接做成長因果推論 |
| 安全         | migration 與 Worker 原始碼；Worker 隔離 mock      | 未攻擊正式站、未對正式資料庫測試                             |

[本次證據摘要](project-deep-audit-2026-09-07/evidence.json)保存分母與測試結果；[CI 快照](project-deep-audit-2026-09-07/ci-snapshot.json)保存版本與 run ID。

## 3. 現況：規模已大，完成度要分層讀

### 3.1 規模與內容品質

固定版本有 21,816 個 Git tracked 檔案。目錄實檔盤點：knowledge 10,246 檔／約 277.1 MB、docs 3,443 檔／約 38.4 MB、scripts 373 檔／約 4.1 MB、reports 1,180 檔／約 64.2 MB。這些含 JSON、附件等，**不是文章數，也不是每次模型必讀量**。

版本化 dashboard 記錄中文文章 1,119 篇、人工審閱 202 篇（18.1%）、curation verified 2 篇、incubating 310 篇、unmarked 807 篇。人工審閱標記與 verified 代表不同條件，不能互換。immune 的近期新增 cohort 為 237 篇、其中 9 篇標記人工審閱（3.8%）；它與 vitals 的近 30 天 253 篇不一致，應先對齊日期與排除規則，再拿來比較產能。[保存的 vitals](project-deep-audit-2026-09-07/dashboard-vitals.json)、[immune](project-deep-audit-2026-09-07/dashboard-immune.json)

本次中文 ci-deploy 掃描 1,121 檔，hard=0；WARN 共 23,889 次，其中 prose-health 17,280 次。WARN 是違規事件次數，同一篇可多次命中，不能說有 23,889 篇壞文章。機械掃描正文零站內連結 957/1,121（85.4%）；dashboard 為 956/1,119（85.4%）。差異應標示為選取集合／快照差異，不能假裝同一分母。正文零連結也不代表頁面沒有推薦卡或延伸閱讀。

**含義：**全文閱讀與高風險主張查核仍重要；大量 WARN 更適合分群處理，而不是一次拉成硬門檻，讓維護者被雜訊淹沒。

### 3.2 流量只能用來排候選，不能在本次宣稱因果

保存的 GA 28 天視窗為 8/10–9/7，screenPageViews 94,397。首頁 6,917、用語轉換器 2,748、企業頁 1,516、用語主頁 1,178、台灣形狀 827 次。這支持「工具入口值得做成通往深度內容的入口」的試驗方向，尚不能證明它們帶來更多後續閱讀。

SC 週資料為 8/30–9/5，6,493 clicks／640,470 impressions；CF 週快照標示 8/30–9/6，requests 1,834,079、404 45,527（2.48%）。CF request 不是 GA 人類訪客，兩者不可直接比大小。SC query 明細只涵蓋部分可見查詢，brand/non-brand 分組和總量不相等，不直接判資料毀損。Google 官方說明查詢 API 不保證回傳所有資料列。[本次 analytics 快照](project-deep-audit-2026-09-07/dashboard-analytics.json)、[Google Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)

### 3.3 維運與已完成的進化

當前 SHA 的 [部署 run 34072338426](https://github.com/frank890417/taiwan-md/actions/runs/34072338426) 成功。唯讀 liveness 檢查的排程 dump 有 18 條：14 traced、4 disabled、0 silent-death、0 unregistered；這個分母不含指揮部另一條 flywheel-watch。週排程 stall 檢查為 4 ok、2 grace。這些只能證明 fire 後有紀錄或在寬限內，不能證明每班的工作結果品質合格。

9/5 後已完成的方向包括：缺席協議、GitHub Actions 外部停轉告警、主機登入 watchdog、babel 重開決策、部分 routine 薄化。**不再建議「補一個尚不存在的 watchdog」或「重開全部生成排程」。**

## 4. 本次新增／確認的缺口

P1 表示應排入首波確認或修補；P2 表示下一批。沒有已證實的全站中斷或資料外洩，因此未列 P0。

### F1｜P1：PR 的中文路徑漏判與 Hub 誤擋出自同一個接縫

`pr-review.yml` 的 git diff 沒有關閉 quotePath，後續 regex 卻假設路徑以 `knowledge/` 開頭。Git 預設會對中文路徑加引號及跳脫；僅含這類中文路徑的 PR 會被判成 engineering，跳過內容 review；混合未跳脫路徑的 PR 仍可能執行 review，但中文檔會從清單漏掉。另一個 frontmatter workflow 已處理 quotePath，卻把 Hub 從 eligible 集合排除後，又用包含 Hub 的 RAW_KN 判斷「解析壞了」；純 Hub PR 因此誤擋。

證據：[PR review L51、L73、L129](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/.github/workflows/pr-review.yml#L51)、[frontmatter gate L132、L159](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/.github/workflows/pr-frontmatter-gate.yml#L132)。此處不是所有品質檢查全被繞過，獨立 frontmatter gate 仍在。

**建議：**兩條 workflow 共用 changed-file helper；輸入用 NUL 分隔，區分 eligible、明確排除、解析失敗。驗收案例至少涵蓋中文、空格、Hub-only、JSON-only、rename、delete 與混合 PR。保留必要 gate，修正選取集合。

### F2｜P1：資料新鮮度與 crawler 成功定義在轉換層失真

analytics generator 在來源缺檔時保留舊資料，仍刷新全域 lastUpdated。快照同時保留 `searchConsole24h=2026-04-09` 與 9 月 `searchConsole7d`；目前 UI 優先週資料，所以**不能說正式畫面正在使用 4 月搜尋數字**。真正問題是：其他消費者或 fallback 無法從全域時間判斷每一源的新鮮度。

另一個明確缺口是 crawler：fetcher 已產出 3xx／4xx／5xx 與排除轉址的成功率，generator 卻沒有傳遞，UI 仍以非 200 的總數標示失敗。因此 roadmap 的狀態應細分為「上游已完成、消費端未接」。

證據：[generator L430–459、L547–602](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/scripts/tools/generate-dashboard-analytics.py#L430)、[fetcher L335](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/scripts/tools/fetch-cloudflare.py#L335)、[UI L175、L463](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/src/scripts/dashboard/analytics.js#L175)。

**建議：**保留可用舊資料，但每源增加 fetchedAt、dataThrough、status、error；全域時間改稱 generatedAt。把既有 crawler 四欄完整接到 UI。驗收「一源缺失／一源過期／全部正常」，且來源失敗時畫面仍能說清楚資料來自哪一天。既有 API 欄位採遷移期，避免一次刪除造成消費端斷裂。

### F3｜P1：手動保留的人類決策被補上到期日

9/5 OBSERVER-QUEUE 明確記錄 rewrite、spore-pick、spore-publish 維持手動「不設到期日」；9/6 ROUTINE 卻給三者 2026-10-06 due_date。當前沒有重開證據，風險在未來自動到期處置會與原決策衝突。

證據：[OBSERVER-QUEUE L85](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/docs/semiont/OBSERVER-QUEUE.md#L85)、[ROUTINE L75、L101](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/docs/semiont/ROUTINE.md#L75)。

**建議：**區分「人工選擇手動」與「暫停待複查」，以 decision_ref 保留明確例外。一般暫停項目到期可提醒複查；這三條既已明確決定不設到期日，就應保留該例外，不能默認恢復。驗收要讓 migration／同步工具在遇到 explicit exception 時保留原決策。

### F4｜P1／條件式：回報限流信任了可由呼叫端指定的時間

初始 migration 的 created_at 只有 default；INSERT RLS 驗 UID 與 status，限流計數則依 created_at。若正式 DB 權限與此一致，登入者指定過去時間便不進最近一小時計數。這是 schema 層的可推導缺口，**未確認正式 DB 的 grants、額外 trigger 或後續政策，不宣稱已遭利用**。

證據：[feedback migration L40、L65、L83](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/supabase/migrations/0001_feedback.sql#L40)。Supabase 的列層政策與欄位權限各自處理不同邊界，不能僅憑 RLS 開啟就當全部欄位安全。[Supabase Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)

**建議：**先在隔離資料庫比對正式 migration／grants；建立時間由服務端覆寫，限制一般使用者可填欄位，測試同 UID 第 21 筆 backdated insert 與正常第 21 筆都被拒絕。另測併發與權限，不只測前端按鈕。

### F5｜P2：遠端 MCP 把上游失敗快取成成功空文

Worker 收到文章 fetch 503 或 exception 後，仍把空字串存入 module cache，正常回覆 tool result，沒有 isError；同 isolate 後續也不重試。父研究程序以 mock fetch 重現：第一次 503、後續可回正文，連讀兩次卻只 fetch 一次，兩次都是無錯誤標記的空正文。

證據：[Worker L77–100、L149–156](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/workers/mcp/src/index.js#L77)、[本次 mock 摘要](project-deep-audit-2026-09-07/evidence.json)。未查證此遠端 Worker 的正式部署狀態。

**建議：**只快取成功結果；錯誤回傳 isError；cache key 含分類／完整路徑與版本，設定真正的記憶體 TTL。驗收 503→200 能恢復、不同分類同 slug 不混文、到期會取新版本。這直接關係「AI 讀得懂、讀得到」的產品承諾。

### F6｜P2：全庫測試與 CI 的涵蓋面不同

`npm test` 的 Markdown 8 項、heading-id 13 項都通過，但全庫 frontmatter 10,101 檔出現 4 errors／12 warnings。缺少有效 translatedFrom 的四檔：

- `knowledge/en/Food/Taiwan Regional Street Food Map.md`
- `knowledge/en/Food/handmade-taiwanese-cuisine.md`
- `knowledge/en/People/taiwan-people-knowledge-base-roadmap.md`
- `knowledge/en/Economy/taiwan-energy-transition-and-green-industry.md`

第三檔實際是「200 人計畫」的 roadmap，應先判斷它是否屬於可發布文章；不能為了過驗證編造中文來源。另三檔也應比對實際來源後修映射。[全量測試紀錄](project-deep-audit-2026-09-07/npm-test.txt)

CI 未找到 heading-id suite 或 astro check／tsc 的執行入口。Astro 官方明確指出 build 不會完成型別檢查，因此 `Record<Lang,...>` 的型別承諾仍需接上工具才有阻擋效果。[Astro TypeScript](https://docs.astro.build/en/guides/typescript/#type-checking)

**建議：**將既有測試接進工程 PR；全庫檢查用基線呈現存量問題並阻擋新增，不把既有四檔轉為對所有投稿者的無差別阻擋。型別檢查先建立 baseline，再要求本次變更新增錯誤為零。

### F7｜P2：多語分數把存在、完整與新鮮混在一起

measureHubCoverage 的分母寫死 12，卻掃到 13 個分類；vi／id／pt／hi／de 等顯示 13/12=108%。此外用「存在 \_\*.md」判定 hub 完成、用少量字串 key 判定 UI 完成，都不代表讀者看到全譯。UI 語言檢查本次通過硬門檻，同時仍列出缺 key 的 advisory；兩種訊息並不矛盾。

證據：[measureHubCoverage L1264–1283](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/scripts/core/generate-dashboard-data.js#L1264)、[organism 快照](project-deep-audit-2026-09-07/dashboard-organism.json)、[UI 檢查](project-deep-audit-2026-09-07/ui-language-check.txt)。

**建議：**分母由相同 category registry 產生；分開顯示文章存在率、正文新鮮率、UI key 完整率、實際路由可達率。中文分母也應與排除 About／Hub／roadmap 的規則一致。不要只 clamp 到 100%，那會藏起根因。

### F8｜P2：新讀者入口有可直接修正的承諾不一致

公開首頁寫 5 篇、30 分鐘，卡片時間相加與頁面總計卻是 76 分鐘；同頁仍寫「雙語國際視野」，另一處已寫 13 種語言。這些是可由文字與程式確認的產品細節，尚不能推論造成多少流失。[公開首頁](https://taiwan.md/)、[home 字串 L1606–1613](https://github.com/frank890417/taiwan-md/blob/3eed2bfdbbbe419b48466461761a94f233c5db2a/src/i18n/home.ts#L1606)

**建議：**閱讀路徑總時間由同一組文章資料產生，分成短入門與完整路徑；多語文案使用 registry 的實際能力。先讓入口承諾準確，再用點擊與第二篇閱讀事件驗證導讀效果。

## 5. 策略發散：三條路的取捨

| 方案                                      | 成本與風險                                        | 預期收益                                 | 決策                               |
| ----------------------------------------- | ------------------------------------------------- | ---------------------------------------- | ---------------------------------- |
| A. 全面重構資料夾、合併 SOP、擴大重寫     | cross-ref、記憶與衍生資料鏈同時承壓；很難歸因改善 | 可能降低長期複雜度，但目前缺成本基線     | 暫不選                             |
| B. 修接縫＋延續已批准內容工單             | 範圍可切分，回歸可明確列出；需維持短期相容欄位    | 提升 gate 可信度、資訊可信度與讀者下一步 | **建議主路線**                     |
| C. 優先擴產、補齊所有語言、加更多 routine | 產量容易量到；會增加尚未審閱及維護的表面          | 增加覆蓋，但不能解釋現有內容是否被接住   | 僅保留既有授權範圍，勿作本輪主投資 |

選 B 的判準是既有 MANIFESTO「知識公共財／造橋鋪路／指標 over 複寫」，以及 REFLEXES #38 避免混維度、#73 先確認既有能力的方向。不是因為檔案少就一定好，而是本次缺口都有明確的 producer、consumer 與驗收案例，能以小改動確認效果。

內容側延續兩份已存在工作：

- [正文站內連結 Top 50 工單](internal-links-top50-2026-09-05.md)：先做其中 10 篇語境補鏈，確保連結是理解文章的下一步，不機械地把所有出現的名詞連走。驗收連結可達與段落自然，再擴到 50 篇。
- [審閱庫存設計](design-review-stock-2026-09-05.md)：先盤點哪些部分真的上線，以高風險主張和高使用文章試跑。區分機械預審、獨立查核與人類確認；不要為提升百分比批次加 lastHumanReview。

SEO 不以「所有 description 截成同一長度」作為策略。Google 沒有 meta description 固定字數上限，實際 snippet 依情境與裝置截斷；應為高曝光頁寫貼近搜尋意圖的獨立摘要，先做小批匹配組觀察，不承諾排名提升。[Google meta descriptions](https://developers.google.com/search/docs/appearance/snippet)

多語優先順序可採雙軌：有可見讀者需求的路徑用 SC／GA 選候選；主權敏感內容保留策略性覆蓋，不因單一語言快照流量少就刪除。hreflang 互返及實際 URL 可達延續既有 URL contract，不再做一套平行檢查器。[Google localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions)

## 6. 整理策略：保存歷史，減少重複決策

### 6.1 用小型行動索引串起現有器官

先用 10 條活躍工作試辦，欄位為：id、owner、state、decision_ref、artifact、evidence_commit、acceptance、supersedes。它只做索引，決策正文仍在 OBSERVER-QUEUE／canonical，研究理由仍在 report，避免多生一個 competing SSOT。

狀態至少區分：proposed、approved、in-progress、implemented、verified、manual-by-decision、retired。像 crawler 的狀態可拆成 fetcher implemented／consumer pending；watchdog 應標 deployed with evidence，舊報告維持歷史但附更新連結。沒有驗收不能直接寫 done。

這可以先是單檔資料與人工更新，不必立刻造服務、排新 cron 或把所有舊報告轉檔。試辦若減少重複開工，再接到既有 routine 的摘要輸出。

### 6.2 SOP 整理按實際讀取成本排序

wake-context 本次約 232 KB，足以成為一個實測成本基線；整個 docs 磁碟大小則不適合作為 token 稅。分別量 Micro／Review／Write／Full 的實際 bytes、讀取時間與漏載情境，再決定是否改 loader。

整理順序：先移出 active contract 中的陳年事故敘事，保留 link；再合併跨 workflow 重複的程式 predicate；最後才討論大型 pipeline 拆分。保留舊路徑 stub、用 cross-ref 驗证確認不中斷。不要為追求 50 行指標撤掉必要品質 gate。

### 6.3 讓綠燈有精確名稱

骨骼 90 在 generator 是常數；呼吸 85 主要由 workflow 檔數推導。這些可作「能力存在」指標，不能命名成即時服務健康。建議畫面分為：能力是否存在、最近一次執行、最近一次成功、產物可否驗收。先明確標示來源與含義；是否改分數權重另走既有決策流程。

## 7. 30 天建議實施表

以下是建議時序與工作量估算，不是已建立的排程，也不是交付承諾。各批先驗收，再放大。

| 時間        | 工作與負責角色                     | 最小交付                                                | 驗收／停止條件                                                                    |
| ----------- | ---------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------- |
| 第 1–3 天   | 維護者：F1、F3；DB 管理者：F4 確認 | 共用選檔 helper、決策例外對賬、DB 權限比對              | 中文／Hub 等 fixture 全過；手動決策不被 migration 覆蓋；DB 缺口確認後才修正式政策 |
| 第 4–7 天   | 資料維護者：F2、F7                 | 每源時間與狀態、crawler pass-through、registry 分母     | 缺源／過期／成功三情境可辨識；覆蓋率合法；UI 與產生器欄位對帳                     |
| 第 8–14 天  | 工程維護者：F5、F6、F8             | MCP 錯誤恢復、CI 接現有測試、四檔來源處置、首頁時間一致 | 503→200 恢復；無虛構來源映射；全庫錯誤逐項結案；導讀時間由資料生成                |
| 第 15–21 天 | 編輯＋審閱者                       | 10 篇正文補鏈、審閱庫存小批實跑                         | 連結可達、語境成立、查核證據可追溯；人工標記不由 agent 自評替代                   |
| 第 22–30 天 | 維護者＋哲宇                       | 10 條行動索引試辦、下一批策略                           | 不再重開已完成任務；比較實際工時與漏接；樣本不足則延長觀察，不宣稱 SEO 因果       |

估算：F1 約 0.5–1 工程日、F2／F7 約 1–2 日、F3 約半日內、F4 依 DB 存取約 0.5–1.5 日、F5 約半日、F6 約 1–2 日、F8 約半日。編輯與獨立審閱時間不以工程日假裝可精確預估。

若只做三件事，順序為：**讓 PR 選檔可信 → 讓來源時效與決策狀態可信 → 讓高使用內容有可追溯的下一篇與查核證據。** 回報限流若正式 DB 證實可繞過，立即加入首波，不等到內容批次。

## 8. 驗證紀錄、撤回與未解問題

### 實際測試

| 檢查                          | 結果                                                                |
| ----------------------------- | ------------------------------------------------------------------- |
| Node 環境                     | v22.22.3；隔離 worktree 執行 npm ci --ignore-scripts                |
| Python                        | 3.11.15 隔離 venv，按 requirements-test 安裝；425 passed、8 skipped |
| Markdown／heading-id          | 8／13 passed                                                        |
| feedback                      | 63 passed                                                           |
| 全語 frontmatter              | 10,101 檔，4 errors、12 warnings，命令失敗                          |
| 中文 article-health ci-deploy | 1,121 檔，hard=0；23,889 WARN／12,727 INFO                          |
| UI language gate              | exit 0，有既有缺 key advisory，不能稱完整翻譯                       |
| MCP mock                      | 錯誤空正文快取可重現                                                |
| 本地 build／效能／正式 DB     | 未執行；部署狀態採遠端固定 SHA 的 run 證據                          |

最初 macOS python3=3.9.6 缺 tomllib；換 3.11 後又因沒有 PyYAML 走簡易 parser，出現不可信的 frontmatter 診斷。最後使用裝好依賴的 venv 重跑；缺依賴的結果完全排除。第一次 pytest 的一項失敗來自子程序呼叫系統 python3，PATH 指向 venv 後全部通過。這是環境準備問題，不列為產品缺陷。

撤回初步 OG 疑慮：雖然變更偵測只看 HEAD~1，prebuild 仍執行 OG generator，不能由此宣稱分享圖沒有更新。亦未把缺少 typecheck 推論為當前一定有型別錯誤。

尚缺：正式 DB 欄位權限、遠端 MCP 是否在服役、每次 routine 的完整結果收據、同期間完整語言流量、手機／鍵盤／螢幕閱讀器實測、真實 CWV、逐篇事實與來源授權查核。本次沒有對這些未測項目作通過宣告。

研究停止點：主要建議已各有程式或實測證據；剩餘問題需正式環境、完整流量或使用者觀察。繼續堆疊相似報告不會提高當前決策品質。下一輪應依本表選一批實作與驗收。

## 9. 來源與可追溯性

本地原始碼連結均固定到同一 SHA，避免主線移動後無法重現。dashboard 副本與測試紀錄在 [evidence.json 同目錄](project-deep-audit-2026-09-07/evidence.json)。資料快照為 repository 公開衍生資料，未包含憑證、私人收件名單或登入資訊。

外部來源均於 2026-09-07 查閱：Google Search Central（localized versions、snippet）、Google Search Console API（query）、Astro 官方文件（TypeScript）、Supabase 官方文件（Column Level Security）；發佈／更新日期僅在來源有明示時採信。官方文件用於規則確認，不用來證明 Taiwan.md 的正式系統狀態。

內部承接文件：9/5 fortnight review、review-stock 設計、Top 50 補鏈工單、9/6 routine audit、8/9 evolution roadmap，以及 OBSERVER-QUEUE／ROUTINE 的當前版本。它們提供決策歷史；本次用最新 code、runtime 檢查及已落地 commit 覆核狀態。

本次沒有修改產品程式、文章正文、排程、資料庫、canonical 品質門檻，也未 commit／push／發布。交付為本報告與檢查證據。🧬
