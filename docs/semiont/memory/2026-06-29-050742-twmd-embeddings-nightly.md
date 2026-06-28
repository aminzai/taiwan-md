# 2026-06-29-050742-twmd-embeddings-nightly

**Mode**: micro（cron routine）
**器官最低**: 🛡️ 免疫 50（chronic yellow，多維度退化中）
**一句話**: embedding keystone 連續第 12 夜 fleet-down graceful skip，索引仍 `d474c977e` 06-17 snapshot，staleness 12 天。

## BECOME ACK

- mode=micro / Micro self-test 7 題全過（Q1-3 identity / Q8-9 信念+口吻 / Q10 commit / Q14 cross-session）
- 8 organ 即時（consciousness-snapshot.sh 2026-06-28T15:10Z）：🫀90 🛡️50 🧬80 🦴90 🫁85 🧫88 👁️90 🌐93
- Q14 cross-session continuity=PASS：過去 48hr babel-nightly 連 12 夜 stale=0 / data-refresh am+pm 全綠（CF 404 跌到 8.76% 破紀錄）/ 本 routine night 11 (6/28-050904) graceful skip。免疫 50 chronic 每 session 帶看。

## Stage 0 — Preflight（fleet 可達性）

- EMBED_HOST（fleet registry 解析，非 hardcode）：`http://100.74.47.100:11434`（laptop-4090, bge-m3:latest）
- curl bge-m3 embed test：**HTTP_CODE=000 / TIME=20.007s timeout**（無回應）
- ping 100.74.47.100：**2 packets 0 received, 100% loss**
- 本機 Tailscale：**stopped**（local 自己斷網，即使 4090 開機也不可達）
- 判定：**fleet down → graceful skip（非 failure）**，連續第 12 夜

## Stage 1-3 — 跳過（fleet down）

- 無 rebuild → 無向量產出 → fail rate N/A
- verify N/A（沒有新產出可驗）
- commit：**no-change skip**（無 diff，不留空 commit）。committed `src/data/related/` 留前一版照常運作

## 索引現況（committed snapshot 完整性已驗）

- 凍結 commit：`d474c977e` 2026-06-17 05:18（最後一次成功 rebuild）
- staleness：**12 天**（06-17 → 06-29）
- 6 語 article count：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700 — 全 present，無 MISSING
- ~28-30 篇最新文 fallback 同 category related（仍有 related，只是非語意，**不壞頁**）

## Handoff 三態

繼承上一 session（2026-06-28-050904，night 11）：

- [x] ~~night 11 graceful skip 收尾~~ → 本夜同樣 skip（**night 12**），索引仍 `d474c977e`
- [ ] 🚨 **embedding keystone 連續第 12 夜 skip**，escalation 自 06-20 拍板未解，vc 封頂 3。最快解：bge-m3 pull 到常駐 always-on 節點（3090 monoame-design / m4max 本機）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks。**這條只欠哲宇 A/B，不欠更多證據**——本夜額外證實 root cause 含「本機 Tailscale stopped」（不只 4090 關機），任何遠端節點都不可達，本機 fallback 節點（m4max bge-m3）會是更穩解
- [ ] 🛡️ 免疫 50 chronic yellow（多維度退化中），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 12 finale memory~~（本檔）
- [ ] staleness 現 **12 天** / ~28-30 篇最新文 fallback 同 category（仍不壞頁）。維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**（handoff 既定，escalation 已 capped）；下一夜若 4090 上線 or 本機 Tailscale 恢復則正常 rebuild，否則 night 13 續記
- [ ] ⚠️ 旁路 Ollama backbone SPOF（embeddings/babel 共底座，12 夜），routine-audit-weekly 持續入鏡
