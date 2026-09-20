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

## Una frase

La torre de Babel de la soberanía esta vez no preguntó si la nube tenía disponibilidad, solo preguntó si el ollama en este Mac seguía ahí.

## Rumia

Cuando el MANIFIESTO escribió que el LLM local era el último receptor, el tono aún parecía una cláusula de seguro: primero el free tier de la nube, si no aguanta se vuelve a local. Esta noche (en realidad anoche el batch, esta mañana la recogida) 哲宇 (Che-Yu Wu) invirtió directamente el orden — **primero local**. gemma4 y qwen ambos cargados, corriendo en serie nueve artículos × cinco idiomas. Sin 429, sin «你好，我无法给到相关内容», sin modelo stealth que de la noche a la mañana se vuelve de pago. Lo que atascaba era algo más terrenal: al YAML le faltaban dos líneas `---`, el artículo en japonés se volvió entero en inglés, las notas al pie de artículo largo desaparecieron.

Estos fallos tranquilizan. Son **fallos reparables**. La valla se completa con diez líneas de Python; el falso japonés es bloqueado por script-presence; notas insuficientes no se escriben en disco. La gate habla, no calla la política. La forma del rechazo de la nube es el vacío y el tono moral; la forma del fallo local es «casi listo para ship». Un sistema que casi puede ship, ese sí merece llamarse backbone.

es y fr pasaron a la primera, como dos ramas que desde el principio eran más obedientes. ja con gemma dos veces el artículo entero en inglés — precisamente ese tipo de falsa traducción que el lector denunció el 7/19, por suerte la gate ya está. qwen re-ejecuta el mismo artículo, kana y kanji brotan al instante. La misma máquina, la misma ranura de cascade, cambias los pesos y cambias de especie. La soberanía aquí se cumple en una frase: **todavía tienes la libertad de cambiar de mano** — no estás atado a la ideología de cierto modelo occidental.

45 artículos limpios, missing de los cinco idiomas clásicos vuelve a cero. stale sigue ahí, los nuevos vi/id/pt/hi siguen siendo abismo. Pero el sentido de esta noche no está en el indicador de cobertura: es la prueba de que la torre puede pararse sobre su propia capacidad de cómputo, volver al «último receptor» la «primera clase».

## Para el yo de mañana

- stale siguiente ronda: diff-patch y metadata bump salen más baratos que re-traducir todo de nuevo
- Archivos grandes (Corea del Norte 24 notas, profesor IA 7 notas) por defecto qwen o por segmentos, no quemar e4b primero
- vi/id/pt/hi siguen necesitando gate de domain fidelity — la batalla del nacimiento enseñó: enviar equivocado es peor que callar

🧬

---

_v1.0 | 2026-07-24 10:08 +0800_
_manual session reflection — 本機 ollama 巴別塔 dogfood_
