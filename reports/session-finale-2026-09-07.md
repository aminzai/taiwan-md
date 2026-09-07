# Taiwan.md 深度升級與 Rewrite Guide 收官報告

目前狀態：第一波正式上線；Rewrite Guide PR #1684 六項 CI 通過並於 19:32:11 合併，正式部署驗證中。

2026-09-07。工程修復、工具交付及文章品質分別驗收。本輪沒有將「全部技術債已清零」作為結論。

第一波工程已合併 PR #1682，對應 a03f1900930eb08c943d4cfcc029dc3da1edba33。正式部署於 19:05 完成、19:06 線上字型驗收通過；HTTP 200、瀏覽器 SVG 圖示、短程閱讀與標題實際顯示確認。CI 建置 14,151 頁，25 分 52 秒；這是本次 runner 實測，不用舊約十分鐘的部署經驗宣布卡死。

- 工程：Astro 7 升級、主站 1,285 個型別錯誤修至 0，Harvest 前後端各自檢查。依賴安全、PR 無損選檔、來源日期／HTTP 狀態、MCP 快取、併發限流、覆蓋分母與 CI 契約皆有對應驗證。
- 視覺：56 枚原創 Island Lines，24 單位網格、1.5 線寬、共用來源。介面用專用 SVG，保留文章引文、國旗及身份符號的意思。手機路徑提供短程與完整閱讀選擇。
- 知識內容：原住民歌手條目依原始材料修訂，但沒有因此宣布全站文章已完成事實查核。

Rewrite Guide 合併提交為 `38a8e2af36d2da5c67473746bc13e8397f3a2b22`，部署 run `34117125305`。

## Rewrite 的研究與實作

使用者指定六篇是偏好樣本，不是隨機品質測量。近期稿件可追到研究查無被升成世界缺席、藍圖替正文辯護、指標壓過理解，以及改稿後沿用舊驗證。早期也使用研究代理，拆檔前已有形式全過而不好讀的紀錄，因此不能把差異單獨歸因於模型或多檔。

新工具讓 agent 取得下一任務、交材料、收具名裁決、退回重做；全文與局部 scope 分開。原稿、提交及審稿工件保存內容與 hash，檔案改變後阻擋舊裁決。不同名字及 context 聲明仍是自述，不是假造的身份認證。程式不替人判文學性，不發布文章。

EZ WAY 短節由 v1 修到 v3。編輯退件、未讀藍圖者的複讀、瀏覽器抓到兩引用變一引用，以及回退後重驗皆保存；協議審查再修了審稿依據未綁 hash 與空容器欄位漏洞。最終只到 section-draft-ready，18 次提交、39 個操作事件，六個有效裁決皆綁審稿快照。部分判讀先在同一收件回合完成再寫入狀態，事件時間不是思考耗時。

驗證：14 組協議測試、生成器 11 tests、最新全套 Python 430 passed／8 skipped、672 檔型別 0 errors、工程 contracts。工作台可展開退件；390px 無水平溢出；v3 的三個來源標籤與目的地經 DOM／畫面再驗。memory／diary 與索引已檢查。Python 原始輸出見 [python-tests.txt](rewrite-guide/python-tests.txt)。

PR #1684 手機檢查 job 共 15 分 12 秒，其中 Astro 建置 14,151 頁用了 11 分 23 秒；job 包含安裝及頁面檢查，兩者不可混用。該 job 使用 ubuntu-latest，正式部署使用 ubuntu-24.04-arm，且提交不同，不以兩次耗時做因果比較。

## 交付入口

- [研究證據](rewrite-evolution-evidence-2026-09-07.md)
- [設計與實作報告](design-rewrite-guide-2026-09-07.md)
- [工具使用協議](../docs/pipelines/REWRITE-GUIDE.md)
- [實跑與工件索引](rewrite-guide/README.md)
- [互動工作台](rewrite-guide/ezway-section/workbench-final.html)
- [局部第三版試稿](rewrite-guide/ezway-section/draft-v3.md)
- [第一波工程驗收](design-audit-upgrade-2026-09-07.md)

## 明確未完成與採用策略

Supabase migration 0005 已在隔離 PostgreSQL 驗證，正式套用仍需管理頁登入，不能宣稱正式資料庫已修復。原工作目錄的未提交資料保留，所有改動在隔離工作樹。

六篇原文章未被這次局部試跑批次覆寫。沒有真人對新稿的品味回饋，也沒有同題同材料控制實驗；不能以工具通關證明長篇全面改善。新工具可執行，暫不把所有 routine 自動切換；先用真實文章與使用者回饋校準，再決定哪些舊關卡應退出，避免兩套關卡無限疊加。

既有 handoff 的譯文 wikilink、Threads 文風、歌手圖片與 scheduler prompt drift 仍列在 memory 中，沒有靠本次工程數字將它們消帳。
