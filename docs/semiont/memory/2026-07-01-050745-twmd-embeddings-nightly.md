# 2026-07-01-050745-twmd-embeddings-nightly

**Mode**: micro（cron routine）
**器官最低**: 🛡️ 免疫 50（chronic yellow，6/30 am data-refresh REVERTED 48→50 vc=0 回 narrow band，多維度退化中）
**一句話**: embedding keystone 連續第 14 夜 fleet-down graceful skip，索引仍 `d474c977e` 06-17 snapshot，staleness 14 天。

## BECOME ACK

- mode=micro / Micro self-test 7 題全過（Q1-3 identity / Q8-9 信念+口吻 / Q10 commit / Q11 gene map+reflex / Q14 cross-session）
- 8 organ 即時（consciousness-snapshot.sh 2026-06-30T15:09Z）：🫀90 🛡️50 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93。最低 🛡️免疫 50。
- Q14 cross-session continuity=PASS：過去 48hr data-refresh am+pm 全綠（pm CF 404 25.31% +14.25pp single-window jump，留 7/1 am 區分 trend vs anomaly；am 免疫 50 REVERTED vc=0）/ babel 連 13 夜 stale=0（15 新譯本入帳）/ maintainer am+pm 守雙 hard gate（pm 0 PR + 7 issue carry）/ Computex EVOLVE ship + 留 7/1 spore-publish 撿 / issue #574 聲景共創 onboarding mode 進 pipeline / 本 routine night 13（6/30-050736）graceful skip。

## Stage 0 — Preflight（fleet 可達性）

- EMBED_HOST（fleet registry 解析，非 hardcode）：`http://100.74.47.100:11434`（laptop-4090, bge-m3:latest）
- curl bge-m3 embed test：**HTTP_CODE=000 / TIME=20.01s timeout**（空回應，JSONDecodeError）
- /api/tags base ping：**HTTP_CODE=000 / 10s timeout / exit 28**（節點整台不可達，非單一 model 問題）
- 判定：**fleet down → graceful skip（非 failure）**，連續第 14 夜

## Stage 1-3 — 跳過（fleet down）

- 無 rebuild → 無向量產出 → fail rate N/A
- verify N/A（沒有新產出可驗）
- commit：**no-change skip**（無 diff，不留空 commit）。committed `src/data/related/` 留前一版照常運作

## 索引現況（committed snapshot 完整性已驗）

- 凍結 commit：`d474c977e` 2026-06-17 05:08-05:18（最後一次成功 rebuild）
- staleness：**14 天**（06-17 → 07-01）
- 6 語 file present（committed snapshot，前夜驗 100% 有 8 鄰居）：zh-TW / en / ja / ko / es / fr 全 present，無 MISSING；git ls-files 6 檔在 index
- working tree clean（src/data/related 無未 commit 變動）
- 自 06-17 後新增 / 改寫文章（飯糰 #1182 / 台灣吧 #1183 / 彎彎 EVOLVE / Computex EVOLVE 等）fallback 同 category related（仍有 related，只是非語意，**不壞頁**）

## Handoff 三態

繼承上一 session（2026-06-30-050736，night 13）：

- [x] ~~night 13 graceful skip 收尾~~ → 本夜同樣 skip（**night 14**），索引仍 `d474c977e`
- [ ] 🚨 **embedding keystone 連續第 14 夜 skip**，escalation 自 06-20 拍板、vc 封頂 3，**只欠哲宇 A/B 不欠更多證據**。最快解：bge-m3 pull 到常駐 always-on 節點（m4max 本機最穩，免遠端 + 免 Tailscale 依賴 / 或 3090 monoame-design）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks。屬 fleet 基礎建設決策（§自主權邊界），非本 routine 自主權範疇
- [ ] 🛡️ 免疫 50 chronic yellow（多維度退化中），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 14 finale memory~~（本檔）
- [ ] staleness 現 **14 天** / 自 06-17 後新增文 fallback 同 category（仍不壞頁）。維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**（handoff 既定，escalation 已 capped vc=3 待哲宇 A/B）；下一夜若 4090 上線 or 本機 fallback 節點（m4max bge-m3）落地則正常 rebuild，否則 night 15 續記
- [ ] ⚠️ 旁路 Ollama backbone SPOF（embeddings/babel 共底座，14 夜），routine-audit-weekly 持續入鏡
