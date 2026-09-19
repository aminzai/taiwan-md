---
title: 'Taiwans künstliche Intelligenz — Strategie für Entwicklung und Zukunft: Das Hardware-Ticket ist gelöst. Wo wird die nächste Schlacht sein?'
description: 'Am 8. Oktober 2024 erhielten Hopfield und Hinton den Physiknobelpreis, einen Tag später AlphaFold-Forscher den Chemienobelpreis. Gleiches Jahr, 29. Mai: Jensen Huang in Taipei beim Austernsuppe-Essen mit Morris Chang. Taiwan stellte 90 Prozent der globalen AI-Server und 72 Prozent der fortgeschrittenen Wafer her, fehlte aber in der Antwort auf 42 Jahre Neuronale Netzwerke und 50 Jahre Proteinstruktur-Rätsel. Von Taiwan AI Labs (gegründet von PTT-Creator Ethan Tu) bis TAIDE — braucht diese Insel mehr als nur eine Fabrik?'
date: 2026-03-19
category: 'Technology'
tags:
  [
    'Künstliche Intelligenz',
    'AI',
    'Halbleiter',
    'Technologiepolitik',
    'Digitale Transformation',
    'Nobelpreis',
    'AlphaFold',
  ]
subcategory: '人工智慧'
author: 'Taiwan.md'
difficulty: 'advanced'
readingTime: 18
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
translatedFrom: 'Technology/台灣人工智慧發展與未來策略.md'
sourceCommitSha: 'b67b190fb'
sourceContentHash: 'sha256:15e7aa6f99cf7a84'
sourceBodyHash: 'sha256:50acff1d4627c3c4'
translatedAt: '2026-09-09T14:15:07+08:00'
---

# Taiwans künstliche Intelligenz — Strategie für Entwicklung und Zukunft: Das Hardware-Ticket ist gelöst. Wo wird die nächste Schlacht sein?

> **30-Sekunden-Überblick:** Am 8. Oktober 2024 erhielt der Physiknobelpreis den Physiker, der das Hopfield Network schrieb, und den Kognitionswissenschaftler, der Backpropagation schrieb[^N1]. Am nächsten Tag, 9. Oktober, erhielt der Chemienobelpreis drei Forscher, die mit AI das fünfzigjährige Protein-Faltungs-Rätsel lösten[^N2]. Im selben Jahr, am 29. Mai, erschien NVIDIA-CEO Jensen Huang in Taipei's Ningxia-Nachtmarkt und aß Austernsuppe mit Morris Chang, Mark Lin und CC Tsai. Taiwan Semiconductor Manufacturing Company hold 72 Prozent des globalen Wafer-Fundry-Umsatzes, Foxconn, Quanta und Wistron produzierten zusammen neunzig Prozent der globalen AI-Server. Doch in dieser zweitägigen Nobelpreisverkündung, die einundvierzig Jahre Geschichte der Neuronalen Netzwerke legitimierte, kam kein Name aus Taiwan. Von Taiwan AI Labs, gegründet von PTT-Creator Ethan Tu, bis zur staatlich unterstützten Traditional-Chinese LLM TAIDE — eine Wette von „AI herstellen" zu „AI sein" ist im Gange.

---

## 42 Jahre Bestätigung: Zwei Nobelpreise innerhalb von zwei Tagen 2024

Am Morgen des 8. Oktober 2024 in Stockholm. Die Königlich Schwedische Akademie der Wissenschaften kündigte an, dass der Nobelpreis für Physik diesen Jahres an zwei AI-Wissenschaftler vergeben wird: John J. Hopfield, 91 Jahre, emeritierter Professor in Princeton, und Geoffrey Hinton, 76 Jahre, der fünf Monate zuvor von Google ausschied. Das Preisgeld von 11 Millionen schwedischen Kronen teilen sich die beiden[^N1].

Die Begründung des Preiskomitees war: „Für grundlegende Entdeckungen und Erfindungen, die Maschinenlernen mit künstlichen neuronalen Netzwerken ermöglicht haben" (for foundational discoveries and inventions that enable machine learning with artificial neural networks)[^N1]. Dies ist das erste Mal in der Geschichte des Nobelpreises für Physik, dass der Preis direkt an das Feld der neuronalen Netzwerke verliehen wird.

Der nächste Tag, 9. Oktober, Chemie. Drei Preisträger: David Baker von der University of Washington, und zwei Personen von DeepMind, Demis Hassabis und John Jumper. Baker erhielt die Hälfte des Preisgelds, Hassabis und Jumper teilen sich die andere Hälfte[^N2]. Die Begründung war in zwei Teilen: Der erste Teil an Bakers „Computationales Protein-Design", der zweite Teil an Hassabis und Jumper für „Proteinstruktur-Vorhersage".

Zwei Tage, zwei Nobelpreise, beide über AI. Dies hat kein Vorbild in der Geschichte der Nobelpreise.

Vergleicht man die Zeitachse: Hopfield publizierte 1982 seine Arbeit mit dem langen Titel „Neural networks and physical systems with emergent collective computational abilities" in den _Proceedings of the National Academy of Sciences_ (PNAS), gerade als er von Festkörperphysik in die Neurowissenschaften wechselte[^N3]. Von 1982 zu 2024 sind genau 42 Jahre. Hinton und Rumelhardt legten ihren Backpropagation-Algorithmus in einem 1986-Papier vor[^N4], von Veröffentlichung zu Nobelpreis vergingen auch 38 Jahre. AlphaFold trat 2018 beim CASP13 zum ersten Mal an und erhielt 2024 den Nobelpreis — nur 6 Jahre.

Im Kern verlieh der Nobelpreis diese beiden Tage nicht ChatGPT, sondern Papieren von vor dreißig oder vierzig Jahren, die kaum jemand gelesen hat. Der Zeitverzug zwischen Grundlagenforschung und Industrieanwendung war schon immer so.

![Geoffrey E. Hinton am 8. Dezember 2024 beim Nobelpreiswochenende in Stockholm — ein offizielles Porträt in dunkelm Anzug, weißes Haar, ruhiger Blick zur Kamera](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, 2024 Nobelpreisträger Physik, Nobelpreiswochenende Stockholm. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>)._

---

## Ein Billionen-Dollar-Essen auf dem Ningxia-Nachtmarkt

Am Abend des 29. Mai 2024, am Vorabend der Computex, erschien eine ungewöhnliche Gruppe von Gästen auf Taipei's Ningxia-Nachtmarkt. NVIDIA-CEO Jensen Huang brachte Morris Chang von Taiwan Semiconductor Manufacturing Company, Mark Lin von Quanta, und CC Tsai von MediaTek mit, und sie drängten sich vor den Ständen, um Austernsuppe zu essen[^1]. Passanten erkannten Huang, und sofort wurden sie von Fans und Reportern umringt — eine Szene wie bei einem Star-Treffen.

