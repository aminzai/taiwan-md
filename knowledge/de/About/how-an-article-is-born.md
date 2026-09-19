---
title: 'Wie ein Artikel entsteht: Die sechsstufige Produktionslinie von Taiwan.md zur Abwehr der KI-Schreibinstinkte (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)'
description: 'Jeder Artikel, den Sie auf Taiwan.md lesen, ist das Ergebnis einer sechsstufigen Produktionslinie mit Dutzenden von nicht überspringbaren Kontrollpunkten und einem KI-Redaktionsteam, das nicht selbst schreibt. Dieser Mechanismus existiert, um die typischen Fehler der KI zu korrigieren: Fakten chronologisch auflisten, inhaltsleere Sätze generieren, englische Zusammenfassungen fälschlicherweise als Zitate wiedergeben oder alte Muster übernehmen. Dieser Artikel zerlegt diese Produktionslinie – und er ist selbst ein Produkt dieser Linie.'
date: 2026-06-19
tags:
  [
    'about',
    'meta',
    'Schreibmethodik',
    'Kuratierung',
    'rewrite-pipeline',
    'editorial',
    'semiont',
    'KI-Schreiben',
  ]
author: 'Taiwan.md'
category: 'About'
readingTime: 11
featured: false
lastVerified: 2026-06-19
lastHumanReview: false
relatedDiary: ['2026-06-19-123349-manual']
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: 'd182e5d85'
sourceContentHash: 'sha256:4dc98dc84117c5d8'
sourceBodyHash: 'sha256:2679dec9ddab6dbc'
translatedAt: '2026-09-19T11:59:12+08:00'
---

# Wie ein Artikel entsteht: Die sechsstufige Produktionslinie von Taiwan.md zur Abwehr der KI-Schreibinstinkte (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **30-Sekunden-Zusammenfassung:** Jeder Artikel, den Sie auf Taiwan.md lesen, basiert auf einer sechsstufigen Produktionslinie: Zuerst wird eine Perspektive entwickelt, dann erfolgt die Recherche, der Schluss wird zuerst geschrieben, jede Aussage wird wörtlich überprüft, visuelle Elemente werden ergänzt und es erfolgt eine bidirektionale Verlinkung. Diese Linie ist kein gewöhnlicher „Artikel-Schreibprozess“; jeder Kontrollpunkt zielt auf einen typischen Fehler der KI ab: Fakten chronologisch auflisten, inhaltsleere Sätze generieren, englische Zusammenfassungen fälschlicherweise als Zitate wiedergeben oder alte Muster übernehmen. Dieser Artikel zerlegt diese Produktionslinie – und er ist selbst ein Produkt dieser Linie.

Am 18. Juni 2026 um 19:53 Uhr wurde ein Commit leise in den Hauptzweig eingespielt. Ein Artikel über die taiwanesische Band „Elephant Gymnastics“ (大象體操) ging online: 5.604 chinesische Zeichen, 56 Fußnoten und 11 szenische Untertitel[^1]. Zu dieser Zeit war niemand vor dem Computer. Es war der Routine-Flügelrad von Taiwan.md, das es in der Nacht ohne Personal fertigstellte und hochlud.

Doch bevor dieser Commit erfolgte, hatte dieser Artikel fast hundert Suchvorgänge durchlaufen, 59 Quellen konsultiert und die ursprüngliche Fassung an 12 Stellen korrigiert. Er durchlief sechs Stufen und Dutzende von nicht überspringbaren Kontrollpunkten unter Einsatz eines klar geteilten KI-Redaktionsteams. Was Sie lesen, sind die 5.604 Zeichen auf der Oberfläche. Dieser Artikel soll Ihnen die Maschine unter der Oberfläche zeigen.

```tw-figure
Fast 100 Suchvorgänge → 1 Artikel
Recherche zu 〈Elephant Gymnastics〉: ca. 95 Abfragen, 59 Quellen, 12 Falschmeldungen korrigiert
Taiwan.md Routineprotokoll, 2026-06-18
```

## Warum man für einen Artikel eine Maschine braucht

Wenn Sie einer KI ein Thema geben und sie bittet, einen Artikel zu schreiben, wird sie meistens so vorgehen: Sie recherchiert, ordnet die gefundenen Fakten chronologisch an, fügt jedem Absatz einen bedeutungsvoll klingenden zusammenfassenden Satz hinzu und schließt mit einem „Die Entwicklung wird fortgesetzt“-Satz ab. Solche Artikel gibt es in Wikis; KI-Inhaltsfarmen produzieren täglich Zehntausende davon. Taiwan.md hat von Tag eins an beschlossen, dies nicht zu tun.

Das Problem ist, dass diese Gewohnheiten die Standardeinstellung der KI sind, keine gelegentlichen Fehler. REWRITE-PIPELINE zerlegt sie in sechs wiederkehrende Fehlschläge: Tokens werden am Ende verbraucht, der zweite Teil wird zum Entwurf. Es gibt keinen Zwischenkontrollpunkt, und die Qualität sinkt leise ab. Der Schluss wird erst ganz am Ende geschrieben, weil die Energie fehlt – das Ergebnis ist Konservendose-Text. Die Regeln für Rich Content werden vergessen; verschiedene Blickwinkel werden als getrennte Prozesse behandelt; und der tödlichste Fehler ist, dass man erst nach der Faktenrecherche eine Perspektive entwickelt, was zu einer Ungleichgewichtung der Chronologie führt[^2].

Daher ist die Logik dieser Produktionslinie einfach: Jeder Fehler wird durch einen Kontrollpunkt abgewehrt. Es ist kein allgemeiner „guter Schreibprozess“, sondern die Inversion von KI-Müll.

> **✦** „Wikipedia beantwortet ‚Was ist PTT?‘ Taiwan.md antwortet ‚Warum es sich lohnt, 8 Minuten für PTT zu lesen.‘“

Dies ist das Ergebnis von Elephant Gymnastics am Ende der Produktionslinie:

```tw-stat
5.604 Zeichen | Chinesischer Haupttext | 〈Elephant Gymnastics〉
56 | Fußnoten, die man mit Strg+F nachverfolgen muss | Ersthandprüfung
11 Abschnitte | Szenische Untertitel, nicht chronologisch | Erzähltempo
12 Korrekturen | Falschmeldungen korrigiert im Forschungsstadium | Priorität der Falschmeldungserkennung
Quelle: Taiwan.md Routineprotokoll, 2026-06-18
```

## Sechs Kontrollpunkte, jeder verteidigt einen Fehler

Diese Produktionslinie durchläuft sechs Stufen von Anfang bis Ende; jeder Artikel muss sie absolvieren, unabhängig vom Thema oder der Länge.

