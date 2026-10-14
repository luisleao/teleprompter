# Teleprompter in the browser

🇧🇷 [Português](README.md) · 🇪🇸 [Español](README.es.md)

A single file (`index.html`) with two screens:

- **Control panel** (`index.html` or `index.html#control`), with two screens: **Control** (a monitor mirroring the prompter, play/pause, scroll mode, speed or voice, progress) and **Script** (a Markdown editor with a preview of how the text will look). The **⚙** gear opens the text, camera, voice, pedal and key settings next to the monitor, which updates live.
- **Prompter** (`index.html#prompter`): the screen that goes to the Elgato Prompter, text only.

The two screens talk through the browser itself (BroadcastChannel, with localStorage as a fallback), so the basics need no server and no internet. Everything you adjust is saved in the browser.

## Languages

The interface works in Portuguese, English and Spanish. The language comes from the browser: `pt` opens in Portuguese, `es` in Spanish and anything else in English. To force a language, use **⚙ → Text → Interface language** (both windows reload). The speech-recognition language starts in the same language and can be changed in **⚙ → Voice**.

The sample scripts live in separate files, one per language: `scripts/roteiro.pt.md`, `scripts/roteiro.en.md` and `scripts/roteiro.es.md`. When the page is served over HTTP (GitHub Pages, `python3 -m http.server`), the **Sample** button and the first launch read those files, so you can edit them without touching the HTML. Opened via `file://`, the page uses a copy embedded in `index.html`; to refresh that copy after changing an `.md`, run `python3 parts/build.py` (or edit the `SAMPLES` constant in the HTML).

## Getting started

You can open `index.html` straight in Chrome (double-click the file). If you prefer serving it over HTTP, go into the folder and run `python3 -m http.server 8000`; then open `http://localhost:8000/index.html`.

1. Open the control panel.
2. Click **Open prompter ↗**. It opens a new window with the text. Drag that window to the Elgato Prompter's display and press **F** (or double-click) for full screen.
3. If the text shows up reversed on the Prompter, open **⚙** and tick **Mirror horizontally** (or vertically).
4. On the **Script** screen, paste or drop your `.md`. Go back to **Control** and press play.

The control screen only shows what the current mode uses: the speed in auto scroll; the status and transcript in voice mode (the speed shows up there again as "fallback scroll" if you turn on the option to keep scrolling without voice). Reached the end? Play again starts over from the top.

The **View here** button shows the prompter in the same window; on the prompter, move the mouse and click **← panel** to come back.

## Script in Markdown

The **Sample** button loads, in the interface language, a chaptered script that explains the teleprompter itself (windows, modes, voice, pedal, settings, camera and Markdown), with camera, screen and cut notes in square brackets. Use it as a test: read it out loud and watch the text follow you.

- `# Title` becomes a section title. Titles are not speech: they stay out of the word count and of voice recognition, and you can hide them on the prompter (⚙ → Text → Show section titles). The ◀ ▶ buttons and the ← → arrows jump from block to block; `Shift + ←/→` jumps from section to section, straight to the first spoken word of each.
- `[text in square brackets]` is a cue: it stands out, can be hidden and **does not take part** in voice recognition.
- `---` marks a pause (three dots in the text).
- `**bold**`, `*italic*`, lists and quotes (`>`) work. Single line breaks are kept.
- `<!-- comment -->` does not show on the prompter.

## Camera marker

In **⚙ → Camera**, turn on the marker to show where the lens sits behind the glass. You can pick the style (reticle, ring or dot), size and color, and position it by dragging the reticle on the panel's preview or on the prompter itself. The **Reading line at camera height** button puts the reading line at the same height, so your eyes stay on the lens while you read. Turn the marker off when you don't need it.

## Follow my voice

Choose **Follow my voice** and press play. The browser asks for microphone access the first time. Pause to stop listening. The ⏮ ◀ ▶ ⏭ buttons and the progress bar keep working: when you jump manually, recognition restarts from that point. How it works:

- The last recognized words are aligned with the script in a tolerant way (it accepts recognition errors, swapped words and fillers like "um", "so", "well").
- If you skip a passage, the text looks for the new position and goes there. If you go back, it goes back.
- If you improvise, the text waits. When you return to the script, it finds the spot again on its own (first near where it was; then across the whole script, if a sentence is recognized well).
- The recognized word is highlighted on the prompter and on the preview; pick the style in ⚙ → Text → Highlight style (background, underline or text color), or turn the highlight off.
- **Look-ahead** (⚙ → *Voice*) is how many words past the speech the reading line sits.
- **Confidence for far jumps** makes big jumps stricter or looser.
- **Keep scrolling slowly if the voice is lost** uses the auto-scroll speed while nothing is recognized.

Recognition uses the Web Speech API, which works well in Chrome and Edge (Chrome usually needs internet to recognize). Firefox and Safari have limited support. With both windows open, "Microphone in window" (⚙ → *Voice*) picks who listens: the control window (default) or the prompter. If the chosen window is not open (single screen, for example), the open one takes the microphone on its own.

## Stream Deck Pedal

Two ways:

**1. By keys (recommended).** In the Stream Deck app, give each pedal a Hotkey action with the keys shown in ⚙ → *Pedal*. Default: left `←` (previous block), center `Space` (play/pause), right `→` (next block). You can change what each pedal does and record other keys; `F13`, `F14` and `F15` are good choices because they don't get in the way of typing. The key goes to the focused window (panel or prompter), so keep one of them in front and the cursor out of the editor (`Esc` leaves the editor).

**2. Over USB (WebHID, experimental).** In ⚙ → *Pedal*, click **Connect pedal over USB** and pick the Stream Deck Pedal. The pedal then talks straight to the page, regardless of focus, and holding the pedal repeats the action (previous or next block, speed, font), like holding a key: you can go all the way to the start or the end without letting go. Play/pause and the other on/off commands don't repeat. The control panel is the one that answers the pedal; with the prompter alone in the window ("View here"), it takes the pedal over and hands it back when the panel opens again. If nothing arrives, close the Stream Deck app and try again. Use **Calibrate pedals** to teach which pedal is which (the page shows the HID report bytes so you can check).

## Shortcuts

| Key | Action |
|---|---|
| `Space` | Play / Pause |
| `↑` `↓` | Speed +5 / −5 |
| `←` `→` | Previous / next block |
| `Shift + ←` `Shift + →` | Previous / next section (titles) |
| `PageUp` `PageDown` | Half a screen back / forward |
| `Home` `End` | Start / end |
| `R` | Restart (start + pause) |
| `V` | Voice mode on / off |
| `B` | Hide / show the text |
| `+` `−` | Bigger / smaller font |
| `M` `Shift + M` | Mirror horizontally / vertically |
| `F` | Full screen (on the prompter) |
| `Esc` | Pause |
