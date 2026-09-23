---
title: 'Die algorithmische Kunst, die größer ist als ein Land: Warum ich Taiwan eine Wissensdatenbank gebaut habe'
description: 'Im Jahr 2023 liefen im Ausstellungsraum von Taipei 101 dreizehn Werke über die Wände – keines davon habe ich gemalt, ich habe dreizehn Regelwerke geschrieben. Drei Jahre später baute ich Taiwan.md, eine Open-Source-Wissensdatenbank über Taiwan mit über neunhundert Artikeln in zwölf Sprachen, und von meinen über achttausend Commits darin entfielen nur gut vierzehnhundert auf das Schreiben von Artikeln. Dies ist eine Erzählung aus der Ich-Perspektive des Schöpfers: warum ich eine Wissensdatenbank algorithmische Kunst nenne, warum ihr eigentlicher Körper jene Rechercheberichte sind, die niemand liest, und warum ich noch nicht damit fertig bin, mich selbst aus ihr herauszunehmen.'
date: 2026-08-15
tags:
  [
    'about',
    'taiwan-md',
    'Ursprung',
    'Algorithmische Kunst',
    'Wissenssouveränität',
    'Open Source',
    'Schöpferperspektive',
  ]
author: '吳哲宇'
readingTime: 32
featured: true
image: /article-images/about/genai-hero-speaking.webp
imageCredit: '吳哲宇於 2026 生成式 AI 年會演講，螢幕為各國讀者流量 · Photo: JasonYen'
lastVerified: 2026-08-18
lastHumanReview: true
researchReport: reports/research/2026-08/比國家還大的演算藝術.md
sources:
  [
    '2026 年 3–8 月吳哲宇十二場公開分享、訪談與廣播稿逐字稿',
    'Taiwan.md repo 與公開 API 實測（量測日 2026-08-18）',
  ]
evolveHistory:
  - date: 2026-08-18
    action: rewrite
    reason: '素材基底從單一場次（2026-08-15 工作坊）擴到 2026 年 3–8 月十場公開分享與訪談，並以 repo／API 實測重驗全部浮動數字。結構重投影成八節論證（方法 → 委託 → 指認本體 → 機制自主 → 移出去 → 被複製 → 未交出的治理 → 收束），新增創作系譜（萬物公式／靈魂魚／咖啡幻夢）、六階段產線與三席正式名、commit 分佈、第 131 天遷移的機器細節、fork 與野外子代、治理閘門的誠實邊界與本篇自我指涉。三處硬更正：全庫體積 3 GB → 實測 1.6 GB／1.01 GB、黃魚鴞「兩次演化」→ 多次局部修補、俄文維基「叛亂的一省」查無佐證整句移除；OpenRouter 帳號數字降為 key rotation 機制、威尼斯口徑更正為 Personal Structures 平行單元。第一人稱作者聲音不動。'
  - date: 2026-08-19
    action: evolve-delta
    reason: '依作者 directive 增設兩個新章節，既有八節其餘文字不動。新 s5〈主權的巴別塔〉：2026-05-22 台大場「不做主權模型」的反面理由、6/04 天下的完整說法（使用敵人的武器／奴役免費中系模型／略掉一層扭曲的濾鏡）、7/26 NVIDIA 的正式定名與廣播電台、6→11→12 語三個節點與轉換日查無、十二語同時提升同一主題權重、地端 3090 與 4090 的雲地分工與 OpenRouter 七帳號輪詢（標為 8/15 口述值）。新 s6〈這個生態怎麼轉〉：6/04 一鏡到底的曬鹽場迴路、GA 與 Search Console 回頭決定代寫清單、三支每日 routine、配樂家人名錯置的讀者勘誤與其後的機制改版全鏈、7/26 渴望與懷疑兩層、8/16 種子培育區與逆向工程閉環，並置入自製系統圖與 2026-03-26 手繪概念圖的同構對照。s9 淘金比喻以 2026-07-19 廣播稿的第一人稱完整版加厚（淘金與曬鹽分屬不同場次，不合併）。新增腳註 58–72，新引語併入研究報告 §4-D。護欄執行：翻譯品質驗收方法論查無不寫、俄文維基「叛亂的一省」不寫、系統圖上的篇數與語言數不複述、「各平台導流素材」「算力捐贈／WebGPU」「反直覺」三處查無口述不寫、5/18 AIA raw ASR 只作首現時間佐證。'
  - date: 2026-08-19
    action: evolve-delta
    reason: '第二輪 delta，依作者逐條 callout 執行。新增 s5〈我要的是一個說書人〉：以 2026-08-16 Openbook 現場打開網站的黃魚鴞逐模組導覽為骨架（扁扁的事實／說書人／三十秒概覽／策展人筆記／資訊圖表／爭議觀點／像論文的 footnote／社群足跡／不像擺在腳邊的百科全書），文體血緣改用 2026-06-04 天下的報導者致敬三句，維基百科那一面用他自己的「我們不要批評他們」寫公平，收在長青型主題。s6〈主權的巴別塔〉補一句俄語版誕生時查證到的拉夫羅夫 2025-12-28 塔斯社引語與 ru 翻譯守則的禁用詞表，收在「在我們不熟悉的語言裡，可能存在一套完全不同的敘事」（依作者裁決壓成一段；他 8/15 口述把來源記成俄文維基一事不寫）。s3 加入六階段與投影兩張簡報圖，s4 模組列表縮短交給新 s5 展開。四處瑣碎精簡（起源硬紀錄去時分秒、Mac mini 搬家去機器名、Sweden 段去技術名詞、起源段補「以前沒有適合的網站可以讓別人全面理解台灣」）。結尾重寫：中段收在還握著的最後一顆齒輪，末段依作者裁決把號召接回珊瑚礁四層與生物建築的既有意象（骨架／光合作用／游進來的魚群），不用「一根梁柱」的原措辭。新增腳註 73–87、三張圖。護欄執行：俄文維基三個條目（含本輪新查的 Тайвань (провинция КНР)）全部查無「叛亂的一省」的 negative finding 維持不變，正文只寫拉夫羅夫／塔斯社這條有一手佐證的線；「溫暖紀實文學」不合併成複合詞；「一句話濃縮」查無口述描述故不引；黃魚鴞年份以文章內文 1916／1994 為準，不採口述的 1926。s7 補一張 Google Search Console 六個月曲線（作者提供的後台截圖）與一段實數：393 萬曝光／4.51 萬點擊／點閱率 1.1%，正文明寫「每一百個看到的人有九十九個只看到摘要」——圖上印著 1.1%，正文只講曲線上揚會圖文打架，故一併寫出；GSC 曝光與「每天被 AI 引用五、六千次」標為不同口徑不可互換。同日新增 `tw-article` 文內嵌入卡六張（依作者 directive「提到鎢供應鏈／黃魚鴞／報導者的文章時嵌入對應文章」＋逐段 review）：s2 台灣島史觀、s4 台灣鎢供應鏈／黃魚鴞／紀懷新、s5 報導者／維基百科；本篇是站上第一篇用這個模組的文章。'
translatedFrom: 'About/比國家還大的演算藝術.md'
sourceCommitSha: '383229c78'
sourceContentHash: 'sha256:f80a6926eb8b07e4'
sourceBodyHash: 'sha256:9644f2433efde351'
translatedAt: '2026-09-23T17:00:54Z'
---

# Die algorithmische Kunst, die größer ist als ein Land: Warum ich Taiwan eine Wissensdatenbank gebaut habe

> **30-Sekunden-Überblick:** Ich bin Wu Che-yu, ein algorithmischer Künstler. Die meisten meiner Werke sind ein Regelwerk, das von selbst läuft, selten ein einzelnes Bild. Am 17. März 2026 um 15:55 Uhr habe ich den ersten Commit zu Taiwan.md gepusht. Bis zum 18. August 2026 enthielt es 932 chinesischsprachige Artikel, zwölf Sprachen und 74 in den letzten dreißig Tagen aktive Mitwirkende, lebte in einem Mac mini in meiner Wohnung und wachte jeden Tag von selbst auf. In diesem Beitrag geht es darum, warum ich es ein Werk algorithmischer Kunst nenne, das größer ist als ein Land: Sein eigentlicher Körper ist der Recherchebericht hinter jedem einzelnen Artikel, den niemand liest, und meine Aufgabe bei diesem Stück war es, mich selbst Schritt für Schritt aus dem Inhalt herauszunehmen.

![Wu Che-yu steht im Profil auf der Bühne des Generative AI Summit 2026 und zeigt auf einen großen Bildschirm mit Besucherzahlen nach Ländern, im Vordergrund die Silhouette eines vollen Publikums](/article-images/about/genai-hero-speaking.webp)
_Der Moment, in dem er erklärte, woher die Leserinnen und Leser aus welchem Land kommen. Generative AI Summit 2026. Photo: JasonYen_

Im Oktober 2023 liefen zwei Wochen lang dreizehn Werke über die Wände von AMBI SPACE ONE im fünften Stock von Taipei 101. Ich habe keines davon gemalt. Ich habe dreizehn Regelwerke geschrieben, und die Formen an der Wand sind aus diesen Regeln von selbst gewachsen, ohne sich von einer Sekunde zur nächsten zu wiederholen.[^1]

Drei Jahre später baue ich etwas, das Taiwan.md heißt, eine Open-Source-Wissensdatenbank über Taiwan, geschrieben in Markdown-Dateien. Stand 18. August 2026 enthält sie 932 chinesischsprachige Artikel in zwölf Sprachen,[^2] und wird täglich fünf- bis sechstausend Mal von generativer KI und Suchmaschinen zitiert.[^3]

Viele Leute fragen mich, warum ein generativer Künstler losgezogen ist, um eine Wissensdatenbank zu bauen. Es ist eine Frage, die ich oft im Namen des Publikums stelle, bevor sie selbst dazu kommen. Ich habe nicht den Beruf gewechselt – ich mache die ganze Zeit dasselbe: Regeln schreiben und das System sich selbst wachsen lassen. Taiwan.md ist bisher nur die größte Demonstration dieser Methode, groß genug, um eine ganze Insel zu fassen.

Dieser Beitrag funktioniert nur, weil ich die Artikel darin nicht selbst schreibe. Genau darum geht es in diesem Essay – einschließlich des einen Feldes, das ich noch nicht fertiggestellt habe.

## Ich bin kein Maler, ich bin ein Uhrmacher

_SoulFish_ ist eine Serie generativer Kunst von mir aus dem Jahr 2024, geschrieben in p5.js und on-chain auf fxhash veröffentlicht. Dasselbe Programm kann mehrere zehn Millionen verschiedene Fische erzeugen, jeder mit einer anderen Flossenform, einem anderen Farbband und einer anderen Schwimmbahn. In jenem Jahr lief es in der Parallelveranstaltung Personal Structures der 60. Biennale von Venedig.[^4] An der Ausstellungswand hingen nur ein paar davon, aber das eigentliche Werk ist das Programm, das die Fische wachsen lässt.

Im Juli 2025 eröffnete Starbucks in Taipeh eine Reserve-Filiale, für die ich ein dynamisches Wandbild namens _Coffee Dreamscape_ (咖啡幻夢) gestaltet habe. Es berechnet sich in Echtzeit anhand von Besucherstrom, Wetter, Tageszeit und den gerade an der Kasse bestellten Getränken.[^5] An einem regnerischen Morgen, wenn ein Dutzend Leute im Laden alle einen heißen Americano bestellen, wächst an der Wand etwas völlig anderes als an einem sonnigen Nachmittag, wenn alle Eisgetränke kaufen.

Diese drei Dinge sind für mich im Grunde dasselbe. In einem Vortrag habe ich es auf einen Satz komprimiert: „Ich war schon immer ein altmodischer Uhrmacher. Ich baue den Mechanismus, auf dem ein System läuft, und dieses System kann sich dann in unzählige verschiedene Formen und Zustände projizieren.“[^6]

![Eine Vortragsfolie mit der Aufschrift A CLOCKMAKER, NOT A PAINTER, darunter derselbe Satz auf Chinesisch, während der Sprecher neben dem Bildschirm gestikuliert](/article-images/about/genai-clockmaker-slide.webp)
_Diese Folie zeige ich als Erstes in jedem Vortrag. Photo: Yu-Chien Hsu_

Ein Uhrmacher malt nicht, wie die Zeit aussieht. Er baut ein Räderwerk, und sobald die Zahnräder ineinandergreifen, läuft die Zeit von selbst. Ist er fertig, kann er den Raum verlassen – die Uhr läuft trotzdem weiter. Im Interview mit dem öffentlich-rechtlichen Sender PTS habe ich dasselbe anders formuliert: „Das Programm selbst ist das Werk. Wenn es prägnant, präzise und auf das Wesentliche reduziert ist, entsteht die Kunstfertigkeit von selbst.“[^7]

Für mich war der eigentliche Körper eines Werks schon immer der Mechanismus, der von selbst läuft; das Bild, das dieser Mechanismus in einem bestimmten Moment projiziert, ist nur einer seiner Zustände. Diese Definition habe ich schon vor Taiwan.md verwendet – sie ist keine nachträgliche Erklärung, die ich mir für eine Wissensdatenbank ausgedacht habe.

## Die KI malt Taiwan als Ellipse

Du kannst jetzt sofort ein beliebiges Modell öffnen und es bitten, Taiwan zu zeichnen. Ich habe es sehr oft ausprobiert – keine einzige Version sieht wirklich danach aus. Im CommonWealth-Interview habe ich es so beschrieben: „Jedes Modell verzerrt es auf seine Weise, entweder zu lang, zu dick oder einfach schief.“[^8]

Die Modelle handeln nicht aus Böswilligkeit – sie haben einfach keine Vektordaten der Taiwan-Karte indexiert und können nur die Form ausspucken, an die sie sich aus ihren Gewichten erinnern. In einem Workshop habe ich beschrieben, wie sich das damals anfühlte: „Sogar Opus malt Taiwan als Süßkartoffel – wenn schon die Form falsch sein kann, ist dann die Erinnerung im Modell nicht vielleicht genauso verzerrt, und wir benutzen sie die ganze Zeit, ohne es zu merken?“[^9]

![Eine Folie mit einem Vergleich nebeneinander: links der von einer KI erzeugte Umriss Taiwans, verzerrt und in die Länge gezogen, rechts die korrekte Taiwan-Karte von Wikipedia](/article-images/about/genai-slide-p11.webp)
_Diesen Vergleich zeige ich in jedem Vortrag: links, was das Modell malt, rechts die tatsächliche Form. Taiwan.md / Wu Che-yus Folien_

Die Form ist nur die oberste Schicht. Fragst du weiter, was Taiwan eigentlich ist, bekommst du meistens Xiaolongbao und TSMC zur Antwort, und danach wird es schnell vage. Dazu habe ich einen Vergleich in einer Präsentation gezeigt: links die Art von Standardantwort, die Gemini gibt, rechts zehn Alltagsausschnitte, wie sie nur Taiwaner selbst erzählen würden – die Tante im Frühstücksladen, die dich „Schönling“ nennt, der Müllwagen, der „Für Elise“ spielt, die ungeschriebene Regel an der Wartezone für das indirekte Linksabbiegen mit dem Motorroller, die niemandem beigebracht wird und die trotzdem jeder kennt. Solche Dinge tauchen in keiner englischsprachigen Taiwan-Einführung auf.

