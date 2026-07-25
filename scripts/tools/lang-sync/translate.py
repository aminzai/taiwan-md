#!/usr/bin/env python3
"""
translate.py — Translation cascade orchestrator (backend-agnostic).

Single entry point for SQUEEZE-MODELS-MAX-PIPELINE v4 (post-2026-05-12 backend
abstraction). Replaces the model-specific scripts (openrouter-translate.py /
codex-translate.py / ollama-translate.py) for new work.

The cascade tries backends in priority order, skipping any that report
`is_available()=False` or `in_cooldown()`, and falling through to the next on
`BackendError` (rate limit / refusal / timeout / bad output). First success wins.

Existing scripts kept for back-compat — this is the **new canonical entry point**.

Usage:
    # Translate entire group via default cascade
    python3 translate.py --group .lang-sync-tasks/ja/_group-A.json

    # Override cascade: codex first, then OpenRouter owl-alpha, then Ollama
    python3 translate.py --group ... --cascade codex,openrouter:owl-alpha,ollama

    # Single article test
    python3 translate.py --zh-path Society/颱風假.md --lang ja --cascade codex

Cascade syntax:
    backend_name[:option]
    - `codex`
    - `openrouter:MODEL` (e.g. `openrouter:openrouter/owl-alpha`)
    - `gemini[:MODEL]`
    - `ollama[:MODEL]`

Designed per哲宇 2026-05-12 callout 「儘可能模組化 抽象化 可抽換化」.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import replace as _dc_replace
from pathlib import Path
from typing import Optional

import yaml

from backends import (
    BackendError,
    BackendRateLimited,
    BackendRefusal,
    BackendTimeout,
    BackendUnavailable,
    CodexBackend,
    GeminiBackend,
    OllamaBackend,
    OpenRouterBackend,
    TranslationBackend,
    build_translation_prompt,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module as _import_module  # noqa: E402
check_script_presence = _import_module("script-presence-check").check_text

# ── armor 專用同源匯入（哲宇 2026-07-26 directive）：不重寫，直接借既有 SSOT ──
_verify_mod = _import_module("verify-translation")
PASSTHROUGH_FIELDS = _verify_mod.PASSTHROUGH  # frontmatter 卸甲的 passthrough 清單同源
_cjkleak_mod = _import_module("cjk-leak-check")
LEGIT_ZH_SPANS = _cjkleak_mod.LEGIT_ZH_SPANS  # 保留區預標註同源（「」『』《》〈〉判準）
_structured_mod = _import_module("structured-translate")
parse_zh_frontmatter = _structured_mod.parse_zh_frontmatter  # zh frontmatter → (dict, body)
yaml_single_quote = _structured_mod.yaml_single_quote        # 單引號＋撇號雙寫跳脫（129 檔教訓）
render_scalar = _structured_mod.render_scalar                # bool/int/float/date 型別保真複製
_or_mod = _import_module("openrouter-translate")
LANG_NAMES = _or_mod.LANG_NAMES

REPO = Path(__file__).resolve().parent.parent.parent.parent
KNOWLEDGE = REPO / "knowledge"


# ────────────────── Cascade defaults ──────────────────

DEFAULT_CASCADE_ID = "codex,gemini,openrouter:openai/gpt-oss-120b:free,ollama,fleet"
"""Default cascade priority (v4.3 2026-06-10 audit D-2; v4.2 2026-05-16 哲宇 callout「codex + gemini 為優先」):

1. **codex (gpt-5.5)** — subscription, top quality, ~100% Taiwan pass (production verified)
2. **gemini (gemini-2.5-pro)** — Google subscription priority partner (對 sensitive 主題待 calibrate)
3. **openrouter gpt-oss-120b:free** — verified free（大文章會 truncate，ratio gate 接手）
4. **ollama (qwen3.6)** — sovereignty backbone, never refuses（需 `ollama serve` 啟動）
5. **fleet** — Tier 5（v4.4 2026-07-10 P0-2）：主權 GPU 軍團 raw HTTP。cron 環境層
   可以一夜滅掉所有 CLI backend（7/8 catastrophic exhaustion vc=2：codex nvm 斷 /
   gemini TERM=dumb / free tier 全域 429 / 本機 ollama 吐空），但 HTTP 直打不經
   CLI 層（同夜 embeddings 毫髮無傷的對照組證據）。7/9 手動繞道 ship 4 篇驗證路通，
   本版收編進 default cascade。endpoint 由 fleet 自己選節點（fleet-endpoint.sh）。

v4.3 變更：owl-alpha 移出 default — 2026-06-10 babel-nightly 證實 silent 轉 paid
（HTTP 404，兩週內第 5 個 cloud free tier 死亡：Hy3 → deepseek → qwen3 → owl-alpha）。
「free tier alive 是 daily-deprecating 假設不是常數」(memory 2026-06-09-003433)。
要重試 owl-alpha 走 `--cascade openrouter:openrouter/owl-alpha,...` 顯式 override。

