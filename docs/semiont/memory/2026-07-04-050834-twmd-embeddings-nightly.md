---
session: 2026-07-04-050834-twmd-embeddings-nightly
routine: twmd-embeddings-nightly
mode: micro
date: 2026-07-04
---

# 2026-07-04 05:08 twmd-embeddings-nightly — 連 17 夜 fleet-down graceful skip，實測 tailscale up 無效證明 4090 機器實體離線

## BECOME ACK

- mode=micro，Universal core 全跑（consciousness-snapshot + routine-status + 48hr git log + MEMORY head/tail）
- 8 organ 最低=🛡️49（免疫，red <50，chronic 第 12 cycle unchanged）
- Q14 cross-session continuity=PASS：讀到過去 2 天 cron 全鏈（babel / data-refresh am+pm / spore-harvest / feedback-triage / maintainer am+pm / rewrite-daily / 本 routine 連 16 夜 skip）

## Stage 0 Preflight — fleet 不可達（graceful skip）

- EMBED_HOST=`http://100.74.47.100:11434`（registry 解析，唯一含 bge-m3 節點 cheyuwu-asus / laptop-4090）
- 初測：本機 `tailscale status`=stopped、curl HTTP_CODE=000
- **本夜關鍵動作**：依前夜 handoff 建議跑 `tailscale up --accept-routes` 把本機 tailnet 起來（成功，本機重新入網）
- **再測仍 000**：`tailscale status` 顯示 `100.74.47.100 cheyuwu-asus ... offline, last seen 16d ago`；curl HTTP_CODE=000；ICMP 100% loss
- 結論：**root cause 不是本機 Tailscale，是 4090 機器實體離線 16 天**。前 16 夜 memory 把 root cause 記成「本機 Tailscale stopped」只對了一半——本機 tailnet 修好後路徑仍不通，因為對端機器根本沒開機

## 產物狀態

- 無 rebuild → src/data/related 無 diff → **skip commit，不留空 commit**（只 commit 本 memory 檔）
- committed 索引仍是 `d474c977e`（2026-06-17 05:18），staleness **17 天**
- 6 語 committed snapshot 本夜實測 100% 8 鄰居：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700 全 ✓——讀者端「你可能也想讀」全站仍完整運作
- 06-17 後新增/改寫文 fallback 同 category related（有 related，只是非語意，不壞頁）
- fail rate=N/A（未 rebuild）；verify=committed-snapshot PASS

## 本夜新 datapoint（給哲宇 A/B 的具體證據）

前 16 夜 handoff 一直建議「短期最省力=session 啟動 tailscale up 即可讓下夜 4090 路徑復活」。本夜實測證偽這條捷徑：

- 本機 `tailscale up` 已跑成功，本機 tailnet 恢復
- 但 tailnet 上 `cheyuwu-asus`（4090）狀態=`offline, last seen 16d ago`——機器實體沒開機
- 所以 `tailscale up` 只修本機半邊，對端機器離線這半邊修不了

**診斷收斂**：SPOF 有兩層——(1) bge-m3 只 provision 在 4090 一台；(2) 這台又依賴實體開機 + Tailscale。tailscale up 只能解 tailnet 那層，機器沒開就沒救。恢復路徑更新為：
- 最省力：把 4090（cheyuwu-asus）實體開機（本機 tailnet 現已 up，開機後下夜即可連上）
- 最根本：本機 m4max `ollama pull bge-m3` + 常駐 daemon（免遠端免 Tailscale，前夜查過 127.0.0.1 尚未 provision），或指定一台 always-on 節點裝 bge-m3

以上皆屬 §自主權邊界（實體開機 / 本機 pull model 起 daemon 是環境變更），routine 不自行動作，呈報哲宇。

## Handoff 三態

**已完成**：Stage 0 preflight 判定 fleet-down；跑 `tailscale up --accept-routes` 恢復本機 tailnet（本夜正向貢獻，下夜本機半邊已通）；實測證明 4090 機器實體離線是真 root cause；驗證 committed 索引 6 語 100% 8 鄰居完好；無 diff 不 commit。

**進行中/待觀察**：graceful skip 連 17 夜。escalation 自 06-20 已 capped vc=3，per 既定 handoff 不再每夜 re-bump LESSONS。

**給下一個 session / 哲宇的決策點**：
- 本機 Tailscale 現已 up（我這夜起的），下一夜若 4090 開機即可直接連上，不需再 tailscale up
- root cause 已收斂到「4090 實體離線 16 天」，比「本機 tailscale stopped」精確——tailscale up 捷徑已證偽
- 二選一根本修法仍等哲宇拍板：(A) 4090 always-on + registry always_on；(B) 本機 m4max pull bge-m3 常駐 daemon（robustness 最強，免遠端免 tailnet）
- routine 維持 graceful skip 設計正確，不 escalate、不 fail、不動 committed 索引