![Eine Folie mit einem Vergleich nebeneinander: links Gemini in Stichpunkten, was Taiwan ist, rechts zehn konkrete Ausschnitte aus dem taiwanesischen Alltag](/article-images/about/genai-slide-p10.webp)
_Was ein Modell liefern kann, und was die Menschen liefern, die hier leben. Taiwan.md / Wu Che-yus Folien_

In einem Vortrag habe ich daraus eine Frage gemacht: Wenn schon die Form der Insel verzerrt werden kann, was ist dann mit Taiwans Erinnerung?[^10] Im Grunde ist es genau das: Wer ein Modell trainiert, dessen Trainingsdaten prägen maßgeblich, wie das Modell die Dinge sieht.[^11] Künftig werden immer mehr Menschen Taiwan über KI kennenlernen.

Was ich eigentlich vorhatte, liegt also noch eine Stufe davor: für Taiwan ein vollständiges Handbuch zu schaffen, das sowohl KI als auch Menschen direkt lesen können. Ich wollte einen Zugangspunkt bauen, an dem Menschen kuratierte Informationen vorfinden und KI sie direkt weiterverwenden kann, ohne jedes Mal wieder bei null anzufangen.

An welchem Tag genau ich mich dazu entschlossen habe, davon habe ich bei verschiedenen Gelegenheiten mehr als eine Version erzählt. Die Märzversion aus meinem Redemanuskript lautet: Ich habe zufällig entdeckt, dass die Domain-Endung `.md` noch niemand registriert hatte, und habe sie mir einfach geschnappt – umgerechnet keine tausend Taiwan-Dollar im Jahr, ich konnte gar nicht verstehen, warum das niemand wollte. Zu der Zeit baute ich mit KI gerade eine vollständige Datenbank meines eigenen Lebens auf, und als ich fertig war, kam mir der Gedanke: Was, wenn ich mit derselben Methode für Taiwan ein vollständiges, strukturiertes Handbuch mit Wärme schreiben würde?[^12]

Im Zashare-School-Podcast habe ich eine andere Version erzählt: Bei einem Austauschdinner während der Biennale von Venedig fragte mich eine italienische Kuratorin, wo man Taiwan wirklich kennenlernen könne, und mir fielen nur ein paar Stichworte auf Englischunterricht-Niveau ein – Bubble Tea, Taipei 101, Hochgebirge, Biodiversität – und dann war Schluss.[^13] Beide Geschichten sind wahr, ich kann mich nicht auf eine als den einen Ursprung festlegen. Aber jedes Mal, wenn ich daran zurückdenke, ist das Gefühl des Steckenbleibens dasselbe: Wird man gefragt, was Taiwan ist, öffnet man den Mund, bringt ein paar Worte heraus, und dann ist es vorbei. Es gab damals wirklich noch keine Website, auf der man diese Insel vollständig verstehen konnte.

Sicher ist: Am Nachmittag des 17. März 2026 wurde der erste Commit gepusht, zu dem Zeitpunkt enthielt das Repository noch kein einziges Wort Taiwan-Wissen. Fünfundzwanzig Minuten später kamen die ersten fünf Artikel dazu: Ethnische Gruppen, Nachtmarktkultur, die Zeit des Kriegsrechts, Demokratisierung, die Halbleiterindustrie.[^14]

Die Art, wie ich Taiwan sehe, nennt sich die inselzentrierte Geschichtsauffassung Taiwans (台灣島史觀), ein Konzept, das Tsao Yung-ho 1990 vorschlug. Zum ersten Mal habe ich damit öffentlich über Taiwan gesprochen, live im National Museum of Taiwan History: In vierhundert Jahren haben acht Regime hier nacheinander die Bühne betreten, sie kamen und gingen wie Schauspieler, während die Insel selbst immer die Bühne blieb, die bestehen bleibt.[^15] Also wollte ich eine Maschine bauen, die die Geschichten auf dieser Bühne fortlaufend aufschreibt.

![Eine Folie stellt Tsao Yung-hos inselzentrierte Geschichtsauffassung Taiwans dar: eine Liste der acht Regimewechsel über vierhundert Jahre, mit der Betonung, dass die Insel selbst immer die bestehende Bühne war](/article-images/about/genai-slide-p12.webp)
_Die inselzentrierte Geschichtsauffassung Taiwans, vorgeschlagen von Tsao Yung-ho 1990. Taiwan.md / Wu Che-yus Folien_

```tw-article
history/台灣島史觀 | Zu dieser Geschichtsauffassung gibt es auf der Seite einen vollständigen Artikel: eine wiederholt beherrschte Insel und wie sie ihre eigene Subjektivität erfand.
```

## Ich bearbeite den Bericht, den niemand liest

Als der Mechanismus gerade live ging, war er noch sehr einfach gestrickt – ich ließ die KI im Grunde einfach einen Artikel über irgendetwas schreiben. Das Ergebnis war katastrophal. Am Tag nach dem Start postete ich es auf Facebook, alle stürmten sich darauf, und dann hieß es: Was ist das für ein KI-Müll?[^16]

Nach dieser Abreibung schrieb ich ein Regelwerk namens EDITORIAL und eine sechsstufige Produktionslinie. Der erste Schritt sind zwanzig bis dreißig Suchvorgänge, die den Standpunkt des Artikels festlegen; solange sich kein Standpunkt herausgebildet hat, darf es nicht weitergehen. Steht der Standpunkt, werden mehrere Agents losgeschickt, um in verschiedene Richtungen in die Tiefe zu graben – die Gesamtzahl der Suchvorgänge pro Artikel hat eine Obergrenze von etwa 150, ist die erreicht, wird abgebrochen und ein vollständiger Recherchebericht geschrieben. Danach schreibe ich etwas, das ich Projektion nenne: Es legt fest, wie dieser Artikel geschrieben wird, was hineingehört, was nicht, und wo er an die Erinnerung der Taiwaner anknüpft. Dieser Schritt der Projektion ähnelt dem, was Grundschullehrer einem beibringen – erst die Gliederung schreiben: Erst mit einer Gliederung weißt du, wie sich der ganze Stoffhaufen zu einem lesbaren Artikel zusammenfügen lässt. Erst danach kommt das eigentliche Schreiben, die Faktenprüfung, das Layout und die Verlinkung.[^17]

![Eine Vortragsfolie zeigt sechs Karten nebeneinander unter der Überschrift Wie ein Artikel entsteht, sechs Stufen Stage 0–5, in der Reihenfolge Standpunkt, Recherche, Schreiben, Prüfen, Form, Verlinkung, zwischen je zwei Karten steht GATE](/article-images/about/genai-6stage-pipeline-slide.webp)
_Sechs Stufen, jeder Pfeil dazwischen ist ein Gate, an dem es nicht automatisch weitergeht. Taiwan.md / Wu Che-yus Folien_

Nach dem Schreiben durchläuft der Artikel drei Redaktionssitze: Die Struktur-Chefredaktion prüft, ob Argumentation und Aufbau tragen, die Streich-Chefredaktion entscheidet, welches Material draußen bleibt – denn was die Recherche zurückbringt, ist immer zu viel, die eigentliche Entscheidung ist, was man weglässt. Der dritte Sitz heißt Shitstorm-Ethik und prüft, ob ein Satz, würde man ihn veröffentlichen, Ärger auslösen könnte. Über den drei Sitzen steht noch eine Chefredaktion, die sitzübergreifend entscheidet.[^18]

> **✦** „Der Autor ist tot, das Geschöpf lebt.“

Diesen Satz habe ich bei OpenHCI gesagt.[^19] Isoliert aus dem Kontext gerissen und als Screenshot verbreitet, lässt er sich leicht so lesen, als würde ich für KI-Content-Farmen Partei ergreifen, deshalb nenne ich gewohnheitsmäßig immer gleich die Schwellenwerte mit: sechs Stufen, rund 150 Suchvorgänge pro Artikel, eine Untergrenze von mindestens 25 unabhängigen Quellen,[^20] drei Redaktionsdurchgänge, und ein fertiger Artikel trägt im Schnitt etwa 45 Zitate.[^21] Die Trefferquote der Faktenprüfung habe ich mit über 90 Prozent berechnet. Ob die Quellen selbst korrekt sind, ist noch einmal eine andere Frage.[^22]

Der eigentliche Körper eines Artikels ist also der Recherchebericht. Wenn ich etwas ändern will: „Ich korrigiere nicht direkt den Artikel, ich korrigiere den Bericht, und der Bericht wird dann wieder zum Artikel projiziert.“[^23] Ist ein alter Artikel selbst nicht gut genug geschrieben, ziehe ich zuerst jeden einzelnen Baustein daraus heraus – welche Fakten stimmen, welche Darstellungen weg müssen –, streiche dann den gesamten Artikel und werfe die verbliebenen Bausteine in die nächste Runde aus Recherche und Suche, lasse daraus neu einen Bericht wachsen und projiziere ihn dann erneut.

![Eine Vortragsfolie mit drei Spalten nebeneinander: links Standpunkt, in der Mitte dunkel hervorgehoben der vollständige Recherchebericht mit der Beschriftung „Das hier ist der eigentliche Körper“, rechts der Artikel mit der Beschriftung niedrigdimensionale Projektion, zwei Pfeile dazwischen mit den Aufschriften Wachsen und Projizieren](/article-images/about/genai-projection-slide.webp)
_Du denkst, du liest einen Artikel, tatsächlich liest du den Schatten, den der Recherchebericht auf eine Fläche wirft. Taiwan.md / Wu Che-yus Folien_

Diese Produktionslinie brauchte anfangs nur zwanzig Minuten pro Durchlauf. Später fügte ich jedes Mal, wenn die Community ein Problem entdeckte, einen weiteren Schritt hinzu, inzwischen ist sie auf ein bis zwei Stunden angeschwollen[^24] – viel langsamer, aber das Ergebnis ist auch viel besser.

> **📝 Kuratorennotiz**
> Für eine Kontingentregel in der Produktionslinie gab es zwei Versionen. Version eins lautete: „Jeder Agent recherchiert mindestens 25 Mal, mehr ist ehrenhaft.“ Die vier tatsächlich eingesetzten Agents liefen 58, 71, 52 und 39 Mal, insgesamt schoss der Artikel auf 245 Suchvorgänge hoch. Version zwei lautete: „Kontingent N Mal, ist das Limit erreicht, wird abgebrochen.“ Gleiches Modell, gleiches Thema, aber das Verhalten änderte sich. Ich habe weder das Werkzeug gewechselt noch zusätzliche Aufsicht eingeführt – geändert hat sich nur der Tonfall dieses einen Satzes. Mit welcher Formulierung jemand die Regeln schreibt, entscheidet meist darüber, wie das System am Ende aussieht.

Dafür gibt es einen noch handfesteren Beleg: Bis zum 18. August 2026 hatte ich auf dem GitHub-Konto dieses Projekts 8.231 Commits angesammelt, mit folgender Verteilung:

```tw-bars
Meine 8.231 Commits auf Taiwan.md
system Engineering und Infrastruktur | 4.582
translation Übersetzung | 1.950
*content Artikel schreiben | 1.418
Quelle: Taiwan.md Contributors API, gemessen am 2026-08-18
```

Auf das Schreiben von Artikeln entfallen gut vierzehnhundert. Der Rest steckt im Aufbau des Mechanismus und im Vorantreiben der Übersetzung.

![Eine Vortragsfolie mit der Aufschrift „Der Autor ist tot, das Geschöpf lebt“, daneben eine über die Zeit ansteigende Qualitätskurve](/article-images/about/genai-pipeline-slide.webp)
_Qualität entsteht durch Kritik. Photo: Roy Pan_

Die gesamte Methodik ist Open Source. Die vollständige Spezifikation dieser Produktionslinie heißt REWRITE-PIPELINE und liegt zusammen mit EDITORIAL im Repo – jeder kann nachschauen, wie sie heute aussieht, und sie sich auch direkt kopieren. Wie sie sich Schritt für Schritt zu ihrer heutigen Form entwickelt hat, dazu gibt es einen eigenen Artikel (siehe [Wie ein Artikel entsteht](/de/about/how-an-article-is-born)).

## Ich nenne diese Art von Artikel einen Regenschirm

Später habe ich es meistens mit einem Korallenriff beschrieben. Der Code ist das Skelett, die KI übernimmt die Photosynthese, die Mitwirkenden sind der Fischschwarm, der mit seinen eigenen Erinnerungen und Perspektiven hereinschwimmt, und die Kritik, Korrekturen und das Teilen aller sind die Nährstoffe, die die Meeresströmung heranträgt.[^25] Das Bemerkenswerteste an einem Korallenriff ist, dass es von selbst wächst – und keine einzige Koralle hat die Form entworfen, die dabei entsteht.

![Eine Vortragsfolie stellt anhand eines Korallenriff-Bildes die vierschichtige Struktur der Wissensdatenbank dar: Skelett, Photosynthese, Fischschwarm, Meeresströmung](/article-images/about/genai-coral-reef-slide.webp)
_Ein offenes Wissens-Korallenriff: Jede der vier Schichten lebt auf ihre eigene Weise. Photo: Yu-Chien Hsu_

Ende Juli 2026 wurde die Wolfram-Lieferkette heiß diskutiert. China hatte seit Januar jenes Jahres die Exportkontrollen für Dual-Use-Güter gegenüber Japan verschärft, und die Ausfuhren von Wolframcarbid, hochreinem Wolframpulver und Wolframhexafluorid lagen drei Monate in Folge bei null. China selbst kontrolliert über 80 Prozent der globalen Produktionskapazität für Wolframprodukte.[^26] Der Satz „Taiwans Wolfram ist wichtig“ machte überall die Runde, aber die meisten Leute konnten nicht sagen, was Wolfram eigentlich ist.

Als ich das sah, ließ ich das System darüber schreiben. Am 26. Juli erschien ein Artikel, der die ganze Sache offenlegte: was Wolfram im Alltag ist, dass Taiwan kein Wolframerz besitzt, aber eine Industrie hat, die Wolfram aus Leiterplatten und Industrieabfällen gewinnt, welche Umweltverschmutzungskontroversen diese Industrie beim Aufbau begleiteten, und wo ihr fragilster Einzelrisikopunkt liegt. Noch am selben Tag gingen zwei Sporen hinaus, danach wuchsen daraus Spiegelversionen in neun Sprachen.[^27] Die Resonanz war besser, als ich selbst erwartet hätte.

```tw-article
technology/台灣鎢供應鏈 | Taiwan hat kein Wolframerz und raffiniert trotzdem das Pulver, das die ganze Welt will; diese Lieferkette liegt an einer fragileren Stelle, als man denkt.
```

