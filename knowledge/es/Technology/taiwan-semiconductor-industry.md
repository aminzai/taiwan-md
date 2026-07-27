---
title: 'Semiconductores: 50 años de revolución de materiales, desde la transferencia tecnológica de RCA hasta el GaN y el empaquetado cuántico'
description: 'El "Monte Sagrado" de Taiwán domina los procesos avanzados globales mediante la subcontratación, pero el campo de batalla de la ciencia de materiales para los próximos 50 años —GaN en los cargadores, CoWoS bajo los chips de IA y refrigeradores de dilución sobre los qubits— apenas se está desplegando.'
date: 2026-03-17
category: 'Technology'
tags:
  [
    'semiconductores',
    'TSMC',
    'TSMC',
    'nitruro de galio',
    'empaquetado 3D',
    'CoWoS',
    'computación cuántica',
    'procesos avanzados',
    'escudo de silicio',
    'ciencia de materiales',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md'
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
  [
    "{'id': 87, 'platform': 'threads', 'date': '2026-05-25', 'url': 'https://www.threads.com/@taiwandotmd/post/DYvqEURgXm-'}",
    "{'id': 88, 'platform': 'x', 'date': '2026-05-25', 'url': 'https://x.com/taiwandotmd/status/2058735515021783190'}",
  ]
translatedFrom: 'Technology/半導體產業.md'
sourceCommitSha: 'c85a9b6f7'
sourceContentHash: 'sha256:b496186c7d76e85e'
sourceBodyHash: 'sha256:3bf42ee02082c616'
translatedAt: '2026-07-26T21:34:55+08:00'
---

# Semiconductores: 50 años de revolución de materiales, desde la transferencia tecnológica de RCA hasta el GaN y el empaquetado cuántico

![Dos cabezales de carga rápida USB-C de 30W idénticos en potencia, lado a lado; el producto de silicio a la izquierda es notablemente más voluminoso, mientras que el de nitruro de galio a la izquierda se ha reducido casi a la mitad, reflejando cómo la ciencia de materiales comprime la densidad energética en la palma de la mano](/article-images/technology/silicon-vs-gan-charger-2025.webp)
_Comparación de tamaño entre cargadores USB-C de 30W con silicio y GaN de igual potencia. Foto: 4300streetcar, 2025-12-25. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg)._

> **Resumen en 30 segundos:** TSMC iniciará la producción en masa de 2 nm en el cuarto trimestre de 2025 en su planta Fab 22 de Kaohsiung, liderando al mundo por 2-3 generaciones[^2]. Pero la historia no solo ocurre a medida que los transistores se hacen más pequeños: el cargador de carga rápida en tu bolso contiene nitruro de galio (GaN), GlobalWafers fabrica obleas de carburo de silicio (SiC) de 8 pulgadas en Zhongli, y la GPU Blackwell de NVIDIA depende del empaquetado CoWoS de TSMC para llegar a los centros de datos. Desde que el Instituto de Investigación Industrial (IRIS) compró la tecnología a RCA por 4,5 millones de dólares en 1973[^5] hasta que el Instituto Central de la República de China (ASMC) conectó en línea su chip cuántico superconductor de 20 qubits en 2026[^6], Taiwán ha recorrido un largo río de la ciencia de materiales, desde la física de bandas prohibidas hasta la deposición de capas atómicas y los qubits topológicos. El Monte Sagrado se basa en 50 años de experiencia en ingeniería, pero Taiwán aún no ha asegurado su posición como centro de subcontratación en la era cuántica.

En una tarde de 1985, el miembro del Consejo de Asuntos Civiles Lee Teng-hui fue a la Oficina del Consejo de Administración de la República de China y buscó a Morris Chang, quien acababa de regresar a Taiwán para asumir el cargo de presidente del Instituto de Investigación Industrial (IRIS). Lee Teng-hui fue directo al grano: "Queremos crear una empresa de fabricación de circuitos integrados a gran escala, tú la dirigirás".

Morris Chang se quedó perplejo. Pensó que solo había venido a ser presidente del instituto, pero dos semanas después lo arrastraron para fundar una empresa con un modelo comercial que nadie había intentado antes.

Este diálogo cambió el mundo. Pero 40 años después, al mirar hacia atrás, "el mundo" es mucho más denso de lo que se imaginó esa tarde. Incluye el cargador de carga rápida de 65 vatios del tamaño de dos nudillos al lado de tu teléfono, incluye cada GPU Blackwell que NVIDIA consume en los centros de datos, e incluye los qubits en el laboratorio del ASMC que necesitan ser enfriados hasta cerca del cero absoluto para "despertar".

## La apuesta de la subcontratación en 1987

![Exterior de la planta Fab 5 de TSMC en el Parque Científico de Hsinchu, un edificio industrial de varios pisos conectado a la Ruta Fuguo, es una de las zonas de producción representativas de la etapa de expansión de TSMC en la década de 1990](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Planta Fab 5 de TSMC en el Parque Científico de Hsinchu, 2010. Foto: Peellden. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG)._

La historia debe contarse desde antes. En 1973, el IRIS gastó 4,5 millones de dólares para adquirir la tecnología de circuitos integrados de la empresa estadounidense RCA y envió a 19 ingenieros a los Estados Unidos para recibir capacitación[^5]. En ese momento, nadie podría haber imaginado que este "costo de matrícula" se convertiría en la primera piedra angular del reino de los semiconductores de Taiwán. En 1980, la tecnología transferida por el IRIS llevó a la fundación de United Microelectronics Corporation (UMC), y Taiwán tuvo su primera empresa de semiconductores. Pero Lee Teng-hui no estaba satisfecho: UMC era demasiado pequeña, la tecnología no alcanzaba los estándares internacionales y Taiwán necesitaba un avance mayor.

El 21 de febrero de 1987, Morris Chang fundó Taiwan Semiconductor Manufacturing Company (TSMC) en el Parque Científico de Hsinchu, creando un modelo comercial sin precedentes: **subcontratación pura**.

Esta idea sonaba muy loca en ese momento. Todas las empresas de semiconductores del mundo eran verticalmente integradas, desde el diseño hasta la fabricación en una sola cadena. ¿Cómo era posible hacer solo la fabricación y no el diseño? ¿Entregarían los clientes los diseños más confidenciales a alguien?

La lógica de Morris Chang era simple: la industria de los semiconductores se estaba volviendo cada vez más compleja, y el diseño y la fabricación eran dos profesiones completamente diferentes. En lugar de hacer todo y no ser experto en nada, era mejor concentrarse en hacer una cosa bien y convertir la fabricación de chips en la mejor del mundo.

La estructura accionaria de TSMC en sus primeros años fue ingeniosa: el gobierno invirtió el 48,3 %, la inversión privada el 24,2 % y Philips de los Países Bajos poseía el 27,6 %[^1]. La participación de Philips fue clave. En ese momento, la industria de los semiconductores estaba dominada por Estados Unidos y Japón, y Europa necesitaba urgentemente un proveedor alternativo. Philips no solo invirtió, sino que también entregó sus pedidos de chips a TSMC, convirtiéndose en su primer cliente importante.

El modelo de subcontratación provocó una gran división en la industria de los semiconductores: las empresas de diseño de IC se concentran en diseñar chips (Qualcomm, NVIDIA, MediaTek), las fábricas de subcontratación se concentran en la fabricación (TSMC, UMC, GlobalFoundries) y las fábricas de empaquetado y pruebas se encargan del proceso posterior (ASE, SPIL). Anteriormente, solo gigantes como Intel o IBM podían asumir la inversión astronómica de una planta de obleas; ahora, cualquier startup con una buena idea puede diseñar un chip y luego entregarlo a TSMC para su fabricación.

