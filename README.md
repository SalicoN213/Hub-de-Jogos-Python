# 🎮 Hub de Jogos em Terminal (Python)

Um ecossistema de jogos clássicos executados via interface de linha de comando (CLI), desenvolvido em Python. O projeto conta com um menu interativo, formatação visual avançada, modularização rigorosa e um script de build automatizado para geração de executáveis (`.exe`).

---

## 🛠️ Jogos Disponíveis

1. **🎲 Adivinhação**: O computador escolhe um número entre 1 e 10 e você deve adivinhar em quantas tentativas conseguir.
2. **✂️ Jokenpô (Pedra, Papel e Tesoura)**: Jogue o clássico jogo contra a IA do computador.
3. **🔢 Par ou Ímpar**: Teste sua sorte escolhendo par ou ímpar contra o número sorteado.
4. **🎰 Caça-Níquel**: Gire os rolos animadamente e tente alinhar símbolos iguais para vencer.
5. **🃏 Blackjack (21)**: Suporte para até 4 jogadores simultâneos contra o Dealer, com gerenciamento de fichas, apostas, dobra (*Double Down*), estouro de pontos e verificação de Blackjack Natural.

---

## 📁 Estrutura do Projeto

```text
hub_de_jogos_1.0/
│
├── main.py              # Ponto de entrada e loop do menu principal
├── build.py             # Script de automação de compilação (.exe)
│
├── utilidades/          # Pacote de funções utilitárias e navegação
│   ├── __init__.py
│   ├── limpar.py        # Limpeza cross-platform do terminal
│   ├── mapas.py         # Mapeamentos do baralho e despacho de funções
│   ├── sair.py          # Gerenciamento do fluxo de reinício do jogo
│   └── titulo.py        # Renderização de artes ASCII via PyFiglet
│
└── jogos/               # Pacote contendo as lógicas dos jogos
    ├── __init__.py
    ├── advinhacao.py
    ├── blackjack.py
    ├── caca_niquel.py
    ├── jokenpo.py
    └── par_ou_impar.py
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- **Python 3.10+** instalado.
- Biblioteca **PyFiglet** para a renderização dos títulos em arte ASCII.

### Passos
1. Clone este repositório ou baixe os arquivos na sua máquina.
2. Instale as dependências necessárias executando no terminal:
   ```bash
   pip install pyfiglet pyinstaller
   ```
3. Execute o projeto diretamente:
   ```bash
   python main.py
   ```

---

## 📦 Como Compilar para Executável (.exe)

O projeto inclui um script automatizado (`build.py`) que:
- Remove compilações e executáveis antigos.
- Inclui automaticamente todas as fontes da biblioteca `pyfiglet`.
- Embute o ícone `.ico` personalizado (caso exista o arquivo `icone.ico` na raiz).
- Mapeia o ambiente Python ativo para evitar erros de dependência.

Para gerar um novo executável após fazer alterações no código, basta executar:

```bash
python build.py
```

O arquivo `HubDeJogos.exe` será gerado diretamente na pasta raiz do projeto.

---

## 💻 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Módulos Nativos:** `random`, `time`, `os`, `sys`, `subprocess`
- **Módulos Externos:** `pyfiglet`
- **Compilador:** `PyInstaller`

---

## 👤 Autor

Desenvolvido por **Nicolas Veloso Lacerda**.