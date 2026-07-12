# /semiont 週報區 — 規劃與實作報告

> 2026-07-12 · session 2026-07-12-142709-weekly-audience（同 session 第三個 goal）
> 觸發：哲宇 /goal「我們有可能在 semiont 頁面放一個週報區嗎？幫我完整規劃放 report 然後完整實作」
> 前情：同日稍早週報已升 v4.2 寄給整個共生圈（[weekly-report-audience-upgrade-2026-07-12.md](weekly-report-audience-upgrade-2026-07-12.md)）

---

## 1. 為什麼可行、為什麼該做

答案是可行，而且路已經鋪好一半。十份週報本來就以 markdown 落在 `reports/weekly/`（公開 repo 內），而 /semiont 的覺醒日記早就示範了完整的「repo 內 markdown → 網站頁面」管線：`src/lib/semiont-diary.ts` 在 build 時直接讀 `docs/semiont/diary/*.md`、用 marked 渲染、餵給 list + entry 兩層頁面。週報區就是同一個模式換個資料夾。

該做的理由跟今天早上把週報寄給共生圈是同一條：週報是 Semiont 每週的自我體檢與反芻，收件的 20 人看得到，但 unreachable 的 30 人、未來的貢獻者、路過的研究者都看不到。放上 /semiont 之後，信箱寄達的與寄不達的人看的是同一份東西，信裡也能放一條「在網頁上讀」的連結（今天升級的可點連結機制剛好用上）。

## 2. 設計

### 路由與資料流

| 層       | 內容                                                                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 資料源   | `reports/weekly/*.md`（10 份起，每週日 +1；`dossier/` 子目錄是內部切菜檔，天然排除——readdir 只收 `.md` 檔案）                              |
| Parser   | 新生 `src/lib/semiont-weekly.ts`：date（檔名）、W 週數、title（H1）、excerpt、bodyHtml、h2 目錄、字數。模式照抄 `semiont-diary.ts`         |
| 列表頁   | `/semiont/weekly/` — 卡片列表，最新在上（`src/pages/semiont/weekly/index.astro` + `semiont-weekly-list.template.astro`）                   |
| 內文頁   | `/semiont/weekly/[date]` — 完整渲染 + h2 目錄 + 上一週/下一週導覽（`[slug].astro` + `semiont-weekly-entry.template.astro`）                |
| 首頁區塊 | `/semiont` landing 新增 📮 週報區：最新一期卡片 + 「全部週報」連結，掛在覺醒日記區旁（`semiont-landing.template.astro`）                   |
| i18n     | `src/i18n/semiont.ts` 加 `semiont.weekly.*` 字串（該檔現有的每個語言 block 都補），頁面本身 zh-TW canonical（跟 diary 同款，不產多語路由） |

### 相對連結改寫（跟 email 同一課）

週報 markdown 裡有相對 repo 連結（如 `../evolution-roadmap-2026-07-10.md`），直接渲染上網站會 404——這正是今天 email 升級修過的問題，網頁層要再修一次。規則同款：`http(s)/mailto/#` 不動；`/` 開頭視為站內路徑不動；其餘相對路徑以 `reports/weekly/` 為基準 normalize 後改寫成 `https://github.com/frank890417/taiwan-md/blob/main/…`。

### 信裡的「在網頁上讀」連結

`send-email-resend.py` 加 `--web-url` 參數：在信件 markdown 最上方插一行「🌐 在網頁上讀這份週報」。WEEKLY-REPORT-PIPELINE Stage 5b 指令帶上 `--web-url "https://taiwan.md/semiont/weekly/${DATE}"`。信與網頁從此互相指向。

### 不做的事（邊界）

- **dossier 不上網**：它是給 Semiont 自己的內部 briefing（pipeline 鐵律 8 本來就禁止當週報送人）。
- **不做多語**：週報是中文反芻文，跟 diary 同樣 zh-TW canonical；en landing 只會看到區塊標題的英文字串與連結。
- **不改週報文體**：網頁區是投影層，週報怎麼寫仍由 WEEKLY-REPORT-PIPELINE Stage 3 管。
- **隱私不變**：週報本來就只含 login 與人數、零 email 地址（v4.2 隱私三不），上網不新增暴露面。

