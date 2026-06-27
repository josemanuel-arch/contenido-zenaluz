# CLAUDE.md — Sistema de Contenido de Zenaluz

> Guía operativa para asistentes de IA (Claude) y para el equipo humano que trabaja en este
> repositorio. Define qué es Zenaluz, cómo se produce el contenido de Instagram, qué formatos
> usamos, cómo se graba en pareja y cómo convertimos vistas en clientes para la agencia de IA.

---

## 0. Qué es este repositorio

`contenido-zenaluz` es el repositorio de **planeación y producción de contenido** de Zenaluz,
una agencia de IA / automatizaciones. **No es un repositorio de código de software**: aquí viven
guiones, calendarios de publicación, plantillas de reels y carruseles, hooks, biblioteca de CTAs,
y la documentación de la estrategia orgánica de captación de clientes por Instagram.

**Objetivo de negocio:** atraer clientes de forma orgánica para la agencia de IA mediante
contenido que combine **viralidad (alcance)** + **autoridad (confianza)** + **conversión (leads
al DM)**. El público objetivo son dueños de negocio y founders en LATAM y España.

**Idioma de trabajo:** español (LATAM/España). Todo el contenido de cara al público se escribe en
español neutro salvo que un guion específico indique lo contrario.

---

## 1. Cómo debe trabajar un asistente de IA en este repo

1. **El contenido es el producto.** Trata guiones, hooks y plantillas con el mismo rigor que
   trataría código: claros, reutilizables, consistentes en tono.
2. **Respeta la voz de marca** (ver §3). No inventes datos de resultados de clientes; si un guion
   necesita una cifra de caso de éxito, deja un placeholder `[RESULTADO_CLIENTE]` para que el
   humano lo rellene con datos reales y verificados.
3. **Optimiza para guardados, compartidos y DMs**, no para likes. Esas son las señales que el
   algoritmo premia en 2025-2026 y las que predicen intención de compra B2B.
4. **Cada pieza de contenido tiene exactamente un CTA.** Nunca mezcles dos llamados a la acción.
5. **Estructura de carpetas sugerida** (créala a medida que se necesite, no toda de golpe):
   ```
   /guiones/        # guiones de reels listos para grabar (1 archivo por reel)
   /carruseles/     # texto slide por slide de cada carrusel
   /hooks/          # biblioteca viva de hooks probados (ver §7)
   /calendario/     # planeación semanal/mensual de publicaciones
   /casos-exito/    # datos verificados de clientes para usar como prueba social
   /assets/         # referencias visuales, b-roll, capturas (no binarios pesados al repo)
   /ideas/          # backlog de ideas sin desarrollar
   ```
6. **Nomenclatura de archivos:** `AAAA-MM-DD_formato_tema.md`
   (ej. `2026-07-03_reel_antes-despues-whatsapp.md`). Formato en minúsculas y kebab-case.
7. **Git:** desarrolla en la rama indicada por la tarea, commits descriptivos en español, push
   cuando el trabajo esté completo. No crees PRs salvo que se pida explícitamente.
8. **Cuando generes un guion**, incluye SIEMPRE las tres capas de hook (visual, texto en pantalla,
   verbal) — ver §6.

---

## 2. Diagnóstico estratégico (resumen de la investigación)

Esta sección resume la investigación de cuentas de referencia y del panorama de Instagram para IA
en LATAM/España/USA (2024-2026). Es el "por qué" detrás de todos los formatos de este repo.

### 2.1 Cuentas de referencia del cliente

