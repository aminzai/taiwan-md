# v3 瀏覽器驗收

2026-09-07，主代理透過 Codex IAB 開啟 `http://localhost:4337/rewrite-guide-preview/draft-v3.html`，來源是 draft-preview-v3.html（由 draft-v3.md 解析）。取得 AX tree、DOM 連結及畫面，確認正文為「可能出現」「提出哪些配套」版本。

連結 DOM 依序：文字 1 → S1（cntId=b1bc5147371d428590c00553ba094bd2）；文字 1 → S1；文字 2 → S2（cntId=5b7a9da7e7674b4e90e0cee314f85191）。AX tree 也呈現三個獨立 link。段落與連結可見，沒有沿用 v2 的單一連結結果。

另檢查工作台：可展開 orient 退件看到具體理由；390px viewport 下 document scrollWidth=390、六個 SVG，未水平溢出，讀完恢復 viewport。工作台匯出為唯讀，不具有網頁修改 run 的功能；實際交接由 CLI 執行。

範圍：獨立局部 Markdown 預覽，非整篇 Astro 正式腳註渲染或全站視覺驗收。