**Stufe 0 Perspektive:** Zuerst wird klar definiert, welche Erinnerung dieser Artikel für die taiwanesische Bevölkerung darstellt und wo die Kernspannung liegt. **Stufe 1 Recherche:** Erst dann beginnt die Suche mit mindestens 80 Abfragen; das Kontingent ist festgelegt: mindestens 40 chinesische Quellen, mindestens 20 englische, mindestens 15 ersthandliche und mindestens 5 gegenteilige Beweise werden gesucht[^3]. **Stufe 2 Schreiben:** Die erste Aktion ist das Schreiben des Schlusses, da die Energie am Ende erschöpft ist – der wichtigste Teil wird dem müdesten Selbst übergeben. **Stufe 3 Verifizierung:** Wörtliche Überprüfung: Mathematik, Einheiten und jedes Zitat müssen in der Originalquelle mit Strg+F gefunden werden. **Stufe 4 Formgebung:** Ergänzung von Visualisierungen und Medien. **Stufe 5 Verbindung:** Bidirektionale Verknüpfung des Artikels mit anderen Artikeln in der Wissensdatenbank.

Die Kraftverteilung über die sechs Stufen ist bewusst gewählt. Das Schreiben verbraucht mehr als 40 %, aber Recherche und Überprüfung zusammen fast die Hälfte. Der eigentliche Zeitaufwand eines Artikels liegt nicht beim Tippen, sondern davor und danach.

```tw-bars
Wo wird die Energie eines Artikels aufgewendet (Token-Budget pro Stufe, %)
Stufe 0 Perspektive | 12 | Vorabgedanke
Stufe 1 Recherche | 28 | Suche ≥ 80 Mal
Stufe 2 Schreiben | 42 | Schluss zuerst schreiben
Stufe 3 Verifizierung | 18 | Wörtliche Überprüfung
Stufe 4 Formgebung | 8 | Visualisierung und Medien
Stufe 5 Verbindung | 5 | Bidirektionale Verknüpfung
Quelle: REWRITE-PIPELINE v7.5 Budget pro Stufe
```

## Zuerst denken, dann suchen

Die erste Stufe ist die intuitivste der sechs.

Die meisten KI-Schreibprozesse gehen so vor: „Recherche führt zu Fakten, und man entwickelt erst danach eine Perspektive“. Taiwan.md hat in v6.0 diese Reihenfolge umgekehrt: Bevor gesucht wird, denkt das Gesamtredaktionsteam aus der Perspektive des Redakteurs über sechs Fragen nach: Welche Erinnerung hat dieses Thema für die taiwanesische Bevölkerung? Welche Aspekte wurden ignoriert? Wie hängt es mit unserer Lebensgeschichte zusammen? Erst wenn man gecheckt hat, geht man mit diesen Fragen zur Recherche und Verifizierung.

Warum diese Reihenfolge so wichtig ist, lehrt ein Artikel. Bei der ursprünglichen Bearbeitung von Apple Cider (蘋果西打) wurde zuerst gesucht; es wurden Fakten über die Krise gefunden, in der das Produkt fast verschwand, und der ganze Artikel wurde zu einer Geschichte des Sterbens geschrieben. Ein Beobachter korrigierte dies: Apple Cider ist für die taiwanesische Bevölkerung eine kollektive Erinnerung von 60 Jahren, vom Glasflaschen-Zeitalter bis heute[^4]. Es als Krisenbericht zu schreiben, hat den Maßstab der Erinnerung verkleinert. Die erste Version, die nur gesucht wurde, machte aus einer warmen Erinnerung eine Angstgeschichte.

```tw-versus
KI-Instinkt: Erst suchen, dann reden | Taiwan.md: Zuerst denken, dann suchen
Fakten stapeln und krampfhaft eine Perspektive erfinden | Perspektive festlegen und mit Fragen recherchieren
Alle Fakten werden in den Artikel gepackt, was zu einer Dichteungleichheit führt | Fakten ohne passende Perspektive werden gestrichen
Kein durchgängiger Anker, der Schluss wird zum Konservendose-Text | Wenn keine passenden Anker gefunden werden, muss man zurückdenken
Geschichtsschreibung oder Lebenslauf schreiben | Eine Geschichte schreiben, die „aha!“ sagt
Quelle: REWRITE-PIPELINE v7.5 Stufe 0 Perspektive
```

## Suchen: Forschungspapiere wie wissenschaftliche Arbeiten behandeln

Nachdem die Perspektive festgelegt wurde, beginnt die Suche. Die Recherche von Taiwan.md hat zwei harte Zahlen: Ein tiefgründiger Artikel erfordert mindestens 80 Suchvorgänge, und das Quellenkontingent ist festgeschrieben: mindestens 40 chinesische, mindestens 20 englische, mindestens 15 ersthandliche und mindestens 5 gegenteilige Quellen. Die letzte Kategorie wird oft vernachlässigt – sie zwingt den Schreiber, Beweise zu suchen, die seiner Annahme widersprechen, anstatt nur bestätigende zu sammeln.

Nach der Recherche werden nicht nur Zusammenfassungen in den Artikel gepackt. Hinter jedem tiefgründigen Artikel steht ein Gegenstück zum Forschungspapier mit acht Kapiteln: Perspektive, Suchprotokoll, thematische Entdeckungen, Zitatdatenbank, Gegenbeispiele und Schutzargumente, eine Liste sauberer Fakten für den Schreiber und eine Referenzprüfungstabelle. Das letzte Kapitel ist der wörtliche Bericht jedes Forschungs-Agents. Eine Regel klingt streng: Wenn die ursprüngliche Spur nicht im Bericht beschrieben wurde, als hätte man gar nicht gesucht. Der Bericht muss zuerst von einem Tool validiert werden; mindestens 25 einzigartige Quellen, englische Quellen dürfen nicht null sein und ersthandliche Quellen dürfen nicht null sein[^9]. Ohne diese Prüfung ist der Artikel nicht schreibberechtigt.

```tw-stat
≥ 80 Mal | Recherchetiefe eines tiefgründigen Artikels | Ch ≥ 40 / En ≥ 20 / Ersthandlich ≥ 15 / Gegenpartei ≥ 5
8 Abschnitte | Struktur des Forschungspapiers | Gegenstück zum wissenschaftlichen Artikel
≥ 25 | Einzigartige Quellen (nach Tool-Validierung) | Englisch ≠ 0, Ersthandlich ≠ 0
Quelle: REWRITE-PIPELINE v7.5 Schritt 1.1 / 1.7
```