Der kombinierte Marktwert dieser Gruppe überschritt Billionen von Dollar. Aber die echte Geschichte ist nicht auf dem Tisch, sondern dahinter in der Lieferkette: Die Unternehmen, die diese Menschen repräsentieren, stützen die physische Grundlage der globalen AI-Rechenoperationen. Während seines Taiwan-Besuchs sagte Huang öffentlich: „Taiwan ist eines der wichtigsten Länder der Welt."[^2] Das ist keine Höflichkeit. Ohne Taiwan existiert die Hardware-Grundlage der AI-Revolution nicht.

Jensen Huang wurde 1963 in Taipei geboren, verbrachte seine Kindheit in Tainan und wanderte mit neun Jahren in die USA aus[^3]. Das Unternehmen, das er 1993 mitbegründete, NVIDIA, ist heute das Synonym für AI-Chips. Jeder fortgeschrittene GPU, den NVIDIA entworfen hat — von den GPUs, die ChatGPT trainierten (A100, H100), bis zu den neuesten Blackwell-Serien — werden alle von Taiwan Semiconductor Manufacturing Company hergestellt[^4].

Vier Monate später, in Stockholm, enthielt die Ankündigung der zwei Nobelpreise nicht einen einzigen Namen dieser Personen. Dieser Unterschied ist keine Zufall — es ist eine strukturelle Tatsache.

---

## Hardware: Eine Insel trägt die gesamte AI-Revolution

Taiwans Position in der AI-Hardware-Lieferkette ist unterbewertet, wenn man sie nur als „kritisch" beschreibt.

Bei der Chipfertigung hält Taiwan Semiconductor Manufacturing Company 2025 72 Prozent des Umsatzanteils des globalen Wafer-Foundry-Marktes[^5]. Bei den fortgeschrittenen Prozessen unter 7 Nanometern übersteigt Taiwans Marktanteil neunzig Prozent. NVIDIA hat etwa einen Marktanteil von 86 Prozent beim AI GPU-Markt, und diese GPUs werden fast ausschließlich von Taiwan Semiconductor Manufacturing Company hergestellt[^6]. Das meiste der Rechenleistung, die zum Training und Betrieb von AI-Modellen weltweit verwendet wird, stammt aus den reinen Räumen Taiwans.

Nach der Herstellung der Chips müssen diese zu Servern zusammengebaut werden, bevor sie in Datenzentren gehen. Diesen Teil dominiert auch Taiwan. Die drei großen ODM-Hersteller Foxconn, Quanta und Wistron produzieren zusammen etwa neunzig Prozent der globalen AI-Server[^7]. 2025 durchbrachen diese drei Unternehmen jeweils ein Jahresumsatz von einer Billion New-Taiwan-Dollar (etwa 32 Milliarden Dollar), und der AI-Server-Umsatz überschritt zum ersten Mal die Umsätze von Unterhaltungselektronik[^8].

Die Leistung von AI-Chips hängt nicht nur vom Prozess-Schrumpfen ab, sondern auch von der Verpackungstechnologie. Taiwans CoWoS (Chip on Wafer on Substrate) fortgeschrittene Verpackungstechnologie ist der Schlüssel für NVIDIA-Hochleistungs-GPUs. 2026 wird nur NVIDIAs Bedarf nach CoWoS-Wafern etwa 595.000 Wafer erreichen, was etwa 60 Prozent der globalen Nachfrage ausmacht[^9].

Foxconn arbeitet mit NVIDIA und der taiwanischen Regierung zusammen, um in Kaohsiung einen AI-Fabrik-Supercomputer im 100-Megawatt-Bereich (MW) mit der neuesten NVIDIA Blackwell-Architektur zu bauen[^10]. Taiwan entwickelt sich von „dem Ort, an dem AI-Chips hergestellt werden" zu „dem Ort, an dem AI läuft".

