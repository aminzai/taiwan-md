---
title: '深度檢查修復實作與驗收紀錄'
description: '承接 F1–F8 與內容、行動索引建議；逐項記錄實作、驗收及正式環境狀態'
type: 'design-doc'
status: 'active'
last_updated: 2026-09-07
---

# 深度檢查修復實作

哲宇 2026-09-07 授權「全部完整升級、修復與紀錄」。基準 origin/main `3eed2bfdb`，採用[研究報告](project-deep-audit-2026-09-07.md)方案 B：修補既有能力的接縫，保留歷史與既有介面。方案 A 大規模搬遷與方案 C 擴產都無法直接解決本次可重現缺陷，因此不採用。

## 實作與驗收清單

| 項目 | 實作                                                | 驗收                                                       | 狀態                              |
| ---- | --------------------------------------------------- | ---------------------------------------------------------- | --------------------------------- |
| F1   | 共用 NUL 安全 PR 選檔與 JSON 清單；Hub 明確排除     | 中文、空白、引號、Hub、JSON、rename、delete、fork fallback | 已實作，回歸通過                  |
| F2   | 每源時效狀態、保留舊資料標示、crawler 欄位接通      | 缺失、過期、成功與 UI 契約                                 | 已實作，舊資料明示狀態            |
| F3   | 手動決策例外資料、規範與儀器對賬                    | 三條維持手動且無到期日                                     | 三條例外一致，其餘漂移另列        |
| F4   | 伺服端時間與併發安全限流 migration                  | 隔離 DB 回溯時間／第 21 筆／權限／併發                     | 隔離 DB 通過；正式待登入          |
| F5   | MCP 成功快取、TTL、完整路徑 key、錯誤回覆           | 503→200、到期、同 slug 不混文                              | 正式已部署並驗證                  |
| F6   | 來源映射修正、規劃文歸位、CI 測試與三個工程型別清零 | 全庫與變更驗證、既有測試進 CI                              | 10,123 篇欄位零警告，型別零錯誤   |
| F7   | registry 分母與多維度量測                           | 比率合法、完整率與存在率分離                               | 已實作，字串存在與品質分離        |
| F8   | 動態閱讀時間、短／完整路徑、多語描述                | 讀者可見時間一致、語言正確、瀏覽器檢查                     | 已實作，手機互動通過              |
| 內容 | Top 50 先 10 篇語境補鏈、審閱小批                   | 連結可達；實質改寫撤下舊版人審標記                         | 10 篇補鏈／查核，音樂篇媒體仍不足 |
| 整理 | 10 條行動索引、量測甦醒載入成本、精確綠燈名稱       | 指標可回溯、無 competing SSOT                              | 已落檔，未冒稱 Full 甦醒          |

## 交付紀律

在隔離 worktree 實作，各批只提交本批檔案。研究報告先提交，實作後補驗收紀錄、memory、diary。修復正式 DB 與遠端 Worker 前先確認可用帳戶及實際部署；沒有驗證的狀態保留為未驗證，不以本地測試代替正式環境驗收。跨 30 天的流量改善屬後續觀察，不能在本次假造結果。

## 技術債與設計交付

主站 Astro 6 與 Harvest UI Astro 5 升級至 7.3.1，保留 unified Markdown 處理器、外連及 wikilink 行為，明確維持 HTML 壓縮。Harvest UI 移除淘汰的 Tailwind 整合，改接 PostCSS。四份 npm 專案（主站、Harvest UI、Harvest backend、MCP）各有鎖檔，此次依賴稽核皆為零已知漏洞。主站原稽核為 13 個，其中 1 critical、10 high。

主站原有 1,285 個型別錯誤已修至 0，Harvest UI 與 backend 各自型別檢查也為 0。修復多語字典鍵型別、Astro Props、RSS、Markdown renderer、D3 與 fallback 資料契約。沒有用忽略註解或舊錯誤基線抵銷。新增 CI 持續跑契約、Python、三專案型別、Harvest UI 建置、依賴稽核及 PostgreSQL 限流測試。

[Island Lines 設計規格](design-island-lines-2026-09-07.md)與[56 枚圖示總覽](island-lines-catalogue-2026-09-07.html)共同交付。分類卡片移除重複色票與失效圖片分支。圖示從一份來源產生，使用同源 SVG，靜態介面在建置時轉換，動態儀表板在既有渲染流程轉換。文章正文、引文、國旗及身分記號保留。Tailwind 限制掃描實際站台來源，避免把歷史報告的程式範例編入正式 CSS。

分析文字增加 HTML 跳脫、拒絕腳本／外站網址，損壞百分比編碼不再中斷頁面。人工智慧文章圖說網址以等價百分比編碼避開 Prettier 的底線誤判，連續兩次格式化仍保留目標。三個舊英文檔名改為小寫 kebab-case 並保留舊址轉址。日本語躲避球文章移除殘留生成指令，補回既有正文對應標題、描述與標籤。

## 驗收證據（2026-09-07）