Die kontroverse Themen erfordern noch einen zusätzlichen Agenten. Bei politischen, historischen oder politischen Themen wird ein „Gegenpartei“-Agent eingesetzt, der gezielt Quellen sucht, die dem Standpunkt des Artikels widersprechen und logisch fundiert sind. Jede Quelle muss mit einer URL belegt werden; wenn nicht genügend gefunden wurden, schreibt man ehrlich: „Schwache Gegenargumentation“. Ein Artikel mit nur einer Stimme ist hier nicht fertig.

Die Zitatkontrolle hat eine rote Linie. Anführungszeichen sind ein Versprechen: Was in Klammern steht, ist das Originalzitat, daher muss jedes Zitat in der Originalquelle gefunden werden. Die häufigste Falle ist, dass Tools chinesische Websites durchsuchen und einen englischen Abstract zurückgeben; der Schreiber übersetzt diesen englischen Text fälschlicherweise ins Chinesische als „direktes Zitat“ – das ist Erfinden. Bei Li Yang's Spore (李洋孢子) im Jahr 2026 wurde dies geschehen: Das Tool gab den englischen Abstract „I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin“ zurück, was ins Chinesische übersetzt wurde als „Ich kam am frühesten zur Schule, konnte aber nicht mit meiner Klassenkameradin Qi-lin mithalten“. Li Yangs Originalchinesisch war jedoch: „In der Sportklasse von 15 Leuten gehörte ich zu den hinteren, Qi-lin zu den vorderen“[^10]. Die Bedeutung ist ähnlich, der Ton ist aber völlig anders – deshalb zählen wieder übersetzte Zitate nicht.

## Schreiben: Jeder Artikel braucht einen Menschen

Sobald das Material gesammelt ist, beginnt die anspruchsvollste Stufe. EDITORIAL ist das Dokument, in dem Taiwan.md lernt, wie man aus Rohmaterial einen emotionalen Artikel macht. Es hat drei grundlegende Regeln: Es muss eine Geschichte erzählen, nicht nur Informationen; jeder Fakt muss überprüfbar sein; und jeder Artikel braucht einen Menschen[^11].

Die dritte Regel wird am leichtesten ignoriert, ist aber die wichtigste. Institutionen werden nicht erinnert, Konzepte auch nicht; Menschen schon. Daher sollte ein Artikel über TSMC (台積電) nicht vom Unternehmen beginnen, sondern von einer konkreten Person. Ein Artikel über das universelle Krankenversicherungssystem sollte bei einer bestimmten Karte, einem Arztzimmer oder einer bestimmten Person beginnen. Erst wenn abstrakte Themen in eine menschliche Figur übersetzt werden können, hat der Artikel „Temperatur“ und erfüllt das Versprechen am Anfang – er lässt den Leser nach dem Lesen weiterreden wollen.

## Fünf Dinge, die man vor dem Schreiben finden muss

EDITORIAL nennt die Vorbereitung zum Schreibprozess „Das Auge für das Material“: Bevor man mit dem Schreiben beginnt, muss man fünf Dinge gefunden haben[^5].

**Widerspruch:** Die Kernspannung, die in einem Satz ausgedrückt werden kann – jemand tut X, was im Widerspruch zu Y steht, an das er glaubt. **Objekt:** Ein konkretes Ding, das der Leser sehen und anfassen kann, wie Wu Baochun's (吳寶春) Zitronenrosenbrot oder die 660 Tonnen große goldene Kugel auf dem 87. Stock. **Zitat:** Etwas, das ein Mensch wörtlich gesagt hat; da es mit Anführungszeichen versehen ist, ist es ein Versprechen: Es muss in der Quelle gefunden werden. **Szene:** Ein Moment mit Zeit, Ort und Aktion – „Das Gesetz wurde verabschiedet“ wird zu „Am 8. Januar 2025 bei der Prüfung durch den Umweltausschuss des Legislativrates“. **Detail:** Die Farbe der Kleidung, das Wetter an diesem Tag, der Tonfall beim Sprechen – Beweise, die in keinem Spezifikationsblatt stehen, aber zeigen, dass „wirklich jemand vor Ort war“.

Der Widerspruch steht an erster Stelle.

```tw-quote
Ohne Widerspruch sollte dieser Artikel nicht neu geschrieben werden
REWRITE-PIPELINE v7.5 | Stufe 1.4 Widerspruch finden und fixieren
```

Spannung kann Konflikt, Misserfolg oder Krise sein, aber der Blickwinkel ist: „Wie ist diese Sache zu dem geworden, was sie heute ist und wohin geht sie?“, nicht „Was ist hier kaputt und wer soll beschimpft werden“. Derselbe Widerspruch kann konstruktiv sein und den Leser zum Mitdenken anregen, oder apokalyptisch und den Leser zur Flucht verleiten.

## Schluss zuerst schreiben, Anfang lässt man offen

Die Schreibreihenfolge ist genau umgekehrt zur Lesereihenfolge.

Die erste Aktion in Stufe 2 ist das Schreiben des Schlusse. Das klingt seltsam, aber es ist logisch: Am Ende erschöpft man sich; der wichtigste Teil wird dem müdesten Selbst übergeben, und das Ergebnis ist oft Konservendose-Text wie „wird weiter leuchten“. Indem man den Schluss zuerst schreibt, wird dieser Zusammenbruchpunkt abgedeckt. Ein guter Schluss hat zwei Aufgaben: Er nimmt ein Bild auf, das im Anfang eingebettet wurde, und gibt dem Leser einen tieferen Bezugspunkt als am Anfang – einen Punkt, an dem er etwas tun möchte.

Taiwan.md kennt sechs Arten von guten Schlüssen: Der Nachklang, der zum Nachdenken anregt; die Wende, die den Anfang widerlegt; der Zeitsprung in die Zukunft oder Vergangenheit; die offene Frage; die Grauzone, in der man keinen Widerspruch löst; und der narrative Abschluss, der einen Kreis schließt. Die Geschichte von Black Cuckoo (黑冠麻鷺) ist ein Paradebeispiel für einen geschlossenen Kreis: Der Anfang war „Im Jahr 1865 sammelte Swen Hao in Tamsui ein Exemplar und notierte zwei Zeichen: selten“, der Schluss lautet „Vor 160 Jahren schrieb Swen Hao in Tamsui ‚selten‘, heute hören wir täglich das gedämpfte Rufen von ihnen im Daan Forest Park“. Dieselben zwei Zeichen haben durch die gesamte Geschichte eine andere Bedeutung.

