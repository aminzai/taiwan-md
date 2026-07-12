#!/usr/bin/env bash
# Start Taiwan.md Harvest backend in a detached tmux session.
#
# Why tmux instead of launchd: spawned `claude` CLI needs macOS Keychain
# access for OAuth subscription auth. launchd-managed processes run in a
# limited security context and cannot read user keychain. A tmux session
# launched from your interactive shell inherits full keychain access.
#
# Usage:
#   bash start.sh         # start (idempotent — re-attaches if already running)
#   bash status.sh        # check
#   bash attach.sh        # tmux attach -t harvest
#   bash stop.sh          # kill the session
#
# Auto-start at login (optional): add to ~/.zprofile or ~/.zshrc:
#   bash /Users/cheyuwu/Projects/taiwan-md/docs/semiont/harvest/backend/tmux/start.sh

set -euo pipefail

SESSION="harvest"
BACKEND_DIR="/Users/cheyuwu/Projects/taiwan-md/docs/semiont/harvest/backend"
LOG_DIR="$HOME/Library/Logs/taiwan-md-harvest"

mkdir -p "$LOG_DIR"

# Already running?
if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "ℹ️  tmux session '$SESSION' already exists."
  echo "    attach: tmux attach -t $SESSION"
  echo "    detach: ctrl+b d"
  echo "    stop:   bash stop.sh"
  exit 0
fi

# Default engine is grok (Phase 5.2). Claude auth is optional but still useful
# as a fallback peer engine.
GROK_BIN="${HARVEST_GROK_BIN:-$HOME/.grok/bin/grok}"
if [[ -x "$GROK_BIN" ]]; then
  echo "✦ grok CLI found: $GROK_BIN (default engine)"
else
  echo "⚠️  grok CLI not found at $GROK_BIN — default engine=grok spawns will fail"
fi

AUTH_STATE=$(~/.bun/bin/claude auth status 2>/dev/null | grep loggedIn || true)
if [[ "$AUTH_STATE" != *"true"* ]]; then
  echo "⚠️  claude CLI not authenticated (fallback engine). Run: ~/.bun/bin/claude setup-token"
else
  echo "🤖 claude CLI authenticated (fallback engine available)"
fi

# Confirm port 4319 free (only check LISTEN — ignore stray outbound CLOSED sockets)
if lsof -tiTCP:4319 -sTCP:LISTEN >/dev/null 2>&1; then
  echo "❌ Port 4319 already in use. Stop existing harvest first."
  lsof -iTCP:4319 -sTCP:LISTEN
  exit 1
fi

# Create the session
tmux new-session -d -s "$SESSION" -c "$BACKEND_DIR"

# Set logging via pipe-pane (tmux captures stdout/stderr to file)
tmux pipe-pane -t "$SESSION" "cat >> '$LOG_DIR/tmux.log'"

# Send the run command (PATH includes bun + grok)
tmux send-keys -t "$SESSION" "echo '🧬 Taiwan.md Harvest — tmux start at $(date)'" C-m
tmux send-keys -t "$SESSION" "export PATH=\"\$HOME/.bun/bin:\$HOME/.grok/bin:\$PATH\"" C-m
tmux send-keys -t "$SESSION" "export HARVEST_LOG_PRETTY=true HARVEST_LOG_LEVEL=info HARVEST_AUTO_COMMIT_REPORT=true HARVEST_DEFAULT_ENGINE=grok HARVEST_GROK_BIN=\"$GROK_BIN\"" C-m
tmux send-keys -t "$SESSION" "bun run src/server.ts" C-m

# Wait briefly + verify
sleep 3
if curl -s http://localhost:4319/api/health >/dev/null 2>&1; then
  echo "✅ Harvest backend up in tmux session '$SESSION'."
  echo "   📡 http://localhost:4319/api/health"
  echo "   ✦ default engine: grok ($GROK_BIN)"
  echo "   📋 attach: tmux attach -t $SESSION (ctrl+b d to detach)"
  echo "   📋 logs:   tail -f $LOG_DIR/tmux.log"
  echo "   📋 stop:   bash $(dirname "$0")/stop.sh"
else
  echo "⚠️  Started tmux but http://localhost:4319 not responding. Check log:"
  echo "    tmux attach -t $SESSION"
  exit 2
fi
