---
slug: 江振誠
stage: '3.1-3.5'
date: 2026-07-18
---

# Stage 3.1-3.5 Audit — 江振誠

執行者：main session（orchestrator，非 sub-agent）。完整過程與逐項發現見 `reports/research/2026-07/江振誠.md` §「Stage 3 Audit」節，本檔為 gate 結果摘要指標。

## Step 3.1 五指 + 結構 + 塑膠 + 自動驗證

- 五指檢測（驚訝點／兩個轉折／策展句／念結尾／一句話轉述）：全數 PASS，手動核對
- 結構驗證：人物與引語、開場前三句具體事實、正文因果鏈、挑戰編織於故事、非百科排列、結尾非罐頭詞、富文本（3 個 📝 callout + 1 pull quote + 1 tw-timeline stat block）、frontmatter（subcategory「餐飲與職人」經 `docs/taxonomy/SUBCATEGORY.md` 驗證為官方範例本身）：全數 PASS
- 塑膠掃描（手動 90 秒 + grep 五品種）：0 命中
- 自動驗證：`--check=prose-health --output=json` HARD=0 WARN=0；`npx astro build` 7910 頁全過、0 錯誤

## Step 3.2 事實鐵三角

- 3.2.1 算術自檢：本文無金額/百分比/比例類敘述，無適用對象
- 3.2.2 金額單位念出來：無適用對象
- 3.2.3 引語逐字核對：已於 Stage 2.5 兩輪 source-fidelity 稽核 + Step 3.6.1 12-agent fan-out 完整執行，詳見主研究報告
- 3.2-bis correction-meta scan：`article-health.py --check=correction-meta` HARD=0 WARN=0

## Step 3.3 FACTCHECK Quick Mode

- Quick Mode 主 session 自跑（非 A 級觸發 spawn agent，但因文章規模達 A 級門檻，Step 3.6 另行升級 Full-equivalent 12-agent fan-out，見 stage36-audit）
- `ARTICLE_HEALTH_NETWORK=1 article-health.py --check=footnote-url`：13 個 warn 逐一人工核實，12 個為 bot-blocking／本機 SSL 問題（直接瀏覽器 fetch 確認存活），**1 個真實 🔴 DEAD-LINK**（businesstoday.com.tw 已改版重導向首頁）——已修正，改綁 La Vie 2014 專訪
- `--profile=rewrite-stage-3-5`：`hard=0`（footnote-format + footnote-density + correction-meta + quote-fidelity 全數 PASS 或僅剩已知假陽性 warn）

## Step 3.4 Story atom audit

全文場景細節（45 度角椅子、訂位推敲、兩個冰箱、大直商圈、迪化街研究所、雞隻催熟天數、胡蘿蔔品種數等）逐條 Ctrl-F 對 source 核對，經 Stage 2.5 + Step 3.6.1 兩輪查核，無遺留未核實場景細節。

## Step 3.5 Title + description spine sync re-check

```
title: '江振誠：他從來不等一件事被定義死，就先轉身'
description: '1997 年，西華飯店一個二十出頭的法式餐廳主廚，主動邀請兩位法國三星主廚來台客座、共事十天，然後買了機票追去法國。從南法削兩年馬鈴薯，到把新加坡的餐廳排名推上世界第 14 隔年主動熄燈，再到台北開出最難訂的 RAW 又在第十年轉身——江振誠最不可替代的動作，是每次快被一個頭銜定義死的時候，先關燈去問下一題：台灣味到底是什麼。'
```

- title 冒號三明治：PASS（人物 + 動作 + 姿態）
- description 吃進核心矛盾：PASS（每次巔峰主動轉身、最後拋出「台灣味是什麼」的懸而未決提問）
- description 已於 Step 3.6.1 同步更新，反映 section 1 開場改寫（主廚／主動邀請，非副主廚／被指派）

## Result: PASS
