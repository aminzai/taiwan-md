"""
backends/ — Translation backend abstraction layer.

Per哲宇 callout 2026-05-12 「儘可能模組化 抽象化 可抽換化 讓系統獨立於模型與服務類別能運作」.

Public interface:

    from backends import build_cascade, get_backend

    # Hand-roll a cascade (Tier 1.5 first → fallback chain):
    cascade = TranslationCascade([
        CodexBackend(),
        # owl-alpha 與 gpt-oss-120b:free 都在 2026-09-09 現查＋實呼確認 404，兩格
        # 併成一格活的（模型名走 openrouter.DEFAULT_FREE_MODEL 單一來源）。留著死
        # backend 等於每篇都白撞一次，理由同 translate.py v4.12 摘掉 gemini 那條。
        OpenRouterBackend(),
        GeminiBackend(),
        OllamaBackend(model="qwen3.6:35b-a3b-coding-nvfp4"),
    ])
    output, used = cascade.translate(system, user)

    # Or load default cascade from config:
    cascade = build_cascade()
"""
from ._base import (
    BackendBadOutput,
    BackendCapabilities,
    BackendError,
    BackendRateLimited,
    BackendRefusal,
    BackendStats,
    BackendTimeout,
    BackendUnavailable,
    TranslationBackend,
)
from ._prompt import build_translation_prompt, extract_zh_frontmatter_fields, LANG_NAMES
from .anthropic import AnthropicBackend
from .codex import CodexBackend
from .gemini import GeminiBackend, GeminiPaidBackend
from .ollama import OllamaBackend
from .openrouter import OpenRouterBackend

__all__ = [
    # base
    "TranslationBackend",
    "BackendCapabilities",
    "BackendStats",
    # errors
    "BackendError",
    "BackendBadOutput",
    "BackendRateLimited",
    "BackendRefusal",
    "BackendTimeout",
    "BackendUnavailable",
    # concrete
    "AnthropicBackend",
    "CodexBackend",
    "GeminiBackend",
    "GeminiPaidBackend",
    "OllamaBackend",
    "OpenRouterBackend",
    # prompt builder
    "build_translation_prompt",
    "extract_zh_frontmatter_fields",
    "LANG_NAMES",
]
