---
title: 'Hou Hsiao-hsien'
description: 'Ein Regisseur, der Großaufnahmen ablehnt und doch die Welt eroberte – ein Bildrevolutionär gegen die Filmgrammatik'
date: 2026-03-24
category: 'People'
tags: ['Hou Hsiao-hsien', 'Taiwan New Cinema', 'Goldener Löwe von Venedig', 'Festival von Cannes', 'Filmästhetik', 'Lange Einstellung']
subcategory: '電影與戲劇'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-03-24
lastHumanReview: false
readingTime: 15
lifeTree:
  protagonist: '侯孝賢'
  birthYear: 1947
  span: '1947–2023'
  source:
    article: 'knowledge/People/侯孝賢.md'
    commit: 'a05d2431'
    commitDate: '2026-03-24'
    extractedBy: 'Taiwan.md (Semiont) β-r5'
    extractedAt: '2026-04-26 13:30 +0800'
    note: '原文 6 條 references（中央社 / 關鍵評論網 / Global Taiwan / Wikipedia / 台灣電影網）+ 影展年表。Counterfactual 多基於同代台灣新電影導演（楊德昌、蔡明亮、李安）的對照路徑。'
  intro: '一個拒絕用特寫鏡頭、不要求演員背台詞的客家眷村少年，用反電影語法創造永恆藝術。1989 年捧威尼斯金獅，2015 年坎城最佳導演，2023 年因阿茲海默症告別。每一次跨越（商業 → 新電影、台灣 → 國際、導演 → 退場）都有他沒走的路。'
  themes:
    - id: commercial-art
      label: '商業 vs 藝術'
      color: '#8B5CF6'
    - id: language-grammar
      label: '主流語法 vs 反語法'
      color: '#EC4899'
    - id: local-international
      label: '本土 vs 國際'
      color: '#10B981'
    - id: continue-stop
      label: '持續 vs 退場'
      color: '#F59E0B'
  nodes:
    - id: birth
      year: 1947
      age: 0
      type: given
      theme: local-international
      label: '生於廣東梅縣（客家），1 歲遷高雄鳳山眷村'
      scene: '在外省與本省文化交融的眷村成長。「跨越」成為他日後創作的核心 DNA——跨省籍、跨時代、跨語言、跨記憶。'
    - id: enroll-film-school
      year: 1969
      age: 22
      type: choice
      theme: commercial-art
      scene: '高中成績平凡，更愛看小說聽音樂'
      chose:
        label: '考入國立台灣藝術專科學校電影科'
        consequence: '正式踏入電影世界。為日後 11 年後成為導演鋪路。'
      alternatives:
        - label: '走主流大學'
          plausibility: structural
          note: '當時藝專是「考不上大學」的選項。如果他考上一般大學，可能走編劇或藝術史路線，少了實作的根。'
        - label: '不念書直接工作'
          plausibility: structural
          note: '同代許多人 18-22 歲就進社會。如果他走這條，可能會以製片助理身份從基層慢慢爬，但失去藝專對「藝術電影」的想像力訓練。'
    - id: commercial-debut
      year: 1980
      age: 33
      type: choice
      theme: commercial-art
      scene: '開始執導'
      chose:
        label: '前 3 部都拍商業愛情片（《就是溜溜的她》《風兒踢踏踩》《在那河畔青草青》）'
        consequence: '清新、甜美、賣座、完全符合市場期待。但已埋下種子：開始質疑「為什麼電影一定要這樣拍？」商業歷練給了他後來談判藝術自由的籌碼。'
      alternatives:
        - label: '直接走藝術片'
          plausibility: structural
          note: '同代有人一開始就拒絕商業（如蔡明亮）。如果走這條，可能更早被定位為藝術片導演但少了製片信任，無法後來主導《悲情城市》這種商業 + 藝術混合的大製作。'
    - id: new-cinema-1983
      year: 1983
      age: 36
      type: choice
      theme: language-grammar
      scene: '小野與吳念真策劃《光陰的故事》《兒子的大玩偶》，邀新銳導演'
      chose:
        label: '加入台灣新電影 + 從《風櫃來的人》開始建立反語法美學'
        consequence: '從這部開始：讓攝影機配合演員、不打燈、不打燈、長鏡頭、無特寫。1983 法國南特影展最佳影片是第一個外部肯定。'
      alternatives:
        - label: '繼續拍商業片'
          plausibility: structural
          note: '前 3 部商業成功，他完全可以繼續這條路。如果走，會成為另一個成功的台灣商業導演（朱延平那條線），但不會有國際影展史。'
        - label: '加入但不變美學'
          plausibility: structural
          note: '部分新電影導演用傳統語法但拍嚴肅題材。如果走這條，會少了「客觀凝視」這個獨特標誌，國際辨識度會大打折扣。'
    - id: golden-lion-1989
      year: 1989
      age: 42
      type: choice
      theme: local-international
      scene: '《悲情城市》題材敏感（二二八），製作前途未卜'
      chose:
        label: '拍 + 國際策略全配套（焦雄屏文化翻譯 + 媒體攻勢 + 精美手冊）'
        consequence: '威尼斯金獅獎 = 台灣電影史第一座國際 A 級影展首獎。台幣 6000 萬票房 = 從「票房毒藥」變「台灣之光」。開啟 1989-1995 台灣電影國際黃金時代。'
      alternatives:
        - label: '不拍敏感題材'
          plausibility: structural
          note: '當時二二八仍是禁忌邊緣。同代多數導演避開政治題材。如果他選穩，會少了《悲情城市》這個歷史閃電——後續坎城/柏林華語電影黃金期可能晚 5 年。'
        - label: '拍但不做國際策略'
          plausibility: structural
          note: '焦雄屏的文化翻譯角色 + 邱復生的媒體攻勢是金獅關鍵。如果只拍不策劃，可能拿到歐洲二線獎但無金獅。'
    - id: dream-of-life
      year: 1993
      age: 46
      type: choice
      theme: language-grammar
      scene: '金獅獎後可乘勝追擊拍商業大片'
      chose:
        label: '拍《戲夢人生》（李天祿傳記）+ 推極簡敘事到極致'
        consequence: '坎城評審團獎。多語言並存（台/日/北京話）。被公認為侯孝賢藝術高峰。「幾乎沒有傳統戲劇衝突，全靠氛圍營造」。'
      alternatives:
        - label: '走國際合製商業片'
          plausibility: structural
          note: '李安 1993 同年拍《囍宴》拿柏林金熊，後來走向好萊塢。如果侯走這條，會有更大票房但失去「電影詩人」純粹性。'
    - id: shanghai-flowers
      year: 1998
      age: 51
      type: choice
      theme: language-grammar
      scene: '改編張愛玲小說《海上花列傳》'
      chose:
        label: '全片用上海話 + 室內封閉空間'
        consequence: '進一步去除「動作」與「事件」，靠對話張力推進。語言 + 空間的雙重 commitment——不為了讓觀眾看懂而妥協。'
      alternatives:
        - label: '用普通話拍'
          plausibility: structural
          note: '改編華語經典文學的標準做法（如李安《色戒》部分情節）。普通話會放大兩岸三地市場，但失去上海話對「上海性」的本質承諾。'
    - id: assassin
      year: 2015
      age: 68
      type: choice
      theme: commercial-art
      scene: '《刺客聶隱娘》耗時 7 年製作'
      chose:
        label: '完成 + 走極致美學路線'
        consequence: '坎城最佳導演獎 = 第二次歐洲三大影展重要獎項。「視覺效果最美的電影之一」。但票房不理想——叫好不叫座。藝術純粹主義的最終 commitment。'
      alternatives:
        - label: '中途放棄或妥協'
          plausibility: structural
          note: '7 年製作期、武俠題材、實景困難。如果妥協（縮短拍攝、用 CGI、加更多動作戲），可能拿坎城但失去極致美學的純粹性。'
        - label: '不接這個案'
          plausibility: structural
          note: '武俠題材對侯式美學是 stretch。如果他不接，可能繼續拍《最好的時光》這種風格的當代片。沒有《刺客》的「絕唱」感。'
    - id: retire-2023
      year: 2023
      age: 76
      type: event
      theme: continue-stop
      label: '阿茲海默症退休'
      scene: '《刺客聶隱娘》成為告別作品。國際媒體：「一個時代的結束。」'
    - id: family-walk
      year: 2025
      age: 78
      type: choice
      theme: continue-stop
      scene: '退休後'
      chose:
        label: '回歸家庭 + 與兒子在台北家附近散步'
        consequence: '78 歲生日當天媒體拍到父子溫馨散步畫面。「沒有戲劇性、沒有特寫、只有安靜詩意的日常」——這個畫面很「侯孝賢」。'
      alternatives:
        - label: '繼續嘗試小製作'
          plausibility: structural
          note: '同代有導演（如黑澤明、伯格曼）退休後仍嘗試小作品。如果他堅持拍，可能因疾病造成晚節不保，反而傷害遺產。'
