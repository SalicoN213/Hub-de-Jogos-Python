"""
Módulo do Jogo Par ou Ímpar (par_ou_impar.py)
Permite ao usuário jogar par ou ímpar contra o computador.
"""

from utilidades import limpar_terminal, sair
from random import randint
from time import sleep


def par_ou_impar():
    """Função principal que gerencia o fluxo do jogo Par ou Ímpar."""
    while True:
        limpar_terminal()

        escolha = None
        computador = randint(1, 10)

        # Validação do número inserido pelo jogador.
        while True:
            try:
                limpar_terminal()
                jogador = int(input('Digite um número: '))
                break
            except ValueError:
                print('\033[1;31mDigite um número inteiro\033[m')
                sleep(1)
        total = computador + jogador

        # Validação da escolha entre Par ('P') ou Ímpar ('I')
        while escolha not in ('P', 'I'):
            limpar_terminal()
            escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]

        limpar_terminal()

        print('\033[36m=-=' * 19)
        print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {total},',
              'deu PAR' if total % 2 == 0 else 'deu IMPAR')
        print('\033[36m=-=\033[m' * 19)

        # Apuração do resultado
        match escolha:
            case 'P':
                if total % 2 == 0:
                    print('\033[1;32m\nVOCÊ GANHOU!!!\033[m')
                else:
                    print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')
            case 'I':
                if total % 2 == 0:
                    print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')
                else:
                    print('\033[1;32m\nVOCÊ GANHOU!!!\033[m')

        sleep(1)

        if sair() == 'N':
            limpar_terminal()
            print('Obrigado por jogar, volte sempre.')
            sleep(1)
            break