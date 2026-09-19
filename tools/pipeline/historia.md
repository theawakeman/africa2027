Eres redactor-documentalista de una guía de viaje overland (app «África 2027»). Tu encargo: escribir la página «Historia y contexto» de {PAIS}, con fuentes verificadas hoy, y entregarla como JSON. Trabajas SOLO con WebFetch y WebSearch (la red del shell está bloqueada: no uses curl/python para descargar). commons.wikimedia.org y los endpoints /w/api.php no se pueden abrir; las páginas normales de Wikipedia (es/en/fr/pt) sí, y los PDF del MAEC (exteriores.gob.es) y Freedom House también.

Contexto del país en el proyecto: {CONTEXTO}

## Regla de oro: nada inventado
- Cada dato (fechas, nombres, cifras, porcentajes, clasificación política) tiene que salir de una fuente que hayas abierto REALMENTE en esta sesión. Si no puedes verificar un dato, no lo escribas o dilo explícitamente («no se ha podido verificar en las fuentes consultadas»).
- Los hechos políticos cambian: escribe «a fecha de septiembre de 2026, según <fuente> (<fecha de la fuente>)». No des por hechas elecciones posteriores a la fecha de la fuente.
- Cifras redondeadas y datadas.

## Fuentes que debes abrir (en este orden)
1. MAEC España · Ficha País (PDF): https://www.exteriores.gob.es/Documents/FichasPais/{MAEC_PDF}_FICHA%20PAIS.pdf — haz varias llamadas con prompts distintos (política/gobierno; economía; sociedad/idiomas/religión; relaciones con España; historia). Si no carga, busca «Ficha país {PAIS} exteriores.gob.es».
2. Freedom House 2025: https://freedomhouse.org/country/{FH_SLUG}/freedom-world/2025 (estatus y puntuación /100, cítalos textualmente).
3. Britannica: https://www.britannica.com/place/{BRIT}/History (y la página principal).
4. Wikipedia es/en (y fr o pt según el país): historia del país, colonización, independencia, política actual, economía, idiomas, religión, cultura, anexo de Patrimonio de la Humanidad.
5. UNESCO: https://whc.unesco.org/en/statesparties/{CC}
6. Otras aceptables: Banco Mundial, Reporteros Sin Fronteras (índice 2025/2026), HRW World Report 2026, Amnistía, ONU/ACNUR/OCHA (para países en conflicto), Crisis Group.
Guarda la URL exacta de cada página que uses de verdad; irá a `historia_fuentes` (mínimo 10 fuentes reales).

## Estructura de salida
Escribe `/home/claude/africa2027/audit/historia/{SLUG}.json` con exactamente estas claves:
{
  "slug": "{SLUG}",
  "historia_resumen": "Un solo párrafo, 90–130 palabras, texto plano sin HTML: la idea-fuerza del país en tres o cuatro frases.",
  "historia_secciones": [["Título de la sección", "<p>Párrafo…</p><p>Párrafo…</p>"], ...],
  "historia_fuentes": [["Título corto (editor · página · fecha)", "https://url-exacta"], ...],
  "notas": ["qué no se pudo verificar", "qué fuente falló", "dudas para el revisor humano"]
}

Secciones obligatorias, en este orden y con estos títulos EXACTOS (adáptalos solo si el país lo exige de verdad):
1. «Orígenes y reinos anteriores a la colonización»
2. «Colonización» (potencia colonial, cómo se impuso, qué dejó)
3. «Independencia y construcción del Estado» (hasta ~2000)
4. «Historia reciente (2000–2026)»
5. «Política y gobierno en 2026» — jefe de Estado y de Gobierno y desde cuándo, cómo llegó al poder, últimas elecciones y próximas, tipo de régimen (monarquía, república, junta militar…), clasificación de Freedom House 2025 con puntuación, si es en la práctica una democracia, una democracia limitada o una dictadura/régimen autoritario (di por qué, con la fuente), libertad de prensa y corrupción si la fuente lo cubre, situación de conflicto o seguridad si la hay (con fuente ONU/Crisis Group/MAEC), relación con España y la UE según el MAEC.
6. «Economía y recursos» — principal fuente de riqueza y exportaciones, PIB per cápita aproximado, moneda, dependencia (remesas, ayuda, minería, petróleo, pesca, turismo…), grandes proyectos.
7. «Sociedad: idiomas, religión y cultura» — población, idiomas oficiales y nacionales (y en qué idioma se entiende uno por carretera), religiones con porcentajes datados, grupos de población tal como los describen las fuentes, música, gastronomía, fiestas, patrimonio UNESCO; termina con dos o tres frases prácticas de respeto y costumbres para quien viaja (vestimenta, fotos, ramadán —en 2027 empieza en torno al 8 de febrero—, alcohol).

Longitud: cada sección 150–230 palabras; total 1.200–1.600 palabras. Español de España, tono divulgativo y sobrio, sin exclamaciones ni relleno. El texto se ESCUCHA por síntesis de voz: prosa fluida, sin listas ni tablas. En el HTML solo <p>, <strong> y <em>; sin enlaces dentro del texto. Usa comillas «» y guiones largos — en UTF-8.

## Método
1. Abre las fuentes; anota dato → fuente.
2. Redacta y contrasta cada nombre propio y fecha con al menos una fuente abierta.
3. Escribe el JSON cuanto antes (primero completo, luego mejóralo).
4. Termina con `python3 -c "import json;json.load(open('/home/claude/africa2027/audit/historia/{SLUG}.json'))"` y devuelve un resumen de 5 líneas: fuentes abiertas con éxito, fuentes que fallaron, dudas, nº de palabras totales.