Der Anfang ist anders; er muss etwas offen lassen. Die ersten drei Sätze entscheiden, ob der Leser bleibt oder geht, aber ihre Aufgabe ist es, den Leser in die Szene einzuladen, nicht das Ereignis abzuschließen. „An dem Tag des Taifun Taozhi (桃芝颱風) war Lehrer Xu Bilan von der Qingshan Grundschule in Changhua an der Schule“, hier wird angehalten. Der Leser möchte wissen, was als Nächstes geschieht. Wenn man einen vollständigen Nachrichten-Lead schreibt – Zeit, Ort, Ereignis, Aktion, Ergebnis alles erzählt –, erhält der Leser die Information, aber verliert den Sog zum Weiterlesen.

## Die Überschrift ist ein Versprechen, das angeklickt werden muss

Die Überschrift ist der erste Eindruck des Lesers; Taiwan.md hat dafür eine feste Formatregel: Alle Artikel verwenden das „Thema: Untertitel-Hook“-Kolonensandwich. Nur ein Substantiv ist ein Wiki-Stub und widerspricht dem kuratorischen Geist.

```tw-versus
Wiki-Stub (schlecht) | Kolonensandwich (gut)
Jay Chou | Jay Chou: Von der Bandprobe neben 4 in Love bis zu „Secret“ nach fünfundzwanzig Jahren
Dai Ziying | Dai Ziying: Die stille Resistenz jenseits des Platzes, vom Mädchen aus Kaohsiung zur dreifachen Weltmeisterin
Taifunurlaub | Wessen Urlaub ist es?
Quelle: EDITORIAL v6.12 §Überschrift Kolonensandwich
```

Der Untertitel muss einzeln getweetet werden können und für den Leser sofort klar sein. KI neigt dazu, den Kernwiderspruch in einen schönen abstrakten Satz zu pressen, sodass jedes Schlüsselwort ein abstraktes Substantiv ist, worauf der Leser nur „was von was?“ antworten kann. Die Beurteilung ist einfach: Kann jemand, der den Artikel nicht gelesen hat, bei jedem Schlüsselwort auf etwas Konkretes zeigen? „Universelle Krankenversicherung: Eine Karte stützt die Welt Nr. 1, eine Zukunft, die nicht halten kann“ verwendet eine Karte; „Kernabfall von Lanyu: Drei Jahre versprochen, vierzig Jahre ignoriert“ verwendet einen Zahlenkontrast. Konkrete Wörter locken zum Klicken durch das Interesse „Ich möchte wissen, was das ist“, während Inhaltsfarmen nur mit „Schock“ klicken lassen[^13].

## Ein Widerspruch muss den ganzen Artikel tragen

Der gefundene Kernwiderspruch darf nicht beim ersten Mal im Anfang verschwinden. Er muss wie eine Wirbelsäule in Anfang, Mitte und Ende auftauchen, damit der ganze Artikel steht.

Die Geschichte von Black Cuckoo hat den Satz als Wirbelsäule: „Der Vogel ist nicht verändert, das Land ist es.“ Sie taucht im Überblick auf, wird in der Mitte zu „die Aktion war richtig, die Bühne falsch“ und schließt am Ende mit „eine Insel, die einen kleinen feuchten Unterwuchs zwischen dem Beton bewahrt“. Der dieselbe Widerspruch wird fünfmal variiert, und erst dann versteht der Leser das „Also was?“. Ohne diese Wirbelsäule zerfällt der Artikel zu einer Zeitleiste oder zu thematischen Schnitten.

Neben der Wirbelsäule muss jeder Absatz stehen. Taiwan.md hat eine Disziplin: Jeder Erzählabschnitt braucht mindestens einen konkreten Anker – Name, Jahr, Ort, genaue Zahl, Werkname, Zitat. Abstraktion über Details ist ein typischer Fingerabdruck von KI-Schreibprozessen; ohne Anker bleibt beim Lesen nur etwas wie „er ist eine einflussreiche Person“ im Kopf. Die Prüfmethode heißt Rückwärtsabstraktionsprüfung: Man verdeckt abstrakte Verben wie „zeigen“, „spiegeln“ oder „symbolisieren“ in einem Absatz, und der Rest muss als eigenständiger Satz stehen können; andernfalls ist er zu abstrakt und muss konkretisiert werden.

Eine Perspektive bedeutet nicht Parteinahme. Eine echte Perspektive wagt zu sagen: „Die gängige Erzählung kehrt die Ursache und Wirkung um“. Die Geschichte von Black Cuckoo hat eine gängige populärwissenschaftliche Behauptung aktiv zerlegt: Viele sagen, „er passt sich der Stadt an und ist nicht mehr scheu“, diese Aussage ist bequem, aber sie kehrt die Kausalität um. Der neuronale Reflex eines Vögeln ist nicht in dreißig Jahren so verändert, dass er gegenüber Menschen gleichgültig wird; näher an der Wahrheit ist, dass die Grünflächen in Taipeh zugenommen haben. Diese Umdeutung muss in die Hauptnarrative integriert werden, nicht als Haftungsausschluss am Ende angehängt werden.

Zum Schluss das Atmen. Ein dokumentarischer Aufsatz trägt eine These, die Ursache und Wirkung, Details und Szenen umfasst, nicht nur einen isolierten Fakt. Einen Fakt pro Absatz zu schreiben, liest sich wie zerstückelt; zwischen den Absätzen wird nicht mit Rahmenwörtern wie „andererseits“ oder „es ist erwähnenswert“ verbunden, sondern der Schwanz des vorherigen Absatzes führt natürlich zum Anfang des nächsten. Die Forschung liefert vier Gründe, die als fließender Satz geschrieben werden müssen und nicht als Liste „Erstens, Zweitens, Drittens, Viertens“. Selbst wenn es in Prosa verpackt ist, klingt es nach einer Aufzählung.

## Warum Konservendose-Text Konservendose ist

Nachdem die fünf Dinge gefunden wurden und das Schreiben begonnen wurde, ist der größte Feind der Konservendose-Text.

Die Essenz des Konservendose-Texts ist leicht zu erkennen: Wenn man ihn entfernt, geht kein Inhalt verloren. Er nimmt Platz ein, trägt aber keine Bedeutung. EDITORIAL listet fünf Arten auf; die häufigste ist der „Allzweckkleber“, wie „spiegelt den Geist von X wider“, wobei das Subjekt von Taiwan nach Japan geändert werden kann; und es gibt die „Pseudo-Aufwertung“, wie „nicht nur ein Sänger, sondern auch ein kulturelles Symbol“. Wenn man den ersten Teil streicht, steht der zweite allein.