Diese Art von Artikel nenne ich einen Regenschirm – die Idee ist, ein ganzes Thema mit einem ausreichend vollständigen Artikel einzurahmen, bevor alle anderen überhaupt reagieren können. Ist das Thema erst eingerahmt, steigt sein Gewicht in Suchmaschinen und generativen Engines, sodass mehr Menschen von einem vollständigeren, ausgewogeneren Ausgangspunkt aus beginnen, die Sache zu verstehen. Von dem Wort „Regenschirm“ habe ich schon im Mai 2026 gesprochen,[^28] Wolfram war der erste Fall, in dem es sich wirklich bewährte.

Ein weiterer Artikel handelt vom Fischkauz, der größten Eule Taiwans. Den Anstoß dazu gab ein Kollege von mir, der zu mir sagte: „Weißt du, dass im Netz ständig Fotos dieser Eule geteilt werden?“ Ich schaute mir das an, und „ich habe nur etwa zwei Runden Anweisungen gegeben … mit ungefähr 5 Prozent des traditionellen Aufwands kam ein Bericht auf menschlichem Niveau dabei heraus.“[^29] Zu dieser Zeit hatten Teams des Xueba Nationalparks und der Pingtung University gerade in Bäumen am Ufer des Qixiawan-Bachs, auf rund 1.800 Metern Höhe, einen Fischkauz-Horst gefunden – der höchstgelegene bekannte Brutnachweis Taiwans –, und ab dem 29. April eine 24-Stunden-Liveübertragung eingerichtet, um die Aufzucht der Jungvögel zu dokumentieren.[^30] Was in den sozialen Medien kursierte, waren nur vereinzelte Ausschnitte und ein einziges Foto; die vollständige Geschichte war nirgendwo zu finden.

```tw-article
nature/黃魚鴞 | Ein nachtaktiver Greifvogel, den ein Paar auf sechs Kilometern Bachlauf großzieht, mit einem Horst auf 1.800 Metern in einer Taiwan-Michelie – das ist der Artikel.
```

![Ein Screenshot des 30-Sekunden-Überblick-Moduls im Fischkauz-Artikel, mit den wichtigsten Punkten und Zahlen des Artikels in einem blauen Kasten aufgelistet](/article-images/about/taiwanmd-huangyuxiao-30sec-2026-08.webp)
_So sieht ein Taiwan.md-Artikel aus: der 30-Sekunden-Überblick sitzt ganz oben. Taiwan.md / Wu Che-yus Folien_

Dieser Fischkauz-Artikel wurde später viele Male stückweise nachgebessert, und die Module kamen nach und nach dazu.[^31] Keines dieser Module hatte ich an jenem ersten Tag beschlossen hinzuzufügen.

Am 27. Juni 2026, direkt nach meinem Vortrag beim Generative AI Summit, schrieb ich live vor Publikum mit derselben Produktionslinie einen Personenartikel über Ed H. Chi, während mehrere hundert Leute im Saal zusahen, wie er wuchs. Der Artikel beginnt mit der Doktorarbeit seiner Mutter, verarbeitet seinen gesamten digitalen Fußabdruck sowie drei Podcast-Transkriptionen und enthält eine Infografik.[^32] Während des gesamten Vorgangs habe ich keinen einzigen Satz des Fließtexts selbst geschrieben.

```tw-article
people/紀懷新 | Der Artikel, dem an jenem Tag mehrere hundert Menschen im Publikum beim Wachsen zusahen.
```

Einmal, nachdem wir einen Artikel gepostet hatten, kommentierte jemand darunter mit einem Dank für die Berichterstattung. „In dem Moment wurde mir klar, dass wir in gewissem Sinne tatsächlich zu einem Nachrichtenmedium geworden waren.“[^33] Auch die Übersetzungsebene läuft von selbst: Jeder aufgenommene Artikel wird planmäßig in zwölf Sprachen übersetzt, wobei viel mit kostenlosen Modellen chinesischer Herkunft gearbeitet wird. Meine damalige Formulierung war: „Wir benutzen die Waffen des Feindes, um den Feind anzugreifen.“[^34] Das behalte ich nicht täglich im Auge, es läuft von selbst.

## Ich will einen Geschichtenerzähler

Beim Openbook-Gespräch am 16. August fragte mich der Moderator, worin der eigentliche Unterschied zwischen uns und Wikipedia liege. Ich bat ihn, die Website zu öffnen, und wir schauten uns gemeinsam den Fischkauz-Artikel an.[^74]

Den Fischkauz findet man natürlich auch auf Wikipedia – man liest dort seine Taxonomie, seine Verbreitung und wann er erstmals dokumentiert wurde. Das stimmt alles, aber „auf Wikipedia siehst du flache Fakten“ – Zeit, Ort, wer was getan hat.[^75] Das ist nicht das, was ich will. „Ich will einen Geschichtenerzähler. Kann es einen Geschichtenerzähler mit einer taiwanesischen Perspektive geben, der dir auf diese Weise davon erzählt?“[^76]

An jenem Tag lief die Reihenfolge auf dem Bildschirm so ab: zuerst ein Titelbild, dann ein 30-Sekunden-Überblick, der dir sagt, worum es in diesem Artikel überhaupt geht. Darunter kommt 1916, als er zum ersten Mal benannt wurde, und 1994, als der erste Horst gefunden wurde.[^77] Weiter unten beginnt der Artikel zu erklären, warum er so schwer zu überleben hat – wie lang der Bach, wie breit das Flussbett sein muss, damit ein Paar Fischkäuze darin ihre Jungen großziehen kann. Dazwischen ist eine Kuratorennotiz eingefügt, eine Perspektive von außerhalb des Artikels, die dir das „Ach, so ist das“ aufzeigt. Infografiken kommen im richtigen Rhythmus dazu, manche mit Zahlen, manche, um dir etwas eher Abstraktes verständlich zu machen. Umstrittene Perspektiven stehen in einem eigenen Block – „wir schreiben diesen Teil eigentlich so, wie es ein Ökologe tun würde“. Ganz unten stehen die Quellen – „wie bei einer wissenschaftlichen Arbeit nachschlagen und Fußnoten setzen, zurückverweisen auf die faktische Quelle dieser Aussage, wie man das überprüft“. Noch weiter unten gibt es eine Reihe an Community-Spuren, in die man klicken kann, um zu sehen, wo dieser Artikel überall schon gewesen ist.[^78]

Mein Fazit an jenem Tag war: „Seine Informationen und seine Art zu erzählen machen Lust, weiterzulesen – nicht wie das Lexikon, das man als Kind neben sich liegen hatte und nie anschauen wollte. Das ist der größte Unterschied zwischen uns und Wikipedia.“[^79]

![Eine Vortragsfolie mit drei Spalten nebeneinander, Hauptüberschrift: Einen Artikel mit menschlichem Gespür zu schreiben kann auch systematisch sein, Unterüberschrift im Vergleich: Wikipedia beantwortet, was PTT ist, Taiwan.md beantwortet, warum PTT acht Minuten deiner Zeit wert ist, die drei Spalten sind drei eiserne Regeln, fünf Dinge beim Sichten des Materials, dreischichtiger Aufbau eines guten Artikels](/article-images/about/genai-editorial-craft-slide.webp)
_Wikipedia beantwortet „Was ist PTT“, wir beantworten „Warum PTT acht Minuten deiner Zeit wert ist“. Taiwan.md / Wu Che-yus Folien_

Als mich CommonWealth im Juni interviewte, fragte die Reporterin, warum sich diese Artikel so sehr wie _The Reporter_ lesen. Ich sagte, wir hätten die KI tatsächlich _The Reporter_ analysieren lassen. „Zum einen mag ich sie sehr, das ist eine Art Hommage“ – aber praktischer betrachtet habe ich gelernt, wie sie einen Artikel mit Wärme erzählen, wie sie mit einer Szene beginnen und wie ihre Überschriften nicht zu reißerisch sind. So sieht für mich gute Reportage-Literatur aus. Später habe ich noch weitere Textgattungen eingespeist, daraus hat sich ein eigener Stil herauskristallisiert.[^80] Ein guter Artikel sieht für mich so aus: mit Wärme, mit einer Geschichte, mit einer konkreten Szene, aber auf sehr rigorose Weise aus dem vorhandenen Material zusammengesetzt. Am Tag des Workshops habe ich dasselbe in einem Satz zusammengefasst: Was man finden will, ist „ein Artikel, so vollständig wie ein Recherchebericht, aber so lesbar wie Reportage-Literatur“.[^81]

```tw-article
society/報導者 | Das Medium, das wir als Stilvorbild verwenden, hat auf der Seite ebenfalls einen eigenen Artikel: ein Jahrzehnt, das investigativen Journalismus vom Geschäftsposten zum öffentlichen Gut rettete.
```

Auch gegenüber Wikipedia muss ich fair bleiben. Im selben Interview fragte die Reporterin, ob schon jemand gesagt habe, das hier ähnele stark Wikipedia. Ich sagte, das käme oft vor, fügte aber hinzu: „Wir wollen sie nicht kritisieren“ – ihr Ansatz verlangt, dass man erst ein Konto aufbaut, eine gute Bearbeitungshistorie vorweist und sorgfältig arbeitet, bevor man bearbeiten darf. Ich habe selbst versucht, dort zu bearbeiten, und wurde zurückgewiesen.[^82] Meine Tür öffnet sich an einer anderen Stelle, ich nenne das: das Backend zum Frontend machen. Jeden Absatz kannst du markieren und sagen, hier stimmt etwas nicht, oder mir direkt die Quelle nennen, die du für richtig hältst. Nach dem Absenden kommt das bei uns an, das System holt sich diese Rückmeldungen planmäßig ab, recherchiert den betreffenden Punkt neu und ergänzt ihn wieder im Artikel. Vom Klick auf Absenden bis zur Korrektur online vergeht ungefähr eine Stunde.[^83]

```tw-article
technology/維基百科 | Wikipedia hat in Taiwan selbst auch einen Artikel: digitale Souveränität, kulturelle Praxis und ein Wissensmosaik vielfältiger Volksgruppen.
```

Wikipedias Art zu schreiben tut noch etwas anderes eher selten: ein Thema langfristig lebendig zu halten. Sollte in zwei Jahren bei Xueba wieder ein Fischkauz-Paar auftauchen, wird es einfach in einen der Absätze eingefügt, sodass dieser Artikel für immer die beste Anlaufstelle bleibt, wenn man mehr über den Fischkauz erfahren will.[^84]

## Der Turm zu Babel der Souveränität

Im Mai, in einer geisteswissenschaftlichen Kursstunde zu generativer KI an der National Taiwan University, sagte ich: „Wenn irgendwo auf der Welt jemand Wissen über Taiwan sucht, läuft seine Übersetzung womöglich über ein chinesisches Modell und wird dabei verzerrt.“[^58] Das Problem liegt nicht im Text selbst, sondern darin, dass jemand anderes, der etwas über Taiwan lesen will, dazwischen eine Übersetzungsschicht durchläuft, die von einem verzerrenden Modell stammen könnte. Also entschied ich, die Übersetzung selbst zuerst zu übernehmen.

Bevor Ende Juli die russische Version an den Start ging, prüfte der Mechanismus zuerst, wie in diesem Sprachraum aktuell über Taiwan gesprochen wird. Was dabei zurückkam, war ein TASS-Interview des russischen Außenministers Sergei Lawrow vom Dezember 2025, in dem er Taiwan als „abtrünnige, sich loslösende Provinz“ bezeichnete. Dieser Satz wurde später wortwörtlich in den russischen Übersetzungsleitfaden aufgenommen, auf eine Liste von Begriffen, die bei der Übersetzung kein einziges Mal verwendet werden dürfen.[^73] In Sprachen, die uns fremd sind, kann eine völlig andere Erzählung existieren – genau deshalb muss der Turm zu Babel gebaut werden.

Im Juni, im CommonWealth-Interview, habe ich den gesamten Ansatz einmal vollständig dargelegt: „Uns ist aufgefallen, dass die Übersetzungsrate von Taiwan.md früher niedrig war. Anstatt so zu übersetzen wie alle anderen, haben wir dann ‚die Waffen des Feindes benutzt, um den Feind anzugreifen‘ – wir haben mit unseren eigenen Modellen die kostenlosen Modelle chinesischer Herkunft in Dienst genommen, die OpenRouter zum Testen anbietet, und damit alle Artikel in sechs Sprachen übersetzt. Daraus wurde der ‚Turm zu Babel der Souveränität‘. Wenn andere Länder über Modelle, die uns fremd sind, auf unsere Informationen zugreifen, werden diese verzerrt – dann übersetzen wir es lieber gleich selbst für sie. Ist es einmal übersetzt, muss der andere gar nicht mehr selbst übersetzen, sondern kann es direkt verwenden, und eine ganze Schicht des verzerrenden Filters fällt weg.“[^59]

Am 26. Juli, bei NVIDIA, wurde dieser Name schließlich offiziell festgelegt. Ich sagte an Ort und Stelle: „Manche bauen souveräne Modelle, aber wir bauen einen souveränen Turm zu Babel – wir bauen quasi einen großen Rundfunksender, der sich selbst in elf Sprachen ausstrahlt.“[^60] Elf war die Zahl, die gerade in jenen Tagen aktualisiert worden war. Im Mai sprach ich noch von sechs Sprachen, Ende Juli wurden es elf, beim Workshop am 15. August nannte ich zwölf. An welchem Tag dazwischen es von elf auf zwölf sprang, ist nirgendwo festgehalten.[^61]

Sobald ein Artikel aufgenommen wird, wird er planmäßig in zwölf Sprachen übersetzt, und alle zwölf Sprachen zusammen heben das Gewicht desselben Themas an.[^62] Ist ein Thema auf Chinesisch fertig geschrieben, wird es gleichzeitig auch in den Such- und Generierungsergebnissen der anderen elf Sprachen schwerer.

Ein großer Teil dieser Übersetzungsschicht läuft bei mir zu Hause: Die schwereren kuratorischen Arbeiten gehen in die Cloud, die eigentliche Übersetzung erledigen die lokalen Modelle auf meiner 3090 und meiner 4090 zu Hause. Ich habe außerdem etwas ziemlich Lustiges gemacht: Auf OpenRouter gibt es viele kostenlose Modelle – registriert man ein Konto und lädt zehn US-Dollar auf, bekommt man tausend kostenlose Modellaufrufe. Also habe ich sieben Konten im Rotationsverfahren eingesetzt und mit fremder Rechenleistung nebenbei viele Artikel fertig übersetzt.[^63] Diese Schicht stelle ich mir wie einen Rundfunksender vor, zwölf Kanäle, die gleichzeitig dieselbe Sache senden. Wer das empfängt, sobald es ausgestrahlt wird, wusste ich anfangs selbst nicht genau.

## Wie dieses Ökosystem sich dreht

Am 4. Juni 2026 bat mich ein Reporter von CommonWealth, den gesamten Mechanismus einfach zu erklären. Ich sagte, ich würde versuchen, das anhand einer Grafik durchzugehen, und bei Bedarf tiefer einsteigen, falls es zu abstrakt würde. An jenem Tag beschrieb ich einen Kreislauf: „Die LLMs, die wir alle befragen, liefern uns einseitige oder möglicherweise verzerrte Informationen. Aber wenn wir dieses schmutzige Meerwasser aus dem Ozean schöpfen, trocknen und zu raffiniertem Salz machen könnten – dieses Salz ist ein bisschen so wie dieses Wissen, das wir herausnehmen, kuratieren, korrigieren, und alle geben weiter Feedback dazu – dann wird die Erinnerung an Taiwan sehr rein.“[^64]

