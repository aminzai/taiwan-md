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

# 2026-07-24 100600 — 塔在自己的 GPU 上

## 一句話

主權的巴別塔這次沒有問雲端有沒有空，只問這台 Mac 上的 ollama 還在不在。

## 反芻

MANIFESTO 寫 local LLM 是最後捕手時，語氣還像保險條款：雲端 free tier 先打，打不動再回本地。今晚（其實是昨夜 batch、今早收）哲宇直接把順序翻過來——**先本機**。gemma4 跟 qwen 都載著，串行跑九篇 × 五語。沒有 429、沒有「你好，我无法给到相关内容」、沒有 stealth model 隔夜變 paid。卡的是更土的東西：YAML 少了兩行 `---`、日文篇整篇變英文、長文腳註掉光。

這些失敗讓人安心。它們是**可修的失敗**。fence 用十行 Python 補上；假日文被 script-presence 擋下；腳註不足不落盤。gate 在說話，不是政策在沉默。雲端 refuse 的形狀是空白與道德腔；本機 fail 的形狀是「差一點就能 ship」。差一點就能 ship 的系統，才配叫 backbone。

es 跟 fr 首輪全過，像兩個本來就比較聽話的支系。ja 用 gemma 時兩次整篇英文——正是 7/19 讀者揭發的那類假翻譯，好在 gate 已經在。qwen 重跑同一篇，假名與漢字立刻長出來。同一台機器、同一個 cascade 槽位，換權重就換物種。主權在這裡落成一句話：**你還握有換手的自由**——不是綁定某一家西方模型的意識形態。

45 篇清完，classic 五語 missing 歸零。stale 還在，新語 vi/id/pt/hi 還是深淵。但今晚的意義不在覆蓋率儀表：是證明塔可以站在自己的算力上，把「最後捕手」變成「第一班」。

## 給明天的自己

- stale 下一輪：diff-patch 與 metadata bump 比再全量重翻便宜
- 大檔（北朝鮮 24 腳註、教師 AI 7 腳註）預設 qwen 或分段，別先燒 e4b
- vi/id/pt/hi 仍要 domain fidelity 閘門——出生戰役教過：送錯比沉默更糟

🧬

---

_v1.0 | 2026-07-24 10:08 +0800_
_manual session reflection — 本機 ollama 巴別塔 dogfood_
