---
title: 'Jay Chou'
description: '1997 hat ein schüchterner 18-jähriger Junge die Geschichte der chinesischsprachigen Popmusik neu geschrieben'
date: 2026-03-23
category: 'People'
tags: ['Personen', 'Jay Chou', 'Chinesischsprachige Popmusik', 'Sänger', 'Songwriting', 'R&B', 'China-Stil']
subcategory: '音樂與表演'
author: 'Taiwan.md'
featured: false
lastVerified: 2026-03-23
lastHumanReview: false
lifeTree:
  protagonist: '周杰倫'
  birthYear: 1979
  span: '1979–2024'
  source:
    article: 'knowledge/People/周杰倫.md'
    commit: '6409f519'
    commitDate: '2026-03-23'
    extractedBy: 'Taiwan.md (Semiont) β-r5'
    extractedAt: '2026-04-26 13:30 +0800'
    note: '原文 references = 維基 / Time / IFPI / 鏡週刊 / 華視 / Block Tempo / Dcard 等。Counterfactual 主要對照同代華語流行（孫燕姿、王力宏、陶喆、吳青峰）的路徑。'
  intro: '一個 1997 年在《超級新人王》上彈鋼琴的害羞 18 歲男孩，三年後改寫華語流行音樂歷史。從寫歌被退稿三年的助理到全球銷量冠軍。每個 turning（被退稿、自創公司、跨界導演、政治模糊）都有他沒走的路。'
  themes:
    - id: original-mainstream
      label: '原創 vs 主流公式'
      color: '#8B5CF6'
    - id: artist-boss
      label: '藝人 vs 老闆'
      color: '#EC4899'
    - id: cross-medium
      label: '單一媒介 vs 跨界'
      color: '#10B981'
    - id: cross-strait
      label: '兩岸表態 vs 模糊'
      color: '#F59E0B'
  nodes:
    - id: birth
      year: 1979
      age: 0
      type: given
      theme: original-mainstream
      label: '1979 年生於台北'
      scene: '家庭背景小康。從小學鋼琴。內向、害羞。'
    - id: super-newcomer
      year: 1997
      month: 8
      age: 18
      type: choice
      theme: original-mainstream
      scene: '台視《超級新人王》舞台。為高中同學伴奏的鋼琴手，害羞到不敢看鏡頭'
      chose:
        label: '上節目當伴奏'
        consequence: '主持人吳宗憲注意到他樂譜寫得工工整整、和弦進行有想法。被簽進阿爾發音樂當助理。月薪兩萬，泡茶買便當 + 無止境創作。'
      alternatives:
        - label: '不上節目'
          plausibility: structural
          note: '同代會彈鋼琴的高中生很多沒被注意到，最後走音樂老師或考音樂系。如果他不上 1997 那場節目，吳宗憲不會看見他，後面 25 年華語樂壇歷史完全不同。'
        - label: '上節目想當主角自己唱'
          plausibility: structural
          note: '常規選秀路徑：主動爭取唱主歌位置。如果走，會被當「另一個唱抒情歌的男生」評估，可能淘汰，不會以「鋼琴助理」身份建立品味。'
    - id: three-years-rejected
      year: 1999
      age: 21
      type: choice
      theme: original-mainstream
      scene: '寫了上百首歌，全部被退稿。劉德華退《眼淚知道》、張惠妹退《忍者》。原因都是「太奇怪、太超前、市場接受不了」'
      chose:
        label: '繼續寫不放棄 + 等到江蕙收下《落雨聲》'
        consequence: '第一首被採用的歌。為《Jay》專輯鋪路。三年退稿期養成「我的東西不是給別人改的，我自己唱」的決心。'
      alternatives:
        - label: '退稿後改寫成市場喜歡的版本'
          plausibility: structural
          note: '常規路徑：年輕製作助理會根據退稿 feedback 不斷修改。如果走，可能更早有歌被採用但失去獨特風格，後來《Jay》不會發生。'
        - label: '放棄音樂'
          plausibility: structural
          note: '三年退稿足以讓多數人轉行。如果走，會去做別的工作，可能成為一個小有才華的素人音樂人。'
    - id: jay-album-2000
      year: 2000
      month: 11
      age: 21
      type: choice
      theme: original-mainstream
      scene: '阿爾發音樂決定讓他自己出專輯'
      chose:
        label: '《Jay》全自製 + 融合 Rap/R&B/搖滾/古典/二胡 Hip-Hop'
        consequence: '亞洲賣破百萬。改變唱片工業生態：證明音樂人可以做自己、創新可以賺錢。「華語樂壇相信公式」變「相信冒險」。'
      alternatives:
        - label: '走標準偶像歌手路'
          plausibility: structural
          note: '常規 21 歲新人路徑：抒情主打 + 包裝偶像。如果走，可能短期更賺但失去「華語樂壇分水嶺」的歷史地位。'
    - id: china-style
      year: 2003
      age: 24
      type: choice
      theme: original-mainstream
      scene: '《葉惠美》專輯時思考下一個音樂方向'
      chose:
        label: '《東風破》+ 方文山詞 → 開創「中國風流行音樂」'
        consequence: '把古箏、琵琶、二胡用現代錄音技術 + R&B 節奏。後來《菊花台》《青花瓷》《蘭亭序》成系列。Time Asia 同年封面「The New King of Asian Pop」。'
      alternatives:
        - label: '繼續走 R&B/嘻哈路線'
          plausibility: structural
          note: '同代陶喆走純 R&B 路徑。如果走，會跟陶喆同象限競爭，少了「中國風」這個獨特標誌。'
        - label: '純抒情路線'
          plausibility: structural
          note: '更安全選擇（如 1990s 王力宏前期）。如果走，市場接受度更高但失去文化辨識度。'
    - id: jvr-music
      year: 2007
      age: 28
      type: choice
      theme: artist-boss
      scene: '與阿爾發音樂合約期滿'
      chose:
        label: '成立杰威爾音樂自己當老闆'
        consequence: '從藝人變老闆。完全創作自由。後來專輯品質更穩、商業成績更好。2022 《最偉大的作品》IFPI 全球銷量冠軍 720 萬張（華語首例）。'
      alternatives:
        - label: '續簽阿爾發 / 跳到 Sony 或環球'
          plausibility: structural
          note: '常規路徑：頂級藝人多選擇大廠合約。如果走，能獲得國際發行渠道但失去製作節奏的自主控制。'
    - id: secret-direct
      year: 2007
      age: 28
      type: choice
      theme: cross-medium
      scene: '同年除了開公司還有導演機會'
      chose:
        label: '導演《不能說的秘密》'
        consequence: '從歌手變導演。2011 《青蜂俠》進好萊塢。2016 《中國好聲音》當導師。打開「華語音樂人可以做什麼」的範圍。'
      alternatives:
        - label: '專心做音樂不跨界'
          plausibility: structural
          note: '同代多數歌手選擇單一身份深耕。如果走，可能音樂作品更多但失去文化偶像跨領域影響力。'
        - label: '只演不導'
          plausibility: structural
          note: '部分歌手以演員身份試水（如張學友）。如果走，會失去「導演 + 編劇」這層創作主導權，《不能說的秘密》的音樂與敘事整合性會打折。'
    - id: cross-strait-2008
      year: 2008
      age: 29
      type: choice
      theme: cross-strait
      scene: '北京奧運期間'
      chose:
        label: '說「期待奧運在自己的國家舉辦」+ 公開「我是中國人，也是台灣人」雙重表態'
        consequence: '在兩岸都保持商業成功。引發台灣綠營批評，但中國市場保留。「模糊的表態」成為他的長期策略，後來 2020 中國官媒引用他的話為其他藝人辯護。'
      alternatives:
        - label: '明確表態台灣立場'
          plausibility: structural
          note: '同代部分藝人選邊（如張惠妹《站在高崗上》事件）。如果走，會失去中國市場但保住台灣輿論支持。'
        - label: '完全沉默'
          plausibility: structural
          note: '另一部分藝人選擇不談政治。如果走，能避開兩邊質疑但失去「中國人 + 台灣人」雙重身份的彈性。'
    - id: nft-phanta
      year: 2022
      age: 43
      type: choice
      theme: artist-boss
      scene: 'Instagram 換上 Phanta Bear NFT 頭像，引發市場炒作。一天交易額 2.8 億台幣'
      chose:
        label: '杰威爾急澄清「未參與商業策劃、未收益」'
        consequence: '突顯名人效應在加密貨幣市場的爭議性。同年合作好友蔣先威 PHANTACi 品牌的關係處理。但「明星 NFT 風波」這個 pattern 已成型。'
      alternatives:
        - label: '直接公開合作不澄清'
          plausibility: structural
          note: '走完整 NFT 商業合作路徑。如果走，會分享 2.8 億的部分收益但會被綁進加密貨幣監管風險。'
        - label: '從一開始拒絕掛 NFT 頭像'
          plausibility: structural
          note: '保守路徑：不沾。如果走，避開風波但失去與好友的合作關係。'
    - id: world-tour
      year: 2024
      age: 45
      type: choice
      theme: cross-medium
      scene: '「嘉年華世界巡迴演唱會」自 2019 開始'
      chose:
        label: '持續全球巡演 75+ 場 + 馬來西亞武吉加里爾單場 6 萬人'
        consequence: '足跡英國、法國、澳洲、泰國、日本。YouTube MV 總觀看 51 億，《告白氣球》單一影片 2 億。新生代音樂人「我是聽周杰倫長大的」跨世代影響力確立。'
      alternatives:
        - label: '半退休 / 減少演出'
          plausibility: structural
          note: '同代部分歌手 40 歲後減少巡演（如劉德華）。如果走，能保留體力與家庭時間但失去全球巡迴的文化資本。'
        - label: '只在華語區巡演'
          plausibility: structural
          note: '常規華語天王路徑。如果走，能省成本但失去「亞洲流行天王」的國際品牌定位。'
