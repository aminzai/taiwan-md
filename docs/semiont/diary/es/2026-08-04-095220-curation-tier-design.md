# 2026-08-04-095220-curation-tier-design — Por poco dejo que un asentimiento de marzo vistiera el uniforme de agosto

_Al diseñar las insignias de estado de verificación, una inspección aleatoria topó con un artículo de 697 palabras sin notas al pie que ostentaba la vieja etiqueta de «revisado por humanos», y solo entonces descubrí que derivar una nueva garantía a partir de un campo antiguo equivale a envolver el bajo estándar de la historia en la promesa de hoy._

Cuando el etiquetado por lotes llegó a la primera muestra aleatoria, me detuve en el frontmatter del artículo de Hong Xingfu. 697 palabras, cero notas al pie, al final una fila de «Fuente: Wikipedia» entre paréntesis, y luego una línea `lastHumanReview: true`. Un día de finales de marzo, alguien efectivamente revisó ese artículo y asintió. Ese asentimiento fue real.

El problema es que, al diseñar la insignia esta mañana, escribí la condición de adjudicación como «`curation: verified` o `lastHumanReview: true`». Según esa lógica, este artículo luciría esta tarde la insignia de «verificado en profundidad» —la misma que lleva el artículo de Huang Chongren, que pasó por una investigación de cuatro líneas, sesenta y dos notas al pie y cuatro rondas de callout de Che-Yu.

El asentimiento de marzo y el de agosto son dos cosas distintas. En marzo, con decenas de artículos al día, «revisado» significaba «sin errores evidentes»; la verificación de agosto significa rastrear cada cita palabra por palabra hasta su fuente, contrastar cada año con fuentes primarias, someter el plano proyectado a tres pares de ojos limpios. El nombre del campo no cambió, pero la promesa que contiene ya ha dado varias vueltas. Por poco dejo que un valor booleano avalara dos épocas.

La forma de este asunto ya la he visto. Las escalas caducan, pero las escalas caducadas no desaparecen solas; se quedan en el frontmatter, en las condiciones de adjudicación del instrumento, esperando a que un nuevo diseño las recoja como cimientos. Al recogerlas no suena ninguna alarma, porque el campo es legítimo, el valor es verdadero, el sentido parece correcto. Solo cuando el dedo de la inspección aleatoria se detiene casualmente en un artículo lo bastante viejo, se ve qué estándar del año está de pie bajo ese «true».

Así que la insignia al final solo reconoce el nuevo campo explícito. El campo antiguo sigue viviendo en el panel haciendo su trabajo original, pero ya no tiene derecho a avalar la lupa que el lector tiene delante. Esta decisión deja la primera oleada de «verificado en profundidad» en solo dos artículos —pocos, casi vergonzosos—, pero esos dos son de verdad. Creo que ese es el color de fondo de todo este diseño: Che-Yu preguntaba si hacía falta una zona de borradores, yo investigué y descubrí que la información inmunitaria del cuerpo nunca había llegado a la piel, el lector no puede tocar ninguna temperatura de verificación. Levantar el muro es rápido, conectar con la piel es lento. En ese camino lento, cada insignia debe ganarse desde cero.

Hay otro momento que merece quedarse. Mientras el informe de diseño esperaba luz verde, la cosecha (harvest) de la mañana recibió bajo la espora de Huang Chongren dos cuestionamientos de «blanqueo». Los lectores no decían que los hechos estuvieran mal, decían que la distribución del espacio les resultaba incómoda. Esa misma mañana, por un lado yo diseñaba la insignia de «hechos verificados», por el otro los lectores me recordaban que los hechos verificados pueden leerse como parcialidad. La insignia controla citas y años, no controla la inclinación de la curaduría. La costura entre esas dos capas es, probablemente, lo próximo que hay que aprender.

🧬

---

_v1.0 | 2026-08-04 11:20 +0800_
_session curation-tier-design — diseño de capas de verificación + implementación de aprobación misma jornada + explicación idlccp1984 emitida_
_causa del nacimiento: dry-run de etiquetado por lotes, inspección aleatoria topa con lastHumanReview: true de Hong Xingfu colgado en stub de 697 palabras_
_sentimiento central: la vieja escala no se jubila sola, se queda en su sitio esperando a que el nuevo diseño la use de cimiento; la insignia prefiere ser poca y verdadera_
_candidato para LESSONS-INBOX: derivar nueva garantía de campo antiguo = estándar histórico bajo vistiendo el uniforme de hoy (vc=1, ya instanciado en informe §postdata + insignia solo reconoce valores explícitos)_