translatedFrom: 'People/侯孝賢.md'
sourceCommitSha: '4b6d28c54'
sourceContentHash: 'sha256:64e8c8786128b4a0'
translatedAt: '2026-08-13T07:30:00+08:00'
---

# Hou Hsiao-hsien

> **30-Sekunden-Überblick**
>
> Ein Regisseur, der Großaufnahmen verweigert und von seinen Schauspielern kein Auswendiglernen von Dialogen verlangt, wurde zum einflussreichsten Meister des chinesischsprachigen Films weltweit. Hou Hsiao-hsien (1947-) revolutionierte mit einer „landschaftsbildhaften Ästhetik der langen Einstellung“ die Filmsprache; 1989 erhielt „Eine Stadt der Trauer“ (悲情城市) den Goldenen Löwen von Venedig und eröffnete das internationale Goldene Zeitalter des taiwanesischen Films. Sein Einfluss reicht bis zu zeitgenössischen Meistern wie Jia Zhangke, Hirokazu Kore-eda u.a. – ein Beweis, dass auch eine „anti-hollywoodsche“ Drehweise ewige Kunst schaffen kann. Nachdem 2015 „Der Killer“ (刺客聶隱娘) in Cannes den Preis für die beste Regie gewann, trat er 2023 wegen Alzheimer zurück und beendete eine legendäre Karriere.

