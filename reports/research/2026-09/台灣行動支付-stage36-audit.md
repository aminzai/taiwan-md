---
slug: 台灣行動支付
stage: '3.6-3.7'
date: 2026-09-01
---

# Stage 3.6-3.7 Audit — 台灣行動支付

## 執行編排

- 1 席來源忠實度 verifier：開啟成文全部 19 則初稿腳註，檢查 claim 與相連來源的承載範圍。
- 1 席定向來源複驗：回修後重驗腳註 4、6、14、15、17 與原腳註 19 刪除狀態。
- 2 席分段事實原子 verifier：前半腳註 1–11、後半腳註 12–18，各自開原始頁面或 PDF 核對數字、分母、年份、樣本、制度與推論語氣。
- 6 席冷讀總編探針：門面兌現、逐段主軸、H2 載體、連結成網、閱讀節奏、立體地愛／倫理；只讀成品，不看研究與投影。
- 1 席最終來源 spot-check：只重驗總編回修新增的支付三層、商家利益面、現金成本限定與假設場景。

## Step 3.6 事實原子結果

### 第一輪發現與處置

1. 腳註 4 原稿以單一金管會教材承擔過多平台與後端描述；縮回教材直接列出的分類。
2. 腳註 6 原稿將電支申報合計推向多重契約；改為「未提供跨機構自然人去重」，並刪除沒有相連人口來源的比較。
3. 腳註 14 原稿由描述性調查推出優惠因果；改為只描述樣本內追蹤點數與精算回饋。
4. 腳註 15 改連經濟部官方 PDF，並補清分母是回表樣本的付款金額。
5. 腳註 17 將合作金庫頁面的工具名由 `icash Pay` 修正為「愛金卡」。
6. 原腳註 19 無法由單一日本來源承擔台日韓三地方法比較，且研究投影已排除此支線；整句與腳註刪除。
7. 腳註 16 的「訊息介接」與「所有公開資料沒有活躍率」均超出相連年報承載；分別收斂為共同 QR 串連兩類機構、以及「央行這份資料沒有提供」。
8. 其他平台申請文件原未相連官方來源；枝節刪除。
9. 結尾攤位場景明示為依 FAQ 構成的假設，不冒充實際個案。

完整 fact-level 回修已 append 至 `reports/research/2026-09/台灣行動支付.md` §8。

### 複驗結果

- 定向來源複驗：5/5 PASS；原腳註 19 與日韓比較無殘留。
- 前半 verifier：數字、樣本、日期與引語全數正確；2 個來源覆蓋缺口已以刪除／收斂處理。
- 後半 verifier：數字、年份、樣本與 TWQR 名單正確；3 個分母／資料範圍問題及 1 個場景標示問題已處理。
- 最終 spot-check：支付三層、商家利益面、現金成本限定與假設場景 4/4 PASS。

## Step 3.7 總編室結果

六席初判皆為局部 revise，沒有要求推翻核心方向。主編合併為七項必改並全部套用：

1. 門面承諾由「資金」收斂為「工具」，正文補清綁定工具、商家契約與交易規格三層。
2. 故障復原提早進開場，並修正「App 相同才能補位」的邏輯倒置。
3. 離線案例由三次降為兩次，4,112.9 萬與費率防守支線壓縮。
4. 三個 H2 加入視角或範圍限定。
5. 電商、全聯、金融科技三條站內連結收斂至目標文章確實提供的內容。
6. 30 秒概覽移除重複樣本／頻率數字，第二節刪除同義重述。
7. 補回商家利益面、現金本身的營運成本與收尾假設標示。

合併 review：`reports/editorial-room/台灣行動支付-chief-review.md`，`overall: pass`；`editorial-room-health.py` exit 0。

## 最終工具 gates

- `article-health.py --profile=rewrite-stage-3-5`：hard=0、warn=0。
- `article-health.py --check=prose-health`：hard=0、warn=0，score=3。
- `article-health.py --profile=rewrite-stage-4`：hard=0、warn=0；4,500 CJK、3 張圖、3 個 tw-* 視覺。
- `prose-flow.py` 定稿前：31 段、median 111、最長 227、長段 3。
- `prose-flow.py` 定稿後：34 段、median 110、最長 175、長段 0；只有「後兩節沒有 tw-* 視覺」一項 soft signal。TWQR 節已有 inline 圖，故不加裝飾性圖表。
- `editorial-room-health.py`：prose-structure 與 chief review 皆 PASS。

## Step 3.8 定稿站

- fresh closing editor 只讀成品、prose-flow 表與閱讀節奏席 findings，不接觸研究、投影或編輯歷程。
- 完整 staging：`reports/article-evolve/台灣行動支付-closing.md`。
- 定稿只做轉場、拆段與語感修順；frontmatter、H2、引語、數字、腳註、URL、表格與 tw-* 模組均保持原子守恆。
- `fact-atom-diff.py knowledge/Technology/台灣行動支付.md reports/article-evolve/台灣行動支付-closing.md`：PASS。
- 主編抽查後套用 staging；canonical 與 staging 最終 byte-for-byte 相同，`diff -q` exit 0。

## 未解疑慮

- 自動 URL 掃描對少數官方網站回報 SSL／403；本輪 verifier 已透過原頁、可下載官方 PDF 或人工開啟方式完成內容核對。
- 本文不提供會快速變動的平台／商家可用名單，也不把合作特店數解讀成活躍率或全市場覆蓋率。

## Result: PASS

（事實原子、總編室、來源 spot-check 與所有 hard gates 均已通過。）
