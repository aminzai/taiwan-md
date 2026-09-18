#!/bin/bash
# launchd com.taiwanmd.babel.nightly（keepalive）的入口。
#
# 歷史：09-14 那班用 `launchctl submit` 掛了 keepalive，指令寫在 /tmp；09-18 改寫
# 三件事（起跑先對 origin 去重、地端 worker 由 fleet 核發、--order forward）；
# 09-19 搬進 repo（/tmp 重開機即消失，keepalive 會空轉）並再改兩件事：
#   1. 不再寫死 --langs 清單——dispatcher 預設就從 langs.py ENABLED_TRANSLATION_LANGS
#      取「有缺口的語言」，寫死清單只會讓新語言在無人察覺下整批漏掉（routine
#      prompt 明文警告過，本 wrapper 自己就是活體標本：12 語硬編）
#   2. 弱適配切軌——每次起跑用 babel-weak-lanes.py 從近兩日實績算 backend×語言
#      的弱格，餵 --worker-skip-langs，讓 worker 把輪次讓給擅長的語言
#
# 重掛方式（改完本檔後）：
#   launchctl remove com.taiwanmd.babel.nightly
#   launchctl submit -l com.taiwanmd.babel.nightly -o /tmp/babel-launchd.out -e /tmp/babel-launchd.err \
#     -- /bin/bash /Users/musebase/Projects/taiwan-md/scripts/tools/lang-sync/babel-launch-wrapper.sh
# 注意 remove 會殺掉正在跑的 dispatcher：先打撈工作樹裡驗過但沒 commit 的譯文
# （status.py 看到檔案就算 fresh，沒 commit 的完稿不會再排進佇列，09-18 教訓）。
set -u
cd /Users/musebase/Projects/taiwan-md || exit 1
git fetch -q origin main 2>/dev/null || echo "wrapper: git fetch 失敗，沿用舊的 origin/main ref" >&2
python3 scripts/tools/lang-sync/babel-origin-exclude.py >&2 || echo "wrapper: 去重清單產生失敗，沿用上一份 .taiwanmd/babel-exclude.tsv" >&2

FLEET_WORKERS="$(~/Projects/muse-bot/fleet/fleetctl workers --service llm --format babel 2>/dev/null)"
[ -z "$FLEET_WORKERS" ] && echo "wrapper: fleet 未核發任何地端 worker，本輪只有雲端 worker" >&2
CLOUD_WORKERS="--worker nemo=openrouter:nvidia/nemotron-3-ultra-550b-a55b:free --worker lagunas=openrouter:poolside/laguna-s-2.1:free"

# shellcheck disable=SC2086
SKIP_LANES="$(python3 scripts/tools/lang-sync/babel-weak-lanes.py --explain $FLEET_WORKERS $CLOUD_WORKERS )"
[ -n "$SKIP_LANES" ] && echo "wrapper: 弱適配切軌 → $SKIP_LANES" >&2

# shellcheck disable=SC2086
exec python3 scripts/tools/lang-sync/babel-dispatch.py \
  $FLEET_WORKERS \
  $CLOUD_WORKERS \
  $SKIP_LANES \
  --exclude-file .taiwanmd/babel-exclude.tsv \
  --order forward --rounds 200 --commit-every 10