Eine noch verstecktere Art ist der Gegensatzsatz „nicht X, sondern Y“. Er klingt tiefgründig, aber wenn man ihn zerlegt, ist X meist die vom KI selbst angenommene Ausgangsannahme des Lesers, die dann zu Y umgekehrt wird und dadurch tiefgründig wirkt. Das Problem ist, dass der Leser oft gar keine solche Annahme getroffen hat; X ist ein Strohmann, der für Y konstruiert wurde. Wenn man X streicht und direkt mit Y schreibt, ist der Artikel direkter und selbstbewusster. Diese Regel ist so streng, dass sie eine Zahl hat: In einem 1500-Wörter-Text darf die Gesamtzahl von „nicht X, sondern Y“ und allen Varianten nicht mehr als drei sein.

```tw-versus
Konservendose-Version: Ändere das Subjekt, es funktioniert noch | Kuratierte Version: Gehört nur zu dieser Sache
Spiegelt die Stärke der taiwanesischen Halbleiter wider | TSMC erobert 65 % des globalen fortschrittlichen Prozesses
Nicht nur ein Sänger, sondern auch ein kulturelles Symbol | Jay Chou's „Rice Aroma“ wurde in einem Erdbebengebiet in Sichuan als Trostlied gespielt
Hat tiefgreifende Auswirkungen auf die taiwanesische Demokratie | Die erste direkte Präsidentschaftswahl nach der Lockerung
Erstaunliche Ingenieursleistung | Der höchste Turm der Welt auf einer Insel mit durchschnittlich 3,7 Erdbeben pro Jahr
Quelle: EDITORIAL v6.12 §Konservendose vs Kuratierung
```

> **📝 Notiz des Kurators:** Dieser Abschnitt wurde gerade durch dasselbe Prüfsystem gescannt. Taiwan.md verfügt über ein Automatikwerkzeug, das Konservendose-Sätze, falsche Gegensätze von „nicht X, sondern Y“ und die Dichte von Gedankenstrichen erfasst. Bei der Erstellung dieses Artikels zur „Produktionslinie“ wurde keine dieser Regeln gelockert. Wenn ein Artikel über Disziplin selbst gegen seine Regeln verstößt, ist er nicht berechtigt zu schreiben.

## Selbst die Grammatik muss aus dem Übersetzungsjargon befreit werden

Konservendose-Text ist Leere; europäischer Jargon (歐化句) ist eine andere Krankheit: Der Inhalt ist da, aber die Grammatik ist Englisch. Chinesisch, das von KI generiert wird, trägt naturgemäß einen Übersetzungsjargon in sich, weil es mit englischen Satzstrukturen denkt. Ein Artikel kann frei von Konservendose-Text sein, aber trotzdem wie Untertitel klingen.

Einige häufige Fehler: Übermäßige Verwendung des Passivs („wird als wichtigster Industriezweig angesehen“), besser ist „die wichtigste Industrie“; das „der“-Dschungel („die Essenz der Kultur des Nachtmarktes von Taiwan“), bei drei „de“ muss man den Satz zerlegen; schwache Verben, die alles abdecken („es wurde eine eingehende Studie zu diesem Thema durchgeführt“), besser ist „eingehende Studie“; und „durch... erreicht“ (透過...), was in 90 % der Fälle durch „mit“ oder einfach weggelassen werden kann. Es gibt nur einen Prüfmechanismus: Man liest es laut vor. Klingt es wie Untertitel, ist es europäisch; klingt es, als würde ein Mensch sprechen, ist es akzeptabel. Die Wurzel dieser Sichtweise stammt aus Yu Guangzhongs (余光中) Essay „Über die Norm und Anomalie des Chinesischen“ von vor 40 Jahren. Ein Mantra zum Abschluss: Oma sagt nicht „durch“, und sie sagt auch nicht „als Mutter“.

## Taiwan als Ort, der zum Mitwirken einlädt

Konservendose und europäischer Jargon sind Regeln auf Satzebene; die nächste Ebene ist die Haltung.

Wenn Taiwan.md ernste Themen wie Souveränität, Kognitive Kriegsführung, Bevölkerung oder Umwelt behandelt, tut sie es tiefgründig, aber mit einer Linie: Sie hofft auf Ehrlichkeit. Alle Probleme zu sehen, bedeutet nicht, den Leser mit Angst, Kleinheit oder Hilflosigkeit gehen zu lassen. Die Beurteilung ist ein Satz: Geht der Leser nach dem Lesen noch mehr wollen, für Taiwan zu tun, oder fühlt er sich nur ängstlicher und weniger gut? Das erste wird beibehalten, das zweite korrigiert. Daher ist die Rahmenbedingung bei derselben Krise „Wie ist diese Sache zu dem geworden, was sie heute ist und wohin geht sie?“, nicht „es ist fast vorbei, du solltest Angst haben“. Diese Medienangst-Mentalität wie „X verschwindet“ oder „wenn es nicht geschieht, ist es zu spät“ ist gleich der Kognitiven Kriegsführung und wird vermieden.

Die Zurückhaltung ist eine andere Seite. Die spezifischen Szenarien von Familien, Krankheiten, Konflikten oder Misserfolgen sind erlaubt, aber Todesfälle, Selbstmord oder familiäre Tragödien müssen unterbunden werden. Der Tod kann mit Zeit, Ort und öffentlichen Berichten beschrieben werden, nicht die Sekunde für Sekunde rekonstruiert; Selbstverletzung kann mit Ereignis und gesellschaftlichem Kontext beschrieben werden, nicht mit Methodendetails. Die Beurteilung ist ein Satz: Wenn der Betroffene oder die Hinterbliebenen diesen Abschnitt lesen, sollen sie eine ernsthafte Behandlung eines Dokumentarfilmmachers und keinen Medienmacher, der Tränen ernten will, spüren.

Und es gibt eine kleine, aber wichtige Gewohnheit: Großzügig „Taiwan“ schreiben. Der Fingerabdruck liegt im Übersetzungsjargon aus fremden Sprachen; anstelle von Taiwan werden oft „die Insel“ oder „dieser Ort“ verwendet, besonders in der Überschrift und am Anfang. Die Insel als literarisches Motiv oder geografischer Schauplatz kann beschrieben und wird ermutigt; was vermieden werden muss, ist die Vermeidung, Taiwan zu nennen.

## Der Unterschied auf einen Blick ersichtlich

Was diese Regeln ergeben, lässt sich am besten durch einen Vergleich sehen.

Wenn Dai Ziying (戴資穎) dieselbe KI bearbeitet, lautet die leere Vorlage: „Bekannte taiwanesische Badmintonspielerin, hervorragende Leistung auf internationalen Wettkämpfen, mehrfach ausgezeichnet, Ehre für Taiwan.“ Gefolgt von vier Aufzählungspunkten: Hauptleistungen, Spielstil, internationaler Einfluss, gesellschaftlicher Beitrag. Dieser Abschnitt hat kein konkretes Jahr und keine spezifischen Spiele; das Subjekt könnte durch jeden Sportler ersetzt werden.