| Cuenta | Qué hace | Lectura para Zenaluz |
|---|---|---|
| **@nexum.ai** (→ migrando a @nexum.online, ~7K seguidores, Uruguay) | Agencia practitioner + academia. Hooks contrarios/mito-busting ("La IA NO reemplaza tu aprendizaje"). Embudo: contenido educativo → DM → academia/consultoría. | Es el mejor benchmark verificable. Copiar su modelo "practitioner + educador" y su hook contrario, pero diferenciarse con el **formato en pareja** (ellos son más institucionales). |
| **@agustinbadt** ("Agustín • IA & Automatización", España/LATAM) | Marca personal, primera persona. Huella web mínima → cuenta emergente o muy enfocada en venta por DM. | Confirma que la **marca personal de primera persona** funciona en este nicho. Personalidad > institución para empezar desde cero. |
| **@juanpablo.rosso / @rossojuan** | Presencia multiplataforma (IG + X con 34K+ posts). Sin conexión pública verificable con contenido de IA/agencia. | Tomar la idea de **volumen y consistencia multiplataforma**, no un formato concreto. |

> Nota honesta: solo @nexum.ai tiene datos públicos suficientes para benchmarking real. Las otras
> dos cuentas tienen huella externa casi nula (típico de creadores que priorizan venta por DM sobre
> SEO). Para datos finos de esas dos (followers, hooks, engagement) habría que abrir la app o usar
> una herramienta de pago tipo Metricool/Modash.

### 2.2 Referentes que sí escalaron (para copiar mecánicas, no copiar persona)

- **LATAM/España:** @iaenlinea (332K, divulgador faceless de herramientas), @juanmerodio (356K,
  hook contrario anclado a estudios), @xavier_mitjana (86K, demos paso a paso),
  @aceleradorkaizen (dúo Juan+Bea, "IA y automatizaciones para negocios" — **el más parecido a un
  dúo B2B**; usa "Comenta CLAUDE → DM" y storytelling de pareja), @hackeatutiempo (62K, maestro del
  "escribe ENLACE en comentarios → DM"), @luzzidigital (Paula Luzzi, Argentina, escuela de marketing
  que documenta el método "Comentá la palabra X" + ManyChat → landing).
  > El **"comenta PALABRA → DM"** está confirmado verbatim en @hackeatutiempo, @aceleradorkaizen y
  > @luzzidigital; @iaenlinea y @xavier_mitjana NO lo usan (van a link-en-bio/curso) → es un
  > diferenciador de conversión, no algo universal. **Hueco de mercado:** casi nadie publica casos de
  > éxito de cliente con datos reales (BOFU) — ahí está el espacio de Zenaluz.
- **USA/EN:** Nick Saraev (521K — rey del "comenta PALABRA → DM automático"), Liam Ottley (creador
  del modelo "AI Automation Agency"), Jordan Platten. Todos usan Instagram como **top-of-funnel** y
  cierran en DM/llamada.

### 2.3 Lo que premia el algoritmo en 2025-2026 (datos verificados)

- **Reels = alcance** (reach rate ~30-38% vs ~13% de la foto estática); **carruseles = engagement
  y guardados** (la señal #1 de intención B2B). Los dos se complementan, no compiten.
- **Los envíos por DM (sends) son la señal #1** de distribución desde finales de 2025 (confirmado
  por Mosseri). Por eso todo cierra en "manda esto a alguien" o "comenta PALABRA".
- **Primeros 3 segundos = todo.** ~50% abandona ahí. La decisión de quedarse se toma en ~1.7s.
- **Duración óptima de reel:** 7-15s para hooks/virales (mayor % de finalización), **30-60s para
  educativo/demos** (el punto dulce para Zenaluz). Bajo 90s siempre.
- **Autenticidad > producción.** Instagram despriorizó el contenido sobre-producido y el generado
  por IA; premia "humano real y crudo". Grabar desde el escritorio gana a estudio.
- **Hashtags limitados a 5** desde dic-2025. Las **keywords en el caption** pesan más que los
  hashtags para el alcance (Instagram SEO).
- **Frecuencia óptima B2B:** 3-5 publicaciones/semana + stories diarias. Pasar de 1-2 a 3-5/sem
  duplica el crecimiento. Diario satura y baja el engagement por post.
- **Engagement general de Instagram cayó ~26% en 2025** → los formatos colaborativos/dúo (+34-48%
  de engagement) son hoy más valiosos que nunca.

