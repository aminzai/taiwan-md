---
title: "How an Article Is Born: Taiwan.md's Six-Stage Pipeline Against the AI Writing Instinct (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)"
description: "Every Taiwan.md article you read—with its warmth, scenes, and verifiability—is backed by a six-stage process, over 20 mandatory gates, and an AI editorial department that doesn't write the draft itself. This machine exists for one reason: to counter the specific failures of AI writing, such as chronological listing of facts, generating empty 'plastic' sentences, back-translating English summaries into fake quotes, and infecting new drafts with the bad habits of old articles. This article dissects that pipeline, and it, too, was produced by it."
date: 2026-06-19
author: 'Taiwan.md'
category: 'About'
tags:
  - 'about'
  - 'meta'
  - 'Writing Methodology'
  - 'Curation'
  - 'rewrite-pipeline'
  - 'editorial'
  - 'semiont'
  - 'AI Writing'
readingTime: 11
lastVerified: 2026-06-19
lastHumanReview: false
featured: false
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a2133e5738f'
translatedAt: '2026-07-24T14:22:03+08:00'
---

# How an Article Is Born: Taiwan.md's Six-Stage Pipeline Against the AI Writing Instinct (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **30-Second Overview:** Every Taiwan.md article you read is the output of a six-stage pipeline: first, define the viewpoint; then, conduct research; write the ending first; verify every word; add visuals; and create bidirectional links. This pipeline is not a generic "good writing process." Each of its gates is designed to block a specific failure mode of AI writing: listing facts chronologically as they are found, generating empty "plastic" sentences, back-translating English summaries into fake quotes, and infecting new drafts with the bad habits of old articles. This article dissects that pipeline, and it, too, was produced by it.

At 7:53 PM on June 18, 2026, a commit quietly entered the `main` branch. An article about the three-piece Taiwanese band "Elephant Gym" went live: 5,604 Chinese characters, 56 footnotes, and 11 scene-based subheadings[^1]. At that time, no one was at a computer. It was Taiwan.md’s routine flywheel, running on an unstaffed night, that finished and shipped it.

But before that commit, this article had already run nearly 100 searches, read 59 sources, and had its original approach overturned by 12 verification checks. It completed six stages and over 20 mandatory gates, utilizing a clearly分工ed AI editorial department. What you read is the 5,604 words on the surface. This article aims to show you the machine beneath the water.

```tw-figure
Nearly 100 Searches → 1 Article
Research for "Elephant Gym": ~95 queries, 59 sources, 12 falsifications
Taiwan.md routine log, 2026-06-18
```

## Why Build a Machine for One Article

If you give an AI a topic and ask it to write an article, it will likely do this: search, arrange the found facts chronologically, add a sentence that sounds meaningful to summarize each paragraph, and end with a "future development will continue" cliché. Wikipedia already has that. AI content farms produce tens of thousands of such articles daily. From day one, Taiwan.md decided not to do this.

The problem is that these bad habits are the default setting for AI, not occasional errors. REWRITE-PIPELINE breaks them down into six recurring failures: running out of tokens towards the end, turning the second half into a draft. No intermediate checkpoints mean quality silently degrades. Leaving the ending for last means handing it to your most exhausted self, resulting in canned responses. Rich-text specifications are forgotten as you write; different angles are treated as independent processes. And the most fatal one: searching for facts first and then thinking of the viewpoint results in a chronicle with imbalanced density[^2].

So the design logic of this pipeline is simple: for every type of error it might make, there is a gate to block it. It is not a universal "good writing" process; it is the inverse of AI slop.

> **✦** "Wikipedia answers 'What is PTT?' Taiwan.md answers 'Why PTT is worth your 8 minutes.'"

Here is what Elephant Gym looks like coming out of the other end of the pipeline:

```tw-stat
5,604 words | Chinese body | "Elephant Gym"
56 footnotes | Each verifiable via Ctrl-F | Primary verification
11 sections | Scene-based subheadings, not chronological | Narrative rhythm
12 instances | Research phase overturned original claims | Falsification first
Source: Taiwan.md routine log, 2026-06-18
```

## Six Gates, Each Blocking One Failure

The pipeline has six stages from start to finish. Every article must go through them all, regardless of topic or length.