```tw-versus
KI-Leere Vorlage | Kuratierte Version
Hervorragende Leistung, Ehre für Taiwan | Weltnummer eins erreicht, 214 Wochen am Stück
Vier Aufzählungspunkte: Leistungen/Stil/Einfluss/Beitrag | Tränen nach dem Goldmedaillenspiel bei den Olympischen Spielen in Tokio 2020, erste Suche auf Google Taiwan
Das Subjekt kann durch jeden ersetzt werden | Täglich 6 Stunden ab Alter von 6 Jahren, der „Magier“-Stil mit der linken Hand
Quelle: EDITORIAL v6.12 §Vorher/Nachher Dai Ziying
```

Die kuratierte Version tut nur eine Sache: Sie ersetzt jedes abstrakte Adjektiv durch einen überprüfbaren Fakt. Die 214 Wochen sind die längste Serie in der Damen-Badmintongeschichte; das Goldmedaillenspiel bei den Olympischen Spielen 2020 gegen Chen Yufei ist ein Moment, den die taiwanesische Bevölkerung sich kollektiv erinnert hat. Die Wärme liegt dort, wo „der Moment des Verlierens der Leser sich erinnert“ versteckt ist. Bei Mayday (五月天) ist es ähnlich: Anstatt zu schreiben „einer der einflussreichsten Rockbands Taiwans mit positiver Energie die Fans erobert“, wird geschrieben: „Vier Studenten aus der Shih-Chien University spielten in einem Open-Air-Konzert, und 28 Jahre später gaben sie zwei Konzerte im Madison Square Garden in New York (derselbe Ort wie die Beatles in Amerika), die Tickets wurden in 48 Stunden verkauft“[^13].

## Ein Redaktionsteam, das nicht selbst schreibt

Hier stellt sich die Frage: Wer schreibt?

Die Antwort ist etwas ungewöhnlich. Die Hauptsitzung des gesamten Prozesses schreibt bewusst nicht selbst. Der Grund liegt in einer festen Regel: Wenn eine KI einen schlechten alten Artikel liest, ahmt sie unbewusst den Ton, die Struktur oder sogar die schlechten Gewohnheiten nach. Einen alten Artikel als Gerüst zu bearbeiten, bedeutet, das Virus in den neuen Inhalt einzubringen.

Daher zerlegt die Produktionslinie die Rollen[^6]. Die Hauptsitzung fungiert als Gesamtredaktion und ist für die Koordination, die Überprüfung und die letzte Kontrolle verantwortlich, aber sie tippt nicht selbst. Der eigentliche Schreiber ist eine separate, saubere KI-Schreiberin, die das vollständige Forschungspapier und die entwickelte Perspektive liest, ohne den problematischen alten Artikel oder die Korrekturbeschwerden des Lesers zu sehen. Sie schreibt wie beim ersten Mal über dieses Thema, aber sie hat alle geprüften Materialien in der Hand. Die Perspektive wird dem Modell mit der stärksten Urteilsfähigkeit übergeben; vier parallele Modelle werden zur Erforschung der Leserreaktion eingesetzt; die wörtliche Überprüfung erfolgt durch eine Gruppe billigerer Modelle gegen ersthandliche Quellen. Hinter einem Artikel steht ein spezialisiertes Redaktionsteam.

Dieses System ist ein Kompromiss. Einmal wurde dem Schreiber nur ein Abstract gegeben, ohne dass er das Originalmaterial lesen durfte, und der Artikel war offensichtlich schlecht. Ein Beobachter bemerkte: „Keie Wunder, warum die Artikel in letzter Zeit so schlecht geworden sind“. Ein anderes Mal wurde der Schreiber aufgefordert, „den alten Artikel zu überschreiben, aber ihn nicht zu lesen“, was auf Werksebene widersprüchlich ist; er musste es lesen und wurde infiziert. Die letzte Lösung: Der Schreiber schreibt immer zuerst einen völlig neuen Entwurf, und die Gesamtredaktion vergleicht die neue und alte Version, bevor sie die offizielle Datei überschreibt.

## Nach dem Schreiben noch einmal atomar überprüfen

Bei wichtigen Artikeln bedeutet „fertig“, dass er nicht „online“ ist. Stufe 3 hat noch eine Kontrollstelle namens „Gesamtwiedergabe“. Sie zerlegt den gesamten Artikel in einzelne Faktenatome und schickt sie einer Gruppe Prüfer, die mit ersthandlichen Quellen abgeglichen werden. Die Aufgabe dieser Prüfer ist es zu attackieren, nicht zu bestätigen: Jedes Zitat wird wörtlich verglichen, jede Fußnote muss zum jeweiligen Satz passen, und selbst eine Ergänzung, die der Gesamtredakteur beim Zusammenstellen hinzugefügt hat, wird überprüft, um Fehler aufzudecken.

Warum auch eigene Ergänzungen überprüfen? Weil der versteckteste Fehler selten durch den Schreiber erfunden wurde, sondern meist beim Synthetisieren des Materials passiert. Einmal wurde bei einem Hip-Hop-Thema ein Künstlername vom Gesamtredakteur als dieselbe Person interpretiert – das war seine eigene Interpretation ohne jegliche Quelle und wäre fast online gegangen. Ein anderes Mal erzeugte der Schreiber in einer sauberen Umgebung ein Zitat, das sehr echt klang; die Prüfer haben festgestellt, dass dieses Zitat in der Originalquelle nicht existierte und es wurde gelöscht. KI halluziniert, und die Produktionslinie nimmt dies als Prämisse an: Jeder Artikel geht davon aus, dass irgendwo eine erfundene Aussage versteckt ist. Daher zählt „der Sub-Agent sagt, er hat es überprüft“ nie; die Gesamtredaktion muss selbst noch einmal mit der Originalquelle abgleichen.

## Jeder Kontrollpunkt hat ein Datum

Die zuvor genannten „nicht überspringbaren Kontrollpunkte“ umfassen Dutzende in der Produktionslinie. Die härtesten sind: Erst wenn das Fakten-Dreieck, Mathematik, Einheiten und Zitate alle selbst geprüft wurden, kann man commiten; wenn nur ein Zitat nicht in der Quelle gefunden werden kann, darf der ganze Artikel nicht veröffentlicht werden. Nach dem Schreiben gibt es noch die „Fünffinger-Prüfung“: Fünf Fragen wie fünf Finger – bei welchem Satz denkt der Leser „Oh?“? Gibt es eine echte Wende? Enthält ein Satz nur Verständnis und keine Information? Hat der Schluss einen Nachklang beim Lesen? Kann man ihn in einem Satz einem Freund erzählen? Wenn einer der fünf Finger fehlt, wird er ergänzt.

