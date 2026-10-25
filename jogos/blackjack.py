"""
Módulo do Jogo Blackjack (blackjack.py)
Implementa toda a lógica do jogo de cartas 21, incluindo classes para Jogador e Dealer,
gerenciamento de apostas, baralho, regras de ases, blackjack natural e apuração final.
"""

def blackjack():
    from utilidades import limpar_terminal, sair, baralho_map
    from random import choice
    from time import sleep

    class Jogador:
        """
        Representa um participante humano na mesa de Blackjack.
        Controla saldo, apostas, mão de cartas, pontuação e status no jogo.
        """
        def __init__(self, nome):
            self.nome = nome
            self.mao = {}          # Dicionário contendo as cartas na mão e seus valores.
            self.pontos = 0        # Pontuação total atual do jogador.
            self.fichas = 100      # Saldo inicial de fichas.
            self.aposta = 0        # Quantidade de fichas apostadas na rodada atual.
            self.estourou = False  # Status indicando se ultrapassou 21 pontos.
            self.ingame = True     # Status indicando se o jogador ainda possui fichas (não faliu).
            self.nblackjack = False# Status indicando se obteve um Blackjack natural (Ás + 10/Figura).

        def __str__(self):
            """Retorna uma representação em string formatada com o estado atual do jogador."""
            mao_str = ', '.join(self.mao.keys()) if self.mao else 'Vazia'
            estorou_str = 'Sim' if self.estourou else 'Não'
            ingame_str = 'Sim' if self.ingame == True else 'Não'
            blackjack_str = 'Sim' if self.nblackjack else 'Não'

            return (f"Nome: {self.nome} | Mão: {mao_str} | Pontos: {self.pontos} | Fichas: {self.fichas}| "
                    f"Apôsta: {self.aposta} | Estourou: {estorou_str} | No Jogo: {ingame_str} | Blackjack Natural: {blackjack_str}")

        def calculo_ases(self):
            """
            Gerencia a regra especial do Ás no Blackjack:
            Se a pontuação passar de 21 e o jogador possuir um Ás valendo 11,
            o seu valor é automaticamente convertido para 1, reduzindo a pontuação em 10.
            """
            if self.pontos > 21:
                for carta, valor in self.mao.items():
                    if carta.startswith('A') and valor == 11:
                        self.mao[carta] = 1
                        self.pontos -= 10
                        break
                # Se mesmo após converter o Ás a pontuação continuar acima de 21, o jogador estourou.
                if self.pontos > 21:
                    self.estourou = True
                    self.aposta = 0

        def sorteio_carta(self):
            """
            Sorteia aleatoriamente uma carta do baralho em uso,
            remove-a do baralho, adiciona à mão do jogador e recalcula os pontos.
            """
            carta = choice(list(baralho_uso.keys()))
            valor = baralho_uso.pop(carta)

            self.mao[carta] = valor
            self.pontos += valor
            self.calculo_ases()

        def realizar_aposta(self):
            """
            Interface de interação para o jogador inserir sua aposta na rodada.
            Valiza se a entrada é numérica, se está nos limites (10 a 100),
            se é múltipla de 10 e se o jogador possui saldo suficiente.
            """
            while True:
                limpar_terminal()
                valor = input(f"{self.nome} (Saldo: {self.fichas}) - Digite a quantidade de fichas apostadas (Min: 10 / Max: 100 / De 10 em 10): ").strip()

                if valor.isnumeric():
                    valor = int(valor)

                    if 10 <= valor <= 100 and valor <= self.fichas and valor % 10 == 0:
                        self.fichas -= valor
                        self.aposta += valor
                        break
                    else:
                        limpar_terminal()
                        print("\033[31mQuantidade apôstada de forma incorreta!!!\033[m")
                        sleep(1)

                else:
                    limpar_terminal()
                    print("\033[31mDigite um número inteiro valido!!!\033[m")
                    sleep(1)

        def verificar_fichas(self):
            """Verifica se o saldo de fichas chegou a zero; se sim, o jogador é eliminado (ingame = False)."""
            if self.fichas == 0:
                self.ingame = False

        def reset(self):
            """Limpa a mão, pontos e apostas ao término de cada rodada, preparando para a seguinte."""
            if not self.ingame:
                return
            self.mao = {}
            self.pontos = 0
            self.aposta = 0
            if self.estourou:
                self.estourou = False
            if self.nblackjack:
                self.nblackjack = False

    class Dealer(Jogador):
        """
        Representa a banca (Dealer) no jogo de Blackjack.
        Herda de Jogador, mas possui atributos e comportamentos específicos,
        como gerenciar uma carta oculta e regras rígidas de compra.
        """
        def __init__ (self):
            self.nome = 'Dealer'
            self.mao = {}
            self.oculta = {}       # Armazena temporariamente a carta oculta na distribuição inicial.
            self.pontos = 0
            self.estourou = False
            self.nblackjack = False

        def __str__ (self):
            """Representação em string do dealer (oculta cartas escondidas do total público)."""
            mao_str = ', '.join(self.mao.keys()) if self.mao else 'Vazia'
            estorou_str = 'Sim' if self.estourou else 'Não'
            return f"Nome: {self.nome} | Mão: {mao_str} | Pontos: {self.pontos} | Estorou: {estorou_str}"

        def jogar_dealer(self):
            """Regra oficial da banca: o dealer é obrigado a comprar cartas continuamente até somar no mínimo 17 pontos."""
            while self.pontos < 17 and not self.estourou:
                self.sorteio_carta()

        def inicio_dealer(self):
            """Distribui uma carta aberta para si e guarda a segunda carta como 'oculta'."""
            self.sorteio_carta()
            carta = choice(list(baralho_uso.keys()))
            valor = baralho_uso.pop(carta)

            self.oculta[carta] = valor

        def revelar_oculta(self):
            """Move a carta oculta para a mão visível do dealer e atualiza seus pontos."""
            if self.oculta:
                carta = list(self.oculta.keys())[0]
                valor = self.oculta.pop(carta)

                self.mao[carta] = valor
                self.pontos += valor
                self.calculo_ases()

        def reset(self):
            """Reseta o estado do dealer para uma nova rodada."""
            self.mao = {}
            self.pontos = 0
            if self.estourou:
                self.estourou = False
            if self.nblackjack:
                self.nblackjack = False

    def embaralhar(baralho_original):
        """Retorna uma cópia nova e íntegra do baralho original para iniciar o jogo/rodada."""
        return baralho_original.copy()

    def adicionar_jogadores():
        """Gerencia o cadastro inicial de 1 a 4 jogadores humanos para a mesa."""
        jogadores_temp = []

        while True:
            limpar_terminal()
            entrada = input("Digite a quantidade de jogadores (1 a 4): ").strip()

            if entrada.isnumeric():
                quantidade = int(entrada)
                if 1 <= quantidade <= 4:
                    for j in range(1, quantidade + 1):
                        limpar_terminal()
                        nome = input(f"Digite o nome do {j}º jogador: ").strip().title()
                        novo_jogador = Jogador(nome)
                        jogadores_temp.append(novo_jogador)
                    break

            limpar_terminal()
            print("\033[31mDigite um número válido entre 1 e 4!!!\033[m")
            sleep(1)

        return jogadores_temp

    def hit(jogador_temp):
        """Ação de pedir carta (Hit): compra mais uma carta do baralho."""
        jogador_temp.sorteio_carta()

    def double(jogador_temp):
        """
        Ação de dobrar a aposta (Double Down):
        Dobra o valor apostado, desconta as fichas correspondentes do saldo
        e puxa obrigatoriamente apenas uma última carta adicional.
        """
        valor = jogador_temp.aposta
        jogador_temp.fichas -= valor
        jogador_temp.aposta += valor
        jogador_temp.sorteio_carta()

    def blackjack_natural(temp):
        """
        Verifica se a mão inicial de exatamente 2 cartas contém um Ás (11)
        junto com uma carta de valor 10 (10, J, Q ou K), caracterizando Blackjack natural.
        """
        if len(temp.mao) == 2:
            tem_as = False
            tem_dez = False

            for carta in temp.mao.keys():
                if carta.startswith('A'):
                    tem_as = True
                elif carta.startswith(('10', 'K', 'Q', 'J')):
                    tem_dez = True

            if tem_as and tem_dez:
                return True

        return False

    def mostrar_mesa(jogadores_temp, dealer_temp):
        """Exibe na tela o status atual da mesa. (Dealer - Jogadores)"""
        print("Mesa:")
        print(f" - {dealer_temp}")
        for jogador_temp in jogadores_temp:
            print(f" - {jogador_temp}")

    def nova_rodada(jogadores_t, dealer_temp):
        """Cria uma lista apenas com os jogadores ativos (ingame == True), limpa o estado de todos os jogadores ativos e retorna a lista e um novo baralho embaralhado."""
        jogadores_temp = [jogador_t for jogador_t in jogadores_t if jogador_t.ingame]

        for j in jogadores_temp:
            j.reset()

        dealer_temp.reset()

        return jogadores_temp, embaralhar(baralho)

    def verificacao_final(jogador_temp, dealer_temp):
        """
        Compara o resultado final entre o jogador e o dealer:
         — Verifica se o dealer teve um blackjack natural
         — Blackjack natural apenas do jogador paga 2.5x a aposta.
         — Vitória por pontos maiores ou se o dealer estourou paga 2x a aposta.
         — Empate devolve a aposta original.
         — Derrota resulta na perda da aposta.
        """

        dealer_temp.nblackjack = blackjack_natural(dealer_temp)

        if jogador_temp.nblackjack and not dealer_temp.nblackjack:
            pagamento = int(jogador_temp.aposta * 3)
            jogador_temp.fichas += pagamento
            jogador_temp.aposta = 0
            print(f"O(A) jogador(a) {jogador_temp.nome} teve um Blackjack natural e recebe {pagamento}")

        elif dealer_temp.estourou or jogador_temp.pontos > dealer_temp.pontos:
            pagamento = jogador_temp.aposta * 2
            jogador_temp.fichas += pagamento
            jogador_temp.aposta = 0
            print(f"O dealer estorou ou o(a) jogador(a) {jogador_temp.nome} teve mais pontos que o dealer, recebendo {pagamento}")

        elif jogador_temp.pontos == dealer_temp.pontos:
            jogador_temp.fichas += jogador_temp.aposta
            jogador_temp.aposta = 0
            print(f"O(A) jogador(a) {jogador_temp.nome} empatou com o dealer recebendo de volta o que apôstou")

        else:
            jogador_temp.aposta = 0
            print(f"O(A) jogador(a) {jogador_temp.nome} perdeu para o dealer, perdendo sua apôsta")

    # Inicialização básica do baralho padrão e do dealer da mesa
    baralho = baralho_map()
    baralho_uso = embaralhar(baralho)
    dealer = Dealer()

    while True:

        # Configura os jogadores da sessão.
        jogadores = adicionar_jogadores()

        while True:
            # Etapa 1: Realização das apostas por cada jogador ativo
            for jogador in jogadores:
                if not jogador.ingame:
                    continue
                jogador.realizar_aposta()

            # Etapa 2: Distribuição inicial de 2 cartas para cada jogador
            for _ in range(2):
                for jogador in jogadores:
                    if not jogador.ingame:
                        continue
                    jogador.sorteio_carta()

            # Distribuição inicial das cartas do dealer
            dealer.inicio_dealer()

            # Verifica quais jogadores conseguiram Blackjack natural logo de início.
            for jogador in jogadores:
                jogador.nblackjack = blackjack_natural(jogador)

            limpar_terminal()

            mostrar_mesa(jogadores, dealer)
            input('\nPressione ENTER para continuar...')

            # Alerta visual para quem obteve Blackjack natural
            for jogador in jogadores:
                if jogador.nblackjack:
                    limpar_terminal()
                    print(f"\033[32mParabens ao jogador(a): {jogador.nome} por conseguir um blackjack natural!!\033[m")
                    print("\033[33mVocê não irá jogar essa rodada, porem só prederá se o Dealer tambem conseguir um blackjack natural\033[m")
                    input("Pressione ENTER para continuar...")

            # Etapa 3: Turno de escolhas e ações de cada jogador
            for jogador in jogadores:
                if jogador.estourou:
                    continue

                if jogador.nblackjack:
                    continue

                while True:

                    # Menu de ações da jogada (Pedir, Dobrar, Parar, Ver Mesa)
                    while True:
                        limpar_terminal()

                        print(jogador)
                        print("""
                            [ 1 ] Pedir carta (Hit)     [ 2 ] Dobrar (Double Down)
                            [ 3 ] Parar (Stand)         [ 4 ] Mostrar Mesa    
                        """)
                        acao = input("Digite sua ação: ").strip()
                        if acao.isnumeric():
                            acao = int(acao)

                            if 1 <= acao <= 4:
                                break

                            else:
                                limpar_terminal()
                                print("\033[31mDigite um número de 1 a 4!!!\033[m")
                                sleep(1)
                        else:
                            limpar_terminal()
                            print("\033[31mDigite um número inteiro!!!\033[m")
                            sleep(1)

                    # Execução da ação escolhida via estrutura match-case
                    match acao:
                        case 1:  # Pedir carta (Hit)
                            hit(jogador)
                            if jogador.estourou:
                                limpar_terminal()
                                print(f"Jogador: {jogador.nome} estourou. \nMão: {', '.join(jogador.mao.keys())}. Valendo: {jogador.pontos}.")
                                print("Ele está fora da rodada, perdendo sua aposta")
                                input("Pressione ENTER para continuar...")
                                break
                        case 2:  # Dobrar aposta (Double Down)
                            if len(jogador.mao) > 2:
                                limpar_terminal()
                                print("\033[31mSó se pode dobrar na primeira jogada\033[m")
                                sleep(1)
                            else:
                                if jogador.fichas >= jogador.aposta:
                                    double(jogador)
                                    if jogador.estourou:
                                        limpar_terminal()
                                        print(f"Jogador: {jogador.nome} estourou. \nMão: {', '.join(jogador.mao.keys())}. Valendo: {jogador.pontos}.")
                                        print("Ele está fora da rodada, perdendo sua aposta")
                                        input("Pressione ENTER para continuar...")
                                        break
                                    else:
                                        limpar_terminal()
                                        print("Saldo da rodada:")
                                        print(f" - {jogador}")
                                        input("Pressione ENTER para continuar...")
                                        break
                                else:
                                    limpar_terminal()
                                    print("\n\033[31mVocê não tem fichas suficientes para dobrar!\033[m")
                                    sleep(1)
                        case 3:  # Parar (Stand)
                            limpar_terminal()
                            print("Passando para o proximo jogador")
                            sleep(1.5)
                            break
                        case 4:  # Mostrar Mesa
                            limpar_terminal()
                            mostrar_mesa(jogadores, dealer)
                            input('\nPressione ENTER para continuar...')

            limpar_terminal()

            # Etapa 4: Vez da banca (Dealer) jogar
            print("Vez do dealer")
            sleep(1.5)
            dealer.revelar_oculta()

            limpar_terminal()

            print("O dealer revela sua carta oculta:")
            print(f" - {dealer}")
            input("Pressione ENTER para continuar...")

            limpar_terminal()

            # Dealer compra cartas se estiver abaixo de 17 pontos.
            if dealer.pontos < 17:
                print("O dealer compra até ficar com um mínimo de 17 pontos")
                dealer.jogar_dealer()
                print(f" - {dealer}")
                input("Pressione ENTER para continuar para a verificação final...")

                limpar_terminal()

            # Etapa 5: Verificação final de resultados para cada jogador
            for jogador in jogadores:
                if jogador.estourou and jogador.ingame:
                    print(f"O(A) jogador(a) {jogador.nome} estorou, perdendo sua apôsta")
                    continue
                verificacao_final(jogador, dealer)

            input("\nPressione ENTER para ver o saldo final da mesa...")

            limpar_terminal()

            # Atualiza o status de sobrevivência (fichas > 0) dos jogadores.
            for jogador in jogadores:
                if jogador.ingame:
                    jogador.verificar_fichas()

            jogadores_ativos = [j for j in jogadores if j.ingame]

            # Condições de encerramento da partida inteira.
            if len(jogadores_ativos) == 0:
                mostrar_mesa(jogadores, dealer)
                print("\n" + "=" * 60)
                print("\033[31m FIM DE JOGO! Suas fichas acabaram e a banca levou tudo!\033[m".center(60))
                print("=" * 60)
                input("\nPressione ENTER para continuar...")
                break

            elif len(jogadores_ativos) == 1 and len(jogadores) > 1:
                campeao = jogadores_ativos[0]
                mostrar_mesa(jogadores, dealer)
                print("\n" + "=" * 110)
                print(f"\033[32m FIM DE JOGO! O(a) jogador(a) {campeao.nome} resistiu até o fim e é o(a) GRANDE VENCEDOR(A) da mesa com {campeao.fichas} fichas!\033[m".center(110))
                print("=" * 110)
                input("Pressione ENTER para continuar...")
                break

            mostrar_mesa(jogadores, dealer)

            input("\nPressione ENTER para ir para a proxima rodada...")

            # Prepara um novo baralho e uma nova lista apenas com os jogadores no jogo (ingame == True) para a próxima rodada.
            jogadores, baralho_uso = nova_rodada(jogadores, dealer)

        limpar_terminal()

        # Pergunta se deseja reiniciar o jogo por completo.
        if sair() == "N":
            break

        # Prepara um novo baralho e uma nova lista apenas com os jogadores no jogo (ingame == True) para a próxima rodada.
        jogadores, baralho_uso = nova_rodada(jogadores, dealer)

if __name__ == "__main__":
    blackjack()