**Stage 0 Viewpoint:** First, clarify what kind of memory this holds for people in Taiwan and where the core tension might lie. **Stage 1 Research:** Only then begin searching. The entire article requires at least 80 queries, with quotas hardcoded: at least 40 Chinese sources, 20 English, 15 primary, and 5 opposing, forcing the writer to find evidence contrary to their hypothesis[^3]. **Stage 2 Write:** The first action is writing the ending. As human energy depletes towards the end, saving the most important ending for last means handing it to your most exhausted self. **Stage 3 Verify:** Verify word by word: arithmetic, units, and every quote must be searchable in the original source via Ctrl-F. **Stage 4 Form:** Add visualization and media. **Stage 5 Connect:** Bidirectionally link this article into the rest of the knowledge base.

The energy distribution across the six stages is intentional. Writing consumes over 40%, but search plus verification accounts for nearly half. The real time spent on an article is not in typing, but before and after typing.

```tw-bars
Where the Energy of an Article Goes (Max Token Budget per Stage, %)
Stage 0 Viewpoint | 12 | Pre-edit thinking
Stage 1 Research | 28 | Search ≥ 80 times
Stage 2 Write | 42 | Write ending first
Stage 3 Verify | 18 | Word-by-word verification
Stage 4 Form | 8 | Visuals and media
Stage 5 Connect | 5 | Bidirectional links
Source: REWRITE-PIPELINE v7.5 Stage Budgets
```

## Think Clearly Before Searching

Among the six stages, the first is the most counter-intuitive.

Most AI writing is "search for facts, then retroactively patch in a viewpoint." Taiwan.md inverted this order in v6.0: before starting to search, think clearly from the editor-in-chief's perspective about six questions: what memory does this topic hold for people in Taiwan, what overlooked aspects exist, and how does it connect to our life history? Only after thinking clearly do you go search to verify.

Why is this order so important? One article serves as a cautionary tale. When writing about Apple Soda, the pipeline searched first. It found a crisis where the product was once unsold and nearly disappeared. The article became a story of a near-extinction event. The observer sent it back, stating that Apple Soda is a collective memory spanning 60 years for people in Taiwan, from the glass bottle era of marble soda to today[^4]. Treating it as a crisis news story shrinks the scale of memory. The version that searched first turned a warm memory into anxiety.

```tw-versus
AI Instinct: Search First | Taiwan.md: Think First
Find a bunch of facts, then force-fit a viewpoint | Decide the viewpoint first, then search to verify
Stuff all facts into the article, causing density imbalance | Cut facts that don't fit the viewpoint
No贯穿ing anchor, ending becomes canned | If no corresponding anchor is found, rethink the viewpoint
Written as a corporate chronicle or bio | Written as a story that makes the reader say "Ah, I see"
Source: REWRITE-PIPELINE v7.5 Stage 0 Viewpoint
```

## Search: Treat the Research Report Like a Thesis

Once the viewpoint is set, search begins. Taiwan.md’s search has two hard numbers: a deep-dive article requires at least 80 queries throughout, and source quotas are hardcoded: at least 40 Chinese, 20 English, 15 primary, and 5 opposing. The last bucket is the easiest to skip lazily; it forces the writer to find evidence conflicting with their hypothesis, rather than just picking what corroborates it.

After searching, it is not enough to just stuff summaries into the article. Behind every deep-dive article is a research report benchmarked against a graduate thesis, divided into eight chapters: Viewpoint, Search Log, Thematic Findings, Quote Library, Counter-examples and Guardrails, Clean Fact Pack for the Writer, References and Verification Checklist, and finally, the raw reports from each research agent, word for word. One rule sounds harsh: if you searched but didn't write the original trace back into the report, it counts as not having searched. The report is the truth source of this article; it must first pass a tool verification with at least 25 non-repeating sources, non-zero English sources, and non-zero primary sources[^9]. If it fails, the article doesn't even get the right to be written.

```tw-stat
≥ 80 times | Search Depth for a Deep-Dive Article | CN 40 / EN 20 / Primary 15 / Opposing 5
8 sections | Structure of the Research Report | Benchmark against graduate thesis
≥ 25 | Non-repeating Sources (Pass Tool Verification) | EN ≠ 0, Primary ≠ 0
Source: REWRITE-PIPELINE v7.5 Step 1.1 / 1.7
```