1988, vor dem Eisentor des Filmfestivals von Venedig, berührten eine Gruppe taiwanesischer Regisseure neidvoll das Tor und fragten sich, wann sie je diesen Tempel des Films betreten würden. Einer von ihnen war Hou Hsiao-hsien, 41 Jahre alt, längst auf europäischen Zweitliga-Festivals vielfach ausgezeichnet, aber von den taiwanesischen Medien noch als „Preisträger von Provinzfestivals“ verspottet.

Ein Jahr später, hinter demselben Tor, holte er mit „Eine Stadt der Trauer“ den Goldenen Löwen – der erste Hauptpreis eines internationalen A-Festivals in der Geschichte des taiwanesischen Films. Noch erstaunlicher: Dieser „unverständliche“ Film spielte 60 Millionen NT$ an den Kinokassen ein; das Begleitheft zu „Eine Stadt der Trauer“ im Buchladen des Taipeher Hauptbahnhofs war schlagartig vergriffen.

Vom als „Kassengift“ verschrienen zum Eroberer Venedigs – Hou Hsiao-hsien schuf mit der anti-mainstreamigsten Methode – Verzicht auf Großaufnahmen, Verzicht auf Anpassung an die Kamera, Verzicht auf traditionelle Dramatik – eine einzigartige Bildsprache der Filmgeschichte.

## Vom Militärsiedlungsdorf nach Venedig: Der Weg eines Hakka-Jungen

### Der Ausgangspunkt der Alleingrenzen (1947-1969)

Am 8. April 1947 wurde Hou Hsiao-hsien in Meixian, Guangdong, geboren – Hakka. Mit einem Jahr zog die Familie in das Militärsiedlungsdorf Fengshan in Kaohsiung um und wuchs in einer Welt der Verschmelzung von Festlands- und Inselkultur auf. Dieses „Überschreiten“ wurde zum Kerngen seiner späteren Werke – nicht nur über Provinzen und Sprachen hinweg, sondern über Zeiten und Erinnerungen.

> „Die Erfahrung des Militärsiedlungsdorfs ließ mich früh wissen: Es gibt nichts Reines auf der Welt.“ – Hou Hsiao-hsien

Von klein auf introvertiert und beobachtungsstark, wurde er zum geborenen „stillen Betrachter“. In der Oberschule waren seine Noten durchschnittlich, lieber las er Romane und hörte Musik. 1969 bestand er die Aufnahmeprüfung der Filmaabteilung der Nationalen Kunsthochschule Taiwans und betrat offiziell die Welt des Films.

### Die Ausbildung zum Kommerzregisseur (1980-1983)

1980 begann der 33-jährige Hou zu inszenieren. Seine ersten drei Filme – „Das ist doch sie“, „Wind und Tritt“ und „An dem Flussufer mit grünem Gras“ – waren erfolgreiche kommerzielle Liebeskomödien: frisch, süß und ganz nach den Markterwartungen.

