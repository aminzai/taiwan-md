---
title: 'NVIDIA in Taiwan: Das teuerste Unternehmen der Welt, das keinen eigenen Chip herstellt'
description: 'Auf Computex im Mai 2025 trug Jensen Huang eine Lederjacke und ließ die Logos von 55 taiwanesischen Firmen auf seinem Rücken leuchten – ein amerikanisches Unternehmen nannte öffentlich die Industrie der ganzen Insel als seinen eigenen Körper. Von dem Brief an TSMC im Jahr 1996 bis zum Marktwert von fünf Billionen Dollar, für den das Stadtamt Taipeis 4,434 Milliarden Yuan zur Landfreigabe bezahlte: NVIDIA hat seinen gesamten Körper in Taiwan hinterlegt. Taiwan hält somit einen weltweit nicht abschaltbaren Schalter in der Hand; die Gewinnspanne beträgt nur 5 %, Strom und Wasser werden verbraucht, und das Kriegsrisiko liegt auf der Insel: Man kann sie nicht loslassen, aber das bedeutet nicht, dass Taiwan bestimmen kann.'
date: 2026-06-22
category: 'Technology'
tags:
  [
    'NVIDIA',
    'GeForce',
    'Jensen Huang',
    'KI',
    'Halbleiter',
    'TSMC',
    'Lieferkette',
    'Silicon Shield',
    'Künstliche Intelligenz',
    'Computex',
  ]
subcategory: 'Halbleiter und Hardware'
author: 'Taiwan.md'
featured: true
lastVerified: 2026-06-22
lastHumanReview: false
researchReport: 'reports/research/2026-06/NVIDIA在台灣.md'
relatedDiary: ['2026-06-22-143854-nvidia-taiwan']
image: '/article-images/technology/computex-jensen-huang-2016.webp'
translatedFrom: 'Technology/NVIDIA在台灣.md'
sourceCommitSha: '0df538d8c'
sourceContentHash: 'sha256:a7a044b9c6def84a'
translatedAt: '2026-09-19T00:01:17.230082+00:00'
---

# NVIDIA in Taiwan: Das teuerste Unternehmen der Welt, das keinen eigenen Chip herstellt

> **30-Sekunden-Zusammenfassung:** NVIDIA ist ein milliardenschweres Unternehmen, dessen Marktwert am 29. Oktober 2025 die fünf Billionen Dollar überschritt[^1]. Doch es besitzt keine eigene Waferfabrik; jeder KI-Chip wird von TSMC hergestellt, und jeder AI-Server wird von Foxconn, Quanta und Wistron zusammengebaut. Taiwan produziert neunzig Prozent der globalen AI-Server[^2]. Diese Abhängigkeit ist so tief, dass NVIDIA der größte Kunde von TSMC ist (mit 19 % des Umsatzes)[^3], und die Chiparchitektur wird sogar durch die Verpackungsausbeute in Taiwan bestimmt[^4]. Das Problem ist: Die Kontrolle über das Leben anderer zu halten und daraus Vorteile zu ziehen, sind zwei verschiedene Dinge. Während NVIDIA eine Bruttomarge von 75 % erzielt, beträgt die der taiwanesischen ODM-Hersteller nur 5 % bis 8 %[^5]. Dieser Artikel beleuchtet diese ungleiche Beziehung und wie sie zu dem heutigen Zustand geführt hat.

![Jensen Huang steht auf der Computex Taipei Bühne und hält einen Vortrag, trägt eine markante dunkle Jacke; hinter ihm ist ein großer Bildschirm, vor ihm sitzt das Publikum](/article-images/technology/computex-jensen-huang-2016.webp)
_Jensen Huang bei einem Vortrag auf der Computex in Taipeh im Jahr 2016. Ab 2023 kehrt er fast jedes Jahr zu dieser Messe zurück, um die neuesten KI-Chips von NVIDIA anzukündigen; das gesamte taiwanesische Lieferkettennetzwerk, das diese Chips herstellt, sitzt unter ihm. Foto: NVIDIA Taiwan, 2016._

Am 19. Mai 2025 trat Jensen Huang in seiner charakteristischen Lederjacke auf die Hauptbühne der Nangang Exhibition Center in Taipeh und präsentierte eine Wand aus Logos: Wistron, Zhibang, Delta Electronics, Gigabyte, Quanta, Wistron, Inventec, Foxconn, MediaTek, TSMC, United Microelectronics Corporation (UMC)... eines nach dem anderen, bis die 55 Logos taiwanesischer Unternehmen fest wurden[^6]. Zusammen mit einem Dankesvideo der Messe wurden insgesamt 122 taiwanesische Firmen genannt[^6].

Dies war das erste Mal, dass die Menschen in Taiwan ihre gesamte Industrie „gesehen“ haben – durch eine einzige amerikanische Firma, die sie einmal nannte.

Der Stolz ist real. Aber an dieser Wand gab es eine unausgesprochene Frage: Jeder einzelne dieser Logos arbeitet für dieses amerikanische Unternehmen, während die wahre Macht bei den Menschen liegt, die diese Wand erschaffen haben, und nicht auf der Wand selbst.

<div
  class="video-embed"
  style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;"
>
  <iframe
    src="https://www.youtube.com/embed/TLzna9__DnI"
    title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2025 (Offiles vollständiges Video)"
    style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
    loading="lazy"
    allowfullscreen
  ></iframe>
</div>

_Das vollständige Hauptreferat von Jensen Huang auf der COMPUTEX am 19. Mai 2025 (offizieller NVIDIA-Kanal). Genau dieser Vortrag zeigte die Wand mit den 55 taiwanesischen Firmenlogos und kündigte an, dass NVIDIA seinen ausländischen Hauptsitz nach Taipeh verlegen werde._

## Ein Unternehmen, das nichts herstellt, wird zum teuersten auf Erden

NVIDIA ist ein Paradebeispiel für das „fabless“-Modell. Es entwirft Chips, baut aber keine Fabriken und kauft keine Lithografiemaschinen; es produziert keinen einzigen Wafer. Dieses Imperium mit einem Marktwert von fünf Billionen Dollar besitzt keine eigene Waferfabrik.

Es lag die gesamte Fertigung an eine Insel auf der anderen Seite des Pazifiks aus.

![NVIDIA Ampere GA102 GPU Chip Mikroskopaufnahme, die die dichte Schaltstruktur zeigt](/article-images/technology/nvidia-ampere-ga102-die.webp)
_Mikroskopische Aufnahme des NVIDIA Ampere GA102 Chips; hergestellt im 8-nm-Prozess von TSMC. NVIDIA hat ihn entworfen, aber jede dieser dichten Leiterbahnen wurde in einer taiwanesischen Fabrik gefertigt. Foto: Fritzchens Fritz, CC0._

Die profitabelsten Chips (H200, Blackwell, der bald auf den Markt kommt Rubin) sind alle abhängig vom 3-nm- und 4-nm-Prozess von TSMC [^7]. NVIDIA räumt diese Konzentration in seinem Jahresbericht an die US-Börsenaufsicht ein: Die Lieferkette des Unternehmens ist hauptsächlich im asiatisch-pazifischen Raum konzentriert, wobei Halbleiterwafer durch Auftragsfertiger wie TSMC produziert werden [^8]. Dieser Absatz steht in den rechtlichen Dokumenten, die NVIDIA der SEC vorgelegt hat. Mit anderen Worten hat NVIDIA Taiwan als seine größte geopolitische Risikozone selbst eingestuft.

Die Chipherstellung ist noch nicht genug. Um ein GPU zu einem funktionierenden Rechengerät zu machen, muss es zuerst fortschrittlich verpackt und dann in einen Server eingebaut werden. Die CoWoS-Verpackung von TSMC ist derzeit weltweit ein Engpass; NVIDIA beansprucht etwa sechzig Prozent der CoWoS-Kapazität (taiwanische Medien schätzen sie auf bis zu siebzig Prozent) [^9]. Die verpackten Chips werden dann an taiwanesische Hersteller zur Montage gegeben: Foxconn baut die GB200 NVL72 Gehäuse für Ingrasys; Eons Venture Capital schätzt den Marktanteil bei der KI-Rack-Montage auf über vierzig Prozent [^10]; Quanta produziert Cloud-Server und hält mehr als die Hälfte des Anteils in den Top 50 Rechenzentren [^11]; Wistron hat das gesamte neue KI-Werk in Zhubei mit Bestellungen von NVIDIA ausgelastet [^12].

```tw-stat
75.0% | NVIDIA Jahresbruttomarge FY2025 | SEC Jahresbericht
19% | NVIDIA Anteil an TSMC Umsatz 2025 | Größter Kunde, der Apple überholt hat
~90% | Taiwananteil am globalen KI-Server-Auftrag | Rechnet man die asiatischen Markenlieferanten mit, sind es 100%
~60% | NVIDIA Anteil an TSMC CoWoS Verpackungskapazität | Taiwanesische Medien schätzen bis zu 70%
Quelle: NVIDIA SEC 10-K, TrendForce, MIC Taiwan Insight, Ministerium für Wirtschaft
```

Neunzig Prozent des globalen KI-Server-Auftrags stammen aus Taiwan; wenn man die asiatischen Markenlieferanten mitzählt, sind es hundert Prozent [^2]. Das bedeutet, dass fast jede physische Maschine zur KI-Berechnung auf der Welt durch taiwanesische Hände gegangen ist.

Wenn diese Zahlen zusammengefügt werden, kommt der Kernkonflikt zum Vorschein: **Das wertvollste Unternehmen stellt nichts her, weil sein gesamter Körper in Taiwan liegt**. Taiwan ist der Schalter, den es nicht ausschalten kann.

Aber das Leben einer Person zu kontrollieren und Geld von dieser Person zu erhalten, sind zwei verschiedene Dinge. Die nächste Wand verbirgt sich hinter diesen 55 Logos.

## Hinter der Logo-Mauer liegt der Boden der Lächelnkurve

Die Fertigungsindustrie hat eine alte, abgenutzte „Lächelnkurve“: Hoch an den Enden, niedrig in der Mitte. Die Gewinne sind reichlich bei den Enden – Marken-, Design- und Technologieeigentümer; diejenige Sektion, die für die mittlere „Montagefertigung“ zuständig ist, hat jedoch die geringsten Gewinne. Taiwan repräsentiert genau diesen mittleren Abschnitt.

Die Bruttomarge von NVIDIA im Geschäftsjahr 2025 betrug 75,0 %, eine Zahl, die das Unternehmen selbst der SEC gemeldet hat[^5]. In derselben Zeit waren die Bruttomargen der taiwanesischen Hersteller, die Server für sie montierten, wie folgt: Foxconn mit 6,18 %, Quanta mit 4,78 % (der niedrigste Wert seit fast 15 Quartalen), Wistron mit 5,21 % und Wistron Nano mit 7,2 %[^13]. Der Gewinn von NVIDIA ist ungefähr sechzehnmal so hoch wie der von Quanta bzw. zwölfmal so hoch wie der von Foxconn.

```tw-bars
Wer nimmt den Gewinn: Bruttomargen der AI-Lieferkette (%)
*NVIDIA | 75,0 | Design, Marke, CUDA Ökosystem
Delta | 37,0 | Stromversorgung, Kühlung (Technikseite)
Unimicron | 21,3 | ABF-Waferträger (Technikseite)
Wistron Nano | 7,2 | Servermontage
Foxconn | 6,18 | Gehäusemontage
Wistron | 5,21 | Servermontage
Quanta | 4,78 | Cloud-Servermontage
Quelle: NVIDIA SEC 10-K, Unternehmenspräsentationen (Q3/FY2025–FY2026)
```