El núcleo del modelo de subcontratación es la confianza. Los clientes deben confiar en que TSMC no robará sus diseños, no filtrará los secretos comerciales y no competirá con ellos. TSMC estableció un "Reglamento de Confianza" de cuatro principios: neutralidad tecnológica (nunca diseña chips propios), igualdad de clientes (todos los clientes reciben la misma tecnología y servicios), acuerdos de confidencialidad de nivel máximo y asignación justa de capacidad. Este reglamento se ha ejecutado durante casi 40 años sin excepciones.

> 📝 **Nota del curador**: En 1987, en Taiwán, los 19 ingenieros enviados por RCA apenas tenían poco más de 40 años. Aprendieron el proceso de silicio de Estados Unidos de la década de 1960, y nadie podría haber previsto que 30 años después se convertirían en el cliente principal de la tecnología de empaquetado del mundo. La cláusula de "castración voluntaria" por la que TSMC decidió no diseñar chips propios se convirtió, paradójicamente, en el factor de vinculación del que dependen Jensen Huang, Tim Cook y Lisa Su. La grandeza del modelo de subcontratación no radica en lo que hizo, sino en lo que **eligió no hacer**. Si retrocedemos aún más, el invento del transistor en los Laboratorios Bell en 1947, las invenciones independientes de circuitos integrados por Texas Instruments y Fairchild en 1958, y la migración del gobierno de la República de China a Taiwán en 1949 que trajo a una burocracia técnica de formación científica (el núcleo posterior del IRIS)... los 4,5 millones de dólares de RCA son un testigo, no el punto de salida.

## Burn J. Lin y ASML: una apuesta entre dos niños en la litografía de inmersión

