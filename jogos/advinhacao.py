"""
Módulo do Jogo de Adivinhação (advinhacao.py)
Implementa o jogo onde o usuário tenta adivinhar um número gerado aleatoriamente entre 1 e 10.
"""

from random import randint
from utilidades import limpar_terminal, sair
from time import sleep


def adivinhacao():
    """Função principal que controla as tentativas e dicas do jogo de adivinhação."""
    while True:
        limpar_terminal()

        tentativas = 0
        jogador = None
        computador = randint(1, 10)

        # Loop até que o jogador acerte o número secreto
        while computador != jogador:
            while True:
                limpar_terminal()

                print('\033[35m=-=' * 20)
                print(f'{'Vou Pensar em um número de 1 a 10':^60}')
                print('\033[35m=-=\033[m' * 20)
                try:
                    jogador = int(input('Digite seu chute: '))
                    break
                except ValueError:
                    print('\033[1;31mDigite um número inteiro!\033[m')
                    sleep(1)

            # Fornece dicas se o número secreto é maior ou menor
            if computador > jogador:
                tentativas +=1
                limpar_terminal()
                print('Mais... Tente Novamente!')
                sleep(1.5)
            if jogador > computador:
                tentativas += 1
                limpar_terminal()
                print('Menos... Tente novamente!')
                sleep(1.5)

        limpar_terminal()

        # Exibe mensagem de vitória baseada no número de tentativas.
        if tentativas == 0:
            print('~' * 60)
            print(f'{'\033[1;032mParabêns você acertou de primeira!!!\033[m':^60}')
            print('~' * 60)
        else:
            print('~' * 60)
            print(f'{f'\033[1;32mParabêns você acerteou em {tentativas} tentativas.\033[m':^60}')
            print('~' * 60)

        if sair() == 'N':
            limpar_terminal()
            print('Obrigado por jogar, volte sempre.')
            sleep(1)
            break