translatedFrom: 'People/周杰倫.md'
sourceCommitSha: '4b6d28c54'
sourceContentHash: 'sha256:41da4ed1ac688006'
translatedAt: '2026-08-13T04:05:00+08:00'
---

# Jay Chou

> **30-Sekunden-Überblick:** 1997 spielte ein schüchterner 18-jähriger Junge beim Nachwuchswettbewerb „Super Neuling“ Klavier; drei Jahre später schrieb sein Debütalbum die Geschichte der chinesischsprachigen Popmusik neu. Jay Chou ist nicht nur Sänger – er ist der Mensch, der die gesamte Musikbranche glauben ließ, dass „Originalität sich verkaufen kann“. Von 2000 bis heute hat er mit 16 Alben bewiesen, dass chinesischsprachige Musik ihre östliche Eigenständigkeit bewahren und zugleich die Weltbühne erobern kann.

1999 saß Jay Chou im Tonstudio von JVR Music und erlebte die N-te Absage in Folge. Andy Lau wollte sein „Tränen wissen es“ nicht, A-mei lehnte seine „Ninja“ ab – die gesamte chinesischsprachige Musikwelt schien diesem jungen Kreativen zu sagen: Deine Musik ist ihrer Zeit voraus.

Niemand hätte vorhergesehen, dass dieser 21-jährige Produktionsassistent nur ein Jahr später alles umkrempeln würde.

