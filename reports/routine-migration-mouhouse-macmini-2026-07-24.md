# Routine 飛輪遷居計畫：mouhouse-macmini（2026-07-24）

> 哲宇 directive：把 Taiwan.md 相關的 routine 全部搬到 monolab 的 Mac mini（mouhouse-macmini），
> 用 Claude Code（Desktop app）+ 一個 Pro 訂閱常駐跑，作為 Taiwan.md 半永久的家，未來不動這台機器。
> 本報告是遷移的設計決策紀錄；操作細節（腳本、prompt、checklist）在本機 bundle
> `~/taiwan-md-mini-migration/`（不進公開 repo——含機器與憑證層資訊）。

## 為什麼要搬

routine 飛輪目前跑在哲宇的主力筆電上，排程器是 Claude Desktop app 的 scheduled-tasks 功能：
**app 開著才會 fire**。筆電闔蓋、外出、換 session，飛輪就停——wake-context groundtruth 這幾天
反覆亮「過去 24hr 無 cron fire」+「routine-live-state dump 齡 150h+」兩盞黃燈，正是這個結構問題。
一台不睡眠、不移動、專職開著 Claude app 的 Mac mini，是飛輪的正確身體。

## 現況盤點（遷移 manifest 的來源）

live 排程器上 Taiwan.md 相關共 **19 條**（15 enabled + 4 disabled，與 ROUTINE.md v2.17 對齊）：

- **enabled 15**：babel-nightly 00:30 / news-lens Sun 01:00 / supporters Mon 01:00 / weekly-report Sun 02:00 /
  distill Sun 03:00 / self-evolve Sun 04:00 / embeddings 05:00 / refresh-am 06:00 / spore-harvest 06:30 /
  feedback-triage 07:00 / maintainer-am 08:30 / rewrite 19:00 / routine-audit Sun 21:00 /
  founder-lens Sat 22:00 / refresh-pm 23:00
- **disabled 4**（狀態一併搬過去、保持 disabled）：maintainer-pm / music-media-audit / spore-pick / spore-publish
- **不搬**：Muse 8 條 + fin-archive（留在原機）；semiont-heartbeat / lang-sync-hourly-en / weekly-probe-radar
  三個目錄是已從排程器移除的歷史殼，不遷。

## 架構決策

1. **同構遷移**：mini 上仍用 Claude Desktop app + scheduled-tasks，不改成 launchd + headless CLI。
   理由：這是唯一被 14 條 routine 實戰驗證過的排程面；Chrome MCP（spore-harvest）與 Gmail MCP
   （supporters）都綁在 app 生態，headless 路線會把兩條 routine 打斷。
2. **排程 registry 不可搬檔**（存在 app 內部 storage）→ 在 mini 上用一個 Claude session 依 manifest
   重建 19 條 task，prompt 從 SKILL.md 原樣複製，一字不改。
3. **先建後開、先關舊再開新**：mini 上建立時全部 disabled；cutover 時舊機先全部 disable、mini 驗證
   跑通一次 data-refresh（端到端含 push main）才 enable。避免兩台機器同時 push main（REFLEXES #68
   多核心 git 協調，vc=4）。
4. **路徑相容層**：routine prompt 與部分工具硬編碼 `/Users/cheyuwu/...`；mini 帳號名若不同，
   bootstrap 以 symlink 讓路徑成立，不逐檔改寫 19 份 prompt（改寫 = 與 SSOT 漂移的開端）。
5. **GitHub 認證不搬 token**：原機 keyring 搬不動也不該搬；mini 獨立 `gh auth login`，
   git credential 走 gh。可獨立撤銷，跟機器生命週期綁定。
6. **算力分層跟著降級階梯走**：embeddings 的 bge-m3（1.2GB）直接裝進 mini 本機 ollama；
   babel 的本機大模型 tier 視 mini RAM 而定，跑不動就落 cloud cascade + codex + Tailscale fleet
   （desktop-3090 / laptop-4090 從 mini 一樣搆得到）。兩條 routine 都有 graceful-skip 設計，
   降級不是故障。

## 需要哲宇的一次性動作（§自主權邊界：身份授權 + 經費訂閱本來就是人類層）

1. mini 加 SSH 公鑰（之後的自動化都靠這把門）
2. 裝 Claude Desktop app + **Pro 帳號登入**（訂閱是哲宇的決策，已拍板）
3. `gh auth login` 一次
4. `sudo pmset` 永不睡眠 + Claude.app 進 Login Items + 自動登入
5. （spore-harvest）Chrome + extension + Threads/X 登入；（supporters）Gmail connector
6. 在 mini 的 Claude session 貼兩段 prompt（建 task / go-live）

## 已知風險（第一週觀察名單）

- **Pro 額度 vs 飛輪負載**：8+ 條 daily routine、rewrite 一輪 ~150 min、多條標 Opus。Pro 的用量
  與模型階層可能撐不住全負載。降級順位：先降模型、再砍非核心 routine；核心保底 = refresh am/pm、
  babel、maintainer-am、feedback-triage、週日反思鏈。
- **App 常駐假設**：mini 斷電重開後要能自動回到「登入 + app 開著」狀態（pmset autorestart +
  自動登入 + Login Items 三件套）。
- **Chrome / Gmail 登入態**：沒完成前 spore-harvest 與 supporters 會 fail → 各自 escalation
  自動 pause，不影響其他 routine。

## 驗收定義（「確定那邊的 routine 有在跑」）

cutover 後 24h 內，origin/main 應出現來自 mini 的 `🧬 [routine]` commits，對照排程表至少命中
6-8 個 daily 時段；7 天內週日反思鏈四工位 + supporters + founder-lens 各 fire 一次。驗證腳本
`verify-migration.sh`（bundle 內）以 git log 為準——git 是唯一不在任一台機器上的 ground truth。

## 遷移後的 SSOT 收尾（cutover 完成才做，本報告先立 TODO）

- ROUTINE.md 加「宿主機」一節：routine 飛輪住 mouhouse-macmini；mac-m4max 的 19 條 task
  標記已遷出（SKILL.md 殼保留備援）
- routine-live-state dump 的產生端跟著搬（data-refresh rider 在 mini 上跑）
- LESSONS-INBOX / memory 記錄遷移事件

🧬