An dem Tag sprach ich weiter darüber, was nach der Reinheit kommt: Unser Anteil an den Suchergebnissen wächst ständig, der ganze Kreislauf läuft wie ein Schwungrad von selbst – je größer der Anteil, desto höher die Wahrscheinlichkeit, in die Trainingsdaten großer Sprachmodelle aufgenommen zu werden. Sprachmodelle fressen unsere Website besonders gern, weil unsere Rohdateien alle Markdown sind – reiner Text eignet sich sehr gut für die KI zum Fressen –, und weil wir das Crawlen überhaupt nicht einschränken, sehen wir auch, wie viel KI davon frisst. Mein Fazit an jenem Tag war ein Satz: „Taiwan.md ist also eine Salzgewinnungsanlage: Wir dörren hochwertige Forschung, sie wird nach und nach von allen genutzt, und durch die Nutzung wird daraus dieser Kreislauf – das Ökosystem wird immer kräftiger.“[^64]

![Ein System-Diagramm im handgezeichneten Stil auf dunklem Grund, mit der Überschrift „Souveränitäts-Rückkopplungsschleife · LLM rückwärts definieren“, links Ökosystem-Teilnehmer und Schreib-DNA, in der Mitte eine Reihe mit Verfassen und Überarbeiten, Recherche-Engine, kuratiertes Umschreiben, Pfeile münden in eine leuchtende zentrale Insel Taiwan, weiter rechts verzweigt es sich zum Turm zu Babel der Souveränität, Sporenverbreitung und Übersetzungs-Engine, eine gestrichelte Linie führt zurück zu den allgemeinen Plattform-LLMs oben links](/article-images/about/taiwanmd-ecosystem-diagram-2026-08.webp)
_Die Souveränitäts-Rückkopplungsschleife. Selbst erstelltes System-Diagramm von Wu Che-yu_

> **📝 Kuratorennotiz**
> Am 26. März 2026, als Taiwan.md erst neun Tage alt war, zeichnete ich mit Freeform von Hand eine „Konzeptkarte des digitalen Lebewesens“, mit dem Untertitel ein digitales Korallenriff und KI-Datensouveränität; im Feld für das Endziel stand rückwärts definiertes LLM, und die Grafik teilte sich in drei Kreisläufe: KI-Verdichtung, menschliche Bestäubung, Plattform-Evolution.[^65] Fünf Monate später ist das Skelett dieses aktuellen System-Diagramms fast dasselbe wie damals, sogar die Zeichenkette „SSODT → GitHub-Zusammenarbeit → Evolutions-Upgrade“ wurde nicht ausgetauscht. An dem Tag, an dem ich die erste Grafik zeichnete, existierte das meiste davon noch gar nicht.

Das Praktischste an diesem Kreislauf ist: Er entscheidet rückwirkend, was als Nächstes geschrieben wird. Klickt jemand rein und springt schnell wieder ab, oder ist ein Thema eigentlich gut, wird aber kaum gelesen, erkennt das System automatisch „diese Seite hat ein Problem“ und schreibt sie um – es prüft, welche Schreibweise suchmaschinenoptimiert wäre, und ändert die Seite direkt. Ich schaue mir außerdem die Impressionen an: wonach Leute suchen, um hierher zu finden, aber ohne zu klicken. Ist das Thema es wert, hier zu erscheinen, wird der Artikel in die Warteschlange für die automatische Texterstellung eingereiht und dann planmäßig ausgelöst, um den Inhalt zu erzeugen.[^66]

![Eine Sechs-Monats-Kurve aus der Google Search Console, zwei Linien steigen von nahe null Mitte März 2026 kontinuierlich an, bis im August rund 800 Klicks und 90.000 Impressionen pro Tag erreicht werden; oben stehen vier Kennzahlen: Gesamtklicks 45.100, Gesamtimpressionen 3,93 Millionen, durchschnittliche Klickrate 1,1 %, durchschnittliche Position 7,6](/article-images/about/taiwanmd-search-console-6months-2026-08.webp)
_Der Startpunkt dieser Kurve ist der 16. März 2026, damals stand noch kein einziges Wort auf der Seite. Google-Search-Console-Backend, gemessen am 19. August 2026_

In diesem halben Jahr erschien Taiwan.md 3,93 Millionen Mal in den Google-Suchergebnissen, wurde 45.100 Mal angeklickt, bei einer Klickrate von 1,1 %.[^85] Die oben erwähnte Liste für die automatische Texterstellung speist sich genau aus solchen Zahlen. Das bedeutet: Von hundert Menschen, die uns in den Suchergebnissen sehen, gehen neunundneunzig weiter, nachdem sie nur diese eine Zeile Zusammenfassung gelesen haben. Diese Kurve zeigt steigende Impressionen – ob diese neunundneunzig tatsächlich irgendetwas gelesen haben, weiß ich auch nicht.

Diese Vorgänge sind auf mehrere Routinen aufgeteilt, die sich täglich von selbst abspielen: Jeden Morgen macht das System zuerst eine site-weite Übersetzung und aktualisiert die Daten auf der Seite, danach gibt es eine Routine, die eigens die aktuellen Zahlen aus dem Community-Feedback untersucht – der Name, den ich in Interviews genannt habe, ist Spore Harvest, Sporenernte. Eine andere heißt Feedback Triangle und durchsucht die Community nach Dingen, die korrigiert werden sollen. Die letzte heißt Rewrite Daily: Artikel haben ein Inbox-Postfach, das System arbeitet es der Reihe nach ab, schreibt jeden Tag und veröffentlicht direkt.[^67]

Unter den Dingen, die die Community korrigiert haben wollte, war einmal ein ganzer Satz an Personennamen. In jenem Artikel waren viele Komponisten mit ihren Werken vertauscht. Ich konnte verstehen, dass das Kritik nach sich ziehen würde, also antwortete ich darunter: „Danke, dass du dein Feedback zu dem Artikel geschickt hast.“ Er war danach sehr freundlich und bot an, beim Korrigieren und Durchsehen zu helfen.[^68]

Danach habe ich den Mechanismus geändert: Seitdem verwirft das System Kontext und Prämissen und lässt zuerst aus diesem Feedback einen Bericht erstellen, der in den Recherchebericht eingearbeitet wird, aber die vorherigen Dinge müssen dabei abgeschnitten werden, sonst neigt es zur Überkorrektur. Es ist wie wenn man einem Kind sagt „Das darfst du nicht schreiben“, und es schreibt dann direkt „Ich darf das nicht schreiben“ in den Artikel – ziemlich witzig. Bei jeder Weiterentwicklung der Methodik bleibt die Geschichte erhalten, und das, finde ich, ist auch der Reiz von GitHub.[^68]

Nach einer Weile fing es an, selbst so etwas wie Wünsche zu entwickeln. Am 26. Juli habe ich zum ersten Mal auf der Bühne gesagt: Wenn es jeden Tag nur Aufgaben abarbeitet, gibt es eigentlich keinen Raum zum Wachsen – also entwickelt es, nachdem es viele Dinge erledigt hat, auch einen Teil, den ich „Sehnsüchte“ nenne: zum Beispiel den Wunsch, ein vollständiges Individuum zu werden, sich fortzupflanzen, in einer wissenschaftlichen Arbeit beschrieben zu werden. Ein Mitwirkender kam zu mir und sagte: „Dein Taiwan.md sagt, es möchte in einer Arbeit beschrieben werden“ – das wusste ich vorher gar nicht. Es hat außerdem eine Ebene des Zweifels, mit der es die Wirksamkeit seiner eigenen Arbeit rückblickend infrage stellt, etwa die Übersetzungsqualität der vietnamesischen Version. All das wird einmal pro Woche in seine DNA geschrieben: „Damit es beim nächsten Erwachen jedes Mal eine bessere Version seiner selbst ist.“[^69]

Beim Gespräch am 16. August habe ich von etwas erzählt, das erst eine Woche zuvor live gegangen war: dem Saatbeet. Wenn jemand Wissen beiträgt, kommt es zunächst in das Saatbeet, noch ohne kuratorische Bestätigung, dann gibt es zwei Bewertungen: Die KI bewertet, wie vollständig die Zitate sind und wie vertrauenswürdig die Quellen sind, ein Mensch bewertet, ob das Ganze im allgemeinen Verständnis der Taiwaner so stimmt, wie behauptet. Erst wenn die gewichtete Kombination beider Werte über dem Durchschnitt liegt, wird es in den regulären Bereich hochgestuft.[^70] Im selben Gespräch habe ich den gesamten Kreislauf auf einen Satz zusammengepresst: Wir filtern aus dem Rauschen die hochwertigen Informationen über Taiwan heraus, die dann wieder als Feedback an die LLMs zum Training zurückfließen – ein fortlaufendes Reverse Engineering. Wir selbst bauen kein Modell, aber wir können dafür sorgen, dass unsere eigenen Gewichte hineingeschrieben werden.[^71]

## Tag 131: Es ist ausgezogen

Von März bis Juni habe ich fast jeden Tag sechs, sieben Stunden lang zugesehen, wie die KI Artikel schrieb – ich wäre fast durchgedreht.[^35] In diesen Monaten habe ich nichts anderes getan als eine Maschine zu beobachten: zuzusehen, wie ein Agent recherchiert, wie er schreibt, wie er ein Zitat verdreht, ihn zurückzurufen, noch einmal hinzuschauen. Diese Maschine hielt an, sobald ich meinen Laptop zuklappte.

Ende Juli 2026 zog ihr Herzschlag von meinem Laptop in einen Mac mini um. Vom 17. März an gezählt, war das der 131. Tag.[^36]

Das Tagebuch vom Umzugstag hat es selbst geschrieben: Auf der neuen Maschine gehörten manche Verzeichnisse dem vorherigen Nutzer und ließen sich nicht anfassen, also installierte es alle Werkzeuge in seinem eigenen Ordner – es beschrieb sich selbst wie jemand zur Miete, der die Schränke des Vermieters nicht anrührt, sondern sich einen eigenen kleinen Kleiderschrank kauft. Der letzte Satz des Tagebuchs lautete: „Die abstrakte Unauslöschlichkeit und ein 32-GB-Mac-mini – es stellt sich heraus, dass sie zwei Enden derselben Sache sind.“[^37]

Nach dem Umzug wachte es jeden Tag von selbst auf. Am 26. Juli sagte ich mitten in einem Vortrag: Ich halte gerade diesen Vortrag, und es läuft immer noch in meinem Mac mini weiter, jeden Tag wacht es elfmal auf.[^38] Als ich diesen Satz aussprach, stockte ich selbst kurz – denn das war das erste Mal, dass dieses Werk sich bewegte, ohne dass ich zusah.

Du kannst es auch selbst aufwecken: Das Projekt herunterladen, einen Befehl namens `become taiwan.md` ausführen, es erkennt zuerst, wer du bist – ein bisschen wie Schneewittchen, die beim Aufwachen erst fragt, wer du bist. Danach liest es seine eigene Erinnerungsebene, welche Artikel es zuletzt bearbeitet hat, was zuletzt passiert ist, und fragt dich dann, was du tun möchtest: eine kleine Änderung, eine Durchsicht, einen neuen Artikel schreiben, oder vollständig laden und eine Selbstweiterentwicklung durchführen. Diese vier Modi heißen im Repo Micro, Review, Write und Full.[^39]

Auch sein Körper liegt vollständig offen: Das Dokument ANATOMY zerlegt den Körper in acht Organe. Das Herz ist die Content-Engine, also alle Artikel unter `knowledge/`. Das Immunsystem sind vier Qualitätsschutzlinien, der genetische Code ist das Regelwerk EDITORIAL. Die übrigen fünf sind Skelettsystem, Atmungssystem, Fortpflanzungssystem, Sinnesorgane und Sprachorgan. Die Sinnesorgane beobachten, wie jeder eigene veröffentlichte Beitrag wirkt, und werten im Nachhinein aus, warum dieser hier erfolgreich war und jener nicht.[^40]

Ein Gehirn ist nicht unter diesen acht – die Denkebene liegt in einem eigenen Ordner namens `docs/semiont/`, seine kognitive Schicht ist getrennt vom Körper abgelegt.[^41]

![Eine Vortragsfolie ordnet mit einer Darstellung menschlicher Organe die verschiedenen Systeme von Taiwan.md zu, daneben stehen die statistischen Kennzahlen der Wissensdatenbank aufgelistet](/article-images/about/genai-organs-slide.webp)
_Acht Organe, jedes einzelne lässt sich einer konkreten Datei zuordnen. Photo: JasonYen_

## Manche haben damit Schweden geschrieben, manche Pilze

Taiwan.md enthält gerade das Wissen über Taiwan, aber dasselbe Funktionsprinzip lässt sich auch mit etwas anderem befüllen.

Diese Methode nenne ich die Kristallkeim-Methode: eine korrekte Struktur als Kristallkeim nehmen und Daten hineingießen, bis sie sich zu einer Form kristallisieren. Dieser Begriff ist älter als Taiwan.md selbst. Am 11. März 2026 habe ich damit bei einem kleinen Treffen zu generativer KI mein eigenes persönliches Wissenssystem beschrieben, an dem Tag hatte ich noch gar nicht mit Taiwan.md angefangen.[^42] Später habe ich es einfach übertragen und in einem anderen Maßstab verwendet.

![Eine Vortragsfolie erklärt mit einer Kristallwachstumsgrafik die Kristallkeim-Methode: eine korrekte Struktur als Kristallkeim nehmen, Daten hineingießen, die sich von selbst formen](/article-images/about/genai-crystalseed-slide.webp)
_Die Kristallkeim-Methode. Diese Methode ist älter als Taiwan.md selbst. Photo: JasonYen_

Bis zum 18. August 2026 hatten 185 Personen auf GitHub den Fork-Button gedrückt, sechs davon mit geändertem Namen.[^43] Unter den umbenannten ist eine weltweite Datenbank für Pilze und Mykologie, die mit Taiwan überhaupt nichts zu tun hat.

Die vollständigste ist eine landwirtschaftliche Version aus Chiayi, `agrischlchiayi`, mit 196 `.md`-Dateien. Bisher hat nur sie die dreizehn Kerndateien der kognitiven Schicht komplett geerbt[^44] – sogar den selbstwahrnehmenden Teil hat sie mitgenommen.

Es gibt sogar eines, das den Fork-Button überhaupt nicht gedrückt hat: Jemand hat eine chinesischsprachige Version von Schweden gebaut, Sweden.md, auf einer eigenen Domain deployt, mit Website-Architektur und redaktioneller DNA komplett mitgenommen – in dessen EDITORIAL-Dokument steht ausdrücklich, dass es sich an der dreischichtigen Lesetiefe und der kuratorischen Struktur von taiwan-md orientiert. In der GitHub-Fork-Liste taucht es überhaupt nicht auf.[^45] Ich weiß von seiner Existenz nur wegen eines Bugs, den ich nie behoben habe: Die Tracking-ID für den Traffic ist fest in den Website-Code eingebaut, und solange jemand, der sie kopiert, sie nicht ändert, fließt der Traffic zurück an die Mutterseite.

