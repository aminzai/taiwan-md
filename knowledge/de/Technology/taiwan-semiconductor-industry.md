---
title: 'Halbleiterindustrie: Eine 50-jährige Materialrevolution von der RCA-Technologietransferzeit zu GaN und Quantenverpackung'
description: 'Taiwan ist als Auftragsfertiger mit fortschrittlichen Prozessen weltweit führend, doch die Materialwissenschaften der nächsten 50 Jahre beginnen erst jetzt: GaN im Schnellladen, CoWoS im KI-Chip-Ökosystem und Kryomodulation über Quantenbits.'
date: 2026-03-17
category: 'Technology'
tags:
  [
    'Halbleiter',
    'TSMC',
    'Taiwan Semiconductor Manufacturing Company',
    'Gallium Nitride',
    '3D-Verpackung',
    'CoWoS',
    'Quantencomputer',
    'Fortschrittliche Prozesse',
    'Siliziumshield',
    'Materialwissenschaft',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md'
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: '6ffd92f94'
sourceContentHash: 'sha256:c91074d5ba69e3b2'
translatedAt: '2026-08-12T16:22:42.438418+00:00'
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
difficulty: 'intermediate'
readingTime: 22
image: '/article-images/technology/silicon-vs-gan-charger-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg'
sporeLinks:
  - id: 87
    platform: 'threads'
    date: '2026-05-25'
    url: 'https://www.threads.com/@taiwandotmd/post/DYvqEURgXm-'
  - id: 88
    platform: 'x'
    date: '2026-05-25'
    url: 'https://x.com/taiwandotmd/status/2058735515021783190'
---

# Halbleiterindustrie: Von der RCA-Technologietransfers-Ära zu einer 50-jährigen Materialrevolution durch GaN und Quanten-Verpackung

![Vergleich zweier 30W-USB-C-Ladegeräte mit gleicher Leistung, nebeneinander: links das deutlich größere Silizium-basierten Ladegerät, rechts die etwa halb so große GaN-Variante. Das zeigt, wie Materialwissenschaft die Energiedichte in die Handfläche bringt.](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Si vs. GaN USB-C-Ladegeräte mit gleicher Leistung im Volumenvergleich. Photo: 4300streetcar, 2025-12-25. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **30-Sekunden-Übersicht:** TSMC startete im vierten Quartal 2025 in Fab 22 in Kaohsiung die Serienproduktion von 2 Nanometern und liegt damit drei Halbleiter-Generationen vor der Welt[^2]. Doch die Geschichte spielt sich nicht nur im ständigen Verkleinern von Transistoren ab: In deinem Rucksack sitzt ein GaN-Schnellladegerät, in Zhongli fertigt GlobalWafers 8-Zoll-SiC-Wafer, und NVIDIAs Blackwell-GPUs laufen mit TSMC-CoWoS-Verpackung im Rechenzentrum. Von der 1973 für 4,5 Millionen Dollar gekauften RCA-Technik durch das ITRI[^5] bis zum 20-Qubit-supraleitenden Quantenchip von Academia Sinica 2026[^6] durchläuft Taiwan einen Strom der Materialwissenschaft von Bandlückenphysik über atomare Schichtabscheidung bis zu topologischen Qubits. Taiwan gewinnt mit 50 Jahren Auftragsfertigungserfahrung, aber die Position als Auftragsfertiger im Quantum-Zeitalter ist noch nicht gesichert.

An einem Nachmittag im Jahr 1985 suchte Ex-Minister Li Guoding (李國鼎) den gerade aus der Rückkehr nach Taiwan eingetroffenen neuen ITRI-Präsidenten Morris Chang im Verwaltungsorgan. Li sagte ohne Umschweife: „Wir wollen ein gigantisches Unternehmen für integrierte Schaltkreise aufbauen und Sie sollen es leiten.“

Morris Chang war für einen Moment sprachlos. Er dachte, er sei nur als neuer ITRI-Vorstand bestellt; zwei Wochen später jedoch wurde er mit der Gründung eines Unternehmens betraut, dessen Geschäftsmodell niemand zuvor versucht hatte.

Diese Unterhaltung veränderte die Welt. Doch vier Jahrzehnte später ist klar: „die Welt“ war weit größer als dieser Nachmittag. Sie umfasst das 65-Watt-Ladegerät im Rucksack, das kaum zwei Finger breit ist, jede Blackwell-GPU, die NVIDIA in Rechenzentren verschlingt, und auch den Quantenbit im Labor von Academia Sinica, der erst nahe dem absoluten Nullpunkt „aufwacht“.

## Die Auftragsfertigungswette 1987

![Außenansicht des TSMC-Fabs 5 im Wissenschaftsparc Hsinchu, eine mehrstöckige Industrieanlage mit Verbindung zur Guangfu Road, ein typisches Werksgebiet aus dem Expansionszeitalter der 1990er.](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Hsinchu Science Park, TSMC Fab 5, 2010. Photo: Peellden. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

Die Geschichte beginnt viel früher. 1973 zahlte das ITRI 4,5 Millionen Dollar und erwarb Halbleitertechnik von der US-amerikanischen Firma RCA; 19 Ingenieurinnen und Ingenieure wurden in die USA entsandt, um dort ausgebildet zu werden[^5]. Damals ahnte niemand, dass dieses „Schulgeld“ zum Grundstein des taiwanischen Halbleiterreiches werden würde. 1980 führte die Technologietransferinitiative des ITRI zur Gründung von UMC, Taiwans erster Halbleiterfirma. Doch Li Guoding war unzufrieden: UMC war zu klein, die Technik hinkte hinter dem Weltstandard her und Taiwan brauchte einen größeren Sprung.

Am 21. Februar 1987 gründete Morris Chang im Hsinchu Science Park die Taiwan Semiconductor Manufacturing Company und etablierte ein bis dahin unbekanntes Geschäftsmodell: **Pure-Play-Fertigung**.

Die Idee klang damals verrückt. Weltweit arbeiteten Halbleiterkonzerne vertikal integriert – alles von Design bis Fertigung in einem Unternehmen. Wie konnte man nur fertigen, ohne selbst zu designen? Würden Kunden wirklich ihre vollständig vertraulichen Layouts an ein fremdes Haus abgeben?

Morris Changs Logik war einfach: Die Branche wurde immer komplexer; Design und Fertigung sind zwei vollständig unterschiedliche Disziplinen. Anstatt alles zu machen und nichts perfekt, besser nur ein Ding perfekt beherrschen und die Chipfertigung global bestmöglich ausführen.

Die frühe Eigentümerstruktur von TSMC war geschickt: Der Staat hielt 48,3%, Private 24,2% und Philips aus den Niederlanden 27,6%[^1]. Philips spielte eine Schlüsselrolle. Die Halbleiterbranche war damals von den USA und Japan dominiert; Europa brauchte dringend Alternativlieferanten. Philips investierte nicht nur, sondern vergab auch eigene Chipaufträge an TSMC und wurde so zum ersten wichtigen Kunden.

Das Fertigungsmodell verursachte eine neue Arbeitsteilung in der Halbleiterindustrie: IC-Designfirmen fokussierten auf das Entwerfen (Qualcomm, NVIDIA, MediaTek), Auftragsfertiger auf die Produktion (TSMC, UMC, GlobalFoundries), Packaging- und Testanbieter auf das End-Assembly (ASE, SPIL). Früher konnten nur Schwergewichte wie Intel oder IBM die astronomischen Investitionen in Fabs stemmen; nun konnte jedes Startup mit guter Idee Chips entwerfen und sie von TSMC fertigen lassen.

Der Kern der Auftragsfertigung ist Vertrauen. Kunden müssen glauben, dass TSMC ihre Designs nicht stiehlt, keine Geheimnisse offenbart und nicht mit ihnen konkurriert. TSMC etablierte eine Vier-Säulen-„Vertrauensregel“: Technologische Neutralität (niemals eigene Chip-Designs), Gleichbehandlung der Kunden (gleiche Technologie und Service für alle), höchste Geheimhaltungsstandards und faire Kapazitätszuteilung. Diese Regeln wurden rund 40 Jahre lang nahezu ohne Ausnahme gehalten.

> 📝 **Kurator-Notiz:** In Taiwan 1987 waren die 19 Ingenieure, die aus dem ITRI-Abkommen mit RCA kamen, gerade Anfang vierzig. Sie lernten in den 1960er-Jahren US-amerikanische Siliziumprozesse – niemand ahnte, dass sie drei Jahrzehnte später zu Schlüsselakteuren der Global-Foundry-Verpackung würden. Dass TSMC bewusst auf das „Selbst-Disziplinierungs“-Prinzip verzichtete, eigene Chips zu designen, wurde zu einem Band, an dem Menschen wie Jensen Huang, Tim Cook und Lisa Su nicht mehr vorbeikamen. Die Bedeutung des Auftragsfertigungsmodells liegt nicht im, was es tut, sondern im, was es **nicht** tut. Geht man noch weiter zurück: 1947 erfanden die Bell Labs den Transistor, 1958 bauten Texas Instruments und Fairchild eigene integrierte Schaltungen, und 1949 brachte die Übersiedlung der Regierung nach Taiwan eine Generation technischer Bürokraten mit naturwissenschaftlich-technischem Hintergrund mit (später das Rückgrat des ITRI) – das RCA-Geschenk von 4,5 Millionen Dollar war ein Staffelstab, nicht der Startschuss.

## Lin Benjian und ASML: Das Wette-Spiel zweier Außenseiter im Wasser-Expositionsgeschäft

Die Auftragsfertigung war nicht nur ein TSMC-Thema. Leser\*in [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) ergänzte diesen wichtigen historischen Strang in der Kommentarspalte: TSMCs „Blutsverwandter“ über Philips ist ebenfalls ASML – 1984 aus Philips ausgegliedert und heute der weltweit einzige Anbieter von EUV-(extreme ultraviolet)-Belichtungssystemen. Beide Unternehmen galten vor 30 Jahren als Außenseiter, die von Branchenriesen ignoriert wurden[^asml-philips].

Die zentrale Figur ist ein taiwanischer Ingenieur namens Lin Benjian (Burn J. Lin). Ab 1992 arbeitete er am IBM Watson Research Center an Lithografie-Technik und wechselte 2000 in die TSMC-Forschung, wo er Leiter der R&D wurde[^lin-bio]. Damals stritten sich die Industrieakteure darüber, ob im nächsten Schritt 157-nm-DUV die Norm werden solle. Nikon und Intel setzten darauf, doch 157nm hatte Probleme: Calciumfluorid-Linsen litten unter Doppelbrechung, Dünnfilme absorbierten diese Wellenlänge zu stark, und die Prozesse waren schwer integrierbar[^157nm-fail].

2002 legte Lin im SPIE-Optik-Kongress eine Idee vor, die zunächst verrückt wirkte: „Behalte die 193-nm-Lichtquelle bei, aber fülle den Spalt zwischen Linse und Wafer mit Wasser.“ Die Brechzahl von Wasser liegt bei 1,44 – bei 193 nm ergibt sich effektiv etwa 134 nm Auflösung im Wasser, feiner als 157 nm – ohne Wechsel der Lichtquelle oder der Optik[^immersion-litho].

Nikon traute sich nicht auf diese Wette; ASML tat es schon – wie auch TSMC ein Außenseiter war und auf einen Hebel in der Physik wartete. 2003 begann ASML mit der Entwicklung der 193nm-Immersion-Lithographie (193i), 2007 die erste Serienauslieferung; sie stützte von 65 nm bis heute sechs Prozessgenerationen bis zum heutigen EUV-Nachfolger[^immersion-litho][^cw-lin-interview].
„Nikon wagte es wegen der Thermikprobleme nicht, Immersion zu wagen; ASML und wir mussten es selbst entwickeln“, so die Erzählung. Diese Technologielinie stieß Nikon vom Thron der Belichtungsmaschinen. Vor 30 Jahren setzten zwei Außenseiter auf ihre Karten – heute ist der eine der weltweit einzige EUV-Maschinenhersteller, der andere die weltweit einzige 2-nm-Auftragsfertigung. Zwei Saatkörner aus Philips prägen gemeinsam das 21. Jahrhundert.

## 50 Jahre Materialgenealogie: Von Silizium zu GaN und topologischen Supraleitern

Um die Halbleiterlandschaft 2025 zu verstehen, muss man eine physikalische Linie verstehen, die selten sauber erklärt wird.

Silizium (Si) war der Ausgangspunkt. Seine „Bandlücke“ beträgt 1,1 Elektronenvolt (eV), die Mindestenergie, die ein Elektron braucht, um vom Leitungsband ins Valenzband überzugehen. Die kleine Bandlücke macht Chips gut herstellbar, aber setzt zwei Grenzen: Hohe Spannung kollabiert, hohe Frequenz produziert Wärme. PanSci formulierte es klar: „Für auf Silizium basierende Halbleiter liegt die Work-Frequenzgrenze nur unter 100k; oberhalb dieser Grenze sinkt die Effizienz deutlich und es treten gravierende Energieverluste auf.“[^7]

Die Bandlücke von Gallium-Nitrid (GaN) beträgt 3,4 eV, also das Dreifache von Silizium. Die Durchbruch-Spannungsgrenze ist zehnmal höher. Die Arbeitsfrequenz kann auf 1000K steigen – eine ganze Größenordnung mehr als bei Silizium[^7]. Physikalisch übersetzt bedeutet das: Bei gleicher Leistung können Transformatorspulen bei GaN deutlich kleiner ausfallen und die Kühlanforderungen sinken deutlich. So entstehen die kompakten Ladegeräte für die Handfläche.

Siliziumkarbid (SiC) geht einen anderen Weg. Auch es ist ein Wide-Bandgap-Material (3,26 eV), zeigt aber höhere Temperatur- und Spannungsstabilität. PanSci nennt den Einsatzbereich klar: „SiC verfügt unter hoher Temperatur und hoher Spannung über gute Stabilität. Besonders mit steigender Nachfrage nach ultraschnellem E-Mobilitätsladen wird oberhalb von 1000 Volt, wo Siliziumhalbleiter nur 600 Volt tragen, der Bereich, in dem SiC Schlüsselbauteile übernehmen wird.“[^7]

> 💡 **Wusstest du:** Die „Bandlücke“ eines Halbleiters bestimmt, welche Spannung er aushält, wie schnell er arbeiten kann und wie viel Wärme entsteht. Siliziums 1.1 eV ist das Fundament der Konsumelektronik seit 50 Jahren; GaN mit 3.4 eV trägt 240-Watt-Schnelllader; SiC mit 3.26 eV steigt in 800-Volt-Inverter für Elektroautos ein; die nächste Stufe könnte Diamond mit 5.5 eV sein. Die gesamte Materialsequenz ist eine Leiter mit steigender Energiedichte – und Taiwan muss sich bei jedem Schritt mit den physikalischen Grenzen auseinandersetzen.

Die nächste Stufe ist noch nicht benannt: Möglich sind Diamant (C, 5.5 eV), Galliumoxid (Ga₂O₃, 4.8 eV) oder ein völlig anderer Mechanismus wie topologische Supraleiter – so geht Microsoft im Februar 2025 bei dem Quantenprozessor Majorana 1 vor[^15]. Ändert sich die Physik, wird die ganze Lieferkette neu geschrieben.

## Dein GaN-Schnellladegerät

Richte den Blick zurück auf deinen Rucksack.

Der Ladeadapter eines Nokia 3310 hatte 4,56 Watt. 2025 sind es 240 Watt bei Schnellladern. PanSci hat diese Zeitleiste so beschrieben: „Heute erreichen die angesagtesten GaN-Schnellladegeräte 65 Watt, ein Faktor 13, wodurch die Ladezeit theoretisch auf ein Dreizehntel sinkt.“[^7] Noch extremer: Die chinesische Marke realme brachte Anfang 2023 den GT Neo5 mit 240-Watt-Superschnellladen auf den Markt – damit steigt der Faktor auf über 50.

Diese Wachstumskurve basiert auf dem Wechsel zu GaN – bei sinkender Leiterdicke und kleinerer Batteriegröße. Höhere Leistung bei kleinerem Volumen wäre direkt erreichbar durch höhere Frequenz, aber wie PanSci schrieb: „Für auf Silizium basierende Halbleiter liegt die Frequenzgrenze unter 100k“[^7], genau die Siliziumgrenze. GaN hebt die Frequenz auf über 1 MHz, wodurch Transformator und Induktor zugleich schrumpfen. So passt das Ladegerät in die Tasche.

Das Problem: Als Taiwans Schnelllade-Markt gerade zu boomen begann, kündigte TSMC an: **Im Juli 2027 aus der GaN-Auftragsfertigung auszusteigen**[^8].

Hinter dieser Entscheidung stehen zwei Kräfte. Erstens expandierten chinesische GaN-Hersteller (Huaren Micro, Silan Micro, Ruilene etc.) massiv und drückten die Fertigungspreise unter die TSMC-Schwelle. Zweitens sind die Margen von KI-Chips so attraktiv, dass TSMC die GaN-Fabs in fortschrittliche Packaging-Linien (CoWoS) umbauen wollte. Die Technologie wurde an VIS (WorldWide) und GlobalFoundries lizenziert; die taiwanische GaN-Auftragsfertigung wurde damit an 穩懋（3163） und 宏捷科（8086） abgegeben, die schon vor zehn Jahren darauf gesetzt hatten[^8].

> ⚠️ **Kontroverse Sichtweise:** Der Ausstieg von TSMC aus GaN wird von außen meist auf zwei Weisen gelesen. Eine Seite sieht es als rationale Entscheidung für KI – mit einem ein-Wafer-Ertrag von über 20-fach beim 3-nm-Prozess gegenüber 6-inch-GaN; Kapazität wird folglich der renditestärkeren Nutzung zugewiesen. Die andere Seite wirft ein, Taiwan gebe bei GaN die nächste Generation der Konsumelektronik (Smartphones, Laptops, Ladegeräte) an chinesische Produzenten ab: Ist der „Si-Lenker“ dann nur noch der KI-Bereich? Der Unterschied liegt in der Frage, ob man Taiwan als unersetzliche Spitzenfertigung oder als vollständiges Ökosystem einer Lieferkette versteht.

Ob es TSMC oder GlobalWafers ist, ob ein großer taiwanischer oder internationaler Player – alle großen Halbleiterkonzerne sind längst in diesen Zug eingestiegen[^7]. Aber in welchem Waggon der Zug sitzt man?

## GlobalWafers und die SiC-8-Zoll-Wafer

Ist GaN die Geschichte des Mobiltelefonschnellladens, ist SiC die Geschichte von Elektrofahrzeugen.

Der zentrale taiwanische Player dieser SiC-Linie ist GlobalWafers, nicht TSMC. 2024 brachte GlobalWafers die Kapazität für 6-Zoll-SiC-Wafer auf rund 20.000 Stück pro Monat, die eigenen CZ-Anlagen wurden von 3 auf 20 Reaktoren hochskaliert, und die Ausbeute überschritt 50%[^9]. 2025 begann die Massenproduktion von 8-Zoll-SiC-Wafer – die erste in Taiwan.

GlobalWafers-CEO Xu Xiulan formulierte es klar: „Central and China Microelectronics (CMC) bildet ein virtuelles IDM-Konstrukt mit Fokus auf SiC; wir greifen die Nachfrage der nächsten fünf Jahre an!“[^9] Die Strategie verknüpft die Muttergesellschaft 中美晶 mit 長晶（環球晶）、磊晶（朋程）、模組（鴻揚半導體） zu einer Kette.

Doch der SiC-Weg verläuft nicht linear nach oben. Im zweiten Halbjahr 2025 expandierten chinesische SiC-Anbieter (Sanan Optoelectronics, 天科合達等) aggressiv, die Welt geriet in Überangebot, und die Auslastung von GlobalWafers bei 6- und 8-Zoll-SiC fiel zeitweise unter 50%[^10]. Das fügte dem 2023 optimistischen PanSci-Skript der steigenden E-Mobility-Nachfrage einen Talpunkt hinzu.

Das Erholungssignal kam aus NVIDIA: Gerüchten zufolge soll die nächste Rubin-GPU-Plattform in einer Zwischenschicht auf SiC setzen, gekoppelt mit 800-Volt-DC-Architekturen in Rechenzentren, mit voller Serienproduktion 2027[^10]. Sollte sich dieses Gerücht bestätigen, wandert GlobalWafers' 8-Zoll-SiC-Kapazität von Elektroautos in KI-Rechenzentren – und die Erzählung leuchtet wieder auf.

> 📝 **Kurator-Notiz:** GaN und SiC werden oft als „Wide-Bandgap-Halbleiter“ gemeinsam bezeichnet, doch in Taiwan ist diese Kategorie weit mehr als nur ein „Material der nächsten Generation“ – sie markiert das erste Feld, in dem Taiwan ein vollständiges Ökosystem ohne TSMC aufbauen kann. GlobalWafers, 漢磊製造, 穩懋封裝, 宏捷科設計: Neben dem „Schutzberg“ Taiwans entsteht daneben eine deutlich ruhigere, aber eigenständige „dritte Bergkette“.

## Jensen Huang und die CoWoS+-Verflechtung

Zurück zum KI-Schlachtfeld.

NVIDIAs H100-GPU nutzt TSMCs 4-nm-Prozess mit CoWoS-S-Verpackung zur Integration von HBM3-Hochgeschwindigkeits-Speicher. Blackwell B200 nutzt CoWoS-L, verbindet zwei Blackwell-GPUs mit einer Grace-CPU; die KI-Trainingsleistung ist gegenüber H100 viermal so hoch[^11]. Die nächste Generation Rubin soll 2026 auf den Markt kommen.

Das Herz jeder GPU-Generation ist dieses Doppelantriebssystem: fortschrittlicher Prozess plus fortschrittliches Packaging. Der Prozess macht Transistoren immer kleiner, das Packaging stapelt einzelne Dies immer näher zusammen. PanSci beschrieb es so mit dem Vergleich Tai9 und Tunnels: „Konventionelles Packaging folgt der verschlungenen Tai-9-Straße mit neun Kurven, während Advanced Packaging direkt durch einen Xueshan-Tunnel trennt und den Datenaustausch deutlich schneller und bequemer macht.“[^12]

Der Kern von CoWoS (Chip-on-Wafer-on-Substrate) ist „Through-Silicon Via“ (TSV): unterschiedliche Dies werden übereinandergelegt, vertikale Mikropfade durchdringen das Siliziumsubstrat, so dass zwei getrennte Stromkreise zu einem dreidimensional verbundenen System werden. PanSci fasst es klar: „3D-Stacking erlaubt, die C-Chips auf der Oberseite des A-Chips zu platzieren, und über TSV-Technik wird das ausgedünnte Siliziumsubstrat mit hochdichten vertikalen Leitungen verbunden – ihre Distanz wird aus kosmisch zu unmittelbarer Nähe.“[^12]

Die Kapazitätszahlen sprechen für sich. Ende 2024 lag die monatliche CoWoS-Kapazität von TSMC bei etwa 35.000 Stück, bis Ende 2025 auf 75.000 gesteigert, mit einem Ziel von 150.000 im Jahr 2028; die jährliche Wachstumsrate liegt bei rund 80%[^13]. NVIDIA hat für TSMC CoWoS-Kapazität bis 2027 gesichert, und **alle Chips, egal in welcher TSMC-Fabrik produziert (inklusive Arizona), müssen für die CoWoS-Verpackung zurück nach Taiwan zurückkehren**[^13].

Das ist Jensen Huangs und TSMCs doppelte Engpassposition. NVIDIA hält das Design, TSMC hält Fertigung und Packaging – beide gemeinsam kontrollieren den kritischen Knoten der KI-Rechenzentren.

Am 2. Juni 2024 legte Jensen Huang in der Computex-Keynote in Taipeh im Universitätsstadion das Bindungsmodell vor; die Folien zeigten zwar die Roadmaps von Blackwell und Rubin, doch jede einzelne enthielt im Hintergrund die CoWoS-Linie in Hsinchu.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_NVIDIA offizielle Kanäle: Jensens Keynote auf Computex 2024 am 2. Juni 2024 im Stadium der Taiwan University, „The Era of AI“. Über zwei Stunden zeigte er nacheinander Blackwell GPU, NVLink, Spectrum-X; die physische Realität hinter jeder Folie war jedoch immer Hsinchu. Er sprach nicht den Satz „Kein TSMC, kein NVIDIA“ aus – doch jede Kapazitätsgrafik tat es bereits._

Die physische Last von 3D-Packaging ist nicht gering. PanSci hat die Schwierigkeit benannt: „Fortschrittliches Packaging verlangt hohe Anforderungen an Planarität und Ausrichtung nackter Chips; ein nicht korrekt leitungsverbundener Kontakt beim Stacking verringert die Ausbeute. Darüber hinaus erzeugt Rechenleistung Wärmeverluste. 3D-Packaging verringert den Abstand zwischen nackten Dies und verschärft so die thermische Kopplung; die Chips erwärmen einander und machen Kühlung schwieriger.“[^12]

Die nächste Etappe sind SoIC (System on Integrated Chips) und SoW-X (System on Wafer). SoIC ist „echtes 3D“ – Wafer-on-Wafer-Stapelung ohne Bumping. SoW-X soll 2027 in Serie gehen, hat eine Maskenfläche 9,5-mal größer als aktuelles CoWoS, integriert über 16 große Rechenchips und übertrifft bestehendes CoWoS in Leistung um 40%[^13]. Je größer KI-Chips werden, desto mehr wirken TSMCs Packaging-Linien wie kleine Fabriken.

## ALD: Schicht für Schicht aufgebaut

![Im Museumsausstellungsfall nebeneinander gezeigte Silicon-Wafer-Belege in verschiedenen Durchmessern, das größte etwa 12 Zoll, mit spiegelnder Oberfläche als Herzstück der Halbleiterherstellung.](/article-images/technology/silicon-wafers-museum-2017.webp)
_Silicon-Wafer-Beispielausstellung, 2017. Photo: ArticCynda. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

3 Nanometer, 2 Nanometer, 1,6 Nanometer. Hinter diesen Zahlen steht eine unscheinbare, aber zentrale Technik: Atomic Layer Deposition (ALD).

ALD wurde in Finnland erfunden und ist dennoch ein Kernschritt in jedem fortgeschrittenen Prozess in Taiwan geworden.

Die Geschichte beginnt in Finnland. 1974 begann der Materialwissenschaftler Tuomo Suntola bei Instrumentarium Oy die ALD-Forschung. 1977 war die Technik reif und stellte sich bei einer industriellen Ausstellung vor[^14]. Damals war ALD zunächst für Elektrolumineszenz-Displays gedacht; Suntola ahnte nicht, dass es 30 Jahre später Nerven im Nanoschritt werden würde. 1999 verkaufte er ALD an den niederländischen Ausrüstungsanbieter ASM. Heute hält ASM über 55% des ALD-Marktes[^14].

PanSci erklärt das Prinzip knapp: „Atomic Layer Deposition ist eine verbesserte Variante der chemischen Gasphasenabscheidung, bei der der Prozess in zwei Schritte getrennt wird. Zuerst wird Precursor A eingespeist und mit der Substratoberfläche reagieren... sobald die Oberfläche gesättigt ist, wird Precursor B zugeführt und reagiert mit den angehefteten Gruppen, wodurch das Zielmaterial entsteht und die Dünnfilm-Bildung abgeschlossen ist.“[^14] Die beiden Precursoren werden abwechselnd einzeln eingespritzt; jede Runde wächst genau eine Atomschicht dick.

> 💡 **Wussten Sie schon?**: Die kleinste Merkmalgröße des 2‑nm‑Prozesses liegt bei ungefähr 20 nebeneinander liegenden Siliziumatomen. Würden Siliziumatome auf Tischtennisbälle vergrößert, wäre ein 2‑nm‑Transistor etwa so lang wie ein Tischtennisfeld. Die Aufgabe von ALD ist es, auf diesem „Feld“ das Isolationsmaterial Kugel für Kugel zu legen.

ASM wird in Taiwan nicht gelistet, aber fast alle 12‑Zoll‑ALD-Anlagen des Unternehmens haben ihre größten Kunden in Taiwan. **Diese Lieferkette ist unsichtbar, aber unersetzlich**: Wenn Taiwans 2‑nm‑Massenfertigung ins Stocken gerät, kann weltweit kein zweites ALD-Unternehmen ausgleichen.

## Nach der 2‑nm‑Ära kommt die Quantenzeit

Hinter der Ängström‑Geschichte (Angstrom, 1 Nanometer = 10 Å) hat TSMC ihre Story noch nicht abgeschlossen.

Im vierten Quartal 2025 startete TSMC mit der 2‑nm‑Massenproduktion im Fab 22 in Kaohsiung; das Fab 20 im Hsinchu Science Park folgte danach[^2]. Die 2‑nm‑Technologie nutzt erstmals GAA‑Transistoren (Gate‑All‑Around) mit Nanoblatt‑Architektur und ersetzt FinFETs, die von 22 nm bis 3 nm durchgängig verwendet wurden[^16]. 2 nm entsprechen etwa 20 Siliziumatomen in der Breite und nähern sich bereits der theoretischen Grenze der Physik. Erstkunden sind Apples A‑Serie‑Chips und NVIDIAs KI‑Chips; die Kapazität der 2‑nm‑Fertigung wird von Quartal zu Quartal ausgebaut[^3].

Als Nächstes kommt 1,6 nm (A16), die 2026 im vierten Quartal in die Massenfertigung gehen soll und erstmals ein „Backside Power Delivery Network“ einführt, intern bei TSMC „Super Power Rail“ genannt[^16]. Bei gleicher Leistungsaufnahme 10 % schneller als N2P, bei gleicher Leistung 15–20 % energieeffizienter.

Aber was kommt nach 1,6 nm? Die Weiterführung der Prozessknoten wird immer teurer. Die Entwicklungskosten eines 28‑nm‑Prozesses lagen bei etwa 1 Milliarde US‑Dollar, bei 7 nm bei 3 Milliarden, bei 3 nm bei 10 Milliarden und 2 nm werden auf über 20 Milliarden geschätzt[^4]. Der exponentielle Verlauf des Moore’schen Gesetzes macht die Entwicklungskosten am Ende astronomisch, was genau das ist, was PanSci als „exponentiell steigende Komplexität und Investitionen bei fortschreitender Dekadenz von Kosten‑Nutzen‑Verhältnis“ beschreibt[^12].

So hat die Halbleiterindustrie ihre Strategie geändert: Horizontale Expansion wird zu vertikaler Stapelung (3D‑Packaging), Silizium wird durch neue Materialien wie GaN/SiC ergänzt, und am Ende könnte der Sprung in eine völlig andere Rechenphysik erfolgen, etwa Quantencomputing.

Das Zeitliniendiagramm der Academia Sinica sieht so aus: Im Oktober 2023 wurde ein supraleitender Quantencomputer mit 5 Qubits fertiggestellt. Im Januar 2024 besichtigte Präsidentin Tsai Ing-wen die Anlage, und der Quantencomputer ging am 29. Januar 2024 online[^6]. PanSci schrieb: „Im Januar 2024 wurde in Taiwan der erste in Taiwan selbst entwickelte Quantencomputer von der Academia Sinica geboren. Trotz nur 5 Qubits markierte das den Startpunkt, um Taiwan einen Platz in der globalen Quantencomputer‑Arena zu sichern.“[^17]

Im Dezember 2025 wurde ein supraleitender Quantenchip mit 20 Qubits fertiggestellt. Im Januar 2026 wurde die Netzverbindung offiziell genutzt[^6]. Die Kohärenzzeit (T1) sprang von 15–30 Mikrosekunden bei 5 Qubits auf 530 Mikrosekunden bei 20 Qubits. Kohärenzzeit ist die Dauer, in der ein Qubit seinen Superpositionszustand halten kann; länger bedeutet: „weniger Rauschen, komplexere Berechnungen möglich“.

Ein ressortübergreifendes nationales Quantenprogramm formierte sich im März 2022 offiziell, mit einem Fünfjahresbudget von 8 Milliarden TWD und 17 Forschungsgruppen[^18]. Das Wirtschaftsministerium richtete im April 2026 das Büro „Quantum Industry Technology Promotion Office“ ein, um akademische F&E und Industrie zusammenzubringen.

Interessant war eine Maßnahme des Industrieforschungsinstituts (ITRI): Die Kontrollchips für Qubits werden mit TSMCs 28‑nm‑Prozess hergestellt. In der CNA‑Meldung vom März 2024 heißt es aus ITRI-Sicht: „Mit Taiwans Stärke im Mikrowellen‑IC‑Design und der 28‑nm‑Fertigung von TSMC wurden Niedrigtemperatur‑Steuerchips und ‑Module (4 K, also –269 °C) entwickelt … Damit werden Steuergeräte kleiner und können in einen Kryostaten gebracht werden, wodurch das Gesamtvolumen um 40 % sinkt und die Verkabelung vereinfacht wird, was kommerzielle Vorteile bringt … Die Leistungsaufnahme dieses Moduls ist im Vergleich zu veröffentlichten Daten internationaler Großanbieter um mehr als 50 % reduziert.“[^19]

> 📝 **Kurator:innen‑Notiz**: Taiwanische Quantensouveränität besteht nicht darin, eigene Qubits herzustellen (das ist eher Gebiet von IBM, Google oder Academia Sinica), sondern darin, die Steuerchips so zu miniaturisieren, dass sie in Kaltkammern passen. Von 5 zu 20 Qubits hat ITRI die Kontrollchips von 1‑Qubit‑Unterstützung über 2‑Qubit zu 8‑Qubit‑Lösungen entwickelt und plant für 2026–2027 20 Qubits. **Der nächste Schritt für die „Hüguer“ (護國神山) ist, die Rolle als Auftragsfertiger im Quantenzeitalter einzunehmen, nicht als Hauptakteur in der Quantenvorherrschaft zu konkurrieren**. Aber diese Auftragsposition ist noch nicht offiziell besetzt.

## Drei Quantenpfade: Supraleitung, Ionenfalle, Topologie

Quantencomputer haben nicht nur einen einzigen Pfad.

**Supraleitende Qubits** (superconducting qubits) sind der Weg von IBM, Google und Academia Sinica. Vorteil: Der Prozess ist kompatibel mit bestehenden Halbleiter‑Fabs (dort spielt Taiwan seine Rolle), und die Steuerung ist schnell. Nachteil: Er benötigt Kühlung nahe des absoluten Nullpunkts (15 mK, etwa –273 °C) in einem Verdünnungskryostaten und ist rauschanfällig. Google erklärte 2019 mit 53‑Qubit‑System „Sycamore“, Quantenüberlegenheit erreicht zu haben: Eine Aufgabe, die einem klassischen Supercomputer in 10.000 Jahren kostet, wurde in 200 Sekunden gelöst.[^20]

**Ionenfallen‑Qubits** (trapped ion qubits) folgen dem Weg der Lasersteuerung einzelner Atome. PanSci fasst die Differenz wie folgt zusammen: „Die Ionenfallen‑Technologie nutzt Laser, um einzelne Atome zur Berechnung zu steuern. Sie bietet hohe Präzision und Stabilität, leidet aber unter technischer Komplexität und hohen Kosten.“[^17] Repräsentante sind IonQ und Quantinuum. Vorteil: hohe Präzision und Stabilität, keine extrem niedrigen Temperaturen nötig. Nachteil: langsame Steuerung und Skalierungsschwierigkeiten.

**Topologische Qubits** (topological qubits) sind Microsofts Wette auf die nächste Generation. Im Februar 2025 stellte Microsoft den Majorana‑1‑Topologieprozessor vor und behauptete eine Skalierung auf eine Million Qubits.[^15] Theoretisch sind topologische Qubits extrem störungsresistent, doch diese Route ist am wenigsten ausgereift; die Existenz der Majorana‑Teilchen ist physikalisch noch in der Verifikationsphase.

Jeder dieser drei Wege hat Risiken. Taiwans Strategie ist: „**Sorge dafür, dass Taiwan in jeder Gewinnerlinie einen Lieferkettenknoten hat**“, statt auf nur einen Weg zu setzen. Der supraleitenden Route folgt TSMCs 28‑nm‑Kontrollchip. Für Ionenfallen braucht es Präzisionsoptik und passt zu Taiwans Photonik‑Industrie; für den Topologie‑Pfad, falls er gelingt, braucht es extrem reine Dünnfilme — wieder im Reich von ALD.

## Übersee-Fabs: Expansion oder Export?

TSMCs Globalisierung beschleunigte sich seit den 2020er‑Jahren.

**Fab 21 in Arizona (USA)**: Phase 1 mit 4‑nm‑Produktion beginnt im ersten Halbjahr 2025; Phase 2 mit 3 nm / 2 nm folgt im zweiten Halbjahr 2027; Phase 3 mit 2 nm / A16 soll vor 2030 anlaufen. Gesamt‑CAPEX rund 165 Milliarden US‑Dollar[^21]. Doch ein wichtiges „Aber“: Das CoWoS‑Packaging für alle KI‑Chips erfolgt weiterhin nur in Taiwan; Wafer aus Arizona werden zurück nach Taiwan zur Verpackung geschickt[^13].

**Fab 1 in Kumamoto, Japan**: 22–28 nm, seit 2024 in Produktion, in Kooperation mit Sony und Toyota. Die geplante Fab 2 (12–16 nm) ist unklar; Teile der Ressourcen wurden nach Arizona verlagert.

**ESMC in Dresden, Deutschland** (TSMC hält 40 %): 28/22/16/12‑nm‑Autochips, Anlagen im dritten Quartal 2025, Serienproduktion 2027, etwa 40.000 Chips/Monat[^22].

Alle diese ausländischen Werke folgen einem gemeinsamen **N‑2‑Prinzip** — **immer zwei Generationen hinter Taiwans Inlandskapazität**. Während Taiwan 2 nm macht, ist im Ausland 4 nm „Top‑of‑Mind“; wenn Taiwan auf 1,6 nm wechselt, arbeitet der Auslandsteil bei 3 nm. Diese Grenze liegt nicht im Vertragstext, sondern in der geopolitischen Produktionslogik.

> ⚠️ **Umstrittene These**: Sind Ausland‑Fabs eine Ausweitung oder eine Aufweichung des Taiwan‑Modells? Befürworter sagen: Kerntechnik bleibt zuhause, Kapazität wird global ausgedehnt — das verwandelt das „einzige Silizium‑Problem“ in eine „Kette“, was das Risiko besser streut. Gegner sagen: Mit jeder ausgesiedelten Fab gehen ausgebildete Ingenieure, ein komplettes Massenfertigungs‑SOP und Kundenbeziehungen ab. In 30 Jahren könnten Arizona oder Kumamoto zur N‑2‑Grenze reifen und diese Lücke langsam schließen. Das N‑2‑Prinzip ist derzeit ein TSMC‑Verpflichtung, keine Naturkonstante.

Parallel zur Auslagerung von Fabs läuft die „Verlagerung von Design-Talenten“. KI‑Chip‑Design braucht heute nicht nur Taiwan; auch Silicon Valley, Tel Aviv und Neu-Delhi haben eigene Designzentren. Taiwans Auftragsmodell wandelt sich von „Insel-eigene Ingenieurskollektive“ zu einer Mischform aus „globale Ingenieure + Insel-Fertigung“.

## Umweltkosten: Die andere Seite des „護國神山“

Der „護國神山“ ist schwer.

Am unmittelbarsten sind die Wasserressourcen. TSMC verbraucht in den drei großen Science‑Parks täglich über 208.000 Tonnen Wasser; Umweltgruppen schätzen, dass der Wasserverbrauch mit neuen Fabriken nach 2025 auf bis zu 770.000 Tonnen/Tag anwachsen kann[^23]. TSMC entgegnet: Jedes Wasservolumen wird im Mittel 3,5‑mal genutzt, die Rückgewinnungsquote liegt bei 87 %, in neuen Werken bei 90 %; 2024 wurden 5,54 Mio. m³ zusätzlich eingespart.

An zweiter Stelle steht der Stromverbrauch. Eine 3‑nm‑Fab benötigt rund 2,1 Milliarden kWh pro Jahr, das entspricht dem Jahresverbrauch von rund 20.000 Haushalten in Taiwan. 2‑nm und 1,6‑nm werden den Verbrauch weiter erhöhen. TSMC verspricht RE100 bis 2050 (100 % erneuerbare Energie), doch die taiwanische Versorgung mit grüner Energie wächst nicht im gleichen Takt wie die Halbleiterexpansion, sodass diese Timeline ständig auf dem Prüfstand steht.

Die dritte Hürde ist die Arbeitszeit. Die Arbeitszeit, Wohnkosten und Geburtenrate im Hsinchu Science Park sind eigene Artikelthemen. Wie in der Materialwissenschaft gibt es auch hier eine „Bandlücke“ der menschlichen Physik: Zeit und Energie eines Menschen haben eine Grenze, jenseits derer Systeme kollabieren.

Die Existenz des „護國神山“ hängt nicht nur von TSMCs Technologie, staatlicher Politik und geopolitischer Gelegenheit ab, sondern auch von 170.000 Beschäftigten in den Science Parks, der gesamten Lieferkette und allen taiwanischen Bewohner:innen, die Strom und Wasser nutzen.

## Volles Ökosystem: Taiwan ist mehr als nur TSMC

Die Wettbewerbsfähigkeit der taiwanischen Halbleiterindustrie erwächst aus dem gesamten Cluster, nicht aus TSMC allein. Auf der IC‑Design‑Seite gibt es MediaTek (top 3 weltweit), Novatek, Realtek und Himax. In der Foundry-Welt neben TSMC gibt es UMC, VIS (Vanguard), und PSMC. Die Packaging‑ und Test‑Stufe wird von ASE (weltweiter Spitzenplatz), Siliconware und KYEC übernommen. Die dritte Halbleiterkategorie wird von GlobalWafers (SiC‑Kristallzucht), Episil, WinSemi (GaN) und Hi‑Joint getragen; Speicherchips werden von Nanya Technology und Winbond gefertigt; auf der Geräte‑ und Materialseite tragen Hersteller wie Gudeng Precision, Scientech und TOPCO als weniger sichtbare Zulieferer dazu.

Ein Chip kann in Taiwan rund um den Kreis gefertigt werden, ohne grenzüberschreitenden Transport. Diese „kurze Kette“ wurde in der COVID‑Zeit von der Welt gesehen und seitdem in die Lieferketten‑Whitepaper aller großen Tech‑Konzerne geschrieben.

Der Hsinchu Science Park wurde 1980 gegründet und hat in über 40 Jahren mehr als 500 Unternehmen mit rund 170.000 Beschäftigten hervorgebracht. Ein Ingenieur kann fünf Jahre bei TSMC arbeiten, dann zu MediaTek wechseln und später zu 日月光 in die Packaging‑Abteilung gehen — solche branchenübergreifenden Talentkreisläufe verteilen technisches Niveau effizient im Ökosystem.

Und die Konkurrenz? Samsung hat zwischen 2022 und 2026 rund 230 Milliarden US‑Dollar in integrierte Vertikalstrategien investiert, doch die Ausbeute in fortgeschrittenen Knoten liegt noch hinter TSMC zurück[^4]. Intel war 2021 mit IDM 2.0, um Design und Fertigung zu vereinen, aber bis 2025 hatte der Contracting‑Teil noch keine großen Kunden — ironischerweise werden Teile von Intels High‑End‑Chips weiterhin von TSMC gefertigt.

## Der Quantum-Standort ist noch frei

Ein Ladegerät fürs Nokia 3310 hatte 4,56 Watt; die Schnellladegeräte von 2025 liegen bei 240 Watt. Faktor 52. Taiwan hat diese 30 Jahre Silizium‑Weg mit 5 Jahren GaN‑Nachholung beschleunigt.

Im Quantenlabor der Academia Sinica benötigen supraleitende Chips 15 Millikelvin (ca. –273 °C). ITRIs Kontrollchips aus TSMCs 28‑nm‑Prozess komprimieren das gesamte notwendige „Steuergerätsvolumen“ von einem ganzen Gebäude auf einen kleinen Kasten. Taiwans Halbleiterkompetenz verschiebt die Grenze des Quantencomputing Schritt für Schritt.

Aber niemand weiß genau, wo diese Grenze wirklich liegt. Von 15 auf 530 Mikrosekunden Kohärenzzeit ist erst der Anfang. Die 19 Ingenieure, die RCA vor 50 Jahren entsandte, hätten vermutlich auch nicht geahnt, dass ihre Arbeit von 1973 in die 2‑nm‑Produktion 2025 münden würde.

Der „護國神山“ beherrscht den Planeten mit 50 Jahren Auftragsfertigungserfahrung. Die nächste 50 Jahre—und die Rolle als Auftragsfertiger im Quantenzeitalter—sind noch nicht gesichert.

> ✦ NVIDIAs Blackwell steht als Cloud‑Inference über deinem Kopf, Globalwafers’ SiC‑Wafer heizen deine Wallboxen vor der Haustür, und die erste ALD‑Schicht aus Tuomo Suntolas Labor in Finnland liegt heute im Gateschicht‑Isolator deines Smartphones: Die Halbleiterindustrie ist kein Sprint, sondern ein 50‑jähriger Klettertour entlang der physikalischen Bandlücken, die nie nur TSMC gehört. Wohin der nächste Schritt führt, wird die Physik zeigen; ob wir ihn gehen, entscheidet Taiwan.

---

**Weiterführende Lektüre**:

- [Taiwanese Enterprises: TSMC](/economy/台灣企業：台積電) — Unternehmensführung, Finanzstruktur und das Ausmaß der Investitionen von TSMC
- [Taiwanese Enterprises: MediaTek](/economy/台灣企業：聯發科技) — Wie der IC‑Design‑Leader in Smartphone‑Chips und KI‑Edge‑Rechenleistung positioniert ist
- [Taiwanese Enterprises: ASE](/economy/台灣企業：日月光半導體) — Global führend im Verpackungs- und Testbereich; Ökosystem nach CoWoS in der Endfertigung
- [Der Gipfelbauer: Der große Einsatz](/art/造山者世紀的賭注) — Dokumentarfilm von Xiao Ju-zhen (2025), 80+ Interviews mit Halbleiter‑Veteranen über fünf Jahre; 2026 besucht es Purdue / Wisconsin / Michigan als CHIPS‑Act‑Investitionszentren
- [Wu Dayou](/people/吳大猷) — Während Taiwans Aufstieg in den 1980ern war er zugleich Akademiepräsident und trat für Grundlagenforschung ein, was dem taiwanischen Forschungsgefüge Grundstrukturen gab
- [Huang Chong-ren](/people/黃崇仁) — Gründer von Reatek/力晶 und Powerchip/力積電; Taiwans Weg, auf fremden Prozesslizenzen eigene Waferfabriken aufzubauen, von 23,2 % auf 6,3 % Marktanteil — ein Abschnitt, der selten erzählt wird
- [Taiwanische Robotikindustrie](/technology/台灣機器人產業) — Warum die Insel, die Halbleiterwelt dominiert, im Roboterzeitalter Nachholbedarf hat; Ein Blick auf die Industriebrüche seit der NCAIR‑Einweihung
- [Taiwanische Aktien- und Kapitalmärkte](/economy/台灣股市與資本市場) — Wie die komplette Lieferkette als 6. Platz im Weltmaßstab der Marktstruktur die taiwanische Börse trägt
- [Taiwan Tungsten Supply Chain](/technology/台灣鎢供應鏈) — Wie sechswertiges Tungsten Kontakte und 3D‑NAND‑Wordlines verbindet, obwohl Taiwan selbst keine Wolfrenvorkommen hat
- [Taiwan AI School](/technology/台灣人工智慧學校) — Wie 10.000 AI‑Ingenieur:innen durch acht Jahre AIA‑Ausbildung die Software‑Seite der Halbleiterlandschaft zurück in den taiwanischen Verbund bringen
- [Computex: Drei große Computer‑Messen, aber zwei gingen nach Hause](/technology/Computex) — TSMCs CoWoS und führende Prozesslinien treffen jedes Jahr im Mai im 45‑jährigen Taipei‑Computex auf KI‑Giganten
- [Taiwan Science Parks](/technology/科技園區發展) — Hsinchu, Nangang, Nantz? (Nacional?); der physische Träger des Halbleiterclusters und geografisches Zentrum des „護國神山“

## Bildquellen

Dieser Artikel nutzt 3 CC/PD‑Bilder, im Cache gespeichert unter `public/article-images/technology/`, um direkte Hotlinks zu Quellservern zu vermeiden:

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Photo: 4300streetcar, 2025-12-25, CC BY 4.0, Wikimedia Commons file Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Photo: Peellden, 2010-09-05, CC BY-SA 3.0, Wikimedia Commons file TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Photo: ArticCynda, 2017-10-23, CC0 public domain, Wikimedia Commons file Silicon_wafers.jpg

## Quellen

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — Laut Semiwiki lag Philips’ Beteiligungsquote bei 27,6 %; ein Schlüsselinvestor für Technologie und Kunden in der Frühphase von TSMC

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — Die 2‑nm‑Massenproduktion bei TSMC beginnt primär im Fab 22 in Kaohsiung, gefolgt vom Fab 20 in Hsinchu

[^3]: [數位時代 — 台積電 2 奈米正式量產](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC startete 2‑nm‑Massenproduktion ab Q4 2025; konkrete monatliche Ausbringung bleibt branchenspezifisch geschätzt und ist nicht offiziell veröffentlicht

[^4]: [科技新報 — 台積電 3 奈米利用率達 100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — Branchenexperten schätzen für TSMCs fortschrittliche Fertigung eine Ausbeute über Wettbewerbern; genaue Ausbeuteraten sind externe Schätzungen, nicht offizielle Angaben

[^5]: [天下雜誌 — 李國鼎與台積電誕生](https://www.cw.com.tw/article/5095492) — 1987 gründete Morris Chang TSMC und etablierte das reine Foundry‑Modell, das die globale Halbleiterarbeitsteilung prägt; Hintergrund: 4,5 Mio. USD für den RCA‑Technologietransfer 1973

[^6]: [中央研究院 — 20 位元超導量子晶片公告](https://www.sinica.edu.tw/News_Content/56/2375) — Academia Sinica vollendete im Dezember 2025 einen 20‑Qubit‑supraleitenden Quantenchip und schaltete ihn am 29. Januar 2026 zu

[^7]: [泛科學（PanSci） — 氮化鎵：用 1/3 的時間，得到一樣的電力](https://pansci.asia/archives/362660) — PanSci‑Redaktion. GaN‑Bandlücke 3,4 eV, Durchbruchspannung zehnfach höher, Betriebsfrequenz 1 MHz vs. 100 kHz bei Silizium; SiC‑Anwendungen für 1000‑Volt‑E‑Ladeinfrastruktur. Content-Curation-Partner gemäß MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC soll GaN‑Foundry im Juli 2027 aufgeben und die Technologie an WorldWide (VIS) und GlobalFoundries übertragen; bei Winstar (3163) liegt die monatliche Auslieferung von 6‑Zoll‑GaN auf rund 500 Wafern

[^9]: [富果直送 — 環球晶 SiC 8 吋晶圓 2025 量產](https://www.fugle.tw/news/article/1234567) — GlobalWafers erreichte Ende 2024 rund 20.000 Wafer pro Monat bei 6‑Zoll‑SiC, baute intern von 3 auf 20 Kristallöfen aus; Ausbeute > 50 %; Strategietext von Hsu Xiulan zu „virtual IDM group“

[^10]: [科技新報 — SiC 供應鏈承壓](https://technews.tw/2025/11/sic-market-oversupply) — Chinesische SiC‑Produktion seit 2025 erhöht den Druck und drückt die Auslastung der 6/8‑Zoll‑SiC‑Kapazitäten von GlobalWafers unter 50 %; Hinweise auf NVIDIA Rubin GPU, die 2027 mit SiC‑Zwischenschicht und 800V‑Hochspannungs‑DC‑Rechenzentren in Produktion gehen

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — NVIDIAs Blackwell B200 nutzt CoWoS-L zur Integration von 2 Blackwell‑GPUs und 1 Grace‑CPU; KI‑Training bis zu 4× schneller als H100; NVIDIA sichert TSMCs CoWoS‑Kapazität bis 2027

[^12]: [泛科學（PanSci） — 三維堆疊：先進封裝如何讓晶片走進雪山隧道](https://pansci.asia/archives/367588) — PanSci‑Redaktion. Prinzipien von CoWoS, SoIC, TSV; das Xue‑shan‑Tunnel‑Metapher; Ausbeute‑ und Wärmeprobleme beim 3D‑Packaging. Content‑Curation‑Partner nach MOU 2026-05-05

[^13]: [Digitimes — TSMC CoWoS 產能擴張規劃](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — TSMC‑CoWoS‑Monatskapazität: 35.000 Ende 2024, 75.000 Ende 2025, Ziel 150.000 im Jahr 2028; NVIDIA sichert die Kapazität bis 2027; Wafer aus Arizona werden nach Taiwan für das Packaging zurückgeführt

[^14]: [泛科學（PanSci） — ALD 原子層沉積：50 年的薄膜革命](https://pansci.asia/archives/377669) — PanSci‑Redaktion. ALD wurde 1974 von Tuomo Suntola bei Instrumentarium Oy entwickelt, 1977 prozessreif, 1999 an ASM verkauft; ASM kontrolliert heute über 55 % Marktanteil; Prinzip der Zweipräzessor‑Abfolge in der Chemie‑Gasphasenabscheidung. Content‑Curation‑Partner nach MOU 2026-05-05

[^15]: [科技新報 — Microsoft Majorana 1 拓樸量子處理器發表](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — Microsoft stellte im Februar 2025 den ersten topologischen Quantenprozessor Majorana 1 vor und behauptete Skalierbarkeit auf bis zu einer Million Qubits

[^16]: [TSMC 官網 — A16 (1.6nm) 製程公告](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — 2 nm nutzt erstmals GAA‑Nanoblatt‑Transistoren (statt FinFET); A16 führt erstmals die Backside‑Power‑Delivery‑Network („Super Power Rail“) ein, Inbetriebnahme Q4 2026, 10 % schneller bei gleicher Leistungsaufnahme, 15–20 % sparsamer bei gleicher Leistung

[^17]: [泛科學（PanSci） — 台灣量子科技：從 5 位元到量產時代](https://pansci.asia/archives/377923) — PanSci‑Redaktion. 2024 brachte Academia Sinica einen 5‑Qubit‑Quantencomputer hervor; supraleitend, Ionenfalle und topologisch als drei Routen dargestellt; Google Sycamore löste mit 53 Qubits in 200 Sekunden ein als 10.000 Jahre klassisch eingeschätztes Problem. Content‑Curation‑Partner nach MOU 2026-05-05

[^18]: [iThome — 量子國家隊 5 年 80 億預算](https://www.ithome.com.tw/news/151234) — Im März 2022 formte Taiwan eine ressortübergreifende „Quantum National Team“ mit einem Fünfjahresbudget von 8 Milliarden TWD und 17 Forschungsgruppen; im April 2026 richtete das Wirtschaftsministerium ein Büro zur Förderung der Quantenindustrie ein

[^19]: [中央社 2024/03/06 — 工研院量子控制晶片](https://www.cna.com.tw/news/ait/202403060123.aspx) — ITRI nutzt TSMCs 28‑nm‑Prozess zur Herstellung 4K‑(−269 °C)‑Niedrigtemperatur‑Quantensteuerchips, wodurch das Volumen um 40 % sinkt und der Energieverbrauch gegenüber internationalen Großanbietern um über 50 % reduziert wird; Fahrplan 1‑Qubit (2024) → 20‑Qubit (2026–2027)

[^20]: [TechNews — Google Sycamore 量子霸權](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — 2019 erreichte Google mit dem 53‑Qubit‑System Sycamore die Quantenüberlegenheit: 200 Sekunden statt rund 10.000 Jahren Rechenzeit im klassischen Supercomputer

[^21]: [SemiAnalysis — TSMC Arizona Fab 21 投資規劃](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — TSMCs drei Investitionsphasen in Arizona betragen zusammen 165 Milliarden US‑Dollar; Phase 1 (4 nm) in Produktion 2025, Phase 2 (3 nm/2 nm) 2027, Phase 3 (2 nm/A16) vor 2030; N‑2‑Prinzip bleibt: Ausland bleibt zwei Generationen hinter Taiwan zurück

[^22]: [Digitimes — ESMC Dresden 2027 量產](https://www.digitimes.com.tw/news/esmc-dresden-2027) — TSMC hält 40 % an ESMC in Dresden; 28/22/16/12‑nm‑Automobilchip‑Werk 2025 H2 installierte Anlagen, Produktion ab 2027, Kapazität etwa 40.000 pro Monat

[^23]: [天下雜誌 — 台積電水資源消耗](https://www.cw.com.tw/article/5128456) — Die drei großen Science Parks von TSMC verbrauchen täglich über 208.000 Tonnen Wasser; Umweltgruppen erwarten nach Produktionsbeginn neuer Werke ab 2025 bis zu 770.000 Tonnen/Tag; TSMC berichtet von 3,5‑facher Wiederverwendung je Wasserportion, 87 % Rückgewinnung (90 % bei neuen Werken) und zusätzlich 5,54 Mio. m³ eingespartem Wasser 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML wurde 1984 durch ein Joint Venture von Philips Netherlands und ASM International im Verhältnis 50/50 gegründet; nach Börsengang 1995 zog ASMI sich zurück; heute ist ASML weltweit einziger EUV‑Lithografie‑Zulieferer

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Lin ben Jian wurde 1942 in Vietnam geboren, arbeitete ab den 1970ern im IBM Watson Research Center an Belichtungstechnik, kehrte 2000 nach Taiwan zurück und leitete Forschungsentwicklung bei TSMC; 2008 erhielt er den SPIE Frits Zernike Award; oft als „Vater der immersiven Lithographie“ bezeichnet

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — Der 157nm‑Ansatz wurde wegen doppelter Brechung in CaF₂‑Linsen, hoher Absorption bei 157nm und Integrationsschwierigkeiten nach 2002–2003 von 193nm‑Immersion ersetzt; die Wette von Intel + Nikon scheiterte

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Burn‑Jeng Lin stellte 2002 die 193nm‑Immersionslithografie bei SPIE vor; ein Brechungsindex von Wasser von 1,44 hebt die effektive 193nm‑Auflösung auf rund 134nm; ASML setzte 2007 in Serie ein und trug so die Moore‑Kurve von 65 nm bis 7 nm um sechs Generationen weiter

[^cw-lin-interview]: [天下雜誌 CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — Interview mit Burn‑Jeng Lin (18.06.2024): Hintergrund zu Nikons Zurückhaltung bei Immersion; seine Rückkehr zu TSMC seit 2000 hat die Einführung von immersion lithography vorangetrieben; 30 Jahre technologische Zusammenarbeit mit ASML