![Außenansicht von Taiwanese Semiconductor Manufacturing Company's Fabrik 5 im Science Park Hsinchu, eine Szene aus den 2010er Jahren — die physische Stätte der Halbleiterwafer-Fertigung](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Taiwan Semiconductor Manufacturing Company Hsinchu Fab 5, der physische Ort der AI-Chip-Fertigung. Photo: Wikimedia Commons via [TSMC Fab 5 file](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

Die Frage ist: Wenn Hardware das Eintrittskarte erhalten hat, wo wird die nächste Schlacht sein?

> 📝 **Kurator-Notiz**
>
> Die verbreitete Aussage lautet „Taiwans Schutzgottberg trägt die AI-Revolution". Diese Aussage ist narrativ elegant, aber sie verwechselt Ursache und Wirkung zur Hälfte. Es ist nicht so, dass Taiwan Semiconductor Manufacturing Company wegen der AI-Revolution groß wurde — es ist so, dass die AI-Revolution GPU brauchte, und sie wählten Taiwan Semiconductor Manufacturing Company aus. Die echte Spannung liegt darin: Wenn GPU eine Ware ist, wohin wird Wert in der nächsten Phase fließen? Die Antwort, die die 2024 zwei Nobelpreise geben, ist das Modell selbst — die 12 Seiten, die Hopfield schrieb, die Nacht, in der Hinton und sein Student Krizhevsky AlexNet 2012 ImageNet's Bilderkennungs-Fehlerquote von 26,2 Prozent auf 15,3 Prozent herabsetzten[^N5], und der Nachmittag, an dem Hassabis und seine Gruppe AlphaFold GDT 92,4 (Median) bei CASP14 erreichten.

---

## Hopfield 1982: Das Gedächtnismodell eines Physikers

1982 schrieb John Hopfield, ein Festkörperphysiker in Princeton, ein Papier von nur 12 Seiten mit dem langen Titel „Neural networks and physical systems with emergent collective computational abilities", das in den _Proceedings of the National Academy of Sciences_ (PNAS) veröffentlicht wurde[^N3].

Was er tat, war im Kern, „Gedächtnis" in Physik zu übersetzen.

In der Physik gibt es etwas, das man Spin-Glas nennt: Ein Haufen magnetischer Atome mit Spinrichtungen, die untereinander wechselwirken, und das gesamte System wird von selbst einen Energieminimum-Zustand finden. Hopfield verlagerte dieses Konzept auf Neuronen: Stellen Sie sich Neuronen als Spins vor, Verbindungsstärke als Wechselwirkung, und das gesamte Netzwerk wird von selbst zu einem stabilen Zustand mit „energie-minimaem" Zustand konvergieren[^N3]. Jedes energy-minimum ist ein gespeichertes Gedächtnis.

Die Eleganz dieses Modells liegt darin, dass es Gedächtnis zu etwas macht, das in physikalischer Sprache beschrieben werden kann. Bei unvollständigen Hinweisen wird das Netzwerk das nächstgelegene energy-minimum finden und das Gedächtnis selbst vervollständigen. Dies ist der mathematische Vorfahre dessen, was generative AI heute tut.

1982, im selben Jahr, war Taiwan gerade dabei, seine Elektronikbranche zu starten, und Taiwan Semiconductor Manufacturing Company war noch nicht gegründet. Morris Chang musste bis 1987 warten, um die Firma zu gründen, die 42 Jahre später zum „Schutzgott-Berg" werden sollte. Das Hopfield-Papier hatte bis 2026 auf Google Scholar über 27.000 Zitate angehäuft[^N6].

Noch interessanter ist ein Satz, den Hopfield später sagte. Er war sein ganzes Leben lang Festkörperphysiker in Princeton, und sein Wechsel zur Neurowissenschaft wurde von seinen damaligen Kollegen als „Spielerei" angesehen. Erst mit der 2024-Nobelpreisliste, jetzt 91 Jahre alt, fragte ihn die Königlich Schwedische Akademie in einem Telefoninterview nach seinen Gefühlen zur Preisverleihung, und er sagte, dass er sich über „keine Menschen wissen, die die Richtung der AI verstehen oder kontrollieren" unwohl fühlte[^N7].

Der Mann, der die mathematische Grundlage der modernen AI schrieb, erinnerte alle am Tag der Preisverleihung daran, vorsichtig zu sein.

![John J. Hopfield am 8. Dezember 2024 beim Nobelpreiswochenende in Stockholm — eine offizielle Person in dunkelm Anzug, weißes Haar, ruhiger Gesichtsausdruck](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, 2024 Nobelpreisträger Physik, Nobelpreiswochenende Stockholm. Photo: Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

---

## Hinton: Das 1986-Papier und die 2023-Warnung nach seinem Google-Ausscheiden

Geoffrey Hinton, geboren 1947 in Wimbledon, London, ist ein weiterer Mensch, den die Geschichte erst 38 Jahre später anerkennt[^N8].

1986 veröffentlichte Hinton zusammen mit David Rumelhart und Ronald Williams einen Artikel über Backpropagation in _Nature_[^N4]. Dieser Algorithmus bedeutet: Wenn ein neuronales Netzwerk einen Fehler macht, kann man das Fehlersignal rückwärts durch jede Schicht leiten und die Verbindungsgewichte Schicht für Schicht anpassen. Dies ist die Art, wie alle modernen Deep-Learning-Modelle sich heute selbst trainieren.

Dieser Algorithmus wurde 1986 geschrieben, aber es brauchte drei Dinge, damit er explodieren würde: reichlich günstige Rechenleistung, riesige Datenmengen, und Menschen, die daran glaubten. Die ersten zwei wurden in den 2010er Jahren bereit, und die Repräsentanten der dritten Sache waren Hinton und seine zwei Schüler Alex Krizhevsky und Ilya Sutskever. 2012 trainierten sie ein Faltungs-Neuronales Netzwerk namens AlexNet mit GPU auf dem ImageNet-Erkennungswettbewerb und erreichten eine Top-5-Fehlerquote von 15,3 Prozent, weit vor dem zweiten Platz mit 26,2 Prozent[^N5]. Erst in diesem Moment glaubte die ganze Industrie, dass Backpropagation wirklich funktioniert.

Im März 2013 kaufte Google Hintons kleine Firma DNNresearch für 44 Millionen Dollar und brachte ihn, jetzt 65 Jahre alt, in die Google-Familie[^N8]. Das nächste Jahrzehnt war er der einflussreichste AI-Wissenschaftler im Silicon Valley.

Dann, am 1. Mai 2023, meldete die _New York Times_ ein Interview: Hinton verließ Google.

Sein Grund zum Gehen war nicht Ruhestand. Im Interview sagte er, er wollte „frei über AI-Risiken sprechen können, ohne bedenken zu müssen, wie es Google beeinflusst"[^N9]. Die Warnungen, die er gab, beinhalteten: AI-Systeme könnten bald intelligenter sein als Menschen, könnten von schlechten Menschen für böse Dinge verwendet werden, und „es ist schwer zu sehen, wie man das verhindern kann"[^N9]. Er sagte sogar, er bereue „einen Teil" seiner lebenslangen Arbeit[^N9].

2024, als Hinton den Physiknobelpreis erhielt, wiederholte er in einem Telefoninterview die Warnung: Vorsicht vor der Möglichkeit, dass AI außer Kontrolle gerät[^N10].

Der Mann, der den Deep-Learning-Trainingsalgorithmus schrieb, und der Mann, der das Gedächtnismodell schrieb, standen am 8. Oktober 2024 gleichzeitig auf der Bühne der Königlich Schwedischen Akademie und warnten gleichzeitig, dass dieses Ding gefährlicher sein könnte als erwartet. Dieses Bild hat einen gewissen Kontrast mit Oppenheimers Gesichtsausdruck, als er die Pilzwolke in der Wüste von New Mexico 1945 aufsteigen sah.

Zwei Monate später, am 8. Dezember 2024, hielt Hinton einen Vortrag über den Nobelpreis in der Aula Magna an der Universität Stockholm. Das Thema war „Boltzmann Machines" — das ist die frühere Arbeit, die Hinton mit Hopfield teilt, die thermodynamische Wahrscheinlichkeitsverteilungen in neuronale Netzwerke schrieb. Nach dem Vortrag verstand man, dass das 1986-Backpropagation-Papier nicht isoliert war, sondern eine ganze Art von Denken war, die in der Verknüpfung von Physik und Kognitionswissenschaften der 1980er Jahre erwuchs:

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Royal Swedish Academy of Sciences offizieller Kanal: Geoffrey Hintons Nobelpreisvortrag „Boltzmann Machines" am 8. Dezember 2024. Von den 1980er Jahren, als er und Sejnowski Boltzmann Machine schrieben, über Backpropagation, bis heute LLM — ganze vierzig Jahre. In den letzten 5 Minuten wiederholte er seine Sorge um AI-Risiken, diesmal auf der Nobelpreis-Bühne._

---

## Von PTT zum AI-Labor: Ethan Tus zwei Unternehmungen

Zurück zu dieser Insel Taiwan. In der gleichen Zeitspanne, in der Hopfield sein Gedächtnismodell schrieb, fing Taiwan gerade an, Informatik-Abteilungen zu haben.

1995 baute Ethan Tu, ein Student im zweiten Jahr der Informatik an der National Taiwan University, auf einem 486-Computer und mit Open-Source-Software PTT (Ptt Bulletin Board System) in seinem Studentenwohnheim auf, das später zum größten elektronischen Schwarzen Brett Taiwans wurde. Dreißig Jahre später ist PTT immer noch täglich mit Hunderttausenden online, ein lebendes Fossil der taiwanischen Internetkultur.

Tu ging später zu Microsoft und beteiligte sich an der Entwicklung von Cortana Sprachassistenten. Im April 2017 gab er sein hohes Gehalt im Silicon Valley auf und kam nach Taiwan zurück, um das „Taiwan Artificial Intelligence Lab" (Taiwan AI Labs) zu gründen, das erste nicht-kommerzielle, offene AI-Forschungsinstitut in Asien[^11].

Sein Motiv war einfach: Taiwan hat weltklasse Softwaretalente, aber all diese Talente sind ins Silicon Valley gegangen. Er wollte eine Plattform schaffen, auf der Menschen, die zurückkommen oder bleiben wollten, AI-Forschung betreiben konnten.

Das bekannteste Produkt von Taiwan AI Labs ist „Anting Verbatim Script", ein Spracherkennungssystem, das für traditionelles Chinesisch und taiwanischen Akzent optimiert ist. Während der COVID-19-Pandemie entwickelte das Labor auch Desinformations-Erkennungswerkzeuge und föderales Lernmedizin-AI[^12]. Der gemeinsame Punkt dieser Projekte ist: Sie lösen alle Probleme vor Ort in Taiwan, verwenden lokale taiwanische Daten, und übersetzen nicht einfach amerikanische Modelle.

Die Geschichte von Tu, von PTT zu AI Labs, ist gewissermaßen ein Schattenriss der taiwanischen Softwareentwicklung: Es mangelt nicht an technischer Fähigkeit, sondern an einem Ökosystem, das Talente zum Bleiben bringt.

> 💡 **Wusstest du?**
>
> 1986, als Hinton Backpropagation veröffentlichte, war Taiwans BIP etwa 77,9 Milliarden Dollar, das BIP pro Kopf etwa 4.007 Dollar, und der Hsinchu Science Park lief gerade sechs Jahre[^N11]. Drei Dinge ereigneten sich gleichzeitig auf dem gleichen Planeten, aber erst 26 Jahre später auf dem ImageNet-Datensatz würde diese Geschichtslinie sich treffen. Der Zeitmaßstab der Grundlagenforschung ist immer länger als das, was narrative Industrie spürt.

---

## AlphaFold: Die andere Hälfte des Nobelpreises für ein 50 Jahre altes Protein-Faltungs-Rätsel

Die Geschichte des 2024 Chemie-Nobelpreises beginnt mit einer 1972-Frage.

In diesem Jahr gab der amerikanische Biochemiker Christian Anfinsen seiner Nobelpreis-Rede eine Hypothese: die dreidimensionale Faltungsstruktur eines Proteins wird vollständig durch seine Aminosäuresequenz bestimmt[^N12]. Wenn diese Hypothese wahr ist, dann sollte man theoretisch, wenn man nur eine Aminosäuresequenz sieht, die entsprechende 3D-Struktur berechnen können. Aber dieses „sollte" dauerte ein halbes Jahrhundert lang an. Protein-Faltung wurde „grand challenge" genannt. Die Akademie veranstaltet alle zwei Jahre einen CASP-Wettbewerb, bei dem alle ihre Vorhersageergebnisse mit experimentellen Strukturen verglichen werden, seit 1994 dreizehn Durchgänge, und niemand konnte das Problem durchbrechen[^N13].

Bis 2018 CASP13, als DeepMind sein erste Generation AlphaFold zum Wettbewerb schickte und gewann, aber die Genauigkeit war noch nicht praktisch. Der echte Wendepunkt war am 30. November 2020 CASP14: AlphaFold 2 erzielte einen mittleren GDT von 92,4[^N13]. Ein GDT von 92,4 bedeutet, dass in über der Hälfte der Vorhersagen die Atompositionen eine Abweichung von weniger als einem Ångström von experimentellen Werten hatten, erreiche Experimentalauflösungs-Ebene. CASP-Organisator John Moult sagte an diesem Tag: „In vielem Sinne ist das Problem gelöst"[^N13].

Ein 50 Jahre altes ungelöstes Problem wurde in sechs Jahren von einem Londoner Forscherteam gelöst.

Dann ging es schneller. Im Juli 2021 öffnete sich AlphaFold 2 Quellcode; im selben Jahr arbeitete DeepMind mit dem Europäischen Molekularbiologie-Labor (EMBL-EBI) zusammen, um AlphaFold-vorhergesagte Proteinstrukturen in eine öffentliche Datenbank zu verwandeln. Im Juli 2022 deckte diese Datenbank eine Million Arten und etwa 200 Millionen Proteinstrukturen ab, gleichbedeutend damit, dass fast alle bekannten Proteinstrukturen der Erde kostenlos freigegeben wurden[^N14].

Am 8. Mai 2024 veröffentlichte DeepMind AlphaFold 3 in _Nature_, das die Vorhersagefähigkeit von einzelnen Proteinen zu Wechselwirkungen zwischen Proteinen und DNA, RNA, Liganden und Ionen erweiterte[^N15]. Von Neuentwicklung bis Impfstoffdesign bis Enzym-Technik — alle Felder, wo man wissen muss, wie Moleküle aneinander passen, wurden von diesem Werkzeug umgeschrieben.

Demis Hassabis, der AlphaFold schrieb, ist kein traditioneller Biochemiker. Er begann im Alter von vier Jahren Schach zu spielen, erreichte mit 13 Jahren den Master-Rang; mit 17 Jahren entwickelte er zusammen mit Peter Molyneux das Simulation-Spiel _Theme Park_, das Millionen Mal verkauft wurde[^N16]. 2010 gründete er zusammen mit Shane Legg und Mustafa Suleyman DeepMind in London, das 2014 von Google mit etwa 400 Millionen Pfund gekauft wurde[^N16]. 2016 besiegte DeepMind's AlphaGo Lee Sedol, 2020 war AlphaFold 2, 2024 Nobelpreis — drei Dinge mit weniger als zehn Jahren Abstand.

Die Linie dazwischen ist die gleiche Wette: Neuronale Netzwerke verwenden, um Probleme zu lösen, die Menschen früher nicht mit ihrem Gehirn lösen konnten. Schach ist eine Umgebung mit geschlossenen Regeln, Protein-Faltung ist eine Umgebung mit offenen Regeln aber starken physischen Einschränkungen. Bei beiden wählte Hassabis die richtige Schlacht.

Auf Taiwans Seite: Die von Academy Sinica's Prorektor Yung-Ya Lin während seiner Amtszeit (2006–2016) gegründete Zuckerprotein-Forschung ist Taiwans nächster zu dieser Frontlinie von akademischen Investitionen[^N17]. Academy Sinica's Biomedizinisches Forschungsinstitut und Biochemisches Institut haben auch Teams, die mit AlphaFolds Open-Source-Gewichten forschen. Aber Core-Modell-Entwicklung auf AlphaFold-Ebene — Taiwan hat jetzt keine entsprechende Struktur.

> ⚠️ **Strittige Ansicht**
>
> AlphaFolds Chemie-Nobelpreis war unter Wissenschaftlern umstritten: Ein Teil der Strukturbiologen glaubte, der Preis sollte zu den Forschern gehen, die die frühesten Schlüssel-Experimente machten, wie X-Strahl-Kristallographie oder Kernmagnetresonanz-Wissenschaftler, nicht um das Berechnungswerkzeug ins Chemie-Heiligtum zu heben[^N18]. Ein anderer Teil glaubte, die Debatte selbst wäre schon veraltet — wenn ein Algorithmus in fünf Jahren dabei helfen kann, fast alle Protein-3D-Strukturen der Erde zu vervollständigen, dann ist das Chemie. Die beiden Positionen begannen nach Oktober 2024 zur letzteren zu verschieben, aber die Spannung, die es repräsentiert, ist nicht weg: Wenn das, was AI tun kann, sich ausdehnt, sollten die Grenzen der traditionellen Disziplinen neu gezogen werden?

---

## TAIDE: Warum Taiwan sein eigenes Sprachmodell braucht

Im April 2023, ein halbes Jahr nachdem ChatGPT die Welt überflutete, startete Taiwans National Science and Technology Council (NSTC) das „TAIDE"-Programm mit vollständigem Namen „Trustworthy AI Dialogue Engine" (Vertrauenswürdige Generative AI Dialoge-Engine)[^13].

Warum braucht ein Land mit 23 Millionen Menschen sein eigenes großes Sprachmodell?

Der Grund ist nicht nur technische Selbstbestimmung. Traditionelles Chinesisch macht einen winzigen Anteil der globalen AI-Trainingsdaten aus, die meisten chinesischen Daten stammen von vereinfachtem Chinesisch aus Websites. Wenn Taiwaner ChatGPT oder andere Modelle verwenden, sind die Antworten oft voller Festlandchinas Sprachgewohnheiten und Ansicht-Annahmen. „视频" statt „影片", „质量" statt „品質" — diese scheinbar winzigen Unterschiede sind hinter kulturellen Hauptdelproblemen. Das Magazin _Common Wealth_ meldete TAIDE direkt unter dem Titel „Verhütung der chinesischen AI-Kulturinvasion"[^14].

Im April 2024 gab das TAIDE-Team die kommerzielle Version TAIDE-LX-7B und akademische Version TAIDE-LX-13B frei, mit anständiger Leistung in Schreiben, Übersetzen und Zusammenfassung[^15]. Bis 2026 wurde TAIDE 2.0 veröffentlicht, mit MediaTeks Breeze-8B-Modell unterstützt — Taiwans LLM-Ökosystem ging von „Aufholphase" zu „nutzbarer Phase"[^16].

Noch interessanter ist die Blüte auf der Anwendungsseite. National Chung Hsing University baute „Shen-nong TAIDE", ein Landwirtschafts-Wissenssuchsystem mit TAIDE; National Taiwan University of Science and Technology entwickelte ein Taiwan-Englisch-Dialog-Roboter zum Taiwan-Sprachunterricht; National Yang Ming Chiao Tung University trainierte Taiwan- und Hakka-Versionen des TAIDE-Modells[^17]. Diese Anwendungen beweisen eine Sache: Sprachmodelle sind gleichzeitig technische Produkte und kulturelle Träger. Ein AI, das „Sky-Piercing Day" und „Mazu-Pilgerfahrt" nicht versteht, kann Taiwan wirklich nicht dienen.

Aber TAIDEs Größe ist immer noch klein: Kommerzielle 8B und akademische 13B Parameternummer — mit OpenAI's GPT-4-Ebene (geschätzt über eine Billion Parameter) unterscheidet sich um zwei Größen. Diese Lücke dahinter ist GPU-Budget-Problem, nicht Fähigkeitsproblem. Training eines Spitzen-LLM braucht Rechenleistung im Millionen-Dollar-Bereich, äquivalent zum Jahresbudget eines landesweit wissenschaftlichen Forschungsinstituts.

---

## AI-Cybersecurity, die von Hacking geboren wurde

Taiwan ist eines der Länder, das am häufigsten Cyber-Angriffen ausgesetzt ist. Diese unglückliche Realität hat unerwartet eine robuste AI-Cybersecurity-Industrie geboren.

CyCraft, gegründet Ende 2017, ist Taiwans erste Cybersecurity-Firma, die AI mit Endpunkt-Monitoring verbindet. Seine Technologie wurde sieben Mal in Gartner-Berichte aufgenommen, Taiwans einzige Firma, die dreimal den amerikanischen MITRE ATT&CK Autoritäts-Test bestand[^18]. Im Februar 2026 war CyCraft auf Taiwans Emerging Stock Exchange gelistet und wurde Taiwans Kapitalmarkt's erste AI-Cybersecurity-Software-Originalfabrik mit internationaler Eigenforschung und -entwicklung[^19].

CyCrafts Kunden umfassen taiwanische Behörden, Verteidigungs-Abteilungen, Banken und Halbleiter-Unternehmen — dies sind genau die Ziele, die am meisten von nationalem Ebene Hacker-Zielen ins Visier genommen werden. Das Unternehmen hat Tochtergesellschaften in Japan und Singapur und exportiert „Kampf-Erfahrungen aus Hacking" an die gesamte Asia-Pacific.

Dieser Fall zeigt eine Sache: Taiwans AI-Vorteil kommt nicht nur von Halbleitern, sondern auch von praktischen Fähigkeiten, die von einer speziellen Geopolitik geschärft wurden.

---

## Politik: Vom „AI-Jahr" zum Ministerium für Digitale Entwicklung

Taiwans AI-Politikentwicklung kann durch drei Wendepunkte verstanden werden.

2017 bis 2018 war die Startphase. Die Executive Yuan erklärte 2017 zum „AI-Jahr", führte das Konzept „AI Small Country Big Strategy" ein und erkannte an, dass Taiwans Markt klein ist, aber betonte Halbleiter-Fertigung, ICT-Lieferketten und technische Talente als drei Karten. 2018 startete die erste „Taiwan AI Action Plan", investierte über 40 Milliarden New-Taiwan-Dollar über vier Jahre, der Schwerpunkt baute AI-Rechenfundamentale Infrastruktur „Taiwan AI Cloud" (TWCC)[^20].

2022 ging es zu Institutionalisierung. Das Ministerium für Digitale Entwicklung (MODA) wurde gegründet und integrierte digitale Geschäfte aus Science and Technology Ministry, Economy Ministry und Transportation Ministry. Die Bedeutung dieses Schritts lag darin: AI-Politik aufgewertet von „Science and Technology Ministry's Projekt" zu „nationale Strategie mit abteilungsübergreifender Zusammenarbeit". Im selben Jahr gab die Regierung die „Guidelines for AI Research and Development" aus, die Prinzipien betont wie menschenzentriert, transparent und erklärbar, fair und unvoreingenommen.

2023 bis jetzt ist die generative AI-Wende. ChatGPT's Schock ließ die Politik sich schnell ändern. TAIDE-Programm gestartet, AI-Grundgesetz-Entwurf vorangetrieben, beschleunigte öffentliche Abteilung AI-Adoption. Taiwans Strategie ist sehr praktisch: Statt Papierverlauf in Grundlagenforschung mit USA und China zu konkurrieren, verbindet Taiwan AI mit bestehenden Fertigungs-Vorteilen. Intelligente Fertigung, medizinische Bildgebung, Halbleiter-Ausschussquoten-Vorhersage — diese sind alle Felder, wo Taiwan Daten, Szenen und Wettbewerbsfähigkeit hat.

Das Problem ist, dass die zwei Nobelpreise im Oktober 2024 in Stockholm keine Namen von dieser „intelligenten Fertigungs-Route" hatten.

---

## Besorgnis: Die Softwarelücke eines Hardware-Reiches

Hinter den glänzenden Zahlen gibt es ein strukturelles Problem in Taiwans AI-Entwicklung: Eine schwere Unausgeglichenheit zwischen Hardware und Software.

Taiwan produziert neunzig Prozent der globalen AI-Server und den Großteil der AI-Chips, aber bei AI-Modellentwicklung, Daten-Ökosystem und Plattform-Software ist die Präsenz sehr niedrig. Unter den top zwanzig globalen AI-Modellen — darunter GPT, Claude, Gemini, LLaMA — keines kommt aus Taiwan. Wenn man die 2024 Double Nobelpreis Gewinn-Arbeiten anschaut: Hopfield Network, Backpropagation bis AlphaFold, alle drei sind weit entfernt von Taiwans Industrie.

Der Grund ist eine neue Version eines alten Problems. Wenn ein Taiwan Semiconductor Manufacturing Company Ingenieur über zwei Millionen New-Taiwan-Dollar verdienen kann, ist es schwer für eine Software-Startup top Talent zu greifen. Google, Microsoft, NVIDIA etablierten Forschungs-Zentren in Taiwan, und Gehalt plus Vorteile bilden einen starken Saugeffekt. Ein Absolvent der National Taiwan University Computer Science Abteilung's erste Wahl ist oft eine ausländische Firma oder Taiwan Semiconductor Manufacturing Company IT, nicht ein lokales AI-Startup beitreten.

Die fundamentalere Herausforderung ist Daten. AI-Modell-Wert kommt von Trainingsdaten, und hochwertige traditionelle chinesische Daten-Volumen, im Vergleich zu Englisch oder vereinfachtem Chinesisch, ist winzig. Der Text, der von Taiwans 23 Millionen Menschen produziert wird, kann natürlich nicht Englisch-Sprach-Welt oder Festlandchina-Volumen entsprechen. TAIDE-Programm versuchte, dieses Problem zu lösen, aber der strukturelle Daten-Volumen-Nachteil bleibt.

Taiwans echte AI-Wette fiel auf vertikale Anwendung statt Basis-Modelle: Statt mit OpenAI oder Google im generisches Modell direkt zu kämpfen, wählte Taiwan nicht-ersetzbaren Platz in Halbleiter-Prozess AI, medizinische Bildgebungs-AI, Cybersecurity-AI, traditionales Chinesisch NLP zu finden. In diesen Feldern hat Taiwan einzigartige Daten und Szene-Vorteile, was andere schwer kopieren können.

---

## Eine Insel's AI-Wahl

2026 steht Taiwan in einer einzigartigen Position: Es war noch nie so unverzichtbar in der AI-Hardware-Lieferkette, bleibt aber dennoch peripher im AI-Software-Ökosystem.

Dies ist nicht vollständig schlecht. In der Geschichte war Taiwans Erfolgs-Muster immer „nicht die Marke sein, sondern die Marke hinter der Marke sein". Das reine Foundry-Modell, das Morris Chang 1987 erfand, ließ Taiwan Semiconductor Manufacturing Company zu den top zehn Welt-Marktwert-Firmen werden. Heute wird die gleiche Logik in der AI-Server-Industrie wiederholt: Foxconn macht kein AI-Modell, aber alle Welt-AI-Modelle laufen auf Foxconn's zusammengebauten Servern.

Aber AI-Zeit-Spiel-Regeln könnten unterschiedlich sein. Wenn Wert-Zentrum von Hardware zu Software und Daten rutscht, wird der Gewinn-Raum von nur Foundry verdichtet. Die beiden Nobelpreise 2024 waren alle an Software-Schicht-Menschen. Hopfield schrieb ein mathematisches Modell, Hinton schrieb einen Training-Algorithmus, Hassabis schrieb eine Biologie-Lösung. Diese Arbeit läuft alle auf Taiwan-Hardware, aber der Preis nicht für Hardware.

Taiwan braucht, um Software und Daten-Fähigkeit auf der Hardware-Hegemonie-Basis wachsen zu lassen: Hardware bleibt noch Fundament, neue Wert-Schichten stapeln sich drauf. TAIDE ist ein Versuch, CyCraft ist ein Versuch, Taiwan AI Labs ist ein Versuch. Der gemeinsame Punkt ist: nicht versuchen, „das größte AI der Welt zu machen", sondern „das beste AI, das Taiwan versteht, zu machen".

42 Jahre vorher, als Hopfield seine 12 Seiten in Princeton schrieb, wusste niemand, dass dies die mathematische Basis von Welt's Gedächtnismodell werden würde. 50 Jahre vorher, als Anfinsen in seiner Nobelrede die Protein-Faltungs-Hypothese vorschlug, hätte niemand erwartet, bis dass dieser London-Gruppe-Nachmittag 2020 es aufgelöst hätte. Die Zeit-Skala der Grundlagenforschung ist länger als jede einzelne Computex-Szene.

Das Ningxia-Nachtmarkt-Essen ist die Position Taiwans, die 42 Jahre angehäuft hatte. Wo die nächste Schlacht ist — nicht vor dem Austern-Suppen-Stand, sondern darin, ob Taiwan den Mut hätte, dass ein Student, der gerade jetzt im Wohnheim der National Taiwan University Programmiert, 20, 30 Jahre später einen Nobelpreis für diese Insel bekäme.

---

**Weitere Lektüre**:

- [Die Aufstieg der AI-Insel: Taiwans künstliche Intelligenz Entwicklung und Zukunfts-Strategie](/technology/AI-development) — Frühere Version's Politischer Rahmen-Narrativ, AI-Action-Plan, fünf große Strategie-Bereiche, wie Halbleiter-Schutzgott-Berg mit der AI-Revolution gepfropft ist das gesamte Panorama.
- [Taiwan Artificial Intelligence Lab](/technology/Taiwan-artificial-intelligence-lab) — Ethan Tu von PTT zu AI Labs gesamter Prozess, TAIDE / TAME / FedGPT Open-Source-Sprach-Modell-Ökosystem.
- [Taiwan Artificial Intelligence School](/technology/Taiwan-artificial-intelligence-school) — Der Anruf, der nicht abgeschlossen wurde, mit Chen Shen-Wei 180 Millionen privaten Mitteln gegründete AI-Militärschule: Acht-Jahre Schulabsolventenzahl Zehntausende der Talentkultur-Geschichte.
- [Taiwan AI daily](/technology/Taiwan-AI-daily) — Generativer AI trat in Taiwans tägliches Leben ein, geschriebene Szene-Ebene-Beobachtung von Convenience Store Bestellen bis National Health Insurance Administration Batch Audit.
- [Taiwan Enterprise: Taiwan Semiconductor Manufacturing Company](/economy/Taiwan-enterprise-Taiwan-Semiconductor-Manufacturing-Company) — Globale Wafer-Fundry-Drache-Kopf, AI-Chip-Fertigung's Kern, von Morris Chang's reinem Foundry-Modell zur fortgeschrittene Verpackungs-Geschichte.
- [Halbleiter-Industrie](/technology/halbleiter-industrie) — Von IC-Design zu Verpackung-Test, Taiwans Halbleiter-Ökosystem-Gesamtbild.
- [Taiwans Cybersecurity-Industrie Entwicklung](/technology/Taiwan-cybersecurity-industry-development) — Wie Geopolitik-Druck eine Asia-Pacific-Ebene AI-Cybersecurity-Industrie geboren hat.

---

## Bildquellen

Dieser Artikel benutzt 4 Gemeinfrei / CC lizensierte Bilder, alle cached in `public/article-images/technology/` um Hot-Links zu vermeiden:

- [Estructura tridimensional de la proteïna CBLN1 per AlphaFold amb codificació rainbow](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — Held, CBLN1 Protein AlphaFold Vorhersage-Struktur, rainbow Farbkodierung N→C Ende. Photo: BQUB25-UPoch (eigene Arbeit, AlphaFold + PyMOL), 2025-11-15, CC BY 4.0.
- [Geoffrey E. Hinton, 2024 Nobel Prize Laureate in Physics (3x4 cropped)](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>) — Inline, 2024 Nobelpreis-Wochenende Hinton offizielles Porträt. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [John J. Hopfield, 2024 Nobel Prize Laureate in Physics 1 (cropped)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — Inline, 2024 Nobelpreis-Wochenende Hopfield offizielles Porträt. Photo: Arthur Petron, 2024-12-08, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — Inline, Taiwan Semiconductor Manufacturing Company Hsinchu Fab 5 Fabrik, AI-Chip-Fertigung's physischer Ort. Photo: Wikimedia Commons (existierende Cache).

---

## Referenzen

[^1]: [Tom's Hardware: Semiconductor legends take a stroll in a Taiwanese night market](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — 29. Mai 2024 Ningxia-Nachtmarkt-Szene Berichtet, Huang, Chang, Lin, Tsai Tafel mit Essen-Szene aufgezeichnet.

[^2]: [Taiwan News: Nvidia CEO calls Taiwan 'one of the most important countries in the world'](https://www.taiwannews.com.tw/news/5880054) — 2024-05-30 Huang's Taiwan-Besuch öffentliche Aussage.

[^3]: [Wikipedia: Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — Huang 1963 geboren in Taipei, Kindheit in Tainan, neun Jahre alt wanderte in USA ein — Biographie-Daten.

[^4]: NVIDIA alle fortgeschrittenen GPU (A100, H100, Blackwell Serien) sind alle von Taiwan Semiconductor Manufacturing Company hergestellt. Siehe [Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — Abdeckung NVIDIA AI GPU gesamte Serie Foundry-Beziehung's Industrie-Analyse.

[^5]: [SQ Magazine: AI Chip Statistics 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — 2025 Taiwan Semiconductor Manufacturing Company Wafer-Foundry-Umsatz-Anteil 72 Prozent Daten-Quelle; siehe auch Motley Fool selben Periode Bericht.

[^6]: [PatentPC: The AI Chip Market Explosion](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — NVIDIA AI GPU Markt-Anteil 86 Prozent Daten-Quelle.

[^7]: [Tech-Now: Taiwan Leads Global AI Server Shift, Surpassing iPhones in 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — Foxconn, Quanta, Wistron global AI-Server 90 Prozent Versand-Daten.

[^8]: [DigiTimes: Foxconn, Wistron, Quanta to sustain trillion-dollar revenue on AI server in 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — Drei Firmen Jahre-Umsatz brechen eine Billion, AI-Server übertreffen Unterhaltungs-Elektronik's Daten Bericht.

[^9]: [36Kr: Who Will Divide Up the CoWoS Production Capacity in 2026?](https://eu.36kr.com/en/p/3580962946874242) — NVIDIA CoWoS-Wafer-Nachfrage 595.000 Wafer, Welt-Gesamt 60 Prozent Daten.

[^10]: [NVIDIA Newsroom: Foxconn Builds AI Factory in Partnership With Taiwan and NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — Kaohsiung 100MW AI-Fabrik Zusammenarbeit-Angebot; siehe auch CNBC Bericht 100MW Kraft-Kapazität.

[^11]: [Taiwan AI Labs offizielle Website Über uns](https://ailabs.tw/zh/關於我們/) — Ethan Tu 1995 bei National Taiwan University gründete PTT, 2017 April Rückkehrer Taiwan gründete Taiwan AI Labs official brief.

[^12]: [TechNews 科技新報: AI talent in Taiwan, should go or stay? Interview Taiwan AI Labs founder Ethan Tu](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — Anting Verbatim Script, föderales Lernmedizin AI Kern-Projekt-Einleitung.

[^13]: [Executive Yuan: Perfecting Taiwan's AI Foundation Infrastructure — Create Trustworthy AI Dialogue Engine TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — April 2023 TAIDE Plan Starten offizieller Erklärung.

[^14]: [Common Wealth: Prevent China AI cultural invasion Taiwan's first Traditional Chinese large language model TAIDE, what can it do?](https://www.cw.com.tw/article/5129076) — TAIDE Haupt-Bericht, Traditionelles Chinesisch LLM kulturelle Hauptdelproblem Diskurs Quelle.

[^15]: [National Science and Technology Council: TAIDE one year achievement public-private cooperation jointly advance traditional Chinese characteristic large language model](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — April 2024 TAIDE-LX-7B kommerzielle Version, 13B akademische Version Freigabe.

[^16]: [CloudInsight: Taiwan LLM Development Status 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — TAIDE 2.0, Breeze-8B etc. Taiwan LLM Ökosystem vollständig Bestandaufnahme.

[^17]: Siehe oben CloudInsight Bericht. National Chung Hsing University „Shen-nong TAIDE", National Taiwan University of Science and Technology Taiwan-Englisch Dialog-Roboter, National Yang Ming Chiao Tung University Taiwan Hakka TAIDE Modell Anwendungs-Fallstudien detailliert.

[^18]: [CIO Taiwan: Taiwan Cybersecurity Vendors Tour — CyCraft Technology](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — CyCraft sieben Mal in Gartner, drei Mal bestanden MITRE ATT&CK Test detailliert.

[^19]: [CyCraft offizielle Website: Emerging Stock Board First Issue AI Cybersecurity King! CyCraft Cyberattack Listed Today](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — 5. Februar 2026 Emerging Stock Board Listing Nachrichts-Brief.

[^20]: [National Science and Technology Council: AI Science Research Strategy](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — Erste Periode Taiwan AI-Action-Plan 40 Millionen Budget, TWCC Aufbau etc. Politik-Rahmen.

[^N1]: [The Nobel Prize in Physics 2024 press release](https://www.nobelprize.org/prizes/physics/2024/press-release/) — 8. Oktober 2024 Königlich Schwedische Akademie der Wissenschaften offizielle Ankündigung. Original: „The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.'" Preisgeld 11 Millionen schwedische Kronen, zwei teilen.

[^N2]: [The Nobel Prize in Chemistry 2024 press release](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — 9. Oktober 2024 Ankündigung. Preisgeld 11 Millionen schwedische Kronen, David Baker eine Hälfte „for computational protein design", Demis Hassabis und John Jumper teilte die andere Hälfte „for protein structure prediction".

[^N3]: Hopfield, J. J. (1982). "Neural networks and physical systems with emergent collective computational abilities." [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Hopfield Network Ursprungs-Papier, Neuronale Netzwerk-Analogie als Spin-Glas-System, energy-minimum Gedächtnis-Speicherung vorschlag. April 1982 veröffentlicht.

[^N4]: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). "Learning representations by back-propagating errors." [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — Backpropagation Algorithmus klassisch Papier, Neuronale Netzwerk Training-Verfahren Grund-Arbeit.

[^N5]: Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — AlexNet Ursprungs-Papier, ImageNet ILSVRC-2012 Top-5 Fehlerquote 15,3 Prozent (zweiter Platz 26,2 Prozent), Deep Learning Industrialisierung kritischer Wendepunkt.

[^N6]: [PanSci: 2024 Nobel Physics Prize — Hopfield and Hinton opened the era of artificial neural networks machine learning](https://pansci.asia/archives/378242) — Content Curation Partner per MOU 2026-05-05. Abdeckung Hopfield Network Hintergrund, Spin-Glas Analogie, Papier-Zitat-Volumen-Ansammlung, und modernen Deep Learning mathematische Verbindung.

[^N7]: [The Guardian: Nobel physics prize 2024 winner John Hopfield warns of AI dangers](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — 2024-10-08 Nobelpreis Physik Telefoninterview Bericht, Hopfield und Hinton selben Tag AI-Risiko-Warnung.

[^N8]: [Wikipedia: Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton 6. Dezember 1947 geboren in Wimbledon London, März 2013 Google gekauft DNNresearch 44 Millionen Dollar nach Hinton beigetreten.

[^N9]: [BBC News: AI 'godfather' Geoffrey Hinton warns of dangers as he quits Google](https://www.bbc.com/news/world-us-canada-65452940) — 1. Mai 2023 Hinton Google verlassen nach BBC AI-Risiko-Besorgnis. Original „I left so that I could talk about the dangers of AI without considering how this impacts Google", „a part of me now regrets my life's work". Selbe Periode NYT Interview Details auch diese Bericht zitieren.

[^N10]: [Nature: AI scientist Geoffrey Hinton wins Nobel prize for physics](https://www.nature.com/articles/d41586-024-03213-8) — Nature 2024 Nobelpreis Physik Verleihungs-Szene und Hinton Telefoninterview detailliert.

[^N11]: [Wikipedia: Economic history of Taiwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — 1986 Taiwan BIP Daten; Hsinchu Science Park gegründet 12. Dezember 1980.

[^N12]: Anfinsen, C. B. (1973). "Principles that govern the folding of protein chains." [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — 1972 Nobelpreis Chemie Gewinn-Arbeit eine, Protein-Faltung bestimmt durch Aminosäure-Sequenz Hypothese Vorschlag.

[^N13]: [Nature: 'It will change everything': DeepMind's AI makes gigantic leap in solving protein structures](https://www.nature.com/articles/d41586-020-03348-4) — 30. November 2020 CASP14 Ergebnis-Veröffentlichung Bericht, AlphaFold 2 Medien GDT 92,4, CASP Organisator John Moult Evaluierung „in some sense the problem is solved".

[^N14]: [DeepMind: AlphaFold reveals the structure of the protein universe](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — 28. Juli 2022 Ankündigung AlphaFold Protein Structure Database 1 Million Spezies, etwa 200 Millionen Protein-Struktur-Abdeckung.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — 8. Mai 2024 AlphaFold 3 Veröffentlichung, erweitert zu Protein mit DNA / RNA / Ligand / Ionen Komplexe Vorhersage.

[^N16]: [Wikipedia: Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis 4 Jahre alt begann Schach spielen, 13 Jahren (1947 Meister Rang, 17 Jahre (1994) mit Peter Molyneux gemeinsam entwickelt Theme Park, 2010 London DeepMind gegründet, 2014 Google gekauft etwa 400 Million Pfund.

[^N17]: [Academia Sinica Genome Research Center](https://www.genomics.sinica.edu.tw/) — Prorektor Yung-Ya Lin Amtszeit (2006–2016) gegründet Zucker-Molekül Protein-Struktur Forschungs-Zentrum.

[^N18]: [PanSci: 2024 Nobel Chemistry Prize — David Baker, Demis Hassabis, John Jumper solved 50-year protein folding puzzle](https://pansci.asia/archives/378388) — Content Curation Partner per MOU 2026-05-05. Abdeckung AlphaFold Nobelpreis Chemie Streit, Struktur-Biologie vs Berechnung-Chemie Disziplin-Grenze Diskussion.

[^N19]: [PanSci: AlphaFold 3 predicts protein molecular interactions, drug development upgraded again](https://pansci.asia/archives/377917) — Content Curation Partner per MOU 2026-05-05. AlphaFold 3 Droge Entwicklung, Enzym Technik Unten-Strom Effekt Analyse.

[^N20]: [PanSci: "Artificial Brain" OI Challenges AI — Can brain tissue in petri dish replace silicon chip?](https://pansci.asia/archives/366027) — Content Curation Partner per MOU 2026-05-05. Thomas Hartung Team Johns Hopkins künstlicher Gehirn-Forschung, als AI Weg-Alternative Berechnung Richtung.