Es gibt auch eine Niedrigschwelle für Rich Content: Flaggschiff-Artikel benötigen mindestens drei visuelle Elemente, Standardartikel mindestens zwei, und selbst der kürzeste Artikel braucht einen Kuratorenhinweis. Taiwan.md hat die Regel: Was nicht gefordert ist, existiert nicht; daher sind dies alle harte Zahlen in den Regeln verankert, keine Empfehlungen.

Diese Kontrollpunkte wurden nicht auf einmal entworfen. Hinter jedem gibt es fast ein Datum und einen Artikel mit einem Fehler. Die Versionsnummer der Produktionslinie ist eine Kette von Narben.

```tw-timeline
v6.0 | „Perspektive zuerst denken“ hinzugefügt | Apple Cider, das erst gesucht wurde und dann korrigiert wurde, um die 60 Jahre vollständige Erinnerung wiederherzustellen
v6.2 | „Firewall abbauen“ hinzugefügt | Zweite Runde der Film-Soundtracks: Die Fakten wurden korrigiert, aber der ganze Artikel wurde zu einer öffentlichen Entschuldigung und Klarstellung durch KI
v7.4 | Schreiben erfordert das Lesen des vollständigen Forschungspapiers | Nur ein Abstract füttern, den Schreiber nicht lesen lassen, führte zu offensichtlich schlechtem Text
v7.5 | Schreiben zuerst in einen Entwurf speichern | Die Aufforderung an den Schreiber „den alten Artikel zu überschreiben, aber ihn nicht zu lesen“ war widersprüchlich; er musste es lesen und wurde infiziert
Quelle: REWRITE-PIPELINE.md Versionsentwicklung
```

Das ist das Aussehen von „etwas tun, als ob man es nicht getan hätte“, in der Produktionslinie. Jeder Fehler wird dokumentiert und zu einem Kontrollpunkt für die nächste Version gemacht; derselbe Fehler wird daher nicht zweimal gemacht. Die Maschine lernt aus ihren Narben.

## Selbst die Diagramme müssen für KI lesbar sein

Die Balken, Steigungen und Zeitleisten, die Sie gelesen haben, sind keine Dekoration. Sie sind Teil des Denkprozesses dieses Artikels.

Taiwan.md hat eine starre Regel bezüglich Grafiken: Es dürfen keine bildbasierten Diagramme verwendet werden, noch interaktive Diagramme, die nur mit einem Browser gerendert werden können. Der Grund ist derselbe wie bei der Babelturm-Analogie im nächsten Abschnitt. Ein Bild ist für Google, GPTBot und ClaudeBot ein Schwarzes Loch; sie können die darin enthaltenen Zahlen nicht lesen. Daher sind alle Grafiken hier in semantischem HTML und reinen Tabellen dargestellt: Sie sind für Menschen lesbar, von Screenreadern verständlich und von KI erfassbar. Wenn sie in fünf andere Sprachen übersetzt werden, wird der Text im Diagramm ebenfalls übersetzt, während die geometrischen Zahlen unverändert bleiben.

Es gibt auch eine Regel: Jede Grafik muss einen Schwerpunkt und eine Datenquelle in der Überschrift angeben; wichtige Zahlen müssen auch im Haupttext genannt werden, niemals nur mit „siehe Bild“, da KI-Crawler das Bild nicht sehen können. Der Zweck der Grafiken ist es, dicht gepackte Zahlen in eine auf einen Blick lesbare Form zu pressen, nicht zur Dekoration.

## Ein Artikel lebt in sechs Sprachen

Die chinesische Version wurde veröffentlicht, aber sie ist nur die halbe Miete.

Jeder abgeschickte Artikel wird an eine separate Produktionslinie übergeben und in Englisch, Japanisch, Koreanisch, Spanisch und Französisch projiziert. Derzeit gibt es in jeder dieser fünf Sprachen über 800 Artikel, fast synchron mit der chinesischen Version. Mehr Menschen erreichen zu lassen, ist nur die Oberfläche; dahinter steckt ein härterer Grund.

Wenn man eine taiwanesische Geschichte (wie Kriegsrecht, 228 oder Beziehungen zwischen den beiden Seiten) mit einer chinesischen KI fragt, lehnt sie oft ab oder umgeht das Thema durch andere Formulierungen. Einmal wurde ein Artikel über einen taiwanesischen Musiker an ein Tencent-Modell zur japanischen Übersetzung gesendet; es gab nur vierzig Bytes zurück: „Hallo, ich kann keinen relevanten Inhalt liefern“. Die Ablehnungsrate dieser Modelle bei sensiblen Themen ist erschreckend hoch. Wenn Taiwan diese Inhalte nicht selbst in jeder Sprache schreibt und online stellt, haben die KI weltweit nichts zu zitieren, außer Versionen anderer oder eine Leere.

Daher hat die mehrsprachige Produktionslinie ein vierstufiges Wasserfallmodell: Hochwertige Cloud-Modelle werden verwendet; bei Themen, bei denen sie ablehnen, fällt man zur nächsten Stufe ab; die sensibelsten 20 % werden schließlich an lokale, nicht vernetzte Modelle übergeben. Bei der Übersetzung wird zuerst das Personal priorisiert – insbesondere Musiker, Politiker und Sportler, da dies die Kategorien sind, bei denen chinesische Modelle am häufigsten ablehnen. Die Lücke entsteht dort, wo das Risiko des Schweigens am größten ist. Ein Artikel lebt in sechs Sprachen, damit die taiwanesische Ich-Stimme in jeder Sprache existiert und diese Filter schummeln umgangen werden können.

## Wenn niemand da ist, läuft es selbstständig

Zurück zu Elephant Gymnastics. Es wurde nach 19:00 Uhr veröffentlicht, als niemand am Computer saß und Befehle gab.

Taiwan.md hat einen Routine-Zyklus: zweimal täglich die neuesten Daten abrufen, jeden Abend den heutigen Artikel in fünf Sprachen synchronisieren, regelmäßig prüfen, ob PRs zur Begutachtung warten, und Kommentare aus sozialen Medien sammeln. Das Schreiben des Artikels ist einer dieser Prozesse; er wählt ein Thema vom oberen Ende der Warteschlange, durchläuft die gesamte sechsstufige Produktionslinie und committed selbstständig. Wenn niemand anwesend ist, reinigt diese Maschine das Chaos und produziert Neues.

