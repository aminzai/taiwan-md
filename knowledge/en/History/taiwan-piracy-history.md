---
title: 'Pirate Kingdom: Reverse-Engineering Counterfeit Years and the Trust Gene in TSMC'
description: 'From the 1970s to the 1990s, Taiwan was branded an international "pirate kingdom." This piece traces the rise and fall of counterfeiting, how the June 12 deadline and Special 301 provisions forced institutional reform, and why TSMC''s "never compete with customers" trust model is the reversal of that history.'
date: 2026-08-18
category: 'History'
tags:
  [
    'copyright',
    'counterfeits',
    'TSMC',
    'Special 301',
    'copyright law',
    'Morris Chang',
  ]
subcategory: '經濟發展史'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-18
lastHumanReview: true
researchReport: 'reports/research/2026-08/pirate-kingdom-tsmc-trust.md'
readingTime: 12
rationale: "{'why_this_hook': '「海盜王國」的國際汙名與台積電信任經濟形成強反差，影片引發的懷舊共鳴可轉化為制度史知識增量', 'whats_excluded': '排除未經正式新聞證實的坊間細節（麥當樂判決最終結果未下筆），排除中國大陸觀點來源', 'where_it_hedges': '「六成仿冒品出自台灣」為 1986 年美聯社轉述美國 ITC 單方估計，文中已標明來源', 'whos_pushing_back': '部分民眾對盜版年代帶有懷舊情感，可能質疑仿冒與台積電成功直接掛鉤的因果敘事'}"
curation: 'incubating'
translatedFrom: 'History/台灣盜版史.md'
sourceCommitSha: '373a07d35'
sourceContentHash: 'sha256:b8045765d1db3274'
sourceBodyHash: 'sha256:a195178fa37b285e'
translatedAt: '2026-09-15T06:51:23+08:00'
---

> **30-second overview:** From the 1970s to the 1990s, Taiwan was branded a "pirate kingdom" by Newsweek due to large-scale counterfeiting and piracy. The U.S. ITC estimated that up to 60% of global counterfeit goods came from Taiwan, and in 1989 it was listed on the U.S. Special 301 Priority Watch List[^4][^5]. This article outlines three turning points: the 1992 copyright law revision and the June 12 deadline ending the comic book war; the 1980s electronics industry shifting from counterfeiting Apple to IBM-compatible OEM manufacturing; and in 1987, TSMC redefining Taiwan manufacturing with a "never compete with customers" trust model. The pirate kingdom did not disappear—it was transformed by institutions and business models into a semiconductor kingdom[^9][^13].

# Pirate Kingdom: Reverse-Engineering Counterfeit Years and the Trust Gene in TSMC

In December 1984, Newsweek and Asia Magazine simultaneously gave Taiwan a title: "a pirate's haven."[^1] Three months earlier, Life Magazine had just published a cover story calling counterfeiting "Taiwan's emerging industry."[^1] After landing, foreign tourists rushed straight to Zhongshan North Road, spending about $25 on a counterfeit Rolex. Bookstore windows displayed pirated simplified Chinese editions of the Encyclopedia Britannica. In the alleyway fruit stalls, pirated comic books piled in plastic baskets for 10 yuan each, waiting for schoolchildren to pick through them.[^2] Around the same time, the "McDonald's" near Taipei Railway Station—with a sign resembling the Golden Arches—had already been open for six years, six years ahead of the real McDonald's entering Taiwan, and in its first trademark lawsuit, McDonald's actually lost the case, with the official reasoning of the trademark review determining the real trademark had "the potential to deceive the public or cause public misunderstanding."[^3] Counterfeiting in 1980s Taiwan was not just an underground economy—it was a legitimate public business: signs dared to go up earlier than the real ones, lawsuits dared to be filed earlier than the real ones. And at that time, almost no one thought anything was wrong, because the line between "counterfeit" and "imitation" was only drawn after the 301 provisions were pushed onto the negotiation table in the United States.

