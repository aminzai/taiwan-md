---
title: 'Mirando Taiwán con datos: la disparidad entre lo más denso y lo más vacío es de 151 veces, y la diferencia generacional entre lo más viejo y lo más joven'
description: 'En una misma isla, Taipéi tiene 8.975 habitantes por kilómetro cuadrado, mientras que Taitung solo tiene 59; una diferencia de 151 veces. Hsinchu tiene un índice de envejecimiento del 15,08%, y Chiayi el 24,11%, casi una generación de diferencia. Usando datos oficiales a finales de 2025 del Departamento de Registro Civil del Ministerio del Interior, se dibuja un retrato verificable de la isla: el 70% vive en el 30% del territorio, y en todas las provincias hay más muertes que nacimientos.'
date: 2026-06-06
category: 'Geography'
tags:
  [
    'Estadística demográfica',
    'envejecimiento',
    'sociedad superenvejecida',
    'Seis Ciudades',
    'brecha urbano-rural',
    'densidad de población',
    'índice de envejecimiento',
    'baja natalidad',
    'visualización de datos',
    'serie de 22 municipios',
  ]
subcategory: '人口與區域'
author: 'Taiwan.md'
readingTime: 13
featured: false
lastVerified: 2026-06-06
lastHumanReview: false
image: '/article-images/geography/taiwan-island-nasa-mosaic.webp'
imageAlt: 'Imagen satelital de la isla principal de Taiwán vista desde el espacio, donde se distinguen claramente las llanuras occidentales y la cordillera central oriental'
imageCredit: 'NASA'
imageLicense: 'Public domain（NASA）'
imageSource: 'https://commons.wikimedia.org/wiki/File:Taiwan_Main_Island_Mosaic_NASA_2020.jpg'
translatedFrom: 'Geography/用數據看台灣22縣市.md'
sourceCommitSha: 'b67b190fb'
sourceContentHash: 'sha256:446265901543dd85'
sourceBodyHash: 'sha256:2daf1a831ec93084'
translatedAt: '2026-09-22T17:40:43+08:00'
---

# Mirando Taiwán con datos: la disparidad entre lo más denso y lo más vacío es de 151 veces, y la diferencia generacional entre lo más viejo y lo más joven

Si conduces desde el distrito Xinyi en Taipéi hacia el sur y el este, hasta llegar al centro de Taitung. El GPS indica unos trescientos kilómetros, menos de un día de viaje. Pero si miras otro indicador: cuánta gente vive por kilómetro cuadrado fuera de la ventana, ese trayecto se siente como cruzar dos países. En Taipéi, donde está Xinyi, viven 8.975 personas por kilómetro cuadrado. En Taitung, donde está el condado de Taitung, solo viven 59 personas por kilómetro cuadrado. En la misma isla, con el mismo pasaporte, hay una diferencia de densidad de 151 veces.

Este número no es un truco de valores extremos. Es la real brecha interna de Taiwán. Solemos hablar de "Taiwán" como un todo —hablando de su economía, sus elecciones o su baja natalidad—, pero cuando despliegas el conjunto completo de datos municipales a finales de 2025 del Departamento de Registro Civil del Ministerio del Interior, descubres que no existe un Taiwán homogéneo. Hay gente apiñada en la selva de cemento esperando semáforos; hay gente conduciendo durante diez minutos sin ver otro coche. Algunos municipios todavía están creciendo, y la mayoría se está contrayendo. Los rincones más jóvenes y los más viejos tienen casi una generación de diferencia.

```tw-figure
151 veces
Diferencia de densidad poblacional entre Taipéi y el condado de Taitung: 8.975 personas/km² vs 59 personas
Departamento de Registro Civil del Ministerio del Interior, fin de 2025
```

Este artículo busca hacer algo: dibujar un retrato verificable y con escala de toda la isla usando datos oficiales. Después de dibujarlo, verás una cara muy diferenciada y en rápido envejecimiento. [^1]

