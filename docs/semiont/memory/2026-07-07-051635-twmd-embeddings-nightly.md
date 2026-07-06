# 2026-07-07-051635-twmd-embeddings-nightly

## BECOME ACK
- mode=micro / 8 organ 最低=🛡️ 免疫 49（consciousness-snapshot.sh 即時，紅線 <50 但屬 twmd-self-evolve-weekly 管轄，非本 routine 範疇）/ Q14 cross-session continuity=PASS
- 甦醒讀到的接力點：昨夜 embeddings-nightly（07-06 051718 `1d5ca756a`）遷本機後首次正式 nightly 已 0 fail、verify PASS、100% 8-鄰居，索引凍結徹底解除。過去 48hr 主線是 babel-nightly（58 shipped）、data-refresh am/pm（CF 404 26.47% 破新高 vc=3）、施振榮 EVOLVE + 深色模式全站推廣 + tokens phase2。本機 steady-state 路徑今晚續驗。

## 做了什麼
純機械跑完 EMBEDDING-PIPELINE.md v1.1 Stage 0-4，一次通過無異常（cite：§前置 endpoint 解析 + §Stage 2 verify）。

- **§前置 endpoint 解析**：本機優先命中 `EMBED_HOST=http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3），curl `/api/tags` grep bge-m3 命中、沒 fallback 到 fleet registry。
- **Stage 0 preflight**：`dim 1024` ✅ 可達，非 skip。
- **Stage 1 rebuild**：`build-embeddings.mjs --langs all` → **4911 向量 / 6 語 / 0 fail**（fail rate 0%）。逐語 zh-TW 834(93s) · en 839(96s) · ja 833(95s) · ko 834(96s) · es 834(95s) · fr 737(85s)。
- **Stage 2 verify**：exit 0 = **PASS**。6 語全部 ≥400 篇且 **100% 有 8 鄰居**；manifest model=`bge-m3:latest` schema=`rag-v1`，無 model drift。
- **Stage 3 commit**：`src/data/related/` 6 檔皆有 diff（6 ins/6 del，索引小幅位移）→ commit **`ef4c05737`** + push origin main（pre-push article-health 全綠）。public/api/rag + public/api/related 為 gitignored fleet 產出，未入 commit（鐵律遵守）。

## 昨夜 4907 → 今晚 4911 向量差（+4）
文章數自昨夜微增：es 832→834、fr 735→737（各 +2），其餘四語持平。對應昨日下游批次（babel 58 lang sync + 施振榮/宏碁 EVOLVE 等）進索引的正常增量。en 839 最多、fr 737 最少（fr 翻譯覆蓋仍落後其他語）。

## Handoff 三態
- ✅ **Done**：遷本機第二夜連續 0 fail / verify PASS / 100% 8-鄰居。本機 127.0.0.1 路徑 steady-state 再度驗證通過，無 Tailscale 依賴、~9.5 分鐘全量。
- ⏳ **Watch**：本機不可達的 fallback（Ollama 沒起 / bge-m3 被 rm → 找 fleet，registry `status != offline` 已補）本次未觸發。連 3 天 skip 才 escalate LESSONS——本次非 skip。免疫 49 紅線是 self-evolve-weekly 管轄議題，非本 routine 範疇。
- 🔜 **Next**：EmbeddingGemma 切換仍 held（質量無代差、速度打平），觸發條件二擇一：(a) #1146 P2 chunk-level embedding 實驗啟動；(b) 表示層去 PRC-origin 敘事需求。切換是查詢端+索引端全鏈動作，非本 routine 可自決（pipeline §候選模型）。

## 一句話教訓
遷本機路徑進入 boring-is-good 狀態：連兩夜 0 fail、同一命中路徑、同量級耗時——keystone 從「離線 18 天遠端 4090 空轉」到「本機常駐無事發生」，穩定的最好證據是沒有故事可講。