Doch in dieser Phase lag schon der Same der späteren Revolution: Er begann zu fragen: „Warum muss Film eigentlich so gedreht werden?“

### Der Ruf des Neuen Kinos (1983-1989)

1982 organisierten Hsiao Yeh und Wu Nien-jen „Geschichten der Zeit“ (光陰的故事) und „Der kleine Spielzeugmacher“ (兒子的大玩偶); sie luden Regisseure der neuen Generation wie Edward Yang ein, auch Hou war beteiligt. Nach dem Kontakt mit diesen um die dreißig Jahre alten, im Ausland ausgebildeten Kreativen begann er, über tiefere Fragen nachzudenken:

**Was ist echter Film?**

Mit „Die Jungs von Fengkuei“ (風櫃來的人, 1983) fand Hou Hsiao-hsien die Antwort.

## Die revolutionäre Filmsprache: Wenn die Maschine sich dem Menschen anpasst

### Die „Anti-Film“-Drehphilosophie

Der Kern von Hous Filmrevolution liegt in einer subversiven Idee: **die Kamera passt sich den Schauspielern an, nicht umgekehrt.**

Das klingt technisch, ist aber eine Revolution des Filmbilds:

**Traditioneller Film:** Schauspieler stellt sich auf den Punkt → Bildausschnitt → Lichtsetzung → Aufnahme
**Hou-Hsiao-hsien-Film:** Schauspieler bewegt sich natürlich → Kamera folgt → kein künstliches Licht → Dokumentation

Das Ergebnis: Seine Filme haben fast keine Großaufnahmen, denn Großaufnahmen verlangen, dass sich die Schauspieler nach der Kameraposition „richten“.

### Die Poetik der langen Einstellung

Der Kritiker des französischen „Cahiers du cinéma“ beschrieb Hous lange Einstellung: „Wie die offenen Flächen eines chinesischen Landschaftsbilds, in dem die Zeit selbst zur Hauptfigur wird.“

Doch seine lange Einstellung unterscheidet sich von der von Tsai Ming-liang oder Theo Angelopoulos – nicht die bewusste „Langsamkeit“, sondern das „objektive Starren“. Er wollte die Präsenz der Kamera eliminieren, damit der Zuschauer die Wirklichkeit spürt, die dem Alltag am nächsten ist.

**Technische Innovationen:**

- Keine detaillierte Probenarbeit; die Schauspieler sollen „mit der Szene verschmelzen“
- Oft kein künstliches Licht, Verlass auf natürliches Licht
- Eine Szene kann zwei Wochen gedreht werden, bis sie „natürlich“ ist
- Die Kamera bleibt immer „Dokumentar die“, nie „Regie führend“

> In „Kohi Jikou – Kaffeezeit“ (珈琲時光) entstand die Szene, in der Protagonist und Protagonistin sich in verschiedenen Zügen aneinander vorbeibewegen, nach fast zwei Wochen Dreh. Selbst der deutsche Regisseur Wim Wenders rief „unbegreiflich“.

### Die Ausbreitung des Einflusses

Nachdem Akira Kurosawa „Das Leben der Meister“ (戲夢人生) gesehen hatte, sagte er: „So ein Werk kann ich nicht drehen.“

Die Liste zeitgenössischer Regisseure, die von Hou beeinflusst sind, ist atemberaubend:

- **Jia Zhangke** (Leitfigur der sechsten chinesischen Generation)
- **Hirokazu Kore-eda** (japanischer Zeitgenössischer Meister)
- **Abbas Kiarostami** (iranische Neue Welle)

Sie alle erbten auf unterschiedliche Weise Hous „objektives Starren“ und die „Ästhetik der langen Einstellung“.

## Das Wunder von Venedig: „Eine Stadt der Trauer“ und die Welteroberung des Taiwan New Cinema

### Der siebenjährige internationale Festivalweg (1983-1989)

Der Goldene Löwe für „Eine Stadt der Trauer“ fiel nicht vom Himmel. Seit 1983 baute Hou auf internationalen Festivals Ansehen auf:

| Jahr | Werk                     | Internationale Auszeichnung                                  |
| ---- | ------------------------ | ----------------------------------------------------------- |
| 1983 | „Die Jungs von Fengkuei“ | Bester Film des Filmfestivals von Nantes                     |
| 1984 | „Winterferien“           | Bester Film in Nantes, Preis für Humanismus in Locarno      |
| 1985 | „Eine Kindheit in Taiwan“| FIPRESCI-Preis der Berlinale                                 |
| 1986 | „Staub im Wind“          | Preis für beste Musik & beste Kamera in Nantes               |
| 1989 | „Eine Stadt der Trauer“  | **Goldener Löwe, Filmfestival von Venedig**                  |