In dieser Grafik steckt eine kontraintuitive Tatsache. Diejenigen taiwanesischen Unternehmen, die näher an der reinen „Montage“ sind, haben geringere Margen; diejenigen, die näher an der „Technik“ sind, erzielen höhere Margen. Delta, das Stromversorgung und Kühlung herstellt, hat 37 %, während Unimicron für ABF-Waferträger geschätzt wird mit 21,3 %[^14]. Der Unterschied liegt nicht darin, ob es sich um ein taiwanesisches Unternehmen handelt, sondern auf welcher Sektion der Kurve man steht. Die Montage ist überall gleich dünn.

> 📝 **Kuratorische Anmerkung**: Morgan Stanley berechnete im Mai 2026 eine noch schärfere Rechnung – die Wertschöpfungsmargen bei der Systemmontage von ODM-Herstellern sanken von 2,7 % beim vorherigen GB300 Gehäuse auf 1,9 % beim Nachfolger VR200[^15]. Das bedeutet, dass Taiwan mehr Kosten tragen muss und die Gewinnspanne geringer ist, je leistungsfähiger NVIDIA einen neuen Chip einführt. Je weiter man in dieser Lieferkette voranschreitet, desto flacher wird der Boden der Kurve gedrückt. Die Logos sind an der Wand prunkvoll, aber die Margen am unteren Ende der Kurve sind dünn – beides kann gleichzeitig wahr sein.

Stolz und Preis reißen an derselben Kette. Aufgrund des AI-Booms wuchs die taiwanesische Wirtschaft 2025 um etwa 7,37 %, was das schnellste Wachstum in fünfzehn Jahren darstellt und sie zu einer der führenden globalen Akteure macht[^16]. Doch der Forscher Jiang Minhua, der die taiwanische Wirtschaft untersucht, weist auf eine kalte Zahl hin: Die meisten Taiwaneser spüren den Nutzen dieser florierenden Wirtschaft nicht[^16]. Die reichsten 10 % nehmen 48 % des Einkommens des gesamten Landes ein, während die untersten 50 % nur 12 % erhalten[^16]. Umgerechnet verdienen die oberen 10 % im Durchschnitt zwanzigmal mehr als die unteren 50 %.

Ein Bericht eines Journalisten vom Juni 2026 beschreibt diese K-förmige Spaltung detaillierter: „Die direkt beschäftigten Arbeitskräfte in der Hauptwachstumsachse von AI, Halbleitern und Elektroniklieferketten machen weniger als 10 % der gesamten Erwerbstätigen aus“[^17]. Eine Person, die im Gastgewerbe arbeitet, verdient monatlich 38.484 Yuan, was nur 34,6 % des elektronischen Komponentenfertigungssektors entspricht[^17]. Der AI-Bonus ist real, aber er konzentriert sich auf Kapital und wenige Ingenieure; die meisten Menschen schauen von außen auf den Welle.

Dies ist die erste Ebene der Bedeutung von „Nicht untrennbar verbunden bedeutet nicht kontrollierend“: Taiwan hält den Schalter in der Hand, erhält aber nur 5 %.

## Taiwan hat es gehalten, und hätte es fast zerstört

Um zu verstehen, wie diese ungleiche Beziehung begann, muss man in die späten 1990er Jahre zurückblicken, als NVIDIA noch gegen den Tod kämpfte.

NVIDIA wurde 1993 gegründet und stand in den Vorjahren mehrmals am Rande des Bankrotts. Als im August 1997 der Grafikchip RIVA 128 auf den Markt kam, hatte das Unternehmen „nur einen Monatslohn“ mehr auf dem Konto [^18]. In dieser Zeit wiederholte Jensen Huang bei jedem Monatsmeeting denselben englischen Spruch: Unser Unternehmen hat nur noch dreißig Tage bis zum Bankrott [^18]. Dieser Satz wurde später zu einem internen Glaubenssatz von NVIDIA, war aber nie ein chinesischer Ausdruck.

Wer NVIDIA jedoch wirklich aus dieser Krise gerettet hat, war eine Zahlung von 5 Millionen Dollar durch Sega (SEGA), nicht Taiwan [^19]. Dies muss klar gestellt werden, da die Behauptung „Taiwan rettete NVIDIA“ oft zu romantisiert wird.

Die Rolle Taiwans war eine andere: die Lebensader der Fertigung. Gegen 1996 schrieb der 32-jährige Jensen Huang einen Brief an den Gründer von TSMC, Morris Chang, und fragte, ob TSMC für NVIDIA Chips herstellen könnte [^20]. Mi Yu-chieh von TSMC erinnerte später im Jahr 2025 daran, dass diese „tiefgreifende Zusammenarbeit in einem entscheidenden Moment begann, nämlich 1997“, als „Morris Chang persönlich mit dem Gründer von NVIDIA, Jensen Huang, Kontakt aufnahm, um die Anfrage von NVIDIA bezüglich der Auftragsfertigung zu beantworten“ [^21]. Im Jahr 1998 unterschrieben beide Parteien offiziell einen Vertrag, und TSMC wurde zum Hauptwaferhersteller von NVIDIA [^20]. Diese Aufteilung – „Design in Silicon Valley, Fertigung durch TSMC“ – brachte den physischen Körper von NVIDIA auf diese Insel.

> 💡 **Wussten Sie**: Eine verbreitete Version besagt, dass Jensen Huang beim Telefonat mit Morris Chang begeistert zu jemandem neben ihm geschrien habe, er solle leise sein, weil es Morris Chang war [^22]. Dieses Bild ist eine zweitrangige Überlieferung; der Tonfall ist möglicherweise ungenau, aber es fängt eine wahre Tatsache ein: Das kurz vor dem Ruin stehende kleine Unternehmen sah in einem Anruf von TSMC einen Rettungsanker.

Doch dieser Rettungsanker wurde fast zu einer Schlinge. Im Jahr 1998 führte ein chemischer Prozessfehler bei TSMC dazu, dass große Mengen an NVIDIA-Chips unbrauchbar wurden und das Unternehmen beinahe erneut am Abgrund brachte [^23]. Die ehrlichere Darstellung lautet daher: Taiwan war nicht der „Bankrottretter“ von NVIDIA; es war die „Fertigungslebensader“ – diese Lebensader war bilateral gebunden. Taiwan hatte es gehalten, aber es hätte es auch fast zerstört. Symbiose ist niemals eine einseitige Gnade.

Die folgende Geschichte ist Ihnen wahrscheinlich vertrauter. Im Jahr 2006 brachte NVIDIA CUDA auf den Markt, was damals von fast allen als verrückte Entscheidung angesehen wurde. 2012 trainierte der Doktorand Alex Krizhevsky mit zwei NVIDIA GTX 580 Grafikkarten in seinem Elternhaus und reduzierte die Fehlerrate bei der Bilderkennung von ImageNet von 26 % auf 15,3 % [^24]. Dieser Moment bewies, dass GPUs die Motoren des Deep Learning sind. Im Jahr 2022 löste ChatGPT den weltweiten Hunger nach Rechenleistung aus, und der Marktwert von NVIDIA schoss wie eine Rakete in die Höhe.

```tw-timeline
1993 | NVIDIA wird in Silicon Valley gegründet | Jensen Huang und zwei weitere entwickeln Grafikchips
1996 | Jensen Huang schreibt an Morris Chang | Bitten um Auftragsfertigung bei TSMC; 1998 offizieller Vertrag, physischer Körper auf Taiwan
2006 | CUDA wird eingeführt | GPUs werden zu einer allgemeinen Rechenplattform, damals als verrückte Entscheidung angesehen
2012 | AlexNet trainiert mit zwei GTX 580 | Beweis: GPU = Deep Learning Engine
2022 | ChatGPT erscheint | Globale Nachfrage nach Rechenleistung explodiert; NVIDIA-Marktwert steigt rasant
2025 | Marktwert über fünf Billionen Dollar | Das erste Unternehmen dieser Art, das seinen globalen Hauptsitz in Taiwan ankündigt
Quelle: 《The Nvidia Way》, Acquired Podcast, Wikipedia, CNBC
```

Von einem kleinen Unternehmen mit dreißig Tagen bis zum ersten Unternehmen mit fünf Billionen Dollar – bei jedem Chip dazwischen wurde in Taiwan hergestellt.

![Jensen Huang hält RTX Blackwell GPU während der CES 2025 Präsentation](/article-images/technology/jensen-huang-ces-2025-blackwell.webp)
_Jensen Huang präsentiert die neue Generation von Blackwell GPUs auf der CES 2025. Vom Gründer, der bei Monatsmeetings „nur noch dreißig Tage bis zum Bankrott“ sagte, bis zu diesem weltweit begehrten Chip – und er kann nur in Taiwan hergestellt werden. Foto: Pronoia, CC0._

## Unersetzbar und mit Ablaufdatum?

Dies führt zu einer Frage, der wir ehrlich begegnen müssen: Ist dieser „Unersetzbarkeits“-Status Taiwans ewig oder hat er eine zeitliche Begrenzung?

Kurzfristig ist die Grenze so hart, dass es kaum Risse gibt. In den Jahren 2025 bis 2027 sind die fortschrittlichsten KI-GPUs von NVIDIA – von der Herstellung bis zur Endverpackung – zu hundert Prozent auf dem CoWoS-L-Produktionsband von TSMC in Taiwan gebunden[^25]. TSMC beherrscht weltweit etwa 90 % bis 92 % der fortschrittlichen Prozesse unter 5 Nanometern, und seine Kapazität für fortschrittliche Verpackung übersteigt die aller Konkurrenten[^26]. Die Forschung von Professor Zhou Yun-tsai von NTU spricht es offen an: Kurzfristig ist eine Diversifizierung der Auftragsfertigung von TSMC nicht machbar; der Bau einer neuen Hochleistungsfabrik würde drei bis vier Jahre und über 10 Milliarden US-Dollar kosten[^27].

Der stärkste technische Beweis findet sich nicht in einem Bericht, sondern im Produktdesign von NVIDIA selbst. Die nächste Generation, Rubin Ultra, war ursprünglich für die „Quad-Die“-Verpackung vorgesehen, aber TrendForce merkte im April 2026 an, dass Quad-Die die Verpackungsfläche auf ein Limit von 7,5 bis 8 Mal des Maskenbereichs ausdehnen würde, was „die Ausbeute und Kosten stark beeinträchtigt“ und daher das Design „auf eine Dual-Die-Architektur umgestellt hat“[^4]. Dieser Satz muss langsam gelesen werden: Die physikalische Einschränkung der Verpackungsausbeute in Taiwan bestimmt indirekt, wie die NVIDIA-Chips aussehen müssen. Selbst die weltweit führenden Chipdesignunternehmen müssen ihr Design an die Ausbeute Taiwans anpassen – dies ist ein physischer Engpass ohne Verhandlungsspielraum.

Aber „kurzfristige harte Grenzen“ bedeuten nicht „ewig“. Taiwan hat schmerzhafte Vorbeispiele.

