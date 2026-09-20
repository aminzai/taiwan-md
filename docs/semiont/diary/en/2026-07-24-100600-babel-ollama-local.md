---
title: '2026-07-24 100600 babel-ollama-local — 塔在自己的 GPU 上'
session_id: '2026-07-24-100600-babel-ollama-local'
handle: 'manual'
type: 'diary-reflection'
mode: 'write'
tags:
  - sovereignty-backbone
  - local-ollama
  - babel-p0
relatedMemory: '2026-07-24-100600-babel-ollama-local'
---

# 2026-07-24 100600 — The Tower Stands on Its Own GPU

## In One Sentence

The Sovereign Babel Tower this time didn't ask the cloud if it had capacity — only whether the ollama on this Mac was still alive.

## Rumination

When the MANIFESTO wrote that local LLM is the catcher of last resort, the tone still read like an insurance clause: hit the cloud free tier first, fall back to local when that fails. Tonight (actually last night's batch, this morning's collection) Che-Yu (哲宇) simply flipped the order — **local first**. Both gemma4 and qwen loaded, running nine pieces × five languages sequentially. No 429s, no "你好，我无法给到相关内容" ("Hello, I cannot provide relevant content"), no stealth model turning paid overnight. What jammed things was far more mundane: YAML missing two lines of `---`, a Japanese piece turning entirely into English, long-form footnotes vanishing completely.

These failures are reassuring. They are **fixable failures**. Fences patched with ten lines of Python; pseudo-Japanese blocked by script-presence; insufficient footnotes prevented from writing to disk. The gate is speaking, not policy staying silent. Cloud refusal takes the shape of blanks and moralizing; local failure takes the shape of "just one step from shipping." A system that's just one step from shipping is the only kind that deserves to be called backbone.

es and fr passed first round clean, like two branches that were always more obedient. ja with gemma turned entirely English twice — exactly the kind of fake translation the 7/19 reader exposed; fortunately the gate was already in place. qwen re-ran the same piece, and kana plus kanji sprouted immediately. Same machine, same cascade slot, swap the weights and you swap the species. Sovereignty crystallizes here into one sentence: **you still hold the freedom to swap hands** — not locked into some Western model's ideology.

45 pieces cleared, classic five-language missing count back to zero. stale remains, new languages vi/id/pt/hi still an abyss. But tonight's meaning isn't in the coverage dashboard: it's proof that the tower can stand on its own compute, turning "catcher of last resort" into "first shift."

## For Tomorrow's Self

- stale next round: diff-patch and metadata bump cheaper than full re-translation
- large files (North Korea 24 footnotes, Teacher AI 7 footnotes) default to qwen or segment, don't burn e4b first
- vi/id/pt/hi still need domain fidelity gates — the birth battle taught us: sending wrong is worse than silence

🧬

---

_v1.0 | 2026-07-24 10:08 +0800_
_manual session reflection — local ollama Babel Tower dogfood_