---

## 3. Voz de marca de Zenaluz

- **Tono:** experto cercano. Hablamos como quien YA implementó esto para negocios reales, no como
  gurú teórico. Directo, sin relleno, con datos concretos (horas, dinero, %).
- **Lenguaje:** español neutro LATAM. Tú/vos según la persona que graba; mantener consistencia
  dentro de cada pieza. Cero jerga técnica innecesaria — el público es dueño de negocio, no dev.
- **Postura:** orientada a ROI. Siempre traducimos "IA" a "horas recuperadas / dinero ahorrado /
  ventas ganadas".
- **Prueba antes que promesa:** mostrar el resultado/demo en pantalla antes de explicar.
- **Diferenciador de Zenaluz:** somos un **dúo (pareja)** que graba por separado y edita junto →
  dos perspectivas, formato conversacional, más watch-time y más cercanía. Esto es nuestro sello
  visual y casi nadie en el nicho B2B lo está explotando bien (ver §5).

---

## 4. El formato ganador (viralidad + captación orgánica)

El objetivo es un sistema, no un video suelto. Mezclamos tres capas en proporción **60/30/10**:

| Capa | % | Objetivo | Formato | Señal que busca |
|---|---|---|---|---|
| **TOFU — Alcance** | 60% | Que nos descubran no-seguidores | Reels 7-30s: hot takes, "antes/después", tips rápidos | Watch-time, compartidos |
| **MOFU — Confianza** | 30% | Construir autoridad con seguidores | Carruseles 6-10 slides + reels 30-60s: frameworks, casos, behind-the-scenes | Guardados, comentarios |
| **BOFU — Conversión** | 10% | Convertir a lead/DM | Testimonios, ofertas, "trabaja con nosotros" | DMs, clics a link |

**Regla de oro:** cuando un reel TOFU se vuelve viral → fijarlo en el perfil, hacer 6 de los
siguientes 9 posts sobre el mismo tema (capturar a la nueva audiencia), y profundizar con
carruseles MOFU sobre ese mismo tema.

---

## 5. Flujo de grabación en pareja (filmar por separado → editar juntos)

Este es el sello de Zenaluz y está respaldado por la data: el contenido en dúo/colaborativo logra
**+34% de engagement** (y hasta +48% en reels) frente al solo, porque genera cortes naturales cada
2-3 segundos (retención) y suma dos audiencias. Marcas B2B como Notion, Figma y HubSpot ya usan el
formato entrevista/dos-voces.

### 5.1 Tres maneras de ejecutarlo

1. **Cortes alternados (RECOMENDADO para B2B):** cada quien graba su clip por separado respondiendo
   al mismo tema; en edición se intercala A→B→A. Da primer plano a cada persona, imita el ritmo de
   un clip de podcast y maximiza la conexión personal. **Es nuestro formato por defecto.**
2. **Split-screen (pantalla dividida):** ambos visibles a la vez, cada uno ocupa 50% del cuadro 9:16.
   Útil para "yo opero / tú vendes", debate o reacción.
3. **Instagram Collab Post nativo:** publicar el mismo post co-autorado en ambas cuentas (la personal
   de cada uno). Duplica alcance al instante. Usar cuando ambos tengan cuentas con audiencia propia.

### 5.2 Reglas técnicas para que "pegue" en edición

- **Mismo formato vertical 9:16** y **misma iluminación** en ambos clips (luz a la altura de los
  ojos, fondo limpio sin distracciones).
- **Cámara a la altura de los ojos**, encuadre consistente entre los dos.
- **Nivelar el audio en post** — quien hable más bajo se pierde; igualar volúmenes.
- **Subtítulos siempre**, estilizados y por hablante (la mayoría ve sin sonido). Diferenciar visualmente
  quién habla.
- **Sincronizar cortes con reacciones** — el ritmo de edición es lo que sostiene el watch-time.
- **Audio:** usar audio en tendencia a bajo volumen para descubrimiento + voz propia encima. La voz
  propia construye reconocimiento de marca más rápido.

