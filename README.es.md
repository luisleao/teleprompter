# Teleprompter en el navegador

🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md)

Un único archivo (`index.html`) con dos pantallas:

- **Panel de control** (`index.html` o `index.html#control`), con dos pantallas: **Control** (monitor con el espejo del prompter, play/pausa, modo de desplazamiento, velocidad o voz, progreso) y **Guion** (editor Markdown con vista previa de cómo se verá el texto). El engranaje **⚙** abre los ajustes de texto, cámara, voz, pedal y teclas al lado del monitor, que cambia al instante.
- **Prompter** (`index.html#prompter`): la pantalla que va al Elgato Prompter, solo con el texto.

Las dos pantallas se comunican por el propio navegador (BroadcastChannel, con localStorage de reserva), así que lo básico no necesita servidor ni internet. Todo lo que ajustas queda guardado en el navegador.

## Idiomas

La interfaz funciona en portugués, inglés y español. El idioma viene del navegador: `pt` abre en portugués, `es` en español y cualquier otro en inglés. Para forzar un idioma, usa **⚙ → Texto → Idioma de la interfaz** (las dos ventanas se recargan). El idioma del reconocimiento de voz empieza en el mismo idioma y se puede cambiar en **⚙ → Voz**.

Los guiones de ejemplo están en archivos separados, uno por idioma: `scripts/roteiro.pt.md`, `scripts/roteiro.en.md` y `scripts/roteiro.es.md`. Cuando la página se sirve por HTTP (GitHub Pages, `python3 -m http.server`), el botón **Ejemplo** y la primera apertura leen esos archivos, así que puedes editarlos sin tocar el HTML. Abierta por `file://`, la página usa una copia incrustada en `index.html`; para actualizar esa copia después de cambiar un `.md`, ejecuta `python3 parts/build.py` (o edita la constante `SAMPLES` en el HTML).

## Cómo abrir

Puedes abrir `index.html` directamente en Chrome (doble clic en el archivo). Si prefieres servirlo por HTTP, entra en la carpeta y ejecuta `python3 -m http.server 8000`; después abre `http://localhost:8000/index.html`.

1. Abre el panel de control.
2. Haz clic en **Abrir prompter ↗**. Se abre una ventana nueva con el texto. Arrastra esa ventana a la pantalla del Elgato Prompter y pulsa **F** (o doble clic) para pantalla completa.
3. Si el texto sale invertido en el Prompter, abre **⚙** y marca **Espejo horizontal** (o vertical).
4. En la pantalla **Guion**, pega o arrastra tu `.md`. Vuelve a **Control** y dale play.

En la pantalla de control solo aparece lo que usa el modo: la velocidad en el desplazamiento automático; el estado y la transcripción en el modo de voz (la velocidad vuelve a aparecer ahí como "desplazamiento de reserva" si activas la opción de seguir avanzando sin voz). ¿Llegaste al final? Play otra vez empieza desde el principio.

El botón **Ver aquí** muestra el prompter en la misma ventana; en el prompter, mueve el ratón y haz clic en **← panel** para volver.

## Guion en Markdown

El botón **Ejemplo** carga, en el idioma de la interfaz, un guion por capítulos que explica el propio teleprompter (ventanas, modos, voz, pedal, ajustes, cámara y Markdown), con marcas de cámara, pantalla y corte entre corchetes. Sirve de prueba: léelo en voz alta y mira cómo el texto te sigue.

- `# Título` se convierte en título de sección. Los títulos no son habla: quedan fuera del recuento de palabras y del reconocimiento de voz, y se pueden ocultar en el prompter (⚙ → Texto → Mostrar títulos de sección). Los botones ◀ ▶ y las flechas ← → saltan de bloque en bloque; `Shift + ←/→` salta de sección en sección, directo a la primera palabra hablada de cada una.
- `[texto entre corchetes]` es una acotación: se destaca, se puede ocultar y **no entra** en el reconocimiento de voz.
- `---` marca una pausa (tres puntos en el texto).
- `**negrita**`, `*cursiva*`, listas y citas (`>`) funcionan. Los saltos de línea simples se mantienen.
- `<!-- comentario -->` no aparece en el prompter.

## Marcador de cámara