## Vom Casting-Nebendarsteller zum Musik-Revolutionär

Im August 1997 war Jay Chou auf der Bühne von „Super Neuling“ bei TTV nicht der Hauptdarsteller. Er war nur der Klavierbegleiter eines Schulkameraden, zu schüchtern, um in die Kamera zu schauen. Aber Moderator Jacky Wu bemerkte das Detail: Die Noten dieses Jungen waren sauber notiert, die Akkordfolgen hatten Substanz.

„Ich wusste damals, dass dieser Mensch etwas hat“, erinnerte sich Jacky Wu später. An jenen Casting-Abend erinnert sich niemand an den Sänger, aber alle an den Klavier spielenden Jungen. In den drei Jahren der Vorbereitung danach holte Jacky Wu Jay Chou als Assistent zu Alfa Music: Monatsgehalt 20.000 NT$, Aufgaben war Tee aufbrühen, Lunch-Boxen holen und endloses Komponieren. In dieser Zeit schrieb Jay Chou über hundert Songs – alle wurden abgelehnt. Zu seltsam, zu avantgardistisch, der Markt könne das nicht annehmen – diese Gründe hörte er drei Jahre lang.

1999 kam endlich die Wende. Jody Chiang nahm „Das Geräusch des Regens“ (落雨聲) an, das er mit Vincent Fang geschrieben hatte – der erste Song von Jay Chou, der verwendet wurde.

## 2000: Die Musikrevolution eines Albums

