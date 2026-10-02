---
title: "Taiwan's Tech Storytelling: 100-Point Chips, 60-Point Microphones"
description: 'Taiwan makes 100-point chips but tends to describe them in the voice of a supplier briefing. For the same chip, Qualcomm tells a myth and MediaTek reads out a spec sheet; NVIDIA makes none of its chips with its own hands, yet its net profit is double that of its foundry. The market worked out this 40-point gap long ago, and the bill is printed right in the net margin.'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'Technology',
    'Storytelling',
    'Branding',
    'Semiconductors',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'Smile Curve',
    'Subtext',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-15
lastHumanReview: false
difficulty: 'beginner'
readingTime: 16
image: '/article-images/technology/tsmc-fab-14b-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg'
rationale:
  why_this_hook: '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。'
  whats_excluded: '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。'
  where_it_hedges: '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。'
  whos_pushing_back: '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '18585807b'
sourceContentHash: 'sha256:056a94a81916a22b'
sourceBodyHash: 'sha256:805b10284be61867'
translatedAt: '2026-10-03T01:02:12+08:00'
---

# Taiwan's Tech Storytelling: 100-Point Chips, 60-Point Microphones

![Exterior of TSMC's Fab 14B at the Southern Taiwan Science Park in Tainan, multi-story industrial buildings stretching under a blue sky, the physical site of advanced-process capacity](/article-images/technology/tsmc-fab-14b-2025.webp)
_TSMC Tainan Fab 14B, May 2025. Photo: 4300streetcar. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **30-second overview:** In June 2024, Jensen Huang (黃仁勳) stood in National Taiwan University Sports Center and talked the chips TSMC makes into an era. In the same quarter, TSMC's investor-conference slides were still financial figures, capacity utilization and a cautious outlook. NVIDIA's FY2026 revenue was US$215.9 billion and its net income US$120.1 billion; TSMC, which makes its chips, had 2025 revenue of US$122.4 billion and net income of US$55.1 billion[^5][^6]. The company that designs the story earns double what the company that does the making earns. What this article does is translate the subtext behind the lines.

On June 2, 2024, at the National Taiwan University Sports Center, Jensen Huang walked on stage in that black leather jacket and spoke for two hours. The scene in the crowd looked like a concert: livestreams, foreign press, a sea of raised phones. He talked about Blackwell and CUDA, turning slide after slide into the opening ceremony of an era[^19].

On the same island, under a hundred kilometers down the road to the south, sits Hsinchu. TSMC's investor conference is a different kind of picture: financial figures, capacity utilization, quarter-over-quarter and year-over-year changes, a conservative guidance range. The world's most advanced chips come off that production line, yet the whole briefing sounds like an accounting class.

The same chip, told two ways. The market worked out the 40-point gap between them long ago.

Taiwanese people have watched the difference between these two scenes all their lives. We are used to it: the product is ours, and the applause belongs to someone else. At trade shows, Taiwanese vendors' booths talk about cost, yield and delivery time, while American brands' stages talk about the future, mission and changing the world. The gap in between is those forty points. This article translates what those forty points look like.

## The Same Chip, Told Two Ways

In October 2024, two launch events fell less than two weeks apart. MediaTek unveiled the Dimensity 9400 in Shenzhen, and Qualcomm held its Snapdragon Summit in Maui, Hawaii[^9][^10].

[MediaTek](/en/economy/mediatek/) is one of the world's largest mobile chip suppliers by shipments, and holds a 70% share of TV chips[^4b]. Qualcomm ships fewer chips than it but beats it on revenue and brand premium. Where is the difference? Qualcomm sells the name "Snapdragon": named in 2006, it has been cultivated for almost twenty years[^8], with its own mascot and its own annual tech festival. At flagship phone launches around the world, the line "Powered by Snapdragon" is more eye-catching than the phone maker's own logo.

MediaTek sells a spec sheet. The Dimensity 9400 launch covered process node, IPC and efficiency curves, and every number held up; the benchmark community crowned it the "efficiency king"[^9]. But consumers only know Snapdragon.

MediaTek actually sat on the shipment throne long ago. In the third quarter of 2020, MediaTek's mobile chip shipments surpassed Qualcomm's for the first time, at a share of about 31%[^7]. But in those years of shipment leadership, most of MediaTek's revenue came from low- and mid-range phones, and the top tier of flagships stayed Qualcomm's. Only when the Dimensity 9000 arrived at the end of 2021 did MediaTek for the first time put a flagship chip into the comparison tables of the Android flagship makers. The specs had caught up, but the launch event still felt like a supplier briefing its customers.

MediaTek does know about this problem. In recent years it has started to learn: its flagship chips now have their own name, its launches have an opening show, and its partner phone makers are willing to put "Dimensity" into their ad copy. The direction is right; it just started more than ten years late. Brand building is a long-distance race, and whoever started running early compounds on every lap.

> 💡 **Did You Know**
> Snapdragon is the English name of the snapdragon flower (a kind of flower); Dimensity's Chinese name, Tianji (天璣), is the third star of the Big Dipper[^8]. One company named itself after something from a garden, the other after something from a star chart, and both are lovely. The difference: Qualcomm cultivated that flower into a brand that walks red carpets, while most of the time Dimensity's starlight still sits on the spec sheet.

> 📝 **Curator's Note**
> The brand war in chips is brutally concrete: when consumers pay, what they recognize is Snapdragon or Dimensity, and nobody asks which one TSMC fabricated. Qualcomm started building its brand in 2006, while MediaTek only hung the "Dimensity" series on its flagships at the end of 2019. Twenty years of compounded narrative is something no spec sheet can catch up with.

## How "Quietly Brilliant" Died

Go back further for a more painful case. On April 7, 2011, HTC's market capitalization surpassed Nokia's, at about US$33.8 billion[^1]. At the time HTC held roughly a fifth of the phone market, ranking with Samsung and Apple as one of the three giants[^2].

On technology choices, HTC got almost everything right: in 2008 it built the first Android phone, the G1[^3]. The 2013 One used a unibody aluminum body, and the big-pixel camera route and the dual lens were both paths it walked first. But do you remember its global brand slogan?

![Close-up of the side of an HTC One M7, with a unibody aluminum design that set the industry's craftsmanship benchmark when it launched in 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Photo: Asmoth, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant."

In the same period, Samsung's ad "The Next Big Thing is already here" directly showed Apple fans lining up at a store entrance, making the people in line look like fools[^18]. HTC made modesty its brand proposition; Samsung cast Apple as the villain. A little over two years later, HTC's share price had crashed from over NT$1,000 to around NT$100[^2].

HTC actually had one chance to turn things around. The 2013 One (M7) led the industry in many ways: the unibody aluminum body, the UltraPixel big-pixel camera, the BoomSound front stereo speakers. That year it won "phone of the year" from every major outlet, yet its sales lost badly to the Samsung S4 of the same period. The M7 launch talked about specs, Samsung talked about lifestyle, and Apple talked about fingerprint unlock as if it were changing the world. Phones of the same generation, three ways of telling it, three fates.

Looking back at HTC's defeat, of course it was more than one slogan. But the loss of the narrative was the first domino to fall: once the market began choosing sides by story, the side that could not tell one was the first put into the basket marked "about to be obsolete." Engineers do not believe this; they feel the product speaks for itself. The product does speak, but most consumers cannot understand it and do not want to listen.

![The HTC Dream with its slide-out keyboard open, the T-Mobile G1 of 2008, the world's first Android phone](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Photo: Marcus Sümnick, CC BY 3.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Curator's Note**
> "Quietly Brilliant" is itself a piece of subtext translation: a company that picks "low-key" as its global brand proposition is handing over its narrative sovereignty of its own accord. Spec sheets get forgotten; stories get remembered. HTC got every technology choice right and every narrative choice wrong.

## The Smile Curve: Taiwan Drew Its Own Predicament 30 Years Ago

HTC's tragedy is not an isolated case, and there is a diagram to prove it.

In 1992, Stan Shih (施振榮) drew the "smile curve" in his book _Re-creating Acer_ (《再造宏碁》): R&D and branding sit at the two ends, where value is highest, and manufacturing sits in the middle, where value is lowest[^4]. Taiwanese people drew this picture themselves, and for the next thirty years the main body of Taiwan's tech industry was stuck at the lowest point of the curve: Foxconn assembles iPhones for Apple at gross margins that have stayed in the single digits for years. Apple takes the vast majority of the profit of the whole phone industry; the peak market-research estimate exceeds eighty percent[^11].

[TSMC](/en/economy/tsmc/) is the exception. With the commandment of "never design its own products," it turned contract manufacturing itself into a business that holds both ends: customers cannot do without it, and it does not need to compete with those customers for consumers' adoration. But this business is built on B2B trust and does not need to tell stories to the general public. TSMC's low profile is a business strategy, and the side effect is this: the place in Taiwan that is best at making chips is exactly the place that least needs to practice telling stories.

It is not that nobody has made it to the right end. In 2006 ASUS founded the sub-brand ROG (Republic of Gamers), cultivating esports players into a community that recognizes a logo, and its "Eye of Ruin" emblem is one of the most recognizable marks in global gaming hardware[^15]. But ROG is a minority: most Taiwanese companies do not even dare to enlarge their logos on the front of their products.

Taiwan has in fact stood at the right end of the curve too. Acer was once one of the world's top three PC brands, and the four letters A-c-e-r were once posted at boarding gates in airports all over the world. But PC profits are too thin, so thin that brand premium could not bear the weight of the right end. ROG proves the right end can be stood on; you just have to pick the right battlefield.

The cruelest thing about the smile curve is that it is a multiple-choice question nobody has retaken in thirty years. Thirty years ago Taiwan chose to stand in the middle because that was the most reasonable answer at the time: no capital, no brands, no market, and contract manufacturing was the only way to survive. What is truly dangerous is continuing to treat the reasonable answer of thirty years ago as today's answer.

## The Economics of Boasting

Numbers are the most honest. NVIDIA's fiscal 2026 (February 2025 to January 2026) revenue was US$215.9 billion and net income US$120.1 billion[^5]. TSMC's full-year 2025 revenue was US$122.4 billion and net income US$55.1 billion[^6]. NVIDIA hands almost all of its chips to TSMC to make; what it sells itself is the CUDA ecosystem and the story of "the AI era." The result: the company that designs the story has 1.8 times the revenue of the company that does the making, and 2.2 times the net income.

Going up the same supply chain to the consumer end, the gradient gets steeper:

| Position in the supply chain | 2025 revenue     | Net income       | Net margin |
| ---------------------------- | ---------------- | ---------------- | ---------- |
| Foxconn (assembling iPhones) | NT$8.1 trillion  | NT$189.4 billion | 2.3%       |
| Apple (selling iPhones)      | US$416.2 billion | US$112.0 billion | 26.9%      |
| TSMC (making chips)          | US$122.4 billion | US$55.1 billion  | 45.0%      |
| NVIDIA (telling the story)   | US$215.9 billion | US$120.1 billion | 55.6%      |

_Data: Foxconn and Apple are fiscal 2025, NVIDIA is FY2026 (ending January 2026), and TSMC is calendar 2025, taken from each company's financial reports (cross-checked against the financial-report boxes on Wikipedia)[^5][^6][^11]._

Assemblers earn 2.3%, brand sellers earn 26.9%, those who make advanced-process chips with their own hands earn 45%, and those who tell the chip as an era earn 55.6%. Valuation is the discounting of future cash flows. Half of the future is built by engineering, and half is told into being. Silicon Valley's default culture is "fake it till you make it" (claim first, then find a way to deliver). Taiwan's default culture is "if it's not done yet, don't dare say it." The gap between the two cultures is not a moral gap but a discount-rate gap: the market discounts "a story you can tell" lightly and "a capability you cannot tell" heavily.

The mechanism of brand premium is also plain: take the same chip fabricated by TSMC, put the Snapdragon logo on it, and what the phone maker is willing to pay extra is the premium. Where does the premium come from? From the spectacle of the launch event, from the Summit held on schedule every year, from developers' habitual expectation that "the next Snapdragon will surely be faster." These things do not go into the spec sheet, but they do go into the financial report.

Some will say this is the market's fault, that Wall Street is hyping. But the same market gives TSMC no discount: TSMC's net margin of forty-five percent is a notch higher than Apple's. The market is in fact very willing to pay for Taiwan's capabilities; the condition is that the capability be told. TSMC's customers tell it for them: every Apple launch and every NVIDIA GTC is a free advertisement for TSMC.

Some ask whether blowing the story up risks turning it into fraud. Jensen Huang's answer is written in the financial reports: every sentence he says has capacity, yield and shipment volume behind it. The line between telling a story well and boasting is whether something catches it after it is told. Taiwan has the something; it just often forgets to tell.

> ⚠️ **Controversial View**
> One camp says Taiwan's 60-point narrative is a virtue: the lifeblood of the foundry business is trust, and a low profile is an asset; if TSMC held launch events all day, its customers would lose sleep. The other camp says the narrative discount transmits systematically: Taiwanese companies are undervalued, pay is undervalued along with them, talent flows to the companies that can tell stories, and the next generation of products becomes even less able to tell a story. Whichever camp you believe, you will end up living in that loop. Both claims are still alive today, and neither has won.

## Taiwan Is Not Bad at Storytelling

Taiwan does have people who tell stories well.

In 2021 Morris Chang (張忠謀) called TSMC the "sacred mountain protecting the nation" (護國神山)[^12]. Four characters made all of Taiwan willingly give way to the chip industry, giving up water and power. It was a top-tier piece of naming in marketing history: from then on, every news item about a water or power shortage automatically became a public-service ad saying "the sacred mountain needs you." At the end of 2024, Morris Chang, in his nineties, published the second volume of his autobiography, and it became a bestseller again[^13b].

That an autobiography became a bestseller is itself telling: an entrepreneur in his nineties wrote his life into two volumes and Taiwanese people lined up to buy them. Taiwanese love to listen to stories and love to buy stories; it is only when it is their own turn to take the stage that their words run short.

The résumés of these Taiwanese storytellers share one trait: Morris Chang spent twenty-five years at Texas Instruments, Jensen Huang started companies in Silicon Valley for thirty years, and Lisa Su (蘇姿丰) studied at MIT through her doctorate. Not one of them honed this skill in Taiwan. Taiwan's soil can grow such people, but Taiwan's workplaces do not teach it. Schools teach you to draw the circuit correctly, not to tell the circuit as an era.

So the problem has never been talent. The problem is that Taiwan's industrial structure sends the people who can tell stories abroad, or into the foundry's meeting rooms. Untying this knot cannot be done by a few companies' marketing departments alone; it has to be changed all the way from corporate governance and pay structures to school education.

![Morris Chang appearing as a leader representative in video footage of the 2021 APEC Economic Leaders' Meeting, an official Office of the President photo](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang at the 2021 APEC Economic Leaders' Meeting. Photo: Wang Yu Ching / Office of the President, CC BY 2.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Stan Shih drawing the smile curve was also selling a concept: one concept got his management philosophy cited by business schools around the world.

Jensen Huang was born in Tainan and went to the United States at age nine[^13]. Lisa Su was born in Tainan and went to the United States at age three[^14]. The two people in the world who tell the semiconductor story best are both Taiwanese seed in American soil.

![Jensen Huang speaking in Stanford University's CS 153 course, wearing his signature black leather jacket and gesturing with both hands](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang speaking in Stanford University's CS 153 course, April 2026. Photo: Anderseidesvik, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Taiwan's startups have storytellers too. Gogoro, founded in 2011, at CES in 2015 told its battery-swapping stations as an "energy network," calling itself an energy company that happens to sell scooters. The story was moving enough that in 2022 it listed on Nasdaq through a SPAC, and in 2024 even BP's Castrol invested US$50 million[^16]. Gogoro is still looking for a closed business loop, but its example shows that being able to tell a story at least gets you a ticket to be tested by the market. Those who cannot tell one do not even get through the door.

The pattern is clear: Taiwan does not lack storytelling talent; it lacks an environment that allows stories to be told big. The foundry gene teaches "the customer is the protagonist," while an environment for storytelling teaches "I can be the protagonist."

> 📝 **Curator's Note**
> The most intriguing thing about the four-character phrase "sacred mountain protecting the nation" is that when Morris Chang said them, he was telling Taiwanese society a story that needed support: electricity, water, land, talent. Telling stories is not vanity; it is the infrastructure of industrial policy. That Taiwanese people understood those four characters at once shows Taiwanese narrative power is not broken, just rarely used outward.

## A Subtext Translation Table

The same technical fact, said two ways. Translate the line behind the line, and the gap shows itself.

| Speaker                            | What is said on the surface                                                                                                | Subtext translation                                                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TSMC investor conference           | "Capacity utilization continues to recover, and we remain confident in long-term growth."                                  | Only I can make the world's most advanced chips, but saying so out loud would no longer sound like an engineer.                                                                      |
| Taiwanese engineer's presentation  | "There is still some room for optimization in this technology."                                                            | We are already number one in the world; we'll take 20% off first so nobody can slap us in the face.                                                                                  |
| American startup pitch, slide one  | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."                                 | The company currently has three engineers and one slide deck, but dreams are priceless, so please send money first.                                                                  |
| Taiwanese startup pitch, slide one | "Team members graduated from NTU, Tsing Hua and NYCU, previously worked at MediaTek for eight years, and hold 12 patents." | We don't know how to tell a vision, so we're using degrees and résumés as body armor.                                                                                                |
| Jensen Huang                       | "The more you buy, the more you save."                                                                                     | This card is expensive, but if you don't buy it, electricity bills and queuing for compute will cost you more.                                                                       |
| Qualcomm Snapdragon Summit         | "The era of on-device AI begins now."                                                                                      | Benchmark scores can wait until the iPhone ships; for now, let you feel you are witnessing an era.                                                                                   |
| HTC 2010 ad                        | "Quietly Brilliant"                                                                                                        | We are very brilliant, but we're too embarrassed to say it loudly.                                                                                                                   |
| Samsung 2011 ad                    | "The Next Big Thing is already here."                                                                                      | The people lining up at the Apple Store look so silly; come buy from us.                                                                                                             |
| Elon Musk                          | "We will make life multiplanetary."                                                                                        | The rockets occasionally blow up right now, but the narrative has to take off first.                                                                                                 |
| Morris Chang 2021                  | "Semiconductors are Taiwan's sacred mountain protecting the nation."                                                       | Four characters made all of Taiwan give way to chips, giving up water and power. One line from a Taiwanese who can tell a story is worth a whole year of investor-conference slides. |

_The quoted lines in the TSMC, Taiwanese engineer, both startup, and Qualcomm rows are illustrative summaries of typical phrasing, not verbatim quotes; the Jensen Huang, HTC, Samsung, Musk and Morris Chang rows are actual public slogans or statements[^17][^18][^12]._

After translating, you will find that the difference between telling a story well and badly is often just two word orders of the same fact.

This table is not meant to mock anyone. Modesty is very useful in engineering: it keeps collaboration going and keeps quality control from cutting corners. But once modesty steps out of the meeting room, it turns into a discount coupon. What Taiwan needs to learn is to keep the modesty in the lab and bring the confidence onto the stage.

## Back to the NTU Sports Center

Every slide Jensen Huang presented that night had its physical site in the cleanrooms of Hsinchu, Taichung and Tainan. After the story was told, the whole world paid the bill. The people in the cleanrooms kept working their shifts, and the investor conferences stayed cautious.

100-point technology does not automatically become a 100-point narrative. Those 40 points need someone to step onto the stage, wear the leather jacket as battle armor, and tell the chip as an era.

Taiwan's next sacred mountain may not be some new chip but some new story.

> ✦ Qualcomm cultivated a single SoC into a brand that walks red carpets, Jensen Huang told the chips TSMC makes as an era, and Morris Chang used four characters to make all of Taiwan give way for semiconductors. Taiwan's technology has 100-point things; what it lacks are people willing to step onto the stage and tell it as a 100-point story.

---

**Further reading**:

- [半導體產業：從 RCA 技轉到氮化鎵與量子封裝的 50 年材料革命](/en/technology/taiwan-semiconductor-industry) — The full technology narrative of the sacred mountain, and the tie of "NVIDIA booking CoWoS capacity"
- [台灣企業：台積電](/en/economy/tsmc) — The governance and financial structure of the company that wrote a low profile into its business model
- [台灣企業：聯發科技](/en/economy/mediatek) — The world's largest mobile chipmaker by shipments, and why its narrative is still catching up
- [台灣企業：宏達電](/en/economy/htc-android-pioneer-vr-transformation) — The full corporate history behind the death of Quietly Brilliant
- [黃仁勳](/en/people/jensen-huang) — Born in Tainan, raised in the United States, the world's best teller of chip stories
- [NVIDIA在台灣](/en/technology/nvidia-in-taiwan) — How that leather jacket relates to Taiwan's supply chain
- [Computex：三大國際電腦展收了兩個，剩下的那個長在台北](/en/technology/computex) — Every May, the world's AI giants take turns telling stories in Taipei with the same script

## Image Sources

This article uses 5 CC-licensed images, cached in `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Photo: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Photo: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Photo: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Photo: Wang Yu Ching / Office of the President, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Photo: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## References

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — On April 7, 2011, HTC's market capitalization of about US$33.8 billion surpassed Nokia's

[^2]: [維基百科 — 宏達國際電子](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — In 2011, phone market share of about 20%, market capitalization topping NT$1 trillion, share price once above NT$1,000

[^3]: [維基百科 — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — The world's first Android phone, 2008

[^4]: [維基百科 — 微笑曲線](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Proposed by Stan Shih in 1992 in _Re-creating Acer_

[^4b]: [維基百科 — 聯發科技](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — One of the world's largest mobile SoC suppliers by shipments; roughly 70% share of TV chips

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — NVIDIA's official press release; FY2026 revenue US$215.9 billion, net income US$120.1 billion (cross-checked against Wikipedia's financial-report box: https://en.wikipedia.org/wiki/Nvidia)

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — TSMC's official investor page; full-year 2025 revenue US$122.42 billion, net income US$55.13 billion (cross-checked against Wikipedia's financial-report box: https://en.wikipedia.org/wiki/TSMC)

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — In the third quarter of 2020, MediaTek's mobile chip shipments surpassed Qualcomm's for the first time, at a share of about 31%

[^8]: [維基百科 — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — The Snapdragon SoC platform was announced in November 2006; the brand name comes from the snapdragon flower, and Dimensity is taken from the third star of the Big Dipper (both naming accounts come from public brand information; an official source link is still to be added)

[^9]: [MediaTek — Dimensity 9400 press release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — The Dimensity 9400 was announced in October 2024; the benchmark community generally credits it with strong efficiency (a summarizing description). For the first phone to ship with it, see [維基百科 — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200)

[^10]: [維基百科 — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 was held in Maui, Hawaii, announcing the Snapdragon 8 Elite (the official press-release URL is dead; the secondhand Wikipedia entry is used instead)

[^11]: [維基百科 — Foxconn](https://en.wikipedia.org/wiki/Foxconn) ／ [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Foxconn fiscal 2025 revenue NT$8.103 trillion, net income NT$189.35 billion (net margin about 2.3%); Apple FY2025 revenue US$416.2 billion, net income US$112.0 billion (net margin about 26.9%). Apple phones' share of industry profit exceeded eighty percent at its peak: Counterpoint's estimates over the years (source link to be added)

[^12]: [維基百科 — 護國神山](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Another name for TSMC (the "silicon shield"); "Semiconductors are Taiwan's sacred mountain protecting the nation" is a public statement by Morris Chang in 2021 (news source link to be added)

[^13]: [維基百科 — 黃仁勳](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Born in Tainan in 1963; emigrated to the United States in 1972 (at age nine)

[^13b]: The second volume of Morris Chang's autobiography was published in November 2024, with sales at bestseller level for that year (source link to be added)

[^14]: [維基百科 — 蘇姿丰](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Born in Tainan in 1969; emigrated to the United States with her family at age three

[^15]: [維基百科 — 華碩](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Founded the sub-brand "Republic of Gamers" (ROG) in 2006

[^16]: [維基百科 — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Founded in 2011; unveiled the Gogoro Smartscooter and its energy network at CES in 2015; listed on Nasdaq in 2022 by merging with the Poema Global SPAC; in 2024 BP's Castrol announced an investment of up to US$50 million

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — Jensen Huang's "The more you buy, the more you save" comes from this official video

[^18]: "Quietly Brilliant" was HTC's global brand slogan from 2009, "The Next Big Thing is Already Here" was Samsung's 2011 Galaxy ad slogan, and "We will make life multiplanetary" is SpaceX's mission statement (all three are public commercial texts)

[^19]: [NVIDIA at Computex 2024 — 官方主題演講影片](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Jensen Huang's Computex keynote at the National Taiwan University Sports Center on June 2, 2024