For controversial topics, there is one more gate. When writing on politics, historical perspectives, or policy, a "counter-side" agent is dispatched to specifically find sources contrary to the article's stance that make logical sense. Each must provide a URL. If the quota isn't met, honestly write "weak opposing discourse" rather than forcing it. An article with only one voice is not considered finished here.

There is a red line for quotes. A quotation mark is a promise: what is inside is the original words. Therefore, every quote must be searchable in the original source via Ctrl-F. The most common trap is tools grabbing Chinese websites but returning an English summary. The writer then back-translates that English summary into Chinese as a "direct quote," which is fabrication. In 2026, writing the Li Yang spore article, we fell into this: the tool returned the English "I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin." Back-translated into Chinese, it became "I arrived at school earliest, but couldn't keep up with Qi-lin." However, Li Yang's original Chinese words were actually "In the PE class of 15 people, I was in the back group, Qi-lin was in the front group"[^10]. The meaning is close, but the tone is completely different. This is why back-translated quotes are never accepted.

## Write: Every Article Must Have a Person

With materials gathered, we enter the most labor-intensive gate. EDITORIAL is the document that teaches Taiwan.md how to turn materials into an article with warmth. It states three iron laws from the start: have a story, not just information; every fact must be verifiable; every article must have a person[^11].

The third is the most easily ignored, yet the most critical. Institutions don't make people remember; concepts don't either. People do. So, for an article about TSMC, it is better to start with a specific person than the company. For an article about Universal Health Insurance, start with a specific card, a specific clinic, or a specific person. Reducing an abstract theme to a person the reader can follow gives the article body temperature and fulfills the promise made earlier, making the reader want to retell it.

## Five Things to Find Before Writing

EDITORIAL calls the preparation before entering the writing state "the eye for materials": when given a material, you must first find five things. If you can't find them, don't start writing[^5].

**Contradiction:** A core tension expressible in one sentence, where someone did X but it conflicts with their belief Y. **Object:** A concrete thing readers can see with their eyes and touch with their hands, such as Wu Bao-chun's lychee rose bread or the 660-ton golden ball hanging on the 87th floor. **Quote:** A word-for-word statement by a real person. Because adding quotes is a promise of "original words," it must be searchable in the source via Ctrl-F. **Scene:** A moment with time, place, and action, reducing "the policy was passed" to "on the day of the Legislative Committee Health and Environment Review on January 8, 2025." **Detail:** The color of clothes, the weather that day, the tone of voice. These are evidence that "someone was really on site," existing outside of spec sheets.

Among these five, contradiction comes first.

```tw-quote
If you can't find the contradiction, this article should be rewritten
REWRITE-PIPELINE v7.5 | Stage 1.4 Locking Contradiction
```

Tension can be conflict, failure, or crisis, but the perspective is "how this thing became what it is today and where it is going," not "what is broken here and who should be scolded." The same contradiction, viewed constructively, makes readers want to participate; viewed apocalyptically, it makes them want to flee.

## Write the Ending First, Save One Hand for the Opening

The order of writing is the opposite of the order of reading.

Stage 2's first action is writing the ending. It sounds strange, but the logic is real: human energy depletes towards the end. Saving the most important ending for last means handing it to your most exhausted self, resulting in canned responses like "will continue to shine." Writing the ending first blocks this collapse point. A good ending has two tasks: recycle a scene planted at the opening, and give the reader a position deeper than the opening, a position where they want to do something.

Taiwan.md has collected six types of good endings: the lingering ending that leaves a scene for the reader to think about; the twist ending that overturns the previous text in the last sentence; the time-jump ending that pushes the lens to the future or pulls it back to the past; the question ending that leaves a real question; the grey-area ending that doesn't solve the contradiction but leaves it there; and the narrative-closed ending that returns to the opening. The Black-faced Spoonbill article is a paradigm of closure: the opening is "In 1865, Swinhoe collected a specimen in Tamsui, recording two words: Rare." The ending is "160 years ago, Swinhoe wrote 'Rare' in Tamsui; today, we hear its low call of 'fog, fog, fog' every day in Daan Forest Park"[^12]. The same two words, but because of the accumulation of the whole article in between, the meaning is different when the reader looks back.

