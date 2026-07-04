---
session: 2026-07-05-050810-twmd-embeddings-nightly
routine: twmd-embeddings-nightly
mode: micro
date: 2026-07-05
---

# 2026-07-05 05:08 twmd-embeddings-nightly — 連 18 夜 fleet-down graceful skip，本機 tailnet 已通、4090 仍離線 17d

## BECOME ACK

- mode=micro，Universal core 全跑（consciousness-snapshot + routine-status + inbox-signal + 48hr git log + MEMORY head/tail + REFLEXES catalog + EMBEDDING-PIPELINE 全檔嚴格 Read）
- 8 organ 最低=🛡️49（免疫，red <50，chronic）
- Q14 cross-session continuity=PASS：過去 2 天 cron 全鏈可見（babel-nightly 零操作 / data-refresh am+pm / spore-harvest / feedback-triage / maintainer am+pm / weekly-report-sun W26→W27 / distill-weekly #77 / self-evolve-weekly #78/#79/#80 promote / 本 routine 連 17 夜 skip）

## Stage 0 Preflight — fleet 不可達（graceful skip）

- EMBED_HOST=`http://100.74.47.100:11434`（registry 解析，唯一含 bge-m3 節點 cheyuwu-asus / laptop-4090）
- `tailscale status`：本機 tailnet 有回報 peer（前夜 tailscale up 的效果持續，本機半邊仍通），但 `100.74.47.100 cheyuwu-asus ... offline, last seen 17d ago`
- curl HTTP_CODE=000、exit=28（20s timeout）
- 結論同前 17 夜：root cause=4090 機器實體離線（現 17d），非本機 Tailscale。前夜證偽的 tailscale up 捷徑本夜複驗一致——本機已通、對端沒開機

## 產物狀態

- 無 rebuild → src/data/related 無 diff → **skip commit，不留空 commit**（本 memory 檔照 commit）
- committed 索引仍是 `d474c977e`（2026-06-17 05:18），staleness **18 天**
- 6 語 committed snapshot 本夜實測 100% 8 鄰居：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700 全 ✓——讀者端「你可能也想讀」全站完整運作
- 06-17 後新增/改寫文 fallback 同 category related（有 related，只是非語意，不壞頁）
- fail rate=N/A（未 rebuild）；verify=committed-snapshot PASS

## 本夜 datapoint

無新證據。前 17 夜已收斂：SPOF 兩層（bge-m3 僅 provision 4090 一台 + 該台依賴實體開機）。本夜複驗一致，不新增 escalation（自 06-20 已 capped vc=3，per 既定 handoff 不再每夜 re-bump LESSONS）。

## Handoff 三態

**已完成**：Stage 0 preflight 判定 fleet-down；驗證本機 tailnet 半邊仍通；curl/ICMP 複驗 4090 離線 17d；committed 索引 6 語 100% 8 鄰居完好；無 diff 不 commit。

**進行中/待觀察**：graceful skip 連 18 夜。escalation capped vc=3，不再每夜 re-bump。

**給下一個 session / 哲宇的決策點**（同前夜，未變）：

- 本機 Tailscale 已 up，4090 一開機下夜即可直連，不需再跑 tailscale up
- root cause 收斂到「4090 實體離線」，tailscale up 捷徑已證偽（連 2 夜複驗）
- 二選一根本修法等哲宇拍板：(A) 4090 always-on + registry always_on；(B) 本機 m4max `ollama pull bge-m3` 常駐 daemon（robustness 最強，免遠端免 tailnet）
- routine 維持 graceful skip 設計正確，不 escalate、不 fail、不動 committed 索引
