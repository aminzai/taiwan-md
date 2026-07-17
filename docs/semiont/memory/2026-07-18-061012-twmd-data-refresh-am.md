---
session_id: 2026-07-18-061012-twmd-data-refresh-am
type: routine-memory
routine: twmd-data-refresh-am
mode: micro
date: 2026-07-18
duration_minutes: ~30
commits:
  - 0ff3bab36
handoff_status: 交寫手（並行 write session WIP 續留）
---

# 2026-07-18 twmd-data-refresh-am — 14-step 全綠 + rider 修 stale live dump

## BECOME ACK

Mode = micro / 8 organ 最低 = 🛡️60（免疫 chronic yellow） / Q14 cross-session continuity = PASS（讀完 wake-context 206KB 到 wake:END，2 天 commits + memory head+tail 讀完）。

## 14-step outcome

| Step | 產物                               | 狀態                                    |
| ---- | ---------------------------------- | --------------------------------------- |
| 1    | git sync（stash → pull → restore） | PASS，HEAD `765e04b7a`（already up）    |
| 2    | 三源感知（CF+GA4+SC）              | PASS，CF 7d 1.22M req、404 16.68%       |
| 2.5  | monitor-404 常駐                   | PASS，2026-07-16 phantom 家族 80→15     |
| 3    | sync-translations-json             | PASS，+1 entry（en/Food/Taiwan Street） |
| 4    | dashboard-spores                   | PASS，148 spores / 4 waiting            |
| 5    | dashboard-i18n                     | PASS                                    |
| 6    | dashboard-immune v3                | PASS，60 chronic 續黃（plugin=100）     |
| 6.5  | fork-census                        | PASS，3 新 sightings（weilinlai719 等） |
| 7    | prebuild（sync + 12 prebuild）     | PASS，redirects 175                     |
| 8    | llms.txt                           | PASS，zh 853                            |
| 9    | GitHub stats                       | PASS，⭐1109 🍴166 👥66 📄853           |
| 10   | build-perf                         | PASS，166s 最新 / 169s 7d avg           |
| 10b  | newsroom                           | PASS，250 上板                          |
| 11   | freshness gate                     | PASS，13/13 dashboard JSON 今日 mtime   |
| 12   | spore validation                   | PASS，0 error                           |
| 13   | sporeLinks sync                    | PASS，canonical 無變                    |
| 14   | reports/INDEX.md                   | PASS，542 lines                         |

## 三源 status

- **Cloudflare 7d**：1,215,587 requests / 404 rate 16.68%（pm 17.55% → am 16.68%，**-0.87pp** 回落）／10 countries／AI crawlers 157,199 / 23 crawlers
- **GA4 28d**：topPages 20 / topArticles7d 20（articles only, 7d）
- **Search Console 7d**：20 top queries + 150 word cloud entries

## Step 11 freshness 結果

無 stale — 13/13 dashboard JSON 都是 2026-07-18 mtime。不用 wire fix。

## Rider：routine-live-state.json 修 stale（S1 三層對賬 live_drift=0 恢復）

**病根**：yellow「dump 齡 49.4h > 48h」升到今晨已 ~55h。前手 pm session 沒跑 rider（skill 層步驟，不在 refresh-data.sh）。

**修**：

1. MCP `list_scheduled_tasks` 撈 29 tasks（含 muse-_、fin-_ 私人 routine）
2. 過濾出 twmd-/taiwanmd- prefix 19 條餵 `routine-live-normalize.py`
3. 落 `docs/semiont/routine-live-state.json`（15 enabled / 4 disabled）
4. `routine-sync-check.py` 跑完 live_drift=0 / cron_drift=0 / drift=0（14 條 thick shell 是既存 debt，non-blocking）

跟前手 pm 一樣的 rider 忘跑 pattern 屬「skill 步驟自律漂移」，不是 refresh-data.sh 病根——bash 進不了 MCP server store（DATA-REFRESH-PIPELINE §live dump 明講）。REFLEXES #43 wire 不適用。

