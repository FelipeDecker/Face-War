# TODO - Face War

Este arquivo reune as tarefas necessarias para transformar o prototipo atual em uma versao completa, jogavel e pronta para distribuicao, alem de ideias para evolucoes futuras.

## TODO: concluir o projeto

### Jogabilidade e fluxo da partida

- [ ] Criar uma tela inicial com titulo, instrucoes resumidas e botao ou tecla para iniciar.
- [ ] Exibir uma tela visual de game over dentro da janela, em vez de mostrar apenas `Game Over` no terminal.
- [ ] Permitir reiniciar a partida sem fechar o programa.
- [ ] Definir uma condicao clara de encerramento e retorno ao menu inicial.
- [ ] Adicionar pontuacao por asteroide destruido e exibir o placar na tela.
- [ ] Definir uma regra de dificuldade e uma meta de partida, como sobreviver por tempo ou atingir determinada pontuacao.
- [ ] Ajustar a geracao de asteroides para que a dificuldade seja previsivel e equilibrada.
- [ ] Testar os limites de movimento, os disparos e as colisoes em diferentes situacoes.

### Interface e experiencia do jogador

- [ ] Exibir pontuacao, tempo de sobrevivencia e estado da partida na interface.
- [ ] Informar visualmente quando o jogador perde, vence ou pausa.
- [ ] Adicionar pausa e retomada da partida.
- [ ] Garantir que textos, imagens e controles tenham boa leitura na resolucao configurada.
- [ ] Definir uma identidade visual consistente para menus, fontes, cores e efeitos.
- [ ] Adicionar controle de volume e opcao para silenciar musica e efeitos.

### Audio, imagens e recursos

- [ ] Decidir o uso de `Background.jpg`, `battleThemeA.mp3` e `Destroyed.wav`, que atualmente nao sao carregados pelo jogo.
- [ ] Adicionar um efeito sonoro para a destruicao de asteroides.
- [ ] Revisar volume, formato, duracao e direitos de uso de todos os recursos.
- [ ] Verificar se todos os recursos sao carregados corretamente quando o jogo e executado pelo codigo-fonte e pelo `app.exe`.
- [ ] Tratar erros de recurso ausente com uma mensagem clara para o usuario.

### Qualidade tecnica

- [ ] Criar um `requirements.txt` com a dependencia e, se necessario, sua versao testada do Pygame.
- [ ] Separar configuracoes como largura, altura, velocidade, taxa de surgimento e caminhos de recursos em um unico local.
- [ ] Corrigir imports que nao sao usados e padronizar nomes de variaveis e classes.
- [ ] Organizar o carregamento de imagens e sons para evitar repeticao e facilitar manutencao.
- [ ] Adicionar testes para limites do jogador, movimento dos inimigos, descarte de sprites e regras de colisao.
- [ ] Verificar o comportamento em diferentes versoes do Python e do Pygame.
- [ ] Registrar os passos oficiais de empacotamento do executavel para que a distribuicao possa ser reproduzida.
- [ ] Testar a execucao em uma maquina Windows sem o ambiente de desenvolvimento instalado.
- [ ] Atualizar esta documentacao sempre que controles, regras ou dependencias mudarem.

## Melhorias futuras

Depois que o TODO principal estiver concluido, o projeto pode evoluir com as seguintes funcionalidades:

### Novas mecanicas

- Sistema de vidas, escudo ou energia para o jogador.
- Diferentes tipos de inimigos, com tamanhos, velocidades e comportamentos distintos.
- Inimigos que atiram ou perseguem o jogador.
- Chefes de fase com padroes de ataque proprios.
- Power-ups para tiro mais rapido, tiro triplo, escudo e recuperacao de vida.
- Municao, recarga e diferentes tipos de projetil.
- Fases com objetivos, cenarios e regras proprias.
- Sistema de ondas, combinacoes de acertos e bonus por precisao.
- Itens colecionaveis e desafios durante a partida.
- Modo cooperativo local ou partidas competitivas.

### Conteudo e apresentacao

- Menu de selecao de fases, dificuldade e personagem.
- Mais personagens jogaveis com atributos diferentes.
- Animacoes para movimento, dano, destruicao e explosoes.
- Particulas, tremor de tela e efeitos visuais para impactos.
- Mais cenarios e temas musicais.
- Creditos, informacoes do projeto e tela de configuracoes.
- Ranking local com melhores pontuacoes.
- Conquistas e estatisticas, como maior pontuacao e maior tempo sobrevivido.

### Acessibilidade e distribuicao

- Configuracao das teclas e suporte a controle ou joystick.
- Modo para daltonismo e alternativas visuais aos sinais sonoros.
- Controle separado de musica e efeitos, incluindo silenciamento rapido.
- Escala de janela, tela cheia e suporte a diferentes resolucoes.
- Empacotamento automatizado para Windows e futuramente Linux ou macOS.
- Versionamento, changelog e releases do jogo.
- Documentacao de contribuicao para novos desenvolvedores.