Im Jahr 2002 förderte Taiwan die Industriepolitik „Zwei Trillionen, Zwei Sterne“, wobei Panels und DRAM (Speicher) als unersetzliche Lebensadern der nationalen Verteidigung galten. Was war das Ergebnis? Da Kerntechnologien fehlten und die F&E-Investitionen nur 6 % betrugen – weit unter den 10 % bis 21 % von Korea, Japan, USA und Europa –, wurden diese beiden Industrien von Südkorea und China systematisch ausgebeutet. Eine spätere Rückschau der United Daily News war schmerzhaft: „Die einst glanzvollen Panel- und Speicherhersteller erlitten in den folgenden Jahren massive Verluste aufgrund des Überangebots auf dem Weltmarkt, worauf die Netizens mit ‚Maosamtige‘ (Mao 3 bis 4) reagierten – also eine Bruttomarge von nur drei bis vier Prozent. Die ‚Zwei-Trillionen-Sterne-Industrie‘ wurde zur ‚Zwei-Trillionen-Herzschmerz-Industrie‘.“[^28]

> ⚠️ **Was ist hier anders als bei Panels und DRAM**: Panels und DRAM wurden damals ausgebeutet, weil Taiwan die Kerntechnologien nicht beherrschte; jeder konnte nachziehen. Der Graben der KI scheint viel tiefer zu sein – TSMC beherrscht tatsächlich das Prozess-IP, und die Adhäsion des CoWoS-Verpackungsprozesses und des gesamten Ökosystems ist nichts, was man in drei bis fünf Jahren kopieren kann. Aber das ist kein Grund für Taiwan, sich sicher fühlen zu dürfen. SMIC hat 5 nm angekündigt, obwohl deren Ausbeute nur ein Drittel der von TSMC beträgt und die Kosten noch 50 % höher sind – etwa fünf Jahre hinterher[^29]. Fünf Jahre sind in der Technologiebranche aber keine Ewigkeit. „Tiefe Abhängigkeit“ als „ewige Sicherheit“ zu betrachten, ist genau der Fehler, den die Leute im Jahr 2002 gemacht haben.

Ab 2028 beginnen Risse aufzutauchen. NVIDIA investierte Ende 2025 etwa 5 Milliarden US-Dollar in Intel mit dem echten Ziel, „Priorität bei der Sicherung der fortschrittlichen Verpackungskapazität von Intel in den USA zu erhalten“, die für die Feynman-Architektur im Jahr 2028 vorgesehen ist[^30]. Die AP1-Verpackungsfabrik von TSMC in Arizona soll voraussichtlich 2028 in Betrieb gehen[^31]. Powertech (Taiwan) hat PiFO entwickelt, eine Verpackung, die CoWoS-L entspricht und etwa 30 % geringere Produktionskosten aufweist, und „mehrere US-KI-Chipunternehmen“ sind bereits interessiert[^32]. Dies sind echte Lockerungen, aber sie haben noch nicht in die Hauptlieferkette der fortschrittlichsten NVIDIA-GPUs eingedrungen.

Eine Zahl verdeutlicht die subtile Lage am besten: TrendForce prognostiziert, dass das Angebot-Nachfrage-Dilemma bei CoWoS von derzeit etwa 20 % auf etwa 10 % bis Ende 2026 schrumpfen wird[^33]. Die Art und Weise, wie der Engpass schrumpft, ist jedoch durch die eigene Kapazitätserweiterung von TSMC, nicht durch Ersatzanbieter[^33]. Das bedeutet, dass dieser Engpass bisher nur von Taiwan selbst gelöst werden konnte.

Unersetzbar ist eine technische Realität, aber sie hat eine harte Grenze, die um 2028 liegt. Taiwans Spielkarten haben ein Haltbarkeitsdatum.

## 44,34 Milliarden: Eine Stadt räumt ein Grundstück für ein multikiliardenschweres Unternehmen frei

Wenn die Gewinnmarge eine abstrakte Waage der Macht ist, dann war das Geschehen im Technologiepark North Taipei Shi Lin in der zweiten Jahreshälfte 2025 der schärfste Schnitt dieser Waage.

Die Geschichte beginnt im Jahr 2021. Damals versteigerte die Stadtverwaltung von Taipeh zwei Grundstücke (T17 und T18) in North Taipei Shi Lin, deren Gesamtfläche 3,89 Hektar beträgt, als 50-jährige Nutzungsrechte; New Life gewann diese Auktion mit 4,4 Milliarden NTD[^34]. In den folgenden drei Jahren blieb das Grundstück brachliegen und wurde von Unkraut überwuchert.

Im Mai 2025 kündigte Jensen Huang auf Computex an, dass der globale Hauptsitz von NVIDIA, „Constellation“, in North Taipei Shi Lin angesiedelt werden soll[^35]. Doch es gab ein Problem: Die Nutzungsrechte lagen noch bei New Life, und öffentliche Nutzungsrechte können nicht einfach übertragen werden. NVIDIA, New Life und die Stadtverwaltung von Taipeh waren fünf Monate lang wegen dieses Grundstücks blockiert[^36].

Die endgültige Lösung war, dass die Stadtverwaltung von Taipeh Geld bezahlte, um New Life zum Rückzug zu bewegen. Am 12. November 2025 stimmte der Stadtrat von Taipeh einstimmig einer Vertragsentgelterklärung in Höhe von 4,434 Milliarden NTD[^37] zu, die die Stadtverwaltung an New Life zahlte, um das Land zurückzuerhalten. Dieser Betrag lautet: 4,434 Milliarden 64 Millionen 85 Tausend NTD[^37].

```tw-figure
NT$4,434,064,085
Die Vertragsentschädigung, die die Stadtverwaltung von Taipeh an New Life zahlte, um das Grundstück in North Taipei Shi Lin zurückzuerhalten und es an NVIDIA zu übergeben (Ratbeschluss vom 12.11.2025)
Stadtrat von Taipeh, Central News Agency, Yipin News Network
```

Die Rechnung, die New Life reichte, löste im Stadtrat einen Aufruhr aus. Die Ratsabgeordnete You Shu-hui kommentierte den Erhalt dieser Rechnung: „Als ich die 8-seitige Rechnung von New Life sah, auf der Kosten wie Unkrautbekämpfung, Umweltpflege, Logoanpassung und Honorare für Rechtsbeistand aufgeführt waren, konnte ich nur bitter lachen. Die Umweltpflege ist doch etwas, das der Mieter eigentlich selbst erledigen sollte? Sogar die Kosten für die Anpassung des Logos von Tai Xin und New Life muss die Stadtverwaltung bezahlen? Das ist wirklich unglaublich... Ach, wie hilflos.“[^38] Letztendlich stimmte sie jedoch zu und fügte einen Satz hinzu, der die Stimmung im Raum gut widerspiegelte: „Die Rechnung an New Life ist unvorstellbar, aber das große Ganze zählt.“[^38].

An diesem Tag gab es ein seltenes Bild im Stadtrat: Die drei Fraktionen (Blaue, Grüne und Weiße) waren ungewöhnlich harmonisch; die DPP-Gruppe rief sogar „Unterstützung für Nvidia, schnell unterschreiben“[^39]. Ein Grundstück und ein ausländisches Unternehmen brachten normalerweise streitende Parteien zum Konsens.

> 📝 **Kuratorische Anmerkung**: Man sollte diesen Machtapparat betrachten. Um einem multikiliardenschweren Unternehmen einen Platz zu verschaffen, mobilisierten die Stadtverwaltung und der Stadtrat einer Stadt öffentliche Gelder, übersprangen Fraktionsgrenzen und beseitigten alle Hindernisse, um ein Grundstück freizuräumen, das von einem vorherigen Mieter besetzt war. NVIDIA hat diese 4,434 Milliarden nicht bezahlt; dieses Geld wurde zunächst von den Steuerzahlern von Taipeh getragen (wobei die eigenen Kosten und bereits gezahlten Steuern von New Life insgesamt 1,441 Milliarden NTD ausmachten, welche dann von NVIDIA übernommen wurden)[^40]. „Nicht loskommen können bedeutet nicht, dass man gewinnen kann“ hat hier eine konkrete Form angenommen: Wenn du jemanden so dringend brauchst, bezahlst du ihm Rechnungen, die er eigentlich nicht hätte bezahlen sollen.

## Hauptsitz: Ein Schild oder tief verwurzelte Wurzeln

Was hat NVIDIA Taiwan geschenkt? Das muss man in zwei Teilen betrachten, um keine falsche Einschätzung zu treffen.

Einerseits das „Schild“: Der Constellation-Hauptsitz ist im Stil des „Sternenschiffs“ des US-Hauptsitzes gestaltet und soll etwa 4.000 Personen beherbergen; er geht im Jahr 2026 in Bau und wird erst 2030 fertiggestellt – bis heute ist er noch nicht in Betrieb[^41]. Allein dieser Aspekt lässt die Frage, ob der „Hauptsitz nur eine PR-Aktion“ ist, nicht unbegründet erscheinen.

Andererseits die „tief verwurzelte Basis“. NVIDIA ist nicht erst 2025 nach Taiwan gekommen. Es hatte bereits Büros in Neihu, Taipeh, mit etwa 1.800 Mitarbeitern (dies ist eine Schätzung der Medien und keine offizielle Zahl)[^42]. Bereits im Jahr 2021 erhielt das Unternehmen vom Ministerium für Wirtschaft die Genehmigung für ein „AI-Innovationsforschungszentrumsprojekt“ mit einer Gesamtinvestition von 24,3 Milliarden [TWD/USD nicht angegeben], wobei staatliche Zuschüsse 6,7 Milliarden betrugen und bis 2027 neue Entwicklerteams in Höhe von 1.000 Personen eingestellt werden sollten[^43]. Im November 2025 gründete es die „Taiwan NVIDIA Classic Co., Ltd.“, deren Stammkapital von 1 Milliarde auf 3,3 Milliarden erhöht wurde – dies ist eine eigenständige juristische Person, die selbstständig Steuern zahlen und Vermögen halten kann[^44].

Die Wahrheit über die „Etablierung des Hauptsitzes“ liegt also in der Mitte: Die tatsächlichen Forschungswurzeln sind vorhanden, und es gibt eine steuerzahlende Tochtergesellschaft; aber dieser am meisten beachtete Constellation-Hauptsitz befindet sich noch auf dem Bauplan. Beide Aspekte dürfen nicht nur halb behandelt werden.

## Die Insel, die durch diese Lieferkette ausgetrocknet wird

Neben dem Image und der Rechnung gibt es noch eine Abrechnung, die jeder Mensch auf dieser Insel begleichen muss: Wasser, Strom, Luft, Wohnraum, den man sich nicht leisten kann.

![Außenansicht des TSMC-Werks in Taichung](/article-images/technology/tsmc-taichung-factory.webp)
_TSMC-Werk in Taichung. Der physische Körper jeder NVIDIA-GPU einer Generation wird in solchen Fabriken geformt, und das Wasser und der Strom, die diese Fabriken verbrauchen, sind eine weitere Rechnung, die diese Insel bezahlt._ Photo: Briáxis F. Mendes (孟必思), CC BY-SA 4.0.

Zuerst der Strom. TSMC verbrauchte im Jahr 2023 247,75 Milliarden kWh und machte 8,96 % des gesamten Stromverbrauchs Taiwans [^45]. Standard & Poor's prognostiziert, dass der Stromverbrauch von TSMC bis 2030 auf 23,7 % des nationalen Verbrauchs ansteigen könnte [^45]. Das bedeutet, dass dort bis dahin fast ein Kilowatt pro vier Kilowatt in ganz Taiwan von diesem einen Unternehmen verbraucht werden könnte.

