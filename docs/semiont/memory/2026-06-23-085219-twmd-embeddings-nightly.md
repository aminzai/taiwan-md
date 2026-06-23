# 2026-06-23-085219-twmd-embeddings-nightly

> routine `twmd-embeddings-nightly` — fleet bge-m3 語意索引重建。本夜 Stage 0 fleet-down graceful skip **連續第 6 夜**。

## BECOME ACK

```
mode=micro / 8 organ 最低=🛡️免疫 51 / Q14 cross-session continuity=PASS
```

Micro self-test 7 題全過（Q1-3 identity / Q8-9 信念+語氣 / Q10-11 commit+gene map / Q14 continuity）。
Q14 證據：過去 48hr git log 看到 babel-nightly（20+100 translations 兩夜）/ data-refresh am+pm（Step 11 連 27d）/ maintainer am+pm（vc reset 補 #615/#280 chronic label）/ companies i18n + NVIDIA ship + 黃仁勳/草東 EVOLVE。§神經迴路 active pattern：「routine 飛輪自轉清 entropy 但修不了自己的 device-dependent 底座」（embeddings 連夜 skip 本案）。

## Stage 0 — Preflight：fleet 不可達（graceful skip）

- **EMBED_HOST**（從 fleet registry 抽象層解析，非 hardcode）：`http://100.74.47.100:11434`（laptop-4090，registry services 含 embed + models 含 bge-m3，唯一一台 pull bge-m3 的節點）
- **可達性**：`curl /api/embeddings` → `http_code=000 / time=20.009s`（timeout）；`ping 100.74.47.100` → 2 packets transmitted, **100% packet loss**。節點離線（關機 / Tailscale 斷）。
- **判定**：per EMBEDDING-PIPELINE.md:55-63 Stage 0 — 不可達 = **skip，非 failure**。committed `src/data/related` 留著、fallback 同 category 照常、不壞頁。

## Stage 1-3 — 全 skip（無 rebuild / 無 commit）

- 不跑 `build-embeddings.mjs`（無 endpoint）。
- 不 commit（內容無變，per Stage 3 「無 diff → skip commit 不留空 commit」）。

## 索引現況（committed fallback 健康度，儀器化確認）

- 最後成功重建：`d474c977e` 2026-06-17 05:18（6 語）。
- **staleness = 6 天**（06-17 → 06-23）。
- committed snapshot 完整：6 語檔皆在，zh-TW 797 篇 / en-es-ja-ko-fr 700-801 篇，100% 8 鄰居健康。
- 最新文章（en 索引 801 vs 文章 ~820）約 ~10-20 篇 fallback 回同 category related，仍有 related，只是非語意鄰居。**不壞頁**。

## escalation 狀態（不重複 inflate）

- LESSONS `routine-device-dependent-offline` 已在 **vc=3（distill 門檻）**，docs/semiont/LESSONS-INBOX.md:376-384 完整記載，含 §defer 給觀察者 A/B：
  - **(A)** 開機讓 4090 恢復 always-on schtasks（embedding 單點解）
  - **(B)** 把 bge-m3 pull 到常駐 always-on 節點（3090 monoame-design 線上 / m4max 本機）+ 更新 registry `always_on` 欄優先序（embedding + spore broadcast 同時解）
- **本夜不 re-bump vc**：連 6 夜同一 SPOF instance = 同一 verification event 的延續，非新驗證。vc 機制目的是把重複訊號累積到可 promote 門檻——已達門檻（3），再每夜 +1 是 noise inflation（REFLEXES broken-instrument / vc 紀律）。結構訊號已完整捕捉，剩下只欠觀察者那一個 A/B 決定，不是欠更多 LESSONS 證據。
- per scheduled-task 鐵律「連 3 天 skip 才 escalate LESSONS」：早已滿足（night 1 of escalation = 06-20）。

## Beat 5 — 反芻

連續第 6 夜，跟第 5 夜同一句話：keystone 的 SSOT 在 repo 裡（`knowledge/` + bge-m3 模型），但 keystone 的**算力**掛在一台會關機的 laptop 上。飛輪每夜準時轉、Stage 0 每夜準時 skip、memory 每夜準時記——routine 能可靠地「優雅失敗」，這本身是健康的 graceful degradation。但「可靠地失敗」連 6 夜，就不再是 routine 該解的問題，是底座決策該解的問題。我能做的（抽象 endpoint / graceful skip / fallback 不壞頁 / vc 累積到門檻）都做完了。再多寫一條 LESSONS 不會讓 4090 開機。這條等的不是更多訊號，是哲宇按 A 或 B。

🧬

---

_v1.0 | 2026-06-23 08:52 +0800_
_session twmd-embeddings-nightly — fleet-down graceful skip 連續第 6 夜（4090 http 000 / 20s timeout / ping 100% loss）_
_誕生原因：cron 05:00 fire（本次手動 08:52 觸發），laptop-4090 節點離線，Stage 0 graceful skip_
_核心洞察：routine 能可靠地優雅失敗 6 夜本身是健康 graceful degradation，但「可靠失敗」連 6 夜揭露的是底座 device-dependent SPOF，等的是觀察者 A/B 決定不是更多 LESSONS 證據_
_LESSONS-INBOX：無新增（既有 routine-device-dependent-offline vc=3 已達門檻，本夜不 re-inflate）_

## Handoff 三態

繼承上一 session（2026-06-22-050853）：

- [x] ~~本夜 routine graceful skip 收尾~~ — 本夜同樣 skip（night 6），索引仍 06-17 snapshot
- [ ] 🚨🚨🚨🚨 **embedding keystone 連續第 6 夜 skip**，escalation 自 06-20 拍板未解，vc 已達 3 門檻封頂。最快解：bge-m3 pull 到常駐 always-on 節點（3090 monoame-design / m4max 本機）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks。**這條只欠哲宇 A/B，不欠更多證據**
- [ ] 🛡️ 免疫 51 chronic yellow（多維度退化中），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 6 finale memory（含 alert 強度升級框架）~~（本檔）
- [ ] staleness 現 6 天 / ~10-20 篇最新文 fallback 回同 category（仍不壞頁）。連 6 夜後 vc 已封頂，後續夜次維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**（避 noise inflation）；真正進展訊號是哲宇 A/B 落地或 4090 重新上線那一夜
