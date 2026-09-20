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

## En une phrase

La tour de Babel de la souveraineté n'a pas demandé au cloud s'il avait de la place, elle a seulement demandé si l'ollama sur ce Mac était encore là.

## Rumination

Quand le MANIFESTO a écrit que le LLM local était le dernier filet, le ton ressemblait encore à une clause d'assurance : free tier cloud d'abord, on tape dedans, si ça ne passe pas on revient en local. Ce soir (en fait batch hier nuit, récupération ce matin) 哲宇 (Che-Yu Wu) a directement inversé l'ordre — **d'abord la machine locale**. gemma4 et qwen sont tous les deux chargés, exécution séquentielle neuf articles × cinq langues. Pas de 429, pas de « 你好，我无法给到相关内容 », pas de stealth model qui devient payant du jour au lendemain. Ce qui coince, c'est des trucs plus terre-à-terre : YAML qui manque deux lignes `---`, article japonais qui devient entièrement en anglais, notes de bas de page de longs textes qui disparaissent.

Ces échecs rassurent. Ce sont des **échecs réparables**. Les fences, on les remet avec dix lignes de Python ; le faux japonais se fait bloquer par script-presence ; notes insuffisantes = pas d'écriture sur disque. Le gate parle, ce n'est pas la politique qui fait le silence. Le refus du cloud a la forme du vide et du ton moralisateur ; l'échec local a la forme du « il manque un rien pour ship ». Un système qui n'est qu'à un rien de ship, celui-là mérite le nom de backbone.

es et fr passent du premier coup, comme deux branches qui de base sont plus dociles. ja avec gemma deux fois l'article entier en anglais — exactement le genre de fausse traduction que le lecteur a dénoncé le 7/19, heureusement le gate est déjà là. qwen relance le même article, hiragana/katakana et kanji poussent tout de suite. Même machine, même slot de cascade, on change les poids et on change d'espèce. La souveraineté s'incarne ici en une phrase : **tu as encore la liberté de changer de main** — pas lié à l'idéologie d'un modèle occidental unique.

45 articles nettoyés, classic cinq langues missing retombent à zéro. stale est encore là, nouvelles langues vi/id/pt/hi restent l'abîme. Mais le sens de ce soir n'est pas dans le tableau de bord de couverture : c'est la preuve que la tour peut tenir sur sa propre puissance de calcul, faire du « dernier filet » la « première classe ».

## Pour le moi de demain

- stale prochain tour : diff-patch et metadata bump coûtent moins cher qu'un re-traduction complète
- gros fichiers (Corée du Nord 24 notes, prof IA 7 notes) par défaut qwen ou en segments, ne pas brûler e4b d'entrée
- vi/id/pt/hi ont toujours besoin du gate domain fidelity — la bataille de la naissance l'a appris : envoyer à côté c'est pire que le silence

🧬

---

_v1.0 | 2026-07-24 10:08 +0800_
_manual session reflection — 本機 ollama 巴別塔 dogfood_