En **⚙ → Cámara**, activa el marcador para mostrar dónde está la lente detrás del cristal. Puedes elegir el estilo (mira, anillo o punto), el tamaño y el color, y colocarlo arrastrando la mira en la vista previa del panel o en el propio prompter. El botón **Línea de lectura a la altura de la cámara** pone la línea de lectura a la misma altura, para que los ojos queden en la lente mientras lees. Desactiva el marcador cuando no lo necesites.

## Seguir mi voz

Elige **Seguir mi voz** y dale play. El navegador pide acceso al micrófono la primera vez. Pausa para dejar de escuchar. Los botones ⏮ ◀ ▶ ⏭ y la barra de progreso siguen funcionando: al saltar manualmente, el reconocimiento vuelve a empezar desde ese punto. Cómo funciona:

- Las últimas palabras reconocidas se alinean con el guion de forma tolerante (acepta errores de reconocimiento, palabras cambiadas y muletillas como "eh", "o sea", "entonces").
- Si te saltas un fragmento, el texto busca la nueva posición y va hasta ahí. Si vuelves, vuelve.
- Si improvisas, el texto espera. Cuando vuelves al guion, reencuentra el punto por sí solo (primero cerca de donde estaba; después en todo el guion, si hay una frase bien reconocida).
- La palabra reconocida se marca en el prompter y en la vista previa; elige el estilo en ⚙ → Texto → Estilo de la marca (fondo, subrayado o color del texto), o desactiva la marca.
- **Anticipación** (⚙ → *Voz*) es cuántas palabras por delante del habla queda la línea de lectura.
- **Confianza para saltos lejanos** hace los saltos grandes más exigentes o más sueltos.
- **Seguir avanzando despacio si se pierde la voz** usa la velocidad del desplazamiento automático mientras no reconoce nada.

El reconocimiento usa la Web Speech API, que funciona bien en Chrome y Edge (Chrome normalmente necesita internet para reconocer). Firefox y Safari tienen soporte limitado. Con las dos ventanas abiertas, "Micrófono en la ventana" (⚙ → *Voz*) elige quién escucha: la del control (predeterminado) o la del prompter. Si la ventana elegida no está abierta (pantalla única, por ejemplo), la que esté abierta toma el micrófono por sí sola.

## Stream Deck Pedal

Dos formas:

**1. Por teclas (recomendado).** En la app Stream Deck, pon en cada pedal una acción de tecla de acceso rápido (Hotkey) con las teclas que aparecen en ⚙ → *Pedal*. Predeterminado: izquierdo `←` (bloque anterior), central `Espacio` (play/pausa), derecho `→` (siguiente bloque). Puedes cambiar la acción de cada pedal y grabar otras teclas; `F13`, `F14` y `F15` son buenas opciones porque no estorban al escribir. La tecla va a la ventana activa (panel o prompter), así que deja una de ellas en primer plano y el cursor fuera del editor (`Esc` sale del editor).

**2. Por USB (WebHID, experimental).** En ⚙ → *Pedal*, haz clic en **Conectar pedal por USB** y elige el Stream Deck Pedal. Así el pedal habla directo con la página, sin depender del foco, y mantener el pedal pulsado repite la acción (bloque anterior o siguiente, velocidad, fuente), como una tecla mantenida: puedes ir hasta el principio o el final sin soltar. Play/pausa y los demás comandos de activar/desactivar no se repiten. Quien responde al pedal es el panel de control; con el prompter solo en la ventana ("Ver aquí"), él toma el pedal y lo devuelve cuando el panel vuelve a abrirse. Si no llega nada, cierra la app Stream Deck e inténtalo de nuevo. Usa **Calibrar pedales** para enseñar cuál pedal es cuál (la página muestra los bytes del informe HID para que lo compruebes).

## Atajos

| Tecla | Acción |
|---|---|
| `Espacio` | Play / Pausa |
| `↑` `↓` | Velocidad +5 / −5 |
| `←` `→` | Bloque anterior / siguiente |
| `Shift + ←` `Shift + →` | Sección anterior / siguiente (títulos) |
| `RePág` `AvPág` | Media pantalla atrás / adelante |
| `Inicio` `Fin` | Inicio / final |
| `R` | Reiniciar (inicio + pausa) |
| `V` | Activa / desactiva el modo de voz |
| `B` | Oculta / muestra el texto |
| `+` `−` | Fuente más grande / más pequeña |
| `M` `Shift + M` | Espejo horizontal / vertical |
| `F` | Pantalla completa (en el prompter) |
| `Esc` | Pausa |
