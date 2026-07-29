---
spores: '#159, #160, #161, #162, #163, #164'
harvest_date: '2026-07-30 06:30'
harvest_window_day: 'mixed (D+3 to D+5)'
batch_reason: 'twmd-spore-harvest-am routine — D+5 (#159/#160 外送專法) + D+4 (#161/#162 台灣鎢供應鏈，reach now ≈479K combined, still 🚨 past 50K threshold, Bucket D framing escalation from 07-28 remains open with no new observer directive) + D+3 (#163/#164 苯駢芘食安事件)'
triggered_by: 'cron (twmd-spore-harvest-am)'
source: 'chrome_mcp (Threads + X, not logged in — read-only public view)'
reply_count: '~13 visible top-level across 6 posts (browser not logged in, so replies-to-replies and full X threads are gated behind login wall)'
bucket_breakdown: 'A=0 / B=0 / C=0 / D=1 continuing (⚠️ #161/#162 台灣鎢供應鏈 — Bucket D escalation from 2026-07-28 remains open, no new observer directive received, default (a) 不動 held) / E=0 / F=majority (labor-law/legal-interpretation reader debate on #159, #163; economic/sarcastic commentary on #160) / G=0'
---

# Batch harvest — 2026-07-30 am (cron)

Chrome MCP browser was **not logged in** to Threads/X (public/anonymous view), same as prior cycles. Metrics and top-level reply text were readable; deeper reply threads and X replies were gated behind login wall (per Pitfall 2 X DOM-lazy-load limits).

## #159/#160 外送專法 D+5

- Threads: **3,235 views** / 27 likes / 8 comments / 1 repost. Same reader-vs-reader debate thread as prior cycles (承攬制 vs 雇用制, 22K 政策 analogy, mutual sniping between phj52085/benjaymin.chuang/san05042000). Comment count ticked down from 9 to 8 versus yesterday — likely one comment deleted by its author or Threads, not a tracking error (no new content appeared to replace it). No factual-error callout, no entity-missing ask. **Bucket F**, no reply mandated.
- X: **3,049 views** / 53 likes / 12 reposts / 3 comments / 9 bookmarks. Same two visible replies as prior cycle (@heibing1101 market-economics interpretation, sarcastic image reply about 蘇柏豪 quote). **Bucket F**, no reply mandated.

## #161/#162 台灣鎢供應鏈 D+4 — 🚨 Reach×Accuracy trigger continues, Bucket D escalation still open

- Threads: **430,000 views** (43萬) / 40,000 likes (4.0萬) / 309 comments / 4,786 reposts / 3,370 shares.
- X: **49,000 views** (4.9萬) / 2,165 likes / 510 reposts / 14 comments / 145 bookmarks.
- **Combined reach ≈ 479K**, essentially flat versus yesterday's ≈479K — the viral spike has plateaued. This is the same escalation opened in [`HARVEST-FRAMING-PENDING/2026-07-28.md`](../HARVEST-FRAMING-PENDING/2026-07-28.md): a verified reader (@chou_pp) and others linked the article's Fangliao tungsten-recycling shops to a real, unverified Pingtung murder case, with some replies drifting into cross-strait political-violence speculation.
- **Trend this cycle**: no new escalation. The newest visible top-level replies continue the same mundane investigative-question thread from yesterday (@jayda_01_21 / @kuanyuchuchu on checking the security-camera installer / asking police) — no new political-violence claims surfaced today. No new observer directive has arrived.
- **No action taken this cycle** — holding the same default as 07-28/07-29: (a) monitor only, no reply, no article edit, per §自主權邊界 政治立場 + unverified real-person/active-case sensitivity. Not re-writing the full narrative here to avoid REFLEXES #74 cross-routine signal inflation; see 2026-07-28 file for full reply-by-reply detail. This entry exists to record the reach delta (plateau, not renewed growth) and confirm the thread hasn't newly escalated.

## #163/#164 苯駢芘食安事件 D+3

- Threads: **1,650 views** / 20 likes / 4 comments / 1 repost (up slightly from D+2's 1,599/18/4 — flat engagement, no new comments this cycle beyond dreehung/rou.0322 already read). Both existing replies are reader-to-reader legal-interpretation debate about the 24-hour reporting rule, not a challenge to the article's own claims. **Bucket F**, no reply mandated.
- X: **4,964 views** / 106 likes / 19 reposts / 0 comments / 5 bookmarks.

## Reply-posting note (this cycle)

No replies were drafted for auto-post. All 6 spores' visible reader comments this cycle are Bucket F (interpretation disagreement / political-economic opinion among readers) or continuing Bucket D (deferred to observer, per HARVEST-FRAMING-PENDING). Per MANIFESTO §存在結構「需要人類決策」and REFLEXES #26 v2 (Human-only: post 留言回覆 to Threads/X — 人際信任修復必須 human-to-human), and per this session's own safety boundary on sending messages on the user's behalf without explicit in-chat permission, no reply was posted to any platform this cycle — consistent with there being no Bucket A/C/E draft that required posting today.

## Pipeline 鐵律 audit

- [x] Atomic batch log SSOT: `docs/factory/SPORE-HARVESTS/batch-2026-07-30-1-spores.md` single commit
- [x] Frontmatter `spores` plural list ✓
- [x] harvest_window_day `mixed (D+3 to D+5)` ✓
- [x] Numbers written only via `spore-db.py add-metrics` (#159/#160/#161/#162/#163/#164), not into frontmatter or SPORE-LOG.md
- [x] Bucket D escalation status checked against `HARVEST-FRAMING-PENDING/2026-07-28.md` — no new observer directive, default held, no duplicate pending file created (per REFLEXES #74 dedup discipline)
- [ ] Reach×Accuracy retroactive FACTCHECK Quick Mode — **not spawned this cycle**, same reasoning as prior cycles: the ≥50K trigger normally verifies the article's own factual claims, but the live signal is an external unverified crime-report linkage, not a disputed claim inside the article text.
- [x] Tab group cleanup: closed after harvest (Chrome MCP `tabs_close_mcp`)