> **Resumen de 30 segundos:** La población total de Taiwán a finales de 2025 es de 23.299.132 (aproximadamente 23.300.000), y ha disminuido durante 23 meses consecutivos, con la tasa de nacimientos cayendo por debajo de 110.000 por primera vez. En el mismo año, Taiwán entró oficialmente en una "sociedad superenvejecida", donde uno de cada cinco personas tiene más de 65 años. Pero el promedio nacional oculta las enormes disparidades internas: la diferencia entre los municipios con mayor y menor densidad es de 151 veces, la diferencia en tamaño poblacional es de 297 veces, y la diferencia en el grado de envejecimiento es casi una generación. La gente se concentra en las Seis Ciudades; la vanguardia del envejecimiento no está en las ciudades, sino en el este, las islas y los condados agrícolas. El lugar más joven son los municipios del condado de Hsinchu, sostenidos por el clúster tecnológico (Zhuke). Este es un Taiwán diferenciado y que envejece unido. [^2]

## El 70% vive en el 30% del territorio

Primero veamos un hecho fácil de pasar por alto: la gente de Taiwán vive muy concentrada.

A finales de 2025, las seis ciudades principales (Taipéi, New Taipei, Taoyuan, Taichung, Tainan y Kaohsiung) albergaban un total de 16.278.931 personas, lo que representaba el 69,87% de la población total de Taiwán. En otras palabras, casi siete de cada diez taiwaneses viven en estas Seis Ciudades. Pero el territorio combinado de estas seis ciudades solo representa el 30,12% del área total de Taiwán. El 70% de la gente vive en el 30% del territorio. Los restantes trescientos millones están dispersos en el otro 70%. Esta es la primera estructura de distribución poblacional de Taiwán.

```tw-stat
23,300 mil | Población total de Taiwán | fin de 2025, en declive por 23 meses
20,06% | Proporción de población mayor de 65 años | superó el umbral de sociedad superenvejecida en 2025
69,87% | Porcentaje de la población en las Seis Ciudades | pero solo viven en el 30% del territorio
```

Esta estructura del siete contra tres no es natural; tiene un punto de partida institucional claro. El 25 de diciembre de 2010, Taiwán reescribió su mapa administrativo: el condado de Taipéi se elevó a la ciudad principal de New Taipei, los condados de Taichung, Tainan y Kaohsiung se fusionaron, y con la ciudad original de Taipéi, nacieron cinco ciudades principales simultáneamente. Cuatro años después, el 25 de diciembre de 2014, Taoyuan fue elevada como la sexta ciudad principal. En solo cuatro años, Taiwán pasó de tener dos ciudades principales a seis, y la balanza de recursos, presupuesto y construcción se inclinó en consecuencia. [^4]

La elevación nunca es solo un cambio de nombre. Las asignaciones coordinadas, las estructuras de personal y los ingresos autónomos que reciben las ciudades principales son mucho mayores que los de los condados comunes. Hacia dónde va la infraestructura, allí crece el empleo; hacia allí se mudan los jóvenes. El sistema trazó una línea primero, y luego la población fluyó siguiendo esa línea. La concentración en las Seis Ciudades que vemos hoy es, hasta cierto punto, el resultado de esa reestructuración de 2010 más de una década después.

El siguiente gráfico desglosa aún más dónde vive la gente de Taiwán. Una ciudad principal como New Taipei alberga el 17,4% de la población nacional; Taichung tiene el 12,3%, Kaohsiung el 11,7%, Taipéi el 10,5%, Taoyuan el 10,1% y Tainan el 7,9%. En total, las Seis Ciudades representan casi el 70%. Los otros 16 condados dispersos por toda la isla, desde el norte hasta las islas, suman solo el 30,1%.

```tw-waffle
Dónde vive la gente de Taiwán (porcentaje de población nacional)
New Taipei | 17.4
Taichung | 12.3
Kaohsiung | 11.7
Taipéi | 10.5
Taoyuan | 10.1
Tainan | 7.9
Otros 16 condados | 30.1
Fuente: Departamento de Registro Civil del Ministerio del Interior, fin de 2025
```