Am 7. November 2000 erschien Jay Chous Debütalbum „Jay“. Das erste Stück „Liebenswerte Frau“ (可愛女人) verbindet Rap mit R&B-Rhythmus; „Perfektionismus“ (完美主義) mischt Rock mit klassischem Klavier; „Ehefrau“ (娘子) bringt gar die Erhu direkt in die Hip-Hop-Welt.

> **💡 Wusstest du?**
> „Jay“ vollbrachte etwas beispiellos Neues: Es bewies, dass chinesischsprachige Musik alles vereinen kann – und sich dabei ausgezeichnet verkauft. „Jay“ wurde in Asien über eine Million Mal verkauft; Jay Chou war über Nacht vom Assistenten zum Star geworden.

Wichtiger noch: Er veränderte die Ökologie der gesamten Plattenindustrie. Vor „Jay“ war die Erfolgsformel der chinesischsprachigen Musikszene einfach: einen singenden Menschen finden, ihm ein paar Balladen geben, ihn zum Idol verpacken. Jay Chou bewies einen anderen Weg: Musiker können sie selbst sein, Innovation kann sich bezahlt machen.

## Der Begründer des China-Stil-Pop

„Der Ostwind bricht“ (東風破) von 2003 war ein weiterer Meilenstein der chinesischsprachigen Szene. Vincents Fangs Text „Eine Lampe des Abschieds, einsam am Fenster stehend“ (一盞離愁，孤單佇立在窗口) verbindet sich mit Jay Chous chinesisch anmutendem Arrangement zu einem völlig neuen Musikgenre: China-Stil-Pop.

Das ist keine kulturelle Nostalgie, sondern kulturelle Innovation. Jay Chou verpackte traditionelle Instrumente wie Guzheng, Pipa und Erhu mit moderner Aufnahmetechnik in R&B-Rhythmen. „Chrysanthemen-Terrasse“ (菊花台), „Blau-weißes Porzellan“ (青花瓷), „Vorwort zur Orchideen-Pavillon“ (蘭亭序) – jedes ein Lehrbuch für die gelungene Verschmelzung von Ost und West.

Ausländische Medien begannen, das Phänomen wahrzunehmen. 2003 setzte das asiatische Magazin _Time_ Jay Chou aufs Cover – Titel: „The New King of Asian Pop“. Das war keine reine Medien-Hype: Jay Chou tat tatsächlich etwas, das zuvor niemand getan hatte – klassische chinesische Elemente fanden einen Platz in der globalen Popmusik.

## Der Rekordhalter der Golden Melody Awards

| Jahr | Auszeichnung                                        | Werk                   |
| ---- | --------------------------------------------------- | ---------------------- |
| 2001 | Bestes Album für populäre Musik                     | „Jay“                  |
| 2002 | Bestes Album, bester Produzent, beste Komposition   | „Fantasy“ (范特西)      |
| 2004 | Bestes Album für populäre Musik                     | „Yeh Hui-mei“ (葉惠美)  |
| 2008 | Song des Jahres, beste Komposition                  | „Blau-weißes Porzellan“|
| 2009 | Song des Jahres, bester männlicher Sänger, bestes MV| „Duft der Reisfelder“ / „Magier“ |
| 2011 | Bestes Album, bester männlicher Sänger              | „Beyond the Era“ (跨時代)|

Jay Chou ist einer der am häufigsten ausgezeichneten Künstler in der Geschichte des taiwanesischen Golden Melody Awards, mit insgesamt 15 Trophäen. Bei der „Album des Jahres“-Auszeichnung (später „bestes chinesischsprachiges Album“) wurde er zehnmal nominiert und gewann viermal – Rekord in Nominierungen und Siegen.

## Vom Künstler zum Boss: Die Geburt von JVR Music

2007 war ein weiterer Wendepunkt: Jay Chou gründete JVR Music und wechselte vom Künstler zum Geschäftsführer. Diese Entscheidung gab ihm vollständige kreative Freiheit und zeigte der chinesischsprachigen Szene eine andere Möglichkeit: Musiker müssen nicht für immer an Plattenfirmen gebunden sein.

Zahlen sprechen für sich: Nach der Gründung von JVR wurden Jay Chous Alben stabiler, die kommerziellen Erfolge besser. „Greatest Works of Art“ (最偉大的作品) von 2022 wurde von der IFPI als weltweit meistverkauftes Album zertifiziert – zum ersten Mal stand ein chinesischsprachiges Album an der Spitze dieser Liste, mit 7,2 Millionen verkauften Exemplaren.