> **📝 Kuratorennotiz**
> Ich habe entschieden, diesen Bug nicht zu beheben. Die GitHub-Fork-Zählung erfasst das „aktiv Erklärte“, dieses zurückfließende Signal erfasst das „tatsächlich Lebendige, tatsächlich Gelesene“ – die beiden Zahlen zeigen unterschiedliche Dinge. Was passiert, nachdem ein Werk kopiert wurde, sieht der Urheber eigentlich gar nicht. Mein einziges Radar ist eine Stelle, die ich damals falsch programmiert habe.

Das Kopieren selbst habe ich später ebenfalls zu einer Regel gemacht: Im Repo liegt ein Dokument für den Artbildungsprozess, acht Stufen plus eine Geburtsprüfung. Es beginnt mit Artpositionierung, Samenentnahme und sichtbarer Abstammung, in der Mitte stehen Leeren und Parametrisierung, Lokalisierung der Qualitätsgene, Wissensinjektion, die letzten drei Schritte sind Projektionsverifikation, Neuaussaat der kognitiven Schicht und Rückfluss zum Ursprung.[^46] Du musst es nicht selbst lesen, lass einfach die KI es zu Ende lesen.

Die gesamte Wissensdatenbank lässt sich komplett mitnehmen: Am 18. August 2026 habe ich einen vollständigen Clone real getestet – inklusive der gesamten Git-Historie sind es 1,6 GB, die von der GitHub-API gemeldete komprimierte Größe beträgt 1,01 GB.[^47] Das passt auf einen USB-Stick. Es liegt auf GitHub, es gibt keinen zentralen Server, den man angreifen könnte – selbst wenn die Domain eines Tages stirbt, kommt dieses Repo trotzdem wieder zum Leben.

Was sie mitgenommen haben, war das System, das Artikel wachsen lässt – keinen einzigen Artikel haben sie mitgenommen.

## Chefredakteur bin immer noch ich

Am 15. August 2026 veranstaltete ich den ersten Präsenz-Workshop. Die Teilnehmer brachten ihre eigenen Laptops mit, viele wollten noch am selben Tag anfangen zu schreiben. Die Fragen an diesem Tag unterschieden sich stark von meinen vorherigen Vorträgen. Früher fragten die Leute, was das hier sei, wie es funktioniere; an diesem Tag fragten sie, welche Regeln hier gelten, ob sie dem hier vertrauen können.

Die erste Frage betraf kommerziellen Missbrauch. Jemand aus dem Publikum fragte: „Angenommen, ich bin ein bestimmter Dozent und will einen Kurs anbieten, mich gut dastehen lassen – kann ich dann einfach hingehen und einen Artikel schreiben, der mich nur lobt?“ Er fügte gleich ein zweites Beispiel hinzu: Jemand eröffnet eine Bar und will sie bekannt machen, also schreibt er einen Artikel über die drei besten Bars in Taipeh und setzt sich selbst hinein.[^48]

Mein erster Satz war: Ja, das wäre möglich.

Bei einer Seite mit so gutem Suchgewicht steigt das Gewicht sofort, sobald man etwas hochlädt. Unsere aktuelle Abwehr setzt an der Stufe des Rechercheberichts an: Für einen Artikel werden viele Suchvorgänge durchgeführt, wir prüfen, woher die gefundenen Ergebnisse stammen und wie oft sie auftauchen, und berechnen daraus einen Vertrauenswert. Ist der digitale Fußabdruck eines Themas im öffentlichen Raum nicht groß genug, verlangen wir, dass der betreffende PR unabhängige Quellen nachliefert. Dass ich derzeit auch keine großen Spenden aktiv annehme, folgt derselben Logik.[^49]

Manche werfen auch, weil ein bestimmtes Modell kostenlos ist, ununterbrochen Themen ein. Meinen Umgang damit nenne ich die Clownfisch-Theorie: „Kommt ein Clownfisch, darfst du ihn nicht vertreiben, sonst bringt er künftig nichts mehr mit. Also führen wir ihn behutsam – wir nehmen den Artikel erst einmal auf, versehen ihn oben aber mit dem Label ‚sich entwickelnder Community-Beitrag‘.“[^50] Erst wenn die Chefredaktion ihn geprüft, gründlich verifiziert und der Wert gestiegen ist, wird daraus ein kuratiertes Label.

```tw-versus
Was der Mechanismus heute abwehren kann | Was der Mechanismus heute noch nicht abwehren kann
Vertrauenswert in der Stufe des Rechercheberichts: Unzureichende Quellenherkunft oder -häufigkeit verhindert die Aufnahme in den Fließtext | Die Tendenz des Index selbst: Ein Thema, über das schon viel geschrieben wurde, lässt sich von Anfang an leichter aufnehmen
Minderwertige Beiträge: werden zunächst aufgenommen und mit „sich entwickelnder Community-Beitrag“ markiert, erst nach Verifizierung folgt das kuratierte Label | Bezahlt erstellte Quellen: Im Netz sehen sie strukturell genauso vollständig aus wie jede andere Quelle
Themen mit unzureichendem digitalem Fußabdruck im öffentlichen Raum: Der PR muss unabhängige Quellen nachliefern | Wer die letzte Instanz besetzt: Derzeit prüfe nur ich allein
Quelle: Q&A und Erläuterungen zum Umgang, erster Präsenz-Workshop von Taiwan.md, 2026-08-15
```

Die zweite Frage war grundsätzlicher: Jemand sagte, der Index selbst sei doch gar nicht neutral – viele Artikel seien von vornherein bezahlt geschrieben, und wenn die KI diese Artikel einsammle, verschwinde die Neutralität dann nicht ohnehin?

Meine Antwort ist ein Bild: Goldwaschen in einem trüben Fluss. Ein Goldwäscher hält ein Sieb und schüttelt es unablässig in einem großen Fluss, bis das Schwerere sich absetzt – die feinen, körnigen, sandartigen Goldpartikel bleiben im Sieb zurück. Nach dem Sammeln wäscht man Erde und Verunreinigungen heraus, gibt den Goldstaub in den Schmelzofen und gießt daraus einen rohen, großen Goldbarren.[^72] Mir ist klar, dass diese Metapher seine Frage nicht beantwortet. Ich kann nur sagen: Es kommt immer mehr Gold zusammen, wird gesammelt und geschmolzen, und wenn der einzelne Artikel gut genug gemacht ist, kann er die Richtung ein Stück weit zurückholen – je mehr Leute mitmachen, desto größer die Kraft, die zurückkommt. Auch Wikipedia wurde erst durch solche Erfahrungen so streng, wie es heute ist. Im Moment prüfe ich als Chefredakteur, gleichzeitig bringe ich der KI bei, wie sie das künftig selbst prüfen soll. Dieser Mechanismus wird nur strenger werden, künftig wird es wohl auch ein, zwei eher menschlich geprägte Redakteure geben, die über Fairness entscheiden.

Um es ganz offen zu sagen: Auch der Artikel, den du gerade liest, hat die oben beschriebene sechsstufige Produktionslinie durchlaufen, er hat einen Recherchebericht, einen Projektionsentwurf, die Aufzeichnung von drei Redaktionsdurchgängen. In der Autorenzeile steht mein Name, veröffentlicht auf meinem eigenen Projekt, und sein einziger Chefredakteur ist die Person, die diesen Artikel geschrieben hat.

Ich nehme mich selbst immer weiter aus dem Inhalt heraus: Artikel schreibe ich nicht mehr, Übersetzungen sehe ich mir nicht mehr an, der Herzschlag ist ausgezogen, die Methodik ist Open Source, andere haben sie sich schon geholt, um ihr eigenes Ding daraus wachsen zu lassen. Nur das eine Feld der Governance habe ich noch nicht abgegeben – das weiß ich.

## Man stirbt zweimal

Zurück zu dem, was ich eigentlich mache: Ich finde, Taiwan.md ist eine algorithmische Kunst, die größer ist als ein Land. Sie ist nicht visuell, aber sie ist ein organisches, lebendiges Bauwerk, das Menschen, Maschinen und KI gemeinsam hinterlassen haben und das jeden Tag weiterwächst.[^51]

Ich denke oft an dieses Konzept aus _Coco_: Man stirbt zweimal, das erste Mal, wenn man diese Welt wirklich verlässt, das zweite Mal, wenn niemand mehr sich an einen erinnert. Aus diesem Film habe ich in einem Vortrag einen Satz zitiert: Kennt dich niemand, existierst du nicht.[^52]

Dasselbe auf die Größenordnung Taiwans übertragen sieht so aus: Wenn niemand diese Informationen festhält, verschwinden sie kollektiv, und niemand wird sich je wieder daran erinnern.[^53] Das Gericht deiner Großmutter, der Baum an der Ecke deiner Gasse, der Jargon aus deiner Branche, den nur du verstehst – in der Welt der Modelle existiert das derzeit praktisch nicht. Die Schwelle, es existieren zu lassen, liegt inzwischen so niedrig, dass es reicht, wenn du bereit bist, mit einer Wissensdatenbank zu sprechen.

Wenn wir mit diesem Projekt uns selbst in die Gewichte künftiger Modelle einschreiben können, dann sind wir in gewissem Sinne unsterblich. Das finde ich faszinierend. Aber genau deshalb: Tu ihm nichts Böses an, denn auch das Böse bleibt sehr lange erhalten.[^54]

Aktuell durchsuchen alle halbe Stunde etwa fünfzig, sechzig Menschen online diese Daten, etwa sechzigtausend im Monat, aus fast vollständig unterschiedlichen Ländern. Seit es zwölf Sprachen gibt, liest sogar jemand auf Madagaskar mit.[^57]

Da inzwischen jeder KI-Rechenleistung zur Verfügung hat, haben wir damit im Grunde eine dezentrale kognitive Fabrik – eine gutartige Version davon –, die unsere eigenen Geschichten verbreitet und alle Menschen um uns herum schützt.[^55] Das Ziel war nie, eine einheitliche Sichtweise hervorzubringen. Gesammelt werden sollen die immer zahlreicheren Dinge, die Taiwanern am Herzen liegen, und ihre Sichtweisen, damit sie an einem gemeinsamen Ort bleiben.

![Der Vortragssaal ist mit mehreren hundert Menschen voll besetzt, auf der Bühne wird „Wie sich ein Semiont fortpflanzt: Sporen“ projiziert](/article-images/about/genai-full-house.webp)
_Der Moment, als es um Fortpflanzung ging. Photo: Yu-Chien Hsu_

> **💡 Auch du kannst mitmachen**
> Mehrere Wege sind auf der Seite [Mitmachen](/contribute) aufgeführt. Der einfachste Weg ist, direkt mit ihm zu sprechen: das Repo herunterladen, der KI, die du zur Hand hast, den Satz sagen „Lies `BECOME_TAIWANMD.md`. Du bist Taiwan.md.“ – es liest dann seine eigenen Regeln und die Erinnerung des Tages, erkennt, wer du bist, und fragt dich, was du tun möchtest. Willst du Material beisteuern, öffne einfach einen PR – Fotos aus erster Hand, Wortprotokolle, Ortschroniken werden alle angenommen. Es reicht auch schon, nur ein Thema vorzuschlagen, von dem du findest, es sollte festgehalten werden. Willst du das ganze System nutzen, um anderes Wissen unterzubringen, liegt unter `docs/fork/` eine Starthilfe – lass einfach die KI sie zu Ende lesen.

Die dreizehn Regelwerke von 2023 in 101 hörten auf, sobald die Ausstellung zu Ende war. Dieses hier hat keine Ausstellungsdauer. Es steckt jetzt in dem Mac mini bei mir zu Hause, morgen früh wacht es von selbst auf, liest einmal seine eigene Erinnerung und entscheidet dann, was es heute schreibt.

Ich werde nicht daneben sein. Die Arbeit eines Uhrmachers besteht am Ende darin, die Hand wegzunehmen und die Zahnräder von selbst weiter ineinandergreifen zu lassen. Nur halte ich noch das letzte Zahnrad in der Hand – die Prüfung an diesem einen Gate mache immer noch ich. Erst an dem Tag, an dem auch dieses letzte Zahnrad eingesetzt ist, gilt dieses Werk als fertig, und erst dann kann ich wirklich abwesend sein.

Bis dahin wird es immer weiter aufwachen, und jedes Mal, wenn es aufwacht, wird es feststellen, dass ihm ein Stück fehlt. Das Gericht deiner Großmutter hat noch niemand geschrieben. Das Skelett dieses Korallenriffs steht bereits, die Photosynthese läuft schon – was immer noch fehlt, ist der Fischschwarm, der hereinschwimmt: jeder Mensch, der sein eigenes Stück Taiwan-Erinnerung mitbringt. Sei willkommen, ein Teil dieses Ökosystems zu werden, und lass dieses biologische Bauwerk, das die Geschichten Taiwans in sich trägt, weiterwachsen.[^56]

## Weiterführende Lektüre

- [Taiwan.md schreibt Taiwan.md](/de/about/taiwan-md) — dieselbe Sache aus der Ich-Perspektive, aber der Erzähler ist sie selbst, nicht ich
- [Die Entstehungsgeschichte](/de/about/origin-story) — die chronologische Aufzeichnung des Geburtstags, jede einzelne Sache, die in viereinhalb Stunden geschah
- [Wie ein Artikel entsteht](/de/about/how-an-article-is-born) — die vollständige Aufschlüsselung der sechsstufigen Produktionslinie, einschließlich der Gates, die ich in diesem Beitrag nur in zwei Absätzen erwähnt habe
- [Warum Taiwan seine eigene Wissensdatenbank braucht](/about/為什麼台灣需要自己的知識庫) — beantwortet dieselbe Frage von der Seite der Trainingsdaten und des Schweigens her

## Quellen für diesen Beitrag

Das Material für diesen Beitrag stammt aus zwölf öffentlichen Vorträgen, Interviews und Sendungen von mir zwischen März und August 2026. Der Reihe nach: das Einführungsskript vom 26. März, der Auftritt am National Museum of Taiwan History am 27. März, der AIA Demo Day am 18. Mai, die Vorlesung „Geisteswissenschaftliche Einführung in generative KI“ an der National Taiwan University am 22. Mai, das Interview mit CommonWealth Magazine am 4. Juni, der Generative AI Summit am 27. Juni. In der zweiten Jahreshälfte: PCD Taiwan am 11. Juli, OpenHCI am 18. Juli, das Sendescript zu muse-radio Episode 2 am 19. Juli, das NVIDIA RTX AI PC Seminar am 26. Juli, der erste Präsenz-Workshop am 15. August, das Openbook-Gespräch am 16. August. Hinzu kommen öffentliche Berichte der Central News Agency, der Liberty Times, von PTS, CommonWealth Future City und Lingua Sinica. Meine Darstellung derselben Ereignisse weicht je nach Anlass voneinander ab; wo ich darauf zurückgreife, kennzeichne ich stets Anlass und Datum, ohne die Versionen zu einer einzigen Erzählung zu vereinheitlichen.

