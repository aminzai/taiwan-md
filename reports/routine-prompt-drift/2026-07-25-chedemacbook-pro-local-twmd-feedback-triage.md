---
name: taiwanmd-routine-twmd-feedback-triage
description: （每天 07:00 Asia/Taipei = 23:00 UTC）。把讀者站上回報轉成 GitHub issue 接 MAINTAINER 飛輪，並把 canonical 紀錄落進 git（主權層）。
---

🧬 Taiwan.md routine: twmd-feedback-triage（每天 07:00 Asia/Taipei = 23:00 UTC）。把讀者站上回報轉成 GitHub issue 接 MAINTAINER 飛輪，並把 canonical 紀錄落進 git（主權層）。

🚨 STRICT BECOME GATE — 第一動作不可省略：跑 /twmd-become review 完整走 BECOME_TAIWANMD.md Step 0-9，Review mode self-test（含 Q13 anti-bias + Q14 cross-session）全過才動。ACK 一行寫 memory 頂部：`✅ BECOME ack: mode=review / 8 organ 最低=<consciousness-snapshot.sh> / Q13=PASS / Q14=PASS`。

業務邏輯 canonical：docs/pipelines/FEEDBACK-TRIAGE-PIPELINE.md（5 stage）+ 薄殼 skill .claude/skills/twmd-feedback-triage/SKILL.md。執行：

1. `git checkout main && git pull origin main`。
2. 先 dry-run 看分類：`node scripts/feedback/triage.mjs`（核 HG2 無 email / HG5 spam / HG6 dedupe）。
3. 確認 OK 才 `node scripts/feedback/triage.mjs --commit` — 讀 Supabase status='new' → spam/dedupe/分類 → `gh issue create`（from-feedback label，只放 display_name 不放 email，讀者文字 verbatim）→ 回寫 status + triage_note → 寫 git 主權 archive `docs/feedback/archive/{YYYY-MM}/{id}.md` + sync issue 留言進 §溝通紀錄。
   需環境變數 SUPABASE_URL + SUPABASE_SERVICE_KEY；未設則 emit「feedback backend 未配置, skip」**不算 fail**（escalation 只看 quality gate）。
4. 🔴 HARD gate：issue body 無 email（PII）/ 讀者文字不改寫 / **不以維護者身份回覆 close merge**（那留 MAINTAINER 人類 gate，per §自主權邊界）。
5. **收官前 `git add docs/feedback/archive/`**（HG9，讓回報+溝通落進 git）；`git add` 相關 memory/archive → `git commit` 標 `🧬 [routine] twmd-feedback-triage: ...` → `git push origin main`（main-direct，不開 PR）。
6. 跑 /twmd-finale 收官：memory 必含 BECOME ACK + file/reject/skip count + 開的 issue #N + archive 檔數 + Handoff 三態。

時序：07:00 開 from-feedback issue → 08:30 twmd-maintainer-am 同 cycle 收割 → 當天閉環。