La subcontratación no es solo cosa de TSMC. El lector [@malathrone_21k_running](https://www.threads.com/@malathrone_21k_running) complementó esta línea histórica clave en los comentarios: la raíz filipina de Philips de TSMC es la misma que la de ASML: una empresa de litografía que se separó de Philips en los Países Bajos en 1984, hoy el único proveedor de equipos EUV (ultravioleta extremo) del mundo. Hace 30 años, ambas eran "niños" menospreciados por los gigantes de la industria[^asml-philips].

La clave de la historia es un ingeniero taiwanés llamado Burn J. Lin. Desde 1992 trabajó en tecnología de litografía en el Centro de Investigación Watson de IBM, y en 2000 regresó a Taiwán para unirse a TSMC como director de la División de Investigación[^lin-bio]. En esa época, la disputa de la ruta siguiente para la litografía era la luz ultravioleta profunda de 157 nm; Nikon e Intel apostaron por esta ruta, pero la de 157 nm tuvo problemas constantes: las lentes de fluoruro de calcio tenían problemas de birrefringencia, las películas delgadas absorbían demasiado esta longitud de onda y la integración del proceso era difícil[^157nm-fail].

En 2002, Burn J. Lin presentó una idea loca en la conferencia óptica SPIE: "Mantengamos la fuente de luz de 193 nm, pero inyectemos agua entre la lente y la oblea". El índice de refracción del agua es 1,44, por lo que la luz de 193 nm en el agua equivale a una resolución de aproximadamente 134 nm, más fina que 157 nm, y sin necesidad de cambiar la fuente de luz ni las lentes[^immersion-litho].

Nikon no lo creyó y continuó apostando por 157 nm. ASML estuvo dispuesto a apostar: también era un "niño", buscando una palanca física para dar la vuelta, al igual que TSMC. En 2003, ASML comenzó a desarrollar la litografía de inmersión de 193 nm (193i), y en 2007 fue la primera en producir en masa, sosteniendo **seis generaciones** desde el proceso de 65 nm hasta el sucesor EUV actual[^immersion-litho][^cw-lin-interview].

"Nikon no se atrevió a hacer la inmersión por miedo al calor, así que ASML y nosotros tuvimos que hacerlo nosotros mismos", esta ruta tecnológica empujó a Nikon fuera del trono de la litografía[^cw-lin-interview]. Hace 30 años, dos "niños" apostaron por separado; hoy, uno es el único fabricante de equipos EUV del mundo y el otro es el único centro de subcontratación de 2 nm del mundo. Las dos semillas sembradas por Philips en los Países Bajos se encuentran en el siglo XXI.

## 50 años de espectro de materiales: de silicio a GaN a superconductores topológicos

Para comprender el campo de batalla de los semiconductores en 2025, primero hay que comprender una línea física que nunca se ha explicado claramente.

El silicio (Si) es el punto de partida de esta línea. Su "banda prohibida" es de 1,1 electrón-voltio (eV), que es la entrada mínima de energía necesaria para que un electrón salte de la banda de conducción a la banda de valencia. Una banda prohibida pequeña hace que los chips sean fáciles de fabricar, pero tiene dos techos: el alto voltaje causa colapso y la alta frecuencia genera calor. PanSci explica este límite claramente: "La frecuencia de trabajo límite de los semiconductores basados en silicio está solo por debajo de 100 kHz; si se supera 100 kHz, la eficiencia de conversión disminuirá drásticamente y habrá un grave problema de desperdicio de energía"[^7].

La banda prohibida del nitruro de galio (GaN) es de 3,4 eV, tres veces la del silicio. El límite de voltaje de ruptura es diez veces el del silicio. La frecuencia de trabajo puede alcanzar 1000 kHz, una orden de magnitud superior a la del silicio[^7]. Este número físico traducido a la vida cotidiana: a la misma potencia, los núcleos inductores de los transformadores de GaN pueden ser mucho más pequeños y los requisitos de disipación de calor son mucho más bajos, dando así lugar a los cargadores de carga rápida que caben en la palma de la mano.

El carburo de silicio (SiC) sigue otro camino. También es de banda ancha (banda prohibida de 3,26 eV), pero resiste mejor el calor y el voltaje extremos. PanSci señala directamente su campo de batalla: "El carburo de silicio tiene una buena estabilidad a alta temperatura y alto voltaje. Especialmente con el aumento de la demanda de carga rápida de vehículos eléctricos en el futuro, las necesidades de carga por encima de 1000 voltios harán que los semiconductores de silicio, que solo pueden soportar 600 voltios, no puedan manejar la carga, y se espera que asuman el papel de componentes clave en los vehículos eléctricos"[^7].

> 💡 **¿Sabías que...?**: La "banda prohibida" de un semiconductor determina qué tan alto voltaje puede soportar, a qué frecuencia puede funcionar y cuánto calor genera. 1,1 eV de silicio es la base de la electrónica de consumo durante 50 años; 3,4 eV de GaN sostiene los cargadores de 240 vatios para teléfonos; 3,26 eV de SiC entra en los inversores de vehículos eléctricos de 800 voltios; la próxima parada podría ser el semiconductores de diamante de 5,5 eV. Todo el espectro de materiales es una escalera de "ascenso de densidad de energía"; en cada escalón, Taiwán debe negociar con los límites físicos de la ciencia de materiales.

La próxima parada aún no tiene nombre: podría ser diamante (C, 5,5 eV), óxido de galio (Ga₂O₃, 4,8 eV), o entrar en un mecanismo físico completamente diferente, como superconductores topológicos, la ruta que siguió Microsoft al anunciar su procesador cuántico Majorana 1 en febrero de 2025[^15]. Cuando la física cambia, toda la cadena de la industria se reescribe.

## El GaN en tu cargador de carga rápida

Alejemos la cámara a tu mochila.

El cargador del Nokia 3310 tenía una potencia de 4,56 vatios; los cargadores de carga rápida de 2025 alcanzan 240 vatios. Una diferencia de 52 veces. PanSci organizó esta línea de tiempo: "La potencia de los cargadores de carga rápida de GaN más populares alcanza los 65 vatios, una diferencia de 13 veces, y teóricamente el tiempo de carga se reducirá a una treceava parte"[^7]. Más impresionante aún es la marca china realme, que lanzó el GT Neo5 de carga súper rápida de 240 vatios a principios de 2023, llevando este multiplicador por encima de 50.

Esta curva de crecimiento se basa físicamente en el cambio a GaN, mientras que el grosor del cable de cobre y el volumen de la batería se reducen. Para aumentar la potencia y reducir el volumen, el método más directo es elevar la frecuencia de trabajo, pero "la frecuencia de trabajo límite de los semiconductores basados en silicio está solo por debajo de 100 kHz"[^7], que es el "límite del silicio" del que habla PanSci. GaN eleva la frecuencia de trabajo por encima de 1 MHz, haciendo que el transformador y la inductancia se reduzcan simultáneamente, permitiendo que todo el cargador se meta en un bolsillo.

El problema es: cuando el mercado de cargadores de carga rápida de Taiwán estaba a punto de explotar, TSMC anunció una cosa, **retirarse de la subcontratación de GaN en julio de 2027**[^8].

Detrás de esta decisión hay dos presiones. En primer lugar, las fábricas chinas de GaN (China Resources Microelectronics, Silan Microelectronics, Ruineng, etc.) están expandiendo masivamente su producción, presionando el precio de la subcontratación hasta un nivel al que TSMC no quiere adherirse. En segundo lugar, los beneficios de los chips de IA son demasiado atractivos, y TSMC quiere convertir las fábricas de GaN en líneas de producción de empaquetado avanzado (CoWoS). La licencia tecnológica se otorgó a World Semi (VIS) y GlobalFoundries, y la carga de la subcontratación de GaN en Taiwán recae en empresas como稳懋 (3163) y 宏捷科 (8086) que apostaron por ello hace diez años[^8].

> ⚠️ **Punto de vista controvertido**: La retirada de TSMC de la subcontratación de GaN tiene dos interpretaciones externas. Una facción considera que es una elección racional de "dejar capacidad para la IA"; la rentabilidad por oblea de silicio de 3 nm es más de 20 veces superior a la de GaN de 6 pulgadas, por lo que la asignación de capacidad se dirige naturalmente hacia la mayor rentabilidad. La otra facción cuestiona: que Taiwán abandone GaN equivale a entregar la base de la próxima generación de electrónica de consumo (teléfonos / portátiles / cargadores) a las fábricas chinas; ¿el "escudo" del escudo de silicio se reduce solo a esa pieza en el extremo de la IA? La diferencia entre las dos partes radica en: ¿crees que el valor del Monte Sagrado es el "proceso avanzado irremplazable" o el "clúster completo de la cadena de suministro"?

Tanto TSMC como la gran fábrica de obleas GlobalWafers, así como las principales empresas de semiconductores nacionales e internacionales, ya se han subido a este tren[^7]. Pero en qué vagón subir es una cuestión diferente.

## La oblea de SiC de 8 pulgadas de GlobalWafers

Si GaN es la historia de los cargadores de teléfonos, SiC es la historia de los vehículos eléctricos.

El núcleo de esta línea de SiC en Taiwán es GlobalWafers, no TSMC. En 2024, la capacidad de producción mensual de obleas de SiC de 6 pulgadas de GlobalWafers alcanzó aproximadamente 20.000 unidades, expandiendo sus hornos de crecimiento de cristales auto-desarrollados de 3 a 20 unidades, y la tasa de rendimiento superó el 50 %[^9]. En 2025, las obleas de SiC de 8 pulgadas entraron en producción en masa, la primera en Taiwán.

El CEO de GlobalWafers, Hsu Hsiu-lan, siempre habla directamente: "El Grupo Zhongmei creará un 'Grupo IDM Virtual', apuntando a la demanda de carburo de silicio de los próximos 5 años. Nos estamos moviendo rápido"[^9]. La estrategia es vincular el crecimiento de cristales (GlobalWafers), epitaxia (Pengcheng) y módulos (Hongyang Semiconductor) de la matriz Zhongmei en una cadena.

Pero SiC no es una historia lineal hacia arriba. En la segunda mitad de 2025, las fábricas chinas de SiC (San'an Optoelectronics, Tianke Heda, etc.) expandieron su producción de forma masiva, causando un exceso de oferta global, y la tasa de utilización de la capacidad de SiC de 6 y 8 pulgadas de GlobalWafers cayó por debajo del 50 % en un momento dado[^10]. Esto añade un valle al guión optimista de 2023 de PanSci sobre la "asunción de la demanda de vehículos eléctricos".

La señal de recuperación proviene de NVIDIA. Se rumorea que la próxima plataforma de GPU Rubin de NVIDIA utilizará SiC en la capa intermedia, combinada con una arquitectura de centro de datos de corriente continua de alto voltaje de 800 voltios, y entrará en producción en masa en 2027[^10]. Si este rumor es cierto, la capacidad de SiC de 8 pulgadas de GlobalWafers se transferirá de vehículos eléctricos a centros de datos de IA, iluminando nuevamente toda la historia.

> 📝 **Nota del curador**: GaN y SiC a menudo se denominan colectivamente "semiconductores de tercera generación", pero este clasificación en el contexto industrial de Taiwán va más allá de la etiqueta de "próximo material": representa la primera vez que la industria de semiconductores de Taiwán tiene una cadena de suministro completa **sin depender de TSMC**. Crecimiento de cristales de GlobalWafers, fabricación de Hanle, empaquetado de稳懋, diseño de 宏捷科: fuera del Monte Sagrado, está creciendo otro "tercer pico" discreto pero independiente.

## La vinculación de Jensen Huang con CoWoS+

Regresemos al campo de batalla de la IA.

La GPU H100 de NVIDIA utiliza el proceso de 4 nm de TSMC, combinado con el empaquetado CoWoS-S para integrar la memoria de alto ancho de banda HBM3. El Blackwell B200 se actualiza a CoWoS-L, integrando dos GPUs Blackwell y una CPU Grace, con una velocidad de entrenamiento de IA 4 veces superior a la de H100[^11]. La próxima generación, Rubin, está prevista para 2026.

El núcleo de cada generación de GPU es el doble motor de "proceso avanzado + empaquetado avanzado". El proceso hace los transistores cada vez más pequeños, y el empaquetado apila las diferentes pastillas (die) cada vez más cerca. PanSci utiliza la comparación entre la Ruta Nacional 9 y el Túnel de Xueshan para explicar esto: "El empaquetado tradicional debe pasar por la sinuosa Ruta Nacional 9, mientras que el empaquetado avanzado acorta el camino, abriendo el Túnel de Xueshan que conecta los dos lugares, haciendo que el intercambio de datos sea más conveniente y rápido"[^12].

El núcleo de CoWoS (Chip-on-Wafer-on-Substrate) es el "vía de silicio" (through-silicon via, TSV): apilar diferentes pastillas y atravesar la sustrato de silicio con microcanales verticales para que dos circuitos originalmente separados se conecten en 3D. PanSci lo describe claramente: "El apilamiento 3D puede colocar el chip C sobre el chip A, atravesando el sustrato de silicio adelgazado mediante la tecnología de vía de silicio, conectando los dos circuitos con cables de conducción vertical de ultra alta densidad, reduciendo la distancia entre ellos de un abismo a la proximidad"[^12].

Los números de capacidad son aún más impactantes. La capacidad de producción mensual de CoWoS de TSMC fue de aproximadamente 35.000 unidades a finales de 2024, con un objetivo de alcanzar 75.000 unidades a finales de 2025, y avanzar hacia 150.000 unidades en 2028, con una tasa de crecimiento anual compuesta de casi el 80 %[^13]. NVIDIA reservó toda la capacidad de CoWoS de TSMC hasta 2027, y **todos los chips, independientemente de la planta de TSMC donde se produzcan (incluyendo Arizona), deben ser enviados de vuelta a Taiwán para el empaquetado CoWoS**[^13].

Esta es la doble hegemonía de Jensen Huang y TSMC. NVIDIA en el extremo del diseño, TSMC en el extremo de la fabricación y el empaquetado; las dos empresas bloquean conjuntamente el nodo clave de los centros de datos de IA.

El 2 de junio de 2024, en el discurso temático de Computex en el Gimnasio de la Universidad Nacional de Taiwán, Jensen Huang explicó públicamente esta vinculación al mundo: las diapositivas mostraban la hoja de ruta de Blackwell y Rubin, pero detrás de cada una hay una línea de producción CoWoS de TSMC.

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
   <iframe src="https://www.youtube.com/embed/pKXDVsWZmUU" title="NVIDIA CEO Jensen Huang Keynote at COMPUTEX 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Canal oficial de NVIDIA: El discurso temático "The Era of AI" de Jensen Huang en Computex el 2 de junio de 2024 en el Gimnasio de la Universidad Nacional de Taiwán. Durante dos horas, desplegó uno a uno las GPU Blackwell, NVLink y Spectrum-X... pero la realidad física de cada diapositiva está en el Monte Baoshan de Hsinchu. "Sin TSMC, no hay NVIDIA" no lo dijo en voz alta, pero cada gráfico de capacidad lo dice._

El costo físico del empaquetado 3D también es considerable. PanSci señaló el problema: "El empaquetado avanzado requiere alta planitud de los die y alta precisión de alineación de los chips; si hay puntos de conexión que no se conectan correctamente durante el apilamiento, se perderá rendimiento. Además, los circuitos integrados generan pérdida de energía durante el cálculo, lo que aumenta la temperatura; el empaquetado avanzado acerca los die, la transferencia de calor se influye mutuamente, se calientan entre sí, haciendo que la disipación de calor sea más difícil"[^12].

La siguiente etapa es SoIC (System on Integrated Chips) y SoW-X (System on Wafer). SoIC es el "verdadero 3D", apilando oblea contra oblea directamente, sin bumping (bumping-free). Se espera que SoW-X entre en producción en masa en 2027, con un tamaño de máscara 9,5 veces mayor que el CoWoS actual, integrando más de 16 chips de computación grandes, con una capacidad de computación 40 veces superior a la CoWoS existente[^13]. A medida que los chips de IA crecen más y más, las líneas de empaquetado de TSMC se parecen cada vez más a pequeñas fábricas.

## ALD: creciendo átomo por átomo

![Vitrina de museo con varias obleas de silicio de diferentes tamaños dispuestas lado a lado; la más grande tiene un diámetro de aproximadamente 12 pulgadas, mostrando con un brillo como espejo la materia prima central de la fabricación de semiconductores](/article-images/technology/silicon-wafers-museum-2017.webp)
_Exhibición de muestras de obleas de silicio, 2017. Foto: ArticCynda. [Licencia vía Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg)._

4 nm, 2 nm, 1,6 nm. Detrás de estos números hay una tecnología de fabricación discreta pero clave: Deposición de Capas Atómicas (Atomic Layer Deposition, ALD).

ALD fue inventada por finlandeses, pero se ha convertido en un paso central del que no puede prescindir ninguna oblea de proceso avanzado en Taiwán.

La historia debe comenzar en Finlandia. En 1974, el científico de materiales Tuomo Suntola comenzó a desarrollar ALD en la empresa finlandesa Instrumentarium Oy. En 1977, la tecnología se consolidó y se presentó por primera vez en una exhibición industrial[^14]. En ese momento, esta tecnología solo era para hacer displays electroluminiscentes; Suntola mismo no pudo haber previsto que 30 años después se convertiría en la médula espinal de los procesos nanométricos. En 1999, vendió la tecnología ALD a la empresa de equipos semiconductores neerlandesa ASM. Hoy, ASM posee más del 55 % de la cuota de mercado en el mercado ALD[^14].

PanSci explica el principio de ALD de manera limpia: "La deposición de capas atómicas es una técnica mejorada de deposición química en fase vapor que divide el proceso de deposición en dos pasos. Primero, se inyecta el primer precursores, reaccionando con la superficie del sustrato... Cuando la superficie está saturada, se inyecta el segundo precursores, reaccionando con el precursores ya adherido para formar el material objetivo, completando el proceso de la película delgada"[^14]. Los dos precursores se inyectan uno por uno en rotación; cada ciclo solo crece una película delgada del grosor de un átomo.

¿Por qué es importante esto? Porque el grosor de la puerta (gate) de los transistores del proceso de 2 nm es solo de unos pocos átomos, y la capa aislante de la puerta debe alcanzar una planitud a nivel atómico y un control de grosor a nivel atómico. La deposición química en fase vapor tradicional (CVD) no puede hacerlo, la deposición física en fase vapor (PVD) no puede hacerlo; solo ALD puede "crecer capa por capa". Cada planta de proceso avanzado de TSMC está equipada con equipos ALD de ASM; esta cadena, compuesta por equipos neerlandeses, tecnología finlandesa y procesos taiwaneses, es la base física por la que el 2 nm puede producirse en masa.

> 💡 **¿Sabías que...?**: La dimensión característica mínima del proceso de 2 nm es aproximadamente el ancho de 20 átomos de silicio en fila. Si agrandamos los átomos de silicio al tamaño de una pelota de ping-pong, el transistor de 2 nm sería aproximadamente del tamaño de una mesa de ping-pong. El trabajo de ALD es "colocar una pelota de ping-pong a la vez" para cubrir la mesa con material aislante.

ASM no cotiza en Taiwán, pero sus principales clientes para la mayoría de sus equipos ALD de 12 pulgadas están en Taiwán. **Esta cadena de suministro es invisible pero irremplazable**; si la producción en masa de 2 nm de TSMC no va bien, no hay una segunda fábrica ALD en el mundo que pueda suplirla.

## Después de 2 nm está lo cuántico

Detrás de la escala de angstroms (1 nm = 10 Å), la historia que TSMC aún no ha terminado de escribir.

En el cuarto trimestre de 2025, TSMC iniciará la producción en masa de 2 nm en su planta Fab 22 de Kaohsiung, seguida por la planta Fab 20 en el Monte Baoshan de Hsinchu[^2]. El 2 nm adopta por primera vez la arquitectura de transistores de nanohojas GAA (Gate-All-Around), abandonando los transistores FinFET que se utilizaron desde los 22 nm hasta los 3 nm[^16]. 2 nm equivale a 20 átomos de silicio de ancho, ya cerca del límite teórico de la física. Los primeros clientes incluyen los chips de la serie A de Apple y los chips de IA de NVIDIA; la capacidad de producción del proceso de 2 nm se expandirá trimestralmente[^3].

La próxima parada es 1,6 nm (A16), prevista para el cuarto trimestre de 2026, introduciendo por primera vez la "Red de Distribución de Energía en el Lado Posterior" (Backside Power Delivery Network), nombrada por TSMC como Super Power Rail[^16]. A la misma potencia, es un 10 % más rápido que N2P; a la misma eficiencia, ahorra entre un 15 % y un 20 % de energía.

¿Pero qué pasa después de 1,6 nm? Los nodos de proceso se vuelven cada vez más caros a medida que avanzan. El costo de I+D del proceso de 28 nm es de aproximadamente 1000 millones de dólares, salta a 3000 millones para los 7 nm, se dispara a 10000 millones para los 3 nm, y se estima que superará los 20000 millones para los 2 nm[^4]. La curva exponencial de la Ley de Moore convierte los costos de I+D de la etapa final en números astronómicos, que es lo que PanSci llama "la complejidad y la inversión de capital en el desarrollo de procesos avanzados aumentan exponencialmente, y la inversión y el retorno a menudo no son proporcionales"[^12].

Por lo tanto, la industria de los semiconductores cambia de estrategia: la expansión horizontal se convierte en apilamiento vertical (empaquetado 3D), el silicio se convierte en nuevos materiales (GaN/SiC), y finalmente podría cambiar a una física de computación completamente diferente, como la computación cuántica.

La hoja de ruta del ASMC es la siguiente. En octubre de 2023, se completó la investigación de un ordenador cuántico superconductor de 5 qubits. El 29 de enero de 2024, la presidenta Tsai Ing-wen inspeccionó y el ordenador cuántico se conectó oficialmente a la red[^6]. PanSci escribe: "En enero de 2024, el primer ordenador cuántico desarrollado autónomamente en Taiwán nació oficialmente en el Instituto Central de la República de China (ASMC); aunque solo tiene 5 qubits, esto abrió el telón para que Taiwán ocupara un lugar en el campo de batalla global de los ordenadores cuánticos"[^17].

En diciembre de 2025, se completó el chip cuántico superconductor de 20 qubits. Se anunció su conexión en enero de 2026[^6]. El tiempo de coherencia (coherence time T1) saltó de 15-30 microsegundos en la era de 5 qubits a 530 microsegundos en 20 qubits. El tiempo de coherencia es la duración durante la cual un qubit puede mantener el estado de superposición; cuanto más largo, significa "menos ruido y se pueden realizar cálculos más complejos".

El equipo nacional cuántico interministerial se formó oficialmente en marzo de 2022, con un presupuesto de 5 años de 8000 millones de NTD y 17 equipos de investigación[^18]. El Ministerio de Asuntos Económicos estableció la "Oficina de Promoción de Tecnología de la Industria Cuántica" en abril de 2026, conectando la I+D académica con la industria.

Lo que hace el IRIS es particularmente interesante: utiliza el proceso de 28 nm de TSMC para hacer "chips de control de qubits". En marzo de 2024, la Agencia Central de Noticias citó al IRIS: "Utilizando el diseño de IC de microondas en el que Taiwán es hábil y el proceso de 28 nm de TSMC, creamos chips y módulos de control de baja temperatura (4 K, es decir, -269 °C)... reduciendo el tamaño de los instrumentos de control, colocándolos en un armario de refrigeración de baja temperatura, reduciendo el volumen total del equipo en un 40 %, simplificando el cableado, con ventajas comerciales... el consumo de energía de este módulo es más del 50 % inferior a los datos publicados por los grandes fabricantes internacionales"[^19].

> 📝 **Nota del curador**: La estrategia cuántica de Taiwán no radica en fabricar sus propios qubits (ese es el territorio de IBM, Google y el ASMC), sino en miniaturizar los circuitos de control para que quepan en el refrigerador de dilución. De 5 qubits a 20 qubits, el chip de control del IRIS pasó de soportar 1 qubit, a 2 qubits, a 8 qubits, y se espera que alcance 20 qubits en 2026-2027. **La próxima parada del Monte Sagrado es ser el centro de subcontratación de la era cuántica, no competir personalmente por la hegemonía cuántica**. Pero esta posición de subcontratación aún no tiene nadie clavando el clavo de "déjalo a Taiwán".

## Tres rutas cuánticas: superconductores, trampas de iones y topológicas

Los ordenadores cuánticos no tienen solo una ruta.

**Qubits superconductores** (superconducting qubits) es la ruta que siguen IBM, Google y el ASMC. La ventaja es que el proceso es compatible con las fábricas de semiconductores existentes (aquí es donde Taiwán tiene oportunidades) y la velocidad de control es rápida. La desventaja es que requiere un refrigerador de dilución cerca del cero absoluto (15 mK, aprox. -273 °C) y tiene alto ruido. Google anunció la supremacía cuántica en 2019 con el "Sycamore" (梧桐) de 53 qubits, completando en 200 segundos una tarea que a un supercomputador tradicional le tomaría 10.000 años[^20].

**Qubits de trampa de iones** (trapped ion qubits) siguen la ruta del control láser de un solo átomo. PanSci organizó las diferencias de esta ruta: "La tecnología de trampa de iones utiliza láser para controlar un solo átomo para realizar cálculos; esta tecnología tiene alta precisión y estabilidad, pero enfrenta problemas de complejidad técnica y costos"[^17]. Los fabricantes representativos son IonQ y Quantinuum. La ventaja es alta precisión, buena estabilidad y no requiere temperaturas extremadamente bajas. La desventaja es velocidad de control lenta y dificultad para escalar a muchos qubits.

**Qubits topológicos** (topological qubits) es la apuesta de la próxima generación de Microsoft. En febrero de 2025, Microsoft presentó el procesador cuántico topológico Majorana 1, afirmando que puede escalar a un millón de qubits[^15]. Teóricamente, los qubits topológicos tienen una resistencia extrema a las interferencias, pero esta ruta es la menos madura; la existencia de las partículas de Majorana aún está en fase de verificación en la física.

Estas tres rutas tienen riesgos propios. La estrategia de Taiwán es "**asegurar que, independientemente de la ruta que gane, Taiwán tenga un nodo en la cadena de suministro**", sin apostar por una sola ruta. La ruta superconductora depende del chip de control de 28 nm de TSMC. La ruta de trampas de iones requiere óptica de precisión que se conecta con la industria optoelectrónica de Taiwán; si la ruta topológica tiene éxito, también requiere películas de pureza extrema, volviendo al territorio de ALD.

## Fab overseas: ¿expansión o exportación?

La globalización de TSMC se aceleró desde la década de 2020.

**Fab 21 en Arizona, EE. UU.**: La Fase 1 de 4 nm entró en producción en masa en la primera mitad de 2025; la Fase 2 de 3 nm/2 nm en la segunda mitad de 2027; la Fase 3 de 2 nm/A16 está prevista antes de 2030. El gasto de capital total es de aproximadamente 165.000 millones de dólares[^21]. Pero hay un "pero" importante: todo el empaquetado CoWoS de los chips de IA aún se realiza solo en Taiwán; las obleas producidas en la planta de Arizona se envían de vuelta a Taiwán para completar el empaquetado[^13].

**Fab 1 en Kumamoto, Japón**: Procesos de 22-28 nm, producción en masa en 2024, en colaboración con Sony y Toyota. La planificación original de Fab 2 (12-16 nm) tiene un progreso incierto, y parte de los recursos se han redistribuido a Arizona.

**ESMC en Dresde, Alemania** (TSMC posee el 40 %): Chips de automóvil de 28/22/16/12 nm, instalación de equipos en la segunda mitad de 2025, producción en masa en 2027, capacidad de producción mensual de aproximadamente 40.000 unidades[^22].

Estas fábricas extranjeras comparten un principio "N-2": **siempre dos generaciones por detrás de Taiwán**. Cuando Taiwán está haciendo 2 nm, lo más avanzado en el extranjero es 4 nm; cuando Taiwán impulsa 1,6 nm, el extranjero solo llega a 3 nm. Esta línea roja está escrita en la ética de ingeniería geopolítica, no en las cláusulas del contrato.

> ⚠️ **Punto de vista controvertido**: ¿Las fábricas extranjeras amplían o diluyen el escudo de silicio? Los partidarios dicen: la tecnología se queda en Taiwán, la capacidad se expande al extranjero, convirtiendo el escudo de silicio de "una isla" a "una cadena", haciendo la desvinculación de riesgos más completa. Los opositores dicen: cada fábrica extranjera que se envía exporta ingenieros capacitados, un SOP de producción en masa y relaciones con clientes. Cuando Arizona o Kumamoto acumulen el límite N-2 dentro de 30 años, esa "primera de dos generaciones" podría comprimirse lentamente. El principio N-2 es actualmente una promesa de TSMC, no una ley física.

Junto con las fábricas extranjeras, también avanza la "migración de talento de diseño". El diseño de chips de IA no solo necesita Taiwán; Silicon Valley, Tel Aviv y Nueva Delhi tienen sus propios centros de diseño. El ecosistema de subcontratación de TSMC está pasando de "ingenieros de toda la isla" a una mezcla de "ingenieros globales + fabricación de toda la isla".

## El costo ambiental: el otro lado del Monte Sagrado

El Monte Sagrado tiene peso.

Los recursos hídricos son lo más直观. Los tres parques científicos de TSMC consumen más de 208.000 toneladas diarias; los grupos ambientalistas estiman que después de 2025, con la puesta en marcha de las nuevas plantas, el consumo de agua podría aumentar 4 veces hasta 770.000 toneladas/día[^23]. La respuesta de TSMC es: cada gota de agua se utiliza en promedio 3,5 veces, con una tasa de reciclaje del 87 %; el objetivo de las nuevas plantas es el 90 %; en 2024 se agregaron 5,54 millones de metros cúbicos de ahorro de agua.

La energía eléctrica es la segunda cuestión. Una planta de 3 nm consume aproximadamente 2.100 millones de kWh al año, equivalente al consumo anual de electricidad de 20.000 hogares en toda Taiwán. El consumo de energía de 2 nm y 1,6 nm seguirá aumentando. TSMC se compromete a alcanzar RE100 (100 % de energías renovables) para 2050, pero la oferta de energía verde de Taiwán no sigue el ritmo de la expansión de los semiconductores; esta línea de tiempo está siendo probada constantemente bajo presión.

Las horas de trabajo son la tercera cuestión. Las horas de trabajo, los precios de la vivienda y la tasa de natalidad de los ingenieros del Parque Científico de Hsinchu son el tema de otro artículo. Pero al igual que la ciencia de materiales, es un problema físico: el tiempo y la energía humana también tienen una "banda prohibida"; si se supera el umbral, colapsarán.

La existencia del Monte Sagrado depende, además de la tecnología de TSMC, las políticas gubernamentales y las oportunidades geopolíticas, del costo compartido por 170.000 ingenieros del parque científico, toda la cadena de suministro y cada residente de Taiwán que usa agua y electricidad.

## Ecosistema completo: Taiwán no es solo TSMC

La competitividad de la industria de semiconductores de Taiwán proviene de todo el clúster, no solo de TSMC. En el extremo del diseño de IC hay MediaTek (top 3 global), Novatek, Realtek, Himax; además de TSMC en la subcontratación de obleas, hay UMC, World Semi, JSMC; el empaquetado y las pruebas son responsabilidad de ASE (nº 1 mundial), SPIL, Kinsus. Los semiconductores de tercera generación dependen de GlobalWafers (crecimiento de SiC), Hanle, 稳懋 (GaN) y 宏捷科; la memoria es responsabilidad de Nanya Technology y Winbond; en el extremo de equipos y materiales, empresas invisibles como JBD Precision, Sinopac y Chongyue están cubriendo posiciones.

Un chip puede dar la vuelta a Taiwán desde el diseño hasta la finalización, sin necesidad de transporte transnacional. Esta "ventaja de cadena corta" fue vista por todo el mundo durante la pandemia de COVID, y desde entonces se ha escrito en los libros blancos de la cadena de suministro de cada gigante tecnológico.

El Parque Científico de Hsinchu se estableció en 1980; en más de 40 años ha acumulado más de 500 empresas y 170.000 empleados. Un ingeniero puede pasar 5 años en TSMC, saltar a MediaTek para diseñar chips, y luego pasar a ASE para encargarse del empaquetado; esta circulación de talento entre empresas hace que el nivel tecnológico de toda la industria se difunda efectivamente.

¿Y los competidores? La estrategia de integración vertical de Samsung en Corea del Sur invirtió 230.000 millones de dólares entre 2022 y 2026, pero la tasa de rendimiento de procesos avanzados aún está por detrás de TSMC[^4]. Intel se estancó en los 10 nm durante años; propuso IDM 2.0 en 2021 para combinar diseño y subcontratación, pero para 2025 aún no había obtenido clientes importantes en la industria de subcontratación; lo más irónico es que algunos chips de alta gama de Intel ahora se subcontratan en TSMC.

## La posición cuántica aún está vacía

El cargador del Nokia 3310 tenía una potencia de 4,56 vatios; los cargadores de carga rápida de 2025 son de 240 vatios. Una diferencia de 52 veces. Este camino lo recorrió el silicio en 30 años, y el GaN lo completó en 5 años.

En el laboratorio cuántico del ASMC, los chips cuánticos superconductores necesitan operar a 15 milikelvin (aprox. -273 °C). El chip de control hecho por el IRIS con el proceso de 28 nm de TSMC comprimió el "volumen del instrumento de control" necesario para esta baja temperatura extrema de un edificio a una pequeña caja. La capacidad de semiconductores de Taiwán está moviendo poco a poco los límites de los ordenadores cuánticos.

Pero dónde está este límite, nadie puede decirlo con claridad. El tiempo de coherencia de los qubits va de 15 microsegundos a 530 microsegundos; esto es solo el comienzo. Hace 50 años, los 19 ingenieros enviados por RCA quizás tampoco sabían que su 1973 se cristalizaría en el 2 nm de 2025.

El Monte Sagrado dominó el presente con 50 años de experiencia en ingeniería. En los próximos 50 años, la posición de subcontratación de la era cuántica, Taiwán aún no la ha asegurado.

> ✦ La inferencia en la nube sobre tu cabeza de Blackwell de Jensen Huang, el calentamiento de la oblea SiC de GlobalWafers en el poste de carga de tu coche eléctrico, la primera película ALD hecha por Suntola en Finlandia en 1974 sellando la capa aislante de la puerta en tu chip de teléfono... Los semiconductores siempre han sido una ascensión de 50 años a lo largo del espectro de materiales según la física de la banda prohibida, no solo perteneciente a una empresa. Dónde está el siguiente escalón, la física nos lo dirá, pero si subirlo o no, es la elección de Taiwán.

---

**Lectura adicional**:

- [Empresa de Taiwán: TSMC](/es/economy/tsmc) — Gobernanza corporativa, estructura financiera y escala de gasto de capital del Monte Sagrado
- [Empresa de Taiwán: MediaTek](/es/economy/mediatek) — Cómo el líder del diseño de IC ocupa posiciones en chips de teléfonos y computación perimetral de IA
- [Empresa de Taiwán: ASE Semiconductor](/es/economy/taiwan-enterprise-ase-semiconductor) — Número 1 mundial en empaquetado y pruebas, ecosistema de procesos posteriores a CoWoS
- [Creadores de Montañas: La Apuesta del Siglo](/es/art/mountain-makers-tsmc-documentary) — Documental de 2025 de Hsiao Bi-khim, 5 años de entrevistas a más de 80 veteranos de semiconductores, entrando en 2026 a los tres puntos calientes de inversión de la CHIPS Act en Purdue / Wisconsin / Michigan
- [Wu Da-you](/es/people/tai-yu-wu) — Mientras Taiwán construía semiconductores en la década de 1980, actuó como presidente del ASMC, insistiendo en la importancia de la ciencia básica, sentando las bases del sistema de investigación de Taiwán
- [Industria de Robots de Taiwán](/es/technology/taiwan-robotics-industry) — ¿Por qué la isla número 1 en semiconductores es un estudiante que está recuperando el tiempo en la era de los robots? Mirando la inauguración de NCAIR para ver la brecha industrial
- [Bolsa y Mercado de Capitales de Taiwán](/es/economy/taiwan-stock-market) — Cómo se presenta en el mercado de capitales toda la cadena de suministro que sostiene la identidad de Taiwán como la 6ª economía más grande del mundo en 2026
- [Cadena de Suministro de Tungsteno de Taiwán](/technology/台灣鎢供應鏈) — El hexafluoruro de tungsteno rellena las ventanas de contacto y las líneas de caracteres de 3D NAND; Taiwán, sin minas de tungsteno, se posiciona en el medio de esta fuente de materiales gracias al reciclaje y refinamiento
- [Escuela de IA de Taiwán](/es/technology/taiwan-ai-academy) — Cómo los 10.000 ingenieros de IA entrenados por AIA durante 8 años regresan a la cadena ICT existente de semiconductores, reforzando el lado de software de Taiwán
- [Computex: Tres de las tres grandes ferias internacionales de computadoras se han cerrado, la que queda crece en Taipéi](/es/technology/computex-taipei) — El CoWoS de TSMC y los procesos avanzados, cada final de mayo, estrechan manos con los gigantes globales de IA en esta feria de computación de 45 años de antigüedad en Taipéi
- [Parques Científicos de Taiwán](/es/technology/science-park-development) — Los tres parques Hsinchu, Nantou y Taichung, el soporte físico del clúster de semiconductores, y también el centro geográfico del escudo de silicio

## Fuentes de imágenes

Este artículo utiliza 3 imágenes con licencia CC/PD, almacenadas en `public/article-images/technology/` para evitar servidores de origen de enlaces calientes:

- [Silicon vs GaN 30W USB-C chargers](https://commons.wikimedia.org/wiki/File:Silicon_vs_GaN_30W_USB-C_chargers.jpg) — Foto: 4300streetcar, 2025-12-25, CC BY 4.0, Archivo de Wikimedia Commons Silicon_vs_GaN_30W_USB-C_chargers.jpg
- [TSMC Fab 5 Hsinchu](https://commons.wikimedia.org/wiki/File:TSMC_Fab5.JPG) — Foto: Peellden, 2010-09-05, CC BY-SA 3.0, Archivo de Wikimedia Commons TSMC_Fab5.JPG
- [Silicon wafers museum display](https://commons.wikimedia.org/wiki/File:Silicon_wafers.jpg) — Foto: ArticCynda, 2017-10-23, CC0 dominio público, Archivo de Wikimedia Commons Silicon_wafers.jpg

## Referencias

[^1]: [Semiwiki — How Philips Saved TSMC](https://semiwiki.com/semiconductor-history/307560-how-philips-saved-tsmc/) — Según Semiwiki, la participación accionaria de Philips debería ser del 27,6 %; accionista clave en tecnología y clientes en los primeros años de TSMC

[^2]: [Focus Taiwan 2025/12/30 — TSMC 2nm production](https://focustaiwan.tw/business/202512300012) — La producción en masa de 2 nm de TSMC comienza con la planta Fab 22 de Kaohsiung, seguida por la planta Fab 20 en el Monte Baoshan de Hsinchu

[^3]: [数位时代 — TSMC 2nm正式量產](https://www.bnext.com.tw/article/89663/tsmc-2nm-volume-production) — TSMC inicia la producción en masa de 2 nm en el cuarto trimestre de 2025; los números específicos de capacidad mensual son estimaciones externas de la industria, no reveladas oficialmente

[^4]: [科技新報 — TSMC 3nm利用率達100%](https://technews.tw/2025/05/26/tsmcs-2nm-process-is-expected-to-reach-full-capacity-in-four-seasons/) — Se estima que la tasa de rendimiento de los procesos avanzados de TSMC es superior a la de los competidores; los números específicos de rendimiento son estimaciones de terceros, no revelaciones oficiales

[^5]: [天下雜誌 — 李國鼎與台積電誕生](https://www.cw.com.tw/article/5095492) — Morris Chang fundó TSMC en 1987, estableciendo el modelo de "subcontratación pura", sentando las bases de la división de trabajo de la industria global de semiconductores; contexto de la transferencia tecnológica de 4,5 millones de dólares de RCA en 1973

[^6]: [中央研究院 — 20 位元超導量子晶片公告](https://www.sinica.edu.tw/News_Content/56/2375) — El ASMC completó el chip cuántico superconductor de 20 qubits en diciembre de 2025, se conectó el 29 de enero de 2026; el tiempo de coherencia T1 alcanza 530 microsegundos

[^7]: [泛科學（PanSci） — 氮化鎵：用 1/3 的時間，得到一樣的電力](https://pansci.asia/archives/362660) — Autor: Redacción de PanSci. Banda prohibida de GaN 3,4 eV, voltaje de ruptura 10 veces, frecuencia de trabajo 1 MHz vs silicio 100 kHz; aplicación de carga rápida de vehículos eléctricos de 1000 voltios de SiC. Socio de Curación de Contenido según MOU 2026-05-05

[^8]: [TrendForce — TSMC exits GaN foundry by July 2027](https://www.trendforce.com/news/2025/08/22/news-tsmc-reportedly-exits-gan-foundry-business-by-2027/) — TSMC se retira de la subcontratación de GaN en julio de 2027, licencia tecnológica a World Semi (VIS) y GlobalFoundries; 稳懋 (3163) tiene una entrega mensual de aproximadamente 500 obleas de GaN de 6 pulgadas

[^9]: [富果直送 — 環球晶 SiC 8 吋晶圓 2025 量產](https://www.fugle.tw/news/article/1234567) — La capacidad de producción mensual de obleas de SiC de 6 pulgadas de GlobalWafers alcanzó 20.000 unidades a finales de 2024, hornos de crecimiento de cristales auto-desarrollados de 3 a 20 unidades, rendimiento > 50 %; estrategia de "Grupo IDM Virtual" de Hsu Hsiu-lan

[^10]: [科技新報 — SiC 供應鏈承壓](https://technews.tw/2025/11/sic-market-oversupply) — La expansión masiva de fábricas chinas de SiC en 2025 hizo que la tasa de utilización de capacidad de SiC de 6/8 pulgadas de GlobalWafers cayera por debajo del 50 %; se rumorea que la GPU Rubin de NVIDIA utilizará una capa intermedia de SiC + centro de datos de corriente continua de 800V de alto voltaje en 2027

[^11]: [SemiAnalysis — NVIDIA Blackwell CoWoS-L Analysis](https://www.semianalysis.com/p/nvidia-blackwell-b200-cowos-l) — NVIDIA Blackwell B200 utiliza CoWoS-L para integrar 2 GPUs Blackwell + 1 CPU Grace; velocidad de entrenamiento de IA 4 veces superior a H100; NVIDIA reserva capacidad CoWoS de TSMC hasta 2027

[^12]: [泛科學（PanSci） — 三維堆疊：先進封裝如何讓晶片走進雪山隧道](https://pansci.asia/archives/367588) — Autor: Redacción de PanSci. Principios de CoWoS / SoIC / TSV; metáfora de Ruta Nacional 9 vs Túnel de Xueshan; desafíos de rendimiento y disipación de calor en empaquetado 3D. Socio de Curación de Contenido según MOU 2026-05-05

[^13]: [Digitimes — TSMC CoWoS 產能擴張規劃](https://www.digitimes.com.tw/iot/article.asp?cat=158&id=0000696823_X1D7L8XB6JNL2Y8XLPZJK) — Capacidad mensual CoWoS de TSMC: 35.000 unidades a finales de 2024, 75.000 a finales de 2025, objetivo de 150.000 en 2028; NVIDIA reserva capacidad hasta 2027; obleas de Arizona enviadas de vuelta a Taiwán para empaquetado

[^14]: [泛科學（PanSci） — ALD 原子層沉積：50 年的薄膜革命](https://pansci.asia/archives/377669) — Autor: Redacción de PanSci. ALD desarrollada por Suntola en Instrumentarium Oy en 1974, tecnología consolidada en 1977, vendida a ASM en 1999; 55 % de cuota de mercado de ASM; principio de doble precursores de deposición química en fase vapor. Socio de Curación de Contenido según MOU 2026-05-05

[^15]: [科技新報 — Microsoft Majorana 1 拓樸量子處理器發表](https://technews.tw/2025/02/20/microsoft-majorana-1-topological-qubit/) — Microsoft presentó el procesador cuántico topológico Majorana 1 en febrero de 2025, afirmando que puede escalar a un millón de qubits

[^16]: [TSMC 官網 — A16 (1.6nm) 製程公告](https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm) — 2 nm adopta por primera vez transistores de nanohojas GAA (abandonando FinFET); A16 introduce por primera vez red de distribución de energía en el lado posterior (Super Power Rail), producción en masa en Q4 2026, 10 % más rápido que N2P a la misma potencia, 15-20 % ahorro de energía a la misma eficiencia

[^17]: [泛科學（PanSci） — 台灣量子科技：從 5 位元到量產時代](https://pansci.asia/archives/377923) — Autor: Redacción de PanSci. Ordenador cuántico de 5 qubits del ASMC en enero de 2024; tres rutas superconductoras vs trampas de iones vs topológicas; 53 qubits de Sycamore de Google resuelven problema de 10.000 años en 200 segundos. Socio de Curación de Contenido según MOU 2026-05-05

[^18]: [iThome — 量子國家隊 5 年 80 億預算](https://www.ithome.com.tw/news/151234) — Equipo nacional cuántico interministerial formado en marzo de 2022, presupuesto de 5 años de 8000 millones de NTD, 17 equipos de investigación; Oficina de Promoción de Tecnología de la Industria Cuántica establecida por el Ministerio de Asuntos Económicos en abril de 2026

[^19]: [中央社 2024/03/06 — 工研院量子控制晶片](https://www.cna.com.tw/news/ait/202403060123.aspx) — IRIS utiliza el proceso de 28 nm de TSMC para crear chip de control cuántico de baja temperatura de 4 K (-269 °C), volumen reducido en 40 %, consumo de energía más del 50 % inferior a grandes fabricantes internacionales; ruta de desarrollo 1 qubit en 2024 → 20 qubits en 2026-2027

[^20]: [TechNews — Google Sycamore 量子霸權](https://technews.tw/2019/10/24/google-sycamore-quantum-supremacy/) — En 2019, el ordenador cuántico Sycamore de 53 qubits de Google alcanzó la supremacía cuántica, completando en 200 segundos una tarea de cálculo que a un supercomputador tradicional le tomaría 10.000 años

[^21]: [SemiAnalysis — TSMC Arizona Fab 21 投資規劃](https://www.semianalysis.com/p/tsmc-arizona-1650b-capex) — Inversión de 165.000 millones de dólares en tres fases de Fab 21 de TSMC en Arizona; Fase 1 (4nm) en 2025, Fase 2 (3nm/2nm) en 2027, Fase 3 (2nm/A16) antes de 2030; principio N-2: el extranjero siempre está dos generaciones por detrás de Taiwán

[^22]: [Digitimes — ESMC Dresden 2027 量產](https://www.digitimes.com.tw/news/esmc-dresden-2027) — TSMC posee el 40 % de ESMC; planta de chips de automóvil de 28/22/16/12 nm en Dresde, Alemania, instalación de equipos en H2 2025, producción en masa en 2027, capacidad de producción mensual de aproximadamente 40.000 unidades

[^23]: [天下雜誌 — 台積電水資源消耗](https://www.cw.com.tw/article/5128456) — Consumo diario de agua de los tres parques científicos de TSMC superior a 208.000 toneladas; grupos ambientalistas estiman que el consumo de agua aumentará a 770.000 toneladas/día después de 2025 con la puesta en marcha de nuevas plantas; respuesta de TSMC: cada gota utilizada 3,5 veces, tasa de reciclaje 87 % (nuevas plantas 90 %), 5,54 millones de metros cúbicos de ahorro de agua agregados en 2024

[^asml-philips]: [Wikipedia — ASML Holding](https://en.wikipedia.org/wiki/ASML_Holding) — ASML se fundó el 1 de abril de 1984 como una joint venture 50/50 de ASM Lithography de Philips (Países Bajos) y ASM International (ASMI); después de la cotización en bolsa en 1995, ASMI se retiró, hoy ASML es el único proveedor de equipos de litografía EUV del mundo

[^lin-bio]: [Wikipedia — Burn-Jeng Lin](https://en.wikipedia.org/wiki/Burn-Jeng_Lin) — Burn J. Lin nació en Vietnam en 1942, trabajó en tecnología de litografía en el Centro de Investigación Watson de IBM desde la década de 1970, se unió a TSMC en Taiwán en 2000 como director de la División de Investigación; recibió el Premio SPIE Frits Zernike en 2008; apodado "Padre de la Litografía de Inmersión"

[^157nm-fail]: [Electronics Weekly — Immersion litho sidelines 157nm](https://www.electronicsweekly.com/news/research-news/process-rd/immersion-litho-sidelines-157nm-2005-05/) — La ruta de 157 nm fue reemplazada por la inmersión de 193 nm después de 2002-2003 debido a problemas de birrefringencia en lentes de fluoruro de calcio (CaF₂), fuerte absorción de películas delgadas a 157 nm y dificultades de integración de procesos; la apuesta de Intel + Nikon falló

[^immersion-litho]: [Wikipedia — Immersion lithography](https://en.wikipedia.org/wiki/Immersion_lithography) — Burn J. Lin presentó la litografía de inmersión de 193 nm en SPIE en 2002; el índice de refracción del agua de 1,44 hace que la resolución equivalente de 193 nm sea de aproximadamente 134 nm; ASML produjo en masa en 2007, sosteniendo desde 65 nm hasta 7 nm, extendiendo la Ley de Moore por seis generaciones

[^cw-lin-interview]: [天下雜誌 CommonWealth — Interview with the Father of Immersion Lithography Who Put TSMC on the Map](https://english.cw.com.tw/article/article.action?id=3720) — Entrevista a Burn J. Lin el 18-06-2024 — Contexto histórico de "Nikon no se atrevió a hacer inmersión"; Burn J. Lin impulsó la adopción de litografía de inmersión en TSMC desde 2000, 30 años de vínculo tecnológico entre TSMC y ASML
