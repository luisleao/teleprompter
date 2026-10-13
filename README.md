# Teleprompter no navegador

Um único arquivo (`index.html`) com duas telas:

- **Painel de controle** (`index.html` ou `index.html#control`), com duas telas: **Controle** (monitor com o espelho do prompter, play/pause, modo de rolagem, velocidade ou voz, progresso) e **Roteiro** (editor Markdown com prévia de como o texto aparece). A engrenagem **⚙** abre os ajustes de texto, câmera, voz, pedal e teclas ao lado do monitor, que muda na hora.
- **Prompter** (`index.html#prompter`): a tela que vai para o Elgato Prompter, só com o texto.

As duas telas conversam pelo próprio navegador (BroadcastChannel, com localStorage de reserva), então não precisa de servidor nem de internet para o básico. Tudo que você ajusta fica salvo no navegador.

## Como abrir

Dá para abrir o `index.html` direto no Chrome (clique duplo no arquivo). Se preferir servir por HTTP, para começar entre na pasta e rode o comando `python3 -m http.server 8000`; depois abra `http://localhost:8000/index.html`.

1. Abra o painel de controle.
2. Clique em **Abrir prompter ↗**. Ele abre uma nova janela com o texto. Arraste essa janela para a tela do Elgato Prompter e pressione **F** (ou dê clique duplo) para tela cheia.
3. Se o texto aparecer invertido no Prompter, abra **⚙** e marque **Espelhar na horizontal** (ou vertical).
4. Na tela **Roteiro**, cole ou arraste seu `.md`. Volte para **Controle** e dê play.

Na tela de controle só aparece o que o modo usa: a velocidade na rolagem automática; o status e a transcrição no modo de voz (a velocidade volta a aparecer ali como “rolagem de reserva” se você ligar a opção de continuar rolando sem voz). Chegou ao fim? Play de novo recomeça do início.

O botão **Ver aqui** mostra o prompter na mesma janela; no prompter, passe o mouse e clique em **← painel** para voltar.

## Roteiro em Markdown

O botão **Exemplo** carrega um roteiro em capítulos que explica o próprio teleprompter (janelas, modos, voz, pedal, ajustes, câmera e Markdown), com marcações de câmera, tela e corte entre colchetes. Serve de teste: leia em voz alta e veja o texto acompanhar.

- `# Título` vira um título de seção. Títulos não são fala: ficam fora da contagem de palavras e do reconhecimento de voz, e dá para escondê-los no prompter (⚙ → Texto → Mostrar títulos de seção). Os botões ◀ ▶ e as setas ← → pulam de bloco em bloco; `Shift + ←/→` pula de seção em seção, direto para a primeira palavra falada de cada uma.
- `[texto entre colchetes]` é uma deixa: aparece em destaque, pode ser escondida e **não entra** no reconhecimento de voz.
- `---` marca uma pausa (três pontos no texto).
- `**negrito**`, `*itálico*`, listas e citações (`>`) funcionam. Quebras de linha simples são mantidas.
- `<!-- comentário -->` não aparece no prompter.

## Marcador da câmera

Em **⚙ → Câmera**, ligue o marcador para mostrar onde está a lente atrás do vidro. Dá para escolher o estilo (mira, anel ou ponto), tamanho e cor, e posicionar arrastando a mira na prévia do painel ou no próprio prompter. O botão **Linha de leitura na altura da câmera** coloca a linha de leitura na mesma altura, para os olhos ficarem na lente enquanto você lê. Desligue o marcador quando não precisar dele.

## Seguir a voz

Escolha **Seguir minha voz** e dê play. O navegador pede acesso ao microfone na primeira vez. Pause para parar de ouvir. Os botões ⏮ ◀ ▶ ⏭ e a barra de progresso continuam valendo: ao pular manualmente, o reconhecimento recomeça daquele ponto. Como funciona:

- As últimas palavras reconhecidas são alinhadas com o roteiro de forma tolerante (aceita erros de reconhecimento, palavras trocadas e "é", "né", "então").
- Se você pular um trecho, o texto procura a nova posição e vai até lá. Se você voltar, ele volta.
- Se você improvisar, o texto espera. Quando voltar ao roteiro, ele reencontra o ponto sozinho (primeiro perto de onde estava; depois no roteiro inteiro, se tiver uma frase bem reconhecida).
- **Antecipação** (⚙ → *Voz*) é quantas palavras à frente da fala a linha de leitura fica.
- **Confiança para pular longe** deixa os pulos grandes mais exigentes ou mais soltos.
- **Continuar rolando devagar se perder a voz** usa a velocidade da rolagem automática enquanto não reconhece nada.

O reconhecimento usa a Web Speech API, que funciona bem no Chrome e no Edge (o Chrome normalmente precisa de internet para reconhecer). Firefox e Safari têm suporte limitado. Com as duas janelas abertas, “Microfone na janela” (⚙ → *Voz*) escolhe quem escuta: a do controle (padrão) ou a do prompter. Se a janela escolhida não estiver aberta (tela única, por exemplo), a que estiver aberta assume o microfone sozinha.

## Stream Deck Pedal

Dois jeitos:

**1. Por teclas (recomendado).** No app Stream Deck, coloque em cada pedal uma ação de tecla de atalho (Hotkey) com as teclas que aparecem em ⚙ → *Pedal*. Padrão: esquerdo `←` (bloco anterior), central `Espaço` (play/pause), direito `→` (próximo bloco). Você pode trocar a ação de cada pedal e gravar outras teclas; `F13`, `F14` e `F15` são boas opções porque não atrapalham a digitação. A tecla vai para a janela que estiver em foco (painel ou prompter), então deixe uma delas em primeiro plano e o cursor fora do editor (`Esc` tira o foco do editor).

**2. Por USB (WebHID, experimental).** Em ⚙ → *Pedal*, clique em **Conectar pedal por USB** e escolha o Stream Deck Pedal. Assim o pedal fala direto com a página, sem depender de foco, e segurar o pedal repete a ação (bloco anterior ou próximo, velocidade, fonte), como uma tecla segurada: dá para ir até o início ou o fim sem soltar. Play/pause e os outros comandos de liga/desliga não repetem. Quem responde ao pedal é o painel de controle; com o prompter sozinho na janela (“Ver aqui”), ele assume o pedal, e devolve quando o painel abre de novo. Se não chegar nada, feche o app Stream Deck e tente de novo. Use **Calibrar pedais** para ensinar qual pedal é qual (o sistema mostra os bytes do relatório HID para você conferir).

## Atalhos

| Tecla | Ação |
|---|---|
| `Espaço` | Play / Pause |
| `↑` `↓` | Velocidade +5 / −5 |
| `←` `→` | Bloco anterior / próximo |
| `Shift + ←` `Shift + →` | Seção anterior / próxima (títulos) |
| `PageUp` `PageDown` | Meia tela para trás / para a frente |
| `Home` `End` | Início / fim |
| `R` | Reiniciar (início + pause) |
| `V` | Liga / desliga o modo de voz |
| `B` | Esconde / mostra o texto |
| `+` `−` | Fonte maior / menor |
| `M` `Shift + M` | Espelhar horizontal / vertical |
| `F` | Tela cheia (no prompter) |
| `Esc` | Pause |