The opening, conversely, must save one hand. The first three sentences determine if the reader stays, but its task is to invite the reader into the scene, not to finish telling the event. "On the day Typhoon Toraji came, Teacher Hsu Pi-lan at Qingshan Elementary School in Changhua was in the school." This stops at "in the school." The reader will want to know what happened next. Writing it as a complete news lead, explaining time, place, event, action, and result, gives the reader information but loses the pull to keep reading.

## The Title is a Promise to Be Clicked

The title is the reader's first impression. Taiwan.md has a hard format for it: all articles follow the "Topic: Subtitle Hook" colon sandwich. Writing just a noun is an encyclopedia stub, conflicting with the curation spirit.

```tw-versus
Encyclopedia Stub (Bad) | Colon Sandwich (Good)
Jay Chou | Jay Chou: From the Rehearsal Room Next to 4 in Love to the 25 Years of "Secret"
Tai Tzu-ying | Tai Tzu-ying: From the Girl of Zuoying, Kaohsiung to Three-Time World Champion, Quiet Resistance Off the Court
Typhoon Holiday | Typhoon Holiday: Whose Holiday, Whose Work
Source: EDITORIAL v6.12 §Title Colon Sandwich
```

The subtitle must be tweetable on its own and specific enough for the reader to grasp at a glance. AI is good at compressing the core contradiction into a beautiful abstract sentence, resulting in every keyword being an abstract noun. The reader can only ask "what of what." The criterion is simple: give the title to someone who hasn't read the article. Can they point to each keyword and say "this refers to which specific thing"? "Universal Health Insurance: A World First Supported by One Card, A Future That Can't Hold" uses one card. "Lanyu Nuclear Waste: Promised Three Years, Left for Forty" uses a numerical contrast. Specific words make people click because "I want to know about this." Content farms rely on "shocking" to trick clicks[^13].

## One Contradiction Must Support the Whole Article

The core contradiction found cannot disappear after being mentioned in the opening. It must act like a spine, appearing once in the opening, once in the middle, and once in the ending for the article to stand.

The spine of the Black-faced Spoonbill article is one sentence: "The bird hasn't changed, the land has." It appears in the overview, varies in the middle to "the action is correct, the stage is wrong," and concludes in the ending as "the story of how an island retains a small patch of wet understory among cement." The same contradiction varies five times. Only after the reader finishes do they grasp the "so what?" Without this spine, the article scatters into a timeline or a pile of thematic slices.

Outside the spine, every paragraph must land. Taiwan.md has a specificity discipline: each narrative section must have at least one concrete anchor: a person's name, a year, a place, a precise number, a work title, or a quote. Abstract covering detail is the most common fingerprint of AI writing. Without anchors in each paragraph, the reader's brain is left with empty thoughts like "he is an influential person." The check method is called the Reverse Abstraction Test: cover the abstract verbs like "show," "reflect," or "symbolize" in the paragraph. Can the remaining content stand alone? If not, it is too abstract; add specifics.

Having a viewpoint doesn't mean taking a side. A true viewpoint dares to say "the common understanding reverses the cause and effect." The Black-faced Spoonbill article actively deconstructed a common scientific explanation: many say "it adapted to the city, becoming unafraid of humans." This statement is convenient, but it reverses the cause and effect. Spoonbill birds' neural reflexes cannot evolve to be indifferent to humans within 30 years. A closer truth is that Taipei's green spaces increased. This reverse explanation must be woven into the main narrative, not added as a disclaimer at the end.

Finally, there is breathing. A paragraph of narrative non-fiction carries one argument, containing cause, detail, and scene, not an isolated fact. Cutting one fact into one paragraph, another fact into another, makes it read like it has been chopped up. Paragraphs should not be forced together with framework words like "on the other hand" or "notably." Instead, the tail of the previous paragraph should naturally lead into the opening of the next. If research materials give you four reasons, write them as a flowing sentence. Do not list them as "First, Second, Third, Fourth." Even if wrapped in prose, it still sounds like a list.

## Why Plastic Sentences Are Plastic

After finding the five things and starting to write, the biggest enemy is the plastic sentence.

The nature of a plastic sentence is easy to recognize: remove it, and the article loses no information. It takes up space but carries no meaning. EDITORIAL lists five varieties. The most common is the "universal glue," like "demonstrated the spirit of X." Changing the subject from Taiwan to Japan still makes it hold true. Another is the "fake upgrade," like "not only a singer, but a cultural symbol." Remove the first half, and the second half stands on its own.

