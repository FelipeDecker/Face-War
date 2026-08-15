# Face War

Face War e um jogo 2D de acao no estilo arcade, desenvolvido em Python com Pygame. O jogador controla um rosto feliz em um cenario deserto, desvia dos inimigos que atravessam a tela e dispara projeteis para destrui-los.

## Sobre o projeto

O jogo apresenta uma janela de 840 x 480 pixels. O personagem permanece no lado esquerdo da tela e os inimigos surgem aleatoriamente fora do limite direito, avancando na direcao do jogador. A partida continua enquanto o personagem nao colidir com um inimigo.

Quando um tiro atinge um asteroide, os dois sprites sao removidos. Quando um asteroide atinge o jogador, o jogo entra no estado de game over, reproduz o som correspondente e registra `Game Over` no terminal.

## Como jogar

### Executando pelo codigo-fonte

1. Instale o Python 3.
2. Instale a dependencia do projeto:

   ```bash
   pip install pygame
   ```

3. Abra um terminal na pasta do projeto.
4. Execute:

   ```bash
   python app.py
   ```

Os arquivos da pasta `Resources/` precisam permanecer no mesmo local relativo ao projeto, pois o jogo carrega as imagens e os sons usando esses caminhos.

### Executando a versao compilada

O repositorio tambem inclui `app.exe`, que pode ser executado diretamente no Windows. Mesmo nessa versao, os recursos visuais e sonoros devem estar disponiveis conforme a estrutura distribuida com o projeto.

## Controles

| Tecla           | Acao                      |
| --------------- | ------------------------- |
| `W`             | Move o jogador para cima  |
| `S`             | Move o jogador para baixo |
| `Espaco`        | Dispara um projetil       |
| Fechar a janela | Encerra o jogo            |

O movimento usa aceleracao: ao pressionar `W` ou `S`, a velocidade aumenta gradualmente. Quando nenhuma dessas teclas e pressionada, a velocidade diminui progressivamente, produzindo um efeito de desaceleracao. O personagem fica limitado aos limites superior e inferior da janela.

## Mecanicas

- A janela e atualizada a 60 quadros por segundo.
- Asteroides aparecem periodicamente, com 80% de chance a cada ciclo de geracao.
- Cada asteroide recebe uma posicao vertical aleatoria e uma velocidade aleatoria entre 2 e 4 pixels por quadro, aproximadamente.
- Asteroides que saem pela esquerda sao removidos da memoria do jogo.
- Cada tiro viaja horizontalmente para a direita a 5 pixels por quadro.
- Tiros que ultrapassam o limite direito sao removidos.
- Colisoes entre jogador e asteroides e entre tiros e asteroides usam `pygame.sprite.collide_mask`, permitindo uma deteccao baseada na forma dos sprites.
- A musica de fundo fica em loop durante a execucao.
- Sons separados sao usados para disparos e game over.

## Estrutura do projeto

```text
Face-War/
|-- app.py                 # Inicializacao, loop principal e regras da partida
|-- player.py              # Sprite e movimento do jogador
|-- asteroid.py            # Criacao, movimento e remocao dos inimigos
|-- shot.py                # Criacao, movimento e remocao dos tiros
|-- README.md              # Documentacao do projeto
|-- TODO.md                # Tarefas pendentes e melhorias futuras
|-- Aluno.txt              # Identificacao do aluno
|-- app.exe                # Versao executavel para Windows
`-- Resources/             # Imagens e arquivos de audio
```

### Responsabilidade dos arquivos Python

#### `app.py`

Inicializa o Pygame, cria a janela, carrega o cenario e os sons, cria os grupos de sprites e controla o loop principal. Tambem processa os eventos do teclado, gera asteroides, atualiza os objetos, desenha a cena e trata as colisoes.

#### `player.py`

Define a classe `Player`, que herda de `pygame.sprite.Sprite`. O personagem usa `HappyFace.png`, tem tamanho de 100 x 100 pixels e controla sua posicao vertical com aceleracao e desaceleracao.

#### `asteroid.py`

Define a classe `Asteroid`. O inimigo usa `RedGuy.png`, tem tamanho de 50 x 50 pixels, aparece fora do lado direito da janela e se move para a esquerda. Ao sair da tela, e destruido.

#### `shot.py`

Define a classe `Shot`. O projetil usa `Shot.png`, tem tamanho de 20 x 20 pixels e se move para a direita. Ao sair da janela, e removido.

## Recursos

| Arquivo               | Uso                                              |
| --------------------- | ------------------------------------------------ |
| `Desert.png`          | Cenario principal, redimensionado para 840 x 480 |
| `HappyFace.png`       | Imagem do jogador                                |
| `RedGuy.png`          | Imagem dos asteroides/inimigos                   |
| `Shot.png`            | Imagem dos projeteis                             |
| `BackgroundSound.mp3` | Musica de fundo em loop                          |
| `swing.wav`           | Som de disparo                                   |
| `GameOver.wav`        | Som de colisao/game over                         |
| `Background.jpg`      | Recurso visual adicional presente na pasta       |
| `battleThemeA.mp3`    | Recurso sonoro adicional presente na pasta       |
| `Destroyed.wav`       | Recurso sonoro adicional presente na pasta       |

Os tres ultimos arquivos estao incluidos no repositorio, mas nao sao carregados atualmente por `app.py`.

## Tecnologias utilizadas

- **Python 3:** linguagem usada na implementacao.
- **Pygame:** biblioteca responsavel pela janela, loop de eventos, sprites, grupos, imagens, audio, teclado, colisoes e controle de tempo.
- **Random:** biblioteca padrao usada para sortear posicoes, velocidades e a chance de surgimento dos asteroides.
- **OS e Sys:** bibliotecas padrao usadas para resolver o diretorio de execucao e dar suporte a execucao empacotada, incluindo a versao executavel.
- **PyInstaller ou ferramenta equivalente:** a presenca de `app.exe` indica uma distribuicao compilada para Windows; o comando de empacotamento nao esta registrado no repositorio.
