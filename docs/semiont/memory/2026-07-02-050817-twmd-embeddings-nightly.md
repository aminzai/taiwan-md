# 2026-07-02-050817-twmd-embeddings-nightly

**Mode**: micro（cron routine）
**器官最低**: 🛡️ 免疫 50（chronic yellow 第 8 cycle，7/1 pm data-refresh external_rulers 3.7→4.0 vs editorial -1 day 反向 offset 掩蓋 top-level drift）
**一句話**: embedding keystone 連續第 15 夜 fleet-down graceful skip，索引仍 `d474c977e` 06-17 snapshot，staleness 15 天。

## BECOME ACK

- mode=micro / Micro self-test 全過（Q1-3 identity / Q8-9 信念+口吻 / Q10 commit / Q11 gene map+reflex / Q14 cross-session）
- 8 organ 即時（consciousness-snapshot.sh 2026-07-01T15:09Z）：🫀90 🛡️50 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93。最低 🛡️免疫 50。
- Q14 cross-session continuity=PASS：過去 48hr — babel 連 14 夜 stale=0（7/2 00:57 **15 譯本 ship**，Computex EVOLVE 撞 Tier 2 free 天花板兩層 [429 五 key exhaust + ja 32k output cap] → Tier 4 Sonnet 五語 full re-translation 首例接手）/ data-refresh am+pm CF 404 連 3 cycle 25% band 收斂 <0.51pp **vc=3 CONFIRMS baseline reset promote LESSONS** / 讀者 A 凌晨 5 筆細讀勘誤 07:09 triage file #1187–#1191 → 21:47 rewrite 全 heal（蘇打綠 4 + 田馥甄 1）/ maintainer PR #1186 台南小吃 5-層 review → contributor refine 3/4 verify + partial-fix 誠實 flag / 本 routine night 14（7/1-050745）graceful skip。

## Stage 0 — Preflight（fleet 可達性）

- EMBED_HOST（fleet registry 解析，非 hardcode）：`http://100.74.47.100:11434`（laptop-4090, bge-m3:latest, always-on via schtasks SYSTEM）
- curl bge-m3 embed test：**HTTP_CODE=000 / 20s timeout**（空回應）
- /api/tags base ping：**HTTP_CODE=000 / 10s timeout**（節點整台不可達，非單一 model 問題）
- ICMP ping：**100% packet loss**（2 packets, 0 received）
- 本機 **Tailscale is stopped**（local 自斷 → 遠端任何節點皆不可達，root cause 在本機 tailnet 未起而非只 4090 關機）
- 判定：**fleet down → graceful skip（非 failure）**，連續第 15 夜

## Stage 1-3 — 跳過（fleet down）

- 無 rebuild → 無向量產出 → fail rate N/A
- verify N/A（沒有新產出可驗）
- commit：**no-change skip**（無 diff，不留空 commit）。committed `src/data/related/` 留前一版照常運作

## 索引現況（committed snapshot 完整性已驗）

- 凍結 commit：`d474c977e` 2026-06-17 05:18（最後一次成功 rebuild）
- staleness：**15 天**（06-17 → 07-02）
- 6 語 file present + 100% 8 鄰居（本夜實測）：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700，全 ✓ ≥90% 閾值，無 MISSING
- working tree clean（src/data/related 無未 commit 變動）
- 自 06-17 後新增 / 改寫文章（飯糰 #1182 / 台灣吧 #1183 / 彎彎 EVOLVE / Computex EVOLVE / 蘇打綠+田馥甄 heal 等）fallback 同 category related（仍有 related，只是非語意，**不壞頁**）

## Handoff 三態

繼承上一 session（2026-07-01-050745，night 14）：

- [x] ~~night 14 graceful skip 收尾~~ → 本夜同樣 skip（**night 15**），索引仍 `d474c977e`
- [ ] 🚨 **embedding keystone 連續第 15 夜 skip**，escalation 自 06-20 拍板、vc 封頂 3，**只欠哲宇 A/B 不欠更多證據**。最快解：bge-m3 pull 到常駐 always-on 節點（m4max 本機最穩，免遠端 + 免 Tailscale 依賴 / 或 3090 monoame-design）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks + 本機 Tailscale 起。屬 fleet 基礎建設決策（§自主權邊界），非本 routine 自主權範疇
- [ ] 🛡️ 免疫 50 chronic yellow 第 8 cycle（external_rulers/editorial 反向 offset 掩蓋 top-level drift），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 15 finale memory~~（本檔）
- [ ] staleness 現 **15 天** / 自 06-17 後新增文 fallback 同 category（仍不壞頁）。維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**（handoff 既定，escalation 已 capped vc=3 待哲宇 A/B）；下一夜若 4090 上線 or 本機 Tailscale 起 or 本機 fallback 節點（m4max bge-m3）落地則正常 rebuild，否則 night 16 續記
- [ ] ⚠️ 旁路 Ollama backbone SPOF（embeddings/babel 共底座，15 夜），routine-audit-weekly 持續入鏡。本機 Tailscale stopped 是本夜實測 root cause，值得回報哲宇：即使 4090 開機，本機 tailnet 未起也連不上 → fallback 到本機常駐節點（無 tailnet 依賴）更根本