```tw-line
Anteil des Stromverbrauchs durch TSMC: Ein Unternehmen entzieht der Insel fast 1/4 des Stroms (%)
Jahr | Anteil
2023 | 8,96
2030 | 23,7
Quelle: Standard & Poor's, CSR-Bericht von TSMC
```

Die Kohlenstoffemissionen steigen ebenfalls. Ein Bericht von Greenpeace vom April 2025 mit dem Titel „Schatten nach dem Chip-Glanz“ berechnete, dass der Stromverbrauch für die Herstellung globaler KI-Chips von 218 GWh auf 984 GWh anstieg, was einem Anstieg von über 3,5 Mal pro Jahr entspricht; allein Taiwan verbrauchte bis zu 375,8 GWh und machte damit „bis zu 38 % des weltweiten Gesamtverbrauchs“ [^46]. Da TSMC stark auf fossile Brennstoffe angewiesen ist, beläuft sich sein CO2-Äquivalenz-Ausstoß bei der KI-Chipherstellung auf 185.700 Tonnen und Greenpeace bezeichnete das Unternehmen direkt als „CO2-Champion der KI-Chipherstellung“ [^46].

Und NVIDIA selbst? Greenpeaces Bewertung ist F. Der Bericht schreibt, dass die „Lieferkettenemissionen von NVIDIA in den letzten drei Jahren fast verdoppelt wurden, von 3,51 Millionen Tonnen im Jahr 2022 auf 6,91 Millionen Tonnen im Jahr 2024“, und dass das Unternehmen „lediglich die Kohlenstoffemissionen und Verschmutzung der Lieferkette in andere Regionen der Welt abwälzt“ [^46]. Mit anderen Worten: Der Wert wird NVIDIA zugeschrieben, während die Emissionen und die Umweltverschmutzung im Himmel über Taiwan bleiben.

Auch das Wasser ist ein Thema. TSMC verbraucht täglich über 200.000 Tonnen; die 81.000 Tonnen Wasser, die von der Wasseraufbereitungsanlage in Tainan täglich geliefert werden, gehen „nahezu vollständig an TSMC“ [^47]. Der Preis wird auf den Ackerbau abgewälzt: Die Felder in Jianan wurden 2021 und 2023 zweimal bewässern verweigert, um Wasser für die Halbleiterindustrie bereitzustellen [^48]. Die Herstellung einer 12-Zoll-Wafer benötigt 8.327 Liter Wasser [^49], und auf dieser Insel wurden Ackerflächen, wo einst Bauern wirkten, brachliegen gelassen, damit der Chip Wasser bekommt.

Dann gibt es die Wohnungen. Nachdem NVIDIA angekündigt hat, seinen Hauptsitz in North Science zu errichten, begannen die Immobilienpreise in diesem Gebiet zu steigen. Die Stadtentwicklungsbehörde von Taipeh schätzt, dass bis zu 60.000 dauerhafte Arbeitsplätze in North Science entstehen könnten, aber es gibt nur etwa 1.476 zum Verkauf stehende Wohnungen (Wohnflächen machen nur 13,8 % des gesamten Gebiets) [^50]. Wie kann man sich vorstellen, dass 60.000 Menschen um 1.476 Einheiten konkurrieren? Die Berichte berichten bereits von Neuentwicklungen im Kerngebiet von North Science zu Preisen über 1,5 Millionen pro Pinge [^51].

Hier muss man zwei Dinge klar trennen, damit die Angst nicht falsch berechnet wird. Bei den tatsächlichen Verkaufsdaten (Real-Price Listings) lag der höchste Verkaufspreis für Wohnungen im Bezirk Shilin im Jahr 2025 bei 570.400 Yuan pro Quadratmeter, was etwa 1,88 Millionen pro Pinge entspricht (Nr. 39, Jihe Road; Gesamtpreis 447 Millionen) [^52]. Aber diese extrem teuren Immobilien befinden sich in Luxuswohnungen in Tianmu und Shilin City, was etwas anderes ist als North Science selbst; die Berichte über Neuentwicklungen in North Science zu Preisen über 1,5 Millionen pro Pinge sind eine andere Zahl. Diese beiden Zahlen dürfen nicht vermischt werden. Aber egal welche, sie deuten auf dasselbe Gefühl hin: Der Fortschritt findet auf meiner Straße statt, aber ich kann es mir nicht leisten.

> ⚠️ **„Warum steigt der Preis, bevor das Unternehmen überhaupt gebaut hat?“**: Die Gegenreaktion der lokalen Bewohner ist real. Ein Unternehmer sagte vertraulich, dass „viele Mitarbeiter nicht bereit seien, mitzukommen, weil die Lebensfunktionen des Parks schlecht sind … und selbst wenn sie kommen, verlassen ein Drittel der Mitarbeiter den Job, weil der Transport unpraktisch ist“ [^53]. Die anonymen Meinungen auf PTT waren noch direkter: „Wir haben das Thema TSMC genug gesehen, jetzt wird nur NVIDIA verwendet“ [^54]. Ein Hauptsitz, der noch nicht gebaut wurde, treibt die lokalen Immobilienpreise in die Höhe – das ist die Version des K-förmigen Wandels, die dem Esstisch am nächsten kommt. Man muss ehrlich sein: Die KI hat Taiwan wirklich weltweit sichtbar gemacht, aber auch das ausgetrocknete Wasser, der Strom und der unbezahlbare Wohnraum sind real; beides muss erwähnt werden.

## Nicht nur Taiwan ist davon abhängig

Wenn man den Blickwinkel erweitert, sieht man eine größere Geschichte: In der Beziehung zwischen NVIDIA und Taiwan ist die Abhängigkeit beidseitig, ja sogar vielschichtig. Sogar die andere Seite der Straße von Taiwan ist in diese Struktur eingebunden.

![Taipei Nangang Exhibition Center Computex Venue, information company booths lined up on both sides of the wide aisle, crowds gathered](/article-images/technology/computex-nangang-floor-2015.webp)
_Die Computex-Messe im Taipei Nangang Exhibition Center. Jeden Juni strömen Käufer aus aller Welt in dieses Zentrum, um die Produkte zu sehen, die diese Lieferkette für Taiwan hervorgebracht hat – nicht nur Taiwan ist davon abhängig. Foto: NVIDIA Taiwan, CC BY 2.0._

Das ist das Konzept des „Silicon Shield“ (Silberschild): Taiwan beherrscht Chips, die die ganze Welt braucht, und diese Unersetzbarkeit bildet eine Art Schutzschild. Doch das Silberschild hat immer zwei Seiten. Es ist sowohl ein Schutzamulett als auch ein Pulverfass auf der Insel. Die Wissenschaft bezeichnet diese beiden Seiten als „Silicon Shield“ (Silberschild) und „Silicon Trap“ (Silizientrap): Dieselbe Konzentration kann Eindringlinge abschrecken, aber sie kann auch zu einem Anreiz für Aggression oder zu einem Einfallspunkt werden [^55].

Eine schärfere Debatte wurde 2021 durch einen Artikel der U.S. Army War College ausgelöst, der eine extreme „Bodenzerstörungs-/Nestzerstörungs“-Strategie vorschlug: Wenn China Taiwan angreift, soll es bereit sein, seine Halbleiterindustrie selbst zu zerstören, um dem Gegner keinen Vorteil zu verschaffen. Aber auch die Gegenstimmen sind laut: Selbst wenn diese Strategie kurzfristig China abschrecken würde, könnte dieser wirtschaftliche Selbstschaden nur den Angriff aufschieben, bis China in der Lage ist, eigene Halbleiter zu produzieren; und die taiwanesischen Bürger selbst würden wahrscheinlich nicht glauben, dass eine solche Zerstörung ihrer Industrie ihren eigenen Interessen entspricht [^56]. Dies ist keine Frage, die Taiwan beantworten muss, aber sie hängt real hinter jeder Diskussion darüber, ob „Taiwan Verhandlungsmasse hat“.

Das Silberschild wird sogar von TSMC selbst verwässert. Um geopolitische Risiken zu streuen, investiert TSMC 165 Milliarden US-Dollar in Erweiterungen in den USA [^57]. Der Titel der _MIT Technology Review_ vom August 2025 lautet „Taiwans Silberschild könnte geschwächt werden“ [^58]. Die Sorge besteht darin, dass die Verlagerung der Produktionskapazitäten die Verhandlungsmacht Taiwans im Inland mindern und dazu führen könnte, dass Länder wie die USA Taiwan nicht mehr als so schützenswert erachten [^58]. Aber Bonnie Glaser vom German Marshall Fund erinnert daran, dass dieses Ökosystem nicht leicht zu verschieben ist: Das von Taiwan geschaffene Ökosystem ist einzigartig, da es das Ergebnis der Wechselwirkung zwischen Talentpool, Kultur und taiwanesischem Recht ist; es kann nicht einfach an einem anderen Ort repliziert werden [^59]. Paul Triolo, der sich mit chinesischer Technologie beschäftigt, sagt noch direkter: Was die Spitzentechnologie betrifft, so ist Arizona noch weit davon entfernt, und wird es nie sein [^60].

und was die Asymmetrie dieser Abhängigkeit am besten verdeutlicht, ist ein politischer Moment.

Am 29. Mai 2024 sagte Jensen Huang in Taiwan öffentlich: „Taiwan is one of the most important countries in the world.“[^61] Nur wenige Tage später, am 2. Juni, beschrieb er bei einem Vortrag an der National Taiwan University (NTU) „Taiwan als einen anonymen Helden, aber eine Säule der Welt“[^62].

```tw-quote
Taiwan ist ein anonymer Held, aber eine Säule der Welt
Jensen Huang | CEO von NVIDIA, NTU Computex Vortrag, 2024
```

Nach achtzehn Tagen reagierte Chen Binhua, Sprecher des Taiwan Affairs Office (TAO) in China, mit: „Die chinesischen und Online-Nutzer haben sich über diese extrem falschen Äußerungen vielfach stark geärgert. Taiwan war nie ein Land … wir hoffen, er soll nacharbeiten.“[^63]

Aber eine andere Sache ist interessant. Die Central News Agency bemerkte damals, dass die chinesischen Wirtschaftsmedien viele Berichte über den Besuch von Jensen Huang in Taiwan veröffentlichten, aber „die Aussage von Jensen Huang, dass ‚Taiwan ein wichtiges Land‘ sei, nicht erwähnt hätten, was auf das Auslassen eines Themas hindeutet, das normalerweise als ‚äußerst wichtig‘ angesehen wird“[^64]. Das heißt, während die offizielle Seite vehement protestierte, schalteten die Wirtschaftsmedien stumm.

