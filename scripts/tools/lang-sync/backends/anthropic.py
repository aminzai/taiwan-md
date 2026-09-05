"""
backends/anthropic.py — Anthropic Claude API backend (Tier 6).

OBSERVER-QUEUE #18，哲宇 2026-09-05 拍板原話「tier 6 用 haiku, 7 用 gemini」。
Direct HTTP call to the Anthropic Messages API via plain urllib — no SDK
dependency, matching the zero-extra-dependency style of the other backends
in this directory.

**這不是** SQUEEZE §第五層「Claude sub-agent 委派」（spawn 一整個 Claude Code
Agent session 去翻一篇，主 session 手動派工、agent 自己判斷怎麼寫檔）。這個
backend 是單次無狀態 API call，跟 codex/gemini/openrouter 一樣可以插進
babel-dispatch.py 的 worker pool 裡自動跑——委派層的成本/彈性換來的是「模型
自己會判斷」，這裡換來的是「跟其他 backend 一樣可以無人值守跑一整夜」。

**資格限制與每夜上限不在這個檔案裡**（backend 不該知道任務優先序，跟其他
backend 一樣只是可插拔的 provider）。實際限制（只服務 P0 missing 與
CRITICAL(<0.5) 截斷檔、每夜上限 BABEL_TIER6_NIGHTLY_CAP）由呼叫端
babel-dispatch.py 的 restricted worker 機制強制——見該檔 §Tier 6/7。

需要 ANTHROPIC_API_KEY（環境變數，或
~/.config/taiwan-md/credentials/anthropic.key，或
~/.config/taiwan-md/credentials/.env 裡的 ANTHROPIC_API_KEY= 一行）。沒有
key 時 is_available() 回 False 並印一次性提示（「Tier 6 未配置」），cascade
自然跳過整個 backend——這是 skip 不是 fail，不會污染 fail_counts。
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import replace as _dc_replace
from pathlib import Path

from ._base import (
    BackendBadOutput,
    BackendCapabilities,
    BackendRateLimited,
    BackendRefusal,
    BackendTimeout,
    BackendUnavailable,
    TranslationBackend,
)

CREDS_DIR = Path.home() / ".config" / "taiwan-md" / "credentials"
KEY_FILE = CREDS_DIR / "anthropic.key"
ENV_FILE = CREDS_DIR / ".env"
API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"
# 2026-09-05 拍板當下查無 ~/.claude 或既有程式碼裡使用中的 Haiku model id
# 字串（環境裡沒有任何 backend 打過 Anthropic API），沿用哲宇任務指示裡
# 給的字串。若這個 id 之後過期，改這一行即可，不影響呼叫端。
DEFAULT_MODEL = "claude-haiku-4-5-20251001"

_warned_missing_key = False  # module-level：多個 worker 共用同一個 process 時只印一次


def _load_api_key() -> str | None:
    v = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if v:
        return v
    if KEY_FILE.exists():
        v = KEY_FILE.read_text(encoding="utf-8").strip()
        if v:
            return v
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("ANTHROPIC_API_KEY="):
                v = line.split("=", 1)[1].strip().strip('"').strip("'")
                if v:
                    return v
    return None


class AnthropicBackend(TranslationBackend):
    CAPABILITIES = BackendCapabilities(
        name="anthropic",
        provider_kind="anthropic-api",
        model=DEFAULT_MODEL,
        cost_kind="paid-per-token",
        typical_latency_s=180,
        max_context_chars=600_000,
        prc_refusal_risk_low=True,
        multilingual_strength=0.90,
        notes="Tier 6（OBSERVER-QUEUE #18，2026-09-05 拍板）— 付費 per-token，"
              "限 P0 missing + CRITICAL(<0.5) 截斷檔，每夜上限由 babel-dispatch "
              "強制。不受 PRC content policy 影響（REFLEXES #39 self-as-fallback）。",
    )

    DEFAULT_TIMEOUT = 300
    DEFAULT_MAX_TOKENS = 8192

    def __init__(self, model: str = None, **config):
        super().__init__(**config)
        if model:
            self.CAPABILITIES = _dc_replace(self.CAPABILITIES, model=model)
        self._api_key = _load_api_key()

    def is_available(self) -> bool:
        global _warned_missing_key
        if not self._api_key:
            if not _warned_missing_key:
                print(f"⚠️  Tier 6 未配置：ANTHROPIC_API_KEY 未設定（{KEY_FILE} "
                      "或環境變數）— skip，不算 fail", file=sys.stderr)
                _warned_missing_key = True
            return False
        return True

    def translate(self, system: str, user: str, *, max_tokens: int = None, timeout: int = None) -> str:
        timeout = timeout or self.DEFAULT_TIMEOUT
        max_tokens = max_tokens or self.DEFAULT_MAX_TOKENS
        payload = json.dumps({
            "model": self.CAPABILITIES.model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }).encode("utf-8")
        req = urllib.request.Request(
            API_URL, data=payload, method="POST",
            headers={
                "x-api-key": self._api_key,
                "anthropic-version": ANTHROPIC_VERSION,
                "content-type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:500]
            if e.code == 429:
                self.mark_cool_down(300)
                self._record_failure("rate_limited", body)
                raise BackendRateLimited(f"HTTP 429: {body}", cool_down_until=self.cool_down_until())
            if e.code == 401:
                self._record_failure("unavailable", body)
                raise BackendUnavailable(f"HTTP 401 (bad ANTHROPIC_API_KEY?): {body}")
            if e.code in (400, 403) and ("policy" in body.lower() or "blocked" in body.lower()):
                self._record_failure("refusal", body)
                raise BackendRefusal(f"HTTP {e.code}: {body}")
            self._record_failure("bad_output", f"HTTP {e.code}: {body}")
            raise BackendBadOutput(f"HTTP {e.code}: {body}")
        except (urllib.error.URLError, TimeoutError) as e:
            self._record_failure("timeout", str(e))
            raise BackendTimeout(f"anthropic API timeout/network error: {e}")

        stop_reason = data.get("stop_reason")
        content_blocks = data.get("content", []) or []
        text = "".join(b.get("text", "") for b in content_blocks if b.get("type") == "text")

        if stop_reason == "max_tokens":
            self._record_failure("bad_output", "truncated (stop_reason=max_tokens)")
            raise BackendBadOutput("output truncated (stop_reason=max_tokens) — tail/footnotes lost, not saved")
        if not text or len(text) < 100:
            self._record_failure("bad_output", f"empty/tiny output: {len(text)} chars")
            raise BackendBadOutput(f"anthropic produced empty/tiny output ({len(text)} chars)")

        self._record_success()
        return text
