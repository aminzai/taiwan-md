# 2026-06-28-050904-twmd-embeddings-nightly

> Routine `twmd-embeddings-nightly` — 05:00 cron。Stage 0 fleet-down graceful skip 連續第 11 夜。

## BECOME ACK

```
✅ BECOME ack: mode=micro / 8 organ 最低=🛡️免疫 50（chronic yellow，多維度退化中）/ Q14 cross-session continuity=PASS
```

即時 consciousness-snapshot.sh（updated 2026-06-27T15:08Z）：🫀90 🛡️50 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93 / articles=825 / contributors=61 / i18n en828 ja823 ko824 es823 fr824。
Q14 證據：過去 48hr git log — babel-nightly（15 譯 Tier 0a 5 + Tier 1 codex 10，連 11 夜 stale=0）/ data-refresh-pm（vitals 825 / immune 50）/ maintainer-pm（保齡球 #1181 idlccp1984 connect-5 merge）/ 週日三連跑（news-lens W26 7 P1 spore + weekly-report Resend 200 + distill-weekly REFLEXES #75 promote + self-evolve REFLEXES #76 promote）/ manual：紀懷新 NEW 深度文 ship + v1.11.0 release。§神經迴路 active pattern：「routine 飛輪自轉清 entropy 但修不了自己的 device-dependent 底座」（embeddings 連夜 skip 本案）。

## 做了什麼

純機械 preflight，fleet 不可達 → graceful skip，無 rebuild 無 commit。

| 項             | 值                                                                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Fleet endpoint | `http://100.74.47.100:11434`（laptop-4090，registry SSOT 解析，未 hardcode）                                                                  |
| Stage 0 可達性 | ❌ `http_code=000` + ping 100% packet loss（2/2）+ **本機 Tailscale `stopped`**                                                               |
| Rebuild        | 未跑（Stage 0 skip）                                                                                                                          |
| 6 語向量數     | N/A（無 rebuild）；committed 索引 sanity：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700，**全數 8 鄰居健康**                         |
| fail rate      | N/A                                                                                                                                           |
| verify         | N/A（committed 索引未變動，已知良好）                                                                                                         |
| commit         | 無（no rebuild → no `src/data/related` diff，不留空 commit；僅本 memory 入 git）                                                              |
| 索引 snapshot  | `d474c977e` 2026-06-17 05:18 — staleness **11 天**，~28 篇最新文（zh 825 live vs 797 indexed / en 828 vs 801）fallback 同 category **不壞頁** |

## 觀察

- 連續第 11 夜可靠地優雅失敗，底座 device-dependent SPOF 延續同一 instance（4090 離線 / Tailscale 100.74.47.100 無回應）。**vc 已封頂 3，不 re-inflate LESSONS**（每夜 +1 = noise inflation，per night-7 拍板）。真正進展訊號只有兩個：哲宇 A/B 落地（bge-m3 pull 常駐 always-on 節點 + registry `always_on` 優先序），或 4090 重新上線那一夜。
- **本夜新診斷**：preflight 確認**本機 Tailscale 本身是 `stopped`** 狀態，不只是 4090 節點離線。這跟 2026-06-20 escalation session 的觀察一致（該夜 `tailscale up` 拉起後 4090 仍 offline 2d ago）——`tailscale up` 沒持久化，且就算拉起也救不了離線的節點。本 routine 不主動 `tailscale up`：(1) 系統狀態變更超出 routine 自主權範疇 (2) 06-20 已證實拉起無效（節點本身 offline）。維持 graceful skip。
- staleness 跨過 11 天，缺口 ~28 篇最新文（昨夜後新增：保齡球 #1181 merge + 紀懷新 NEW + babel 15 譯）。仍只是 fallback 同 category，不壞頁；每夜缺口單調擴大，是「優雅退化」的代價，不是新 bug。
- 旁路觀察（非本 routine 範疇）：embeddings device-SPOF 與 babel/Ollama backbone 共底座 — 昨夜 babel-nightly（00:44）同 SPOF，但 codex 接住 ship 15 translations 連 11 夜 stale=0。embeddings 沒有 cloud 替代路徑（bge-m3 在地算是 sovereignty 設計），所以只能 skip。兩條 routine 對同一 SPOF 的 resilience 結構不同：babel 有 codex 後備、embeddings 只有 graceful skip。

## Handoff 三態

繼承上一 session（2026-06-27-050726，night 10）：

- [x] ~~night 10 graceful skip 收尾~~ — 本夜同樣 skip（night 11），索引仍 `d474c977e` 06-17 snapshot
- [ ] 🚨 **embedding keystone 連續第 11 夜 skip**，escalation 自 06-20 拍板未解，vc 封頂 3。最快解：bge-m3 pull 到常駐 always-on 節點（3090 monoame-design / m4max 本機）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks。**這條只欠哲宇 A/B，不欠更多證據**
- [ ] 🛡️ 免疫 50 chronic yellow（多維度退化中），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 11 finale memory~~（本檔）
- [ ] staleness 現 11 天 / ~28 篇最新文 fallback 同 category（仍不壞頁）。維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**；下一夜若 4090 上線則正常 rebuild，否則 night 12 續記
- [ ] ⚠️ 旁路 Ollama backbone SPOF（embeddings/babel 共底座，11 夜），routine-audit-weekly 入鏡