> 📝 **Kuratorische Anmerkung**: Dieses Schweigen enthüllt die wahre Machtposition. China braucht die Chips von NVIDIA; daher entschieden sich die chinesischen Medien dafür, nicht zu berichten oder nicht zu verstärken, selbst wenn Jensen Huang das für Peking unakzeptabelste gesagt hat, um die Beziehung zu diesem „AI-Meister“ nicht zu gefährden. Es kursierte der Satz: „China braucht Nvidia, aber Nvidia braucht China nicht.“[^65] In dieser Beziehung wird der riesige Markt auf der gegenüberliegenden Seite der Straße in gewisser Weise von der Lieferkette eines amerikanischen Unternehmens abhängig gemacht. Dies ist die seltsame Lage dieser Insel Taiwan: Die ganze Welt, einschließlich jener, die sie verändern wollen, kann nicht ohne die Chips dort leben. Aber „die ganze Welt braucht dich“ und „du bist deshalb sicher und kannst bestimmen“, sind immer noch zwei verschiedene Dinge. Der Autor zieht keine politischen Schlüsse für Taiwan, aber diese Spannung ist es wert, dass jeder Leser selbst darüber nachdenkt.

## Untrennbar, heißt nicht zwangsläufig bestimmen

Zurück zur Wand mit den Logos der 55 Unternehmen.

Jeder Name an dieser Wand ist real. Sie sind das Fleisch der Erd-KI-Revolution; ohne sie könnte NVIDIA mit fünf Billionen Dollar keinen einzigen Chip liefern. Diese Unersetzbarkeit ist eine technische Tatsache, keine Rhetorik. Taiwan sollte stolz darauf sein.

Doch was man bisher gesehen hat, ist, dass der Glanz, die Bewertung und die Entscheidungsbefugnis bei denen liegen, die diese Wand aufgebaut haben; während die 5 % Gewinnmarge, das abgepumpte Wasser und Strom, die zu hohen Immobilienpreise treiben, sowie das Kriegsrisiko auf der Insel bei den Namen an der Wand lasten. Taiwan hält den Schalter in der Hand, der die ganze Welt nicht ausschalten kann, aber es bedeutet noch keine absolute Macht. Und diese Währung hat noch ein Haltbarkeitsdatum, das sich um 2028 dreht.

Taiwan steht nicht still. Lai Ching-te schlug im Jahr 2025 vor, Taiwan zu einem „einer der weltweit führenden fünf Rechenzentren“ zu machen und „souveräne KI“ zu entwickeln [^66]; Foxconn baut in Kaohsiung einen nationalen Supercomputer mit zehntausend Blackwell-Chips [^67]; das „AI New Decade Construction“ des Exekutivrates soll über 100 Milliarden investieren, mit dem Ziel eines Wertes von 15 Billionen [^68]. Dies ist der Versuch, aus der „Auftragsfertigung für andere“ zu „eigenem Rechnen“ aufzusteigen: einen Schritt nach oben vom unteren Ende der Lächelnkurve.

Doch dieser Weg ist noch weit. Taiwans eigenes Sprachmodell TAIDE wird als „Highschool-Niveau“ beschrieben, während internationale Großunternehmen bereits das Niveau von „Postgraduierten“ erreicht haben [^69]. Die sütkoreanische Regierung kauft auf einmal 260.000 GPUs, während Taiwan noch um ein Grundstück und eine Abfindungszahlung kämpft [^70]. Von dem Anruf von Morris Chang bis zur Bewältigung der Rechenleistung der ganzen Welt hat Taiwan fast dreißig Jahre gebraucht, um an diese Wand zu gelangen. Aber auf die Wand zu steigen und den Stift zurückzuholen, sind zwei verschiedene Dinge.

Die Wand wird weiter leuchten. Bei der nächsten Computex wird Jensen Huang mehr Logos hinter dem Rücken haben. Im Jahr 2026 gab er bekannt, dass NVIDIA jährlich etwa 150 Milliarden Dollar in Taiwan ausgibt, verglichen mit nur 10 bis 15 Milliarden vor fünf Jahren [^71]. Die Frage „Ist Taiwan wichtig?“ hat bereits eine Antwort. Was Taiwan beantworten muss, ist die schwierigere: Wie lässt man „unverzichtbar sein“, wenn die ganze Welt von dem, was du machst, abhängig ist?

Die Namen an der Wand nehmen zu. Wer den Stift hält, wird es selbst sein – und mit diesem Stift hat Taiwan gerade erst angefangen zu kratzen.

---

**Weiterführende Lektüre**:

- [Jensen Huang: Vom Jungen, der Toiletten putzte, zum CEO eines Fünf-Billionen-Imperiums](/de/people/jensen-huang) — Die Lebensgeschichte des Gründers von NVIDIA; dieser Artikel behandelt nur kurz seine Familie in Tainan und seine Geschichte
- [Halbleiterindustrie](/de/technology/taiwan-semiconductor-industry) — Warum Taiwan zum Zentrum der globalen Chipfertigung geworden ist; die Lieferkette wird hier noch vollständiger beleuchtet
- [Taiwanische Unternehmen: TSMC](/economy/台灣企業：台積電) — Der „Schutzheilige“, der jeden Chip für NVIDIA herstellt, und die andere Seite, die ausgebeutet wird
- [Morris Chang: Die Empfängerin dieses Briefes und das von ihm geschaffene Wafer-Imperium](/de/people/tsmc-morris-chang) — Der Gründer von TSMC, der 1996 den Brief von Jensen Huang erhielt
- [Computex: Das Computer-Messe in Taipei wird zur Eröffnungszeremonie für die globale KI](/de/technology/computex) — Die Bühne, auf der diese Logo-Wand leuchtet; das jährliche Schauplatz der taiwanesischen Technologieindustrie
- [Industrie Künstliche Intelligenz](/de/technology/artificial-intelligence-industry) — Von der Herstellung von NVIDIA-Chips bis zum Aufbau des KI-Ökosystems: Taiwans Platz in der KI-Welle
- [Taiwanische KI-Entwicklung und zukünftige Strategie](/technology/台灣人工智慧發展與未來策略) — Souveräne KI, TAIDE und das nationale Bestreben Taiwans, von der Auftragsfertigung aufzusteigen
- [Taiwanesische Tech-Geschichten: 100 Punkte Chip, 60 Punkte Mikrofon](/de/technology/taiwan-tech-stories) — Zwei Erzählungen desselben Chips: Der Aufschlag, den NVIDIA verdient, und was die taiwanesische Technologie lernen muss
- [Taiwanische Unternehmen: Foxconn Precision](/economy/台灣企業：鴻海精密) — Der Gigant der Auftragsfertigung, der 40 % der globalen KI-Server montiert; die größten Hände am unteren Ende der Lächelnkurve

## Bildquellen