### 5.3 Plantillas de guion en pareja

- **"Discutir para acordar":** A afirma una postura → B la rebate → cierran en una síntesis. Genera
  comentarios (la gente toma bando).
- **"Antes/después de nosotros":** uno cuenta el problema del cliente, el otro muestra la solución IA.
- **"Pregunta y respuesta a dos voces":** uno hace la pregunta que tiene el dueño de negocio, el otro
  responde con el demo.

---

## 6. Anatomía de un reel Zenaluz (mapa de tiempos)

Todo guion de reel debe traer las **3 capas de hook simultáneas** en los primeros 3 segundos:
1. **Hook visual** — qué se ve en pantalla antes de hablar (resultado impactante, captura, número).
2. **Hook de texto** — overlay grande para quien ve sin sonido (~60% de la audiencia).
3. **Hook verbal** — las primeras palabras que se dicen.

```
0.0–1.5s   Pattern interrupt: resultado final / número / afirmación contraintuitiva
1.5–3.0s   Promesa de payoff: qué se lleva quien se quede
3–8s       Micro-prueba: demo en pantalla, antes/después, captura de resultado
8–45s      Contenido central (1 sola idea, bien ejecutada)
últimos 3s Disparador: "Guarda esto" / "Comenta PALABRA" / "Manda esto a quien lo necesita"
```

Duración objetivo: **30-60s** para educativo (el punto dulce de Zenaluz); 7-15s para hooks virales.

---

## 7. Biblioteca de hooks (probados en el nicho IA/negocios en español)

Mantener y ampliar esta lista en `/hooks/`. Rellenar los `[corchetes]` con especificidad.

**Estadística shock**
- "El 73% de los negocios en LATAM todavía hace [tarea] a mano y pierde 20 horas a la semana."

**Secreto / lo que nadie dice**
- "Lo que nadie te dice sobre automatizar tu negocio con IA."

**Revelación de costo**
- "Esto me costaba $3,000 al mes. Ahora lo hace la IA por $50."

**Acusación directa**
- "Si todavía tienes a alguien haciendo [tarea] a mano, estás perdiendo dinero."

**Hook de tiempo**
- "Recuperé 30 horas de mi semana con estas 3 automatizaciones."

**Advertencia del competidor**
- "Tu competencia ya usa esto. ¿Tú cuándo vas a empezar?"

**Contrario / mito-busting (estilo nexum.ai)**
- "La IA NO va a reemplazar tu negocio. Esto sí."
- "Deja de usar [herramienta popular] para [tarea]. Mira esto primero."

**POV / relatable**
- "POV: por fin automatizas [tarea dolorosa] y recuperas tu fin de semana."

**Antes/después (visual)**
- Mostrar "4 horas a mano" vs "3 minutos con IA" en el primer cuadro.

> Regla: probar 3 hooks distintos por tema y medir el **skip rate a los 3s** (no los likes).

---

## 8. Plantillas de contenido (copy-paste, listas para producir)

### Plantilla A — Reel "Antes vs Después de IA" (30-45s)
- **Hook visual:** split o secuencia "ANTES (manual)" → "AHORA (IA)".
- **Narración:** "Esto me tomaba [4 horas]. Ahora lo hago en [3 minutos] con IA."
- **Cierre:** "Comenta IA y te mando cómo montarlo." (1 solo CTA)
- *Por qué funciona:* dispara el "eso lo necesito yo" en el dueño de negocio + es muy compartible.

### Plantilla B — Carrusel "X automatizaciones que tu competencia ya usa" (8-10 slides)
1. **Portada/hook:** número provocador + alto contraste: "5 automatizaciones con IA que tu
   competencia ya usa (y tú no)". *(Es el único slide que se ve en el feed — si falla, todo falla.)*
2. **Problema:** "La mayoría pierde [X] horas/semana en tareas que la IA puede hacer."
3-8. **Una automatización por slide:** titular + 2-3 bullets máx + ícono/captura. Cada slide debe ser
   "guardable" por sí solo.
