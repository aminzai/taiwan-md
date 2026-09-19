---
title: 'Der Backslash im Zeichen „Gōng“: Die zwei Schichten Standard-Steuer, die taiwanesische Ingenieure täglich zahlen'
description: "Auf einem Windows 11 mit Locale zh-TW warf das Übersetzungsstatus-Skript die über 4000 erfassten Pfade allesamt in „root“, „Technology“ wurde null, während die Linux-CI in derselben Woche grün war. Das Skript trennt Kategorienamen mit Slash, das Dateisystem nutzt Backslash – es lässt sich nicht auftrennen. Eine ältere Schicht steckt im Zeichen selbst: Das zweite Byte von „Gōng“ (功) in Big5 ist der ASCII-Backslash, in Entwicklerkreisen „Xǔ Gōng Gài“ (許功蓋) genannt. Wie Pfade geschrieben sind, welche Symbole in Zeichen wohnen – die Standardwerte haben diese Maschine nicht mitgedacht. Git's quotePath ist eine weitere, anders gelagerte Linie."
date: 2026-08-13
category: 'Technology'
tags:
  [
    'Open Source',
    'Windows',
    'Big5',
    'UTF-8',
    'Zeichenkodierung',
    'Traditionelles Chinesisch',
  ]
subcategory: '文字與工具'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-13
lastHumanReview: false
translatedFrom: 'Technology/功字裡的那根反斜線.md'
sourceCommitSha: '5dcaeea42'
sourceContentHash: 'sha256:57b41e308a296fb4'
sourceBodyHash: 'sha256:9af4500f829effce'
translatedAt: '2026-09-19T01:37:32+08:00'
---

