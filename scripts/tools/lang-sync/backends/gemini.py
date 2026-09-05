"""
backends/gemini.py — Google Gemini CLI subprocess backend.

Uses the `gemini` CLI tool (gemini-cli) which authenticates via Google Workspace
subscription (~/.gemini/oauth_creds.json). Provides direct access to Gemini models
without going through OpenRouter — independent quota.

Strengths: large context, strong multilingual (especially ja/ko/es/fr from a Google
training corpus), Google Workspace subscription absorbs cost.

Weaknesses: requires --skip-trust flag for non-interactive use; CLI overhead per call;
quota may hit "exhausted your capacity on this model. Your quota will reset after Xs"
but auto-retries.

Per哲宇 callout 2026-05-12 alongside codex: "用我的 gemini 訂閱處理".
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
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


class GeminiBackend(TranslationBackend):
    CAPABILITIES = BackendCapabilities(
        name="gemini",
        provider_kind="gemini-cli",
        model="gemini-2.5-pro",  # default; CLI may select via --model
        cost_kind="subscription",
        typical_latency_s=30,         # gemini CLI is faster than codex per call
        max_context_chars=1_000_000,  # gemini-2.5-pro has 1M context
        prc_refusal_risk_low=True,
        multilingual_strength=0.90,
        notes="Google Workspace subscription via gemini-cli. Strong multilingual + low refusal. "
              "Lower per-call overhead than codex but tighter QPM throttling.",
    )

    DEFAULT_TIMEOUT = 300
    AUTH_FILE = Path.home() / ".gemini" / "oauth_creds.json"

    def __init__(self, model: str = None, **config):
        super().__init__(**config)
        if model:
            self.CAPABILITIES = BackendCapabilities(**{**self.CAPABILITIES.__dict__, "model": model})

    def is_available(self) -> bool:
        if not shutil.which("gemini"):
            return False
        if not self.AUTH_FILE.exists():
            return False
        return True

    def translate(self, system: str, user: str, *, max_tokens: int = 32000, timeout: int = None) -> str:
        timeout = timeout or self.DEFAULT_TIMEOUT
        # gemini CLI doesn't have separate system/user roles — concatenate
        full_prompt = (
            "SYSTEM INSTRUCTIONS (follow strictly, do not echo):\n"
            "================================================================\n"
            f"{system}\n\n"
            "================================================================\n"
            "USER REQUEST:\n"
            f"{user}\n\n"
            "OUTPUT: ONLY the translated markdown content. No preamble, no commentary."
        )

        # TERM=dumb 是舊版 CLI 的選擇；gemini-cli ≥0.41 對 dumb terminal 直接 exit 1
        # （2026-07-18 出生戰役 health-check 病根），改給真實 TERM。
        env = {**os.environ, "TERM": "xterm-256color", "GEMINI_CLI_TRUST_WORKSPACE": "true"}
        cmd = ["gemini", "--skip-trust", "--prompt", full_prompt]
        if self.CAPABILITIES.model and self.CAPABILITIES.model != "default":
            cmd.extend(["--model", self.CAPABILITIES.model])

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                env=env,
            )
        except subprocess.TimeoutExpired:
            self._record_failure("timeout", f"gemini CLI timed out after {timeout}s")
            raise BackendTimeout(f"gemini CLI timed out after {timeout}s")
        except FileNotFoundError:
            self._record_failure("unavailable", "gemini CLI not installed")
            raise BackendUnavailable("gemini CLI not found in PATH")

        if result.returncode != 0:
            err = (result.stderr or result.stdout)[:500]
            # Quota exhaustion message
            if "exhausted your capacity" in err or "quota" in err.lower():
                self.mark_cool_down(300)
                self._record_failure("rate_limited", err)
                raise BackendRateLimited(err[:200], cool_down_until=self.cool_down_until())
            self._record_failure("bad_output", f"exit {result.returncode}: {err}")
            raise BackendBadOutput(f"gemini exit {result.returncode}: {err}")

        output = _extract_gemini_output(result.stdout)
        if not output or len(output) < 100:
            self._record_failure("bad_output", f"empty/tiny output: {len(output)} chars")
            raise BackendBadOutput(f"gemini produced empty/tiny output ({len(output)} chars)")

        self._record_success()
        return output


# ────────────────── helpers ──────────────────

_GEMINI_NOISE_PATTERNS = (
    re.compile(r"^Warning: 256-color support not detected.*$", re.MULTILINE),
    re.compile(r"^Ripgrep is not available.*$", re.MULTILINE),
    re.compile(r"^Attempt \d+ failed: .*Retrying after \d+ms\.\.\.$", re.MULTILINE),
    re.compile(r"^Loaded cached credentials\.$", re.MULTILINE),
)


def _extract_gemini_output(stdout: str) -> str:
    """Strip gemini CLI noise (color warnings, ripgrep fallback, retry messages)."""
    out = stdout
    for pat in _GEMINI_NOISE_PATTERNS:
        out = pat.sub("", out)
    return out.strip()


# ────────────────── Tier 7: paid API key path ──────────────────
#
# OBSERVER-QUEUE #18，哲宇 2026-09-05 拍板原話「tier 6 用 haiku, 7 用 gemini」。
# 完全獨立於上面的 GeminiBackend（CLI + Workspace 訂閱）——那條路 2026-07-18
# 起永久死亡（IneligibleTierError: UNSUPPORTED_CLIENT，需遷移 Antigravity，
# 帳號決策屬哲宇，不在本次任務範圍），2026-09-05 複測仍是同一個錯誤
# （`gemini --skip-trust --prompt ...` 幾秒內回同一個 exception）。這個類走
# Google Generative Language API 的個人 API key 路徑，跟訂閱/CLI 無關，
# 是否可用只取決於有沒有 GEMINI_API_KEY。

class GeminiPaidBackend(TranslationBackend):
    """Tier 7 最後手段——付費 API key，只在 Tier 6 也失敗時才碰（資格限制與
    每夜上限由 babel-dispatch.py 的 restricted worker 機制強制，這個類本身
    跟其他 backend 一樣是無狀態的可插拔 provider）。"""

    CAPABILITIES = BackendCapabilities(
        name="gemini-paid",
        provider_kind="gemini-api",
        model="gemini-2.5-pro",
        cost_kind="paid-per-token",
        typical_latency_s=60,
        max_context_chars=1_000_000,
        prc_refusal_risk_low=True,
        multilingual_strength=0.90,
        notes="Tier 7（2026-09-05 拍板）— Google Generative Language API 付費金鑰路徑，"
              "跟訂閱版 GeminiBackend（CLI，2026-07-18 起永久死亡）完全獨立的認證管道。"
              "未配置 GEMINI_API_KEY 時 skip 不 fail。",
    )

    API_URL_TMPL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    KEY_FILE = Path.home() / ".config" / "taiwan-md" / "credentials" / "gemini.key"
    ENV_FILE = Path.home() / ".config" / "taiwan-md" / "credentials" / ".env"
    DEFAULT_TIMEOUT = 300
    DEFAULT_MAX_TOKENS = 8192

    _warned_missing_key = False  # class-level：多個 worker 共用同一個 process 時只印一次

    def __init__(self, model: str = None, **config):
        super().__init__(**config)
        if model:
            self.CAPABILITIES = _dc_replace(self.CAPABILITIES, model=model)
        self._api_key = self._load_key()

    def _load_key(self) -> str | None:
        v = os.environ.get("GEMINI_API_KEY", "").strip()
        if v:
            return v
        if self.KEY_FILE.exists():
            v = self.KEY_FILE.read_text(encoding="utf-8").strip()
            if v:
                return v
        if self.ENV_FILE.exists():
            for line in self.ENV_FILE.read_text(encoding="utf-8").splitlines():
                if line.startswith("GEMINI_API_KEY="):
                    v = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if v:
                        return v
        return None

    def is_available(self) -> bool:
        if not self._api_key:
            if not GeminiPaidBackend._warned_missing_key:
                print("⚠️  Tier 7 未配置：GEMINI_API_KEY 未設定"
                      f"（{self.KEY_FILE} 或環境變數）— 需哲宇提供，skip 不算 fail",
                      file=sys.stderr)
                GeminiPaidBackend._warned_missing_key = True
            return False
        return True

    def translate(self, system: str, user: str, *, max_tokens: int = None, timeout: int = None) -> str:
        timeout = timeout or self.DEFAULT_TIMEOUT
        max_tokens = max_tokens or self.DEFAULT_MAX_TOKENS
        url = self.API_URL_TMPL.format(model=self.CAPABILITIES.model, key=self._api_key)
        payload = json.dumps({
            "systemInstruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
            "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.3},
        }).encode("utf-8")
        req = urllib.request.Request(url, data=payload, method="POST",
                                      headers={"content-type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:500]
            if e.code == 429:
                self.mark_cool_down(300)
                self._record_failure("rate_limited", body)
                raise BackendRateLimited(f"HTTP 429: {body}", cool_down_until=self.cool_down_until())
            if e.code in (400, 401, 403):
                self._record_failure("unavailable", body)
                raise BackendUnavailable(f"HTTP {e.code} (bad GEMINI_API_KEY or blocked?): {body}")
            self._record_failure("bad_output", f"HTTP {e.code}: {body}")
            raise BackendBadOutput(f"HTTP {e.code}: {body}")
        except (urllib.error.URLError, TimeoutError) as e:
            self._record_failure("timeout", str(e))
            raise BackendTimeout(f"gemini API timeout/network error: {e}")

        candidates = data.get("candidates") or []
        if not candidates:
            feedback = data.get("promptFeedback", {})
            self._record_failure("refusal", f"no candidates: {feedback}")
            raise BackendRefusal(f"gemini API returned no candidates (promptFeedback={feedback})")
        cand = candidates[0]
        finish_reason = cand.get("finishReason")
        parts = cand.get("content", {}).get("parts", []) or []
        text = "".join(p.get("text", "") for p in parts)

        if finish_reason == "MAX_TOKENS":
            self._record_failure("bad_output", "truncated (finishReason=MAX_TOKENS)")
            raise BackendBadOutput("output truncated (finishReason=MAX_TOKENS) — tail/footnotes lost, not saved")
        if not text or len(text) < 100:
            self._record_failure("bad_output", f"empty/tiny output: {len(text)} chars")
            raise BackendBadOutput(f"gemini API produced empty/tiny output ({len(text)} chars)")

        self._record_success()
        return text