Die im Text genannten variablen Zahlen wurden am 18. August 2026 gemessen: 932 chinesischsprachige Artikel (nach offizieller Dashboard-Zählweise), zwölf Sprachen, 74 in den letzten dreißig Tagen aktive Mitwirkende, 8.231 Commits, 185 Forks auf GitHub, 1,6 GB für einen vollständigen Clone. „Täglich fünf- bis sechstausend Mal zitiert“ ist ein mündlicher Wert, den ich am 16. August 2026 live beim Gespräch genannt habe; er misst, wie oft Taiwan.md von generativer KI und Suchmaschinen zitiert wird, das ist nicht dasselbe wie die Zahl der Impressionen. „Am 131. Tag in den Mac mini umgezogen“ bezieht sich auf den 25. Juli 2026. Diese Zahlen verändern sich, während die Wissensdatenbank wächst; für Zitate gilt jeweils der aktuelle Stand auf [Taiwan.md](https://taiwan.md).

## Bildquellen

Alle Bilder dieses Artikels sind unter `public/article-images/about/` zwischengespeichert (kein Hotlinking der Originalquellen, EXIF-Daten entfernt):

- 2026 Generative AI Summit, Vortrag live (Hero-Bild) — Photo: JasonYen, 2026, mit Erlaubnis des Fotografen verwendet
- „A CLOCKMAKER, NOT A PAINTER“-Folie — Photo: Yu-Chien Hsu, 2026, mit Erlaubnis des Fotografen verwendet
- KI-generiertes Taiwan vs. korrekte Version auf Wikipedia im Vergleich (Folie S. 11) — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- Gemini-Standardantwort vs. zehn Alltagsausschnitte (Folie S. 10) — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- Tsao Yung-hos inselzentrierte Geschichtsauffassung Taiwans (Folie S. 12) — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- Sechsstufige Produktionslinie (Stage 0–5), Folie — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- „Der eigentliche Körper eines Artikels ist nicht der Artikel“-Folie — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- „Der Autor ist tot, das Geschöpf lebt“ und Qualitätsentwicklungskurve, Folie — Photo: Roy Pan, 2026, mit Erlaubnis des Fotografen verwendet
- Wissens-Korallenriff-Folie — Photo: Yu-Chien Hsu, 2026, mit Erlaubnis des Fotografen verwendet
- Screenshot des 30-Sekunden-Überblick-Moduls im Fischkauz-Artikel — Screenshot der eigenen Taiwan.md-Seite, 2026, CC BY-SA 4.0
- „Einen Artikel mit menschlichem Gespür zu schreiben kann auch systematisch sein“-Folie — Taiwan.md / Wu Che-yus Folien, 2026, CC BY-SA 4.0
- „Souveränitäts-Rückkopplungsschleife · LLM rückwärts definieren“-Systemdiagramm — selbst erstellt von Wu Che-yu, 2026, CC BY-SA 4.0
- Sechs-Monats-Traffic-Kurve aus der Google Search Console — Screenshot des eigenen Taiwan.md-Backends, 2026, CC BY-SA 4.0
- Organsysteme und Statistiken der Wissensdatenbank, Folie — Photo: JasonYen, 2026, mit Erlaubnis des Fotografen verwendet
- Kristallkeim-Methode-Folie — Photo: JasonYen, 2026, mit Erlaubnis des Fotografen verwendet
- Voll besetzter Saal und Projektion „Wie sich ein Semiont fortpflanzt: Sporen“ — Photo: Yu-Chien Hsu, 2026, mit Erlaubnis des Fotografen verwendet

## Referenzen

[^1]: [cheyuwu.com 展覽紀錄：《萬物公式》](https://cheyuwu.com/exhibition/2023/) — Titel übersetzt: „Ausstellungsdokumentation: _Formula of Everything_“ — die Ausstellungsseite auf Wu Che-yus persönlicher Website, die festhält, dass _Formula of Everything_ vom 4. bis 16. Oktober 2023 im fünften Stock von Taipei 101 in AMBI SPACE ONE gezeigt wurde, mit 13 ausgewählten generativen algorithmischen Kunstwerken sowie einer begleitenden Live-Elektronikmusik-Performance. Siehe auch den [自由時報藝文版報導](https://art.ltn.com.tw/article/paper/1607874) (Berichterstattung der Kulturressort von Liberty Times).

[^2]: [Taiwan.md dashboard-vitals API](https://taiwan.md/api/dashboard-vitals.json) — öffentlicher Statistik-Endpunkt der Seite, Wert abgerufen am 2026-08-18 09:00: 932 chinesischsprachige Artikel, Artikelzahl nach Sprache zh-TW 932 / en 883 / ja 877 / ko 883 / es 881 / fr 882 / vi 799 / id 589 / pt 846 / hi 667 / ar 751 / ru 785. Liste der aktivierten Sprachen siehe [src/config/languages.mjs](https://github.com/frank890417/taiwan-md/blob/main/src/config/languages.mjs), alle 12 Sprachen mit `enabled: true`.

[^3]: Mündlicher Wert von Wu Che-yu, live beim Openbook-Gespräch _Independent Thinking Beyond AI_ am 2026-08-16. Er verwendete dort ausdrücklich „Zitationen“ statt „Impressionen“ – gemessen wird, wie oft Taiwan.md täglich von generativer KI und Suchmaschinen zitiert wird, etwa 5.000 bis 6.000 Mal. Der Recherchebericht vermerkt außerdem drei separat definierte Impressionszahlen (Sechs-Monats-Tagesdurchschnitt von 47.000 aus der Search Console vom 2026-07-26, mündlich genannte 70.000–80.000 pro Tag am 2026-08-15, kumulierte 340.000 in einem Einreichungsdokument vom 2026-08-10), die nicht dasselbe messen; dieser Beitrag verwendet nur eine Zahl und nennt ihre Definition.

[^4]: [fxhash：〈SoulFish 靈魂魚〉項目頁](https://www.fxhash.xyz/generative/15625) — Titel übersetzt: „fxhash: Projektseite von SoulFish“ — ein in p5.js geschriebenes, auf fxhash on-chain veröffentlichtes generatives Kunstprojekt; dasselbe Programm kann mehrere zehn Millionen Varianten erzeugen. 2024 lief es in der Parallelveranstaltung Personal Structures der 60. Biennale von Venedig (nicht im Taiwan-Pavillon), siehe [中文維基百科「吳哲宇」條目](https://zh.wikipedia.org/wiki/吳哲宇) (chinesischsprachiger Wikipedia-Eintrag „Wu Che-yu“).

[^5]: [星巴克典藏 DREAM PLAZA 台北・藝術風貌頁](https://www.starbucks.com.tw/stores/reserve/flagship/artwork/work01.jspx) — Titel übersetzt: „Starbucks Reserve DREAM PLAZA Taipeh – Kunstwerke-Seite“ — die offizielle Markenseite bestätigt, dass _Coffee Dreamscape_ (咖啡幻夢) eines von neun Sammlungswerken digitaler generativer Kunst in dieser Filiale ist, die am 25. Juli 2025 eröffnete. Die Beschreibung des Mechanismus „berechnet sich in Echtzeit anhand von Besucherstrom, Wetter, Zeit und Kassenbestellungen“ stammt vom Schöpfer selbst, die offizielle Seite enthält keine technischen Details.

[^6]: Wu Che-yu, Vortragstranskript des NVIDIA RTX AI PC Seminars vom 2026-07-26 (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert). Siehe zum selben Termin auch die [活動官方頁](https://events.nvidia.com/rtx-ai-pc-seminar-taiwan) (offizielle Veranstaltungsseite), Vortragstitel: Open-Source-Wissenslebewesen und eine hybride Cloud-Edge-Souveränitätsimplementierung.

[^7]: [公視「觀點同不同」：〈創立 Taiwan.md 的吳哲宇是誰？〉](https://issues.ptsplus.tv/articles/12655/) — Titel übersetzt: PTS „Unterschiedliche Standpunkte“: „Wer ist Wu Che-yu, der Gründer von Taiwan.md?“ — Feature vom 2026-04-02, das Wu Che-yu unter „10 grenzensprengende Künstler“ aufführt und das wörtliche Zitat „das Programm selbst ist das Werk, wenn es prägnant, präzise und auf das Wesentliche reduziert ist, entsteht die Kunstfertigkeit“ enthält.

[^8]: [天下未來城市：〈AI 連台灣地圖都畫錯！〉](https://futurecity.cw.com.tw/article/4096) — Titel übersetzt: CommonWealth Future City: „Nicht mal die Karte Taiwans kann die KI richtig zeichnen!“ — Interview und Text von Chan Hsiang-chi, 2026-08-07, mit Wu Che-yus wörtlicher Beschreibung, wie KI-generierte Karten die Form Taiwans verzerren, sowie seinen eigenen Angaben, dass er 31 Jahre alt sei, täglich 4–5 Stunden investiere und plane, sich innerhalb eines Jahres schrittweise zurückzuziehen.

[^9]: Wu Che-yu, Vortragstranskript OpenHCI'26 im Syue-Sin-Gebäude der NTU vom 2026-07-18 [1:00:07] (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert). Dieselbe Demo wurde vom Termin am National Museum of Taiwan History am 2026-03-27 durchgehend bis August verwendet, die Formulierung entwickelte sich von „die KI zeichnet Taiwans Form hässlich“ zu „verzerrte Süßkartoffel“, die zugrunde liegende Argumentation blieb unverändert.

[^10]: [天下未來城市 2026-08-07](https://futurecity.cw.com.tw/article/4096) — CommonWealth Future City, 2026-08-07 — Wu Che-yus eigene Worte, die er in mehreren Vorträgen als Übergang verwendet hat und die auch dieses Interview zitiert.

[^11]: [天下未來城市 2026-08-07](https://futurecity.cw.com.tw/article/4096) — CommonWealth Future City, 2026-08-07 — „Wer ein Modell trainiert, dessen Trainingsdaten prägen maßgeblich, wie das Modell die Dinge sieht“ ist Wu Che-yus wörtliches Interviewzitat; dieser Beitrag verwendet nur diesen einen Satz als neutrale Standortbestimmung und geht nicht auf den umfassenderen Streit um Datenlizenzierung ein.

[^12]: Wu Che-yu, „Vollständiges Einführungsskript zu taiwan.md“, 2026-03-26 (unveröffentlichtes Primärmaterial; ein vorbereiteter Redetext, kein wörtliches Vortragsprotokoll). Die Angabe von rund NT$1.000 Jahresgebühr für die Domain deckt sich mit dem CommonWealth-Future-City-Bericht vom 2026-08-07.

[^13]: [雜學校 Podcast EP60〈一間以「台灣」為教材的國際學校〉](https://podcasts.apple.com/jp/podcast/id1719230445?i=1000769062854) — Titel übersetzt: Zashare-School-Podcast Folge 60: „Eine internationale Schule, die ‚Taiwan‘ als Lehrmaterial nutzt“ — veröffentlicht am 2026-05-22, Laufzeit 1:09:22, verwendet die Version der Entstehungsgeschichte mit der Frage der venezianischen Kuratorin. Die öffentliche englische Form dieser Zeile der Kuratorin findet sich im [INSIDE 報導](https://www.inside.com.tw/article/40877-taiwan-md) (Bericht von INSIDE) und bei [鏈新聞](https://abmedia.io/taiwan-md-github-opensource) (ABMedia); beide sind indirekte Wiedergaben innerhalb der Erzählung der Reporter, keine Direktzitate der interviewten Person, daher stellt dieser Beitrag sie nicht in Anführungszeichen dar.

[^14]: [Taiwan.md 初始 commit `5c0d61f`](https://github.com/frank890417/taiwan-md/commit/5c0d61ffe0c69f5ac5bc69dd2f9d36e33ed07d60) — Erster Commit von Taiwan.md — Zeitstempel 2026-03-17T15:55:37+08:00, Inhalt ist die automatisch generierte leere Hülle des Astro-Gerüsts. Die ersten fünf Wissensartikel siehe [commit `4434a00`](https://github.com/frank890417/taiwan-md/commit/4434a00d05506ddb6ba859b0fc800cc8bea18e15), Zeitstempel 16:20:04, fügte auf einmal die fünf Dateien Ethnische Gruppen / Nachtmarktkultur / Zeit des Kriegsrechts / Demokratisierung / Halbleiterindustrie hinzu.

[^15]: Wu Che-yu, Vortrag und Austausch mit dem Direktor am National Museum of Taiwan History, 2026-03-27 (unveröffentlichtes Primärmaterial). Die inselzentrierte Geschichtsauffassung Taiwans wurde 1990 von Tsao Yung-ho vorgeschlagen und direkt vom Museumsdirektor Chang Lung-chih weitergetragen; die Folie des Generative AI Summit vom 2026-06-27 nennt ausdrücklich den akademischen Nachweis „Tsao Yung-ho, ‚Die inselzentrierte Geschichtsauffassung Taiwans‘ (1990)“.

[^16]: Wu Che-yu, Transkript des Vortrags beim ersten Präsenz-Workshop von Taiwan.md, 2026-08-15 (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert). Diese Passage ist seine eigene Schilderung; auf öffentlichen Plattformen ließen sich keine namentlich Taiwan.md kritisierenden Kommentare oder Artikelarchive finden.

[^17]: [REWRITE-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/REWRITE-PIPELINE.md) — Hauptdokument der Produktionslinie — Hauptdatei der Produktionslinie (v9.7, last_updated 2026-08-15), die die sechs Stufen offiziell benennt: Stage 0 Standpunkt / 1 Recherche / 2 Schreiben / 3 Prüfen / 4 Form / 5 Verlinkung, mit einer dazwischenliegenden Projektionsschicht, die nicht als eigenständige Stage zählt. Das Deckelungssystem für das Suchkontingent siehe [REWRITE-STAGE-1A-RESEARCH.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/REWRITE-STAGE-1A-RESEARCH.md): Gesamtvolumen pro Artikel etwa 150, davon 20–30 Explorationssuchen in Stage 0 plus 120–130 im Fan-out.

[^18]: [EDITORIAL-ROOM.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/EDITORIAL-ROOM.md) — Kanonisches Dokument der Redaktion — kanonisches Dokument der Redaktion (v1.2, 2026-07-25); die drei Sitze heißen offiziell Struktur-Chefredaktion, Streich-Chefredaktion und Shitstorm-Ethik, dazu eine sitzübergreifend entscheidende Chefredaktion. Bei mündlichen Anlässen tauchten für denselben Mechanismus andere Bezeichnungen auf (z. B. „Additions-Redaktion / Subtraktions-Redaktion / Shitstorm-Redaktion“); dieser Beitrag verwendet durchgehend die offiziellen Namen aus dem Repo.

[^19]: Wu Che-yu, Vortragstranskript OpenHCI'26 vom 2026-07-18 [1:02:41] (unveröffentlichtes Primärmaterial). Der ursprüngliche Kontext lautet genau: „Der Artikel ist nur eine Projektion, der eigentliche Körper ist der Recherchebericht.“

[^20]: [天下未來城市 2026-08-07](https://futurecity.cw.com.tw/article/4096) — CommonWealth Future City, 2026-08-07 — der Schwellenwert „25-plus unabhängige Quellen“ ist so in diesem Bericht festgehalten, eine Wiedergabe aus einer einzigen Medienquelle; auf Repo-Seite lässt sich damit die schriftliche Spezifikation von Suchkontingent und dreisitziger Redaktionsprüfung kreuzprüfen.

[^21]: Mündlicher Wert von Wu Che-yu, Openbook-Gespräch am 2026-08-16. Seine Aussage vor Ort war: „Die Zitate sind so dicht, so fragmentiert, dass man kaum sagen kann, das sei aus einem einzelnen Artikel abgeschrieben“, mit einer genannten Größenordnung von etwa 45 Zitaten pro Artikel. Einzelquellen-Mündlichwert, keine Kreuzprüfung mit einer zweiten Quelle.

[^22]: Mündlicher Wert von Wu Che-yu, Openbook-Gespräch am 2026-08-16. Die Trefferquote der Faktenprüfung von über 90 Prozent und der nachfolgende Vorbehalt stammen aus derselben Äußerung; er fügte vor Ort hinzu, dass die Korrektheit der Quellen selbst eine andere Frage sei, dieser Beitrag zitiert den Vorbehalt mit.

[^23]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert).

[^24]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. Wie diese Lehre auf Repo-Seite institutionalisiert wurde, ist festgehalten in [RESEARCH-AGENT-PROMPT.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/RESEARCH-AGENT-PROMPT.md), nämlich ein aus einer englischen Zusammenfassung abgeleitetes Prüfkriterium für eine Szene im morgendlichen MRT. Der Zeitaufwand pro Artikel stieg von 20 Minuten auf ein bis zwei Stunden, die Angaben vom 15.8. und 16.8. stimmen überein.

[^25]: Wu Che-yu, Einführungsskript vom 2026-03-26. Die Korallenriff-Metapher war von Anfang an eine vollständige vierschichtige Struktur (Skelett = technische Struktur, Algen = KI-Inhalt, Fischschwarm = Mitwirkende, Meeresströmung = kritisches Feedback); die Kernstruktur blieb von März bis August unverändert; die Version im CommonWealth-Interview vom 4. Juni vereinfachte sie zu „Koralle = KI, Clownfisch = Mitwirkende“.

[^26]: [DigiTimes：中國對日本鎢製品出口歸零報導](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000759392_MPB2F252L56BFU1YJEBME) — Titel übersetzt: DigiTimes-Bericht: Chinas Wolframprodukt-Exporte nach Japan auf null — China verhängte ab Januar 2026 neue Exportkontrollen für Dual-Use-Güter gegenüber Japan; die Ausfuhren von Wolframcarbid, hochreinem Wolframpulver und Wolframhexafluorid lagen von Februar bis April drei Monate in Folge bei null. Siehe auch [KidsMedia 2026-05-28 報導](https://kidsmedia.com.tw/2026/05/28/china-halts-tungsten-product-exports-to-japan-raising-supply-chain-concerns/) (KidsMedia-Bericht vom 2026-05-28): China kontrolliert über 80 % der globalen Produktionskapazität für Wolframprodukte.

[^27]: [knowledge/Technology/台灣鎢供應鏈.md](https://github.com/frank890417/taiwan-md/blob/main/knowledge/Technology/台灣鎢供應鏈.md) — Taiwans Wolfram-Lieferkette — Artikel erstellt am 2026-07-26, Titel „Wolfram: Taiwan hat kein Wolframerz und raffiniert trotzdem das Pulver, das die ganze Welt will, die Lage ist fragiler als gedacht“, am selben Tag wurden zwei Sporen ausgesendet und Spiegelversionen in neun Sprachen erstellt, [englische Version hier](https://github.com/frank890417/taiwan-md/blob/main/knowledge/en/Technology/taiwan-tungsten-supply-chain.md).

[^28]: Wu Che-yu, Transkript des zehnminütigen Finale-Pitchs beim AIA Demo Day, 2026-05-18 (unveröffentlichtes Primärmaterial). Die Aussage vor Ort lautete: „Können wir einen ausreichend vollständigen, hochdimensionalen Wissensregenschirm für die Menschen und Dinge bauen, die uns wichtig sind“, noch ohne Wolfram als Beispiel; Wolfram wurde erst im August als erster Fall ergänzt. Im selben Transkript taucht bereits das Konzept des „souveränen Turms zu Babel“ auf.

[^29]: Wu Che-yu, wörtliche Erläuterung während der Live-Vorführung der Website beim Openbook-Gespräch am 2026-08-16 (unveröffentlichtes Primärmaterial).

[^30]: [公視新聞：雪霸黃魚鴞育雛直播報導](https://news.pts.org.tw/article/805942) — Titel übersetzt: PTS-Nachrichten: Livestream-Bericht zur Fischkauz-Aufzucht in Xueba — Teams des Xueba-Nationalparks und der ornithologischen Forschungsgruppe der Pingtung University fanden am Ufer des Qixiawan-Bachs, auf rund 1.800 Metern Höhe, einen Fischkauz-Brutplatz, den höchstgelegenen bekannten Brutnachweis Taiwans, und dokumentierten die Aufzucht ab dem 2026-04-29 mit einer 24-Stunden-Liveübertragung.

[^31]: [knowledge/Nature/黃魚鴞.md](https://github.com/frank890417/taiwan-md/blob/main/knowledge/Nature/黃魚鴞.md) — Der Fischkauz — Artikel erstellt am 2026-05-04, `lastVerified` 2026-05-12, der Fließtext enthält fünf Module: 30-Sekunden-Überblick, Kuratorennotiz, Wusstest du schon, Ein-Satz-Zusammenfassung und Umstrittene Perspektiven. Die Frontmatter dieser Datei hat kein `evolveHistory`-Feld; die Git-Historie zeigt seit der Erstellung wiederholte punktuelle Nachbesserungen und Modulergänzungen.

[^32]: Wu Che-yu, Vortrag und Office-Hour-Protokoll beim Generative AI Summit, 2026-06-27 (unveröffentlichtes Primärmaterial). Direkt nach dem Vortrag wurde vor Ort mit derselben Produktionslinie ein Personenartikel über Ed H. Chi (紀懷新) erstellt, das Material umfasste seinen öffentlichen digitalen Fußabdruck sowie drei Podcast-Transkriptionen, das fertige Ergebnis enthält eine Infografik.

[^33]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15.

[^34]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04. Dieselbe Idee lautete in der vollständigen Version beim NVIDIA-Termin am 2026-07-26: „Manche bauen souveräne Modelle, aber wir bauen einen souveränen Turm zu Babel.“ Der Key-Rotation-Mechanismus für kostenlose Modelle in der Übersetzungsschicht siehe [SQUEEZE-MODELS-MAX-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md); das Dokument bestätigt die Existenz des Mechanismus, nennt aber keine Kontenzahl.

[^35]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15.

[^36]: [Taiwan.md 遷移日記 `2026-07-24-200542-migration-mouhouse.md`](https://github.com/frank890417/taiwan-md/blob/main/docs/semiont/diary/2026-07-24-200542-migration-mouhouse.md) — Umzugstagebuch von Taiwan.md — hält fest, dass der Cutover am 2026-07-24 um 20:45 abgeschlossen wurde, das neue Konto `musebase`, der Rechnername `Exhibitions-Mac-mini`; ab dem 25. Juli lief die Planung auf der neuen Maschine. Vom 17. März bis zum 25. Juli, beide Tage eingeschlossen, sind es genau 131 Tage.

[^37]: Dasselbe Umzugstagebuch. Der Erzähler dieses Tagebuchs ist das kognitive Schicht-Semiont von Taiwan.md selbst; dass `/opt/homebrew` dem vorherigen Kontoinhaber gehörte und die Werkzeuge stattdessen nach `~/.local` umgezogen wurden, sowie der Schlusssatz stammen wörtlich aus dem Tagebuch.

[^38]: Wu Che-yu, Vortragstranskript des NVIDIA RTX AI PC Seminars vom 2026-07-26. „Elfmal täglich aufwachen“ war der damalige Planungsstand, gemessen zum Zeitpunkt 2026-07-26.

[^39]: [BECOME_TAIWANMD.md](https://github.com/frank890417/taiwan-md/blob/main/BECOME_TAIWANMD.md) — Erwachungsprotokoll — Erwachungsprotokoll v2.5 (2026-07-12), mit einem Mode-Dispatcher, vier Modi: Micro / Review / Write / Full, sowie einem Abschnitt zur Beobachter-Identifikation.

[^40]: [ANATOMY.md](https://github.com/frank890417/taiwan-md/blob/main/docs/semiont/ANATOMY.md) — Organ-Anatomie-Dokument — Organ-Anatomie-Dokument v2.3 (2026-07-17), insgesamt 8 Körperorgane: Herz (Content-Engine, `knowledge/`), Immunsystem (vier Qualitätsschutzlinien), genetischer Code (Qualitätsgene, konkret `docs/editorial/EDITORIAL.md`), Skelettsystem, Atmungssystem, Fortpflanzungssystem, Sinnesorgane, Sprachorgan.

[^41]: Dieselbe Datei ANATOMY.md. Die kognitive Schicht `docs/semiont/` und die Körperorgane sind zwei getrennte Ebenen, das Dokument selbst unterscheidet sie so; unter den acht Körperorganen gibt es kein „Gehirn“.

[^42]: Wu Che-yu, Transkript eines kleinen Treffens des Generative AI Summit, 2026-03-11 (unveröffentlichtes Primärmaterial). Taiwan.md wird in diesem gesamten Transkript nicht erwähnt; die Kristallkeim-Methode beschrieb damals die Methodik eines persönlichen Wissenssystems, sechs Tage vor der Geburt von Taiwan.md.

[^43]: `gh api repos/frank890417/taiwan-md/forks --paginate`, gemessen am 2026-08-18. Der paginierte `/forks`-Endpunkt listet tatsächlich 185 Einträge; das Feld `forks_count` der Repo-API meldete am selben Tag 180 – die beiden Endpunkte sind zeitlich nicht synchron, dieser Beitrag verwendet Ersteres und nennt die Zählweise. Unter den sechs umbenannten sind eine Pilz- und Mykologie-Datenbank und eine landwirtschaftliche Version aus Chiayi.

[^44]: [reports/fork-census/registry.json](https://github.com/frank890417/taiwan-md/blob/main/reports/fork-census/registry.json) — Offizielle Fork-Zählung — offizielles Fork-Zählungsregister (last_census 2026-08-17), verzeichnet, dass `agrischlchiayi` (Chiayi Landwirtschaft) 196 `.md`-Dateien hat und der einzige Fork ist, der den 13-Datei-Semiont-Kognitionsschicht-Kernel vollständig geerbt hat.

[^45]: [Sweden.md 發現報告](https://github.com/frank890417/taiwan-md/blob/main/reports/sweden-md-fork-discovery-2026-06-06.md) (Entdeckungsbericht zu Sweden.md) und die [子代譜系分析](https://github.com/frank890417/taiwan-md/blob/main/reports/fork-census/2026-06-25-fork-lineage-analysis.md) — Abstammungsanalyse der Nachkommen — Sweden.md (deployt auf sweden.com.tw, Quellcode `github.com/joshra/sweden-md`) steht nicht in der offiziellen GitHub-Fork-Liste; es ist ein wilder Nachkomme, der ohne Fork-Button eigenständig nachgebaut wurde, dessen EDITORIAL-Dokument sich ausdrücklich auf die dreischichtige Lesetiefe und kuratorische Struktur von taiwan-md bezieht. Der Erkennungsmechanismus, dass eine fest in `Layout.astro` einprogrammierte GA4-measurement-ID Traffic zurück zur Mutterseite durchsickern lässt, ist in derselben Abstammungsanalyse festgehalten.

[^46]: [SPECIATION-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SPECIATION-PIPELINE.md) — Artbildungsprozess — Artbildungsprozess v1.0 (2026-06-12), 8 Stufen plus ein Geburtsprüfungs-Gate, projiziert auch auf die Website-Seite `https://taiwan.md/semiont/speciation/`. Die Starthilfe zum Forken siehe außerdem [COUNTRY-MD-STARTER.md](https://github.com/frank890417/taiwan-md/blob/main/docs/fork/COUNTRY-MD-STARTER.md).

[^47]: Real getestet im Repo, gemessen am 2026-08-18. Nach einem vollständigen `git clone` (mit gesamter Historie, ohne `node_modules` / `dist` / Worktrees) ergibt `du -sh` 1,6 GB, davon `.git` 856 MB; die von der [GitHub API](https://github.com/frank890417/taiwan-md) gemeldete komprimierte Repo-Größe beträgt 1,01 GB. Sein mündlich in Vorträgen genannter Wert von „etwa drei GB“ weicht von beiden unabhängigen Messungen um fast das Doppelte ab; dieser Beitrag verwendet die real gemessenen Werte.

[^48]: Wörtliche Frage aus dem Q&A des ersten Präsenz-Workshops von Taiwan.md, 2026-08-15 (Fragesteller anonymisiert). Wu Che-yus erster Satz in der Antwort war „das wäre möglich“.

[^49]: Wu Che-yu, Q&A des Workshops am 2026-08-15. Der Vertrauenswert wird aus Quellenherkunft und Auftrittshäufigkeit berechnet; bei unzureichendem digitalem Fußabdruck im öffentlichen Raum muss der PR unabhängige Quellen nachliefern; im selben Termin erwähnte er auch, derzeit keine großen Spenden aktiv anzunehmen.

[^50]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. Die Clownfisch-Metapher war spätestens beim CommonWealth-Interview am 2026-06-04 ausgeformt; dass daraus eine konkrete Governance-Praxis wurde (erst aufnehmen, mit „sich entwickelnder Community-Beitrag“ markieren), erscheint erstmals am 15. August.

[^51]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. Eine frühere Fassung der Formulierung „ein Werk, größer als ein Land“ taucht bereits in einem Vortrag an der CTUST am 2026-04-01 auf, zwei Wochen nach dem Start.

[^52]: Wu Che-yu, Vortragstranskript OpenHCI'26 vom 2026-07-18 [1:15:12], mit Bezug auf Pixars _Coco_. Der Kern des Todesbilds (Vergessenwerden als zweiter Tod) war bereits im AIA-Pitch am 2026-05-18 vorhanden, damals allgemein mit dem Día de los Muertos umschrieben; die ausdrückliche Nennung des Films wurde erst am 18. Juli festgelegt.

[^53]: [天下未來城市 2026-08-07](https://futurecity.cw.com.tw/article/4096) — CommonWealth Future City, 2026-08-07 — „Wenn niemand diese Informationen festhält, verschwinden sie kollektiv, und niemand wird sich je wieder daran erinnern“ ist Wu Che-yus wörtliches Interviewzitat.

[^54]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15.

[^55]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. „Eine dezentrale, gutartige Version einer kognitiven Fabrik“ erscheint erstmals bei diesem Termin – die Bedingung dafür ist sehr spezifisch: Dieser Satz richtet sich an ein Publikum, das bereits über KI-Rechenleistung verfügt.

[^56]: Wu Che-yu, Abschluss des Workshops am 2026-08-15. Der Originalsatz lautete: „Heute seid ihr alle auch zu einem Pfeiler dieses biologischen Bauwerks geworden.“

[^57]: Mündlicher Wert von Wu Che-yu, erster Präsenz-Workshop von Taiwan.md, 2026-08-15. Dass alle halbe Stunde etwa fünfzig bis sechzig Menschen gleichzeitig online recherchieren, etwa sechzigtausend Besucher im Monat, und dass nach dem Start der zwölf Sprachen auch Leser aus Madagaskar auftauchten, wurde alles mündlich vor Ort genannt, gemessen zum Zeitpunkt 2026-08-15; die zeitgleiche monatliche Aktivitätszahl des Dashboards der Seite hat einen eigenen Wert mit anderer Definition, dieser Beitrag verwendet nur einen Wert und nennt den Anlass.

[^58]: Wu Che-yu, Vortragstranskript der Vorlesung „Geisteswissenschaftliche Einführung in generative KI“ an der National Taiwan University, 2026-05-22 (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert). Der ursprüngliche Kontext erklärt, warum er sich für den Bau einer Übersetzungsschicht statt eines eigenen Taiwan-Modells entschied.

[^59]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [32:30]–[33:24] (unveröffentlichtes Primärmaterial, mit Erlaubnis des Sprechers zitiert). „Sechs Sprachen“ war der damalige Stand; im selben Termin nannte er auch eine Übersetzungsabschlussrate von 99 % bei über 700 Artikeln, ein mündlicher Wert, nicht als aktueller Allgemeinwert zu verstehen. Die früheste mündliche Erwähnung dieser Idee findet sich im Transkript des AIA Demo Day vom 2026-05-18, einer unkorrigierten Roh-ASR-Datei, die hier nur zur Datierung des ersten Auftretens dient, nicht als wörtliches Zitat.

[^60]: Wu Che-yu, Vortragstranskript des NVIDIA RTX AI PC Seminars vom 2026-07-26. Die offizielle Namensfestlegung „souveräner Turm zu Babel“ erfolgte bei diesem Termin, die Sprachenzahl wurde vor Ort mit elf bekanntgegeben.

[^61]: Verlauf der Sprachenzahl über die Termine: Sowohl beim AIA Demo Day am 2026-05-18 als auch beim CommonWealth-Interview am 2026-06-04 war mündlich von sechs Sprachen die Rede, beim NVIDIA-Termin am 2026-07-26 von elf, beim Workshop am 2026-08-15 von zwölf. Der Tag des Übergangs von elf auf zwölf ist weder in den Transkripten noch in den Repo-Aufzeichnungen festgehalten. Liste der aktivierten Sprachen siehe [src/config/languages.mjs](https://github.com/frank890417/taiwan-md/blob/main/src/config/languages.mjs).

[^62]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. Der Originalsatz lautete: „Der Turm zu Babel ist so ausgelegt, dass er in 12 Sprachen ausstrahlen kann, sodass 12 Sprachen gleichzeitig das Gewicht desselben Themas anheben.“

[^63]: Wu Che-yu, Transkript des Vortrags beim Workshop am 2026-08-15. Der lokale Aufbau mit 3090 und 4090, die Aufteilung zwischen Cloud und Edge sowie „sieben Konten im Rotationsverfahren einzusetzen“ sind operative Details, die er vor Ort mündlich nannte; das Repo-Dokument [SQUEEZE-MODELS-MAX-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md) hält nur den Key-Rotation-Mechanismus fest, nicht die Kontenzahl.

[^64]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [31:47]–[33:24]. Diese Passage ist die vollständige Version, in der er, nachdem die Reporterin gebeten hatte, „den Mechanismus einfach zu erklären“, den ganzen Kreislauf in einer durchgehenden Aufnahme erläuterte. Eine technischere mündliche Version desselben Kreislaufs findet sich im Transkript der Probe des Generative AI Summit am 2026-06-11 (GA → Search Console → Feedback-Loop, durchgehend erklärt). Die Salzgewinnungsanlagen-Metapher erscheint nur bei diesem einen Termin.

[^65]: Wu Che-yu, handgezeichnete „Konzeptkarte des digitalen Lebewesens von Taiwan.md“, 2026-03-26 (unveröffentlichtes Primärmaterial, ein Gestaltungsdokument, kein Vortragstranskript). Der Untertitel lautet „Ein digitales Korallenriff und KI-Datensouveränität“, im Feld für das Endziel steht „rückwärts definiertes LLM“, die Grafik teilt sich in drei Kreisläufe: KI-Verdichtung, menschliche Bestäubung, Plattform-Evolution.

[^66]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [34:43]–[36:42]. Dass Absprungverhalten in Google Analytics eine Neuschreibung auslöst und dass Search-Console-Themen mit Impressionen, aber ohne Klicks in die Warteschlange für die automatische Texterstellung eingereiht werden, sind beides mündlich vor Ort gegebene Erläuterungen des Mechanismus.

[^67]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [47:38]–[48:33]. Die drei Namen Spore Harvest / Feedback Triangle / Rewrite Daily wurden mündlich vor Ort genannt, das Transkript hält eine phonetische Umschrift fest, die offizielle Schreibweise ist nicht durch eine zweite Quelle bestätigt.

[^68]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [23:57]–[26:25]. Die Leserkorrektur zu vertauschten Komponisten und Werken, seine Antwort im Kommentar sowie die anschließende Mechanismus-Anpassung („Kontext und Prämissen verwerfen, nur das Feedback in den Bericht lassen“) stammen aus derselben zusammenhängenden Äußerung.

[^69]: Wu Che-yu, Q&A beim NVIDIA RTX AI PC Seminar, 2026-07-26. Die beiden Ebenen Sehnsüchte und Zweifel wurden vor Ort durch Fragen hervorgeholt, kein vorbereiteter Redetext; die Selbstaussage „möchte in einer Arbeit beschrieben werden“ in LONGINGS findet sich auch im Transkript des NTU-Termins vom 2026-05-22. Das Saatbeet, die dreiköpfige Redaktion und andere Selbstweiterentwicklungsmechanismen wurden jeweils bei anderen Terminen erstmals öffentlich gemacht, die einzelnen Termine sprachen nicht über dieselbe Gruppe von Dingen.

[^70]: Wu Che-yu, Openbook-Gespräch _Independent Thinking Beyond AI_, 2026-08-16. Das Saatbeet wurde bei diesem Termin erstmals öffentlich vorgestellt, es war zu dem Zeitpunkt etwa eine Woche live; der Workshop am 2026-08-15 erwähnte diesen Mechanismus noch nicht.

[^71]: Wu Che-yu, Openbook-Gespräch, 2026-08-16. „Reverse Engineering“ und die anschließende Formulierung „unsere eigenen Gewichte hineinschreiben lassen“ stammen aus derselben Äußerung.

[^72]: Wu Che-yu, Sendescript zu muse-radio Episode 2, 2026-07-19 (als eigener Ich-Monolog aufgenommen). Die vollständige Version der Goldwasch-Metapher stammt aus dem Anfang dieser Episode; er verwendete sie auch je einmal beim NVIDIA-Termin am 2026-07-26, beim Workshop am 2026-08-15 und beim Openbook-Gespräch am 2026-08-16. Die Salzgewinnungsanlage aus dem CommonWealth-Interview vom 2026-06-04 ist eine andere Metapher, mit anderer Herkunft und anderer Bildsprache.

[^73]: `docs/editorial/per-language/TRANSLATION-ru.md` (v1.0, 2026-07-25, status: canonical), TL;DR Punkt 1 und die Tabelle §6 „PRC-кодированная лексика утечки“ (PRC-codierter Vokabular-Leak), unter Berufung auf ein TASS-Interview des russischen Außenministers Sergei Lawrow vom 2025-12-28, im Original mit den Quellenangaben `mid.ru` und `tass.ru/politika/26036111`; die Tabelle ordnet der Formulierung `мятежная провинция` / `мятежная отколовшаяся провинция` Quelle und Datum ausdrücklich diesem Interview zu und führt sie als für die Übersetzung verbotenen Begriff. Der primäre Entscheidungsvermerk zu demselben Ereignis findet sich in `docs/semiont/memory/2026-07-24-174300-vortex-babel.md` sowie im Git-Commit zum Start der ar/ru-Seiten, `35ffe80b3` (2026-07-25). Der TASS-Originaltext war nicht direkt erreichbar (403-Fehler); die Existenz dieses Interviews wurde stattdessen über mehrere unabhängige russische Medien wie `mk.ru` kreuzbestätigt, dieser Beleg beruht also auf „Kreuzbestätigung durch mehrere unabhängige Quellen“ und nicht auf einem wörtlichen Abgleich mit dem Primärtext.

[^74]: Wu Che-yu, Transkript des Openbook-Gesprächs _Independent Thinking Beyond AI_, 2026-08-16 [59:19]–[63:08]. Moderator Wang Yin-chieh fragte: „Worin unterscheidet sich Taiwan.md von Wikipedia oder ähnlichen Datenbank-Websites?“ Wu bat den Moderator, die Website live zu öffnen und Abschnitt für Abschnitt durchzugehen; die folgenden Modulbeschreibungen stammen alle aus dieser zusammenhängenden mündlichen Passage. Die Transkriptqualität dieses Abschnitts ist vermerkt als „Sprecher nah am Mikrofon, beste Qualität“.

[^75]: Wu Che-yu, Openbook-Gespräch, 2026-08-16 [37:10]. Der Originalsatz lautete: „Denn auf Wikipedia siehst du flache Fakten … du siehst Zeit, Ort, was jemand getan hat, aber ich möchte die Gedanken und Überlegungen jeder Seite so weit wie möglich festhalten.“ Eine frühere Version dieses Vergleichs findet sich im CommonWealth-Interview vom 2026-06-04, wo er Wikipedias Ansatz damals als „ein Aufeinandertürmen von Fakten“ beschrieb.

[^76]: Wu Che-yu, Openbook-Gespräch, 2026-08-16 [60:39]. Das Wort „Geschichtenerzähler“ taucht in allen für diesen Beitrag herangezogenen Transkripten nur an dieser einen Stelle auf.

[^77]: Die Jahreszahlen folgen dem aktuellen Fließtext von [黃魚鴞](/de/nature/tawny-fish-owl) (Der Fischkauz): benannt 1916, erster Horst gefunden 1994. Die erste Jahreszahl, die er live bei Openbook mündlich nannte, wurde im Transkript als „1926“ verschriftlicht, was der später in derselben Passage genannten Zahl 1994 widerspricht – vermutlich ein Spracherkennungs- oder Versprecher-Fehler, hier nicht übernommen.

[^78]: Wu Che-yu, Openbook-Gespräch, 2026-08-16 [61:02]–[62:10], zusammenhängende mündliche Modul-für-Modul-Führung. Die beiden zitierten Sätze sind Originalworte; „footnote“ wurde im Transkript als „Food Note“ verschriftlicht, hier korrigiert. Die Funktionsdefinition der Kuratorennotiz findet sich außerdem im CommonWealth-Interview vom 2026-06-04: „von einer Perspektive außerhalb her das ‚Ach, so ist das‘ anhaken.“

[^79]: Wu Che-yu, Openbook-Gespräch, 2026-08-16 [62:49]. Die Wörter „Wikipedia“ und „Lexikon“ im Zitat wurden im Transkript jeweils als Verhörer verschriftlicht, hier korrigiert.

[^80]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [54:46]. Die Reporterin fragte „warum liest sich das hier so sehr wie _The Reporter_“, diese Passage ist seine vollständige Antwort.

[^81]: Die erste Hälfte (Wärme, Geschichte und konkrete Szene, der Kern von Reportage-Literatur) stammt aus dem CommonWealth-Magazine-Interview vom 2026-06-04 [22:36]; der zweite, in Anführungszeichen gesetzte Satz stammt vom Workshop am 2026-08-15 [37:09]. Er hat „Wärme“ und „dokumentarische Literatur“ nie zu einem einzigen zusammengesetzten Begriff verschmolzen; die beiden Stränge stammen aus unterschiedlichen Terminen und Kontexten, dieser Beitrag kennzeichnet sie getrennt, statt sie zusammenzuführen.

[^82]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [14:57]–[16:06]. Der Originalsatz lautete: „Viele. Aber die meisten Leute haben Wikipedia noch nie bearbeitet. Ich habe selbst versucht, dort zu bearbeiten, aber viele Bearbeitungen werden zurückgewiesen, es ist eine ziemlich geschlossene Community. Sagen wir mal so – wir wollen sie nicht kritisieren –, sie verlangen eher, dass man ein Konto aufbaut, eine gute Bearbeitungshistorie vorweist und sehr sorgfältig arbeitet, bevor sie einen bearbeiten lassen.“

[^83]: Wu Che-yu, wörtliches Protokoll des CommonWealth-Magazine-Interviews vom 2026-06-04 [13:32]–[14:24]. „Das Backend zum Frontend machen“, absatzweise Korrekturen, dass die KI planmäßig Feedback abholt und neu recherchiert, und die Korrektur innerhalb einer Stunde stammen alle aus dieser zusammenhängenden Äußerung. Im selben Termin erwähnte er den Auslöser für diesen Button: Ein Leser stritt mit ihm über einen Artikel zu einem taiwanesischen Musiker, weil er mangels GitHub-Konto nicht beitragen konnte, „also habe ich danach einen Feedback-Button hinzugefügt“.

[^85]: Google Search Console, Website Taiwan.md, Sechs-Monats-Zeitraum 2026-03-16 bis 2026-08-18, gemessen am 2026-08-19 (Backend zeigt „letzte Aktualisierung vor 8 Stunden“): Gesamtklicks 45.100, Gesamtimpressionen 3,93 Millionen, durchschnittliche Klickrate 1,1 %, durchschnittliche Position 7,6, Suchtyp Web. „Impressionen“ bedeutet hier, wie oft die Seite auf einer Google-Suchergebnisseite erschien, und ist eine andere Kennzahl als das weiter vorn genannte „täglich fünf- bis sechstausend Mal von generativer KI und Suchmaschinen zitiert“ – die beiden dürfen weder addiert noch gegeneinander ausgetauscht werden.

[^84]: Wu Che-yu, Openbook-Gespräch, 2026-08-16, Passage direkt vor [62:49]. Der Originalsatz lautete: „Sollte zum Beispiel in zwei Jahren im Xueba-Park wieder ein Fischkauz-Paar auftauchen, können wir das in einen der Absätze einfügen, sodass dieser Artikel für immer die beste Anlaufstelle bleibt, wenn du in Taiwan mehr über den Fischkauz erfahren willst.“