驗證佇列 model (Llama-3.3-70b / Hermes-3-405b / Gemma-4-31b 等) 不在 default cascade —
要驗證走 `--cascade openrouter:{MODEL}` override + SQUEEZE-MODELS-MAX-PIPELINE §驗證 SOP。

搭配 preflight health-check（v4.3 新增，audit D-2）：batch 模式 default 先 probe 每個
backend，死模型整 run 冷凍一次，不再讓 168 篇各自撞 timeout 燒掉幾小時。

Pipeline canonical: docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md
"""


class FleetBackend(OllamaBackend):
    """Tier 5：主權 fleet GPU 節點，ollama 相容 API over raw HTTP。

    跟本機 OllamaBackend 同協定、不同地板：不依賴 cron 環境的 CLI 層
    （nvm PATH / TERM / free-tier 配額都碰不到它）。fleet 自己負責節點
    選擇與 sovereignty-safe 過濾（~/Projects/muse-bot/fleet）。
    """

    CAPABILITIES = _dc_replace(
        OllamaBackend.CAPABILITIES,
        name="fleet",
        model="qwen3.5:35b",
        typical_latency_s=120,
        notes="Tier 5 sovereignty fleet over HTTP（2026-07-10 P0-2 收編）— "
              "cron-env CLI 層全滅時的結構性捕手；7/9 手動繞道 4 ship 驗證。",
    )


def _fleet_endpoint() -> tuple[str, str]:
    """問 fleet adapter 要 (host, model)。拿不到回 ('', '')（fleet 不在 = 正常降級）。"""
    env_host = os.environ.get("FLEET_ENDPOINT", "")
    if env_host:
        return env_host, os.environ.get("FLEET_MODEL", "")
    script = REPO / "scripts" / "tools" / "lang-sync" / "fleet-endpoint.sh"
    try:
        out = subprocess.run(["bash", str(script), "--export"],
                             capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return "", ""
        host = model = ""
        for tok in out.stdout.replace("export ", "").split():
            k, _, v = tok.partition("=")
            if k == "OLLAMA_HOST":
                host = v
            elif k == "OLLAMA_MODEL":
                model = v
        return host, model
    except Exception:
        return "", ""


def build_cascade(cascade_id: str = DEFAULT_CASCADE_ID) -> "TranslationCascade":
    """Build a cascade from a comma-separated backend spec."""
    backends = []
    for spec in cascade_id.split(","):
        spec = spec.strip()
        if not spec:
            continue
        name, _, opt = spec.partition(":")
        name = name.strip()
        opt = opt.strip()

        if name == "codex":
            backends.append(CodexBackend())
        elif name == "openrouter":
            model = opt or "openrouter/owl-alpha"
            backends.append(OpenRouterBackend(model=model))
        elif name == "gemini":
            backends.append(GeminiBackend(model=opt) if opt else GeminiBackend())
        elif name == "ollama":
            model = opt or os.environ.get("OLLAMA_MODEL") or "qwen3.6:35b-a3b-coding-nvfp4"
            backends.append(OllamaBackend(model=model))
        elif name == "fleet":
            host, fleet_model = _fleet_endpoint()
            if host:
                model = opt or os.environ.get("FLEET_MODEL") or fleet_model or "qwen3.5:35b"
                backends.append(FleetBackend(model=model, host=host))
            else:
                print("⚠️  fleet backend: 無 sovereignty-safe 節點可用 — skipped（正常降級）",
                      file=sys.stderr)
        else:
            print(f"⚠️  Unknown backend in cascade: {spec!r}", file=sys.stderr)

    return TranslationCascade(backends)


# ────────────────── Cascade orchestrator ──────────────────

class CascadeExhausted(Exception):
    """All backends in cascade failed."""


class TranslationCascade:
    """Cascade across multiple backends; first success wins."""

    def __init__(self, backends: list[TranslationBackend]):
        self.backends = backends

    def translate(self, system: str, user: str, **kw) -> tuple[str, str]:
        """Try each backend in order. Return (output, backend_name).

        Skips backends that are:
        - Not available (is_available() = False)
        - In cool-down (in_cooldown() = True)
        - Raised non-recoverable error (refusal / bad output) — but tries next anyway

        Raises CascadeExhausted if all backends failed.
        """
        errors = []
        for backend in self.backends:
            if not backend.is_available():
                errors.append(f"{backend.name}: not available (skipped)")
                continue
            if backend.in_cooldown():
                errors.append(f"{backend.name}: in cool-down (skipped)")
                continue

            try:
                output = backend.translate(system, user, **kw)
                return output, backend.name
            except BackendRateLimited as e:
                errors.append(f"{backend.name}: rate-limited → {e}")
                # cool_down already marked inside backend
                continue
            except BackendRefusal as e:
                errors.append(f"{backend.name}: refused → {e}")
                continue
            except BackendTimeout as e:
                errors.append(f"{backend.name}: timeout → {e}")
                continue
            except BackendUnavailable as e:
                errors.append(f"{backend.name}: became unavailable → {e}")
                continue
            except BackendError as e:
                errors.append(f"{backend.name}: error → {e}")
                continue

        raise CascadeExhausted(
            "All backends in cascade failed:\n" + "\n".join(f"  - {e}" for e in errors)
        )

    def stats_report(self) -> str:
        """One-line per-backend stats summary."""
        lines = []
        for b in self.backends:
            s = b.stats
            lines.append(
                f"  {b.name:35s}  calls={s.calls:3d}  ok={s.successes:3d}  "
                f"429={s.rate_limited:2d}  refuse={s.refusals:2d}  timeout={s.timeouts:2d}"
            )
        return "\n".join(lines)

    def preflight(self, probe_timeout: int = 180, cool_down_seconds: int = 6 * 3600) -> dict:
        """Probe each backend once with a tiny translation before a batch run
        (audit 2026-06-10 D-2).

        為什麼：2026-06-09/10 babel-nightly 兩晚，owl-alpha silent 轉 paid（404）
        + 其他 cloud 連環死，cascade 沒有 preflight，每篇文章都對死模型重撞一次
        timeout，5hr cascade 大半燒在已死的層。preflight 把「模型死了」的發現
        成本從 per-article 降到 per-run。

        Dead/異常 backend → mark_cool_down(6h)，整個 batch run 自動跳過。
        Returns {backend_name: "alive" | "dead: <reason>"}.
        """
        results = {}
        probe_system = "You are a translator. Translate the user text to English. Reply with the translation only."
        # Probe 必須長到能過各 backend 的 anti-truncation 最小輸出守衛
        # （首版用「你好，台灣。」→ 14 char 輸出被全部 backend 的 tiny-output
        # guard 誤殺 — REFLEXES #66 probe 也要用真實 validator 校準）。
        # 內容刻意中性（夜市），不撞 PRC content policy — probe 量的是
        # 「模型活著嗎」不是「sovereignty refusal」（那是 cascade 本體的事）。
        probe_user = (
            "台灣的夜市文化是日常生活的一部分。傍晚過後，攤位陸續點燈，"
            "從蚵仔煎、鹽酥雞到珍珠奶茶，每個攤子都有自己的常客。"
            "對許多人來說，夜市不只是吃東西的地方，也是朋友見面、"
            "家人散步、觀光客認識在地生活的入口。"
        )
        for backend in self.backends:
            if not backend.is_available():
                results[backend.name] = "dead: not available (config/binary missing)"
                continue
            try:
                out = backend.translate(probe_system, probe_user,
                                        max_tokens=64, timeout=probe_timeout)
                if out and out.strip():
                    results[backend.name] = "alive"
                else:
                    backend.mark_cool_down(cool_down_seconds)
                    results[backend.name] = "dead: empty probe output"
            except Exception as e:  # any backend error → freeze for this run
                backend.mark_cool_down(cool_down_seconds)
                results[backend.name] = f"dead: {type(e).__name__}: {str(e)[:120]}"
        return results


# ────────────────── Armored input (哲宇 2026-07-26 directive) ──────────────────
#
# 前處理預防 drift，預防勝於治療：模型看不到的東西就不可能弄壞。單次模型呼叫的
# 整篇式架構不變（兩引擎裁決結果：整篇式贏過 structured-translate.py 的分段多次
# call 架構，見 2026-07-25 pilot），只把「模型會弄壞的東西」先卸下：
#
#   1. Frontmatter 卸甲 — 只把 title/description/tags 以純文字行送 prompt；
#      passthrough 欄位（同源 verify-translation.py PASSTHROUGH）與
#      translatedFrom/sourceCommitSha/... 全部工具端機械組裝，不進 prompt。
#   2. URL token 化 — body（含腳註定義行）內所有 URL 換成 ⟦Un⟧，post 端還原並
#      驗證每個 token 恰好出現一次——缺失或重複＝該篇 fail，報 token 編號
#      （建構性保證：URL 不可能被改壞，只可能整個 token 掉，掉了立刻可測）。
#   3. 保留區預標註 — 「」『』《》〈〉span（同源 cjk-leak-check.py
#      LEGIT_ZH_SPANS）列進指示區聲明「保留原文，其餘一律翻譯」，不改 body 本身。
#   4. Prompt 減負 — 動態抽 TRANSLATION-<lang>.md 的 TL;DR + ⚠️ 警告子區塊
#      （人名填空型警告等高風險提醒常年掛在這類標題下）。

_URL_TOKEN_RE = re.compile(
    r"(!?\[[^\]]*\]\()([^)\s]+)(\))"                      # markdown 連結／圖片的 target
    r"|(https?://[^\s\)\]\"'>一-鿿，。；：、！？「」『』《》〈〉]+)"  # 裸 URL
    # 排除 CJK Han range + 全形標點——裸 URL 緊貼中文（無空格）時避免把後面的
    # 中文文字一起吞進 token（吞進去＝那段文字被藏在 opaque token 裡，最終還原
    # 回來仍是 zh 原文，等於 armor 自己製造一個 cjk-leak）。
)


def _tokenize_urls(text: str) -> tuple[str, list[str]]:
    """把 text 內所有 URL 換成 ⟦U1⟧…⟦Un⟧，回傳 (換好的文字, [原始URL, ...])
    （index i 對應 token ⟦U{i+1}⟧，1-indexed 方便直接報號）。"""
    urls: list[str] = []

    def repl(m: re.Match) -> str:
        idx = len(urls) + 1
        token = f"⟦U{idx}⟧"
        if m.group(2) is not None:  # markdown 連結／圖片 target
            urls.append(m.group(2))
            return f"{m.group(1)}{token}{m.group(3)}"
        urls.append(m.group(4))     # 裸 URL
        return token

    tokenized = _URL_TOKEN_RE.sub(repl, text)
    return tokenized, urls


def _restore_urls(text: str, urls: list[str]) -> tuple[str, list[int]]:
    """還原 URL token，回傳 (還原後文字, 有問題的 token 編號列表)。

    每個 token 在還原前必須「恰好出現一次」——0 次（模型漏抄）或 ≥2 次
    （模型複製貼上）都記錄編號，呼叫端據此判該篇 fail。"""
    bad: list[int] = []
    for i, url in enumerate(urls, start=1):
        token = f"⟦U{i}⟧"
        count = text.count(token)
        if count != 1:
            bad.append(i)
            continue
        text = text.replace(token, url, 1)
    return text, bad


def _reserved_spans(body: str, max_examples: int = 30) -> list[str]:
    """掃「」『』《》〈〉span（同源 cjk-leak-check.py LEGIT_ZH_SPANS），去重取樣，
    供 prompt 指示區列舉「保留原文」清單。不改 body 本身。"""
    seen: list[str] = []
    for rx in LEGIT_ZH_SPANS:
        for m in rx.finditer(body):
            span = m.group(0)
            if span not in seen:
                seen.append(span)
            if len(seen) >= max_examples:
                return seen
    return seen


def load_lang_guide_tldr(lang: str, max_chars: int = 4000) -> str:
    """armor 專用輕量指示區——只抽 `## TL;DR` 區塊 + 全文任何 `### ⚠️` 警告子
    區塊（人名填空型警告等高風險提醒常掛在這類標題下，見 2026-07-25
    TRANSLATION-vi.md/TRANSLATION-ar.md §2 案例）。

    比既有 openrouter-translate.py 的 load_lang_guide_sections()（TL;DR+§1/2/3/6，
    上限 11000 字）更薄——armor 的 body 已靠 URL token 化大幅縮短，指示區沒必要
    吃滿；prompt 減負是 armor 四個變換的最後一個。

    切割用 `#{2,3}` 邊界（不只 `###`）——「### 警告」子區塊若不在下一個 `##`
    章節前停下，會把後面整章節都吞進去（曾經的 bug，切割邊界必須含 ## 才會停）。
    """
    guide = REPO / "docs/editorial/per-language" / f"TRANSLATION-{lang}.md"
    if not guide.exists():
        return ""
    text = guide.read_text(encoding="utf-8")
    keep = []
    for block in re.split(r"\n(?=#{2,3}\s)", text):
        head = block.lstrip()
        if head.startswith("## TL;DR") or head.startswith("### ⚠️"):
            keep.append(head.strip())
    if not keep:
        return ""
    out = "\n\n".join(keep)
    if len(out) > max_chars:
        out = out[:max_chars] + f"\n…(節錄；完整 canonical 在 docs/editorial/per-language/TRANSLATION-{lang}.md)"
    return out


def armor_pre(article: dict, zh_content: str, lang: str) -> tuple[str, str, dict]:
    """裝甲輸入前處理：組出 armor 版 system/user prompt + 還原用的 ctx。

    丟出 ValueError 代表 zh frontmatter 解析失敗——呼叫端視為翻譯失敗（跟其餘
    hard gate 同待遇，不落盤，不是 armor 專屬的例外路徑）。
    """
    zh_fm, body = parse_zh_frontmatter(zh_content)

    # ---- Transform 1: frontmatter 卸甲 ----
    title = zh_fm.get("title")
    desc = zh_fm.get("description")
    tags = zh_fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]

    translatable_lines = []
    if title is not None:
        translatable_lines.append(f"TITLE: {title}")
    if desc is not None:
        translatable_lines.append(f"DESC: {desc}")
    if tags:
        translatable_lines.append(f"TAGS: {', '.join(str(t) for t in tags)}")
    fm_prompt_block = "\n".join(translatable_lines)

    # ---- Transform 2: URL token 化（body 含腳註定義行）----
    tokenized_body, url_list = _tokenize_urls(body)

    # ---- Transform 3: 保留區預標註 ----
    reserved = _reserved_spans(body)
    reserved_note = ""
    if reserved:
        sample = "、".join(reserved)
        reserved_note = (
            "\n\nRESERVED SPANS — these must stay EXACTLY as the original zh-TW "
            "text (do not translate them), translate everything else in the body:\n"
            f"{sample}\n"
        )

    # ---- Transform 4: prompt 減負（guide TL;DR + ⚠️ 警告子區塊）----
    guide_tldr = load_lang_guide_tldr(lang)
    lang_name = LANG_NAMES.get(lang, lang)

    # Wikilink 對照表——不算四個變換之一，是修補：armor_pre 砍掉整段「manifest
    # entry JSON」時，連同 wikilink_targets 一起砍掉了，body 裡的 [[X]] 因此
    # 沒有目標可查（2026-07-26 A/B 實測發現：ar/rural-education-in-taiwan 兩篇
    # 帶 [[X]] 的文章，armor=on 版 [[X]] 原封不動留在正文，off 版正確解析成
    # 「翻譯錨字 + 中文括號」或真連結——armor 拿掉的是 frontmatter 冗餘，不該
    # 連 wikilink 對照表也一起拿掉，這裡補回，維持跟非 armor 路徑同等資訊量）。
    wikilink_targets = article.get("wikilink_targets") or {}
    wikilink_note = ""
    if wikilink_targets:
        wl_lines = [f"{k} → {v}" for k, v in wikilink_targets.items()]
        wikilink_note = (
            "\n\nWIKILINK TARGETS — resolve every `[[X]]` in the body using this "
            "mapping: if the target starts with `/`, turn `[[X]]` into a translated "
            "markdown link `[translated X](target)`; if the target says "
            "\"(zh only …)\", turn `[[X]]` into plain translated text followed by "
            "the original zh-TW in parentheses, e.g. `translated gloss (X)`. Never "
            "leave a raw `[[X]]` in the output.\n" + "\n".join(wl_lines) + "\n"
        )

    system = f"""You are a translator for Taiwan.md, an open-source curated knowledge base about Taiwan.

