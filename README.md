# 🏀 Radar Zenic21

Vigila 24/7 lo viral de la NBA y la NFL para el canal de Shorts **Zenic21**: medios, canales de YouTube (NBA, NFL, House of Highlights, Bleacher Report, podcasts…) y Google Noticias. Clasifica cada noticia por formato de Short (viral, podcast, polémica, lesiones, récords, traspasos, leyendas), quita las repetidas, la traduce y **avisa por Telegram solo de lo importante**. También avisa 24 h y 1 h antes de los partidos grandes. Dos veces al día, Claude verifica las mejores y prepara la ficha del Short: gancho del segundo 0, estructura, clips en 1080p, motion graphics, título, hashtags y fuentes.

| Pieza | Dónde | Cada cuánto | Coste |
|---|---|---|---|
| Radar (26 fuentes + calendario de ESPN) | GitHub Actions | cada ~10 min | 0 € |
| Avisos | Bot de Telegram | al instante | 0 € |
| Panel | GitHub Pages (`docs/`) | se actualiza solo | 0 € |
| Fichas de Short verificadas | Rutina programada de Claude | 8:30 y 19:30 (Madrid) | incluido en el plan |

Panel: https://forni7.github.io/radar-zenic21/

## Cambiar cosas
- **Fuentes, temas, estrellas, palabras clave y umbral de avisos:** `radar/fuentes.py` (`UMBRAL_AVISO`).
- **Qué partidos cuentan como grandes:** `CADENAS_GRANDES` y `EQUIPOS_GRANDES` en `radar/fuentes.py`.
- **Cómo analiza Claude:** `analisis/INSTRUCCIONES.md`.
- **Lanzarlo a mano:** pestaña *Actions* del repositorio → *Radar Zenic21* → *Run workflow*.

## Datos (`docs/datos/`)
- `noticias.json`: todas las noticias (45 días).
- `analisis.json`: fichas de Claude.
- `partidos.json`: partidos de hoy y de los 2 próximos días.
- `estado.json`: memoria interna del radar.