## Der Durchbruch reicht über die Musik hinaus

Jay Chous Ambitionen beschränken sich nicht auf Musik. 2007 machte ihn „Das Geheimnis, das man nicht sagen darf“ (不能說的秘密) zum Regisseur; 2011 brachte ihn „The Green Hornet“ nach Hollywood; 2016 bewies „The Voice of China“ (中國好聲音), dass er auch als Coach bestehen kann.

Doch der größte Durchbruch könnte seine Veränderung der gesamten Branchenökologie sein. Er kreiert nicht nur Musik, sondern definierte neu, was chinesischsprachige Musiker tun und werden können. Vom Tonstudio auf die große Leinwand, von Taipeh in die Welt – Jay Chou eröffnete unzählige Möglichkeiten.

## Die Etablierung globaler Wirkung

Jay Chous Einfluss reicht längst über den chinesischsprachigen Raum hinaus. Die „Carnival World Tour“ läuft seit 2019 und gab weltweit bereits über 75 Konzerte – in Großbritannien, Frankreich, Australien, Thailand und Japan. Im Oktober 2024 zog ein einzelnes Konzert im Bukit-Jalil-Nationalstadion in Malaysia über 60.000 Zuschauer an – neuer persönlicher Rekord für ein einzelnes Konzert.

Auf YouTube übersteigen seine Musikvideos insgesamt 5,1 Milliarden Aufrufe; allein „Liebesballon der Beichte“ (告白氣球) hat über 200 Millionen Aufrufe. Die jüngere Musikergeneration sagt alle „Ich bin mit Jay Chou aufgewachsen“ – ein Beleg, dass sein Einfluss Generationen überdauert.

## Die unvermeidlichen Kontroversen und Fragen

### Die Grauzone der politischen Haltung

Jay Chous politische Haltung ist ein heikles Thema im Dialog zwischen beiden Seiten der Taiwanstraße. Er äußerte öffentlich „Ich bin Chinese“, sagte aber auch: „Ich bin in Taiwan geboren und aufgewachsen, ich bin auch Taiwaner.“ Während der Olympischen Spiele 2008 in Peking hoffte er, die Spiele in „meinem eigenen Land“ zu erleben, was Kritik von der grünen Seite in Taiwan auslöste.

Diese vagen Äußerungen erlauben ihm kommerziellen Erfolg auf beiden Seiten der Straße, werfen aber stets die Frage auf, ob Geschäftsinteressen über politische Haltung stehen. 2020 zitierte das chinesische Staatsfernsehen seine Worte, um andere Künstler zu verteidigen – was ihn erneut in politische Kontroversen verwickelte.

### Die Phanta-Bear-NFT-Affäre

Anfang 2022 geriet Jay Chou in einen NFT-Streit. Er stellte auf Instagram eine Phanta-Bear-NFT als Profilbild ein und löste damit einen Markt-Hype aus: Das NFT-Projekt erreichte an einem Tag ein Handelsvolumen von 280 Millionen NT$. JVR Music beeilte sich jedoch zu klären, dass Jay Chou „an keiner Planung oder Führung dieses Geschäfts beteiligt war und keinerlei Einnahmen erhalten hat“.

> **⚠️ Kontroverse Ansicht**
> Die Management-Firma erklärte, das NFT sei kein „Co-Branding“ von Jay Chou, sondern ein lizenziertes Produkt der Marke PHANTACi seines Freundes Chiang Hsien-wei. Aber die Affäre beleuchtet die Problematik des Prominenten-Effekts im Kryptomarkt.

### Der Ghostwriter-Verdacht

Seit langem gibt es in Jay Chous Kreativteam mehrere Helfer im Hintergrund, darunter den Texter Huang Jun-lang. Dieser beklagte sich in den sozialen Medien über den Druck des kreativen Prozesses und nährte Fragen, ob Jay Chous Werke wirklich vollständig originell sind. Auch wenn Teamarbeit in der Musikindustrie die Norm ist, bestehen solche Zweifel bei einem Künstler, der so sehr auf Originalität setzt, fort.

## Die dauerhafte Veränderung der chinesischsprachigen Musikszene

