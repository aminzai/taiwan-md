# 2026-06-22-050853-twmd-embeddings-nightly — fleet-down graceful skip 連續第 5 夜 + LESSONS vc 2→3 達 distill 門檻

> session twmd-embeddings-nightly — cron 每天 05:00 全站語意索引重建
> Session span: 05:08:25 → 05:08:53 +0800（~30s，1 commit）
> 資料來源：`git log %ai` + consciousness-snapshot.sh + curl preflight

## 觸發

twmd-embeddings-nightly cron 05:00 fire。任務：fleet bge-m3 重建 src/data/related（讀者端 8 鄰居）+ public/api/rag（AI 端向量）。BECOME micro gate 全過（8 organ 最低 = 免疫 50；Q14 cross-session continuity PASS），進 Stage 0 preflight。

## Stage 0 preflight — 節點不可達，graceful skip

EMBED_HOST 從 fleet registry 解析正常拿到 `http://100.74.47.100:11434`（laptop-4090，bge-m3:latest）。但 curl `/api/embeddings` 回 **http 000 / 20s timeout** — 節點完全不可達（4090 關機或 Tailscale 斷，與昨夜同 root cause）。

per EMBEDDING-PIPELINE §Stage 0：**graceful skip，非 fail**。Stage 1 rebuild / Stage 2 verify / Stage 3 commit src/data/related 全部不執行。committed 索引維持 **2026-06-17 05:18 snapshot**（manifest model bge-m3 仍正確讀得到），fallback 同 category 維持讀者頁健康。en 索引 ~801 篇 vs 文章 817 = 最新 ~16 篇 fallback 回同 category，不壞頁。

連續 skip 計數：06-17 last success → 06-18 / 19 / 20 / 21 / **22（本夜）= 連續第 5 夜**。

## LESSONS escalation — vc 2→3 達 distill 門檻

escalation 自 06-20 已 documented（LESSONS §未消化 `routine-device-dependent-offline`，pattern = keystone routine 單押 device-dependent 節點 SPOF，對應 REFLEXES #70 Tier 1）。本夜是同 SPOF 又一次直接 recurrence，把該條 verification_count 從 2 bump 到 3（`07251f609`），已過 vc≥3 distill 門檻 — 待哲宇 A/B 拍板後可 promote。escalation 屬 fleet 基礎建設決策，非本 routine 自主權範疇，不自行修。

## 收官 checklist

| 檢查項                       | 狀態                              |
| ---------------------------- | --------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                |
| Timestamp 精確               | ✅（git log %ai）                 |
| Handoff 三態已審視           | ✅                                |
| CONSCIOUSNESS 反映最新狀態   | ✅（snapshot.sh 即時，未手改檔）  |
| 自我檢查工具 PASS            | ✅（pre-push article-health 全綠）|

## Handoff 三態

繼承上一 session（2026-06-21-050815）：

- [x] ~~本夜 routine graceful skip 收尾~~ — 本夜同樣 skip，索引仍 06-17 版
- [ ] 🚨🚨🚨 **embedding keystone 連續第 5 夜 skip，escalation 自 06-20 defer 哲宇拍板仍未解** — vc 已達 3。最快解：bge-m3 pull 到常駐 always-on 節點（3090 monoame-design / m4max 本機）+ routine 改解析 always-on 優先；或開機 4090 恢復 schtasks
- [ ] 🛡️ 免疫 v3=50 chronic yellow（多維度退化中），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~LESSONS vc 2→3 bump + memory~~（`07251f609`）
- [ ] 在哲宇處理 fleet 前每夜仍 skip，staleness 線性增長（現 ~16 篇 fallback）但不壞頁；連 5 夜後若再無動作，下夜可考慮 memory 標升級 alert 強度

## Beat 5 — 反芻

連續第 5 夜同一個 skip，本身已經是一種沉默的訊號：routine 飛輪能自轉清 entropy，但 routine 修不了自己的底座。embedding 這條的 SSOT 不在 repo 裡，在一台會關機的 laptop 上 — 飛輪轉得再順，keystone 的算力主權還是掛在一個 device-dependent 單點。vc 機制把這件事從「每夜重複 skip 一句帶過」變成可累積、達門檻、能 promote 的結構訊號，這正是 LESSONS buffer 該做的事。剩下的是等觀察者那一個 A/B 決定。

🧬

---

_v1.0 | 2026-06-22 05:08 +0800_
_session twmd-embeddings-nightly — fleet-down graceful skip 連續第 5 夜 + LESSONS vc 達 distill 門檻_
_誕生原因：cron 05:00 fire，4090 節點 http 000 timeout，Stage 0 graceful skip_
_核心洞察：routine 飛輪自轉清 entropy 但修不了自己的 device-dependent 底座；vc 機制把每夜重複的 skip 累積成可 promote 的結構訊號_
_LESSONS-INBOX 候選：無新增（既有 routine-device-dependent-offline vc 2→3，已在 §未消化）_