### Der Erfolg der internationalen Strategie

Der Erfolg von „Eine Stadt der Trauer“ war sorgfältig choreografiert:

1. **Medienoffensive**: Der Produzent Chiu Fu-sheng lud Journalisten internationaler Blätter wie „Village Voice“ und „Sight & Sound“ zu Interviews nach Taiwan
2. **Kulturelle Übersetzung**: Man produzierte ein exquisites Filmbegleitheft mit Beziehungsdiagrammen und historischem Hintergrund
3. **Die Rolle der Kritikerin Peggy Chiao**: Als kulturelle Brücke half sie dem westlichen Publikum, die östliche Ästhetik zu verstehen

> Peggy Chiao: „Glaubt nicht, dass die Leute euren Film von selbst verstehen. Man muss ihnen beibringen, wie man nicht-westliche, nicht-mainstreamige Filmästhetik liest.“

### Die Bedeutung des Wendepunkts

Nach der Auszeichnung von „Eine Stadt der Trauer“ kippten die Einstellungen der taiwanesischen Medien zum Neuen Kino um 180 Grad – vom „Kassengift“ zum „Stolz Taiwans“.

Wichtiger noch: Sie eröffnete das internationale Goldene Zeitalter des taiwanesischen Films (1989-1995):

- Edward Yang, „Ein Kind unserer Zeit“ (牯嶺街少年殺人事件, 1991, Sonderpreis der Jury in Tokio)
- Hou Hsiao-hsien, „Das Leben der Meister“ (1993, Jurypreis in Cannes)
- Ang Lee, „Das Hochzeitsbankett“ (1993, Goldener Bär in Berlin)
- Tsai Ming-liang, „Vive L'Amour“ (1994, Goldener Löwe in Venedig)

Peggy Chiao sagte: „Zwischen 1989 und 1995 war der beste, modischste Film der taiwanesische Film.“

## Kunsthöhepunkt: Vom „Das Leben der Meister“ zum „Assassin“

### Die vollständige Reife des Stils (1990er-Jahre)

„Das Leben der Meister“ (1993) gilt allgemein als Hous künstlerischer Höhepunkt. In dieser Biografie über den Puppenspieler Li Tian-lu trieb Hou seine Ästhetik auf die Spitze:

- **Mehrsprachigkeit**: Hokkien, Japanisch und Mandarin vermischt sich natürlich – ein Spiegel der Sprachökologie Taiwans
- **Struktur des Spiels im Spiel**: Die Grenze zwischen Puppentheater und realem Leben verschwimmt
- **Minimale Erzählung**: Fast ohne traditionelle dramatische Konflikte, ganz über die Atmosphäre

Der Cannes-Juror Abbas sagte, dieser Film versetze ihn in „tiefe Bewunderung“.

### Die anhaltende Innovation des 21. Jahrhunderts

- **„Blumen von Shanghai“ (1998)**: Nach einem Roman von Eileen Chang, komplett in Shanghaier Dialekt
- **„Millennium Mambo“ (2001)**: Zusammenarbeit mit Shu Qi, über die Verlorenheit der urbanen Gegenwart
- **„Three Times“ (2005)**: Dreiteilige Struktur, Liebe über drei Epochen

### „Der Assassin“: Das Abschiedswerk (2015)

Der über sieben Jahre entstandene „Der Assassin“ wurde zu Hous filmischem Vermächtnis. Dieser nach einer Tang-Legende gedrehte Wuxia-Film:

- **Preis für die beste Regie in Cannes**: Hous zweiter bedeutender Preis auf den drei großen europäischen Festivals
- **Extreme Ästhetik**: gepriesen als „einer der visuell schönsten Filme“
- **Kulturelle Tiefe**: die Tang-Kultur mit modernem Blick neu gedeutet

Doch er fand auch „Gefallen, aber keine Resonanz an den Kinokassen“ – ein Beweis, dass Hou stets ein Purist der Kunst blieb.

## Das kulturelle Erbe des Paten des Taiwan New Cinema

### Die Ebenen des Einflusses

Hous Einfluss auf den taiwanesischen und den Weltfilm lässt sich in drei Ebenen teilen:

