#!/usr/bin/env bash
# restart-vortex.sh — 一鍵重啟巴別塔四軌（含算力自檢與編組原則）
#
# 為什麼有這支：渦流的產線編組是三天實測演化出來的（模型×語言適配、
# 擅長語種共軌、專軌避單點），每次重啟手打四條長指令既慢又容易漏參數。
# 2026-07-27 哲宇帶機器出門前建立，回來一個指令續戰。
#
# 編組依據見 SQUEEZE-MODELS-MAX-PIPELINE.md §模型×語言適配／§編組原則。
# 用法：bash scripts/tools/lang-sync/restart-vortex.sh [--stale-only]

set -uo pipefail
cd "$(dirname "$0")/../../.." || exit 1
REPO=$(pwd)

L4090="http://100.74.47.100:11434"
D3090="http://100.101.135.15:11434"
MAC="http://127.0.0.1:11434"

echo "🗼 巴別塔渦流重啟 — $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# ── 前置：算力自檢（端點活著不等於能產出，但不通就一定不能用）──
echo "▸ 端點探測"
for pair in "mac=$MAC" "l4090=$L4090" "d3090=$D3090"; do
  name="${pair%%=*}"; url="${pair#*=}"
  if curl -s --max-time 6 "$url/api/version" >/dev/null 2>&1; then
    echo "   ✅ $name"
  else
    echo "   ❌ $name 不可達（Tailscale 開了嗎？該軌會空轉自動收工）"
  fi
done
echo ""

# ── 殘留清理（重啟前必做，避免雙份產線互撞）──
if pgrep -f "babel-dispatch" >/dev/null 2>&1; then
  echo "▸ 清理殘留產線"
  pkill -f "babel-dispatch" 2>/dev/null
  pkill -f "translate.py --group" 2>/dev/null
  sleep 3
fi

start() {   # start <logname> <描述> <args...>
  local log="$1"; shift
  local desc="$1"; shift
  nohup python3 -u scripts/tools/lang-sync/babel-dispatch.py "$@" \
    --order forward --rounds 300 --commit-every 50 > "/tmp/$log" 2>&1 &
  echo "   PID $! — $desc"
  disown
}

echo "▸ 起跑（全軍 forward 由新到舊；排序鍵：失敗沉底→新鮮窗→缺頁先於過期→編輯時間）"

# 雙 GPU 歐語軌：2026-07-28 preflight 近兩日實績顯示 d3090×ja=0%、
# d3090×ko=14%、l4090×ja=10%。弱適配不靠重試，先把日韓切出這條軌；
# en/es/fr 仍由兩台互相補位，保留節點級容錯。
if [ "${1:-}" = "--stale-only" ]; then
  start babel-stale-gpu.log "雙 GPU 三語 stale 專軌" --langs en,es,fr --priority p1 \
    --worker "l4090=ollama:gemma4:26b@$L4090" --worker "d3090=ollama:qwen3:32b@$D3090"
else
  start babel-gpu-euro.log "雙 GPU 歐語軌" --langs en,es,fr \
    --worker "l4090=ollama:gemma4:26b@$L4090" --worker "d3090=ollama:qwen3:32b@$D3090"
fi

# 本機 qwen3.6 改吃六語；近兩日 mac×ja/ar=0%、mac×ru=10%，三語切到
# nemotron 雲端軌，避免同一弱適配再燒一次完整翻譯成本。
start babel-mac-all.log "本機 qwen3.6 六語軌" --langs ko,es,fr,id,pt,hi \
  --worker "mac=ollama:qwen3.6:35b-a3b-coding-nvfp4@$MAC"

# nemotron 在葡俄阿印尼印地 42-60%，但翻越南語只有 2-6%——所以 vi 不進這軌。
# ja 暫移入此軌做實績驗收；若 n≥8 仍低於 15%，下一輪再切換模型。
start babel-cloud.log "雲端 nemotron×4（六語）" --langs ja,id,pt,hi,ar,ru \
  --worker "nemo=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \
  --worker "nemo2=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \
  --worker "nemo3=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free" \
  --worker "nemo4=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free"

# laguna 翻越南語 43-71% 是全場最佳（nemotron 只有 2-6%）——專軌用三併發避單點
start babel-vi-rescue.log "越南語專軌 laguna×3" --langs vi \
  --worker "laguna=openrouter:poolside/laguna-xs-2.1:free" \
  --worker "laguna2=openrouter:poolside/laguna-xs-2.1:free" \
  --worker "laguna3=openrouter:poolside/laguna-xs-2.1:free"

sleep 3
echo ""
echo "▸ 確認：$(pgrep -f babel-dispatch | wc -l | tr -d ' ') 條產線在跑"
echo ""
echo "接下來："
echo "  巡檢   bash scripts/tools/lang-sync/restart-vortex.sh --check  （或見 BABEL-VORTEX-LOOP.md §三重巡檢）"
echo "  進度   python3 scripts/tools/lang-sync/babel-pulse.py --no-commit"
echo "  渦流   讀 docs/pipelines/BABEL-VORTEX-LOOP.md 照它執行"
