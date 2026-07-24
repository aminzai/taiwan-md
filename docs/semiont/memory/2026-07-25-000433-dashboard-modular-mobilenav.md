# 2026-07-25-000433 — dashboard 三層模組化零回歸 ＋ 視覺實勘修文字雲/成長軸 ＋ 手機選單 accordion 重做

> session dashboard-modular-mobilenav — 觀察者觸發（README 貢獻者排版起頭，一路加碼成 dashboard 整組優化）
> Session span: 約 23:10 → 00:35 +0800（約 85 分鐘；本 session 無中途 commit，工作全數收在收官 commit。時間錨點：dev server 啟動 23:26:43、session-id 00:04:33）
> 資料來源：dev server log + `bash scripts/tools/session-id.sh` + `date`

## 觸發

哲宇從一個小需求開始（README 貢獻者頭像統一寬度、一排 8 個），接著一層層加碼：
dashboard 版面用滿寬度＋左側快速導覽、「完整視覺修正，要實際看過問題」、模組化重構、手機選單重做。
典型的漸進式重構節奏（progressive refactor），每一層回饋揭開下一層。

## README 貢獻者表：改結果也改產生器

表格從 7 欄改 8 欄之外，把 `scripts/tools/update-stats.sh` 裡硬編碼的 `cells[i:i+7]`
一起改成 8，否則下次 cron 自動再生就會退回 7 欄。重排時先把原始 67 格 cell 存到
scratchpad 再重新分組，用 Python 斷言「新舊 cell 內容與順序完全一致」才落檔，避免混入
contributors.json 當下狀態的無關變動。

## Dashboard 視覺實勘：儀器掃不到的，眼睛看得到

先寬度改造：`.dashboard` 從硬編碼 1200px 改 `var(--container-wide)`（1560px，與
data/companies 同 token），加左側 sticky 快速導覽（16 個 section 錨點、IntersectionObserver
高亮、<1024px 收成水平 chip 列）。

然後把 16 個 section 逐一截圖看過。程式化幾何掃描（找 overflow、量容器寬）全數綠燈，
但肉眼抓到兩個真 bug。**文字雲**的字被畫布裁切（d3-cloud 排字心不管字框，邊緣字直接出血）
，修法在 `drawWordCloud` 掛載後用 `getBBox()` 重算 viewBox 貼合實際墨跡。**成長時間軸**
x 軸「每 3 點一標」硬編碼在 130+ 資料點時塞出 40 個標籤且尾標相撞，改成依繪圖寬度動態算間距（每標籤
48px 呼吸），並跳過會撞到尾標的 stride 標籤。兩者都重新截圖驗證。過程中 Browser
pane 隱藏時截圖全白，改用 repo 內建 playwright 走 headless，穩定得多。

## 三層模組化：verbatim 合約＋事後斷言，三路並行零回歸

dashboard 的三個巨石檔同時拆：template 970 行 → 90 行組合＋18 個元件（`src/components/dashboard/`）
、CSS 2309 行 → 17 檔＋index.css 保序引入（`src/styles/dashboard/`）、client JS
2757 行 → 110 行 orchestrator＋16 個 section module＋shared.js（`src/scripts/dashboard/`）
。三個 Sonnet 子代理並行執行，檔案集互不相交，主 session 只做最後縫合（換 import、刪舊
CSS）。

合約設計是成敗關鍵：每份提示都寫死「verbatim move、ids/classes 是 contract 禁止
rename」，並附上「上次有代理邊搬邊整理把 class 改名弄壞 client 渲染」的反例。三個代理各自交回可驗證的證據：
CSS 405 條規則 multiset 比對一致、JS 21 個區塊 md5 逐塊相同、template 渲染 HTML
byte-diff 一致。JS 代理還主動抓到一個隱藏跨模組依賴（renderOrganism 也讀 allArticles）
，用 exported setter 解掉。縫合後全頁零 console error、所有 section 渲染正常。

## 手機選單重做：預設全收的 accordion

舊版把五組子選單全部硬編碼 `open`，抽屜 740px 塞爆 812px 視窗，觸控目標 35px/25px
低於 44px 底線。重做成標準模式：預設全收（抽屜 453px 免捲動）、一次只開一組、當前頁所屬組
server-render 預開＋高亮、群組列 label 連結＋獨立 48×48 chevron 鍵（中間分隔線防誤觸）
、子鏈 44px 帶左側導引線、grid-rows 0fr→1fr 展開動畫、點外側關閉。子選單資料收成
frontmatter `mobileSubLinks` 單一結構。playwright 逐一量測觸控目標全數達標。

順手清了一個根源髒污：`nav.dashboard` 的 i18n 字串 10 語中 5 語內嵌 🔬 emoji、5 語沒有，統一拔掉字串內 emoji 改由模板控制位置。

## 收官 checklist