> **30-Sekunden-Überblick:** Ich führte das Übersetzungsstatus-Skript aus, der Bildschirm zeigte 4546, alles in `root`. Auf GitHub war die Linux-CI grün. Erst später erkannte ich zwei Dinge. Der Backslash in Windows-Pfaden, das Skript trennt mit Slash und kommt nicht durch. Das zweite Byte von „Gōng“ in Big5 ist selbst der ASCII-Backslash `\`. Zwei Dinge, unterschiedliche Mechanismen, doch sie treten oft auf demselben traditionell-chinesischen Windows gemeinsam auf.

Ich betreue auf einem Windows 11 mit Locale zh-TW das Übersetzungsstatus-Skript von Taiwan.md. An jenem Abend startete ich wie gewohnt `i18n-status.py` und wartete, bis das Terminal die Zahl ausgab. Die Konsole lief unter cp950. Die Ausgabe zeigte keine roten Fehler.

Der Bildschirm blieb bei 4546 stehen. Alles in einer einzigen Kategorie namens `root`. Technology stand auf 0.

In derselben Woche, nach dem Push auf GitHub, war die CI unter Linux grün.

Die Skriptvariable heißt `zh_articles`, sie scannt Pfade unter `knowledge` – außer den englischen, about- und Unterstrich-Verzeichnissen; Japanisch, Koreanisch, Arabisch werden ebenfalls mitgezählt. An jenem Abend schaffte sie es nicht einmal, die Kategorienamen herauszuschneiden; über viertausend Pfade landeten im selben Fach. Keine Ausnahme, keine Warnung. Die Statistik sah aus, als sei die ganze Site kaputt, dabei fehlte keine einzige Datei.[^8]

Auf der Platte lauten die Pfade `knowledge\Technology\irgendein-artikel.md`, Verzeichnisse werden durch Backslash getrennt. Das Skript nutzt `split('/')`, um den Kategorienamen zu holen. Unter Linux funktioniert diese Zeile, weil Pfade dort nun mal Slash nutzen. Unter Windows trifft sie den Backslash nicht, der komplette Pfad kommt unverändert zurück, der Artikel wird in das Standard-`root` geworfen.[^1]

Nachdem ich `pathlib` die Verzeichnisbehandlung überließ, standen unter Technology 59 Artikel – exakt so viele wie im Ordner. Dazwischen lag nur eine Annahme: Welche Art Strich deine Maschine als Trennzeichen nutzt.

> **📝 Kuratorische Anmerkung:** Die Skriptsyntax war nicht falsch, die CI lief tatsächlich durch. Der Riss liegt zwischen „der Maschine, vor der der Autor tatsächlich sitzt“ und „der Maschine, die das Tool annimmt“. Diese Naht gehört keinem einzelnen Glied der Kette, also fühlt sich niemand zuständig, sie im Blick zu behalten.

## Der Strich im „Gōng“

Der Pfad ist die erste Schicht. Die zweite ist älter, sie sitzt im Zeichen.

Big5 wurde 1984 finalisiert, ein chinesisches Zeichen zwei Bytes. Fällt das zweite Byte in `0x40` bis `0x7E`, überlappt es mit gängigen ASCII-Symbolen: `[`, `]`, `{`, `}`, `\`, `|`. Der damalige stellvertretende Professor am Department of Information Management der Chaoyang University of Technology, Hong Chao-gui (洪朝貴, Ruhestand August 2023), schrieb auf seiner Lehrseite: „Da 40-7E der ASCII-Codebereich gängiger Zeichen ist, bereitet dies Programmierern manchmal Schwierigkeiten.“[^2]

„Gōng“ (功) hat den Code `A5 5C`. Das nachfolgende `0x5C` ist im ASCII der Backslash `\`. Ein Programm, das byteweise einen String scannt und `\` als Escape- oder Trennzeichen behandelt, stolpert über die zweite Hälfte von „Gōng“ und hält sie für einen Pfadtrenner. Steht „Gōng“ im Dateinamen oder im Pfad, kann es hier stürzen.

In den Entwicklerkreisen Taiwans und Hongkongs heißt das Phänomen „Xǔ Gōng Gài“ (許功蓋): „Xǔ“ ist `B3 5C`, „Gōng“ `A5 5C`, „Gài“ `BB 5C` – drei häufige Zeichen, hintereinander geschrieben wie ein Personenname.[^5] Hong Chao-gui listete zusätzlich „Jiā Yě Chéng Zhèn Gōng“ (加也程陣功) auf, deren zweites Byte jeweils auf `[`, `]`, `{`, `}`, `\` fällt, und veröffentlichte das Scan-Tool `b5tm`.[^2] Wenn ein Bug einen Personennamen bekommt, liegt das meist daran, dass er häufig genug auftritt, damit eine Generation ihn beim Namen nennen kann.

2015 wechselte der Autor des Blogs „Dark Thread“ (黑暗執行緒) auf Visual Studio 2015. Die alten `.cs`-Dateien lagen noch im BIG5-Format. Nachdem der Compiler auf Roslyn umgestellt wurde, verwandelten sich die Xǔ-Gōng-Gài-Stellen in den Dateien in Kompilierfehler.

Zwei Tage später sagte ein Kollege, sie seien ebenfalls hängengeblieben, hätten lange gesucht und schließlich genau jenen Artikel wiedergefunden. Ein Nutzer hatte zehntausende Dateien, die Konvertierung ließ noch Hunderte übrig, „man konnte nur VS2015 Goodbye sagen“. Später schrieb er ein Batch-Tool zur UTF-8-Konvertierung, weil manuelles Speichern nicht mehr schaffbar war.[^7]

Das ist nicht dieselbe Sache wie das vorige `split('/')`. Das eine ist ein modernes Tool, das annimmt, wie ein Pfad aussieht. Das andere ist die Entscheidung vor vierzig Jahren, Doppelbyte zu wählen, wodurch Symbole in den Leib der Zeichen einzogen. Unterschiedliche Mechanismen, aber die Rechnung kommt oft auf demselben cp950-Rechner zusammen. Wie die Eingabeseite Zeichen in den Computer bringt, siehe [Ostasiatische Eingabemethoden](/de/technology/east-asian-input-methods/). Hier geht es darum, was passiert, nachdem die Zeichen bereits auf der Platte liegen – ob die Toolchain sie noch erkennt.

## Die Standardwerte haben für diese Maschine keinen Zweig geöffnet

Git hat `core.quotePath` standardmäßig aktiv. Dateinamen mit Bytes über `0x80` zeigt `git status` als Oktal-Sequenzen wie `\344\270\255`. Die chinesischen Dateinamen sind noch da, man versteht nur nicht mehr, was das eigene Repository sagt.[^3] Es escaped die High-Bytes von UTF-8. Big5s `0x5C` ist eine andere Linie. Beiden sieht man den Backslash an, die Ursache ist eine andere.

Python 3 unter Windows nutzt bei `open()` ohne `encoding='utf-8'` möglicherweise die System-Locale. Dieselbe UTF-8-Datei, Linux liest sie, diese Maschine deutet sie per cp950 – Satzzeichen oder Zhuyin zerbrechen.[^4] Ich habe das einmal bezahlt: Per PowerShell 5.1 `Get-Content | Set-Content` eine UTF-8-Datei bearbeitet, der lange Gedankenstrich wurde im Diff zu `??`. Auch das ist Standard-Steuer, nicht das zweite Thema.

Wenn Statusmeldungen Emoji enthalten, stürzt diese cp950-Konsole direkt ab. Der Zeichensatz kennt diese Symbole nicht, Python kann sie nicht ausgeben, die Exception knallt bis nach ganz oben. Die Linux-CI fängt das nicht, weil sie nicht auf dieser Maschine läuft.

Git, Python, CI-Beispielpfade mit `$HOME/project/src` – für zh-TW-Windows wurde kein eigener Zweig geöffnet.

Hong Chao-gui sagte 2015 in einem iThome-Interview über Regierungsdokumente, welches Format sie öffnen und wie lange sie leben. Der Artikel gibt seine Aussage wieder: Wenn die Regierung nur Microsoft-Produkte nutzt, um Dateien zu öffnen, vertraut sie darauf, dass Microsoft länger lebt als die Republik China.[^6] Jener Satz handelt von Dateiformaten und Aufbewahrungsfristen. An welche Standard-Toolkette Daten gebunden sind, wird mit der Zeit zur Frage, wer sie noch lesen kann. Open-Source-Zusammenarbeit bindet sich an die Standardumgebung einer bestimmten Maschinenart. Zum Ringen zwischen Civic Tech und Regierungsdateiformaten siehe [Open-Source-Community und g0v](/de/technology/open-source-and-g0v/). Zur Kultur, mit der taiwanesische Entwickler diese Diskrepanz langfristig absorbieren, siehe [Taiwanesischer Open-Source-Geist](/de/technology/taiwan-open-source-spirit/).

Pfadtrennzeichen, Terminalkodierung, `$HOME` in CI-Beispielen – nirgends wurde ein Ast für diese Maschine angelegt. An dem Tag, als 4546 Pfade falsch einsortiert wurden, meldete keine einzige Codezeile einen Fehler. Die Statistik sah normal aus, bis man vor dieser Maschine saß.

## Weiterführende Links

- [Taiwanesischer Open-Source-Geist](/de/technology/taiwan-open-source-spirit): Kultur und Kontext der Beteiligung taiwanesischer Entwickler an Open Source.
- [Ostasiatische Eingabemethoden](/de/technology/east-asian-input-methods): Wie Zeichen in den Computer gelangen, von Zeichentabellen bis zur Tastatur.
- [Open-Source-Community und g0v](/de/technology/open-source-and-g0v): Zusammenarbeit zwischen offenen Daten und Regierungsformaten.

## Quellen

[^1]: [Microsoft Learn: Dateipfadformate auf Windows-Systemen](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — .NET-Dokumentation erklärt, dass klassische DOS-Pfade Backslash als Verzeichnistrenner nutzen, Slash wird in Backslash umgewandelt.

[^2]: [Hong Chao-gui: Big-5-Kodierungsprobleme, die beim Programmieren auftreten können](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Lehrseite listet häufige Zeichen auf, deren zweites Byte in den gefährlichen ASCII-Bereich fällt (Jiā Yě Chéng Zhèn Gōng), und stellt das Scan-Tool b5tm vor. Am Seitenende keine Angabe der akademischen Rangstufe. iThome 2015 nennt ihn stellvertretenden Professor. Eigene Homepage führt 1997–2023 am Chaoyang Department of Information Management, Ruhestand August 2023.

[^3]: [git-config: core.quotePath](https://git-scm.com/docs/git-config) — Offizielle Dokumentation: Standardmäßig werden Pfade mit Bytes > 0x80 als Oktal-Escape-Sequenzen angezeigt.

[^4]: [Python 3: open()](https://docs.python.org/3/library/functions.html#open) — Funktionsdokumentation: Wird encoding nicht angegeben, kann die System-Locale als Standardkodierung herangezogen werden.

[^5]: [Wikipedia: Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Führt „Gōng“ 0xA55C, „Xǔ“ 0xB35C, „Gài“ 0xBB5C auf und erläutert, dass dieses Problem scherzhaft Xǔ Gōng Gài genannt wird.

[^6]: [iThome: Interview Hong Chao-gui](https://www.ithome.com.tw/news/93606) — 2015-Interview, im Text als stellvertretender Professor am Department of Information Management der Chaoyang University of Technology bezeichnet. Originalseite oft 403, der Satz zur Microsoft-Lebensdauer nur über Suchergebnisse zitierbarer Berichterstattung wiedergegeben, nicht als wörtliches Originalzitat.

[^7]: [Dark Thread: Potenzielle Lösung – VS2015 BIG5-Kompatibilitätsproblem beheben](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — 2015er Eintrag zur Kompilierung von BIG5-Quellcode unter Visual Studio 2015, Xǔ Gōng Gài verursacht Kompilierfehler. Text enthält „man konnte nur VS2015 Goodbye sagen“.

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Zusammengeführt am 2026-07-26. Vor dem Fix unter Windows nur root: 4546 Kategorien, nach Fix Technology zh: 59. Gleichzeitig Entfernung der Emoji, die die cp950-Konsole zum Absturz brachten.