## 3. 實作紀錄

新增五檔、修改四檔（站體五檔 + i18n 由 Sonnet 分身依規格建置，主 session 驗收；email 與 pipeline 由主 session 親手）：

| 檔案                                                              | 角色                                                                             |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `src/lib/semiont-weekly.ts`（新，279 行）                         | parser：讀檔、W 週數（ISO-8601）、excerpt、h2 目錄、相對連結改寫、字數           |
| `src/pages/semiont/weekly/index.astro` + `[slug].astro`（新）     | 路由薄殼，鏡射 diary（prev=較新、next=較舊）                                     |
| `src/templates/semiont-weekly-list.template.astro`（新，118 行）  | 列表：統計行 + 排序 + 「從第一份開始讀」+ 卡片（週數徽章/標題/摘要）             |
| `src/templates/semiont-weekly-entry.template.astro`（新，332 行） | 內文：麵包屑 + meta 行 + h2 目錄 + 上/下週導覽                                   |
| `src/templates/semiont-landing.template.astro`（+59 行）          | landing 📮 週報區：最新一期卡片 + 說明 + 「看全部 {count} 份週報」               |
| `src/i18n/semiont.ts`（+18 鍵值）                                 | `semiont.weekly.*` 三鍵 × 六語言 block 全補                                      |
| `scripts/tools/send-email-resend.py`（+`--web-url`）              | 信件頂部「🌐 在網頁上讀這份週報」（轉換器無 blockquote 分支，用粗體段落+分隔線） |
| `docs/pipelines/WEEKLY-REPORT-PIPELINE.md`（v4.3）                | Stage 5b 指令帶 `--web-url`，信與網頁互相指向                                    |

分身自主的四個合理判斷（驗收通過）：列表不做按日分組（週報一天一份）；`makeExcerpt` 加 `_底線斜體_` 剝除（週報開頭慣用底線斜體，不剝每張卡片都帶底線）；`semiont.weekly.notice` 不掛 zh-TW-only 開關（它是六語都該看的區塊說明，不是道歉字串）；不新開 component 檔（inline markup，守住檔案清單邊界）。

## 4. 驗證紀錄

分身自測 + 主 session 獨立重驗（dev server localhost:4322）雙層：

- **Parser**：10 份全解析；W 週數與 Python `datetime.isocalendar()` 十份全對齊（W19～W28）；`../evolution-roadmap-2026-07-10.md` 改寫成精確的 GitHub blob 網址；h2 目錄十章全抓到。
- **頁面**：`/semiont/weekly` 與 `/semiont/weekly/2026-07-12` HTTP 200、視覺截圖確認（列表統計行「10 份 · 127,580 字」、W28 卡片；內文頁 W28 徽章 + 14,366 字 meta + 十章目錄側欄）；最舊一份（2026-05-09）邊界導覽正確。
- **Landing 週報區**：「寄給共生圈的週報」+「看全部 10 份週報」都渲染（DOM 驗證 opacity 1 / visible；日記卡片維持 3 張不受影響）。截圖層有個插曲：landing 捲動後 Browser pane 截圖回傳空白，DOM 檢查證實是截圖合成器的怪癖不是頁面 bug——elementFromPoint 在該捲動位置命中日記卡。
- **Console 0 錯誤；mobile 375px 無水平溢出。**
- **信件端**：`--web-url` dry-run 驗證頂部連結 href 正確、無 `>` 殘字。
- **i18n**：`grep -c "semiont.weekly"` = 18 = 3 鍵 × 6 語言。

一個順手發現（不修）：2026-06-01 那份週報內文自稱 W22，ISO 週數實為 W23——歷史文件的作者筆誤，按「時間是結構」修補協議保留原文，週數徽章以 parser 的 ISO 計算為準。

---

_v1.0 | 2026-07-12 — 哲宇 /goal 觸發；規劃 + 實作 + 驗證同 session_
