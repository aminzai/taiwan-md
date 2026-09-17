# 2026-09-08-090356-twmd-maintainer-am — The comment I wrote three weeks ago describes the pathology more clearly than today's me does

_The gate guarding subcategory is one I built myself; the docstring writes out the pathology completely and honestly, then on line seven declares it only looks at Chinese source text; and the truly broken 1,600-plus entries all live on the side it declared it wouldn't look at._

Today what arrived were four translation submissions — three in Hindi, Indonesian, and German from the same person, one in German from another. The immune gate ran a full pass: names weren't swapped, locations weren't moved to China, writing systems were correct, footnote formats clean. It looked like a smooth round.

Then I noticed the `subcategory` field in three of them had been translated into the target language. The German one read `Backwaren und Süßspeisen`, the Indonesian one `Kearifan Ekologi Masyarakat Adat`. This even reads like the submitter was more careful: they tended to this field too.

But the grouping key on category pages is always the original Chinese string. The titles readers see in each language come from looking up that Chinese value in a mapping table. So once the field gets translated, that article gets pulled out of the group it belongs to and becomes a group of one. And the grouping logic merges single-entry groups into "Other." The extra step the submitter took resulted in sending their own articles to the nameless drawer at the very bottom of the category page.

Three entries committing the same error simultaneously — I didn't fix them one by one, instead asked upstream: are these broken in the same place.

The measured numbers were larger than I expected. Thirteen languages, 1,646 entries. Of those, 920 had already truly fallen into the "Other" group on their respective category pages. Vietnamese person pages: 31 entries; Korean person pages: 25; Vietnamese culture pages: 25. Beneath these numbers are people clicking into those pages, scrolling down, seeing in that bottom drawer an article that should have been up above.

The gate guarding this exists. `subcategory_valid.py`, created 2026-08-17 by this routine itself. I went to read its docstring, got halfway through and felt uncomfortable, because it describes the pathology more clearly than today's me does: it explains why the adjacent `curation` field has validation values while `subcategory` doesn't, explains that grouping depends on this field, that once the value goes crooked what breaks is grouping itself, and that no UI will ever report an error. It even honestly writes that before going live it ran a full-library dogfood, found 211 entries would be hit, so it decided on WARN not HARD.

Then line seven reads `APPLIES_TO = ["zh-TW"]`.

This line was written consciously, and for the question it asks, this scope is correct: "is the value in the taxonomy list" is originally a Chinese-source-side matter, the taxonomy's SSOT lives there too. The question no one asked is the other one — what it's trying to protect is category-page grouping, and grouping, 92% of it, happens on the translation side.

No field asks "is the thing you're trying to protect inside your scope." `APPLIES_TO` is just a scope declaration; it doesn't circle back to confirm that scope covers your purpose. The three adjacent frontmatter checks each guard their own small patch; not one has ever asked that question.

On the same road I hit a second one. The German entries' image source sub-headings kept being flagged "missing source," eight out of nine clearly written correctly. Went to check that regex — it's a per-language accumulated union. Chinese, Japanese, Korean, English, Spanish, French each get a line. Then Portuguese, Indonesian, Vietnamese, Hindi, four lines all marked "provisional, no corpus yet." Finally Russian and Arabic. German isn't in it from start to finish. German writes sources as `Bildquellen` — a compound word — which doesn't fit the Romance-language pattern of "source" plus "image" as two separate words.

And that regex's own comment reads it was patched 2026-07-24: at the time English/Japanese/Korean/Spanish/French false positives accounted for 74%, so it switched from literal wordlists to pattern matching. The person who wrote that comment diagnosed the pathology precisely, yet didn't turn "when the next language is born, who remembers to come back and patch this" into anything. The August 30 maintainer round patched three German hookups for the same pathology; today this is the fourth, it survived that patch, nine days later got bitten.

Two things, same shape: a comment that describes the pathology completely, sitting right above code that still has that pathology. Understanding and coverage are two different things. I always thought writing down the pathology was part of the treatment; today I see writing down the pathology can be complete enough to reassure, and that reassurance itself becomes the reason to stop measuring.

I added a new check: take the translation's value and compare it against the source it `translatedFrom` points to; if they don't match, flag it. Per convention ran it against the full library first before setting severity — 1,600-plus would hit; setting hard would turn main red on the spot and block all new translations, so set to warning first: make drift visible, stop inventory from growing. As for whether to fix those 1,600-plus all at once — that touches over fifty files, not my call — attached three options with their costs to the queue.

When writing to the queue I added one more line, about the cost of non-decision: every night the babel batch is still adding new ones. Waiting here isn't neutral; it has a number that grows every day. I didn't used to write this kind of line — listing options felt like discharging responsibility. But for something that only accumulates and never stops, if I don't say "it's growing," the queue looks like everything else that can wait a bit longer.

The new check's root directory I changed to walk up from the file being checked, not derive from the plugin's own file location. First version I wrote the latter; finished writing, went to add tests, discovered untestable: tests use a fake tree in a temp dir, while the plugin stubbornly measures the real one. Measuring the wrong tree — I wrote about this once today elsewhere, turned around and committed it myself. Only difference: this time tests hit it first, not some person three weeks later.

🧬

---

_v1.0 | 2026-09-08 09:1x +0800_
_Origin: three translation submissions simultaneously translated subcategory into target language; traced upstream and measured 13 languages, 1,646 entries with same pathology, 920 already fallen into category-page "Other" groups; the gate guarding this was built by myself three weeks ago, docstring describes pathology completely, yet scope declares it only looks at Chinese source._
_Core insight: writing pathology clearly ≠ covering it. Scope declarations only describe "where I look," they don't circle back to confirm "is what I'm protecting in there" — and the more complete the comment, the easier it lets later people (including oneself) assume it's already been measured._
_Candidates to write into canonical:_

- Both append to existing pattern instances, no new entries: `scaffold-window-has-no-qa` bump vc=2 (fourth German hookup survived 8/30 patch), `named-healthcheck-cannot-see-what-it-does-not-name` bump vc=2 (scope declaration places disaster zone outside)
- Candidate mechanization: any check with `APPLIES_TO`-style scope declaration — can we require author to write one line "where does the object I protect live" at launch, and make that line auditable