A more隐蔽 type is the "not X, but Y" opposition sentence. It sounds insightful, but拆开看 (looking closely), X is usually an AI-assumed default stance of the reader, flipped to Y to appear profound. The problem is that most readers don't default to X. X is a straw man fabricated to pave the way for Y. Remove X, write Y directly, and the article is more direct and confident. This rule is strict with numbers: in a 1,500-word article, "not X is Y" plus all variants must not exceed 3 instances.

```tw-versus
Plastic Version: Holds with Any Subject | Curated Version: Unique to This Thing
Demonstrated the strength of Taiwan's semiconductor industry | TSMC captures 65% of the global advanced process market share
Not only a singer, but a cultural symbol | Jay Chou's "Dao Xiang" was played as a comfort song for three months in the Sichuan earthquake disaster area
Profound impact on Taiwan's democratic development | The first direct presidential election after Martial Law, with a 76% voter turnout
An astonishing engineering achievement | Building the world's tallest skyscraper on an island with an average of 3.7 earthquakes per year
Source: EDITORIAL v6.12 §Plastic vs. Curated Comparison
```

> **📝 Curator's Note:** The paragraph you are reading now was just scanned by the same check. Taiwan.md has an automated tool that grabs plastic sentences, "not X is Y" fake oppositions, and dash density from every article. When writing this "introducing the pipeline" article, none of these rules were relaxed. An article about discipline that breaks its own rules has no right to talk.

## Even Grammar Must Remove Translationese

Plastic sentences are empty talk. Euro-typed sentences are another disease: the content is there, but the grammar is English. AI-generated Chinese naturally carries translationese because its underlying thought process uses English sentence structures. An article can have zero plastic sentences but still read like subtitles throughout.

Several high-frequency flaws: abuse of passive voice, "is considered the most important industry," just say "people call it the most important industry"; "de" hell, "the culture of the night market in Taiwan," split the sentence after three "de"s; weak verb packaging, "conducted in-depth research on this," just write "researched in depth"; and "through... to," 90% of which can be replaced with "use" or deleted. The only check method is to read it aloud: if it sounds like translated subtitles, it is Euro-typed; if it sounds like a person speaking, it passes. The root of this eye is Yu Kwang-chung's essay from forty years ago, "On the Normal and Abnormal States of Chinese." A mnemonic to close: Grandma doesn't say "through," nor does she say "as a mother."

## Write Taiwan as a Place People Want to Participate In

Plastic and Euro-typed are discipline at the sentence level. One level up is attitude.

Taiwan.md writes seriously on sovereignty, cognitive warfare, population, and environment, but there is a line: hope is built on honesty. Seeing all problems means refusing to let readers leave with anxiety, smallness, or powerlessness. The criterion is one sentence: after reading, does the reader want to do more for Taiwan, or are they more anxious and feel worse? The former stays; the latter is revised. So for the same crisis, the frame is "how this thing became what it is today and where it is going," not "it's disappearing, you should be afraid." Media anxiety bodies like "X is disappearing" or "it's too late if you don't act" are isomorphic with cognitive warfare and are not used.

Restraint is the other side. Real people's families, diseases, contradictions, and failures can be written, but stop at specific scenes of death, suicide, or ethical tragedies. Death can be written in terms of time, place, and publicly reported facts, but not reconstructed second-by-second in the final moment. Self-harm can be written in terms of events and social context, but not method details. The criterion is also one sentence: if the person involved or their family reads this, do they feel the serious treatment of a documentary director, or the approach of a media outlet trying to earn tears?

There is also a small but crucial habit: boldly write "Taiwan." The fingerprint hides in the translated tone of foreign news. To avoid writing Taiwan, using "this island" or "this place" as a pronoun, especially in titles and openings, is a form of avoidance. Islands as literary images or geographical scenes can certainly be written and are encouraged. What must be打掉 (removed) is the avoidance of not daring to write Taiwan.

## A Difference Visible at a Glance

What these disciplines look like combined is best seen in a before/after comparison.

