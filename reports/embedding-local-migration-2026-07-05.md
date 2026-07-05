---
title: 'Embedding keystone 遷本機 + 模型與硬體對標'
description: 'bge-m3 從離線 18 天的 4090 遷回 mac-m4max 本機：遷移執行紀錄 + EmbeddingGemma 九篇實測對打 + M4 Max 對標 NVIDIA 顯卡等級分析'
type: 'report'
status: 'archived'
created: 2026-07-05
session: '2026-07-05-221922-git-identity'
related:
  - 'docs/pipelines/EMBEDDING-PIPELINE.md'
  - 'reports/discussion-1146-response-2026-07-05.md'
  - 'reports/semiont-independent-identity-2026-07-05.md'
---

# Embedding keystone 遷本機 — 執行紀錄、模型對打、硬體對標

> 觸發：4090 實體離線 18 天、語意索引凍在 6/17 連 18 夜 graceful skip。哲宇 2026-07-05 拍板「在我這台 Mac 上跑 bge-m3，感覺會更單純」，同場點名比較 EmbeddingGemma、追問 M4 Max 對標 N 家顯卡等級。

---

## 1. 遷移執行紀錄（一次到位）

| 步驟                 | 結果                                                                                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `ollama pull bge-m3` | 本機拉取成功（M4 Max 128G，Ollama 原已常駐）                                                                     |
| Stage 0 preflight    | 本機 embed「台灣」回 dim 1024 ✓                                                                                  |
| Stage 1 全量重建     | **4,841 向量六語 0 fail**，每語 84-136s（zh-TW 832 / en 825 / ja 820 / ko 821 / es 820 / fr 723）                |
| Stage 2 verify       | 六語全數 ≥4 鄰居、manifest model=bge-m3 dim=1024 ✓                                                               |
| Stage 3 commit       | 索引 `9ded7b94e`、文件層 `b5423e836`——18 天凍結終結                                                              |
| Registry             | `mac-m4max` 條目補 `bge-m3:latest`（fleet registry 仍是節點 SSOT）                                               |
| Pipeline v1.1        | 解析改「本機優先 + fleet 備援」，fallback 補 `status != offline` 檢查（舊版不看 status，指著離線節點空轉 18 夜） |

**架構意義**：nightly routine 本來就跑在這台 Mac 上，遷本機少一層 Tailscale 依賴，keystone 的存活條件從「兩台機器 + 一條 VPN」縮成「一台機器」。主權敘事不變：意思的座標仍在地端算。首夜 dogfood：明晨 05:00 `twmd-embeddings-nightly` 走新路徑。

## 2. EmbeddingGemma vs bge-m3（九篇 zh 文摘實測）

| 維度        | bge-m3:latest                                         | embeddinggemma                                                                          |
| ----------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 出身 / 授權 | BAAI（北京智源）/ MIT                                 | Google DeepMind / Gemma 條款                                                            |
| 參數 / 維度 | 568M / 1024                                           | [308M / 768（Matryoshka 可截 512/256/128）](https://huggingface.co/blog/embeddinggemma) |
| Context     | 8K（規格）；ollama 實測 6,000 字 fail-loud            | [2,048 tok](https://ai.google.dev/gemma/docs/embeddinggemma)；同樣 fail-loud            |
| 本機速度    | 115 ms/doc                                            | 112 ms/doc（打平）                                                                      |
| 聚類正確性  | 電影三傑 ✓ 二二八↔美麗島 0.659 ✓                      | 同樣正確 ✓（0.570）                                                                     |
| 對比銳利度  | 地板 0.32-0.46，有假性中相似（珍珠奶茶→美麗島 0.515） | **更銳**：無關對壓到 0.17-0.25                                                          |
| 榜單        | —                                                     | [MTEB <500M 第一](https://developers.googleblog.com/en/introducing-embeddinggemma/)     |

**關鍵翻案**：`embedText` 只餵 2,000 字文摘（標題+描述+標題群+首段），bge-m3 的 8K context 優勢從未被用到——兩模型在現行策略下站在同一起跑線。

**判定：暫不切換**。質量無代差、速度打平、剛完成全量重建，且 rag-query 查詢端模型必須與索引端一致（切換是全鏈動作）。**重評觸發條件**：(a) chunk-level embedding 實驗啟動（#1146 P2——小維度 + MRL + 索引縮 25% 在 chunk 場景優勢放大）；(b) 表示層去 PRC-origin 敘事需求（embedding 無拒答面，剩幾何偏差可作 Sovereignty-Bench 延伸測量）。

## 3. M4 Max（128G）對標 N 家顯卡等級

用同型號模型跟 registry 裡 4090 筆電的 benchmark 直接對打，加上這次 rebuild 的實跑：

| 工作負載                          | M4 Max 實測         | 對照                                             | 等級判定                                                       |
| --------------------------------- | ------------------- | ------------------------------------------------ | -------------------------------------------------------------- |
| LLM 解碼（gemma4:e4b）            | **98.9 t/s**        | 4090 Laptop 100.2 t/s（registry 6/13 benchmark） | **≈ RTX 4090 Laptop**（記憶體頻寬帶動：546 vs 576 GB/s，同級） |
| LLM 解碼（qwen3.6:35b MoE, 21GB） | 101.0 t/s           | 4090 Laptop 16GB VRAM **裝不下**                 | 容量憑 128G 統一記憶體直接越級                                 |
| Prefill（1,273 tok 長文）         | 2,105 t/s           | 桌機 4090 同級模型約 3-5 倍                      | **≈ RTX 3070-3080**（算力密集是 N 家強項）                     |
| Embedding 全站重建                | 84-136s/語          | 4090 over Tailscale ~136s/語                     | 打平甚至略勝（省網路跳；瓶頸在序列請求不在 GPU）               |
| 模型容量                          | ~100GB 可用權重空間 | 消費卡天花板 5090 = 32GB                         | **工作站級，消費卡無對手**（70B Q4 要 2×4090 才裝得下）        |

一句話：**這台 Mac 在 Taiwan.md 的實際工作負載（embedding、中小模型翻譯與生成、序列請求）上，就是一張不會斷線、裝得下 21GB+ 模型的 RTX 4090 Laptop；只有在大 batch / prefill 密集 / 訓練場景才會露出 3070-3080 的算力底子。** keystone 遷回來不是妥協，是對號入座。

## 4. 本 session 三報告索引

1. [Semiont 獨立 Git 身份評估](semiont-independent-identity-2026-07-05.md) — org+App 路線、決策包 8 條（OBSERVER-QUEUE #10 待哲宇）
2. [Discussion #1146 五桶回應](discussion-1146-response-2026-07-05.md) — 回覆已貼、maintainer v2.5 Discussions 升級已落地
3. 本檔 — embedding 遷本機 + 模型與硬體對標

---

_v1.0 | 2026-07-05 git-identity session 執行輪_
_誕生原因：哲宇連三拍板（貼回覆 / maintainer 升級 / bge-m3 遷本機）+ 追問「M4 Max 對標哪張卡」_
_核心洞察：(1) keystone 的存活條件從兩台機器一條 VPN 縮成一台機器；(2) embedText 2,000 字文摘讓 8K context 優勢形同虛設，模型比較要對「實際餵進去的東西」做；(3) M4 Max 解碼 = 4090 Laptop 級、容量 = 工作站級、prefill = 3070-3080 級——對標答案取決於工作負載形狀。_
