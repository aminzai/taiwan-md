---
slug: 江振誠
stage: '3.6-3.7'
date: 2026-07-18
tier: 'A（5631 CJK chars ≥ 3000 門檻 + 30 footnotes + 多句直接引語）'
---

# Stage 3.6 成品總驗三關 + Stage 3.7 總編對抗總評 Audit — 江振誠

執行者：main session（orchestrator）派 12 個 parallel Sonnet agent（7 adversarial verifier + 5 chief-editor probe），逐項發現與修正完整記錄於 `reports/research/2026-07/江振誠.md` §「Step 3.6.1 + 3.7」節，本檔為 gate 結果摘要。

## Step 3.6.1 原子重驗 fan-out

7 個 adversarial verifier 依成品 H2 段落分工（非依研究子題），各自讀該段全文 + 全部腳註來源 URL，逐 atom（引語/數字/日期/歸屬/詮釋 gloss/footnote-claim 綁定）開原頁核對。

匯總：約 90+ 個 atom 逐條查核，**12 個 ❌/重大 ⚠️ 確認並修正**（詳見主研究報告表格），涵蓋 4 類 drift：

1. **引語逐字 diff**：0 個捏造引語，2 個縮寫/改句型的已知假陽性（已回填 SSOT）
2. **詮釋 gloss 獨立 atom**：VERSE 引語「它」referent 誤植（台灣味譜→應為台灣味本身）、45 度角椅子場景城市/年代誤植（RAW→應為新加坡 Restaurant André）
3. **footnote-claim 綁定**：4 處確認綁錯來源（TIME 雜誌封號掛 SCMP 應掛天下雜誌、太太前雜誌總編輯掛 taster.life 應掛中國時報、Timeless 引語掛遠見應掛 500 輯、[^12] 未實際支撐其自身聲稱的雙城並進時序）
4. **writer 自漂移**：建物年代「1930 年代」查無依據（來源僅稱 century-old）、座位數加總邏輯錯誤（56+20 應為 56 含 20）、「一年半」低估實際 23.6 個月

全數 12 項已修正並 append 主研究報告 §audit（含查證軌跡 + verdict + 根因）。

## Step 3.6.2 順稿（閱讀感檢查）

大範圍改寫後重讀全文：段落牆（無 >280 字單段）、framing 詞硬接（無「值得一提」類殘留）、文章機械自述（無）、一致性殘渣（description 已同步 section 1 開場改寫；結尾排比指涉核對無 dangling；策展人筆記無引用已勘誤舊事實）、中英夾雜殘留（無）。

**發現並修正 1 項連帶回歸**：改寫過程一度把 prose-health 破折號從 7 個推到 14 個、對位句型從 3 個推到 4 個（score 3→4，跌出 pass 門檻）；逐一核對後把新增破折號改回標點、拆掉多餘對位句型，score 收斂回 3（與改寫前打平）。

## Step 3.6.3 視覺同步

逐一檢查媒體 × 敘事對位：

- hero 圖（archi 藝廚招牌）＋收尾前圖（archi 藝廚用餐空間）：原本正文零呼應 archi 藝廚身分，**已修正**——section 6 新增兩句明確交代 archi 藝廚是什麼、跟宜蘭家居生活的關係
- PDIS 照片（2021 年造訪公共數位創新空間）：原插在 section 2/3 交界（1997-2008 敘事中間），與周圍時間軸脫節，**已修正**——搬遷至 section 6（「現在，他還在轉身」），語境貼近拍攝年份
- tw-timeline stat block：與正文年份逐一核對一致，無需調整
- YouTube iframe ×2（《初心》預告片、米其林官方 RAW 影片）：頻道歸屬、標題、內容主旨三項經 Step 3.6.1 verifier 直接開啟核實，皆吻合

三關全過。

## Step 3.7 總編對抗總評

5 個 parallel Sonnet 探針（門面兌現／逐段主軸服務／H2載體還原／連結成網／立體地愛），各自冷讀成品全文（未看投影藍圖、未看研究報告），falsification 姿態。

**結果：5/5 verdict=revise**。完整 review 檔：`reports/editorial-room/江振誠-chief-review.md`（room: chief，`editorial-room-health.py` exit 0 PASS）。

必改清單 7 條中 6 條 accept 並執行（archi 藝廚身分補入、PDIS 圖搬遷、兩個 H2 小標補主詞動詞、24 節氣段補注、三處 footnote 綁定修正、「讓這個人更立體」與免責矛盾句改寫、結尾補保留態度），1 條經攻防輪 defend 保留現狀（「我是誰」小標引號用法——與正文 section 4 的既定 echo map 對仗設計一致，非孤立問題，且改動範圍已超出 Step 3.7 職權）。

## 最終 Gate 結果

```
footnote 1-30 序列完整（30 def，無孤兒，無缺號）
article-health.py --profile=rewrite-stage-3-5:  hard=0  warn=2  info=4  PASS
article-health.py --check=format-structure:      hard=0  warn=0          PASS
article-health.py --check=word-count:            5631 CJK chars (125%)   PASS
article-health.py --check=prose-health:          score=3 (≤3=pass)       PASS
bash scripts/core/sync.sh + npx astro build:      7910 頁，0 錯誤          PASS
editorial-room-health.py（prose-structure-review）: exit 0                PASS
editorial-room-health.py（chief-review）:           exit 0                PASS
```

## Result: PASS
