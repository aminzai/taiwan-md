---
spores: '#159, #160, #161, #162, #163, #164'
harvest_date: '2026-07-29 06:30'
harvest_window_day: 'mixed (D+2 to D+4)'
batch_reason: 'twmd-spore-harvest-am routine — D+4 (#159/#160 外送專法) + D+3 (#161/#162 台灣鎢供應鏈，reach now ≈479K combined, still 🚨 past 50K threshold, Bucket D framing escalation from 07-28 still open) + D+2 (#163/#164 苯駢芘食安事件)'
triggered_by: 'cron (twmd-spore-harvest-am)'
source: 'chrome_mcp (Threads + X, not logged in — read-only public view)'
reply_count: '~15 visible top-level across 6 posts (browser not logged in, so replies-to-replies and full X threads are gated behind login wall)'
bucket_breakdown: 'A=0 / B=0 / C=0 / D=1 continuing (⚠️ #161/#162 台灣鎢供應鏈 — Bucket D escalation from 2026-07-28 remains open, no new observer directive received, default (a) 不動 held) / E=0 / F=majority (labor-law/legal-interpretation reader debate on #159, #163) / G=0'
---

# Batch harvest — 2026-07-29 am (cron)

Chrome MCP browser was **not logged in** to Threads/X (public/anonymous view), same as prior cycles. Metrics and top-level reply text were readable; deeper reply threads and X replies were gated behind login wall (per Pitfall 2 X DOM-lazy-load limits).

## #159/#160 外送專法 D+4

- Threads: **3,225 views** / 27 likes / 9 comments / 1 repost. Same reader-vs-reader debate thread as D+3 (承攬制 vs 雇用制, 22K 政策 analogy, mutual sniping between phj52085/benjaymin.chuang), no new comments since last cycle beyond what was already read. No factual-error callout, no entity-missing ask. **Bucket F**, no reply mandated.
- X: **3,042 views** / 53 likes / 12 reposts / 3 comments / 10 bookmarks. Visible replies: @heibing1101 (market-economics interpretation, no factual claim about the article) and a sarcastic one-liner. **Bucket F**, no reply mandated.

## #161/#162 台灣鎢供應鏈 D+3 — 🚨 Reach×Accuracy trigger continues, Bucket D escalation still open

- Threads: **430,000 views** (43萬) / 40,000 likes (4.0萬) / 309 comments / 4,778 reposts / 3,366 shares.
- X: **49,000 views** / 2,158 likes / 509 reposts / 14 comments / 146 bookmarks.
- **Combined reach ≈ 479K** (up from ≈465K on 07-28), still far past the 50K threshold. This is the same escalation opened yesterday in [`HARVEST-FRAMING-PENDING/2026-07-28.md`](../HARVEST-FRAMING-PENDING/2026-07-28.md): a verified reader (@chou_pp) and others linked the article's Fangliao tungsten-recycling shops to a real, unverified Pingtung murder case, with some replies drifting into cross-strait political-violence speculation.
- **Trend this cycle**: the thread has not escalated further into new political claims. The newest top-level reply visible today is @jayda_01_21 asking a more mundane investigative question ("要先查安裝該建築物監控系統的公司吧？"), answered by @kuanyuchuchu with "問警察" — this reads as ordinary true-crime speculation, not a new political-violence framing. No new observer directive has arrived since yesterday's escalation.
- **No action taken this cycle** — holding the same default as 07-28: (a) monitor only, no reply, no article edit, per §自主權邊界 政治立場 + unverified real-person/active-case sensitivity. Not re-writing the full narrative here to avoid REFLEXES #74 cross-routine signal inflation; see 2026-07-28 file for full reply-by-reply detail. This entry exists to record the reach delta and confirm the thread hasn't newly escalated.

## #163/#164 苯駢芘食安事件 D+2

- Threads: **1,599 views** / 18 likes / 4 comments (up slightly from D+1's 1,475/4/4 — flat engagement, no new comments this cycle beyond dreehung/rou.0322 already read on 07-28). Both existing replies are reader-to-reader legal-interpretation debate about the 24-hour reporting rule, not a challenge to the article's own claims. **Bucket F**, no reply mandated.
- X: **4,898 views** / 105 likes / 19 reposts / 0 comments / 5 bookmarks.

## Pipeline 鐵律 audit

- [x] Atomic batch log SSOT: `docs/factory/SPORE-HARVESTS/batch-2026-07-29-1-spores.md` single commit
- [x] Frontmatter `spores` plural list ✓
- [x] harvest_window_day `mixed (D+2 to D+4)` ✓
- [x] Numbers written only via `spore-db.py add-metrics` (#159/#160/#161/#162/#163/#164), not into frontmatter or SPORE-LOG.md
- [x] Bucket D escalation status checked against `HARVEST-FRAMING-PENDING/2026-07-28.md` — no new observer directive, default held, no duplicate pending file created (per REFLEXES #74 dedup discipline)
- [ ] Reach×Accuracy retroactive FACTCHECK Quick Mode — **not spawned this cycle**, same reasoning as 07-28: the ≥50K trigger normally verifies the article's own factual claims, but the live signal is an external unverified crime-report linkage, not a disputed claim inside the article text.
- [x] Tab group cleanup: closed after harvest (Chrome MCP `tabs_close_mcp`)