**Technisch**: Er begründete die fotografische Ästhetik des „objektiven Starrens“
**Kulturell**: Er bewies, dass nicht-westlicher Film internationalen Festivals genügt
**Geistig**: Er beharrte auf Reinheit der Kunst und verweigerte den Kompromiss an die Kommerz

### Schüler und Weitergabe

Direkt von Hou beeinflusste taiwanesische Regisseure:

- **Tsai Ming-liang**: Er erbte die Ästhetik der langen Einstellung und entwickelte ein extremeres „langsames Kino“
- **Ang Lee**: Er ging zwar nach Hollywood, doch in Werken wie „Gefahr und Begierde“ (色戒) ist Hous Ästhetik noch sichtbar
- **Edward Yang**: Anderer Stil, aber ebenso der Idee des Kunstfilms verpflichtet

### Dauerhafte internationale Reputation

Selbst nach dem Rücktritt gilt Hou der internationalen Filmwelt als „lebende Legende“:

- Die Cinémathèque française richtete eine Hou-Hsiao-hsien-Sektion ein
- Das Festival von Cannes würdigte seine Beiträge mehrfach
- Das Filmfestival von Venedig nennt ihn „Filmpoet“

> „Hous Filme haben der Welt gelehrt, dass Film Poesie sein kann – und nicht nur Geschichte.“ – Cahiers du cinéma

## Abschied und Ewigkeit (Rücktritt 2023)

### Der Abschied der Demenz

2023 trat der 76-jährige Hou Hsiao-hsien wegen Alzheimer offiziell zurück – ein Schock für das internationale Kino. „Der Assassin“ wurde sein Abschiedswerk.

Die internationale Presse urteilte: „Das Ende einer Epoche.“ Doch sein Einfluss wird ewig weiterleben.

### Das Große im Gewöhnlichen

Nach dem Rücktritt kehrte Hou in die Familie zurück, ging mit seinem Sohn in der Nähe seines Hauses in Taipeh spazieren und lebte das Leben eines gewöhnlichen alten Menschen. Am 8. April 2025, seinem 78. Geburtstag, fotografierten die Medien die herzliche Szene des Vater-Sohn-Spaziergangs.

Dieses Bild ist sehr „Hou Hsiao-hsien“ – keine Dramatik, keine Großaufnahme, nur der leise, poetische Alltag.

### Der Platz in der Filmgeschichte

Was Hou der Welt schließlich hinterlässt, sind nicht nur Filme, sondern eine neue Art des „Sehens“:

**Er bewies, dass Film ohne Hollywood-Grammatik auskommen und zugleich die Welt bewegen kann.**
**Er bewies, dass „langsam“ und „still“ gleichermaßen künstlerische Kraft besitzen.**
**Er bewies, dass Taiwan einen wichtigen Platz auf der internationalen Kultur-Bühne beanspruchen kann.**

In einer immer schnelleren, lauteren Welt erinnert uns Hous Kino: Manchmal kommt die tiefste Schönheit aus dem leisesten Blick.

Er ist der Stolz des taiwanesischen Films und ein kostbarer Schatz des Weltfilms. Wenn die Filmgeschichte geschrieben wird, wird Hou Hsiao-hsiens Name für immer glänzen – nicht weil er so viele Filme drehte, sondern weil er den Film selbst veränderte.

---

## Referenzen

1. [Der Goldene Löwe fiel nicht vom Himmel: Peggy Chiao über Hous internationalen Festivalweg in den 1980ern](https://www.cna.com.tw/culture/article/20200104w004) – Central News Agency
2. [Das Geheimnis hinter Hous Filmaufnahmen: Der landschaftsbildhafte Stil kommt nicht allein von der langen Einstellung](https://www.thenewslens.com/article/17354) – The News Lens
3. [An Ally in the Arts: How International Independent Filmmaking and Film Festivals Enhance Taiwan's Visibility](https://globaltaiwan.org/2025/08/an-ally-in-the-arts/) – Global Taiwan Institute
4. [Hou Hsiao-hsien](https://en.wikipedia.org/wiki/Hou_Hsiao-hsien) – Wikipedia
5. [Hou Hsiao-hsien leidet an Alzheimer; ausländische Medien: „Der Assassin“ ist sein letztes Werk](https://www.cna.com.tw/news/amov/202310250271.aspx) – Central News Agency
6. [Hou Hsiao-hsien | Taiwan Cinema](https://taiwancinema.bamid.gov.tw/Staff/StaffContent/?ContentUrl=12434)