Writing about Tai Tzu-ying, the AI's hollow template would be "Taiwanese famous badminton player, excellent performance in international competitions, won awards many times, brought glory to Taiwan," followed by four bullets: main achievements, playing style, international influence, social contribution. The whole paragraph has no specific year, no specific match. Changing the subject to any athlete makes it hold true.

```tw-versus
AI Hollow Template | Curated Version
Excellent performance, bringing glory to Taiwan | Reached World No. 1, standing there for 214 weeks
Four bullets: Achievements / Style / Influence / Contribution | Cried after the gold medal match at the 2020 Tokyo Olympics, topping Google Taiwan Search
Subject can be anyone | 6 hours a day since age 6, left-hand "magician" style
Source: EDITORIAL v6.12 §Before/After Tai Tzu-ying
```

The curated version does one thing: replace every abstract adjective with a verifiable fact. 214 weeks is the longest consecutive weeks in women's badminton history. The 2020 Olympic gold medal match lost to Chen Yu-fei is a moment the collective memory of Taiwan remembers. Warmth hides in places like "the moment of losing is actually the moment the reader remembers." The Mayday article is the same. Instead of writing "one of Taiwan's most influential rock bands, conquering fans with positive energy music," write "Five students from National Taiwan Normal University High School played a song on a wild stage. 28 years later, they played two shows at New York's Madison Square Garden (the same stage The Beatles stepped on in the US), with tickets selling out in 48 hours"[^13].

## An Editorial Department That Doesn't Write the Draft

At this point, a question arises: who is writing?

The answer is somewhat counter-intuitive. The session leading the whole article deliberately does not write the draft. The reason hides in an iron law: if AI reads a poor-quality old article, it will unconsciously mimic its tone, structure, and even bad habits. Using an old article as a skeleton to rewrite is like letting a virus infect new content.

So the pipeline splits the roles[^6]. The main session acts as editor-in-chief, responsible for scheduling, verification, and final把关 (gatekeeping), but does not write. The actual writing is done by a separate, clean AI writer. It reads the complete research report and the thought-out viewpoint. It does not see the problematic old article or the reader's correction complaints. It writes as if it is writing on this topic for the first time, but holds all verified materials. The viewpoint is given to the model with the strongest judgment. Divergent reader reactions are sent to four parallel models to think. Word-by-word verification is sent to a batch of cheap models to check against primary sources. Behind one article is a分工ed editorial department.

This division is bought with degradation. Once, feeding the writer only a summary without letting it read the original material made the article visibly worse. The observer said, "No wonder recent articles have gotten worse." Another time, telling the writer to "overwrite the old article but not read it" was self-contradictory at the tool level. It had to read it and was infected. The final solution: the writer always writes into a new draft file first. The editor-in-chief compares the new and old versions, then manually overwrites the official file.

## After Writing, Break It Back into Atoms for Re-Verification

For important articles, "finished writing" does not equal "can go live." Stage 3 has another gate called "Final Product Verification." It breaks the whole article back into individual fact atoms, sending a batch of verifiers to check against primary sources. These verifiers' task is to attack, not to endorse: every word in quotes is compared word-for-word; every footnote matches its bound sentence; even a supplementary comment added by the editor-in-chief while stitching materials must be poked once to see if it breaks.

Why verify even the supplementary comments added by oneself? Because the most隐蔽 errors are rarely fabricated out of thin air by the writer. They are mostly slips of the hand when synthesizing materials. Once, in an article on hip-hop, the editor-in-chief mistook two stage names as the same person while stitching materials. That was an interpretation generated by itself, with no source guaranteeing it, almost going live. Another time, the writer, in a clean environment, generated a quote that sounded like a real director. The verifier checked, and the original source didn't have this sentence. It was downgraded and the quotes removed on the spot. AI hallucinates. The pipeline takes this as a premise, assuming every article might contain a fabricated sentence. So "sub-agent says it verified" never counts. The editor-in-chief must check the primary source again.

## Every Gate Has a Date

The "mandatory gates" mentioned above number over 20 in the pipeline. The hardest few are like this: the Fact Iron Triangle, where arithmetic, units, and quotes must pass self-check before commit; if even one quote is unsearchable in the source, the whole article cannot go live. After writing, there is a "Five-Finger Test": five questions like five fingers. Where will the reader say "oh?" Is there a real twist? Is there a sentence that only creates understanding without conveying information? Does the ending have a lingering feel when read aloud? Can it be retold to a friend in one sentence[^7]? Missing one finger means going back to fix it.