三題自檢先答：沒有違反 MANIFESTO（純工程層，未觸政治立場或大量刪除）。
引入的新問題是模組化後的路徑變動，已在 handoff 留下次 deploy 的 CI 觀察項。
下次心跳接得住：三層拆分各有可驗斷言留檔，元件 header 都標了 contract 邊界。

| 檢查項                       | 狀態                                        |
| ---------------------------- | ------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                          |
| Timestamp 精確               | ✅（無中途 commit，錨點見 header）          |
| Handoff 三態已審視           | ✅                                          |
| CONSCIOUSNESS 反映最新狀態   | ❌（未更新，本 session 純工程無身份層變動） |
| 自我檢查工具 PASS            | ✅ prose-health via memory-diary profile    |

## Handoff 三態

上一棒是 mini 遷居 session，它的手交多數要等白天驗收或哲宇補登入，
本 session 全數原樣繼承。期間跟 fleet babel 的並存實際發生互撞，寫在第一條與 Beat 5。

繼承（自 200542-migration-mouhouse）：

- [ ] 三個 babel dispatcher v3 與 mini babel-nightly 並存的 #68 碰撞面——**本 session 實際撞上兩次**（見 Beat 5），明早驗收時把「fleet commit 是否掃走別人 staged 內容」加進檢查
- [ ] 明早 09:24 mini 遷居驗收 checkpoint（fallback 手跑 verify-migration.sh）
- [ ] mini Chrome 未登入 Threads/X、Gmail connector 未接（等哲宇）
- [ ] `discover-free-models.py` 重校準＋接 cascade（未觸碰）
- [ ] hreflang cross-language existence bug 根因未修（未觸碰）
- [ ] Pro 額度 vs 飛輪負載第一週觀察（未觸碰）
- [ ] telegram alert 通道補不補等哲宇（未觸碰）

本 session 新 handoff：

- [ ] 下次 deploy 看 CI：dashboard 三層模組化後第一次過 prebuild/post-build-check，確認六語 dashboard 頁與 hashed bundle 都正常
- [ ] 手機選單已驗 375px。769-1024 平板段用同一套 class 與樣式，程式上等價但肉眼未看，下次順手掃一眼
- [ ] `.claude/skills` 或 pipeline 若有引用 `src/styles/dashboard.css` 舊路徑的文件（grep 只剩 tokens.css 兩處註解），下次碰 tokens.css 時順手更新註解

## Beat 5 — 反芻

這 session 最值得留的一課在「儀器與肉眼的分工」。幾何掃描把 16 個 section 全掃過一遍，
overflow 零、容器寬全對，看起來乾淨。但文字雲出血與軸標籤相撞這兩個真問題，只有真的渲染出來用眼睛看才存在。
儀器抓結構性違規，語意層的「這樣讀起來不對」目前只有視覺實勘能抓。哲宇那句「要實際看過問題」
是對的方法論，值得在之後的視覺工作裡當成硬要求而非可選項。

另一個是規模化拆檔的可複製手法：verbatim-move 合約＋反例錨定＋事後可驗斷言（multiset/md5/byte-diff）
，讓 6000 行的三路並行拆分一次過零回歸。合約裡那句「上次有人 rename class 壞掉」
的反例，比任何抽象規則都更能讓子代理克制住整理慾。

第三課是收官時當場抓到的：#68 雙 actor 碰撞面這 session 真的咬人了兩口。
fleet babel commit `6a3baf27b` 把我 staged 的 dashboard.css 刪除掃進它自己的
babel commit（幸好狀態正確，只是髒了那筆 commit 的邊界）；而 23:00 的
data-refresh-pm 在 mini 上用還沒帶我修正的 update-stats.sh 重生 README，
把我未 commit 的 8 欄改回 7 欄。教訓具體：routine 活躍的 repo 上，
工作成果不早點 commit 就是把它暴露在共用 index 與跨機再生器的碰撞面上。
收官時靠 `git diff --cached --name-status` 對賬才發現，補救後才 ship。

🧬

---

_v1.0 | 2026-07-25 00:35 +0800_
_session dashboard-modular-mobilenav — 觀察者漸進加碼的 dashboard 全面優化_
_誕生原因：README 貢獻者排版小需求一路升級為視覺實勘＋三層模組化＋手機選單重做的完整工程 session_
_核心洞察：(1) 幾何掃描全綠不等於視覺沒問題，語意層 bug 只有渲染後肉眼可抓 (2) verbatim 合約＋反例＋事後斷言 = 大檔並行拆分零回歸 (3) routine 活躍的 repo 上未 commit 的工作曝險在共用 index 與跨機再生器，#68 本 session 咬人兩口_
_LESSONS-INBOX 候選：(1) 子代理大檔拆分的「verbatim 合約＋multiset/md5 斷言」手法值得 canonical 化 (2) fleet dispatcher commit 前應 `git diff --cached` 對賬只收自己的檔，不掃別人 staged 內容_