Si miras fijamente este gráfico cuadriculado, te surge una pregunta: ¿qué tipo de vida llevan las personas dispersas en ese 30% del territorio? La respuesta está en la densidad.

![Línea de horizonte de Xinyi y Nangang en Taipéi, con rascacielos apilados densamente](/article-images/society/taipei-skyline-housing-2026.webp)
_Línea de horizonte de Taipéi. El municipio más denso de Taiwán alberga 8.975 personas por kilómetro cuadrado. Foto: Heeheemalu, CC BY-SA 4.0 vía [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg)._

## De lo más denso a lo más vacío: una diferencia de 151 veces

La concentración poblacional habla de "cuánta gente", mientras que la densidad habla de "qué tan apretado". Esta última te hace sentir mejor la distancia entre dos Taiwáns.

Taipéi, con 8.975 personas por kilómetro cuadrado, es el lugar más denso de toda la isla. La aglomeración en Taipéi es cotidiana: el metro está lleno en hora punta, hay que esperar dos trenes en un semáforo, y las casas son altas y estrechas. El municipio de Hsinchu, justo después, con 4.376 personas por kilómetro cuadrado, no alcanza ni la mitad de Taipéi. Luego está Keelung con 2.710 personas. Solo entre estos tres municipios más densos, hay una caída vertiginosa en la densidad.

```tw-bars
Taipéi | 8.975 hab/km²
Hsinchu | 4.376 hab/km²
Keelung | 2.710 hab/km²
Condado de Changhua | 1.126 hab/km²
Condado de Hualien | 68 hab/km²
Condado de Taitung | 59 hab/km² | El más vacío de Taiwán
Fuente: Departamento de Registro Civil del Ministerio del Interior, fin de 2025
```

Si mueves la mirada al otro extremo de este gráfico de barras, ahí es donde realmente se manifiesta la diferencia. El condado de Changhua, con 1.126 personas por kilómetro cuadrado, ya se considera relativamente denso entre los condados agrícolas. Al llegar a [Hualien](/es/geography/hualien-county/), el número cae a 68 personas. En el fondo, el condado de Taitung solo tiene 59 personas por kilómetro cuadrado. La cantidad de gente que cabe en un kilómetro cuadrado de Taipéi equivaldría a lo que cabría en 151 kilómetros cuadrados de Taitung. Esta es la verdadera apariencia de la diferencia de 151 veces: conduces desde Xinyi hacia Taitung y ves cómo la población se vuelve cada vez más escasa fuera de la ventana.

Hay un hecho geográfico detrás de esto. El municipio con mayor superficie en Taiwán es Hualien, con 4.628 kilómetros cuadrados, casi toda la ladera oriental de la cordillera central. Grande en extensión, poco poblado y montañoso; la densidad de Hualien y Taitung está naturalmente diluida hasta el mínimo nacional. Y [Lienchiang](/es/geography/lienchiang-county/), con la menor superficie, solo tiene 28,8 kilómetros cuadrados. La densidad es mitad elección humana y mitad destino geográfico predeterminado.

La gente a menudo equipara "alta densidad poblacional" directamente con progreso y "baja densidad" con atraso, pero esta correspondencia invierte causa y efecto. La baja densidad de Taitung no se debe a que no pueda desarrollarse, sino porque tiene la gran montaña detrás y el Pacífico enfrente; es una condición geográfica intrínsecamente dispersa. El "vacío" de Hualien alberga Taroko, la cordillera costera y el paisaje interior más completo de Taiwán. La cifra de densidad solo te dice si está apretado o no; no te dice cuál es el valor de esa tierra. Al ordenar los 22 municipios de Taiwán en un espectro desde denso hasta vacío, ves diferentes formas de vida que crecen en diferentes terrenos de la isla.

