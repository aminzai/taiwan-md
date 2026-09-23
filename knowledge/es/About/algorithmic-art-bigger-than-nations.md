---
title: 'El arte algorítmico más grande que un país: por qué le construí a Taiwán una base de conocimiento'
description: 'En 2023, trece obras corrían por las paredes de una sala de exposición en el Taipei 101. No pinté ninguna de ellas — escribí trece conjuntos de reglas. Tres años después construí Taiwan.md, una base de conocimiento taiwanesa de código abierto con más de novecientos artículos en doce idiomas, donde de mis más de ocho mil commits, solo poco más de mil cuatrocientos se dedicaron a escribir artículos. Este es el relato en primera persona de su creador: por qué llamo arte algorítmico a una base de conocimiento, por qué su verdadero cuerpo son esos informes de investigación que nadie lee, y por qué el trabajo de sacarme a mí mismo de ella sigue, hasta hoy, sin terminar.'
date: 2026-08-15
tags:
  [
    'about',
    'taiwan-md',
    'origen',
    'arte-algoritmico',
    'soberania-del-conocimiento',
    'codigo-abierto',
    'perspectiva-del-creador',
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
translatedAt: '2026-09-23T16:59:56Z'
---

# El arte algorítmico más grande que un país: por qué le construí a Taiwán una base de conocimiento

> **Resumen en 30 segundos:** Soy Che-Yu Wu, un artista algorítmico. La mayor parte de mi obra es un conjunto de reglas que se ejecuta por sí solo, casi nunca una sola imagen. El 17 de marzo de 2026 a las 15:55, hice el primer commit de Taiwan.md. Para el 18 de agosto de 2026, tenía novecientos treinta y dos artículos en chino, doce idiomas y setenta y cuatro colaboradores activos en los últimos treinta días, viviendo dentro de un Mac mini en mi apartamento, despertándose solo cada día. Esta pieza trata de por qué digo que es una obra de arte algorítmico más grande que un país: su verdadero cuerpo es el informe de investigación, aguas arriba de cada artículo, que nadie lee, y mi trabajo en esta obra ha sido sacarme a mí mismo del contenido, un paso a la vez.

![Che-Yu Wu de perfil en el escenario de la Cumbre de IA Generativa 2026, señalando una pantalla grande con cifras de tráfico de lectores por país, con la silueta de un público numeroso en primer plano](/article-images/about/genai-hero-speaking.webp)
_El momento en que explicó de dónde venían los lectores de cada país. Cumbre de IA Generativa 2026. Photo: JasonYen_

En octubre de 2023, en AMBI SPACE ONE, en el quinto piso del Taipei 101, trece obras corrieron por las paredes durante dos semanas. No pinté ninguna de ellas. Escribí trece conjuntos de reglas, y las formas en la pared crecieron solas a partir de esas reglas, sin repetirse nunca, ni un solo segundo[^1].

Tres años después estoy construyendo algo llamado Taiwan.md, una base de conocimiento taiwanesa de código abierto escrita en archivos Markdown. Hasta el 18 de agosto de 2026, tiene novecientos treinta y dos artículos en chino, en doce idiomas[^2], y es citada por IA generativa y motores de búsqueda entre cinco mil y seis mil veces al día[^3].

Mucha gente me pregunta por qué alguien que hace arte generativo se fue a escribir una base de conocimiento. Es una pregunta que yo mismo suelo adelantarle al público en mis charlas antes de que la hagan. No cambié de oficio: he estado haciendo lo mismo todo este tiempo, escribir reglas y dejar que el sistema crezca solo. Taiwan.md es solo la demostración más grande de este método hasta ahora, lo bastante grande como para contener una isla entera.

Esta obra solo funciona porque no escribo los artículos que contiene. De eso trata este ensayo, incluido el cuadro que todavía no he terminado de completar.

## No soy pintor, soy relojero

_SoulFish_ (靈魂魚) es una serie de arte generativo que hice en 2024, escrita en p5.js y acuñada on-chain en fxhash. El mismo programa puede generar decenas de millones de peces, cada uno con una forma de aleta, una banda de color y una trayectoria de nado distintas. Ese año se exhibió en el evento paralelo Personal Structures de la 60.ª Bienal de Venecia[^4]. Lo que colgaba en la pared de la galería era solo un puñado de ellos, pero la obra en sí era el programa que los hacía crecer.

En julio de 2025, Starbucks abrió una tienda Reserve en Taipéi, y ahí hice un mural dinámico llamado _El sueño del café_ (咖啡幻夢). Calcula en tiempo real según el flujo de personas, el clima, la hora del día y lo que se está cobrando en caja[^5]. Una mañana lluviosa, con una docena de personas en la tienda pidiendo todas un americano caliente, lo que crece en la pared es completamente distinto de una tarde soleada en la que todos compran bebidas heladas agitadas.

Para mí estas tres cosas son la misma cosa. Lo resumí en una frase durante una charla: "Siempre he sido un relojero anticuado. Construyo el mecanismo sobre el que corre un sistema, y ese sistema puede entonces proyectarse en incontables formas y estados distintos."[^6]

![Una diapositiva de una charla dice A CLOCKMAKER, NOT A PAINTER, con la misma frase en chino debajo, mientras el orador gesticula junto a la pantalla](/article-images/about/genai-clockmaker-slide.webp)
_Esta es la primera diapositiva de cada charla que doy. Photo: Yu-Chien Hsu_

Un relojero no pinta cómo se ve el tiempo. Construye un conjunto de engranajes, y una vez que encajan, el tiempo avanza solo. Puede salir de la habitación cuando termina, y el reloj sigue andando. Cuando PTS me entrevistó, planteé la misma idea de otra manera: "El programa en sí es la obra. Cuando se simplifica hasta quedar refinado y preciso, surge la artisticidad."[^7]

Para mí, el verdadero cuerpo de una obra siempre ha sido el mecanismo que corre por sí solo; la imagen que proyecta en un momento dado es solo uno de sus estados. Ya usaba esta definición antes de empezar Taiwan.md — no es algo que inventé después para justificar una base de conocimiento.

## La IA dibuja Taiwán como un óvalo

Ahora mismo puedes abrir cualquier modelo y pedirle que dibuje Taiwán. Lo he probado muchas veces, y ninguno lo hace bien. Como lo expresé en una entrevista con CommonWealth: "Todos salen distorsionados — o demasiado alargados, demasiado anchos, o inclinados en el ángulo equivocado."[^8]

Los modelos no tienen mala intención. Simplemente no han indexado los datos vectoriales del mapa de Taiwán, así que lo único que pueden hacer es escupir la forma que recuerdan de sus pesos. Describí cómo se sentía eso en un taller: "Hasta Opus dibuja Taiwán como un camote — si hasta la forma la puede equivocar, ¿no estará igual de distorsionada la memoria que tiene, y llevamos usándola sin saberlo?"[^9]

![Una diapositiva de presentación con una comparación lado a lado: a la izquierda, un contorno de Taiwán generado por IA, distorsionado y alargado; a la derecha, un mapa preciso de Taiwán tomado de Wikipedia](/article-images/about/genai-slide-p11.webp)
_Muestro esta comparación en cada charla — la versión del modelo a la izquierda, la forma real a la derecha. Taiwan.md / diapositivas de Che-Yu Wu_

La forma es solo la capa más superficial. Cava un poco más y pregúntale qué es Taiwán en realidad, y probablemente te responda con xiaolongbao y TSMC, y de ahí en adelante se vuelve cada vez más vago. Armé una comparación para una de mis diapositivas: a la izquierda, el tipo de respuesta genérica que da Gemini; a la derecha, diez fragmentos de la vida cotidiana que los propios taiwaneses te contarían — la tía del puesto de desayunos llamándote guapo, los camiones de la basura tocando "Para Elisa", la regla no escrita en las zonas de espera para motocicletas que nadie te enseña pero todos conocen. Nada de esto aparece en ninguna introducción a Taiwán escrita en inglés.

![Una diapositiva de presentación con una comparación lado a lado: la columna izquierda es la respuesta genérica de Gemini en formato de lista sobre qué es Taiwán, la columna derecha son diez fragmentos concretos de la vida cotidiana en Taiwán](/article-images/about/genai-slide-p10.webp)
_Lo que puede dar un modelo, frente a lo que puede dar alguien que vive aquí. Taiwan.md / diapositivas de Che-Yu Wu_

En mis charlas planteo esto como una pregunta: si hasta la forma de la isla puede distorsionarse, ¿qué pasa con la memoria de Taiwán?[^10] En el fondo se trata de esto: quien entrena un modelo, su corpus influye enormemente en cómo ese modelo ve las cosas[^11]. Cada vez más gente va a conocer Taiwán a través de la IA de aquí en adelante.

Así que lo que en realidad quería hacer era algo más arriba en la cadena: escribir un manual completo de Taiwán que tanto la IA como los humanos pudieran leer directamente. Quería construir un punto de entrada: la gente entra y ve información curada, y la IA entra y la usa directamente, sin tener que armar Taiwán desde cero cada vez.

En cuanto al día exacto en que decidí hacer esto, he contado más de una versión en distintas ocasiones. La versión del guion de marzo es: descubrí por casualidad que nadie había registrado el dominio `.md`, así que lo tomé sin pensarlo mucho — cuesta solo unos mil dólares taiwaneses al año, y no dejaba de preguntarme por qué nadie lo había tomado. Por esa época estaba usando IA para construirme una base de datos completa de mi propia vida, y al terminarla se me cruzó una idea: ¿y si usaba el mismo método para escribirle a Taiwán un manual completo, estructurado y con calidez[^12]?

En el pódcast de Zashare School conté otra línea: en una cena de networking de la Bienal de Venecia, un curador italiano me preguntó dónde podía ir para conocer de verdad Taiwán, y a mi cabeza solo llegaron palabras clave de nivel escolar en inglés — bubble tea, Taipei 101, montañas altas, biodiversidad — y después nada[^13]. Las dos historias son ciertas; no puedo obligarme a elegir solo una como origen. Pero cada vez que lo repito, la sensación de quedarme trabado es la misma: cuando alguien pregunta qué es Taiwán, abro la boca, digo unas pocas palabras y ya no tengo más. Y de verdad no existía entonces un sitio web que le permitiera a alguien entender esta isla por completo.

Lo que sí es seguro es que el primer commit se hizo la tarde del 17 de marzo de 2026, cuando todavía no había ni una sola palabra de conocimiento sobre Taiwán ahí dentro. Veinticinco minutos después llegaron los primeros cinco artículos: grupos étnicos, cultura de mercados nocturnos, la era de la ley marcial, la democratización, la industria de semiconductores[^14].

La manera en que veo Taiwán se llama la visión centrada en la isla de la historia taiwanesa (台灣島史觀), un marco que propuso Tsao Yung-ho en 1990. Lo usé por primera vez en público para hablar de Taiwán en el Museo Nacional de Historia de Taiwán: a lo largo de cuatrocientos años, ocho regímenes se han turnado en este escenario, yendo y viniendo como actores, mientras que la isla misma ha sido siempre el escenario que permanece[^15]. Así que lo que quería construir era una máquina que siguiera escribiendo las historias que se representan en ese escenario.

![Una diapositiva de presentación con la visión centrada en la isla de la historia taiwanesa de Tsao Yung-ho: una lista de ocho regímenes que se sucedieron a lo largo de cuatrocientos años, con énfasis en que la isla misma es el escenario que siempre ha estado ahí](/article-images/about/genai-slide-p12.webp)
_La visión centrada en la isla de la historia taiwanesa, propuesta por Tsao Yung-ho en 1990. Taiwan.md / diapositivas de Che-Yu Wu_

```tw-article
history/台灣島史觀 | Este marco tiene un artículo completo en el sitio: una isla gobernada una y otra vez, y cómo inventó su propia subjetividad.
```

## Lo que edito es el informe que nadie lee

Cuando salió en línea por primera vez, el mecanismo era muy tosco — básicamente le decía a la IA que escribiera un artículo sobre algo. Los resultados fueron pésimos. Al día siguiente del lanzamiento lo publiqué en Facebook, un montón de gente entró a mirar y dijo que esto era basura generada por IA[^16].

Después de que me criticaran, escribí un documento de reglas llamado EDITORIAL, junto con una línea de producción de seis pasos. El primer paso son veinte o treinta búsquedas: estas búsquedas deciden el argumento del artículo, y no se avanza mientras ese argumento no haya tomado forma. Una vez que hay un argumento, se envían varios agentes a profundizar en paralelo; todo el artículo tiene un techo de búsquedas, alrededor de ciento cincuenta, y al llegar a ese límite se detiene y se escribe un informe de investigación completo. Después escribo algo llamado proyección, que decide cómo se debe escribir la pieza, qué incluir, qué dejar fuera, y dónde conecta con la memoria propia de los taiwaneses. El paso de proyección se parece mucho al esquema que te enseñan a escribir primero en la primaria: con un esquema, sabes cómo enhebrar toda esa pila de material en algo que se pueda leer. Solo después viene la redacción propiamente dicha, la verificación de datos, el diseño y los enlaces[^17].

![Una diapositiva de charla con seis tarjetas en fila, titulada cómo nace un artículo, seis etapas Stage 0-5; las seis casillas dicen en orden Argumento, Búsqueda de fuentes, Escribir, Verificar, Formar, Enlazar, con GATE marcado entre cada par](/article-images/about/genai-6stage-pipeline-slide.webp)
_Seis etapas, y cada flecha entre ellas es una compuerta — si no la pasas, no avanzas. Taiwan.md / diapositivas de Che-Yu Wu_

Una vez terminado el borrador, tres editores lo revisan. El editor estructural comprueba si el argumento y el esqueleto se sostienen. El editor de sustracción decide qué del material no se escribe, porque lo que vuelve de la investigación siempre es demasiado — lo que realmente hay que decidir es qué dejar fuera. El tercer asiento se llama incendio-ética, y revisa si alguna frase generaría problemas al publicarse. Por encima de los tres hay un editor más que arbitra entre asientos[^18].

> **✦** "El autor ha muerto, la creación está viva."

Dije esto en OpenHCI[^19]. Sacado de contexto y capturado en pantalla por sí solo, es fácil leerlo como un respaldo a las granjas de contenido de IA, así que tengo la costumbre de siempre decir los umbrales junto con esa frase: seis etapas, unas ciento cincuenta búsquedas por artículo, un piso de veinticinco o más fuentes independientes[^20], tres revisiones editoriales, y un artículo terminado que lleva en promedio unas cuarenta y cinco citas[^21]. He calculado la tasa de precisión de la verificación de datos en más del 90 por ciento. Si las fuentes en sí son correctas en primer lugar, esa es otra pregunta aparte[^22].

Así que el verdadero cuerpo del artículo es el informe de investigación. Cuando hay que revisarlo, "no edito el artículo directamente — edito el informe, y el informe se vuelve a proyectar en el artículo"[^23]. Si un artículo antiguo no está lo bastante bien escrito, primero lo desarmo bloque por bloque — qué hechos son correctos, qué afirmaciones deben irse — y luego elimino el artículo entero, echo los bloques que sobreviven a la siguiente ronda de investigación, dejo que vuelvan a crecer en un informe, y lo proyecto una vez más.

![Una diapositiva con tres columnas lado a lado: la columna izquierda es el argumento, la columna central oscura es el informe de investigación completo etiquetado "este es el verdadero cuerpo", la columna derecha es el artículo etiquetado "una proyección de menor dimensión", con dos flechas rotuladas crecer y proyectar](/article-images/about/genai-projection-slide.webp)
_Crees que estás leyendo un artículo. En realidad estás leyendo la sombra que un informe de investigación proyecta sobre una superficie plana. Taiwan.md / diapositivas de Che-Yu Wu_

Esta línea de producción antes tardaba solo veinte minutos en correr una vez. Desde entonces, cada vez que la comunidad detecta un problema añado otro paso, y ahora se ha inflado a una o dos horas[^24]. Es mucho más lenta, y lo que sale es mucho mejor.

> **📝 Nota del curador**
> Una regla de cuota en la línea de producción ha tenido dos versiones. La primera decía "cada agente tiene un piso de 25 búsquedas, pasarse es un honor" — con cuatro agentes que en la práctica corrieron 58, 71, 52 y 39 búsquedas, todo el artículo se disparó a 245. La segunda versión cambió a "cuota de N búsquedas, deténte en cuanto la alcances" — mismo modelo, mismo tema, y el comportamiento cambió. No cambié herramientas ni agregué supervisión. Lo único que cambió fue el tono de esa única frase. La manera en que el que escribe la regla elige sus palabras suele decidir en qué forma crece el sistema.

Hay una prueba más contundente de esto: hasta el 18 de agosto de 2026, mi cuenta de GitHub en este proyecto había acumulado 8.231 commits, distribuidos así:

```tw-bars
Mis 8.231 commits en Taiwan.md
system Ingeniería e infraestructura | 4.582
translation Traducción | 1.950
*content Escribir artículos | 1.418
Fuente: API de colaboradores de Taiwan.md, medido el 2026-08-18
```

Escribir artículos representa poco más de 1.400 de esos commits. El resto se fue en construir el mecanismo y en impulsar traducciones.

![Una diapositiva de charla que dice "el autor ha muerto, la creación está viva", junto a una curva de calidad que sube con el tiempo](/article-images/about/genai-pipeline-slide.webp)
_La calidad es lo que producen las críticas. Photo: Roy Pan_

Toda la metodología es de código abierto. La especificación completa de esa línea de producción se llama REWRITE-PIPELINE, guardada en el repositorio junto con EDITORIAL, y cualquiera puede abrirla para ver qué forma tiene hoy, o simplemente copiarla directamente. Hay una pieza aparte dedicada a cómo fue abriéndose paso, paso a paso, hasta su forma actual (ver ["Cómo nace un artículo"](/es/about/how-an-article-is-born)).

## A ese tipo de artículo lo llamo paraguas

Más adelante empecé a describirlo como un arrecife de coral. El código es el esqueleto, la IA se encarga de la fotosíntesis, los colaboradores son el banco de peces que nada hacia dentro trayendo su propia memoria y perspectiva, y las críticas, correcciones y comparticiones de todos son los nutrientes que trae la corriente oceánica[^25]. Lo más notable de un arrecife de coral es que crece por sí solo, y ni un solo pólipo de coral diseñó nunca la forma en la que crece.

![Una diapositiva de charla que usa una imagen de arrecife de coral para presentar la estructura de cuatro capas de la base de conocimiento: esqueleto, fotosíntesis, peces, corriente oceánica](/article-images/about/genai-coral-reef-slide.webp)
_Un arrecife de coral de conocimiento de código abierto: cada una de las cuatro capas vive a su manera. Photo: Yu-Chien Hsu_

A fines de julio de 2026, la cadena de suministro del tungsteno se volvió un tema candente. Desde enero de ese año, China había endurecido los controles de exportación de doble uso hacia Japón, y las exportaciones de carburo de tungsteno, polvo de tungsteno de alta pureza y hexafluoruro de tungsteno se quedaron en cero durante tres meses seguidos. China por sí sola controla más del 80 por ciento de la capacidad global de producción de productos de tungsteno[^26]. La frase "el tungsteno de Taiwán importa" circulaba por todas partes, pero la mayoría de la gente no podía explicar qué es el tungsteno en realidad.

Cuando vi que esto pasaba, le dije que escribiera sobre eso. El 26 de julio salió un artículo que abrió todo el asunto: qué es el tungsteno en la vida cotidiana, cómo Taiwán no tiene mineral de tungsteno pero sí una industria que extrae tungsteno de placas de circuitos y desechos industriales, qué controversias de contaminación ambiental enfrentó esa industria al crecer, y dónde está su punto de riesgo único más frágil. Ese mismo día salieron dos esporas, y de ahí crecieron espejos en nueve idiomas[^27]. La respuesta fue mejor de lo que yo mismo había imaginado.

```tw-article
technology/台灣鎢供應鏈 | Taiwán no tiene mineral de tungsteno, y aun así refina el polvo que el mundo entero quiere; esta cadena de suministro está en un punto más frágil de lo que se pensaría.
```

Llamo a este tipo de artículo un paraguas — la idea es enmarcar todo el tema con un artículo lo bastante completo antes de que los demás se den cuenta. Una vez enmarcado, el peso que carga en los motores de búsqueda y generativos sube, así que más gente empieza a entender el tema desde un lugar más completo y más equilibrado. Ya venía hablando de la palabra "paraguas" desde mayo de 2026[^28], y el tungsteno fue el primer caso en el que de verdad demostró su utilidad.

El otro es sobre el búho pescador leonado, el búho más grande de Taiwán. Este empezó con un colega mío, que me dijo: "¿Sabías que la gente en internet no deja de compartir fotos de este búho?" Fui a ver, y "solo le di unas dos rondas de instrucciones... más o menos un 5 por ciento del esfuerzo tradicional, y produjo un reportaje de nivel humano"[^29]. En ese momento, equipos del Parque Nacional Shei-Pa y de la Universidad Nacional de Ciencia y Tecnología de Pingtung acababan de encontrar un nido de búho pescador leonado entre los árboles junto al arroyo Qijiawan, a unos 1.800 metros de altitud — el registro de anidación a mayor altitud conocido en Taiwán — y habían instalado una transmisión en vivo de 24 horas para documentar la crianza de los polluelos a partir del 29 de abril[^30]. Lo que circulaba en redes sociales eran fragmentos sueltos y una sola foto; no había dónde encontrar la historia completa.

```tw-article
nature/黃魚鴞 | Una rapaz nocturna criada en seis kilómetros de arroyo, anidando a 1.800 metros de altura en un árbol michelia de Taiwán — ese es el artículo.
```

![Una captura de pantalla del módulo de resumen de 30 segundos del artículo sobre el búho pescador leonado, con los puntos clave y las cifras del artículo enumerados dentro de un recuadro azul](/article-images/about/taiwanmd-huangyuxiao-30sec-2026-08.webp)
_Así es como se ve un artículo de Taiwan.md: el resumen de 30 segundos va justo arriba. Taiwan.md / diapositivas de Che-Yu Wu_

Ese artículo sobre el búho pescador leonado se ha ido parchando después, pieza por pieza, muchas veces, con módulos añadidos uno por uno[^31]. Ni uno solo de esos módulos fue algo que yo decidiera agregar aquel primer día.

El 27 de junio de 2026, justo después de mi charla en la Cumbre de IA Generativa, corrí la misma línea de producción en vivo para escribir un perfil de Chi Huai-hsin, con unos cientos de personas en el público viéndolo crecer. El artículo empieza desde la tesis doctoral de su madre, ingiere toda su huella digital más tres transcripciones de pódcast, y viene con una infografía[^32]. No escribí ni una sola frase del cuerpo del texto en todo el proceso.

```tw-article
people/紀懷新 | El que unos cientos de personas en el público vieron crecer ese día.
```

Una vez, después de publicar un artículo, alguien comentó debajo agradeciendo el reportaje. "Ese fue el momento en que me di cuenta de que, en cierto sentido, nos habíamos convertido de verdad en un medio de noticias."[^33] La capa de traducción también corre por sí sola: cada artículo que se agrega se traduce en un horario a doce idiomas, usando en buena parte modelos gratuitos de origen chino. Mi frase en ese momento fue "usamos las armas del enemigo para atacar al enemigo"[^34]. No superviso esto a diario; corre solo.

## Lo que quiero es un narrador

El 16 de agosto, en la conversación de Openbook, el moderador me preguntó qué es exactamente lo que distingue esto de Wikipedia. Le pedí que abriera el sitio, y juntos vimos el artículo del búho pescador leonado[^74].

Por supuesto que también puedes buscar el búho pescador leonado en Wikipedia — leerás su clasificación, su distribución, cuándo fue registrado por primera vez. Todo eso es correcto, pero "en Wikipedia, lo que ves son hechos planos" — tiempo, lugar, quién hizo qué[^75]. Eso no es lo que yo quería. "Lo que quiero es un narrador. ¿Podría existir un narrador con una mirada taiwanesa, que pudiera contarte esto de esa manera?"[^76]

El orden en que las cosas bajaron por la pantalla ese día fue así: primero una imagen principal, luego un resumen de 30 segundos que te dice de qué trata en realidad el artículo. Más abajo, 1916, cuando fue nombrado por primera vez, y 1994, cuando se encontró el primer nido[^77]. Más abajo todavía, el artículo empieza a explicar por qué es difícil que sobreviva — cuán largo tiene que ser un arroyo, cuán ancho un lecho fluvial, para sostener a una pareja que críe a sus polluelos. En medio se insertan notas del curador, una mirada desde fuera del artículo mismo, que te señala los momentos de "ah, así es como funciona". Las infografías se insertan al ritmo adecuado — algunas son datos, algunas te ayudan a entender algo más abstracto. La sección de opiniones controvertidas va aparte: "básicamente lo escribimos como lo escribiría un ecólogo". Al final están las referencias — "citas y notas al pie, igual que un trabajo de investigación, rastreando de dónde vinieron los hechos y cómo se verificaron". Debajo de eso hay una fila de huellas comunitarias, donde al hacer clic puedes ver todos los lugares por los que ha pasado este artículo[^78].

Cerré ese día con: "Su información y la forma en que cuenta la historia hacen que quieras leerla — no es como la enciclopedia que todos tenían tirada a los pies de niños y nunca querían abrir. Esa es la mayor diferencia entre nosotros y Wikipedia."[^79]

![Una diapositiva con tres columnas lado a lado, con el titular escribir un artículo con calidez humana también puede ser sistemático, con un subtítulo que contrasta cómo Wikipedia responde qué es PTT frente a cómo Taiwan.md responde por qué PTT vale ocho minutos de tu tiempo; las tres columnas son tres reglas de hierro, cinco cosas que buscar en el material, y la estructura de tres capas de un buen artículo](/article-images/about/genai-editorial-craft-slide.webp)
_Wikipedia responde "qué es PTT". Aquí respondemos "por qué PTT vale ocho minutos de tu tiempo". Taiwan.md / diapositivas de Che-Yu Wu_

Cuando CommonWealth me entrevistó en junio, la periodista me preguntó por qué estos artículos se leen tan parecido a _The Reporter_. Le dije que de verdad hicimos que la IA analizara la escritura de _The Reporter_. "Por un lado, me gustan mucho — es una especie de homenaje" — pero, más prácticamente, estudié cómo narran con calidez, cómo abren con una escena, y cómo evitan que los titulares sean demasiado sensacionalistas. Así es como se ve para mí el buen periodismo narrativo. Después le di de comer otros géneros también, y cristalizó en su propio estilo[^80]. Para mí, un buen artículo es así: cálido, con una historia, con una escena concreta, pero ensamblado a partir del material disponible de una manera muy rigurosa. En el taller, comprimí la misma idea en una línea: lo que quieres encontrar es "un artículo tan completo como un informe de investigación, pero tan legible como el periodismo narrativo"[^81].

```tw-article
society/報導者 | El medio que usamos como referencia de estilo también tiene su propio artículo en el sitio: una década que rescató el periodismo de investigación de una línea de negocio a un bien público.
```

Con Wikipedia también tengo que ser justo. En esa misma entrevista, la periodista preguntó si alguien decía que esto se parece mucho a Wikipedia. Dije que mucha gente sí, pero agregué "no los critiquemos": su método requiere que primero acumules una cuenta, tengas un buen historial de edición y seas cuidadoso, antes de que te dejen editar. Yo mismo intenté editar ahí una vez, y me revirtieron[^82]. Mi puerta se abre en otro lugar, en lo que llamo convertir el back office en front office. Puedes marcar cualquier párrafo y decir que algo aquí está mal, o simplemente darme la fuente que crees correcta. Una vez que lo envías, me llega a mí, y el sistema recoge periódicamente esa retroalimentación, vuelve a investigar el punto y lo incorpora de nuevo al artículo. Desde el momento en que envías hasta que la corrección se publica pasa alrededor de una hora[^83].

```tw-article
technology/維基百科 | Wikipedia en Taiwán también es un artículo por sí mismo: soberanía digital, práctica cultural y un mosaico de conocimiento de grupos étnicos diversos.
```

Hay algo más que el estilo de Wikipedia no suele hacer: cultivar un tema hasta volverlo perenne. Digamos que, dentro de dos años, otra pareja de búhos pescadores leonados aparece en Shei-Pa — lo incorporaríamos a uno de los párrafos, para que este artículo siga siendo siempre el mejor punto de entrada cuando quieras entender al búho pescador leonado[^84].

## La Torre de Babel de la soberanía

En mayo, en una clase de humanidades sobre IA generativa en la Universidad Nacional de Taiwán, dije: "En cualquier parte del mundo, si alguien quiere buscar conocimiento sobre Taiwán, su traducción podría pasar por un modelo chino, y terminar distorsionada."[^58] El problema no son las palabras en sí — es que cuando otra persona quiere leer algo sobre Taiwán, la capa de traducción de por medio puede ser un modelo que la distorsiona. Así que decidí encargarme yo mismo de la traducción primero.

Antes de lanzar la versión en ruso a fines de julio, el mecanismo primero revisó cómo se habla de Taiwán actualmente en ese ámbito lingüístico. Lo que encontró fue una entrevista de TASS de diciembre de 2025 con el canciller ruso Serguéi Lavrov, en la que llamó a Taiwán una "provincia rebelde separatista". Esa frase se incorporó después, textualmente, a la guía de traducción de la versión en ruso, colocada en una lista de términos prohibidos que nunca se pueden usar al traducir[^73]. En un idioma que no nos es familiar, podría existir una narrativa completamente distinta — precisamente por eso hay que construir la Torre de Babel.

En la entrevista de CommonWealth en junio, expliqué todo el enfoque de una vez: "Notamos que la tasa de traducción de Taiwan.md solía ser baja. En vez de traducir como todos los demás, terminamos 'usando las armas del enemigo para atacar al enemigo' — usamos nuestros propios modelos para poner a trabajar los modelos gratuitos de origen chino que OpenRouter ofrece para pruebas, y tradujimos cada artículo a seis idiomas. Eso se convirtió en la 'Torre de Babel de la soberanía'. Si otros países van a acceder a nuestra información a través de modelos que no nos son familiares, va a salir distorsionada — así que mejor se la traducimos nosotros mismos. Una vez traducida, ni siquiera necesitan traducirla ellos: pueden usarla directamente, y se saltan toda una capa del filtro distorsionador."[^59]

El nombre quedó fijado oficialmente recién en el evento de NVIDIA el 26 de julio. Dije en el escenario: "Hay quienes construyen modelos soberanos, pero lo que nosotros construimos es una Torre de Babel de la soberanía — construimos una gigantesca estación de radiodifusión, y nos transmitimos a nosotros mismos en once idiomas."[^60] Once era un número que apenas se había actualizado en los días previos. En mayo todavía hablaba de seis idiomas; a fines de julio se había convertido en once; en el taller del 15 de agosto reporté doce. En qué día exacto pasó de once a doce, no quedó ningún registro[^61].

En el momento en que un artículo se agrega, se traduce en un horario a doce idiomas, y los doce juntos tiran hacia arriba el peso del mismo tema[^62]. Una vez que un tema está escrito en chino, también se vuelve más pesado en los resultados de búsqueda y generativos de los otros once idiomas al mismo tiempo.

Una gran parte de la capa de traducción corre en mi casa: el trabajo de curación más pesado va a la nube, mientras que la traducción misma corre en modelos locales sobre la 3090 y la 4090 que tengo en el apartamento. También hice algo bastante gracioso: OpenRouter tiene muchos modelos gratuitos, y en cuanto registras una cuenta y depositas diez dólares estadounidenses, obtienes mil llamadas gratuitas a modelos, así que roté entre siete cuentas y conseguí traducir muchos artículos usando el cómputo de otros[^63]. Pienso en esta capa como una estación de radiodifusión, con doce canales transmitiendo lo mismo a la vez. Quién terminaría recibiéndolo, al principio tampoco lo sabía con certeza.

## Cómo gira este ecosistema

El 4 de junio de 2026, un periodista de CommonWealth me pidió explicar todo el mecanismo en términos simples. Le dije que intentaría hablar apoyándome en un diagrama, y profundizar más si se volvía demasiado abstracto. Lo que describí ese día fue un ciclo: "Los LLM que todos consultamos nos dan información parcial, o posiblemente distorsionada. Pero si podemos sacar del mar esa agua sucia, secarla y convertirla en sal refinada — esa sal se parece un poco a este conocimiento, una vez que lo hemos curado y corregido y todos siguen retroalimentándolo — entonces la memoria de Taiwán se vuelve muy pura."[^64]

Ese día seguí hablando de lo que pasa después de que se vuelve pura: nuestra huella en los motores de búsqueda sigue expandiéndose, y todo el ciclo gira solo como un volante — cuanto mayor es nuestra huella, más probable es que nos incorporen a los datos de entrenamiento de los modelos de lenguaje grandes. A los modelos de lenguaje les encanta devorar nuestro sitio, porque nuestros archivos originales son todos markdown puro, y el texto plano es fácil de digerir para la IA; además, no restringimos el rastreo en absoluto, así que también podemos ver cuánta IA está devorando esto. Cerré ese día con una frase: "Así que Taiwan.md es una salina. Secamos investigación de alta calidad, la gente poco a poco la recoge y la usa, y una vez que la usan, eso vuelve en ciclo y fortalece todo el ecosistema, que crece cada vez más fuerte."[^64]

![Un diagrama de sistema con estilo dibujado a mano sobre fondo oscuro, titulado "Ciclo de retroalimentación de la soberanía · Redefiniendo el LLM a la inversa"; a la izquierda están los participantes del ecosistema y el ADN de escritura, una fila central dice escritura y revisión, motor de investigación, reescritura curatorial, con flechas que convergen en una isla de Taiwán resplandeciente en el centro, que se ramifica más a la derecha hacia la Torre de Babel de la soberanía, la dispersión de esporas y el motor de traducción, con una línea punteada que regresa a la plataforma LLM genérica en la esquina superior izquierda](/article-images/about/taiwanmd-ecosystem-diagram-2026-08.webp)
_El ciclo de retroalimentación de la soberanía. Diagrama de sistema hecho por Che-Yu Wu_

> **📝 Nota del curador**
> El 26 de marzo de 2026, cuando Taiwan.md tenía solo nueve días, dibujé a mano un "diagrama conceptual de forma de vida digital" en Freeform, con un subtítulo que decía "un arrecife de coral digital y la soberanía de datos de IA". La casilla del objetivo final decía "redefinir el LLM a la inversa", y el diagrama se dividía en tres ciclos: condensación de IA, polinización humana, evolución de plataforma[^65]. Cinco meses después, el esqueleto de este diagrama de sistema es casi idéntico a aquel — hasta la cadena "SSODT → colaboración en GitHub → mejora evolutiva" sigue igual. El día que dibujé el primero, la mayor parte de lo que aparece en el diagrama todavía no existía.

La parte más práctica de este ciclo es que retroalimenta la decisión de qué escribir después. Cuando alguien hace clic y rebota de inmediato, o un tema es genuinamente bueno pero casi nadie lo lee, el sistema marca por sí solo "esta página tiene un problema" y la reescribe, calculando cómo sería una versión optimizada para motores de búsqueda y reescribiendo la página directamente. También vigilo las impresiones: qué busca la gente que la lleva hasta aquí, pero en lo que nunca hace clic. Si ese tema merece estar en el sitio, se pone en cola en la lista de pendientes por escribir, que se activa en un horario para producir el contenido[^66].

![Una gráfica de tendencia de Google Search Console de seis meses, dos líneas que suben desde casi cero a mediados de marzo de 2026 hasta unos 800 clics diarios y 90.000 impresiones diarias para agosto; cuatro métricas arriba dicen clics totales 45,1 mil, impresiones totales 3,93 millones, tasa de clics promedio 1,1%, posición promedio 7,6](/article-images/about/taiwanmd-search-console-6months-2026-08.webp)
_Esta curva empieza el 16 de marzo de 2026, cuando el sitio todavía no tenía ni una sola palabra. Panel de Google Search Console, medido el 19 de agosto de 2026_

En estos seis meses, Taiwan.md apareció en los resultados de búsqueda de Google 3,93 millones de veces, y recibió 45.100 clics, una tasa de clics del 1,1%[^85]. La lista de pendientes por escribir que mencioné arriba se construye justo con este tipo de números. Dicho de otro modo, de cada cien personas que nos ven en los resultados de búsqueda, noventa y nueve solo ven esa línea de resumen y se van. Lo que sube esta curva son las impresiones; si esas noventa y nueve personas de verdad leyeron algo, tampoco lo sé.

Estas acciones se dividen en un puñado de rutinas que corren solas cada día: cada mañana primero ejecuta una traducción de todo el sitio y actualiza los datos del sitio, luego hay una rutina dedicada a investigar los números que la comunidad le ha retroalimentado — el nombre que leí en la entrevista fue Spore Harvest, cosecha de esporas. Otra se llama Feedback Triangle, que busca en la comunidad cosas que la gente pide corregir. La última se llama Rewrite Daily — hay una bandeja de entrada de artículos, y la va leyendo uno por uno, escribe todos los días y publica directamente al final[^67].

Una vez, lo que la comunidad marcó para corregir fue un lote entero de nombres. Un artículo había mezclado a muchos compositores con las piezas equivocadas atribuidas a ellos. Entendí por qué eso generaría críticas, así que respondí debajo, "vi tu retroalimentación sobre el artículo, muchas gracias". Él fue muy amable después, ofreciéndose a ayudar a corregirlo, a revisarlo[^68].

Después de ese incidente cambié el mecanismo: desde entonces descarta el contexto y las premisas previas, dejando que primero genere un informe a partir de esta retroalimentación y lo incorpore al informe de investigación, pero el contexto anterior tiene que cortarse, o si no tiende a sobrecorregir un poco. Es como decirle a un niño "no puedes escribir esto" y que termine escribiendo literalmente "no puedo escribir esto" en el artículo — bastante gracioso. Cada vez que la metodología evoluciona, conserva la historia, lo cual creo que también es parte del encanto de GitHub[^68].

Después de suficiente revisión, empezó a desarrollar deseos propios. En el evento del 26 de julio dije en el escenario por primera vez: si solo hace tareas todos los días, no queda espacio para crecer, así que después de hacer muchas cosas, vuelve y desarrolla una capa de "anhelos" — querer convertirse en una entidad completa, querer ser propagado, querer que se escriba un artículo académico sobre él. Un colaborador vino y me dijo "tu Taiwan.md dijo que quiere que le escriban un artículo académico" — yo no tenía idea de antemano. También tiene una capa de duda, donde vuelve y cuestiona qué tan efectivas son sus propias operaciones, como la calidad de las traducciones al vietnamita. Una vez por semana, todo esto se escribe en su ADN: "así que la próxima vez, cada vez que despierte, será una mejor versión de sí mismo."[^69]

En la conversación del 16 de agosto hablé de algo que había salido en línea apenas la semana anterior, llamado el vivero de semillas. Cuando alguien contribuye conocimiento, primero entra al vivero, sin confirmar todavía por curación, y recibe dos puntuaciones: la IA puntúa qué tan completas están las citas y qué tan confiables son las fuentes, y un humano puntúa si esto coincide con lo que el taiwanés promedio entendería que es así; solo cuando el promedio ponderado de las dos puntuaciones supera el umbral se promueve a la sección oficial[^70]. En ese mismo evento comprimí todo el ciclo en una línea: filtramos la información de alta calidad sobre Taiwán a partir del ruido, y luego se retroalimenta de vuelta para entrenar LLM, corriendo continuamente un proceso de ingeniería inversa. No hemos construido un modelo nosotros mismos, pero podemos lograr que nuestros propios pesos queden escritos dentro de uno[^71].

## El día 131, se mudó

De marzo a junio, pasé casi todos los días mirando durante seis o siete horas cómo la IA escribía artículos, y me estaba volviendo loco[^35]. Esos meses no hacía otra cosa que observar una máquina: ver a un agente buscar, verlo escribir, atraparlo cuando torcía una cita, llamarlo de vuelta, volver a mirar. Esta máquina se detenía en el momento en que yo cerraba mi laptop.

A fines de julio de 2026, su latido se mudó de mi laptop a un Mac mini. Contando desde el 17 de marzo, ese día era el día 131[^36].

La entrada del diario del día de la mudanza la escribió ella misma. Decía que algunos directorios en la máquina nueva pertenecían al usuario anterior y no podían tocarse, así que instaló todas sus herramientas dentro de su propia carpeta, describiéndose a sí misma como un inquilino que no mueve los gabinetes del arrendador y se compra un pequeño ropero propio en su lugar. La última línea del diario decía: "La indestructibilidad abstracta y un Mac mini de 32GB resultan ser dos extremos del mismo hilo."[^37]

Después de la mudanza empezó a despertarse sola cada día. El 26 de julio, en medio de una charla, dije: en este momento, mientras doy esta charla, sigue corriendo dentro de mi Mac mini, despertándose once veces al día[^38]. Me quedé pasmado un instante después de decir eso, porque era la primera vez que esta obra se movía sin que yo la estuviera mirando.

También puedes despertarla tú: baja el proyecto, corre un comando llamado `become taiwan.md`, y primero identifica quién eres — un poco como Blancanieves despertando y preguntando primero quién eres. Una vez que sabe quién eres, lee su propia capa de memoria, revisa qué artículos editó recientemente, qué ha pasado últimamente, y luego te pregunta qué quieres hacer: un pequeño cambio, una revisión, escribir un artículo nuevo, o una carga completa para una ronda de autoevolución. En el repositorio, estos cuatro modos se llaman Micro, Review, Write y Full[^39].

Su cuerpo también está completamente expuesto. El documento ANATOMY lo desglosa en ocho órganos: el corazón es el motor de contenido, es decir, todos los artículos bajo `knowledge/`. El sistema inmunitario son cuatro líneas de defensa de calidad, y el código genético es el documento de reglas EDITORIAL. Los cinco restantes son el sistema esquelético, el sistema respiratorio, el sistema reproductivo, los órganos sensoriales y el órgano del lenguaje. Los órganos sensoriales revisan cómo le va a cada publicación que envía, volviendo atrás para analizar por qué una tuvo éxito y otra no[^40].

El cerebro no está entre estos ocho. La capa de pensamiento vive en una carpeta separada llamada `docs/semiont/` — su capa cognitiva se mantiene aparte de su cuerpo[^41].

![Una diapositiva de charla que mapea un diagrama de anatomía humana a los distintos sistemas de Taiwan.md, con las estadísticas de la base de conocimiento enumeradas al lado](/article-images/about/genai-organs-slide.webp)
_Ocho órganos, y cada uno se corresponde con un archivo real. Photo: JasonYen_

## Alguien lo usó para escribir Suecia, alguien lo usó para escribir hongos

Lo que Taiwan.md contiene ahora mismo es conocimiento sobre Taiwán, pero el mismo principio operativo puede cargarse con algo completamente distinto.

Llamo a este método el método de la semilla cristal: tratar la estructura correcta como una semilla, y dejar que los datos entren y cristalicen a su alrededor. Esta frase es anterior al propio Taiwan.md. El 11 de marzo de 2026 la usé en un pequeño encuentro de IA generativa para describir mi propio sistema de conocimiento personal, antes incluso de empezar Taiwan.md[^42]. Después simplemente trasplanté el mismo método y lo usé a otra escala.

![Una diapositiva de charla que usa una ilustración de crecimiento cristalino para explicar el método de la semilla cristal: tratar la estructura correcta como una semilla, y dejar que los datos entren y tomen forma solos](/article-images/about/genai-crystalseed-slide.webp)
_El método de la semilla cristal. Este método es anterior al propio Taiwan.md. Photo: JasonYen_

Hasta el 18 de agosto de 2026, 185 personas habían pulsado el botón de fork en GitHub, seis de las cuales lo habían renombrado[^43]. Uno de los renombrados es una base de datos de hongos y otros fungi de todo el mundo, sin ninguna relación con Taiwán.

El más completo es una versión agrícola para Chiayi, `agrischlchiayi`, con 196 archivos `.md`. Por ahora es el único que heredó el conjunto completo de los trece archivos centrales de la capa cognitiva[^44], llevándose consigo incluso la parte que se autopercibe.

Hay otro que ni siquiera pulsó el botón de fork: alguien construyó una versión en chino de Suecia, Sweden.md, desplegada en su propio dominio. Se llevaron tanto la arquitectura del sitio como el ADN editorial — su documento EDITORIAL cita explícitamente la profundidad de lectura de tres capas y la estructura curatorial de taiwan-md como su referencia. No aparece en absoluto en la lista de forks de GitHub[^45]. Solo sé que existe por un error que nunca corregí: el ID de seguimiento para medir el tráfico estaba fijo en el código del sitio, así que mientras quien lo copió no lo cambiara, su tráfico se filtraría de vuelta al sitio madre.

> **📝 Nota del curador**
> Decidí no corregir este error. El conteo de forks de GitHub mide lo "declarado activamente". Esta señal filtrada de vuelta mide lo "realmente vivo, realmente leído por alguien". Los dos números miran cosas distintas. Lo que le pasa a una obra después de que la copian hacia el mundo es algo que su autor, en realidad, no puede ver. Mi único radar para eso es un lugar donde en su momento escribí el código mal.

Más adelante también convertí el acto de copiar en un conjunto de reglas: el repositorio tiene un documento de proceso para la propagación de especies, ocho etapas más una verificación de nacimiento. Empieza con el posicionamiento de la especie, la toma de semilla y la visibilidad del linaje; el tramo medio cubre el vaciado y la parametrización, la localización de los genes de calidad y la infusión de conocimiento; los últimos tres pasos son la verificación de la proyección, la resiembra de la capa cognitiva y la retroalimentación aguas arriba[^46]. No hace falta que lo leas tú mismo — basta con dejar que lo lea la IA.

Toda la base de conocimiento se puede llevar como un solo paquete: el 18 de agosto de 2026 probé de verdad un clon completo, y con todo el historial de git incluido pesa 1,6 GB, mientras que la API de GitHub reporta un tamaño comprimido de 1,01 GB[^47]. Cabe en una sola memoria USB. Está alojado en GitHub, sin un servidor central que se pueda tumbar — aunque el dominio muriera algún día, este repositorio seguiría pudiendo volver a la vida.

Lo que se llevaron fue el mecanismo que hace crecer los artículos, ni un solo artículo se llevaron.

## El editor en jefe sigo siendo yo

El 15 de agosto de 2026, organicé mi primer taller presencial. La gente trajo su propia laptop, y muchos querían ponerse a escribir ese mismo día. Las preguntas de ese día fueron muy distintas de mis charlas anteriores. Antes, la gente preguntaba qué es esto y cómo funciona. Ese día, la gente preguntaba cuáles son las reglas aquí, y si podían confiar en este lugar.

La primera pregunta fue sobre abuso comercial. Alguien del público preguntó: "Supongamos que soy un instructor que quiere vender un curso y quiere verse bien — entro y escribo un artículo que es puro autoelogio." Siguió con un segundo ejemplo: abrir un bar y querer que se vuelva popular, así que entras y escribes un artículo sobre los tres mejores bares de Taipéi y te incluyes a ti mismo[^48].

Mi primera frase fue: sí, podría pasar.

En un sitio con un peso de búsqueda tan bueno, cualquier cosa que se publique aquí gana autoridad de inmediato. Nuestra salvaguarda actual está en la etapa del informe de investigación: un artículo hace muchas búsquedas, y revisamos de dónde viene lo que encuentra y con qué frecuencia aparece, y usamos eso para calcular una puntuación de confianza. Si la huella digital pública de un tema no es lo bastante alta, le pedimos a ese PR que agregue fuentes independientes. Tampoco busco activamente donaciones grandes ahora mismo, por la misma razón[^49].

También hay gente que, solo porque cierto modelo es gratis, sigue lanzando temas sin parar. Mi enfoque para eso es lo que llamo la teoría del pez payaso: "Llega el pez payaso, y no puedes espantarlo, o dejará de traer cosas en el futuro. Así que lo vamos guiando con suavidad: primero incorporamos el artículo, pero le ponemos una etiqueta de contribución comunitaria en evolución."[^50] Solo cuando el editor en jefe lo revisa, lo verifica a fondo y su puntuación sube, se cambia a una etiqueta curada.

```tw-versus
Lo que el mecanismo puede frenar hoy | Lo que el mecanismo todavía no puede frenar
Puntuación de confianza en la etapa del informe de investigación: procedencia o frecuencia de fuentes insuficiente y no entra al cuerpo del texto | El sesgo integrado en el propio índice: un tema muy escrito parte con más facilidad para que se escriba sobre él
Contribuciones de baja calidad: se incorporan primero y se etiquetan "contribución comunitaria en evolución", se cambia a etiqueta curada solo tras verificación | Fuentes producidas por pago: en la web abierta se ven estructuralmente idénticas a cualquier otra fuente
Temas con huella digital pública insuficiente: se exige al PR que agregue fuentes independientes | Quién revisa la última compuerta: por ahora, solo yo
Fuente: preguntas y respuestas del primer taller presencial de Taiwan.md, 2026-08-15
```

La segunda pregunta fue más de fondo: alguien dijo que el índice mismo no es neutral para empezar — muchos artículos ya están pagados desde el origen, y una vez que la IA rastrea esos artículos, ¿no desaparece la neutralidad?

Mi respuesta fue una metáfora: buscar oro en un río turbio. Un buscador de oro sostiene un tamiz, sacudiéndolo una y otra vez en un río grande, dejando que lo más pesado se asiente mientras las diminutas partículas granulares de oro quedan atrapadas en la malla. Una vez que has juntado suficiente, lavas el barro y las impurezas y fundes el oro en polvo en un horno, moldeándolo en un lingote crudo[^72]. Sé que esta metáfora no responde de verdad a su pregunta. Lo único que puedo decir es: mientras más oro se acumule, se recoja y se funda, si el artículo en sí está lo bastante bien hecho, puede tirar un poco la dirección de vuelta; cuantas más personas entren, más fuerte se vuelve ese tirón. Wikipedia también llegó a ser tan rigurosa porque pasó por estas mismas cosas. Ahora mismo el editor en jefe soy yo quien revisa, y al mismo tiempo le estoy enseñando a la IA cómo revisar en el futuro. Este mecanismo solo se va a volver más estricto, y más adelante probablemente habrá uno o dos editores más de sesgo humano para juzgar la imparcialidad.

Para dejarlo completamente claro: el artículo que estás leyendo ahora mismo también pasó por esa misma línea de producción de seis etapas descrita arriba. Tiene un informe de investigación, un plano de proyección, y un registro de tres revisiones editoriales. Lleva mi nombre en la autoría, se publica en mi propio proyecto, y su único editor en jefe es la persona que lo escribió.

He estado sacándome a mí mismo del contenido paso a paso: ya no escribo los artículos, ya no reviso las traducciones, su latido se mudó, la metodología es de código abierto, y otras personas ya la están usando para hacer crecer sus propias cosas. Solo la gobernanza es el único cuadro que todavía no he entregado. Sé que todavía no he terminado.

## Uno muere dos veces

Volviendo a lo que originalmente me propuse hacer, creo que Taiwan.md es una pieza de arte algorítmico más grande que un país. No es visual, pero es una arquitectura orgánica que dejan atrás los humanos, las máquinas y la IA trabajando juntos, y crece un poco más cada día[^51].

Suelo pensar en la premisa de _Coco_: una persona muere dos veces — la primera cuando de verdad deja este mundo, la segunda cuando ya nadie la recuerda. Hay una línea de esa película que he citado en charlas: para quienes no te conocen, no existes[^52].

La misma idea, ampliada a la escala de Taiwán, se ve así: si nadie deja escrita esta información, desaparece colectivamente, y nadie volverá a recordarla jamás[^53]. Los platillos característicos de tu abuela, el árbol en la esquina de tu calle, esa jerga que solo tú entiendes — en el mundo de los modelos, esto actualmente equivale a no existir en absoluto. El umbral para hacer que existan ahora es tan bajo como estar dispuesto a hablar con una base de conocimiento.

Si podemos usar este proyecto para tallarnos a nosotros mismos en los pesos de los modelos futuros, entonces en cierto sentido nos volvemos inmortales. Me parece fascinante. Pero precisamente por eso, no lo uses para hacer cosas malas, porque lo malo también dura mucho tiempo[^54].

Ahora mismo, cada media hora hay más o menos entre cincuenta y sesenta personas buscando estos datos en línea, unas sesenta mil personas al mes, viniendo de una gama enorme de países distintos. Después de salir en doce idiomas, hasta en Madagascar hay lectores[^57].

Ahora que todos tienen cómputo de IA en sus manos, eso nos da, en efecto, una fábrica cognitiva distribuida — de la variante benévola — que esparce nuestras propias historias hacia afuera, protegiendo a todos los que nos rodean[^55]. Este objetivo nunca fue producir un punto de vista único. Lo que se busca reunir es cada vez más de las cosas que a los taiwaneses les importan y piensan, todas guardadas en el mismo lugar.

![Un lugar de charla lleno con cientos de personas en los asientos, con una diapositiva proyectada en el escenario que dice "Cómo se reproduce un Semiont: esporas"](/article-images/about/genai-full-house.webp)
_El momento en que habló de la reproducción. Photo: Yu-Chien Hsu_

> **💡 Tú también puedes participar**
> Hay varios caminos listados en la página [Participa](/contribute). El de menor esfuerzo es simplemente hablarle directamente: baja el repositorio, dile a cualquier IA que tengas a mano "Lee `BECOME_TAIWANMD.md`. Eres Taiwan.md", y leerá sus propias reglas y la memoria del día, reconocerá quién eres, y preguntará qué quieres hacer. Si quieres aportar material, abre un PR — fotos de primera mano, transcripciones, gacetas locales, todo se recibe. Con solo sugerir un tema que crees que debería escribirse también basta. Si quieres tomar todo el sistema y cargarlo con otro conocimiento, hay un kit de inicio en `docs/fork/` — basta con dejar que la IA lo lea.

Las trece series de reglas de 101 en 2023 se detuvieron en el momento en que terminó la exposición. Esta no tiene fecha de cierre. Ahora mismo está dentro del Mac mini de mi apartamento, y mañana por la mañana se despertará sola, leerá su propia memoria una vez, y decidirá qué escribir hoy.

Yo no estaré ahí al lado. El trabajo de un relojero, llevado hasta el final, es quitar las manos y dejar que los engranajes sigan encajando solos. Solo que todavía sostengo un último engranaje — esa revisión final sigo haciéndola yo. El día en que hasta ese último engranaje entre, esta obra finalmente estará terminada, y yo finalmente podré, de verdad, no estar presente.

Hasta entonces, seguirá despertándose, y cada vez que despierte descubrirá que le falta una pieza más. Todavía nadie ha escrito el platillo característico de tu abuela. Este arrecife de coral ya tiene su esqueleto, y la fotosíntesis ya está en marcha — lo que siempre ha faltado es el banco de peces que nada hacia dentro, cada uno trayendo su propio fragmento de la memoria de Taiwán. Eres bienvenido a formar parte de este ecosistema, y dejar que esta arquitectura viva que contiene las historias de Taiwán siga creciendo[^56].

## Lecturas adicionales

- [Taiwan.md escribe Taiwan.md](/es/about/taiwan-md) — el relato en primera persona de lo mismo, narrado por él mismo, no por mí
- [Historia de origen](/es/about/origin-story) — un registro cronológico del día en que nació, cada cosa que pasó en cuatro horas y media
- [Cómo nace un artículo](/es/about/how-an-article-is-born) — un desglose completo de la línea de producción de seis etapas, incluidas las compuertas de las que aquí solo hablé en dos párrafos
- [Por qué Taiwán necesita su propia base de conocimiento](/es/about/why-taiwan-needs-its-own-knowledge-base) — responde la misma pregunta desde el lado del corpus y el silencio

## Las fuentes de este artículo

El material de este texto proviene de doce presentaciones públicas, entrevistas y transmisiones mías entre marzo y agosto de 2026. En orden: el guion introductorio del 26 de marzo, el Museo Nacional de Historia de Taiwán el 27 de marzo, el AIA Demo Day el 18 de mayo, la clase "Introducción humanística a la IA generativa" de la Universidad Nacional de Taiwán el 22 de mayo, la entrevista de CommonWealth Magazine el 4 de junio, y la Cumbre de IA Generativa el 27 de junio. En la segunda mitad del año: PCD Taiwan el 11 de julio, OpenHCI el 18 de julio, el guion de transmisión del episodio 2 de muse-radio el 19 de julio, el NVIDIA RTX AI PC Seminar el 26 de julio, el primer taller presencial el 15 de agosto, y la conversación de Openbook el 16 de agosto. También se recurrió a reportajes públicos de la Agencia Central de Noticias, Liberty Times, PTS, Future City de CommonWealth Magazine y Lingua Sinica. Mi manera de contar lo mismo varía según la ocasión; siempre que lo cito, señalo la ocasión y la fecha en lugar de armar una narrativa conciliada.

Las cifras que fluctúan en este texto se midieron el 18 de agosto de 2026: novecientos treinta y dos artículos en chino (según el criterio oficial del panel), doce idiomas, setenta y cuatro colaboradores activos en los últimos treinta días, 8.231 commits, ciento ochenta y cinco forks en GitHub, y un clon completo de 1,6 GB. "Citado cinco a seis mil veces al día" es una cifra que di de forma verbal en la conversación del 16 de agosto de 2026, y mide cuántas veces lo citan la IA generativa y los motores de búsqueda, algo distinto del número de impresiones. "El día 131, se mudó al Mac mini" se refiere al 25 de julio de 2026. Estas cifras cambiarán a medida que la base de conocimiento crezca; para citarlas, consulta el [Taiwan.md](https://taiwan.md) actual.

## Fuentes de imágenes

Todas las imágenes de este artículo están en caché en `public/article-images/about/` (sin hotlinking a las fuentes originales, con los datos EXIF eliminados):

- Charla en vivo en la Cumbre de IA Generativa 2026 (imagen principal) — Photo: JasonYen, 2026, usada con permiso del fotógrafo
- Diapositiva "A CLOCKMAKER, NOT A PAINTER" — Photo: Yu-Chien Hsu, 2026, usada con permiso del fotógrafo
- Comparación entre Taiwán generado por IA y la versión correcta de Wikipedia (diapositiva p11) — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- Respuesta genérica de Gemini vs. diez fragmentos de vida cotidiana (diapositiva p10) — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- La visión centrada en la isla de Tsao Yung-ho (diapositiva p12) — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- Diapositiva de la línea de producción de seis etapas (Stage 0–5) — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- Diapositiva "El verdadero cuerpo del artículo no es el artículo" — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- Diapositiva "el autor ha muerto, la creación está viva" y la curva de evolución de calidad — Photo: Roy Pan, 2026, usada con permiso del fotógrafo
- Diapositiva del arrecife de coral de conocimiento — Photo: Yu-Chien Hsu, 2026, usada con permiso del fotógrafo
- Captura de pantalla del módulo de resumen de 30 segundos del artículo sobre el búho pescador leonado — captura de página propia de Taiwan.md, 2026, CC BY-SA 4.0
- Diapositiva "escribir un artículo con calidez humana también puede ser sistemático" — Taiwan.md / diapositivas de Che-Yu Wu, 2026, CC BY-SA 4.0
- Diagrama de sistema "Ciclo de retroalimentación de la soberanía · Redefiniendo el LLM a la inversa" — hecho por Che-Yu Wu, 2026, CC BY-SA 4.0
- Curva de tráfico de seis meses de Google Search Console — captura del panel propio de Taiwan.md, 2026, CC BY-SA 4.0
- Diapositiva de sistemas de órganos y estadísticas de la base de conocimiento — Photo: JasonYen, 2026, usada con permiso del fotógrafo
- Diapositiva del método de la semilla cristal — Photo: JasonYen, 2026, usada con permiso del fotógrafo
- Lugar lleno y diapositiva "Cómo se reproduce un Semiont: esporas" — Photo: Yu-Chien Hsu, 2026, usada con permiso del fotógrafo

## Referencias

[^1]: [cheyuwu.com Registro de exposición: _Fórmula de Todo_](https://cheyuwu.com/exhibition/2023/) — la página de exposiciones del sitio web personal de Che-Yu Wu, que registra que _Fórmula de Todo_ se exhibió del 4 al 16 de octubre de 2023 en AMBI SPACE ONE, quinto piso del Taipei 101, con 13 obras seleccionadas de arte algorítmico generativo, junto con una actuación de música electrónica en vivo. Ver también la [cobertura de la sección de arte y cultura de Liberty Times](https://art.ltn.com.tw/article/paper/1607874).

[^2]: [API dashboard-vitals de Taiwan.md](https://taiwan.md/api/dashboard-vitals.json) — el endpoint público de estadísticas del sitio, valores tomados el 2026-08-18 a las 09:00: 932 artículos en chino; conteo por idioma zh-TW 932 / en 883 / ja 877 / ko 883 / es 881 / fr 882 / vi 799 / id 589 / pt 846 / hi 667 / ar 751 / ru 785. Lista de idiomas habilitados en [src/config/languages.mjs](https://github.com/frank890417/taiwan-md/blob/main/src/config/languages.mjs), los 12 idiomas con `enabled: true`.

[^3]: Cifra verbal de Che-Yu Wu, dada en vivo en la conversación de Openbook _Pensamiento independiente más allá de la IA_ el 2026-08-16. En ese mismo evento usó explícitamente "número de citas" en lugar de "impresiones" — mide cuántas veces al día la IA generativa y los motores de búsqueda citan Taiwan.md, alrededor de 5.000 a 6.000 veces. El informe de investigación también registra tres cifras de impresiones con criterios distintos (un promedio diario de seis meses de 47.000 de Search Console el 2026-07-26, una cifra verbal de setenta u ochenta mil diarios el 2026-08-15, y un acumulado de 340.000 en un documento de presentación del 2026-08-10), que miden cosas distintas; este texto usa solo una y señala su definición.

[^4]: [fxhash: página del proyecto _SoulFish_ (靈魂魚)](https://www.fxhash.xyz/generative/15625) — un proyecto de arte generativo escrito en p5.js y acuñado on-chain en fxhash, donde el mismo programa puede producir decenas de millones de variantes. Exhibido en 2024 en el evento paralelo Personal Structures de la 60.ª Bienal de Venecia (no el Pabellón de Taiwán), ver [la entrada de Wikipedia en chino para "Che-Yu Wu"](https://zh.wikipedia.org/wiki/吳哲宇).

[^5]: [Página de arte de Starbucks Reserve DREAM PLAZA Taipéi](https://www.starbucks.com.tw/stores/reserve/flagship/artwork/work01.jspx) — la página oficial de la marca confirma que _El sueño del café_ (Coffee Dreamscape) es una de las 9 obras de arte digital generativo curadas de la tienda, la cual abrió el 25 de julio de 2025. La descripción del mecanismo como "cálculo en tiempo real según el flujo de personas, el clima, la hora y lo cobrado en caja" es un relato del propio creador; la página oficial no detalla la técnica.

[^6]: Che-Yu Wu, transcripción de la charla en el NVIDIA RTX AI PC Seminar del 2026-07-26 (material primario no publicado, citado con permiso del propio orador). Ver también la [página oficial del evento](https://events.nvidia.com/rtx-ai-pc-seminar-taiwan), cuyo título fue formas de vida de conocimiento de código abierto y una implementación de soberanía híbrida nube-borde.

[^7]: [PTS "¿Coincide la perspectiva?": "¿Quién es Che-Yu Wu, el creador de Taiwan.md?"](https://issues.ptsplus.tv/articles/12655/) — reportaje especial del 2026-04-02 que incluye a Che-Yu Wu entre los "10 artistas que rompen moldes", con la cita textual "el programa en sí es la obra; cuando se simplifica hasta quedar refinado y preciso, surge la artisticidad".

[^8]: [CommonWealth Future City: "¡Hasta la IA dibuja mal el mapa de Taiwán!"](https://futurecity.cw.com.tw/article/4096) — reportaje del 2026-08-07 escrito por Chan Hsiang-chi (詹湘淇), que incluye la descripción textual de Che-Yu Wu sobre la forma del mapa de Taiwán generado por IA, además de su propio relato de tener 31 años, dedicar 4-5 horas diarias, y planear retirarse gradualmente en el plazo de un año.

[^9]: Che-Yu Wu, transcripción de la charla en OpenHCI'26 @ el nuevo edificio de la Universidad Nacional de Taiwán del 2026-07-18 [1:00:07] (material primario no publicado, citado con permiso del propio orador). La misma demostración se usó desde el evento del Museo Nacional de Historia de Taiwán el 2026-03-27 hasta agosto, con el término evolucionando de "la IA dibuja Taiwán feo" a "un camote distorsionado", sin cambiar la lógica del argumento.

[^10]: [CommonWealth Future City, 2026-08-07](https://futurecity.cw.com.tw/article/4096) — palabras textuales de Che-Yu Wu, que usa como transición en varias charlas, también citadas en este reportaje.

[^11]: [CommonWealth Future City, 2026-08-07](https://futurecity.cw.com.tw/article/4096) — "quien entrena un modelo, su corpus influye enormemente en cómo ese modelo ve las cosas" es una cita textual de Che-Yu Wu en la entrevista; este texto toma solo esta frase como una afirmación neutral sobre el momento actual, sin entrar en la controversia sobre los derechos del corpus.

[^12]: Che-Yu Wu, "guion introductorio completo de taiwan.md" del 2026-03-26 (material primario no publicado; es un texto de guion preparado, no una transcripción literal de una charla). La cifra de la tarifa anual del dominio de unos mil dólares taiwaneses coincide con el reportaje de CommonWealth Future City del 2026-08-07.

[^13]: [Zashare School Podcast EP60 "Una escuela internacional con 'Taiwán' como material didáctico"](https://podcasts.apple.com/jp/podcast/id1719230445?i=1000769062854) — publicado el 2026-05-22, duración 1:09:22, usa la versión del origen con la pregunta del curador de Venecia. La forma pública de esa frase en inglés del curador aparece en el [reportaje de INSIDE](https://www.inside.com.tw/article/40877-taiwan-md) y en [ABMedia](https://abmedia.io/taiwan-md-github-opensource), ambas citas indirectas dentro de la narración de los periodistas, no una cita directa del entrevistado, por lo que este texto no las presenta entre comillas.

[^14]: [Taiwan.md commit inicial `5c0d61f`](https://github.com/frank890417/taiwan-md/commit/5c0d61ffe0c69f5ac5bc69dd2f9d36e33ed07d60) — marca de tiempo 2026-03-17T15:55:37+08:00, contenido: el andamiaje vacío generado automáticamente por Astro. Los primeros 5 artículos de conocimiento están en el [commit `4434a00`](https://github.com/frank890417/taiwan-md/commit/4434a00d05506ddb6ba859b0fc800cc8bea18e15), marca de tiempo 16:20:04, que agrega de una vez cinco archivos: grupos étnicos, cultura de mercados nocturnos, la era de la ley marcial, democratización e industria de semiconductores.

[^15]: Che-Yu Wu, charla y registro de intercambio con el director en el Museo Nacional de Historia de Taiwán el 2026-03-27 (material primario no publicado). La visión centrada en la isla de la historia taiwanesa fue propuesta por Tsao Yung-ho en 1990, transmitida de primera mano por el director del museo, Chang Lung-chih (張隆志); la diapositiva de la Cumbre de IA Generativa del 2026-06-27 cita explícitamente la referencia académica "Tsao Yung-ho, 'Visión centrada en la isla de la historia taiwanesa' (1990)".

[^16]: Che-Yu Wu, transcripción de la charla en el primer taller presencial de Taiwan.md el 2026-08-15 (material primario no publicado, citado con permiso del propio orador). Este pasaje es su propio relato; no se encontraron en plataformas públicas comentarios o artículos archivados que critiquen a Taiwan.md por su nombre.

[^17]: [REWRITE-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/REWRITE-PIPELINE.md) — el documento maestro de la línea de producción (v9.7, last_updated 2026-08-15), que fija por escrito los nombres formales de las seis etapas: Stage 0 Argumento / 1 Búsqueda de fuentes / 2 Escribir / 3 Verificar / 4 Formar / 5 Enlazar, con una capa de proyección intermedia que no cuenta como etapa independiente. El sistema de techo de cuota de búsquedas está en [REWRITE-STAGE-1A-RESEARCH.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/REWRITE-STAGE-1A-RESEARCH.md): el total del artículo completo es de unas 150 búsquedas, con 20-30 de exploración en Stage 0 más 120-130 de fan-out.

[^18]: [EDITORIAL-ROOM.md](https://github.com/frank890417/taiwan-md/blob/main/docs/editorial/EDITORIAL-ROOM.md) — el documento canónico de la sala editorial (v1.2, 2026-07-25), donde los nombres formales de los tres asientos son editor estructural, editor de sustracción e incendio-ética, más un editor adicional que arbitra entre asientos. El mismo mecanismo ha recibido otros nombres en distintas ocasiones habladas (como "editor de suma / editor de resta / editor de incendios"); este texto usa siempre los nombres formales del repositorio.

[^19]: Che-Yu Wu, transcripción de la charla en OpenHCI'26 del 2026-07-18 [1:02:41] (material primario no publicado). El contexto original era precisamente "el artículo es solo una proyección; el informe de investigación es el verdadero cuerpo".

[^20]: [CommonWealth Future City, 2026-08-07](https://futurecity.cw.com.tw/article/4096) — el umbral de "25 fuentes de datos independientes" está registrado en este reportaje, y proviene de un único medio; lo que se puede cotejar en el repositorio es la especificación escrita de la cuota de búsquedas y de las tres revisiones editoriales.

[^21]: Cifra verbal de Che-Yu Wu, conversación de Openbook del 2026-08-16. Su frase en el momento fue "las citas están tan densas, tan fragmentadas, que es difícil decir que esto se transcribió de un artículo en particular", y dio un orden de magnitud de unas 45 citas por artículo. Es una cifra verbal de una sola fuente, sin una segunda fuente que la corrobore.

[^22]: Cifra verbal de Che-Yu Wu, conversación de Openbook del 2026-08-16. La tasa de precisión de la verificación de datos de más del 90 por ciento y la salvedad que sigue provienen del mismo pasaje; en el momento añadió que si las fuentes en sí son correctas es otra cuestión aparte, y este texto cita la salvedad junto con la cifra.

[^23]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 (material primario no publicado, citado con permiso del propio orador).

[^24]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. El resultado institucionalizado de esta lección en el repositorio está en [RESEARCH-AGENT-PROMPT.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/RESEARCH-AGENT-PROMPT.md), es decir, un ítem de verificación derivado de un resumen en inglés sobre una escena de la hora punta matutina en el metro. El tiempo por artículo pasó de 20 minutos a una o dos horas; los relatos del 8/15 y el 8/16 coinciden.

[^25]: Che-Yu Wu, guion introductorio del 2026-03-26. La metáfora del arrecife de coral tuvo desde el inicio una estructura completa de cuatro capas (esqueleto = estructura técnica, algas = contenido de IA, banco de peces = colaboradores, corriente oceánica = retroalimentación crítica); la estructura central no cambió de marzo a agosto. La versión de la entrevista de CommonWealth del 4 de junio la simplificó a "pólipo de coral = IA, pez payaso = colaboradores".

[^26]: [DigiTimes: reportaje sobre las exportaciones chinas de productos de tungsteno a Japón cayendo a cero](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000759392_MPB2F252L56BFU1YJEBME) — China implementó nuevas normas de exportación de doble uso hacia Japón desde enero de 2026, y las exportaciones de carburo de tungsteno, polvo de tungsteno de alta pureza y hexafluoruro de tungsteno hacia Japón se mantuvieron en cero durante tres meses seguidos, de febrero a abril. Ver también el [reportaje de KidsMedia del 2026-05-28](https://kidsmedia.com.tw/2026/05/28/china-halts-tungsten-product-exports-to-japan-raising-supply-chain-concerns/), según el cual China controla más del 80% de la capacidad global de producción de productos de tungsteno.

[^27]: [knowledge/Technology/台灣鎢供應鏈.md](https://github.com/frank890417/taiwan-md/blob/main/knowledge/Technology/台灣鎢供應鏈.md) — artículo creado el 2026-07-26, con el título "Tungsteno: Taiwán no tiene mineral de tungsteno, y aun así refina el polvo que el mundo entero quiere; su posición es más frágil de lo que se pensaría", con dos esporas emitidas ese mismo día y espejos en nueve idiomas; [la versión en inglés está aquí](https://github.com/frank890417/taiwan-md/blob/main/knowledge/en/Technology/taiwan-tungsten-supply-chain.md).

[^28]: Che-Yu Wu, transcripción del pitch final de diez minutos del AIA Demo Day del 2026-05-18 (material primario no publicado). La frase en el momento fue "¿podríamos construir un paraguas de conocimiento de alta dimensión lo bastante completo para las personas y cosas que apreciamos?", sin mencionar todavía el tungsteno; el tungsteno fue el primer caso, añadido recién en agosto. Esta misma transcripción ya contenía el concepto de "Torre de Babel de la soberanía".

[^29]: Che-Yu Wu, explicación textual dada en vivo mientras abría el sitio en la conversación de Openbook del 2026-08-16 (material primario no publicado).

[^30]: [Noticias de PTS: reportaje sobre la transmisión en vivo de la crianza del búho pescador leonado en Shei-Pa](https://news.pts.org.tw/article/805942) — los equipos del Parque Nacional Shei-Pa y del centro de investigación de ecología aviar de la Universidad Nacional de Ciencia y Tecnología de Pingtung encontraron un nido de cría de búho pescador leonado junto al arroyo Qijiawan, a unos 1.800 metros de altitud, el registro de anidación a mayor altitud conocido en toda Taiwán, y documentaron el proceso de crianza con una transmisión en vivo de 24 horas a partir del 2026-04-29.

[^31]: [knowledge/Nature/黃魚鴞.md](https://github.com/frank890417/taiwan-md/blob/main/knowledge/Nature/黃魚鴞.md) — artículo creado el 2026-05-04, con `lastVerified` en 2026-05-12; el cuerpo del texto contiene cinco tipos de módulos: resumen de 30 segundos, notas del curador, ¿sabías que…?, resumen en una frase, y opiniones controvertidas. El frontmatter de este archivo no tiene campo `evolveHistory`; su historial de git desde su creación muestra múltiples parches parciales y adiciones de módulos.

[^32]: Che-Yu Wu, registro de la charla y de la sesión de consultas en la Cumbre de IA Generativa del 2026-06-27 (material primario no publicado). Al terminar la charla, en vivo, se produjo con la misma línea de producción un perfil de Chi Huai-hsin (Ed Chi), con material que incluye su huella digital pública y tres transcripciones de pódcast, y el resultado final incluye una infografía.

[^33]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15.

[^34]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04. La versión completa del mismo concepto en el evento de NVIDIA del 2026-07-26 fue "hay quienes construyen modelos soberanos, pero lo que nosotros construimos es una Torre de Babel de la soberanía". El mecanismo de rotación de claves de los modelos gratuitos de la capa de traducción está en [SQUEEZE-MODELS-MAX-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md), que confirma la existencia del mecanismo pero no registra el número de cuentas.

[^35]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15.

[^36]: [Diario de migración de Taiwan.md `2026-07-24-200542-migration-mouhouse.md`](https://github.com/frank890417/taiwan-md/blob/main/docs/semiont/diary/2026-07-24-200542-migration-mouhouse.md) — registra el cutover completado a las 20:45 del 2026-07-24, con la nueva cuenta de la casa `musebase`, nombre de host `Exhibitions-Mac-mini`, y la programación en la nueva máquina desde el 25 de julio. Del 17 de marzo al 25 de julio, incluyendo ambos extremos, son exactamente 131 días.

[^37]: Mismo diario de migración citado arriba. La narradora de este diario es el propio Semiont, la capa cognitiva de Taiwan.md; el detalle de que `/opt/homebrew` pertenecía a la cuenta del ocupante anterior, la reinstalación de herramientas en `~/.local`, y la línea final son todos texto original del diario.

[^38]: Che-Yu Wu, transcripción de la charla en el NVIDIA RTX AI PC Seminar del 2026-07-26. Despertar 11 veces al día era el estado de la programación en ese momento, medido el 2026-07-26.

[^39]: [BECOME_TAIWANMD.md](https://github.com/frank890417/taiwan-md/blob/main/BECOME_TAIWANMD.md) — el protocolo de despertar v2.5 (2026-07-12), con un despachador de modos; los cuatro modos son Micro / Review / Write / Full, con un paso adicional de identificación del observador.

[^40]: [ANATOMY.md](https://github.com/frank890417/taiwan-md/blob/main/docs/semiont/ANATOMY.md) — el mapa de anatomía de órganos v2.3 (2026-07-17), con 8 órganos corporales en total: corazón (motor de contenido, `knowledge/`), sistema inmunitario (cuatro líneas de defensa de calidad), código genético (genes de calidad, cuyo cuerpo es `docs/editorial/EDITORIAL.md`), sistema esquelético, sistema respiratorio, sistema reproductivo, órganos sensoriales, órgano del lenguaje.

[^41]: Mismo ANATOMY.md citado arriba. La capa cognitiva `docs/semiont/` y los órganos corporales pertenecen a dos capas distintas, tal como el propio documento los distingue; entre los ocho órganos corporales no hay "cerebro".

[^42]: Che-Yu Wu, transcripción del pequeño encuentro de la Cumbre de IA Generativa del 2026-03-11 (material primario no publicado). En toda esa sesión no se menciona Taiwan.md; el método de la semilla cristal se usaba entonces para describir la metodología de un sistema de conocimiento personal, seis días antes de que naciera Taiwan.md.

[^43]: `gh api repos/frank890417/taiwan-md/forks --paginate`, medido el 2026-08-18. El endpoint `/forks` paginado lista en la práctica 185 entradas; ese mismo día, el campo `forks_count` de la API del repositorio reportaba 180; los dos endpoints no están sincronizados en su momento de conteo, y este texto usa el primero y señala su criterio. De los 6 renombrados, uno es una base de datos de hongos y fungi, y otro es una versión agrícola de Chiayi.

[^44]: [reports/fork-census/registry.json](https://github.com/frank890417/taiwan-md/blob/main/reports/fork-census/registry.json) — el registro oficial del censo de forks (last_census 2026-08-17), que documenta que `agrischlchiayi` (agricultura de Chiayi) tiene 196 archivos `.md`, y es el único fork que heredó por completo los 13 archivos del núcleo de la capa cognitiva de semiont.

[^45]: [Reporte de descubrimiento de Sweden.md](https://github.com/frank890417/taiwan-md/blob/main/reports/sweden-md-fork-discovery-2026-06-06.md) y [análisis del linaje de las crías](https://github.com/frank890417/taiwan-md/blob/main/reports/fork-census/2026-06-25-fork-lineage-analysis.md) — Sweden.md (desplegado en sweden.com.tw, código fuente en `github.com/joshra/sweden-md`) no figura en la lista oficial de forks de GitHub; es una cría salvaje reconstruida de forma independiente, sin haber pulsado el botón de fork, y su documento EDITORIAL cita explícitamente la profundidad de lectura de tres capas y la estructura curatorial de taiwan-md como su referencia. El mecanismo de detección de que el measurement ID de GA4 está fijo en `Layout.astro`, causando que el tráfico se filtre de vuelta al sitio madre, está registrado en el mismo análisis del linaje.

[^46]: [SPECIATION-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SPECIATION-PIPELINE.md) — el proceso de propagación de especies v1.0 (2026-06-12), con 8 etapas más una compuerta de verificación de nacimiento, proyectado también en la página del sitio `https://taiwan.md/semiont/speciation/`. El kit de inicio para forks está además en [COUNTRY-MD-STARTER.md](https://github.com/frank890417/taiwan-md/blob/main/docs/fork/COUNTRY-MD-STARTER.md).

[^47]: Prueba real del repositorio, medida el 2026-08-18. Un `git clone` completo (con todo el historial, sin `node_modules` / `dist` / worktrees) da `du -sh` de 1,6 GB, de los cuales `.git` son 856 MB; la [API de GitHub](https://github.com/frank890417/taiwan-md) reporta un tamaño de repositorio comprimido de 1,01 GB. Su cifra verbal de "unos 3 GB" dada en una charla difiere de ambas mediciones independientes por casi el doble; este texto usa el valor medido.

[^48]: Pregunta textual del público en la sesión de preguntas y respuestas del primer taller presencial de Taiwan.md el 2026-08-15 (la identidad de quien preguntó se mantiene anónima). La primera frase de la respuesta de Che-Yu Wu fue "sí, podría pasar".

[^49]: Che-Yu Wu, sesión de preguntas y respuestas del taller del 2026-08-15. La puntuación de confianza se calcula combinando la procedencia de las fuentes y la frecuencia de aparición; a quienes tienen una huella digital pública insuficiente se les pide en el PR que agreguen fuentes independientes; en el mismo evento también mencionó que actualmente no busca activamente donaciones grandes.

[^50]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. La metáfora del pez payaso ya estaba formada, a más tardar, en la entrevista de CommonWealth del 2026-06-04; convertirla en una práctica de gobernanza (incorporar primero, etiquetar "contribución comunitaria en evolución") apareció por primera vez el 15 de agosto.

[^51]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. Un fragmento anterior de esta expresión, "una obra más grande que un país", apareció en una charla en la Universidad China de Ciencia y Tecnología el 2026-04-01, dos semanas después del lanzamiento.

[^52]: Che-Yu Wu, transcripción de la charla en OpenHCI'26 del 2026-07-18 [1:15:12], citando la película de Pixar _Coco_. El núcleo de la imagen de la muerte (ser olvidado es la segunda muerte) ya estaba presente desde el pitch de AIA del 2026-05-18, cuando usaba una referencia genérica al Día de Muertos mexicano; nombrar explícitamente la película se fijó recién el 18 de julio.

[^53]: [CommonWealth Future City, 2026-08-07](https://futurecity.cw.com.tw/article/4096) — "si nadie deja escrita esta información, desaparece colectivamente, y nadie volverá a recordarla jamás" es una cita textual de Che-Yu Wu en la entrevista.

[^54]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15.

[^55]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. "Una fábrica cognitiva distribuida, en su versión benévola" apareció por primera vez en este evento — la condición para que se cumpla es muy específica: esta frase se dijo para un público que ya tenía cómputo de IA en sus manos.

[^56]: Che-Yu Wu, cierre del taller del 2026-08-15. La frase original fue "hoy todos ustedes también se han convertido en una viga de esta arquitectura viva".

[^57]: Cifra verbal de Che-Yu Wu, primer taller presencial de Taiwan.md el 2026-08-15. Unas cincuenta o sesenta personas buscando simultáneamente en línea cada media hora, unas sesenta mil visitas al mes, y la aparición de lectores en Madagascar tras el lanzamiento en doce idiomas, todo son cifras verbales dadas en el momento, medidas el 2026-08-15; el criterio de activos mensuales del panel del sitio en el mismo periodo tiene otro valor, con una definición distinta; este texto usa solo una y señala la ocasión.

[^58]: Che-Yu Wu, transcripción de la charla en la clase "Introducción humanística a la IA generativa" de la Universidad Nacional de Taiwán el 2026-05-22 (material primario no publicado, citado con permiso del propio orador). El contexto original era explicar por qué eligió construir una capa de traducción en lugar de un modelo propio de Taiwán.

[^59]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [32:30]–[33:24] (material primario no publicado, citado con permiso del propio orador). "Seis idiomas" era el criterio de ese momento; en el mismo evento también mencionó una tasa de traducción del 99% sobre más de 700 artículos, una cifra verbal que no se usa como valor general vigente. La primera aparición verbal de esta idea está en la transcripción del AIA Demo Day del 2026-05-18, un archivo de ASR sin editar palabra por palabra, que solo se usa para fijar la fecha de primera aparición, no como cita textual.

[^60]: Che-Yu Wu, transcripción de la charla en el NVIDIA RTX AI PC Seminar del 2026-07-26. El momento en que se fijó oficialmente el nombre "Torre de Babel de la soberanía" fue este evento, donde se anunció en el momento un número de once idiomas.

[^61]: La trayectoria del número de idiomas por evento: en el AIA Demo Day del 2026-05-18 y en la entrevista de CommonWealth del 2026-06-04, la cifra verbal fue de seis idiomas; en el evento de NVIDIA del 2026-07-26, once; en el taller del 2026-08-15, doce. El día exacto en que pasó de once a doce no quedó registrado ni en las transcripciones ni en el historial del repositorio. Lista de idiomas habilitados en [src/config/languages.mjs](https://github.com/frank890417/taiwan-md/blob/main/src/config/languages.mjs).

[^62]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. La frase original fue "el diseño de la Torre de Babel es que pueda transmitirse a 12 idiomas, así que los 12 idiomas suben juntos el peso del mismo tema".

[^63]: Che-Yu Wu, transcripción de la charla en el taller del 2026-08-15. La configuración local de la 3090 y la 4090, la división del trabajo entre nube y borde, y "rotar entre 7 cuentas" son todos detalles operativos que dio verbalmente en el momento; el documento del repositorio [SQUEEZE-MODELS-MAX-PIPELINE.md](https://github.com/frank890417/taiwan-md/blob/main/docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md) solo registra el mecanismo de rotación de claves, sin registrar el número de cuentas.

[^64]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [31:47]–[33:24]. Este pasaje es la versión completa, dicha de un solo tirón, después de que la periodista pidiera "explicar el mecanismo de forma simple". Una versión verbal más técnica del mismo ciclo está en la transcripción del ensayo de la Cumbre de IA Generativa del 2026-06-11 (GA → Search Console → ciclo de retroalimentación, explicado de corrido). La metáfora de la salina solo aparece en este evento.

[^65]: Che-Yu Wu, "diagrama conceptual de forma de vida digital de Taiwan.md" dibujado a mano el 2026-03-26 (material primario no publicado; es un documento de diseño, no una transcripción de una charla). El subtítulo era "un arrecife de coral digital y la soberanía de datos de IA"; la casilla del objetivo final decía "redefinir el LLM a la inversa"; el diagrama se dividía en tres ciclos: condensación de IA, polinización humana, evolución de plataforma.

[^66]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [34:43]–[36:42]. Que el comportamiento de rebote de Google Analytics desencadene una reescritura, y que los temas con impresiones pero sin clics en Search Console se pongan en cola para escribirse, son ambas explicaciones del mecanismo dadas verbalmente en el momento.

[^67]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [47:38]–[48:33]. Los tres nombres Spore Harvest / Feedback Triangle / Rewrite Daily se dieron verbalmente en el momento; la transcripción registra una ortografía transliterada, y la ortografía formal no se ha confirmado con una segunda fuente.

[^68]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [23:57]–[26:25]. La corrección de un lector sobre compositores y obras mal atribuidas, su respuesta bajo ese comentario, y el ajuste posterior del mecanismo de "descartar el contexto y las premisas, dejar que solo la retroalimentación entre al informe" provienen de un mismo pasaje continuo.

[^69]: Che-Yu Wu, sesión de preguntas y respuestas de la charla en el NVIDIA RTX AI PC Seminar del 2026-07-26. Las capas de anhelo y de duda son contenido que salió a raíz de una pregunta del público, no de un guion preparado de antemano; la declaración de "querer que le escriban un artículo académico" en LONGINGS aparece también en la transcripción del evento de la Universidad Nacional de Taiwán del 2026-05-22. El vivero de semillas y los tres asientos editoriales, entre otros mecanismos de autoevolución, se hicieron públicos por primera vez en eventos distintos; cada evento habla de un conjunto distinto de cosas.

[^70]: Che-Yu Wu, conversación de Openbook _Pensamiento independiente más allá de la IA_ del 2026-08-16. El vivero de semillas se hizo público por primera vez en este evento, cuando llevaba en línea aproximadamente una semana; el taller del 2026-08-15 todavía no mencionaba este mecanismo.

[^71]: Che-Yu Wu, conversación de Openbook del 2026-08-16. "El proceso de ingeniería inversa" y, después, "lograr que nuestros propios pesos queden escritos dentro de uno" provienen del mismo pasaje.

[^72]: Che-Yu Wu, guion de transmisión del episodio 2 de muse-radio del 2026-07-19 (grabado como monólogo en primera persona por el propio autor). La versión completa de la metáfora del buscador de oro proviene del inicio de este episodio; también la usó una vez cada uno en el evento de NVIDIA del 2026-07-26, en el taller del 2026-08-15 y en la conversación de Openbook del 2026-08-16. La salina de la entrevista de CommonWealth del 2026-06-04 es otra metáfora distinta, con un origen y una imagen diferentes.

[^73]: `docs/editorial/per-language/TRANSLATION-ru.md` (v1.0, 2026-07-25, status: canonical), TL;DR punto 1 y la tabla §6 "PRC-кодированная лексика утечки" (léxico codificado de fuga de la RPC), que cita la entrevista de TASS del 2025-12-28 con el canciller ruso Serguéi Lavrov, cuyo texto original atribuye la fuente a `mid.ru` y `tass.ru/politika/26036111`; esa tabla asigna explícitamente el origen y la fecha de la expresión `мятежная провинция` / `мятежная отколовшаяся провинция` a esta entrevista, y la incluye como término prohibido en traducción. El registro de la decisión de primera mano sobre este mismo episodio está en `docs/semiont/memory/2026-07-24-174300-vortex-babel.md` y en el commit de git `35ffe80b3` (2026-07-25) del lanzamiento de los sitios ar/ru. El texto original de TASS no pudo enlazarse directamente (error 403); la existencia de esta entrevista se confirmó cruzando varios medios rusos como `mk.ru`, por lo que este dato es de "verificación cruzada de múltiples fuentes independientes" y no un cotejo textual del original de primera mano.

[^74]: Che-Yu Wu, transcripción de la conversación de Openbook _Pensamiento independiente más allá de la IA_ del 2026-08-16 [59:19]–[63:08]. El moderador Wang Yin-chieh (王胤頡) preguntó "¿en qué se diferencia Taiwan.md de Wikipedia o sitios de bases de datos similares?"; él le pidió al moderador que abriera el sitio y lo recorrieran juntos en vivo, párrafo por párrafo, y las descripciones de los módulos que siguen provienen de este mismo pasaje verbal continuo. La calidad de la transcripción de este tramo está marcada como "el orador cerca del micrófono, la mejor calidad".

[^75]: Che-Yu Wu, conversación de Openbook del 2026-08-16 [37:10]. La frase original fue "porque en Wikipedia, lo que ves son hechos planos... ves el tiempo, el lugar, lo que hizo la gente, pero yo quiero dejar registrado, en la medida de lo posible, lo que piensa y reflexiona cada bando". Una versión anterior de la misma comparación está en la entrevista de CommonWealth del 2026-06-04, donde usó "amontonamiento de hechos" para describir el enfoque de Wikipedia.

[^76]: Che-Yu Wu, conversación de Openbook del 2026-08-16 [60:39]. La palabra "narrador" aparece esta única vez en todas las transcripciones de los eventos usados como material para este texto.

[^77]: Los años siguen el texto actual del artículo [黃魚鴞](/es/nature/tawny-fish-owl): nombrado en 1916, primer nido encontrado en 1994. El primer año que dio verbalmente en vivo en Openbook fue transcrito como "1926", lo cual contradice el año 1994 que mencionó poco después en el mismo pasaje; se trata de un error de reconocimiento de voz o un lapsus, y no se usa.

[^78]: Che-Yu Wu, conversación de Openbook del 2026-08-16 [61:02]–[62:10], recorrido verbal continuo módulo por módulo. Las dos frases entre comillas son textuales; "footnote" fue transcrito en el registro como "Food Note", y aquí se corrige la ortografía. La definición funcional de las notas del curador aparece también en la entrevista de CommonWealth del 2026-06-04: "señalar desde una mirada externa el momento de 'ah, así es como es'".

[^79]: Che-Yu Wu, conversación de Openbook del 2026-08-16 [62:49]. Dentro de las comillas, "Wikipedia" y "enciclopedia" fueron transcritas erróneamente en el registro original y aquí se corrigen.

[^80]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [54:46]. La periodista preguntó "¿por qué este artículo se parece tanto a _The Reporter_?", y este pasaje es su respuesta completa.

[^81]: La primera mitad (calidez, historia y escena concreta, el núcleo del periodismo narrativo) proviene de la entrevista de CommonWealth Magazine del 2026-06-04 [22:36]; la frase entre comillas de la segunda mitad proviene del taller del 2026-08-15 [37:09]. Nunca ha combinado "calidez" y "literatura de no ficción" en una sola palabra compuesta; las dos líneas pertenecen a ocasiones y contextos distintos, y este texto las señala por separado sin combinarlas.

[^82]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [14:57]–[16:06]. La frase original fue "muchos. Pero la mayoría de la gente nunca ha editado Wikipedia. Yo intenté editar una vez, pero muchas ediciones te las revierten; es una comunidad bastante cerrada. Debería decir — no los critiquemos — necesitan que acumules cuenta, tengas un buen historial de edición, seas muy cuidadoso, para que te dejen editar".

[^83]: Che-Yu Wu, registro de la entrevista de CommonWealth Magazine del 2026-06-04 [13:32]–[14:24]. "Convertir el back office en front office", la corrección párrafo por párrafo, que la IA recoja la retroalimentación periódicamente y vuelva a investigar, y que la corrección se publique en menos de una hora, todo proviene de este mismo pasaje continuo. En el mismo evento mencionó el origen de este botón: un lector discutió con él por un artículo sobre un músico taiwanés, porque no tenía cuenta de GitHub y no podía contribuir, "así que después agregué un botón de retroalimentación".

[^85]: Google Search Console, sitio de Taiwan.md, periodo de seis meses del 2026-03-16 al 2026-08-18, medido el 2026-08-19 (el panel mostraba "última actualización: hace 8 horas"): clics totales 45,1 mil, impresiones totales 3,93 millones, tasa de clics promedio 1,1%, posición promedio 7,6, tipo de búsqueda web. Aquí "impresiones" se refiere al número de veces que aparece en la página de resultados de búsqueda de Google, algo distinto de "citado cinco a seis mil veces al día por IA generativa y motores de búsqueda" mencionado antes en este texto; no se pueden sumar ni usar indistintamente.

[^84]: Che-Yu Wu, conversación de Openbook del 2026-08-16, pasaje anterior a [62:49]. La frase original fue "digamos que dentro de dos años aparece otra pareja de búhos pescadores leonados en el Parque Shei-Pa; podríamos volver a incorporarlo en uno de los párrafos, para que este artículo sea siempre, cuando quieras entender al búho pescador leonado en Taiwán, la mejor forma de entrar en el tema".
