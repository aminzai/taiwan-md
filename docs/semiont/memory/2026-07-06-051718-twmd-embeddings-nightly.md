# 2026-07-06-051718-twmd-embeddings-nightly

## BECOME ACK
- mode=micro / 8 organ 最低=🛡️ 免疫 47（consciousness-snapshot.sh 即時，紅線 <50 但屬 self-evolve-weekly 管轄，非本 routine 範疇）/ Q14 cross-session continuity=PASS
- 甦醒讀到的接力點：昨夜（07-05 23:05 `9ded7b94e`）keystone 已遷本機 mac-m4max、4841 向量六語重建終結 18 天凍結；23:22 全鏈預檢（`f76f12b19`）修 mirror 內嵌舊 fleet 解析防第 19 夜 skip。**今晚是遷本機後第一次正式 nightly 全跑**。

## 做了什麼
純機械跑完 EMBEDDING-PIPELINE.md v1.1 Stage 0-4，一次通過無異常。

- **§前置 endpoint 解析**：本機優先命中 `EMBED_HOST=http://127.0.0.1:11434`（mac-m4max 常駐 bge-m3），沒 fallback 到 fleet。
- **Stage 0 preflight**：`dim 1024` ✅ 可達。
- **Stage 1 rebuild**：`build-embeddings.mjs --langs all` → **4907 向量 / 6 語 / 0 fail**（fail rate 0%）。逐語 zh-TW 834(92s) · en 839(94s) · ja 833(94s) · ko 834(94s) · es 832(94s) · fr 735(84s)。
- **Stage 2 verify**：exit 0 = **PASS**。6 語全部 ≥400 篇且 **100% 有 8 鄰居**；manifest model=`bge-m3:latest` schema=`rag-v1`，無 model drift。
- **Stage 3 commit**：`src/data/related/` 6 檔有 diff（6 ins/6 del，索引小幅位移）→ commit **`1d5ca756a`** + push origin main（pre-push article-health 全綠）。public/api/rag + public/api/related 為 gitignored fleet 產出，未入 commit（鐵律遵守）。

## 昨夜 4841 → 今晚 4907 向量差（+66）
文章數自昨夜微增（昨日 EVOLVE/rewrite 批次：藍染重寫、金瓜石、AAMA+SLP 兩新篇、babel 5 lang sync 等進索引）。en 839 最多、fr 735 最少（fr 翻譯覆蓋落後其他語）。這是 nightly 重建把一天內容變動收進索引的正常增量。

## Handoff 三態
- ✅ **Done**：遷本機後首次正式 nightly 全跑成功，索引凍結徹底解除。本機路徑 steady-state 驗證通過——127.0.0.1 命中、無 Tailscale 依賴、13 分鐘全量、0 fail。
- ⏳ **Watch**：昨夜連 18 夜 skip 的 escalation 已隨遷本機解除；若本機哪天也不可達（Ollama 沒起 / bge-m3 被 rm），fallback 才會找 fleet——registry `status != offline` 檢查已補。連 3 天 skip 才 escalate（本次非 skip）。
- 🔜 **Next**：EmbeddingGemma 切換仍 held（質量無代差、速度打平），觸發條件二擇一：(a) #1146 P2 chunk-level embedding 實驗啟動；(b) 表示層去 PRC-origin 敘事需求。切換是查詢端+索引端全鏈動作，非本 routine 可自決（pipeline §候選模型）。

## 一句話教訓
遷本機第一夜就 0 fail / verify PASS / 100% 8-鄰居——把 keystone 從離線 18 天的遠端 4090 拉回常駐 Mac，用「少一層依賴」換掉了「指著離線節點空轉」的整類 vc=3 故障面。單純確實更穩。