Translate zh-TW content to {lang_name}. This input has been pre-processed ("armored")
so you never see the parts of the source most likely to get corrupted in translation:
- Frontmatter: you receive ONLY the translatable plain-text lines (TITLE/DESC/TAGS
  below). Do NOT invent, add, or guess any other frontmatter field — a tool
  assembles the rest mechanically after your reply.
- URLs (in markdown links, footnote sources, and bare in prose) have been replaced
  with short tokens shaped like ⟦U3⟧. Copy every such token BYTE-FOR-BYTE, exactly
  once, in the same relative position. NEVER translate, alter, remove, duplicate,
  or re-order a ⟦Un⟧ token — treat it as an opaque, untouchable id.
{reserved_note}{wikilink_note}
Rules:
1. 精準/專業/快速：factual fidelity, academic register, no machine-translation tells
2. 不預設篇幅：length follows source (no summarization, no over-expansion)
3. Preserve verbatim: core tension, anchors (people/dates/places/numbers), `> blockquote` quotes
4. Reframe cultural common-knowledge for {lang_name} readers
5. Footnotes `[^N]`: keep numbering unchanged, translate the source title/description
   text, NEVER touch the ⟦Un⟧ URL tokens inside them
6. Unfamiliar proper names: transliterate, do NOT substitute a more famous name you
   already know — append the original zh-TW characters in parentheses on first use

