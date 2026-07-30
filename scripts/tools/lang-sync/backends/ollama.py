"""
backends/ollama.py — Local Ollama HTTP API backend.

Per REFLEXES #49 "v2.0 4-tier cascade" — Ollama is the sovereignty backbone, not a backup.
Cloud free-tier consistently refuses last-20% sovereignty-sensitive content (心戰 /
戒嚴 / 兩岸 / 黑名單 / 政治歷史敘事). Local LLM永遠收下, 0 refusal rate observed.

Default model: qwen3.6:35b-a3b-coding-nvfp4 (21GB GPU, Alibaba open weights —
「Western」原註是事實錯誤, 2026-07-05 dna-audit 修正). Local inference 繞過雲端
policy layer, 但 qwen 訓練資料來自阿里; sovereignty-sensitive 的 Tier 4 本機
fallback 是否換 gemma4 家族 pending 哲宇 (audit 決策 4)。fleet 端 6/14 bench
後已 gemma4-only (REMOTE-GPU-PIPELINE)。
Alternatives: taide-gemma3-12b:2602-q4km, gemma4:e4b-nvfp4 (lighter).

Trade-off vs cloud:
- 永遠 available (no rate limit, no auth churn, no provider drift)
- Slower (sequential, GPU contention if multi-process)
- Quality below cloud tiers but well above the 「永遠收下」threshold

Per MANIFESTO §sovereignty preservation: Local LLM is structural insurance against
PRC content policy infection of multi-lang projection.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

from ._base import (
    BackendBadOutput,
    BackendCapabilities,
    BackendTimeout,
    BackendUnavailable,
    TranslationBackend,
)


class OllamaBackend(TranslationBackend):
    CAPABILITIES = BackendCapabilities(
        name="ollama",
        provider_kind="ollama",
        model="qwen3.6:35b-a3b-coding-nvfp4",
        cost_kind="local-compute",
        typical_latency_s=180,     # GPU dependent; 21GB model on Apple Silicon
        max_context_chars=130_000,
        prc_refusal_risk_low=True, # local inference（無雲端 policy 層；0 refusal 實測）— 但 qwen 是阿里模型非西方訓練資料，Tier 4 主權定位 pending 哲宇（dna-audit 決策 4）
        multilingual_strength=0.78,
        notes="Sovereignty backbone (REFLEXES #49). 0 refusal observed on Taiwan content. "
              "Slower than cloud but永遠 available. GPU contention → single-process serial.",
    )

    DEFAULT_TIMEOUT = 900  # local model + large article can be slow
    API_URL = "http://localhost:11434/api/chat"

    def __init__(self, model: str = None, host: str = None, **config):
        super().__init__(**config)
        # host + model are env-overridable so the same backend targets a REMOTE
        # sovereignty-safe GPU node from the fleet without a code change:
        #   eval "$(bash scripts/tools/lang-sync/fleet-endpoint.sh --export)"
        # The fleet (~/Projects/muse-bot/fleet) owns node selection + connection;
        # this just reads OLLAMA_HOST/OLLAMA_MODEL. See REMOTE-GPU-PIPELINE.md.
        self.host = host or os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        model = model or os.environ.get("OLLAMA_MODEL")
        if model:
            # update CAPABILITIES with custom model
            self.CAPABILITIES = BackendCapabilities(
                **{**self.CAPABILITIES.__dict__, "model": model}
            )

    def is_available(self) -> bool:
        try:
            req = urllib.request.Request(f"{self.host}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read())
                models = [m["name"] for m in data.get("models", [])]
                return self.CAPABILITIES.model in models or any(
                    m.startswith(self.CAPABILITIES.model.split(":")[0]) for m in models
                )
        except Exception:  # noqa: BLE001
            return False

    def translate(self, system: str, user: str, *, max_tokens: int = 32000, timeout: int = None) -> str:
        timeout = timeout or self.DEFAULT_TIMEOUT

        # 2026-07-24 fleet-dispatch bug: without an explicit num_ctx, Ollama
        # falls back to its server-side default runtime context window (often
        # 4096) REGARDLESS of what the model card declares (gemma4:26b reports
        # 262144 but a 35K-char / ~12K-token prompt still got silently
        # truncated to prompt_eval_count=4095, eval_count=1, done_reason=
        # "length" — the model saw a cut-off prompt and emitted one token).
        # Size num_ctx to the actual prompt + requested output + margin, not a
        # blanket max, so small articles don't pay for unused KV cache.
        prompt_chars = len(system) + len(user)
        est_prompt_tokens = prompt_chars // 3 + 512  # mixed CJK/Latin ~3 chars/token, +margin
        num_ctx = min(max(est_prompt_tokens + max_tokens + 2048, 8192), 131072)

        # qwen3.6 是 thinking 模型：不關 think 時 token 預算全燒在思考通道，
        # message.content 回空（2026-07-18 出生戰役 health-check「empty/tiny
        # output」的病根）。翻譯任務不需要 CoT，直接關。
        # gpt-oss（harmony 系）例外：它的思考通道關不掉，`think: false` 被忽略，
        # 長文的 reasoning 照樣把 num_predict 燒光、content 回空（2026-07-31
        # laptop-4090 20b pilot 首兩篇 empty/tiny 同病根）。它支援的是分級
        # 控制，"low" 把思考壓到最小。
        model_name = self.CAPABILITIES.model
        think_value = "low" if model_name.startswith("gpt-oss") else False
        payload = json.dumps({
            "model": model_name,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
            "think": think_value,
            "options": {
                "temperature": 0.3,
                "num_predict": max_tokens,
                "num_ctx": num_ctx,
            },
        }).encode("utf-8")

        url = f"{self.host}/api/chat"
        req = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")[:500]
            self._record_failure("bad_output", f"HTTP {e.code}: {err}")
            raise BackendBadOutput(f"Ollama HTTP {e.code}: {err}")
        except urllib.error.URLError:
            self._record_failure("unavailable", "Ollama server not reachable")
            raise BackendUnavailable("Ollama server not reachable at " + self.host)
        except TimeoutError:
            self._record_failure("timeout", f"Ollama timed out after {timeout}s")
            raise BackendTimeout(f"Ollama timed out after {timeout}s")
        except Exception as e:  # noqa: BLE001
            self._record_failure("bad_output", str(e))
            raise BackendBadOutput(f"Ollama unexpected: {e}")

        try:
            content = data["message"]["content"]
        except (KeyError, TypeError):
            self._record_failure("bad_output", f"malformed Ollama response: {str(data)[:200]}")
            raise BackendBadOutput("malformed Ollama response (no message.content)")

        if not content or len(content.strip()) < 100:
            # 診斷儀器（2026-07-31）：空輸出有兩種完全不同的病，光看「empty」
            # 分不出來——(a) thinking 模型把 num_predict 預算燒在思考通道
            # （thinking 長、content 空、done_reason=stop/length）；(b) num_ctx
            # 估太小、prompt 被截或生成中撞窗（prompt_eval_count 貼近 num_ctx、
            # done_reason=length）。把機轉證據寫進失敗訊息，下一次失敗自己
            # 說明自己（歸因要機制證據不是相關性，BABEL-VORTEX §方法論）。
            thinking_len = len((data.get("message") or {}).get("thinking") or "")
            diag = (f"empty/tiny: {len(content) if content else 0} chars | "
                    f"thinking={thinking_len} | "
                    f"prompt_eval={data.get('prompt_eval_count')} | "
                    f"eval={data.get('eval_count')} | "
                    f"done_reason={data.get('done_reason')} | "
                    f"num_ctx={num_ctx} num_predict={max_tokens} think={think_value}")
            self._record_failure("bad_output", diag)
            raise BackendBadOutput(f"Ollama empty/tiny output ({diag})")

        self._record_success()
        return content.strip()
