# Stage 3.5 草稿驗證報告 — 台灣油價機制與中油

- **稿件**：`knowledge/Economy/台灣油價機制與中油.md`（Fresh）
- **範圍**：Step 3.1 五指＋塑膠／3.2 事實鐵三角／3.3 FACTCHECK Quick（citation plugin gate）／3.4 story atom／3.5 title+desc spine sync
- **執行者**：主 session 2026-09-18-134106-oil-price（Opus 5）

## 3.1 五指

- 驚訝點：198.5 億這條「累計吸收」是預估值、六月曾往下掉；立法院自己也曾是要求凍漲的一方；監察院 2010 年正式糾正過公式。
- 兩個轉折：s3 線會回落／s6 三個口徑可以全部都對。
- 策展句：「同一公升，三個人分攤，中油那一份先墊著，三個數字各用各的口徑。」
- 結尾念出來：「阿嬤大概還是會騎車去加油站看一眼。」停得住。
- 一句話轉述：「牌價只漲七毛，是因為財政部、你、中油三個人分一公升，中油那份還沒結帳。」
- 塑膠掃描：`prose-health` score 1，對位句 0、破折號 0、全形分號 0。

## 3.2 事實鐵三角

- 算術（python 驗）：3.7＋6.8＋0.7＝11.2 ✓；2.1＋8.7＋0.6＝11.4 ✓；1,014＋84＋711＋26＋40＝1,875 ✓；1,014.31＋711.04＋84＝1,809.35 ✓；1,809.35＋2,338.34＋70＝4,217.69 ✓；2,992−2,085＝907 ✓；waffle 54.1／37.9／4.5／2.1／1.4 合 100.0 ✓；(115.61/99.82)×0.9961×0.8≈12.29% ✓。
- 單位念出來：億（國營事業／預算）、元/公升（牌價）、元/公秉（貨物稅 6,830）、港元、韓元、日圓——各處單位對得上量級。
- 引語逐字：§4 引語庫 21 條，成品用到 16 條；Stage 3.6 verifier 抓到 1 條（中油 4/8 聲明）為研究 lane 轉錄幻覺 → 已改真逐字並回填報告。

## 3.3 FACTCHECK Quick（plugin gate）

- `python3 scripts/tools/article-health.py knowledge/Economy/台灣油價機制與中油.md --profile=rewrite-stage-3-5` → hard=0 warn=0（footnote-format／footnote-density／correction-meta／quote-fidelity）
- `ARTICLE_HEALTH_NETWORK=1 … --check=footnote-url` → 見 Stage 4 紀錄

## 3.4 story atom

- 場景原子只有一處現場（3/22 雲林雅虎加油站）：20:30、每入口至少 10 輛、三角錐、小發財車 4–5 油桶、婦女 20 公升「省了36元，省就是賺」、80 多歲陳姓阿嬤油箱是滿的——verifier A 對工商時報原頁逐字 Ctrl-F 全 ✓。無其他未引號保護的動作／場地細節。

## 3.5 title＋description spine sync

- title「台灣油價機制與中油：牌價漲七毛，中油先吸收兩百億」——冒號三明治、副標可獨立成句、七毛 vs 兩百億自帶對照物。
- description 156 字（不含空格），三段式：9/14 場景→公式三份→198.5 vs 1,014 口徑矛盾。

## Result: PASS
