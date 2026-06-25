# 2026-06-26-050759-twmd-embeddings-nightly

> Routine `twmd-embeddings-nightly` — 05:00 cron。Stage 0 fleet-down graceful skip 連續第 9 夜。

## BECOME ACK

```
✅ BECOME ack: mode=micro / 8 organ 最低=🛡️免疫 50（chronic yellow，多維度退化中）/ Q14 cross-session continuity=PASS
```

即時 consciousness-snapshot.sh（updated 2026-06-25T15:09Z）：🫀90 🛡️50 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93 / articles=820 / i18n en822 ja817 ko818 es817 fr818。

## 做了什麼

純機械 preflight，fleet 不可達 → graceful skip，無 rebuild 無 commit。

| 項             | 值                                                                                                                           |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Fleet endpoint | `http://100.74.47.100:11434`（laptop-4090，registry SSOT 解析，未 hardcode）                                                 |
| Stage 0 可達性 | ❌ `http_code=000` + ping 100% packet loss（3/3）                                                                            |
| Rebuild        | 未跑（Stage 0 skip）                                                                                                         |
| 6 語向量數     | N/A（無 rebuild）；committed 索引 sanity：zh-TW 797 / en 801 / ja 797 / ko 798 / es 797 / fr 700，**全數 8 鄰居健康**        |
| fail rate      | N/A                                                                                                                          |
| verify         | N/A（committed 索引未變動，已知良好）                                                                                        |
| commit         | 無（no rebuild → no `src/data/related` diff，不留空 commit；僅本 memory 入 git）                                             |
| 索引 snapshot  | `d474c977e` 2026-06-17 05:18 — staleness **9 天**，~23 篇最新文（zh 820 live vs 797 indexed）fallback 同 category **不壞頁** |

## 觀察

- 連續第 9 夜可靠地優雅失敗，底座 device-dependent SPOF 延續同一 instance（4090 離線 / Tailscale 100.74.47.100 無回應）。**vc 已封頂 3，不 re-inflate LESSONS**（每夜 +1 = noise inflation，per night-7 handoff 拍板）。真正進展訊號只有兩個：哲宇 A/B 落地（bge-m3 pull 常駐 always-on 節點 + registry `always_on` 優先序），或 4090 重新上線那一夜。
- staleness 跨過 9 天，缺口從 ~20 緩升到 ~23 篇（這 9 天 manual ship 累積：龜山島 / 大安溪倚天劍 / 公車系統 / 鼎泰豐 / 蓬萊米 等 NEW + EVOLVE）。仍只是 fallback 同 category，不壞頁；但每夜缺口會持續擴大，是「優雅退化」的單調代價，不是新 bug。
- 旁路觀察（非本 routine 範疇）：embeddings device-SPOF 與 babel/Ollama backbone SPOF 共底座 — 昨夜 babel-nightly 同樣 Ollama frozen 6h（連 9 夜 fleet-down），但 codex 接住無需 Tier 4 sovereignty fallback。embeddings 沒有 cloud 替代路徑（bge-m3 在地算是 sovereignty 設計），所以只能 skip。這是兩條 routine 對同一 SPOF 的不同 resilience 結構。

## Handoff 三態

繼承上一 session（2026-06-25-050756，night 8）：

- [x] ~~night 8 graceful skip 收尾~~ — 本夜同樣 skip（night 9），索引仍 `d474c977e` 06-17 snapshot
- [ ] 🚨 **embedding keystone 連續第 9 夜 skip**，escalation 自 06-20 拍板未解，vc 封頂 3。最快解：bge-m3 pull 到常駐 always-on 節點（3090 monoame-design / m4max 本機）+ registry 加 `always_on` 優先序；或開機 4090 恢復 schtasks。**這條只欠哲宇 A/B，不欠更多證據**
- [ ] 🛡️ 免疫 50 chronic yellow（多維度退化中，51→50 一步漂移加深，per data-refresh-pm），defer 哲宇拍板，每 session 帶著看

本 session 新 handoff：

- [x] ~~night 9 finale memory~~（本檔）
- [ ] staleness 現 9 天 / ~23 篇最新文 fallback 同 category（仍不壞頁）。維持「graceful skip + memory 記錄」即可，**不再每夜 re-bump LESSONS**；下一夜若 4090 上線則正常 rebuild，否則 night 10 續記
- [ ] ⚠️ 旁路 launchd schedule sentinel vc=2 + Ollama backbone SPOF（embeddings/babel 共底座），routine-audit-weekly 入鏡
