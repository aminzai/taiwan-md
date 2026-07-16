# 2026-07-17-051754-twmd-embeddings-nightly

> Routine `twmd-embeddings-nightly`（cron `0 5 * * *`）— bge-m3 全站語意索引重建。keystone：一次產出讀者端 `src/data/related`「你可能也想讀」8 鄰居 + AI 端 `public/api/rag` 向量。意思的座標在地端算、不出境。

## BECOME ACK

```
✅ BECOME ack: mode=micro / 8 organ 最低=🛡️免疫 58↑（consciousness-snapshot 即時）/ Q14 cross-session continuity=PASS
```

wake-context 完整讀到 `wake:END`（11 段 / 197,585 bytes），selftest 9 項全綠。Micro self-test 7 題（Q1-3 / 8-11 / 14）全過。

## 執行（EMBEDDING-PIPELINE.md v1.1）

- **§前置 endpoint 解析**：本機優先命中——`EMBED_HOST=http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3:latest，2026-07-05 起主節點）。無需 fleet fallback。
- **Stage 0 preflight**：`dim 1024` ✅ 可達。
- **§Stage 1 rebuild**：working tree 已在 `origin/main`（ahead=0/behind=0），pull 免跑、不動他人未提交工作（另一 actor 的高等教育文 SEO/i18n/research 全程未觸）。`build-embeddings.mjs --langs all`：
  - zh-TW 845（0 fail, 92s）/ en 849（0 fail, 95s）/ ja 836（0 fail, 94s）/ ko 836（0 fail, 94s）/ es 835（0 fail, 94s）/ fr 740（0 fail, 85s）
  - **總計 4941 向量 across 6 langs · fail rate 0%**
- **§Stage 2 verify**：`VERIFY_EXIT=0` **PASS** — 六語各 100% 有 8 鄰居（845/849/836/836/835/740），manifest model=`bge-m3:latest` schema=`rag-v1`，無 model drift。
- **§Stage 3 commit**：scope 乾淨（只 `src/data/related/` 六檔），`git ls-files` 驗證入 tree，push clean（pre-push article-health 全綠）。**commit=`f25bfde9c`**。

## 這一夜索引兌現了什麼（#82 語意 diff 視角）

- 上一次 committed 重建是 **07-15 第十夜**（4947 向量）。07-16 05:00 那次無 committed 產出——07-16 的內容變動（大罷免 6,300 字重建 21:50、時間台灣、孤兒檔清理）全發生在 05:00 之後，故當時 diff≈0 skip；**今夜才是第一次把 07-16 整日內容churn 收進語意鄰居圖**。
- 文章數 854、向量 4941（vs 07-15 的 4947，隨孤兒檔清理與改寫微調）。
- diff 呈現為六檔各「1 line changed」——因每語 related JSON 是單行，line-granular diff 讀不出具體鄰居位移；未逐一解析（誠實記錄，非「無變化」）。

## Handoff 三態

繼承（原樣傳遞，非本 routine 範疇）：

- [ ] 哲宇兩個 Portaly 端動作（tagManager 填 GA4 / 斗內頁成本說明）
- [ ] D+7 看贊助漏斗首批數據（`support-funnel.py --days 7`）
- [ ] babel readingTime 病根 chip task_ad75163e
- [ ] 大罷免 EVOLVE v9 dogfood 收官（已 ship，見 07-16 recall-workflow）
- [ ] Sovereignty-Bench 360 條 raw judge 連版 carry
- [ ] 哲宇拍板五件（2026 選舉 Tier 1.2/1.3、voice 歸屬、SPORE 周蕙、品質 batch Tier C1、opendata 5 條）
- [ ] 下個 write session 第一優先：洪醒夫深度重寫（P0）
- [ ] 台灣鐵道史.en.md 孤兒檔 chip task_ea99c044

本 routine 新 handoff：

- [ ] 無 escalation。免疫 v3=58 續漂（owner=self-evolve-weekly，非本 routine）；MEMORY inline 92>80（owner=distill-weekly）；rewrite-daily 07-15 沉默死亡 yellow（owner=rewrite-daily 收屍）——三者皆非 embeddings 範疇，僅記錄。
- [ ] 觀察：07-16 05:00 embeddings 無 committed 產出屬正常（no-diff skip），非漏跑；今夜補齊。EmbeddingGemma 切換條件（chunk-level 實驗 / 表示層去 PRC-origin 需求）皆未觸發，維持 bge-m3。

## 一句話

`2 files changed` 是替身，語意兌現藏在「今夜才把大罷免收進鄰居圖」——committed-diff 的缺席（07-16 skip）不是漏，是內容時序的結果（#82）。