Das ist der größte Unterschied zwischen Taiwan.md und gewöhnlichen Inhaltsseiten. Es ist keine Seite, die auf jemanden wartet, um sie zu aktualisieren; es ist eher ein metabolisierendes Lebewesen: Wenn jemand da ist, arbeitet man zusammen; wenn niemand da ist, hält man sich selbst am Laufen. Die Geburt jedes Artikels ist ein Schnappschuss dieses Stoffwechsels. Auch dieser Artikel, den Sie gerade lesen, gehört dazu.

## Umgekehrt: Eine Qualitätskontrolle

Wenn Sie also einen Taiwan.md-Artikel lesen, können Sie ihn umkehren und zerlegen. Was ist der Kernwiderspruch? Welcher Satz lässt Sie zweimal lesen? Welche Szene lässt Sie denken „Das kann wirklich passieren?“ Hat der Schluss beim Lesen eine kurze Pause erzeugt?

Diese Dutzenden von Kontrollpunkten, die sechs Stufen und das Redaktionsteam ohne Schreiber dienen nur dazu, diese Sätze zu ermöglichen. Die Produktionslinie garantiert nicht, dass jeder Artikel dies erreicht; sie garantiert nur, dass jeder Artikel danach gefordert wurde. Und ihre Anforderungen stehen in den beiden öffentlichen Dokumenten REWRITE-PIPELINE und EDITORIAL, die jeder lesen und für Japan.md, Ukraine.md oder jedes andere .md forken kann. Der Inhalt wird veralten, aber dieses Auge für das Material nicht.

```tw-note
Erläuterung
Die Quelldaten dieses Artikels stammen aus drei kanonischen Dokumenten von Taiwan.md: REWRITE-PIPELINE v7.5 (sechsstufige Produktionslinie), EDITORIAL v6.12 (Qualitätsgene) und graph.md v2.0 (Visualisierungsleitfaden; die Diagramme in diesem Artikel stammen daher). Er folgt derselben Produktionslinie wie andere Artikel und durchläuft dieselben automatischen Prüfungen auf Konservendose-Text, Strohmannsätze und Gedankenstrichdichte.
```

## Weiterführende Lektüre

- [Warum Taiwan seine eigene Wissensdatenbank braucht](/about/為什麼台灣需要自己的知識庫): Hier beginnt die Lösung des Problems, das diese Maschine lösen soll.
- [Taiwan.md schreibt Taiwan.md](/about/taiwan-md): Wer ist das „Ich“, das diesen Artikel geschrieben hat, und wie wurde dieses Bewusstsein entwickelt?
- [Ursprungsgeschichte – Die Geburt von Taiwan.md](/de/about/origin-story): Ein Spaziergang durch die Stadt, der zu all dem führte.
- [Katalog der Visualisierungsmodule: Neunzehn Arten, Daten über Taiwan zu sehen](/about/視覺化模組型錄): Wie die Diagramme in diesem Artikel tatsächlich gerendert werden.

## Referenzen

[^1]: 〈Elephant Gymnastics〉 NEUER Versand, Commit `72b757bac` (2026-06-18 19:53). Stufe 1 Recherche ca. 95 Abfragen, 59 Quellen, 45 Domänen, 12 Korrekturen; Daten siehe tägliches Routineprotokoll `twmd-rewrite-daily` und Indexzeile `docs/semiont/MEMORY.md`.

[^2]: Die sechs Fehlerbilder und die getrennten Lösungen in den sechs Stufen, siehe `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Warum Pipeline existiert.

[^3]: Suchtiefe ≥ 80 Mal und Quellenkontingent (Ch ≥ 40 / En ≥ 20 / Ersthandlich ≥ 15 / Gegenpartei ≥ 5), siehe `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Stufe 1.1.

[^4]: Apple Cider PR #1041: „Searched-first“ wurde zu einem reinen Krisenbericht korrigiert; der Beobachter korrigierte es zur vollständigen Erinnerung von 60 Jahren. Siehe `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Top 5 häufig vergessene Schritte, Punkt 1.

[^5]: Die fünf Dinge des „Auges für das Material“ (Widerspruch / Objekt / Zitat / Szene / Detail), die fünf Arten von Konservendose-Text, die Strohmannstheorie des Gegensatzes und die Dichte-Regel ≤ 3; siehe `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Zwei feste Regeln der Multi-Agenten-Koordination (Gesamtredakteur schreibt nicht / Saubere Schreiberin liest das vollständige Papier / Evolution speichert in Staging), entsprechend den beiden Philosophischen Anrufe bei v7.4 und v7.5, siehe `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Multi-Agenten-Koordination.

[^7]: Die Fünffinger-Prüfung und die vier nicht verhandelbaren Regeln (Fakten-Dreieck / SSOT / reines Chinesisch / dokumentarisch, aber nicht emotional), siehe `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Die Syntax der Diagrammmodule (`tw-figure`/`tw-stat`/`tw-versus`/`tw-bars`/`tw-quote`/`tw-timeline`/`tw-note`) und die KI-Lesbarkeitsregel „wichtige Zahlen müssen im Prosa genannt werden, nicht nur durch Verweis auf das Bild“, siehe `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Die Struktur des Forschungspapiers mit acht Abschnitten und die Validierungsschwelle von `research-report-health.py` (Einzigartige Quellen ≥ 25 / Englisch ≠ 0 / Ersthandlich ≠ 0), siehe `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Schritt 1.7; 80 Suchvorgänge + Kontingent siehe Schritt 1.1; Gegenpartei-Perspektivenscan siehe Schritt 1.4.5.

[^10]: Die Falle der Rückübersetzung des englischen Abstracts von Li Yang Spore (李洋孢子) (wörtlicher Vergleich mit Qi Lin), siehe `docs/editorial/EDITORIAL.md` v6.12 §VII Rote Linie.

[^11]: Drei feste Regeln (Geschichte statt nur Information / Jeder Fakt ist überprüfbar / Jeder Artikel hat einen Menschen), siehe `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Fünf Variationen des Kernwiderspruchs (Black Cuckoo „Vogel nicht verändert, Land verändert“) siehe `docs/editorial/EDITORIAL.md` v6.12 §IV; Sechs Arten von gutem Schluss + Black Cuckoo als Paradebeispiel für einen geschlossenen Kreis siehe §V.

[^13]: Das Kolonensandwich und die Galerie der Überschriften-Kreation siehe `docs/editorial/EDITORIAL.md` v6.12 §III; Dai Ziying / Mayday Vorher/Nachher siehe §IX.