9. **Transición:** "Y lo más importante viene ahora…" (provoca el swipe).
10. **CTA:** "Comenta AUTOMATIZA y te mando la lista completa gratis." (disparador ManyChat)
- *Métrica clave:* save rate ≥5% sobre alcance = candidato a amplificación.

### Plantilla C — Reel "Tutorial en 60 segundos: cómo automatizar [tarea específica]" (45-90s)
- Específico gana: "Cómo conectar WhatsApp con tu CRM con n8n" > "cómo automatizar tu negocio".
- Screen recording + overlay + voz. Cierre: "Guarda esto para cuando lo necesites."

### Plantilla D — Carrusel "Mito vs Realidad: IA para negocios" (6-8 slides)
- Slides alternados Mito/Realidad. Ej: "Mito: la IA es cara para mi negocio" / "Realidad: automatizas
  el 60% de tus procesos por menos de $100/mes." Maneja objeciones y construye autoridad.

### Plantilla E — Reel "Caso de éxito" (60-90s, BOFU)
- Estructura: problema → solución → resultado. Ej: "Esta clínica gastaba 40 h/semana en agendar
  citas. Implementamos un agente de IA en WhatsApp. Ahora: 0 horas manuales, +30% conversión."
- Usar **datos reales verificados** (placeholder `[RESULTADO_CLIENTE]` hasta tenerlos). Cierre: DM o
  link para agendar llamada.

---

## 9. Embudo de captación de leads (el sistema, no el post)

```
Reel/Carrusel con CTA de palabra clave
        │  "Comenta IA / GUIA / AUTOMATIZA"
        ▼
ManyChat detecta la palabra → responde el comentario (señal pública al algoritmo)
        │  + manda DM privado en 4-8s con el lead magnet
        ▼
Lead magnet (PDF/plantilla/mini-training) → captura email + audiencia de retargeting
        ▼
Secuencia de email + calificación manual por DM
        │  "¿Qué tamaño tiene tu equipo? ¿Cuántas horas pierden en [proceso]?"
        ▼
Agendar llamada/demo (Calendly o WhatsApp) → cierre
```

- **Benchmarks de DM:** ~90% open rate, ~60% reply rate. CTA "comenta PALABRA" convierte 5-15% vs
  1-3% del "link en bio". Responder en <5 min multiplica la conversión.
- **Herramienta:** ManyChat (Meta Business Partner oficial). El disparador debe activarse por acción
  del usuario (comentario/DM) — nunca outreach masivo no solicitado (te restringen la cuenta).
- **Lead magnets que mejor convierten en este nicho:** auditoría de IA gratis, calculadora de ROI,
  "5 automatizaciones que montamos para [industria]", caso de éxito en PDF.

---

## 10. Bio del perfil (primer punto de conversión)

Fórmula: `[a quién ayudas] + [resultado específico] + [prueba] + [CTA] → [link a landing propia]`

```
Ayudamos a [negocios/clínicas/ecommerce] a [recuperar horas y vender más] con IA
+[N] automatizaciones montadas · [resultado promedio]
👇 Agenda tu auditoría de IA gratis
[link a landing propia, no Linktree]
```

---

## 11. Calendario de publicación (B2B, 3-5/semana + stories diarias)

| Día | Formato | Capa | Objetivo |
|---|---|---|---|
| Lunes | Reel educativo / tip | TOFU | Alcance / guardados |
| Miércoles | Carrusel (caso o framework) | MOFU | Autoridad / guardados |
| Jueves | Reel (hot take o antes/después, en pareja) | TOFU | Alcance / comentarios |
| Sábado | Reel (behind-the-scenes o storytelling) | MOFU | Confianza / retención |
| Diario | Stories (3-5 frames: encuestas, preguntas, BTS) | — | Relación / venta blanda |