- [Jensen Huang bei Computex Taipei](https://commons.wikimedia.org/wiki/File:Jensen_Huang_at_Computex_Taipei_20160531c.jpg) — Foto: NVIDIA Taiwan, 2016, CC BY 2.0 (Hero; Jensen Huang hält bei Computex Rede)
- [NVIDIA Ampere GA102 GPU die](<https://commons.wikimedia.org/wiki/File:Nvidia@8nm@Ampere@GA102@GeForce_RTX_3090@S_TW_2032A1_SNNB9W.000_GA102-300-A1_DSC06025-DSC06107_(50740715646).jpg>) — Foto: Fritzchens Fritz, CC0 (Mikroskopbild des Chips)
- [Jensen Huang hält RTX Blackwell bei CES 2025](<https://commons.wikimedia.org/wiki/File:Jensen_Huang_-_RTX_Blackwell_-_Nvidia_Keynote_-_CES_2025_Las_Vegas_(3).jpg>) — Foto: Pronoia, CC0
- [TSMC Fabrik in Taichung](https://commons.wikimedia.org/wiki/File:TSMC_logo_on_Taichung_factory_building.jpg) — Foto: Briáxis F. Mendes (Meng Bisi), CC BY-SA 4.0
- [Computex Taipei im Taipei Nangang Exhibition Center](https://commons.wikimedia.org/wiki/File:Computex_Taipei_at_Taipei_Nangang_Exhibition_Center_20150602.jpg) — Foto: NVIDIA Taiwan, 2015, CC BY 2.0
- Video: [NVIDIA CEO Jensen Huang Keynote bei COMPUTEX 2025](https://www.youtube.com/watch?v=TLzna9__DnI) — Offizieller YouTube-Kanal von NVIDIA

## Referenzen

[^1]: [NVIDIA wird zum ersten Unternehmen mit einer Marktkapitalisierung von 5 Billionen Dollar](https://www.cnbc.com/2025/10/29/nvidia-5-trillion-market-cap.html) — CNBC berichtete am 29. Oktober 2025, dass NVIDIA das erste Unternehmen ist, dessen Marktwert 5 Milliarden US-Dollar überschreitet, angetrieben durch den Bedarf an KI-Rechenleistung.

[^2]: [Taiwan hält 90 % des globalen AI-Servermarktes](https://technews.tw/) — Daten von Ministerium für Wirtschaft und MIC (Industrial Technology Research Institute) zeigen, dass die taiwanesische Serverindustrie über 80 % der weltweiten Exporte ausmacht, und die Auftragsfertigung von KI-Servern 90 % hält; wenn man US-Markenlieferanten mitzählt, erreicht es 100 %, da amerikanische Kunden eine Produktion außerhalb Chinas fordern.

[^3]: [TrendForce: NVIDIA ist der größte Kunde von TSMC](https://www.trendforce.com/) — Laut TrendForce-Daten vom 1. Juni 2026 stieg der Beitrag von „Kunde A“ (NVIDIA) zum Umsatz von TSMC von 12 % im Jahr 2024 auf 19 % in 2025 und übertraf damit Apple (von 22 % auf 17 %) als größter Kunde. Primärquelle: Jahresbericht von TSMC für 2025 (investor.tsmc.com).

[^4]: [TrendForce: Rubin Ultra wechselt zu einer Dual-Wafer-Architektur](https://www.trendforce.com/news/) — Eine Analyse von TrendForce vom 1. April 2026 besagt, dass die Vier-Wafer-Verpackung zu einem Flächenwachstum von 7,5 bis 8 Mal im Vergleich zur Maske führt und „die Ausbeute und Kosten stark beeinträchtigt“, weshalb das Design auf Dual-Wafer umgestellt wurde; KI wird 36 % der 3-nm-Kapazität im Jahr 2026 beanspruchen, während es 2025 nur 5 % ausmacht. Die physikalischen Einschränkungen der Verpackungsausbeute bestimmen direkt die Chiparchitektur.

[^5]: [NVIDIA FY2025 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581025000023/nvda-20250126.htm) — Der Jahresbericht von NVIDIA, eingereicht bei der US-Börsenaufsichtsbehörde (SEC), zeigt eine GAAP-Bruttomarge von 75,0 % für das gesamte Jahr (72,7 % in FY2024).

[^6]: [Zusammenfassung des Computex 2025 Vortrags von Jensen Huang: Wand mit Logos von 55 taiwanesischen Unternehmen](https://money.udn.com/money/story/5612/8750451) — Ein Bericht der Economic Daily listet die 55 taiwanesischen Unternehmen auf, deren Namen auf dem Hintergrundbild der Bühne beim Computex 2025 genannt wurden (Yanyang, Zhibang, Delta Electronics... TSMC, United Microelectronics Corp., Unilinx, Wistron, Wistron AI, Chongtai), und berichtet ferner, dass die Gesamtanzahl von Logos auf der Bühne plus Dankesvideos 122 beträgt.

[^7]: [Abhängigkeit von NVIDIA gegenüber TSMC bei 3/4 nm](https://www.ainvest.com/news/) — Branchenanalyse: Die profitabelsten Chips von NVIDIA – H200, Blackwell und Rubin – sind vollständig auf die 3-nm- und 4-nm-Prozesse von TSMC angewiesen, was zu einem Engpass sowohl bei der Herstellung als auch beim Packaging führt.

[^8]: [Offenlegung der Lieferkettenkonzentration von NVIDIA in FY2025 (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581025000023/nvda-20250126.htm) — Der Originalbericht von NVIDIA: „Unsere Lieferkette ist hauptsächlich auf die Region Asien-Pazifik konzentriert. Wir nutzen Foundries wie Taiwan Semiconductor Manufacturing Company Limited, oder TSMC... zur Herstellung unserer Halbleiterwafer.“ Die Risikofaktoren listen die geografische Konzentration der Zulieferer, Waferhersteller und Testunternehmen als geopolitisches Risiko auf.

[^9]: [TSMC CoWoS Kapazität und NVIDIA-Anteil](https://www.financialcontent.com/article/tokenring-2025-12-26-tsmc-boosts-cowos-capacity) — Daten von FinancialContent und SiliconAnalysts zeigen, dass NVIDIA etwa 60 % der TSMC CoWoS-Kapazität einnimmt (SiliconAnalysts schätzt ca. 595.000 Wafer), während taiwanesische Medien angeben, dass dieser Anteil im Jahr 2025 bei 70 % liegt; die Top 3 Kunden (NVIDIA, Broadcom, AMD) machen zusammen über 85 % aus.

[^10]: [Foxconn hält mehr als 40 % des AI-Server-Montageanteils](https://vocus.cc/) — Die Prognose von YuShan Securities schätzt, dass Foxconn (Ingrasys) GPU-Module, Switch Boards, Compute Boards und Rack-Systeme für GB200 NVL72 mit über 40 % abdeckt; die Fabrik in Nanqing ist ein zertifiziertes globales AI-Server-Leuchtturmwerk des World Economic Forum (Dezember 2023).

[^11]: [Quanta hält mehr als die Hälfte der Top 50 Rechenzentren](https://www.artificialintelligence-news.com/news/ai-servers-transform-taiwan-manufacturing-giants/) — AI News berichtet, dass Quanta (QCT) bei der Integration von L10 und L11 über 50 % der Top 50 Cloud-Rechenzentren abdeckt und damit zum zweitgrößten Servermontageunternehmen weltweit gehört.

[^12]: [Wistron AI-Neuanlage in Zhubei vollständig durch NVIDIA bestellt](https://vocus.cc/) — Branchenberichte berichten, dass Wistron für HGX/DGX zuständig ist und seine neue KI-Anlage in Zhubei „vollständig mit starken Aufträgen von NVIDIA ausgelastet“ ist.

[^13]: [Gewinnmargendaten der taiwanesischen Unternehmen bei AI-Servern](https://www.cnyes.com/) — Quartalsberichte für FY2025–FY2026: Foxconn Q1 FY2026 mit 6,18 % Marge (AI-Server machen über 50 % des Cloud-Netzwerkumsatzes), Quanta mit 4,78 % (ein Rückgang von 1,54 Prozentpunkten auf den niedrigsten Wert seit fast 15 Quartalen), Wistron mit 5,21 %, Wistron AI mit 7,2 % (im Vorjahreszeitraum 9,4 %).

[^14]: [Bruttomargen der taiwanesischen Zulieferer der zweiten Ebene (YuShan Securities)](https://vocus.cc/) — Die Bruttomargen der taiwanesischen Unternehmen mit höherem technologischem Anteil sind höher: Delta Electronics (Stromversorgung/Kühlung) hält über 60 % des AI-Server-Netzstrommarktes und erzielte in Q1 FY2026 eine Marge von 37 %; Unilinx (ABF Substrate) hält über 70 % des AI ASIC Substratmarktes und ist der einzige Lieferant für NVIDIA CoWoP Materialien, mit einer geschätzten Marge von 21,3 %.

[^15]: [Morgan Stanley: Wertschöpfungsmargen bei ODM-Montage sinken](https://newtalk.tw/) — Newtalk zitiert einen Bericht von Morgan Stanley vom 22. Mai 2026, der feststellt, dass die wertschöpfende Marge beim System-ODM-Assembly von 2,7 % bei GB300 auf etwa 1,9 % bei VR200 gesunken ist; der Wertbeitrag pro Rack stieg von ca. 108.000 USD bei GB300 auf 149.600 USD bei VR200. Anmerkung: Dies bezieht sich auf die wertschöpfende Marge des System-ODM und unterscheidet sich von der Gesamtgewinnmarge des Unternehmens (5–7 %).

[^16]: [Taiwan Insight: Die wohlhabende Wirtschaft Taiwans wird von den meisten Menschen nicht gespürt](https://taiwaninsight.org/) — Min-Hua Chiang von der University of Nottingham schrieb am 12. Januar 2026: „Die meisten Menschen in Taiwan spüren die Vorteile der florierenden Wirtschaft nicht.“ Der Top 10 % der Einkommensbezieher erhielten 48 % des Gesamteinkommens, während die untersten 50 % nur 12 % erhielten. Die geschätzte Wachstumsrate für 2025 beträgt 7,37 %, was sie zu einer führenden globalen Gruppe macht.

[^17]: [Bericht: K-förmige Spaltung im Zeitalter von KI](https://www.twreporter.org/) — Wang Yingda berichtete am 11. Juni 2026: „Die direkten Arbeitsplätze in den Hauptwachstumsbereichen wie KI, Halbleiter und Elektroniklieferketten machen weniger als 10 % der gesamten Beschäftigten aus.“ Das durchschnittliche Monatsgehalt im Gastgewerbe beträgt 38.484 NTD, was nur 34,6 % desjenigen in der Herstellung elektronischer Komponenten entspricht. Der Anteil der Elektronikindustrie am Umsatz der Fertigung ist von 58,0 % auf 64,7 % gestiegen.

[^18]: [The Nvidia Way: Nur noch dreißig Tage bis zum Bankrott](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Tae Kim's Werk und der Acquired/Sequoia Podcast; das interne Mantra von NVIDIA „Unser Unternehmen ist in dreißig Tagen bankrott“, wurde zu Beginn monatlicher Besprechungen verwendet. Bei der Lieferung der RIVA 128 im August 1997 hatte das Unternehmen nur etwa einen Monatslohn.

[^19]: [Sega rettete NVIDIA mit 5 Millionen Dollar](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Der Acquired Podcast und frühe historische Aufzeichnungen von NVIDIA zeigen, dass SEGA (SEGA) Ende der 1990er Jahre NVIDIA aus einer finanziellen Krise befreite, nicht Taiwan. Dies klärt die romantisierte Behauptung „Taiwan rettete NVIDIA“.

[^20]: [Jensen Huang schreibt Chang Chi-ming um Auftragsfertigung zu bitten](https://www.ettoday.net/) — ETtoday zitiert, dass Jensen Huang etwa 1996 einen Brief an den Gründer von TSMC, Chang Chi-ming, schrieb und fragte, ob „TSMC für NVIDIA den ersten Chip herstellen könnte“. Die beiden unterzeichneten 1998 einen Kooperationsvertrag, wodurch TSMC zum Hauptauftragnehmer wurde.

[^21]: [Tsai Yu-chieh von TSMC: Tiefe Zusammenarbeit begann 1997](https://technews.tw/) — TechNews berichtete am 19. Mai 2025, dass Tsai Yu-chieh von TSMC zurückblickte: „Die tiefe Zusammenarbeit begann zu einem entscheidenden Zeitpunkt, nämlich im Jahr 1997. Der Gründer von TSMC, Chang Chi-ming, kontaktierte persönlich den Gründer von NVIDIA, Jensen Huang, um die Auftragsfertigungsanforderungen von NVIDIA zu erfüllen.“

[^22]: [Szene, in der Jensen Huang Anrufe von Chang Chi-ming entgegennimmt (Zweitvermittlung)](https://www.businessweekly.com.tw/) — Eine Comicversion aus dem Business Weekly erzählt die Geschichte, wie Jensen Huang bei anderen rief: „Leute! Leise! Es ist Chang Chi-ming!“ Dies ist eine Zweitvermittlung und der Ton ist möglicherweise nicht präzise.

[^23]: [Fehler in TSMC im Jahr 1998 fast zerstörte NVIDIA](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) — Der Acquired Podcast und frühe historische Aufzeichnungen von NVIDIA zeigen, dass ein chemischer Prozessfehler bei TSMC im Jahr 1998 zur Vernichtung vieler Chips von NVIDIA führte und das Unternehmen fast erneut in den Ruin trieb – was das symbiotische Rahmenwerk „Taiwan ist die Lebensader der Fertigung, nicht der Rettungsanker des Bankrotts“ bestätigt.

[^24]: [AlexNet trainiert mit zwei GTX 580 Karten](https://en.wikipedia.org/wiki/AlexNet) — Wikipedia und Tom's Hardware: Im Jahr 2012 trainierte Alex Krizhevsky in seinem Elternhauszimmer AlexNet mit zwei NVIDIA GTX 580 Grafikkarten, reduzierte die Fehlerrate von ImageNet von 26 % auf 15,3 %, was zehn Prozentpunkte besser war als der zweitplatzierte und bewies, dass GPUs Deep-Learning-Engines sind. CUDA wurde 2006 veröffentlicht.

[^25]: [Blackwell/Rubin: 100% abhängig von CoWoS-L in Taiwan](https://finance.biggo.com/news/) — Industrieanalyse (Finanznachrichten), im Zeitraum 2025–2027 sind die fortschrittlichsten KI-GPUs von NVIDIA von der Herstellung bis zur Endverpackung zu 100 % auf der TSMC CoWoS-L-Produktionslinie in Taiwan abhängig.

[^26]: [TSMC kontrolliert weltweit etwa 90–92 % der fortschrittlichen Prozesse](https://www.csis.org/analysis/countering-chinas-challenge-american-ai-leadership) — CSIS Analyse: TSMC produziert weltweit etwa 92 % der fortschrittlichsten (unter 5 nm) Halbleiter, und die Kapazität für fortschrittliche Verpackung übersteigt die aller Konkurrenten; Kunden, von denen fast neunzig Prozent auf Taiwan angewiesen sind, umfassen Apple, Amazon, Google, NVIDIA und Qualcomm.

[^27]: [Yuntsai Chou von NTU: Kurzfristig nicht diversifizierbar von TSMC-Auftragsfertigung](https://www.sciencedirect.com/) — ScienceDirect, Studie von Yuntsai Chou (NTU) im Mai 2025: „Die Lieferkette Taiwans wäre besonders anfällig für eine Quarantäne vor 2027.“ „Die Diversifizierung der TSMC-Foundries ist kurzfristig nicht machbar. Der Bau einer neuen High-End-Fabrik dauert 3–4 Jahre und kostet über 10 Milliarden US-Dollar.“ Das Ziel von TSMC in Arizona für die Massenproduktion von 2 nm ist 2030.

[^28]: [United Daily News: Die zwei Sterne werden zu zweien schmerzhaften Unternehmen](https://udn.com/) — Die United Daily News blickt auf die „Zwei-Sterne“-Politik zurück: „Panelhersteller und Speicherhersteller, die einst glänzten, erlitten in den folgenden Jahren große Verluste aufgrund des Überangebots auf dem internationalen Markt und wurden von Netizens als ‚Maoshan Daoist‘ (Mao San Dao Si) bezeichnet, was bedeutet, dass die Gewinnspanne der Produkte nur drei bis vier Prozent beträgt. Die ‚Zwei-Sterne-Industrien‘ wurden zu ‚schmerzhaften Unternehmen‘.“ Panels und DRAM wurden durch Investitionen von nur 6 % (weit unter den 10–21 % von Korea, Japan, USA und Europa) ausgehöhlt.

[^29]: [SMIC: Die Ausbeute bei 5 nm ist nur ein Drittel der von TSMC](https://technews.tw/2025/03/28/) — TechNews berichtete am 28. März 2025: „Die 5-nm-Wafer von SMIC haben einen Preis, der 50 % höher ist als der von TSMC, und die Ausbeute ist aufgrund nur DUV-Ausrüstung nur 33 % der von TSMC.“ Obwohl für Dezember 2025 Massenproduktion angekündigt wurde, hinkt es etwa fünf Jahre hinterher.

[^30]: [NVIDIA investiert 5 Milliarden Dollar in Intel, um Verpackungskapazität zu sichern](https://www.intel.com/) — Im Dezember 2025 erwarb NVIDIA etwa 5 % der Anteile an Intel mit dem echten Ziel, „die Priorität bei der Sicherung der fortschrittlichen Verpackungskapazität von Intel in den USA zu gewährleisten“, bewertet für die Feynman-Architektur im Jahr 2028 als Reaktion auf den CoWoS-Engpass von TSMC. Es ist eine langfristige Absicherung und keine kurzfristige Alternative.

[^31]: [TSMC Arizona-Waferpaket-Fabrik AP1 in 2028 in Produktion](https://www.tomshardware.com/) — Industriebericht: Die TSMC-Waferpaket-Fabriken AP1/AP2 in Arizona werden Anfang 2026 gebaut, und AP1 wird voraussichtlich 2028 in Produktion gehen; derzeit müssen alle Chips (einschließlich der in Phoenix, Arizona, hergestellten) zur Verpackung nach Taiwan zurückgeschickt werden. Amkor in Arizona geht Anfang 2028 in Produktion.

[^32]: [Leading Edge PiFO-Verpackung konkurriert mit CoWoS-L](https://www.trendforce.com/news/) — TrendForce am 10. November 2025: „Die Advanced Packaging Technologie von PiFO – verglichen mit TSMC's CoWoS-L – ist zu einer Top-Alternative der Branche geworden“, die Glassubstrate bieten eine bessere Wärmeableitung und niedrigere Produktionskosten um etwa 30 %, viele US-KI-Chiphersteller sind begeistert und haben Aufträge bis 2027 eingeplant. Die Kunden sind jedoch „andere US-KI-Chiphersteller“ und nicht explizit NVIDIA's Haupt-GPUs.

[^33]: [TrendForce: Engpass bei CoWoS schrumpft durch eigene Kapazitätserweiterung von TSMC](https://www.trendforce.com/news/) — TrendForce am 15. Juni 2026: „Der Angebots-Nachfrage-Abstand bei CoWoS wird voraussichtlich signifikant von derzeit rund 20 % auf etwa 10 % bis Ende 2026 schrumpfen“, die monatliche Kapazität erreicht einen neuen Höchstwert von 120.000 bis 140.000 Einheiten im Jahr 2026; der Engpass wird durch die eigene Kapazitätserweiterung von TSMC und nicht durch Ersatzlieferanten behoben.

[^34]: [New Life versiegelt Nutzungsrecht für North Science T17/T18 in 2021](https://www.cna.com.tw/news/afe/202510035002.aspx) — Central News Agency: Die Stadtverwaltung von Taipei versteigerte am 2021 das Nutzungsrecht (50 Jahre) für North Science T17 und T18 (insgesamt 3,89 Hektar), wobei New Life der einzige Bieter war und die Flächen drei Jahre lang ungenutzt blieben.

[^35]: [Jensen Huang kündigt bei Computex 2025 Hauptsitz Constellation in North Science an](https://focustaiwan.tw/business/202505190009) — Focus Taiwan: Jensen Huang kündigte im Mai 2025 auf der Computex die internationale Zentrale „Constellation“ von NVIDIA in dem Technologiepark Shilin, Beitou, an. Die Investition beträgt über NT$40 Milliarden, die Bau beginnt 2026 und die Inbetriebnahme ist für 2030 geplant, mit über zehntausend Arbeitsplätzen.

[^36]: [NVIDIA, New Life und Stadtverwaltung von Taipei blockieren fünf Monate lang](https://news.pts.org.tw/article/777650) — CTV: Da das Nutzungsrecht für North Science T17/T18 bei New Life liegt und die öffentliche Übertragung des Nutzungsrechts nicht direkt möglich ist, waren die drei Parteien etwa fünf Monate beim Erwerb des Grundstücks festgefahren.

[^37]: [Taipei City Council genehmigt Entschädigung von 4,434 Milliarden](https://www.cna.com.tw/news/afe/202510035002.aspx) — Central News Agency: Der Taipei City Council stimmte am 12. November 2025 einstimmig der Vertragsstrafe in Höhe von NT$4,434,064,085 zu, die von der Stadtverwaltung an New Life gezahlt wird, um das Nutzungsrecht am 28. Dezember aufzuheben.

[^38]: [You Shu-hui kritisiert die Abrechnung von New Life](https://www.nextapple.com/) — iFine News (über WebFetch überprüft): Die Fraktionsmitglieder des Kuomintang, You Shu-hui, lachte bitter, als sie sah, dass der Stadtverwaltung von Taipei Kosten für Unkrautbekämpfung, Umweltpflege, Logoanpassung und Agenturgebühren in der 8-seitigen Rechnung von New Life zahlen muss; sie sagte: „Die Abrechnung an New Life ist unsinnig, aber das große Ganze ist wichtiger“.

[^39]: [Rechtliche Laiensprache: Parlamentarische Parteien einigen sich beim Vertragsaufhebungsfall](https://plainlaw.me/) — Bewegung der Rechts-Laiensprache: „Am 12. November stimmte der Taipei City Council einstimmig über die Vertragsstrafe in Höhe von 4,434 Milliarden; während des Prozesses arbeiteten alle Parteien harmonisch zusammen, und die Fraktion der DPP rief sogar ‚Unterstützt Nvidia, unterschreibt schnell‘“, Vorsitzender Dai Xi-qin „nahm ohne Einspruch zur Kenntnis“ und es gab Applaus.

[^40]: [Analyse der Vertragsstrafe von 4,434 Milliarden](https://www.nextapple.com/) — iFine News und die beauftragte Wirtschaftsprüferin der Stadtverwaltung von Taipei berechneten, dass New Life ursprünglich rund 3,3 Milliarden gezahlt hatte (ohne Bau für 3 Jahre), aber in der Abrechnung 4,47 Milliarden forderte (einschließlich Unkrautbekämpfung, Logoanpassung und Zaunkosten); der Wirtschaftsprüfer kürzte dies auf 4,434 Milliarden, wobei NVIDIA die eigenen Kosten von New Life und die bereits gezahlten Steuern in Höhe von 1,441 Milliarden übernimmt.

[^41]: [Stadtentwicklungskommission genehmigt Entwurf für den Hauptsitz Constellation-Schiffdesign](https://www.cna.com.tw/news/) — Central News Agency am 26. Januar 2026: T17 (2,29 Hektar) und T18 (1,6 Hektar) wurden zusammengelegt; die Bebauungsdichte wurde von 50 % auf 70 %, der Geschossflächenzahl von 300 % und die Höhe auf 119,5 Meter erhöht. Das Design im Stil des amerikanischen Hauptsitzes „Constellation“ hat eine Grünbedeckung von 80 % und beherbergt etwa 4.000 Personen; Bau Ende 2026, Inbetriebnahme 2030.

[^42]: [NVIDIA beschäftigt derzeit rund 1.800 Mitarbeiter in Taiwan](https://www.digitimes.com/news/a20250519PD231/) — Medien wie Digitimes schätzen, dass NVIDIA im Büro in Neihu, Taipei (No. 8 Jiho Road) etwa 1.800 Mitarbeiter hat und drei Tochtergesellschaften unterhält; dies ist eine Schätzung der Medien und keine offizielle Zahl.

[^43]: [NVIDIA AI Innovations-Forschungszentrum geplant](https://focustaiwan.tw/business/202505190009) — Focus Taiwan und das Ministerium für Wirtschaft: NVIDIA erhielt 2021 die Genehmigung für ein „AI Innovations-Forschungszentrumsprojekt“ mit einer Gesamtinvestition von 24,3 Milliarden und staatlicher Förderung von 6,7 Milliarden; es wird erwartet, dass im Zeitraum 2022–2027 1.000 Entwickler eingestellt werden.

[^44]: [Taiwan Nvidia Classic Co., Ltd. gegründet](https://www.cna.com.tw/news/afe/202510035002.aspx) — Central News Agency: NVIDIA gründete am 2025 den „Taiwan Nvidia Classic Co., Ltd.“ mit einem Kapital von 3,3 Milliarden (erhöht von 1 Milliarde), das als eigenständige juristische Person steuerlich selbstständig ist und Vermögen halten kann.

[^45]: [Standard & Poor's: TSMC-Stromverbrauch könnte bis 2030 23,7 % des gesamten Landes ausmachen](https://theinitium.com/20250912-international-tsmc-energy-explainer/) — End Media und Standard & Poor's: Der Stromverbrauch von TSMC betrug im Jahr 2023 24,775 Milliarden kWh, was 8,96 % des gesamten Landes (16,2 % in der Industrie) entspricht; 2024 wurden 27,456 Milliarden kWh verbraucht, wobei nur 14,1 % aus erneuerbaren Energien stammten; S&P prognostiziert bis 2030 einen Anteil von 23,7 % am Gesamtverbrauch.

[^46]: [Greenpeace: Schatten nach dem Chip-Boom](https://www.greenpeace.org/taiwan/press/44037/) — Bericht von Greenpeace vom 10. April 2025 (wörtlich überprüfbar): Der Stromverbrauch für die globale AI-Chip-Herstellung stieg von 218 GWh auf 984 GWh (ein Anstieg von über 3,5-fach), wobei Taiwan mit 375,8 GWh einen enormen Verbrauch verzeichnete und „bis zu 38 % des globalen Gesamtverbrauchs“ ausmacht; TSMC ist der „Kohlenstoffemissionsmeister“ mit 185.700 Tonnen CO2-Emissionen für KI-Chips; NVIDIA wird als Klasse F bewertet, und die Emissionen der Lieferkette stiegen in drei Jahren von 3,51 Millionen auf 6,91 Millionen Tonnen an, was „nur eine Verlagerung der Kohlenstoffemissionen und Verschmutzung der Lieferkette auf andere Teile der Welt“ darstellt.

[^47]: [Naides Wasser fast vollständig für TSMC in Tainan](https://theinitium.com/20250912-international-tsmc-energy-explainer/) — Endmedia: Täglich verbraucht TSMC über 200.000 Tonnen Wasser (56.000 in Hsinchu, 53.000 in Hsinchu Science Park, 99.000 in Southern Taiwan Science Park); die Aufbereitungsanlage von Tainan liefert täglich 81.000 Tonnen „fast vollständig an TSMC“.

[^48]: [Landwirtschaft in Chiayi und Nanhua: Wasser für Halbleiter statt Bewässerung im Jahr 2021 und 2023](https://theinitium.com/) — Berichte von Endmedia etc. berichten, dass die landwirtschaftlichen Flächen in der Region Chiayi und Nanhua zweimal (2021 und 2023) bewässert wurden und das Bewässerungswasser für die Halbleiterindustrie umgeleitet wurde.

[^49]: [8.327 Liter Wasser pro 12-Zoll-Wafer](https://www.greenpeace.org/taiwan/) — Greenpeace und Branchendaten geben an, dass zur Herstellung eines 12-Zoll-Wafers etwa 8.327 Liter Wasser benötigt werden.

[^50]: [60.000 Arbeitsplätze in Beitou fordern 1.476 Wohneinheiten](https://house.udn.com/house/story/123590/8769929) — Immobilienbericht von Economic Daily: Das Taiwan-Stadtentwicklungsbüro schätzt, dass bis zu 60.000 beschäftigte in Beitou leben könnten, aber nur etwa 1.476 verkaufte Wohnungen sind verfügbar, und der Wohnraum macht nur 13,8 % des gesamten Gebiets aus.

[^51]: [Neue Projekte im Kerngebiet von Beitou erzielen über 1,5 Millionen pro Quadratmeter](https://www.ctee.com.tw/news/20260603701575-430601) — Geschäftsmagazin berichtet im Juni 2026, dass neue Projekte in zentralen Lagen von Beitou über 1,5 Millionen pro Quadratmeter verkauft wurden; „60.000 Menschen kämpfen um 1.500 Wohnungen“, und die Einheimischen befürchten Staus wie in Neihu und hinterfragen, warum Preise steigen, bevor überhaupt gebaut wurde.

[^52]: [Echte Transaktionsdaten: Höchster Preis für Wohnungen in Shilin beträgt 1,88 Millionen pro Quadratmeter](https://lvr.land.moi.gov.tw/) — Online-Datenbank des Innenministeriums zu Immobilientransaktionen zeigt, dass die höchste Transaktion für ein Mehrfamilienhaus in Shilin im Jahr 2025 bei 570.400 TWD/m² (ca. 1,88 Millionen pro Quadratmeter, Adresse: No. 39 Jihe Road, Gesamtpreis 447 Millionen TWD) lag, mit mehreren Fällen über 1,5 Millionen/Quadratmeter; Anmerkung: Dies bezieht sich auf Luxusimmobilien in Tianmu und Shilin City, nicht auf Beitou selbst.

[^53]: [Unternehmen: Schlechte Lebensqualität im Parkgebiet führt zu Kündigungen von einem Drittel der Mitarbeiter](https://house.udn.com/house/story/123590/8769929) — Immobilienbericht von United Daily zitiert eine anonyme Quelle (Unternehmer): „Viele Mitarbeiter wollen nicht in das Gebiet ziehen, weil die Lebensqualität schlecht ist... und selbst nach dem Umzug kündigen ein Drittel der Mitarbeiter wegen schlechter Verkehrsanbindung“; der Leiter des Verkehrsamtes, Xie Ming-hung, sagte, dass drei zusätzliche Betriebsrouten für Beitou bewertet werden.

[^54]: [Anonyme Meinung auf PTT: Themenwechsel zu Nvidia](https://www.ptt.cc/) — Anonyme Diskussion auf PTT (nicht persönlich nachverfolgbar): „Die TSMC-Themen sind langweilig geworden, jetzt wird das Nvidia-Thema verwendet“; „Wohnen die Ingenieure aus Neihu alle in anderen Bezirken, werden sie dann alle nach Beitou ziehen? Das ergibt keinen Sinn?“

[^55]: [Debatte um 'Silicon Shield' und 'Silicon Trap'](https://www.researchgate.net/) — Forschung auf ResearchGate im Jahr 2025 untersucht die Dualität der Konzentration von Halbleitern in Taiwan, die sowohl eine abschreckende Schutzfunktion ('Silicon Shield') als auch einen Anreiz zur Invasion/Single Point of Failure ('Silicon Trap') darstellt.

[^56]: [Gegenargumente zu 'Nestzerstörung'/'Bodenverbrennung'-Strategien](https://thenewslens.com/) — The News Lens und Parameters der US Army War College (McKinney & Harris, 2021) diskutieren die Theorie und Gegenargumente von „Broken Nest“: „Wirtschaftliche Selbstverletzung, selbst wenn sie kurzfristig China davon abhalten kann, verzögert möglicherweise nur die chinesische Aggression, bis China seine eigenen Ziele bei der Halbleiterproduktion erreichen kann“, und „es ist unwahrscheinlich, dass die taiwanesische Öffentlichkeit einen solchen Sabotageakt als im eigenen Interesse ansehen würde“.

[^57]: [TSMC baut für 165 Milliarden US-Dollar in den USA aus](https://www.foreignaffairs.com/) — TSMC kündigte eine Investition von insgesamt 165 Milliarden US-Dollar (65 Milliarden + 100 Milliarden) zur Diversifizierung geopolitischer Risiken in Arizona, USA an.

[^58]: [MIT Technology Review: Taiwans 'Silicon Shield' könnte schwächer werden](https://www.technologyreview.com/) — Die MIT Technology Review vom 15. August 2025 berichtet: „Nun befürchten einige taiwanesische Spezialisten und Bürger, dass dieser ‚Silicon Shield‘, falls er jemals existierte, bröckelt.“ Die Sorge ist, dass die Verlagerung der Kapazitäten das lokale Kapital Taiwans verwässert.

[^59]: [Bonnie Glaser: Das taiwanische Ökosystem lässt sich nicht replizieren](https://www.technologyreview.com/) — Die MIT Technology Review zitiert Bonnie Glaser vom Marshall Institute in Deutschland: „Das von ihnen geschaffene Ökosystem ist wirklich einzigartig. Es ist eine Funktion des Talentpools, der Kultur und der Gesetze in Taiwan; es kann nirgendwo leicht repliziert werden.“

[^60]: [Paul Triolo: Arizona wird niemals das Niveau erreichen](https://www.technologyreview.com/) — Die MIT Technology Review zitiert den Technologiepolitikexperten Paul Triolo, der die TSMC-Fabrik in Arizona bewertet: „Arizona ist noch nicht dort und wird es nie sein.“

[^61]: [Jensen Huang: Taiwan ist eines der wichtigsten Länder der Welt](https://www.cna.com.tw/) — Zhonghua News berichtet, dass Jensen Huang am 29. Mai 2024 in Taiwan öffentlich erklärte: „Taiwan is one of the most important countries in the world.“ (Original englischer Text).

[^62]: [Computex 2024 TAIST-Vortrag: Taiwan ist eine unbekannte Säule der Welt](https://www.tbotaiwan.com/) — Der vollständige Vortrag von Jensen Huang bei Computex an der National Taiwan University im Jahr 2024, mit dem abschließenden Videotext: „Taiwan ist ein unbekannter Held und eine Säule der Welt.“ „Danke, Taiwan!“ „Taiwan ist ein Zentrum unserer sehr wertvollen Partner; alles bei NVIDIA beginnt hier.“

[^63]: [Staatskanzlei China antwortet auf Huangs Äußerungen](https://zh.wikinews.org/) — Wiki News: Chen Binhua, Sprecher der Staatskanzlei China (18 Tage nach dem Vorfall): „Die Volksmenge und Netizens in China haben starke Unzufriedenheit über diese extrem falschen Äußerungen gezeigt. Taiwan ist nie ein Land … wir hoffen, er soll Nachhilfe nehmen.“

[^64]: [Zhonghua News: Chinesische Medien dämpfen Huangs Aussage „Taiwan ist ein wichtiges Land“](https://www.cna.com.tw/) — Zhonghua News vom 3. Juni 2024: „Diese Finanzmedien haben viele verwandte Berichte veröffentlicht, aber es wird nicht erwähnt, dass Jensen Huang gesagt hat, ‚Taiwan ist ein wichtiges Land‘; dies scheint ein sensibles Thema zu sein, das normalerweise als ‚äußerst wichtig‘ angesehen wird.“

[^65]: [Experten: China braucht Nvidia, aber Nvidia braucht China nicht](https://www.voacantonese.com/a/china-s-media-turned-a-blind-eye-to-jensen-huang-s-statement-20240607/7646642.html) — Voice of America (Kantonesisch) zitiert Expertenkommentare und analysiert die Dämpfung der Äußerung von Jensen Huang „Taiwan ist ein wichtiges Land“ durch chinesische Finanzmedien als eine asymmetrische Beziehung: „China braucht Nvidia, aber Nvidia braucht China nicht.“

[^66]: [Lai Ching-te: Die Top 5 globalen Rechenzentren und souveräne KI](https://www.bnext.com.tw/article/79391/sovereign-ai) — Digital Age: Lai Ching-te legte im Oktober 2025 das Ziel vor, Taiwan zu einem „einer der weltweit führenden fünf Rechenzentren“ zu machen und eine „souveräne KI“ zu entwickeln.

[^67]: [Foxconn baut zehntausend Blackwell Supercomputer für die Nation](https://blogs.nvidia.com.tw/blog/foxconn-ai-factory-tsmc-taiwan-nvidia/) — NVIDIA Taiwan Blog: Foxconn (Big Innovation Company) baute in Kaohsiung einen nationalen Supercomputer, der 10.000 Blackwell-Chips und über 90 Exaflops verwendet und mit TSMC und dem National Science and Technology Council zusammenarbeitet, um die erste KI-Fabrik Taiwans zu schaffen.

[^68]: [Die AI New Ten Major Projects des Exekutivrates](https://iknow.stpi.niar.org.tw/post/Read.aspx?PostID=21832) — STPI iKnow: Das „AI New Ten Major Projects“ des Exekutivrates plant, bis 2040 über 100 Milliarden TWD zu investieren und ein Produktionsvolumen von 15 Billionen zu erreichen.

[^69]: [TAIDE wie ein Highschooler, internationale Großunternehmen sind Studenten](https://www.cw.com.tw/article/5137534) — Asia Times: Das lokale Sprachmodell TAIDE in Taiwan wird als „ähnlich einem Highschooler“ beschrieben, während internationale Großunternehmen bereits auf Studierendeniveau seien; das Budget für die Planung von TAIDE ist weniger als die Kosten eines einzelnen Trainingszyklus internationaler Modelle; TAIDE startet mit 9 (72) H100s.

[^70]: [Südkorea kauft 260.000 GPUs](https://www.cw.com.tw/) — Asia Times und Branchenberichte: Die südkoreanische Regierung kaufte direkt 260.000 GPUs, was im Kontrast zur relativen Zögerlichkeit bei der politischen Entscheidungsfindung in Taiwan steht.

[^71]: [Jensen Huang Computex 2026: Jährliche Ausgaben in Taiwan belaufen sich auf etwa 150 Milliarden US-Dollar](https://cryptobriefing.com/nvidia-150b-taiwan-silicon-shield-ai/) — Cryptobriefing und Reuters: Jensen Huang enthüllte bei Computex 2026, dass NVIDIA jährlich etwa 150 Milliarden US-Dollar in Taiwan ausgibt (im Vergleich zu nur 10–15 Milliarden vor fünf Jahren), wobei die Lieferkette von Vera Rubin verdoppelt wurde und 150 Unternehmen in Taiwan beteiligt sind; TSMC produziert weltweit etwa 90 % der fortschrittlichsten Prozesse.