The reach of plagiarism also extended into the entertainment industry. At the end of the 1980s, the "Little Tigers" who became popular across China, Taiwan, and Hong Kong copied the group structure and performance style of the Japanese idol group "Teen Tigers." The "Golden Five Treasures" concept of the ratings champion "Golden Partners" was taken from the Japanese TBS program. The signature role "Big Sister" of the Yang Fan was modeled after the character of the Japanese comedy master Shimura Takeshi. These programs and groups were not officially authorized copies, but rather local producers who learned from the Japanese TV signals frame by frame. This was an era without authorization fees or factory supervision—the survival mode of the Taiwan entertainment industry.

> In March 1986, The New York Times quoted a Western diplomat: "Until a few years ago, Taiwan was the world's undisputed capital of counterfeiting and piracy."[^2]

📝 Curator's note: The global status of Taiwan's semiconductor industry and a whole era of notorious counterfeiting are connected not by a rupture, but by the same group of people.

![Huaxi Street Tourist Night Market archway and vendors: In the 1980s, the "Snake Market" was where foreign tourists purchased counterfeit watches and electronic goods (image provided by Wikimedia Commons author, CC0 public domain license)](https://upload.wikimedia.org/wikipedia/commons/e/e0/Huaxi_Street_Night_Market.jpg)

## Who Called Taiwan the Pirate Kingdom

"Pirate Kingdom" was not a metaphor, but a documented diplomatic record. The Office of the United States Trade Representative has published the "Special 301 Provisions" watchlist every year since 1989, and Taiwan was on the "Priority Watch List" in the first year, remaining on and off the list for nearly twenty years until it was officially removed in January 2009[^4]. To understand the weight of this title, we must return to the temporal coordinates: mid-1980s Taiwan, whose export volume had grown from the billion-dollar level in 1970 to $38.8 billion in 1986, making it one of the fastest-growing economies in the world at the time, with exports simultaneously including genuine goods and counterfeit goods—this is exactly what made Washington and business owners anxious[^11]. In the removal report, the U.S. described Taiwan as having transformed "from a haven for pirates into a holy land of innovation and R&D." The same document also recorded the birth and death of the Pirate Kingdom[^4].

The scene of mid-1980s Taiwan was even worse than the list. In March 1986, New York Times reporter John Burns visited the market in person: at the Huaxi Street Night Market (then called Snake Market), a counterfeit Rolex sold for only $10, while the same period Tiffany's genuine price for ethnic Chinese was $8,850. A pirated WordStar word processing software cost $5. The counterfeit Yale lock brand name "Yeal," with one extra letter, dared to go on the shelves.[^2] In September of the same year, the Associated Press reported more directly, citing the U.S. International Trade Commission (ITC) estimates: in the early 1980s, up to 60% of circulating counterfeit goods came from Taiwan.[^5] The Reagan administration's public statement at the time was that American industry lost $2 billion annually due to counterfeiting. In 1986, Business Weekly calculated even more harshly, claiming counterfeiting caused the loss of 750,000 jobs in the United States.[^6]

```tw-stat
# Key figures of Taiwan's Pirate Kingdom #
1989|Starting point|First included in the U.S. Special 301 Priority Watch List
2009|Removal|Officially removed from the U.S. Special 301 watchlist
60%|Counterfeit ratio|Estimated 60% of global counterfeit goods came from Taiwan in the early 1980s (ITC)
750,000|Lost jobs|Number of jobs lost in the U.S. due to counterfeiting in 1986, according to Business Weekly
Source: U.S. International Trade Commission (ITC) / Office of the U.S. Trade Representative / Business Weekly, 1986-2009
```

📝 Curator's note: An economy with tens of billions in exports, where 60% of global counterfeit goods came from its factories—this is not petty theft, but a national production line.

## Comics: From Censorship System to the June 12 Deadline

The proliferation of pirated comics surprisingly began with the government's own control. In the 1960s, the government implemented strict comic censorship, with local creators repeatedly failing to pass review, causing the local comic market to shrink. Pirated Japanese comics, however, bribed censors to obtain government-issued legitimate publication numbers, flooding the market at extremely low prices without paying royalties.[^7] In other words, during the heyday of pirated comics, the pirates held government-issued certification documents.[^7]

This structure of "legitimate piracy" shaped a unique upbringing for a generation of Taiwanese comic readers. Children in alleyway fruit stalls and bookstore clusters near schools could buy a Japanese comic for NT$10 or NT$20: no copyright page, inconsistent translation quality, and even the protagonist's name might change between different publishers, but the price was only one-tenth of genuine magazines. Comics were no longer a leisure activity for the middle class, but a daily necessity for the common people. The government used the censorship system to kill the livelihoods of local creators, while simultaneously endorsing pirates with publication numbers. The local comic industry was completely crushed under this double pressure.

On July 15, 1987, the lifting of martial law rendered the submission system invalid overnight, and pirated comics entered a warring states period. Publishers such as Dongli, Daren, and Jicheng simultaneously rushed to translate the same popular work, with "Dragon Ball" and "Slam Dunk" each being translated by different publishers, and readers buying the same comic might end up with four different translations.[^8] At the peak of the warring states period, the circulation of "Young Fast News" reached 230,000 copies per issue, a figure higher than the total circulation of many genuine magazines at the time.[^8]

On June 12, 1992, the revised Copyright Act took effect, allowing foreign-translated reproductions printed under the old law to continue selling during a two-year buffer period—meaning after June 12, 1994, all pirated translated comics had to be removed from shelves. Comic fans called this day the "June 12 Deadline," and the scene of bookstores clearing out before the deadline became a collective memory of that generation of Taiwanese people.[^9] In the last few months before the deadline, bookstores and comic rental shops throughout Taiwan piled their inventory to the door, marked "clearance sale," and many students used money that could originally only buy one book to carry back half a bag of pirated books— this was the funeral of pirated comics, and also the opening ceremony of the genuine era.

The transformation after the deadline was not completed overnight. Genuine licensed comics were priced several times higher than pirated ones, and publishers had to learn the editing process, translator specifications, and copyright distribution from the original Japanese factories. The original pirates turned into copyright managers and editors. On the reader side, they were also adapting: from "available at any store" to "only one publisher has the genuine version," purchasing genuine single volumes and supporting the publisher became the new daily routine of comic fans in the late 1990s. The deadline forced structural transformation: Dongli signed "Akira" with Kadokawa Shoten in January 1992, becoming the first officially contracted Taiwanese comic work, and pirates one by one transformed into genuine agents.[^8]

```tw-timeline
# Forty years of pirated comics: from legitimate piracy to genuine agency #
1960s|Censorship era|Local comics declined, pirated Japanese comics circulated at low prices with government publication numbers
1987|Lifting of martial arts|Submission system failed, multiple publishers rushed to translate the same work
1992.1|Genuine signing|Dongli signed "Akira" with Kadokawa Shoten, the first genuine agency
1992.6|Copyright Act revision|Revised Copyright Act took effect, foreign works first received protection
1994.6.12|June 12 deadline|Last sale day of pirated translated reproductions, the piracy era ended
2009|International removal|Removed from the U.S. Special 301 watchlist
Source: Republic of China Copyright Act Article 112 / Commercial Times, 1992-2009
```

![The Jicheng comic rental store in Shilin District, established in 1986, still in operation today—rental bookstores were the nerve endings of pirated comic circulation from the 1980s to the 1990s (image provided by Wikimedia Commons author, CC BY-SA 3.0 license)](https://upload.wikimedia.org/wikipedia/commons/f/f1/Ikkoku-kan_Comic_Bookshop_Shilin_Branch_20101209.jpg)

## Electronics Industry: Reverse Engineering Started by Disassembling Apple

Taiwan's electronics industry also made its first fortune from disassembly. In 1981, Acer (then named Multitech) launched a $70 "Professor One" educational microcomputer, followed in the next year by a NT$7,950 "Professor Two," which was almost a complete copy of the Apple II.[^10] A 1984 report by The Christian Science Monitor wrote that in the computer shops along Zhongshan North Road in Taipei, a counterfeit Apple computer could be burned in two hours for $350, about half the original price.[^11] Around the same time, Tongtai Computer launched the "Little Tongtai," and Jicheng Electronics launched the unauthorized Nintendo-compatible game console "Little Genius," with counterfeits spreading from computers to gaming consoles.[^10]

![Ximending pedestrian area night market signs: The electronic malls and ready-made stalls around Ximending were the main distribution centers for counterfeits and pirated software during the Pirate Kingdom era (image provided by Wikimedia Commons author, CC BY 3.0 license)](https://upload.wikimedia.org/wikipedia/commons/2/23/Ximending_Main_Alley_at_Night.jpg)

In 1983, Apple Computer officially sued Taiwanese manufacturers for infringement. Acer's Professor Two was seized by U.S. customs, with Apple claiming its manual was translated from Apple II documents, and ultimately Acer was required to pay $20 in compensation for each machine.[^10] These lawsuits led to two outcomes. First, Taiwanese manufacturers honed their reverse engineering skills—disassembly, replication, and rapid modification—and shifted toward IBM's open architecture-compatible OEM/ODM manufacturing. IBM contacted 11 Taiwanese manufacturers in the early 1980s, with 7 signing agreements to stop producing counterfeits and publicly apologizing, then moving to licensed manufacturing.[^11] Second, due to frequent trademark disputes with the Multitech brand overseas, Stan Hwang reluctantly spent $2 million in 1987 to abandon the accumulated brand value and renamed it Acer.[^10]

The electronic community in the Hsinchu Science Park was grown up during this "from counterfeits to OEM" transition period. Engineers from the counterfeiting era learned to read circuits, modify designs, and rush deadlines. These skills instantly found legitimate export channels after IBM's open architecture, directly laying the foundation for Taiwan's later electronics manufacturing dominance.[^11]

It is worth mentioning that this transformation was not a moral awakening unique to Taiwan, but rather a result of IBM's open architecture bringing about changes in the industrial structure. After the hardware specifications of the IBM PC were made public, the compatible machine market no longer needed to crack the prototype, only to assemble and fine-tune faster and cheaper than the original factory—this is exactly the skill that Taiwanese manufacturers spent twenty years honing in the counterfeiting trenches. From "copying manuscripts" to "rushing OEM schedules," the skills are the same set of skills, the difference is only in the contract authorization terms. This skill spectrum extended all the way to notebook computer OEM, motherboard OEM, and finally found the highest-level export in the clean room of chip manufacturing. Taiwan's electronics manufacturing services (EMS) and ODM system became the world's first for the next thirty years, starting from the late 1990s, with over 70% of global notebook shipments designed or assembled by the Taiwan supply chain. The muscle memory of rapid molding, rapid modification, and rapid mass production honed during the counterfeiting years is the foundation of this 70% share.[^11]

![Taipei's Guanghua Digital Plaza and the old Guanghua Bridge electronic district: From the 1960s to the 1990s, the computer street around Guanghua Mall was the cradle of Taiwan's electronic components and assembly culture, and also the core scene of pirated computer circulation (image provided by Wikimedia Commons author, CC BY-SA 3.0 license)](https://upload.wikimedia.org/wikipedia/commons/f/fe/Guang_Hua_Digital_Plaza_and_Mitsubishi_Delica_4WD_20080203.jpg)

## Special 301 Provisions: Reform Season Under the U.S. Tariff Knife

The account of losses caused by counterfeiting in the United States ultimately became a diplomatic and trade weapon. The United States repeatedly threatened to impose trade retaliation against Taiwan in the 1980s. In 1984, the Taiwan government began to ban the export of counterfeit goods, established special task forces, revised the Trademark Law in 1983, and included computer software under the protection of the Copyright Act.[^11][^12] Enforcement was also under pressure: the number of criminal prosecutions increased from 344 cases in 1983 to 629 cases in 1985, and customs publicly crushing seized counterfeit computers became an annual news scene.[^2][^5] After Taiwan was first included in the Special 301 list in 1989, the government successively revised the Patent Law, Trademark Law, and Copyright Law, with enforcement power and statutory sentences increased in tandem.[^4][^12] The 1992 Copyright Act revision was the most devastating: it removed the statutory restrictions on translation rights, explicitly listed computer programs as works, and granted foreign works the first-time protection in Taiwan, directly ending the "legal" gray area of printing foreign books and software.[^9] After the revision, the Ministry of Economic Affairs also established an Intellectual Property Rights Coordination Meeting to coordinate enforcement, with each district prosecutor's office configuring special prosecutors, investigating from night market vendors all the way to printing factories and importers.

The shadow of Special 301 not only fell on legal provisions, but also on daily industries. After counterfeit exports were banned, the Huaxi Street Night Market and Ximending's counterfeit stalls lost their main source of income. The clothing industry was forced to withdraw from counterfeiting Adidas and Nike sewing lines and turn to legitimate OEM manufacturing— the same sewing machines, the same workers, only the labels sewn into the fabric changed from Abiba to international brand authorization marks. In 1984, the "Fairy Tale World Amusement Park" in Hsinchu Guangxi, which mimicked Disneyland, and the giant unauthorized Mickey Mouse landmark on Miaolun Mountain in Hualien, were all gradually eliminated or modified after intellectual property regulations tightened, becoming an embarrassing record in the history of local tourism.[^12] The sign of the Pirate Kingdom was dismantled piece by piece by regulations.

The irony of this revision logic is: the Pirate Kingdom's exit was not a spontaneous moral awakening of Taiwanese society, but an institutional transplant under the knife of trade retaliation. The Taiwanese think tank "Observing Magazine" directly stated in a retrospective article that Taiwan was gradually establishing modern intellectual property rights systems in the process of responding to U.S. intellectual property requirements.[^12] Until 2009, this externally driven legal system took twenty years to complete.[^4]

```tw-versus
# Mid-1980s: Dual legal standards of the Pirate Kingdom #
Genuine Tiffany watch|8,850 USD|Price cited by The New York Times in 1986 in Taipei
Counterfeit Rolex|10 USD|Same period Huaxi Street Night Market price
Genuine software and computers|Market price|Two hours to counterfeit in Zhongshan North Road computer shop
Pirated WordStar software|5 USD|Hundreds of times cheaper than genuine price
Source: The New York Times / Los Angeles Times, 1986
```

## The Reversal of Trust: Why TSMC Must Be the Opposite of Counterfeits

In 1987, five years before the Copyright Act revision and in the same year as the lifting of martial law, Morris Chang founded TSMC. TSMC's business model was an intentionally designed counter-proposition: only wafer foundry, no product brands, absolutely never competing with customers. TSMC's official position to this day states, "We have always positioned our customers as partners and never compete with them," and lists "integrity and honesty" as the most basic and important core values.[^13] The current chairman, Wayne Chiang, summed it up even more directly: "The first step to gaining customer trust is not competing with customers."[^14]

This model was established because wafer foundry orders are essentially trust-based transactions. Design companies hand over circuit diagrams that have not yet been taped out and will be ruined once leaked to a foundry for production. If the foundry has a counterfeiting background, or might jump out and make products themselves, no one will place orders. In a country that had just been called "a pirate's haven" by Newsweek, Chang was building a business model that required national-level reputation backing—TSMC's trust was a direct negation of the Pirate Kingdom image.[^1]

Putting the timeline back to 1987, this choice was much more risky than it seems in hindsight. At the time, the mainstream of the international semiconductor industry was the integrated device manufacturer (IDM) model of Intel and Texas Instruments—self-designed, self-produced, and self-sold products. No one believed that a company that only produced without designing could survive. Intel once refused to invest in TSMC, and partners in Europe and Japan successively withdrew, with Chang guaranteeing this never-before-verified business model with his personal reputation under almost no alliances.[^15] The technical premise for the foundry model to stand was that the capital threshold of wafer manufacturing was high enough that design companies could not build their own factories—but the business premise was only one word: trust.

The dividends of trust have been compounding year by year for the past thirty years. Because it never competes with customers, TSMC simultaneously became the foundry for Intel, Qualcomm, NVIDIA, and Apple—companies that compete with each other, all laying their most confidential process requirements on Chang's clean room. If TSMC made its own products, the entire customer network would collapse within a quarter. TSMC turned "trust" into a moat, so even if competitors catch up in technology, they cannot steal customers, because the risk of customers moving factories is not just cost, but the possibility of confidential information leakage.[^14][^15] In a 2021 interview with Xu Jinhong, Chang's answer to the most important element of TSMC's success was only one word: "trust."[^15] In his handwritten company development strategy assessment in 1998, among more than ten options, the only "not to do" was the low-price strategy—because low prices would attract customers who are solely price-driven, eroding trust.[^15]

```tw-figure
# trust #
The most important single element of TSMC's success
—Morris Chang, 2021 interview with Xu Jinhong
Source: Newtalk News, 2021
```

![TSMC Factory 6 exterior: In 1987, Morris Chang founded TSMC, whose pure wafer foundry model was built on "never competing with customers," completely breaking away from the Pirate Kingdom image (image provided by Wikimedia Commons author, CC BY 4.0 license)](https://upload.wikimedia.org/wikipedia/commons/3/3a/TSMC_Fab_6_front_May_2025.jpg)

![Intel Pentium processor on a wafer: TSMC's trust model brought the most confidential chip designs of customers into the clean room, with every chip on the same piece of silicon being a physical witness of the trust transaction (image provided by Wikimedia Commons author, CC BY 2.0 license)](https://upload.wikimedia.org/wikipedia/commons/6/65/Wafer_with_Pentium_chips.jpg)

📝 Curator's note: McDonald's vs. McDonald's, Little Professor vs. Apple II, Snake Market vs. TSMC—on the same island over forty years, "copying" was trained into "trust."

## Aftermath: What the Pirate Kingdom Left Behind for Today

In 2009, the U.S. Trade Representative's removal report defined Taiwan as "a holy land of innovation and R&D."[^4] Looking back, the legacy left by the Pirate Kingdom era is two-sided. On the positive side is the engineering capability honed by reverse engineering—disassembly, replication, modification, and rushing deadlines. This set of skills found legitimate export channels in the era of IBM's open architecture and wafer foundry, nurturing the complete industrial chain from OEM to semiconductors.[^10][^11] The data today best illustrates the scale of this reversal: TSMC alone accounts for more than half of the global wafer foundry revenue, and almost all of the advanced process market share, with its market value once accounting for nearly 30% of the total market value of the Taiwan stock market. Thirty years ago, the same island was scolded as a counterfeiting country, and today, chip design companies around the world compete to hand over their most confidential drawings to it.[^13][^14] On the negative side is the trust debt: trademark grabbing (the McDonald's lawsuit took years to settle), brand disputes (Multitech was forced to change its name), and international image, causing Taiwanese companies to pay several decades of reputation costs in overseas markets.[^3][^10]

It is worth noting that in this journey from counterfeits to trust, Taiwan is not alone. The United States was once called by Europe in the 19th century as the largest copyright infringement country, Germany in the early stages of industrialization mass-produced British machinery and was required by British law to label "Made in Germany" to distinguish, and Japan after the war also experienced a period of intensive counterfeiting and imitation during its rapid economic development.[^6] The common script of each country is: counterfeiting is a shortcut to catch up, but only when the system closes the shortcut and opens up the path to turn real skills into value can the industry complete the upgrade. Taiwan's particularity is that the closing of the road and the opening of the road almost happened at the same time— the 1992 Copyright Act revision pushed pirates toward genuine versions, while TSMC, born in 1987, redefined the credit rating of "Made in Taiwan" with "trust." In the same year that one road was closed, another road was being laid in the clean room of Hsinchu.[^9][^13]

The Pirate Kingdom did not disappear—it was transformed by institutions and business models into a semiconductor kingdom. And every time someone today criticizes a certain country as a new counterfeiting country, history's response is often the same sentence: they are just still in the years of the Pirate Kingdom.

**Extended reading:** If interested in the literary context of the June 12 deadline, you can read Zhang Zhongxin's "Commentary on the Copyright Act" for a detailed analysis of Article 112, as well as Li Lingyi's 2015 doctoral dissertation "Research on the Taiwanese Comic Industry" from National Taiwan University.[^9]

## References

[^1]: [Taiwan Tries to Get Its Computer Pirates Off High-Tech Seas](https://www.csmonitor.com/1984/1206/120632.html) — Christian Science Monitor, December 6, 1984, reporting on the reality of Taiwan's counterfeit Apple computers and government crackdown

[^2]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — The New York Times, March 30, 1986, reporting on the Snake Market counterfeit Rolex prices, the Yeal counterfeit lock, and the number of prosecutions

[^3]: [Taiwan Industry Association News: Trademark Litigation Historical Data](https://www.taie.com.tw/data/magazine/1730856057OGWXL.pdf) — Taiwan Trademark Association Newsletter published the McDonald's vs. McDonald's trademark litigation, in which McDonald's lost the first instance

[^4]: [Is Taiwan a Pirate Kingdom?](https://www.chinatimes.com/newspapers/20131229000166-260209) — The China Times, by Guo Qinchun column, compiling the Special 301 list entry and exit records and the U.S. removal evaluation in 2009

[^5]: ['Knockoff' King Taiwan Tries to Mend Its Ways](https://www.latimes.com/archives/la-xpm-1986-09-02-fi-13692-story.html) — Los Angeles Times, September 2, 1986, Associated Press report, citing the ITC's 60% counterfeit ratio and Lee Daoxuan's remarks

[^6]: [From the Counterfeiting Capital of the World](https://scholarship.law.vanderbilt.edu/cgi/viewcontent.cgi?article=1488&context=vjtl) — Vanderbilt Law Review academic discussion, reviewing Taiwan's counterfeiting industry and U.S. intellectual property pressure

[^7]: [Taiwan and Hong Kong Piracy Period](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Wikipedia summary of the background and publication number issues of Taiwan and Hong Kong's pirated Japanese comics from the 1960s to the 1990s

[^8]: [Young Fast News and Piracy Warring States](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Wikipedia records the post-martial law rush to translate, the 230,000 circulation of Young Fast News, and Dongli's signing of "Akira"

[^9]: [June 12 Deadline](https://zh.wikipedia.org/zh-hant/%E5%85%AD%E4%B8%80%E4%BA%8C%E5%A4%A7%E9%99%90) — Wikipedia details the 1992 Copyright Act revision, Article 112 buffer period, and the specifics of June 12, 1994

[^10]: [Collection of Technology: The Ancestor of Taiwanese Computers](https://scitechvista.nat.gov.tw/Article/c000008/detail?ID=e5ccc61e-3d6d-44a8-97ca-6bb19a390f51) — National Science and Technology Museum, "Scientific Development" No. 474, recording the Little Professor series and Apple litigation compensation

[^11]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — The New York Times also records the 1984 customs seizure, IBM signing and apology, and the timeline of revisions (supplementary 301 retaliation background see [^4])

[^12]: [From Pirate Kingdom to Scam Paradise](http://old.observer-taipei.com/www.observer-taipei.com/article7f6f.html?id=1105) — "Observing Magazine" NO.33 reviews the forced establishment of Taiwan's intellectual property legal system under the Special 301 provisions

[^13]: [Corporate Core Values and Business Philosophy](https://www.tsmc.com/chinese/aboutTSMC/values) — TSMC official website, publishing the core value of integrity and honesty and the business philosophy of "never competing with customers"

[^14]: [Wayne Chiang: Not Competing with Customers Is the First Step of Trust](https://www.cna.com.tw/news/afe/202402290371.aspx) — Central News Agency, February 29, 2024, interviewing Wayne Chiang on TSMC's trust model

[^15]: [Xu Jinhong Asks Morris Chang: The Most Important Element of TSMC's Success](https://newtalk.tw/news/view/2021-11-02/660071) — Newtalk News, November 2, 2021, reporting Morris Chang's answer of "trust" and not doing low-price strategies