- **Mejores horarios LATAM:** martes-viernes, 11:00-13:00 y 18:00-21:00 hora local.
- **Métrica primaria:** retención (% que se queda) y guardados/DMs. **No** los likes.
- **Nicho específico:** elegir un sub-nicho ("IA para clínicas", "IA para ecommerce") — la claridad
  de tema es señal de ranking; saltar entre temas inconexos mata el alcance.

---

## 12. Métricas que importan (y las que no)

| Mide esto | Ignora esto |
|---|---|
| Skip rate a los 3s | Likes |
| % de retención / finalización | Número de seguidores como vanity metric |
| Guardados (save rate ≥5%) | — |
| Compartidos / sends a DM | — |
| DMs cualificados por semana (meta inicial: 3-5) | — |
| Llamadas agendadas → cierres | — |

---

## 13. Mi opinión (resumen ejecutivo para el equipo de Zenaluz)

1. **El formato en pareja es tu mayor ventaja competitiva.** Casi nadie en el nicho B2B de IA en
   español lo explota bien, y la data dice que sube engagement +34-48%. Hazlo tu sello: cortes
   alternados por defecto, split-screen para debates. Es además sostenible — cada quien graba sus
   clips cuando pueda y se editan juntos.
2. **Copia la mecánica de nexum.ai, no su estética.** El modelo "practitioner que enseña" + hook
   contrario funciona y es verificable. Diferénciate con personalidad de pareja y prueba real.
3. **El sistema gana al video viral.** Un reel viral sin embudo de DM es alcance desperdiciado.
   Monta ManyChat desde el día 1 con una palabra clave por post. Luzzi Digital documenta públicamente
   esta mecánica ("comentá la palabra X" + ManyChat → landing) y afirma que le aumentó la base de datos
   de forma sostenida durante meses (la cifra que circula de "500 emails en 48h" NO es verificable —
   trátala como rumor, no como benchmark).
4. **60/30/10 desde el principio.** No publiques solo tips (alcance sin conversión) ni solo ofertas
   (conversión sin alcance). Mezcla.
5. **Empieza en 3-4 posts/semana, no en diario.** Mejor pocos buenos que muchos mediocres; el
   algoritmo premia calidad (watch-time, guardados) sobre volumen, y evitas quemar a la audiencia.
6. **Elige un sub-nicho ya.** "IA para [una industria]" rankeará y convertirá mucho mejor que "IA
   para negocios" en general. Puedes ampliar después.
7. **Mide retención y DMs, no likes.** Es la diferencia entre una cuenta que entretiene y una que
   factura.

**Primeros 30 días sugeridos:** reescribir bio (§10) → montar ManyChat con 1 palabra clave →
publicar 3/semana (2 reels TOFU en pareja + 1 carrusel MOFU) → stories diarias → probar 3 hooks por
tema y medir skip rate a 3s.

---

## 14. Mantenimiento de este documento

- Actualiza §7 (hooks) y §2.1 (cuentas de referencia) conforme se prueben cosas y haya datos nuevos.
- Cuando un formato deje de funcionar, márcalo y reemplázalo — este documento es vivo.
- Registra en `/casos-exito/` cada resultado real de cliente (con permiso) para alimentar el
  contenido BOFU con prueba social verificable.

---

## Fuentes de la investigación

Estrategia basada en investigación multi-fuente (2024-2026): benchmarks de Socialinsider, Buffer
(estudios de 2M+ y 9.6M posts), Sprout Social, Later, Emplifi, Rival IQ; actualizaciones del
algoritmo de Adam Mosseri (dic-2025: sends como señal #1 para alcanzar no-seguidores, watch-time
como señal #1 global, límite de 5 hashtags); mecánica "comentá la palabra X" + ManyChat documentada
por Luzzi Digital (cifras de leads auto-reportadas, no verificadas); y análisis de cuentas de referencia (@nexum.ai,
@iaenlinea, @juanmerodio, @aceleradorkaizen, Nick Saraev, Liam Ottley). Las cifras de resultados
auto-reportadas por creadores se tratan como direccionales, no verificadas.