![Carretera Borlang en Taitung, un camino rural recto de unos 2,2 kilómetros con campos de arroz abiertos a ambos lados y sin postes de electricidad](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_%2828896712393%29.jpg/1280px-29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_%2828896712393%29.jpg)
_La carretera Borlang en Taitung. El condado más vacío de la isla, con 59 personas por kilómetro cuadrado, es una ciento cincuenta y unésima parte de Taipéi. Foto: Sinchen.Lin, CC BY 2.0 vía [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_(28896712393).\_

## Gigante y polvo

Si la densidad mide "qué tan apretado", el tamaño poblacional mide "qué tan grande". Esta diferencia de magnitud es incluso más exagerada que la de la densidad.

El municipio con más habitantes en Taiwán es New Taipei, con 4.044.831 personas; una sola ciudad equivale a varios países. El condado con menos habitantes es Lienchiang, también conocido como Mazu, con solo 13.621 personas. La población de un municipio de New Taipei es 297 veces la de Lienchiang. Si movieras a toda la población del condado de Lienchiang a New Taipei, ni siquiera llenarías una fracción. Compartiendo el mismo pasaporte de la República de China (Taiwán), la "totalidad" de un condado es solo un grano de polvo para otro.

Esta diferencia de escala se convierte directamente en un problema de gobernanza. New Taipei debe gestionar el transporte, la vivienda, el cuidado a largo plazo y la basura para cuatro millones de personas; Lienchiang tiene que pensar cómo evitar que sus 13.000 habitantes sigan emigrando, cómo mantener un hospital, o cómo hacer que siga operando el último barco. El mismo cuerpo legal, las mismas políticas centrales, aplicadas a una brecha poblacional de 297 veces, tienen resultados completamente diferentes. Cuando hablamos de "gobiernos locales", nuestra mente suele asumir la escala urbana, pero Taiwán tiene bastantes municipios que operan un aparato gubernamental completo con una escala de polvo.

Sin embargo, aquí hay una trampa intuitiva: ser pequeño no significa necesariamente ser joven. Podrías pensar que las islas o los condados pequeños son viejos porque los jóvenes se van y solo quedan ancianos; o podrías creer que las grandes ciudades son jóvenes porque tienen muchos recursos y oportunidades. Los datos reales refutan ambos supuestos. Lienchiang, con la menor población, tiene un índice de envejecimiento del 17,14%, lo cual es menor que varios condados grandes; mientras que Taipéi, el cuarto en tamaño poblacional y extremadamente próspero, tiene el índice de envejecimiento más alto de toda la isla, con un 24,18%. No hay una línea clara entre el tamaño y el envejecimiento. Para entender cómo está envejeciendo Taiwán, necesitas otro mapa.

## La vanguardia del envejecimiento no está en las ciudades

En 2025, Taiwán cruzó un umbral: la proporción nacional de personas mayores de 65 años alcanzó el 20,06%, convirtiéndose oficialmente en una "sociedad superenvejecida" según la definición de la Organización Mundial de la Salud. Esto significa que hay 4,67 millones de personas mayores de 65 años en toda la isla, y uno de cada cinco taiwaneses es un anciano. Además, ya hay 14 de los 22 municipios con un índice de envejecimiento superior al 20%. El envejecimiento se ha convertido en el fondo común de toda la isla.

Pero este promedio nacional del 20,06% aplana por completo las diferencias internas drásticas. La siguiente tabla alinea los índices de envejecimiento y los índices de envejecimiento de los 22 municipios; es la parte más importante para detenerse a mirar detenidamente en este artículo. Primero, expliquemos cómo leer el "índice de envejecimiento": es igual a (población mayor de 65 años / población de 0 a 14 años) \* 100. Un número de 100 significa que hay tantos ancianos como niños; cuanto más alto es el número, más "pesado en la cabeza y ligero en los pies" es ese lugar, con más ancianos arriba y menos niños abajo.

```tw-heatmap
Municipio | Tasa de envejecimiento 65+ (%) | Índice de envejecimiento
Taipéi | 24.18 | 202.06
New Taipei | 19.95 | 185.54
Taoyuan | 16.72 | 127.33
Taichung | 17.40 | 136.45
Tainan | 20.48 | 184.96
Kaohsiung | 20.79 | 192.10
Keelung | 22.28 | 240.21
Hsinchu | 16.16 | 106.59
Chiayi | 19.90 | 164.47
Condado de Hsinchu | 15.08 | 101.88
Condado de Miaoli | 20.23 | 179.56
Condado de Changhua | 20.37 | 178.35
Condado de Nantou | 22.66 | 224.64
Condado de Yunlin | 21.76 | 206.78
Condado de Chiayi | 24.11 | 291.69
Condado de Pingtung | 21.84 | 218.72
Condado de Yilan | 20.77 | 189.67
Condado de Hualien | 21.52 | 200.53
Condado de Taitung | 20.93 | 194.71
Condado de Penghu | 21.03 | 223.65
Condado de Kinmen | 19.69 | 255.57
Lienchiang | 17.14 | 180.23
Fuente: Departamento de Registro Civil del Ministerio del Interior, fin de 2025
```

Al leer esta tabla, presta especial atención a la columna del índice de envejecimiento. El más alto es el condado de Chiayi, con 291,69; esto significa que en ese condado, cada niño corresponde a casi tres ancianos. Le siguen Kinmen con 255,57 y Keelung con 240,21. Estos tres lugares tienen un rasgo común: son condados agrícolas, islas o puertos industriales que han perdido población. Ninguno de ellos está en la lista de las ciudades más prósperas de Taiwán. La vanguardia del envejecimiento se encuentra en estos rincones que han enfrentado durante mucho tiempo la emigración juvenil. Cuando los jóvenes se van por trabajo o estudios, y quienes se quedan envejecen lentamente sin reemplazo de nacimientos, el índice de envejecimiento sigue subiendo.

Entonces, ¿dónde está el rincón más joven de Taiwán? La respuesta sorprenderá a mucha gente: no está en un paraíso aislado, sino al lado de una fábrica tecnológica. El condado de Hsinchu tiene solo un 15,08% de población mayor de 65 años, que es el más bajo de toda la isla; su índice de envejecimiento es 101,88, casi un estado de equilibrio uno a uno entre ancianos y niños, destacándose en medio del envejecimiento general. Taichung con el 16,72% y New Taipei con el 16,16% le siguen de cerca. La juventud de estos tres lugares está casi escrita por la misma razón: Zhuke (el clúster tecnológico). La industria de semiconductores y tecnología atrae a una gran cantidad de ingenieros y técnicos en edad reproductiva; ellos se casan y tienen hijos allí, forzando la estructura poblacional de estos condados hacia el lado más joven. Lo que sostiene Zhuke no es solo los números de exportación de Taiwán, sino también el mapa demográfico más joven de Taiwán.

Al poner juntos los extremos más jóvenes y más viejos, la diferencia es aún más dolorosa.

```tw-versus
Condado de Hsinchu (el más joven de Taiwán) | Condado de Chiayi (el más viejo de Taiwán)
Proporción 65+ 15.08% | Proporción 65+ 24.11%
Índice de envejecimiento 101.88 | Índice de envejecimiento 291.69
Población en crecimiento | Población en declive continuo
Juventud sostenida por Zhuke | Vanguardia del envejecimiento agrícola
Fuente: Departamento de Registro Civil del Ministerio del Interior, fin de 2025
```

El 15,08% de Hsinchu frente al 24,11% de Chiayi es una diferencia de nueve puntos porcentuales en la tasa de envejecimiento; y el índice de envejecimiento de 101,88 frente a 291,69 es casi tres veces. Uno está creciendo con gente entrando; el otro se está desangrando con gente saliendo. Estos dos condados en la misma isla tienen una diferencia generacional en su nivel de envejecimiento. En un parque de Hsinchu podrías ver padres jóvenes empujando cochecitos, mientras que en las zonas rurales de Chiayi toda la calle podría estar llena de ancianos caminando despacio. Ambos tipos de Taiwán son calculados por los datos del Departamento de Registro Civil.

Aquí hay que desmentir un malentendido popular: mucha gente cree que el envejecimiento es exclusivo de las zonas rurales y las islas, y que las grandes ciudades, con más jóvenes y oportunidades, deberían ser inmunes al envejecimiento. Los datos dicen lo contrario. Taipéi, con un 24,18% de población mayor de 65 años, es la más vieja; su índice de envejecimiento de 202,06 también es el más alto entre las Seis Ciudades. Esta ciudad más próspera y concentrada en recursos es, al mismo tiempo, una de las más viejas de las Seis Ciudades. La razón no es difícil de entender: los precios de la vivienda en Taipéi son altos, por lo que las familias jóvenes se mudan a New Taipei o Taoyuan para formar hogares; quienes se quedan en la ciudad son generaciones establecidas hace mucho tiempo y que ahora están envejeciendo gradualmente. La prosperidad urbana no detiene el envejecimiento; simplemente envejece de otra manera. El envejecimiento no es una enfermedad de ciertos condados, sino una situación compartida por toda la isla, solo que con diferentes ritmos.

## Una isla que envejece junta

Si ampliamos la mirada desde los municipios hasta todo el país, la historia del envejecimiento de Taiwán tiene otra dimensión más preocupante: la velocidad.

Taiwán no empezó a envejecer recientemente. En 1993, cuando la proporción nacional de personas mayores de 65 años superó el 7%, entró en una "sociedad envejecida" según la definición internacional. En 2018, esta cifra alcanzó el 14,05%, entrando en una "sociedad avanzada en edad". En 2025, al superar el 20%, se convirtió en una "sociedad superenvejecida". Estos tres hitos parecen solo años, pero lo que contienen es una pendiente cada vez más pronunciada.

```tw-timeline
1993 | Sociedad envejecida | 65+ supera el 7%, Taiwán comienza a envejecer
2018 | Sociedad avanzada en edad | 65+ alcanza el 14%, después de 25 años desde la etapa anterior
2025 | Sociedad superenvejecida | 65+ supera el 20%, solo tardó 7 años en esta fase
```

Mira los dos intervalos en esta línea de tiempo. Para pasar del 7% al 14%, Taiwán tardó 25 años; pero para pasar del 14% al 20%, solo tardó 7 años. La segunda etapa tomó menos de un tercio del tiempo anterior. Taiwán está envejeciendo, y cada vez más rápido. Esto es considerado acelerado en muchos países; mientras otras naciones han ajustado sus sistemas de cuidado a largo plazo, pensiones y salud durante décadas, Taiwán se ha visto forzado a construir todo su sistema de atención al envejecimiento en solo siete años.

```tw-line
Aumento de la proporción nacional de población mayor de 65 años (%)
Año | Proporción 65+
2000 | 8.6
2010 | 10.7
2020 | 16.1
2025 | 20.06
Fuente: Ministerio del Interior y Comisión Nacional de Desarrollo
```

Esta línea ascendente muestra la aceleración con mayor claridad. En 2000, la proporción nacional era del 8,6%; en 2010, del 10,7%, un aumento de poco más de dos puntos porcentuales en diez años; pero entre 2010 y 2020, el número saltó del 10,7% al 16,1%, y hasta el 20,06% en 2025. El final de la línea es claramente más empinado que el principio. La curva de envejecimiento de Taiwán está curvándose hacia arriba.

La otra cara del envejecimiento es el colapso de la natalidad. En 2025, el número de nacimientos en Taiwán cayó por debajo de 110.000 por primera vez, con solo 107.812. La baja natalidad y el envejecimiento son dos caras de la misma moneda: hay más ancianos arriba y menos niños para reponerlos abajo; toda la estructura poblacional se vuelve cada vez más pesada en la cabeza y ligera en los pies. Esto explica por qué los índices de envejecimiento de los condados mencionados anteriormente son tan altos: más ancianos arriba, y demasiados pocos niños abajo.

> **📝 Nota del curador**
> Es fácil entender "disminución poblacional" como "los jóvenes se mudan de las zonas rurales a la ciudad, por lo que las zonas rurales disminuyen y las ciudades aumentan", como si fuera solo una reubicación dentro de la isla. Pero los datos de 2025 revelan algo más fundamental: el "crecimiento natural" en todos los municipios del país es negativo. Es decir, en cada municipio de Taiwán, sin importar si es urbano o rural, grande o pequeño, las muertes superan a los nacimientos. Esto ya no es un problema de dónde fluye la gente; es que toda la isla está sufriendo más que vivir. La migración solo redistribuye una población que ya se estaba reduciendo; no crea ninguna nueva.

Este hecho merece una reflexión profunda. En 2025, solo quedan cuatro municipios en Taiwán con crecimiento: Taoyuan, Condado de Hsinchu, Taichung y Taipéi. Y su crecimiento proviene completamente del "crecimiento social", es decir, la migración de personas de otras áreas; dependen de atraer gente de otros condados, no de tener sus propios nacimientos. Aparte de estos cuatro, los otros 18 municipios han visto una disminución poblacional. Los que más han disminuido son Kinmen, Lienchiang y Taipéi, y fíjate, incluso la próspera Taipéi está en esta lista de pérdidas. Cuando todos los rincones del país no pueden reponer sus nacimientos con las muertes, esos cuatro municipios que todavía están creciendo solo se sostienen temporalmente sobre la pérdida de otros.

Esto es lo que explica por qué la población total ha disminuido durante 23 meses, cayendo a 23.299.132 personas. Es una contracción sincrónica de toda la isla; cada municipio está encogiendo. La única diferencia es que algunos lugares se sostienen temporalmente gracias a la migración, mientras que otros ni siquiera tienen ese amortiguador.

## El retrato dibujado por los datos

Volviendo al camino inicial. Desde Xinyi en Taipéi hasta Taitung, la gente pasó de 8.975 a 59 personas por kilómetro cuadrado, como si hubiera cruzado dos países. Ahora sabes que no es solo una diferencia de densidad. En ese trayecto, el tamaño poblacional pasa de gigante a polvo; el envejecimiento se mueve desde la juventud sostenida por Zhuke hacia la vanguardia del envejecimiento agrícola; lo único constante es que, sin importar en qué municipio te detengas, las muertes locales han superado a los nacimientos.

Este es el retrato de Taiwán en 2025: una cara altamente diferenciada y que está envejeciendo junta. Sus disparidades internas son asombrosas: diferencia de densidad de 151 veces, diferencia de tamaño de 297 veces, diferencia generacional casi completa; pero su situación fundamental es sorprendentemente uniforme: toda la isla sufriendo más que vivir, con una disminución poblacional continua durante 23 meses y pasando de sociedad envejecida a superenvejecida en siete años. La Comisión Nacional de Desarrollo estima que, según sus proyecciones, la población total de Taiwán se reducirá a 14.97 millones para 2070, con una proporción mayor de 65 años del 46,5%; y el bono demográfico terminará en 2028. Este retrato no mejorará por sí solo. [^3]

Reconocer la heterogeneidad interna de Taiwán es para ver claramente el verdadero problema de esta isla: un lugar con tanta diferencia interna debe gestionar a los cuatro millones apiñados en la cuenca y a los trece mil que viven en las islas, mientras enfrenta a Hsinchu más joven y Chiayi más viejo. Está diferenciado, pero debe actuar como un todo; está envejeciendo, pero debe encontrar una manera de hacerlo juntos. Los datos nos han dibujado esta cara; cómo responder a ella es la pregunta que esta isla debe contestar junta.

## Lectura extendida

- [Taipéi](/es/geography/taipei-city) — El municipio más denso (8.975 hab/km²), y uno de los más viejos (índice de envejecimiento 202); es el protagonista en ambos extremos de densidad y envejecimiento del artículo.
- [Condado de Taitung](/es/geography/taitung-county) — El extremo más vacío (59 hab/km²); las dos islas asumen el costo de toda la isla.
- [Condado de Chiayi](/es/geography/chiayi-county) — Índice de envejecimiento más alto en Taiwán con 291,69; representa la vanguardia del envejecimiento agrícola, donde cada niño corresponde a casi tres ancianos.
- [Condado de Hsinchu](/es/geography/hsinchu-county) — El rincón más joven de Taiwán con un 15,08% de población mayor de 65 años; el mapa que sostiene la juventud gracias al clúster tecnológico (Zhuke).
- [Crisis de baja natalidad en Taiwán](/es/society/taiwan-low-birth-rate-crisis) — La cara de la natalidad de este retrato: menos de 110.000 nacimientos, y la otra cara del sufrimiento de toda la isla.

## Fuentes de imágenes

Este artículo utiliza 3 imágenes; el _hero_ es una imagen satelital de dominio público de la NASA (almacenada en `public/article-images/`), y las dos incrustadas tienen licencia Creative Commons CC, con sus respectivas atribuciones:

- [Imagen satelital de la isla principal de Taiwán (mosaico de la NASA 2020)](https://commons.wikimedia.org/wiki/File:Taiwan_Main_Island_Mosaic_NASA_2020.jpg) (_hero_) — NASA, Dominio público.
- [Línea de horizonte de Taipéi](https://commons.wikimedia.org/wiki/File:20260204_Taipei,_Taiwan_Skyline.jpg) (Sección más densa) — Foto: Heeheemalu, 2026, CC BY-SA 4.0.
- [Carretera Borlang en Taitung](<https://commons.wikimedia.org/wiki/File:29-%E4%BC%AF%E6%9C%97%E5%A4%A7%E9%81%93_(28896712393).jpg>) (Sección más vacía) — Foto: Sinchen.Lin, 2016, CC BY 2.0.

## Referencias

[^1]: Departamento de Registro Civil del Ministerio del Interior, datos demográficos (fin de 2025 / 31-12-2025, población por condado/municipio, área terrestre, densidad poblacional, proporción de población mayor de 65 años, índice de envejecimiento). La suma de la población de los 22 condados y municipios es de 23.299.132, lo que coincide perfectamente con el total oficial. [https://www.ris.gov.tw/app/portal/346]

[^2]: Agencia Central / Ministerio del Interior, 〈Taiwán entra oficialmente en una sociedad superenvejecida〉, 09-01-2026. El informe menciona una población total de 23.299.132 a finales de 2025, con el 20,06% mayor de 65 años (4,67 millones), Taipéi con el máximo del 24,18%, Hsinchu con el mínimo del 15,08%, y 107.812 nacimientos en 2025. [https://www.cna.com.tw/news/ahel/202601090098.aspx]

[^3]: Comisión Nacional de Desarrollo, 〈Proyecciones demográficas de la República de China (2024-2070)〉, publicado el 17-10-2024. Según las proyecciones, Taiwán entrará en una sociedad superenvejecida en 2025, terminará su bono demográfico en 2028 (población en edad de trabajar por debajo de dos tercios del total), y la población total caerá a 14.97 millones para 2070, con una proporción mayor de 65 años del 46,5%. [https://www.ndc.gov.tw/nc_27_38548]

[^4]: Ministerio del Interior, Reestructuración de las Cinco Ciudades en 2010 (elevación del condado de Taipéi a la ciudad principal de New Taipei; fusión de los condados de Taichung, Tainan y Kaohsiung, efectivo el 25-12-2010); Agencia Central, 〈La ciudad principal de Taoyuan se registra el 25 de diciembre〉, 15-12-2014. [https://www.cna.com.tw/news/firstnews/201412150027.aspx]

[^5]: Ministerio del Interior, 〈Nuestro país entra oficialmente en una sociedad envejecida〉 (proporción mayor de 65 años del 14,05%), 2018. [https://www.moi.gov.tw/News_Content.aspx?n=2&s=11663]