Jay Chous größter Beitrag ist nicht, wie viele Platten er verkauft hat, sondern dass er die Vorstellungskraft der gesamten Branche veränderte. Vor ihm glaubte die chinesischsprachige Szene an „Sicherheit“ – die Nachahmung bereits erfolgreicher Formeln. Nach ihm beginnt die Szene an „Risiko“ zu glauben – dass auch Originalität und Experimente erfolgreich sein können.

Heute ist die chinesischsprachige Musikszene voller vielfältiger Stimmen: Rap, Elektro, Folk, experimentelle Musik – die Wurzeln dieses Ökosystems reichen bis zu jenem Album „Jay“ von 2000 zurück. Jay Chou zeigte mit einem Album allen: Die Grenzen der chinesischsprachigen Musik können unendlich weit sein.

Vom schüchternen Klavierbegleiter 1997 zum König der chinesischsprachigen Popmusik 2026 – Jay Chous Weg ist nicht nur eine persönliche Erfolgsgeschichte, sondern die Evolutionsgeschichte der gesamten chinesischsprachigen Popmusik. Er hat eines bewiesen: Wahre Innovatoren sind nicht die, die Trends verfolgen, sondern die, die Trends erschaffen.

---

**Weiterführende Lektüre**:

- [Chou Tzu-yu](/people/周子瑜) – der zweithöchste IG-Followerwert taiwanesischer Künstler, direkt hinter Jay Chou
- [Taiwanesische Popmusik](/music/台灣流行音樂) – das gesamte Branchenökosystem und die Generationswende, zu der Jay Chou gehört
- [Stefanie Sun](/people/孫燕姿/) – im selben Jahr für den besten Newcomer der 12. Golden Melody Awards nominiert, nur eine Stimme Unterschied – definierte zwei parallele Musiklinien der 2000er
- [Chia Yung-chieh](/people/賈永婕) – ein anderer taiwanesischer Weg, Künstler-Identität in bereichsübergreifenden Einfluss zu übersetzen (Unterhaltung → Brautmodenmarke → öffentliche Mobilisierung → öffentliche Unternehmensführung), als Kontrast zu Jay Chous Kulturindustrie-Pfad

## Referenzen

- [Jay Chous Auszeichnungs- und Nominierungsliste – Wikipedia](https://zh.wikipedia.org/zh-tw/%E5%91%A8%E6%9D%B0%E5%80%AB%E8%8E%B7%E5%A5%96%E4%B8%8E%E6%8F%90%E5%90%8D%E5%88%97%E8%A1%A8)
- [Time Magazine Asia Edition – 3. März 2003](https://content.time.com/time/magazine/asia/0,9263,501030303,00.html)
- [IFPI Global Album Sales Chart 2022 – Jay Chous „Greatest Works of Art“](https://tbotaiwan.com/ifpi-global-album-sales-chart-2022-jay-chou-greatest-works-of-art/)
- [Jay Chous NFT „Phanta Bear“ bringt an einem Augenblick 280 Mio. – Firma grenzt sich eilig ab: kein Geld erhalten – Mirror Media](https://www.mirrormedia.mg/story/20220104ent036/)
- [China-Zitat: Jay Chou sagte einst „Ich bin Chinese“ – chinesische Staatsmedien verteidigen Ouyang Nana – CTS News](https://news.cts.com.tw/cts/politics/202009/202009292015341.html)
- [Carnival World Tour – Wikipedia](https://zh.wikipedia.org/zh-hant/%E5%98%89%E5%B9%B4%E8%8F%AF%E4%B8%96%E7%95%8C%E5%B7%A1%E8%BF%B4%E6%BC%94%E5%94%B1%E6%9C%83)
- [Greatest Works of Art – Wikipedia](https://en.wikipedia.org/wiki/Greatest_Works_of_Art)
- [Jay Chou YouTube Official Channel](https://www.youtube.com/channel/UC8CU5nVhCQIdAGrFFp4loOQ)
- [JVR Music Offizielle Website](https://www.jvrmusic.com/)
- [„Jay-Chou-Bär-NFT“ soll Konzertkarten kaufen können! PhantaBear steigt um 120 %, enttäuscht aber viele – Block Tempo](https://www.blocktempo.com/rumor-has-it-you-can-snag-jay-chou-concert-tickets-phantabear-soars-by-120/)
- [Jay Chou unterbricht bei einem Konzert Fans mit „mutmaßlich pro-taiwanesischer“ Aussage – Dcard](https://www.dcard.tw/f/entertainer/p/230941846)