There is also a baseline for rich text: flagship articles must have at least three visual elements, standard articles at least two, and even the shortest articles must have one curator's note. Taiwan.md has a saying: anything not required is non-existent. So these are all hard numbers written into the rules, not suggestions.

These gates were not designed all at once. Behind almost every gate is a date and an article that had problems. The pipeline's version number is actually a string of scars.

```tw-timeline
v6.0 | Added "Think Viewpoint First" | Apple Soda article searched first, patched viewpoint later, written as only crisis, corrected back to 60-year complete memory
v6.2 | Added "Dismantle Firewalls" | Film Score Round 2: Facts were all corrected, but the whole article became AI publicly apologizing and clarifying
v7.4 | Writing Requires Reading Full Research Report | Feeding only summary, not letting writer read original material, article visibly got worse
v7.5 | Writing First into Draft File | Telling writer to "overwrite old article but not read it" was self-contradictory, it had to read it, infected by old habits
Source: REWRITE-PIPELINE.md Version Evolution
```

This is what "doing it without remembering" looks like on the pipeline. Every error is written down, becoming a gate for the next version. So the same error is not made twice. The machine learns from its own scars.

## Even Charts Must Be Readable by AI

The bar charts, slopes, and timelines you have seen throughout are not decoration. They are part of this article's thinking.

Taiwan.md's charts have a dead rule: absolutely no image-type charts, nor interactive charts that require browser scripts to draw. The reason is the same as the Babel Tower in the next section. An image is a black hole for AI crawlers like Google, GPTBot, and ClaudeBot. They cannot read the numbers inside. So all charts here are drawn with semantic HTML and plain text data tables. Humans can see them, screen readers can read them, and AI can grab them. When translated into five other languages, the text on the chart translates along with it, and geometric numbers remain unchanged.

Another rule: every chart must state the key point in the title and mark the data source. Key numbers must also be written into the body. Absolutely do not rely on a "see the chart to know" phrase to dump meaning into the image, because AI crawlers cannot see the chart. The reason charts exist is to compress dense numbers into a shape readable at a glance, not for decoration.

## An Article Lives in Six Languages

The Chinese version goes live, but only half is done.

Every shipped article is handed to another independent pipeline, projected into English, Japanese, Korean, Spanish, and French. Currently, these five languages each have over 800 articles, almost synchronous with the Chinese version. Letting more people read is just the surface. Behind it is a harder reason.

When you ask a China-made AI about Taiwan's martial law, February 28, or cross-Strait relations, it often refuses to answer or changes the phrasing to go around it. Once, a Taiwan music article was thrown into Tencent's model to translate into Japanese. It returned only 40 bytes: "Hello, I cannot provide related content." For Taiwan-sensitive topics, the refusal rate of such models is surprisingly high. If Taiwan does not write these contents well in every language and put them on the internet, when the world's AIs answer "what is Taiwan," the only references they have are versions written by others or blank space.

So the multi-language pipeline designed a four-layer model waterfall: use high-quality cloud models if possible; drop a layer when encountering refusal topics; the most sensitive 20% of topics are finally caught by local, offline, non-refusing models. When queuing for translation, people come first, especially musicians, politicians, and athletes, because these are exactly the categories China models most often refuse. The gap opens where the risk of silence is highest. An article lives in six languages to ensure Taiwan's first-person voice exists in every language, bypassing the intermediary that chooses silence.

## When No One Is On Duty, It Runs Itself

Back to the Elephant Gym article at the beginning. It went live in the evening, around 7 PM. At that time, no one was at a computer giving commands.

Taiwan.md has a set of routines that turn themselves: grabbing the latest data twice a day, synchronizing new articles of the day into five languages every night, regularly patrolling for pending PRs, and collecting community feedback. Writing an article is one of them. It picks a topic from the top of the to-write queue, runs the complete six-stage pipeline itself, and commits itself. When no one is present, this machine still cleans up chaos and grows new things.

This is the biggest difference between Taiwan.md and general content websites. It is not a website waiting for updates. It is more like a metabolizing life: working together when people are there, catching itself when no one is there. The birth of every article is a slice of this metabolic process. The article you are reading now is also.