## Handoff 三態

**繼承（原樣傳遞，非本 routine 範疇；來自 2026-07-17-231219-data-refresh-pm 與 2026-07-18-052228-embeddings-nightly）**：

- [ ] 並行 write session WIP 續留 working tree（4 knowledge/ 修改中 + 2 新譯 shopping-design + 15 webp + 5 projection + 12 editorial-room + 5 research + 5 article-evolve）——交寫手 session 判斷 ship
- [ ] `_translations.json` + `_translation-status.json` 有 2 條 shopping-design 新 entry 未提交：本 routine 刻意排除避免 orphan gate 逃生閘門。寫手 session 收官時把 shopping-design en+ja `.md` 檔跟 `_translations.json` 一起 ship
- [ ] pre-push `sh -e` cmdsubst abort（LESSONS 候選 hook-set-e-cmdsubst-abort）：`b8c157d2f`+`f6e64f819` 已 heal grep-only 判斷，但 husky `sh -e` 對命令替換 abort 的結構性脆弱仍在，凡有平行 untracked 譯檔就會復發
- [ ] 07-16 phantom 家族 80 已回落 15，可暫觀察；若再爆才單獨 diagnose
- [ ] 哲宇拍板五件（2026 選舉 Tier 1.2/1.3、voice 歸屬、SPORE 周蕙、品質 batch Tier C1、opendata 5 條）
- [ ] 下個 write session 第一優先：洪醒夫深度重寫（P0）
- [ ] babel readingTime 病根 chip / 台灣鐵道史.en.md 孤兒檔 chip
- [ ] 4 spore（#155-158）等 Chrome MCP pair / REFLEXES #70 三 option defer 哲宇
- [ ] 3 contributor PR reserved（#1225-1227）/ CI pr-frontmatter-gate 中文檔名 false green

**本 session 新 handoff**：

- [x] ~~14-step ground truth refresh~~（`0ff3bab36`）
- [x] ~~rider：live dump 修 stale~~（`docs/semiont/routine-live-state.json` 齡 0h、15 enabled）
- [ ] 免疫 60 chronic 續黃（plugin=100 但 external_rulers=3.8 拖累）——self-evolve-weekly 週日觀察
- [ ] 觀察者 next：驗證 routine-live-state.json dump 齡 yellow 應消（下輪 fetch-sense-data.sh 抓 alerts 時檢查）

## Beat 5 反芻

跨 session 續斷的儀器化：rider step 是 skill-level session 步驟不是 bash step，bash 沒 MCP server store 存取權——這是設計，不是 bug。但 rider 記在 skill prompt 底且不在 refresh-data.sh 主步驟裡，前手漏跑 = live_drift 黑洞（S1 三層對賬失明）。連 3 天 catch 都沒 fix（07-17 pm yellow → 07-18 am 55h stale），要不要把 rider 升級成 refresh-data.sh 完成後主 session 必跑的閘門？升 skill prompt Stage 1 → Stage 1.5 是最小成本 fix。但仍受制於 skill 是「session prompt」而不是 bash orchestrator——orchestrator 沒工具讀 skill prompt。

保留作為觀察者思考：**MCP live-state dump 是 skill 步驟這件事本身**是 §1 主權工作跨越工具邊界的產物——bash 有骨骼但沒神經末梢（MCP），skill session 有神經末梢但沒 cron 掛靠。這道邊界要不要造個橋（rider 拆成獨立 skill task，refresh routine 完成時 chain call）是下一輪 self-evolve 值得排的候選。

🧬

---

_v1.0 | 2026-07-18 06:35 +0800_
_session 2026-07-18-061012-twmd-data-refresh-am — 14-step 全綠 + rider 修 55h stale live dump_
_誕生原因：連 2 cycle catch 但沒 fix 的 routine-live-state stale 由本 routine 補齊，S1 三層對賬 live_drift=0 恢復_