| 契約                | 實測                                                                                                |
| ------------------- | --------------------------------------------------------------------------------------------------- |
| 主站型別            | 667 個檔案，0 errors                                                                                |
| Python              | 428 passed，8 skipped；跳過不視為通過                                                               |
| JS 契約             | Markdown、heading id、PR 路徑、分母、圖示、分析輸入、MCP 與 feedback 全通過                         |
| 全庫 frontmatter    | 10,123 篇，0 errors、0 warnings                                                                     |
| Harvest UI          | 32 檔 0 errors、0 warnings；3 hints；3 頁建置通過                                                   |
| Feedback DB         | PostgreSQL 17 隔離測試：25 併發僅 20 筆成功、21 筆拒絕、偽造時間／管理欄位拒絕、service role 可處理 |
| 第一輪 Astro 7 全站 | 14,150 頁，12m 9s；嚴格 URL 契約通過，公告死址 0、別名洩漏 0                                        |
| UI                  | 桌面 1280px、手機 390px 無水平溢出；首頁 143 個 SVG；短程 28 分鐘／完整 76 分鐘可展開               |
| 最終站台            | 14,151 頁，12m 59s；36,969 個公告 URL 零死址、零別名洩漏、零 sitemap 缺席                           |

原始稽核仍保留於[研究報告](project-deep-audit-2026-09-07.md)。本次測試輸出整理在同名證據資料夾；初次建置的 CSS 警告已另作來源範圍修復，最終建置已確認沒有 CSS minification 警告，初次紀錄仍保留。

## 正式環境與限制

MCP 已部署到 `mcp.taiwan.md`，版本 `cd4ee91e-fac5-458b-a8a1-1fb7cff8db37`。正式 initialize 與「夜市」搜尋均回傳 HTTP 200，搜尋有完整分類路徑。對應程式提交 `c8fde9496`。

Supabase migration 0005 尚未套用正式資料庫：管理頁停在登入畫面，已請哲宇完成登入。服務角色金鑰不提供 schema 管理權限，因此沒有拿本地測試冒充正式已修。主站部署將在最終建置與提交後另外記錄。

這次清除的是已辨識並實作驗收的工程缺陷，不能宣稱所有未知技術債與全站文章品質問題都已歸零。已知剩餘事項：原住民歌手文章缺足量適切授權圖片、既有譯文 wikilink、Threads 舊文文風、其他 routine prompt 快照漂移，以及原分工的考試專題。它們在本輪 memory 留下來源與下一步。三條手動例外已對齊，但其他 routine 狀態仍須重新讀真正 scheduler 才能判定。

語言字串存在率不等於翻譯品質，能力分數不等於健康，流量與留存的改善也需要後續真實觀測。本輪沒有虛造 30 天效果。

## 官方升級依據

- [Astro 7 migration](https://docs.astro.build/en/guides/upgrade-to/v7/)：Markdown processor、Vite 與編譯行為。
- [Astro releases](https://github.com/withastro/astro/releases)：升級版本來源。
- [Sharp 0.35.4](https://sharp.pixelplumbing.com/changelog/v0.35.4)：影像依賴修補。
- [Tailwind source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files)：明確控制掃描範圍。
- [Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/)：dry-run、部署與正式驗證。

最後提交檢查另抓到小寫 resources 舊分類漏掃：驗證器改按磁碟實際分類目錄遍歷，納入 23 篇原本漏掃檔案，總計 10,123 篇仍為零錯誤、零警告。新增隔離路徑回歸測試。

開發伺服器在全庫格式化與資料同步後觸及 Node 預設約 4 GiB heap 而退出。`npm run dev` 補上 8 GiB 預設並尊重既有 NODE_OPTIONS；這是大站開發容量設定，未據此宣稱排除長期記憶體洩漏。最終視覺驗收使用建置產物預覽，避免把熱更新狀態當成正式產物。

遠端 content review 的四項誤報已修正：既有維護者精選以 PR base 比對保留，新設精選與無法讀取基準仍拒絕；小寫 resources 舊分類納入。隔離 Git 回歸測試驗證原有精選、新設精選、缺基準與大小寫目錄。另修正 Bash 變數緊鄰全形括號的展開錯誤。修正後遠端 review 通過。

最終靜態 UI 驗收：英文 1280px、阿拉伯文 RTL 390px、美食 390px 與中文首頁 390px 均無水平溢出。中文首頁 161 個 SVG，完整閱讀路徑 76 分鐘可展開。瀏覽器尺寸已還原。實際輸出見證據目錄 `static-ui-checks.json` 與 `final-build-result.log`。

交付 PR：[#1682](https://github.com/frank890417/taiwan-md/pull/1682)。主站待 CI 全數通過後合併部署，不能把 PR 建置視為正式上線。哲宇指定下一階段為 rewrite-pipeline 互動引導工具；以其提供的四篇近期文章與黃魚鴞、張懸與安溥兩篇早期文章為對照，另立研究，不以工程分數代表文章好壞。