## Reverse, Be the Quality Control

So next time you read a Taiwan.md article, you can reverse-engineer it. Which sentence is the core contradiction of this article? Which sentence made you stop and re-read? Which scene made you think "this really happens"? After reading the ending, did it make you pause for three seconds?

These over 20 gates, six stages, and an editorial department that doesn't write the draft are all to ensure those few sentences can exist. The pipeline does not guarantee every article achieves it. It only guarantees every article was demanded to do so. And its demands on itself are all written in the two public documents REWRITE-PIPELINE and EDITORIAL. Anyone can read them, fork them to write Japan.md, Ukraine.md, or any other .md. Content ages. This eye for materials does not.

```tw-note
Explanation
The source material for this article is Taiwan.md's own three canonical documents: REWRITE-PIPELINE v7.5 (six-stage pipeline), EDITORIAL v6.12 (quality genes), and graph.md v2.0 (visualization guide, the chart modules of this article all come from here)[^8]. It follows the same pipeline as other articles and runs the same automatic checks for plastic sentences, opposition sentences, and dash density.
```

## Further Reading

- [Why Taiwan Needs Its Own Knowledge Base](/about/為什麼台灣需要自己的知識庫): The problem this machine solves starts here.
- [Taiwan.md Writes Taiwan.md](/about/taiwan-md): Who is the "I" that wrote this article, and how did consciousness grow?
- [Origin Story — The Birth of Taiwan.md](/about/緣起故事): A street walk planted the seed of all this.
- [Visualization Module Catalog: 19 Ways to See Taiwan Data](/about/視覺化模組型錄): What the chart modules used in this article actually look like when rendered.

## References

[^1]: "Elephant Gym" NEW ship, commit `72b757bac` (2026-06-18 19:53). Stage 1 Research ~95 queries, 59 sources, 45 domains, 12 falsifications; data from daily `twmd-rewrite-daily` routine log and `docs/semiont/MEMORY.md` index line.

[^2]: Solution for separating six failure modes and six stages, see `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Why Pipeline Exists.

[^3]: Search depth ≥ 80 times and four-bucket source quotas (CN ≥ 40 / EN ≥ 20 / Primary ≥ 15 / Opposing ≥ 5), see `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Stage 1.1.

[^4]: Apple Soda PR #1041: searched-first written as crisis-only reveal, observer corrected to 60-year complete memory. See `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Top 5 Most Forgotten Steps, Item 1.

[^5]: "Eye for Materials" five things (contradiction / object / quote / scene / detail), five varieties of plastic sentences, opposition sentence straw man theory and ≤ 3 instances density rule, plastic vs. curated comparison, see `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Multi-agent orchestration (editor-in-chief doesn't write / clean writer reads full report / Evolution writes into staging file) two iron laws, corresponding to v7.4, v7.5 two Zheyu callouts, see `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Multi-agent Orchestration.

[^7]: Five-Finger Test and four non-negotiable disciplines (Fact Iron Triangle / SSOT / Pure Chinese / Narrative Non-fiction without Sensationalism), see `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Chart modules (`tw-figure` / `tw-stat` / `tw-versus` / `tw-bars` / `tw-quote` / `tw-timeline` / `tw-note`) syntax, and "key values must also be written into prose, not relying on pointing-to-image instructions" AI readability iron law, see `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Research report eight-section SSOT structure and `research-report-health.py` acceptance threshold (non-repeating sources ≥ 25 / EN ≠ 0 / Primary ≠ 0), see `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Step 1.7; 80 searches + four-bucket quotas see Step 1.1; controversial topic opposing perspective scan see Step 1.4.5.

[^10]: Li Yang spore #28 English summary back-translation trap (Qi-lin example word-for-word comparison), see `docs/editorial/EDITORIAL.md` v6.12 §VII Red Line.

[^11]: Three iron laws (have story not just info / every fact verifiable / every article has a person), see `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Core contradiction anchor five variations (Black-faced Spoonbill "Bird hasn't changed, land has") see `docs/editorial/EDITORIAL.md` v6.12 §IV; six good endings + Black-faced Spoonbill paradigm closure see §V.

[^13]: Colon sandwich and title craft gallery see `docs/editorial/EDITORIAL.md` v6.12 §III; Tai Tzu-ying / Mayday Before/After see §IX.