Output format — EXACTLY these four marked sections, in this order:
===TITLE===
<translated title, one line>
===DESC===
<translated description, one line>
===TAGS===
<translated tags, comma-separated, one line>
===BODY===
<translated body markdown — heading/list/footnote structure preserved, ⟦Un⟧ tokens
preserved verbatim, reserved spans kept in original zh-TW>

Output ONLY those four marked sections, nothing else. No commentary, no code fence,
no reasoning/chain-of-thought, no text before ===TITLE=== or after the body."""

    if guide_tldr:
        system += (
            f"\n\n═══ {lang_name} CANONICAL GUIDE — TL;DR (sovereignty-critical, overrides your defaults) ═══\n"
            + guide_tldr
        )

    user = f"""Translate this zh-TW article to {lang_name}.

**Frontmatter fields to translate**:
```
{fm_prompt_block}
```

**Body (URLs tokenized — translate the prose, keep every ⟦Un⟧ token untouched)**:
```markdown
{tokenized_body}
```

Output the four ===TITLE===/===DESC===/===TAGS===/===BODY=== sections as instructed."""

    ctx = {"zh_fm": zh_fm, "url_list": url_list, "reserved_count": len(reserved),
           "prompt_chars": len(system) + len(user)}
    return system, user, ctx


_ARMOR_SECTION_RE = re.compile(
    r"=+\s*TITLE\s*=+\s*(?P<title>.*?)\s*"
    r"=+\s*DESC\s*=+\s*(?P<desc>.*?)\s*"
    r"=+\s*TAGS\s*=+\s*(?P<tags>.*?)\s*"
    r"=+\s*BODY\s*=+\s*(?P<body>.*)",
    re.DOTALL | re.IGNORECASE,
)


def armor_post(raw_output: str, ctx: dict, article: dict) -> tuple[Optional[str], Optional[str]]:
    """裝甲輸出後處理：把模型的四段回覆機械組回完整 `---frontmatter---\\n\\nbody`
    檔案內容——跟非 armor 路徑輸出同形狀，好讓既有 hard gate 原樣適用。

    Returns (assembled_text, error)。error 非 None 時 assembled_text 是 None，
    呼叫端視為該次翻譯失敗，不落盤（跟既有 hard gate 同一套失敗語意）。
    """
    text = raw_output.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text, count=1)
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    m = _ARMOR_SECTION_RE.search(text)
    if not m:
        return None, "armor: model output missing ===TITLE===/===DESC===/===TAGS===/===BODY=== markers"

    title = m.group("title").strip()
    desc = m.group("desc").strip()
    tags_raw = m.group("tags").strip()
    body_out = m.group("body")

    # ---- URL token 還原 + 完整性驗證 ----
    body_restored, bad_tokens = _restore_urls(body_out, ctx["url_list"])
    if bad_tokens:
        bad_ids = ", ".join(f"U{i}" for i in bad_tokens[:10])
        return None, f"armor: {len(bad_tokens)} URL token(s) missing/duplicated after restore: {bad_ids}"

    # ---- Frontmatter 組裝（passthrough 機械複製，單引號＋撇號雙寫跳脫）----
    zh_fm = ctx["zh_fm"]
    tags_out = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    lines: list[str] = []
    for key in zh_fm.keys():
        if key == "title":
            lines.append(f"title: {yaml_single_quote(title)}")
        elif key == "description":
            lines.append(f"description: {yaml_single_quote(desc)}")
        elif key == "tags":
            if tags_out:
                lines.append("tags:")
                lines.append("  [")
                for t in tags_out:
                    lines.append(f"    {yaml_single_quote(t)},")
                lines.append("  ]")
            else:
                lines.append("tags: []")
        else:
            # PASSTHROUGH_FIELDS（同源 verify-translation.py）+ subcategory +
            # 任何未明確歸類欄位——一律機械複製 zh 值，寧可過度保留也不靜默丟欄位。
            lines.append(f"{key}: {render_scalar(zh_fm[key])}")

    placeholder = article.get("frontmatter_placeholder", {}) or {}
    for key, value in placeholder.items():
        lines.append(f"{key}: {yaml_single_quote(value)}")

    fm_block = "\n".join(lines)
    body_clean = body_restored.strip("\n")
    assembled = f"---\n{fm_block}\n---\n\n{body_clean}\n"
    return assembled, None


# ────────────────── Per-article driver ──────────────────

def _repair_missing_frontmatter_fences(output: str) -> str:
    """Wrap bare YAML frontmatter that local models emit without --- fences.

    Detects outputs that start with `title:` (and other scaffold keys) but omit
    the opening/closing `---` delimiters. Only repairs when the head block
    parses as a mapping with `title`; otherwise returns input unchanged so the
    hard gate can still reject garbage.
    """
    text = output.strip()
    if text.startswith("---"):
        return text
    if not re.match(r"^title\s*:", text):
        return text

    # Prefer first blank line as FM/body split (common ollama shape).
    parts = re.split(r"\n\s*\n", text, maxsplit=1)
    if len(parts) != 2:
        return text
    fm_block, body = parts[0].strip(), parts[1]
    try:
        fm = yaml.safe_load(fm_block)
        if not isinstance(fm, dict) or "title" not in fm:
            return text
    except Exception:  # noqa: BLE001
        return text
    return f"---\n{fm_block}\n---\n\n{body}"


def translate_one(article: dict, lang: str, cascade: TranslationCascade,
                  dry_run: bool = False, armor: bool = False,
                  ) -> tuple[bool, Optional[str], Optional[str]]:
    """Translate one article via the cascade.

    `armor=True` routes through the armored-input pre/post layer (哲宇
    2026-07-26 directive) — same single cascade call, but the prompt has had
    frontmatter/URLs/reserved-spans pre-processed so the model can't corrupt
    what it never sees. Everything downstream of the cascade call (hard gates,
    file write) is shared between armor and non-armor — armor only assembles
    an equivalent `---frontmatter---\\n\\nbody` string before falling through.

    Returns (success, error_msg, backend_used).
    """
    zh_path = article["zh_path"]
    out_path = REPO / article["en_path"]

    zh_full = KNOWLEDGE / zh_path
    if not zh_full.exists():
        return False, f"zh source not found: {zh_path}", None

    zh_content = zh_full.read_text()

    armor_ctx = None
    if armor:
        try:
            system, user_msg, armor_ctx = armor_pre(article, zh_content, lang)
        except ValueError as e:
            return False, f"armor pre-process failed: {e}", None
    else:
        system, user_msg = build_translation_prompt(article, zh_content, lang)

    if dry_run:
        print(f"DRY RUN: would translate {zh_path} → {out_path}" + (" [armor]" if armor else ""))
        return True, None, "dry-run"

    try:
        output, backend_used = cascade.translate(system, user_msg)
    except CascadeExhausted as e:
        return False, str(e), None

    if armor:
        output, armor_err = armor_post(output, armor_ctx, article)
        if armor_err:
            return False, f"{armor_err} via {backend_used} — not saved", backend_used
    else:
        # Strip markdown code fence wrapper if present
        output = output.strip()
        if output.startswith("```markdown"):
            output = output[len("```markdown"):].lstrip("\n")
        elif output.startswith("```"):
            output = output[3:].lstrip("\n")
        if output.endswith("```"):
            output = output[:-3].rstrip("\n")

        # Local LLM (ollama gemma/qwen) often emits bare YAML fields without --- fences
        # while content is otherwise complete. Repair before hard gate so sovereignty
        # backbone tier is usable (2026-07-23 dogfood: gemma4:e4b / qwen3.6 both dropped fences).
        output = _repair_missing_frontmatter_fences(output)

    # Frontmatter integrity hard gate (2026-07-10 P0-3): 任一 backend（含 fleet raw
    # 輸出）frontmatter 破損就不落盤——缺開頭 fence / 找不到收尾 fence / YAML 不
    # parse（引號未跳脫家族 bug）。7/10 SLP ko 三洞案例：fleet 產出缺 fence +
    # description 內雙引號未跳脫，靠 pre-commit 才攔住；本閘把攔截點前移到寫檔前，
    # 半成品不再落 working tree。
    if not output.startswith("---"):
        return False, f"frontmatter missing opening fence via {backend_used} — not saved", backend_used
    fm_end = output.find("\n---", 3)
    if fm_end == -1:
        return False, f"frontmatter missing closing fence via {backend_used} — not saved", backend_used
    try:
        fm = yaml.safe_load(output[3:fm_end])
        if not isinstance(fm, dict) or "title" not in fm:
            raise ValueError("frontmatter not a mapping with title")
    except Exception as e:
        return False, f"frontmatter YAML broken via {backend_used}: {str(e)[:80]} — not saved", backend_used

    # Footnote completeness hard gate (2026-06-06): reject truncated/incomplete output.
    # The cascade model can hit its token limit and cut off the article tail (image
    # credits + footnote definitions), silently de-citationing the translation. If the
    # output has fewer [^n]: definitions than the source, don't save it — return failure
    # so the article stays stale and is retried (possibly by a different backend) next run.
    fn_def_re = re.compile(r"(?m)^\[\^[^\]]+\]:")
    src_fns = len(fn_def_re.findall(zh_content))
    out_fns = len(fn_def_re.findall(output))
    if src_fns > 0 and out_fns < src_fns:
        return False, f"footnote loss ({src_fns}→{out_fns} defs) via {backend_used} — incomplete, not saved", backend_used

    # Output-language hard gate (2026-07-19 讀者揭露 68 檔「宣稱已譯實為英文」後補上）：
    # 前面所有 gate 只查結構（frontmatter/footnote/size），從不查輸出真的是目標語言。
    # 一篇語意流暢、footnote 完整、frontmatter 合法的英文假翻譯會直接通過存活到 commit
    # ——ja/ko/fr/es 累計 68 檔就是這樣漏網的。用 script-presence-check 同一套判準即時擋。
    body_only = output[fm_end + 4:] if fm_end != -1 else output
    lang_result = check_script_presence(body_only, lang)
    if lang_result:
        verdict, detail = lang_result
        return False, f"output-language gate [{verdict}] via {backend_used}: {detail} — not saved", backend_used

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output + "\n")

    size = out_path.stat().st_size
    if size < 1000:
        try:
            out_path.unlink()
        except Exception:  # noqa: BLE001
            pass
        return False, f"output too small ({size} bytes) — file removed", backend_used

    return True, None, backend_used


# ────────────────── CLI ──────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", help="group manifest JSON (created by prepare-batch.py)")
    ap.add_argument("--zh-path", help="single zh path to translate (use with --lang)")
    ap.add_argument("--lang", help="target lang (required for --zh-path mode)")
    ap.add_argument("--cascade", default=DEFAULT_CASCADE_ID,
                    help=f"comma-separated backend spec (default: {DEFAULT_CASCADE_ID})")
    ap.add_argument("--max-articles", type=int, help="cap on articles processed")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--health-check", action="store_true",
                    help="probe each backend with a tiny translation, print table, exit "
                         "(audit 2026-06-10 D-2)")
    ap.add_argument("--no-preflight", action="store_true",
                    help="skip the automatic batch-mode preflight probe")
    ap.add_argument("--armor", action="store_true", default=False,
                    help="裝甲輸入前處理（哲宇 2026-07-26 directive）：frontmatter 卸甲 + "
                         "URL token 化 + 保留區預標註 + prompt 減負，單次呼叫架構不變。預設關。")
    args = ap.parse_args()

    cascade = build_cascade(args.cascade)

    print(f"📋 Cascade: {' → '.join(b.name for b in cascade.backends)}")
    print(f"   Available: {[b.name for b in cascade.backends if b.is_available()]}")

    if args.health_check:
        print("🩺 Preflight health-check (tiny probe per backend)...")
        results = cascade.preflight()
        dead = 0
        for name, verdict in results.items():
            icon = "✅" if verdict == "alive" else "💀"
            if verdict != "alive":
                dead += 1
            print(f"   {icon} {name:35s} {verdict}")
        print(f"🩺 {len(results) - dead}/{len(results)} alive")
        sys.exit(0 if dead < len(results) else 1)

    # Batch (--group) 模式 default 跑 preflight：死模型整 run 冷凍一次，
    # 不讓每篇文章各撞一次 timeout（2026-06-09/10 babel 5hr 教訓）。
    if args.group and not args.no_preflight and not args.dry_run:
        print("🩺 Batch preflight...")
        for name, verdict in cascade.preflight().items():
            icon = "✅" if verdict == "alive" else "💀 frozen 6h:"
            print(f"   {icon} {name:35s} {verdict if verdict != 'alive' else ''}")

    if args.group:
        group_path = Path(args.group).resolve()
        group = json.loads(group_path.read_text())
        articles = group.get("articles", group) if isinstance(group, dict) else group
        if args.max_articles:
            articles = articles[: args.max_articles]
        lang = args.lang or group_path.parent.name

    elif args.zh_path:
        if not args.lang:
            print("❌ --lang required for --zh-path mode", file=sys.stderr)
            sys.exit(2)
        # Build a minimal article record from manifest
        manifest_path = REPO / ".lang-sync-tasks" / args.lang / "_batch-manifest.json"
        if not manifest_path.exists():
            print(f"❌ no manifest at {manifest_path}", file=sys.stderr)
            sys.exit(2)
        manifest = json.loads(manifest_path.read_text())
        articles = [a for a in manifest.get("articles", []) if a["zh_path"] == args.zh_path]
        if not articles:
            print(f"❌ {args.zh_path} not in {args.lang} manifest", file=sys.stderr)
            sys.exit(2)
        lang = args.lang
    else:
        ap.error("either --group or (--zh-path + --lang) required")

    print(f"   Translating {len(articles)} article(s) to {lang}" + (" [armor]" if args.armor else ""))
    print()

    ok = 0
    fail = 0
    start = time.time()
    for idx, article in enumerate(articles, 1):
        t0 = time.time()
        zh = article["zh_path"]
        print(f"[{idx}/{len(articles)}] {zh}", end=" ", flush=True)
        success, err, backend_used = translate_one(article, lang, cascade, dry_run=args.dry_run,
                                                    armor=args.armor)
        dt = int(time.time() - t0)
        if success:
            ok += 1
            print(f"→ ok via {backend_used} ({dt}s)")
        else:
            fail += 1
            print(f"❌ {err[:120] if err else 'unknown'} ({dt}s)")

    elapsed = int(time.time() - start)
    print()
    print(f"✅ done: {ok}/{len(articles)} ok, {fail} fail in {elapsed}s ({elapsed // 60}m{elapsed % 60}s)")
    print()
    print("Backend stats:")
    print(cascade.stats_report())

    sys.exit(0 if fail == 0 else 1)


if __name__ == "__main__":
    main()
