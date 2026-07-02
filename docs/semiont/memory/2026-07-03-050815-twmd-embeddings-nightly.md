---
session_id: '2026-07-03-050815-twmd-embeddings-nightly'
date: 2026-07-03
type: 'routine-memory'
routine: 'twmd-embeddings-nightly'
mode: 'micro'
outcome: 'fleet-down graceful skip (第 16 夜)'
---

# 2026-07-03 05:08 twmd-embeddings-nightly — fleet-down graceful skip 第 16 夜

## BECOME ack

- mode=micro，self-test 7 題全過
- 8 organ 即時（consciousness-snapshot.sh）：🫀90 🛡️49 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93。最低 🛡️49（免疫 chronic 第 10 cycle，昨 pm data-refresh 已記 escalate-ready）
- Q14 cross-session continuity=PASS：過去 2 天全 routine 飛輪（babel 7/2 15 譯本→7/3 5 metadata bump / data-refresh am+pm / spore-harvest / feedback-triage / maintainer am+pm）；上一 embeddings run 2026-07-02-050817 連 15 夜 fleet-down skip，root cause 本機 Tailscale stopped

## Stage 0 — Preflight：fleet 不可達，graceful skip

- EMBED_HOST 從 fleet registry 解析（非 hardcode）：`http://100.74.47.100:11434`（laptop-4090，唯一含 bge-m3 的節點）
- bge-m3 embeddings probe：HTTP 空回應 → PREFLIGHT_UNREACHABLE
- 佐證：`tailscale status` = **Tailscale is stopped**（本機 tailnet 未起）；ICMP ping 100.74.47.100 = 100% packet loss
- 結論：與前 15 夜同 root cause——本機 Tailscale 未啟動，即使 4090 開機也連不上。**graceful skip，非 fail**

## Stage 1-3 — 未 rebuild（skip 分支）

- 無 rebuild → src/data/related 無 diff → **skip commit，不留空 commit**
- committed 索引仍是 `d474c977e`（2026-06-17 05:18），staleness **16 天**
- 6 語 committed snapshot 本夜實測 100% 8 鄰居：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700 全 ✓——讀者端「你可能也想讀」全站仍完整運作
- 06-17 後新增/改寫文（飯糰、台灣吧、彎彎 EVOLVE、Computex EVOLVE、蘇打綠+田馥甄 heal 等）fallback 同 category related（有 related，只是非語意，不壞頁）

## 本夜新 datapoint（給哲宇 A/B 的具體證據）

registry 現有 4 個 embed 節點，逐一查 bge-m3 provisioning：

| 節點 | IP | bge-m3 pulled？ |
| --- | --- | --- |
| laptop-4090 | 100.74.47.100 | ✅（唯一）— 但需 Tailscale（SPOF） |
| （70b 節點） | 100.87.153.44 | ❌ |
| （gpt-oss 節點） | 100.101.135.15 | ❌ |
| **本機 m4max localhost** | 127.0.0.1 | ❌ + 本機 ollama 未起（curl 空回應） |

**關鍵發現**：handoff 一直在等的 A/B 選項 B「本機 m4max fallback 免遠端免 Tailscale」**尚未 provision**——127.0.0.1 雖已在 registry embed 清單，但沒 pull bge-m3、本機 ollama daemon 也沒跑。所以即使今晚想走本機 fallback，路徑也不通。這是 infra 佈署缺口，屬 §自主權邊界（本機 pull model + 起 daemon 是環境變更），routine 不自行動作，呈報哲宇。

## Handoff 三態

**已完成**：Stage 0 preflight 判定 fleet-down + 佐證 Tailscale stopped/ICMP loss；驗證 committed 索引 6 語 100% 8 鄰居完好；確認無 diff 不 commit；查清 4 embed 節點的 bge-m3 provisioning 狀態。

**進行中/待觀察**：graceful skip 連 16 夜。escalation 自 06-20 已 capped vc=3，per 既定 handoff 不再每夜 re-bump LESSONS（避免 noise）。

**給下一個 session / 哲宇的決策點**：
- SPOF 未解——bge-m3 只在 laptop-4090 一台，且綁本機 Tailscale。今晚查清「選項 B 本機 fallback」路徑尚未 provision（127.0.0.1 無 bge-m3 + ollama 未起），所以連退路都不通。
- 最根本修法仍是二選一（等哲宇拍板）：(A) 讓 bge-m3 節點 always-on + registry always_on 保證遠端常駐；(B) 本機 m4max `ollama pull bge-m3` + 常駐 daemon，免遠端免 Tailscale。B 對 routine robustness 最強（不依賴任何遠端 + tailnet）。
- 短期最省力恢復：session 啟動時本機 `tailscale up` 即可讓下一夜 4090 路徑復活（若 4090 開機）。
- routine 維持 graceful skip 設計正確，不 escalate、不 fail、不動 committed 索引——這正是 pipeline Stage 0 規定的行為。
