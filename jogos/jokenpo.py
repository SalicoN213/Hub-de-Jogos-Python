"""
Módulo do Jogo Jokenpô (jokenpo.py)
Implementa o clássico jogo Pedra, Papel e Tesoura contra o computador.
"""

from random import randint
from time import sleep
from utilidades import limpar_terminal, sair

def jokenpo():
    """Função principal que gerencia as jogadas, validações e regras do Jokenpô."""
    while True:
        itens = ['Pedra', 'Papel', 'Tesoura']
        computador = randint(0, 2)

        # Loop para garantir a escolha válida do jogador.
        while True:
            try:
                limpar_terminal()
                print('\033[35m=-=' * 10)
                print('''    ESCOLHA:
        [ 1 ]Pedra
        [ 2 ]Papel
        [ 3 ]Tesoura''')
                print('\033[35m=-=\033[m' * 10)
                jogador = int(input('Sua Escolha: ')) - 1
                break
            except ValueError:
                limpar_terminal()
                print('\033[1;31mEscolha um número inteiro entre 1 e 3!!!\033[m')
                sleep(1)

        # Efeito dramático de contagem
        limpar_terminal()
        print('\033[1;36mJO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ\033[m')
        sleep(1)
        limpar_terminal()

        print('\033[35m~' * 40)
        print(f'{f'O computador escolheu {itens[computador]}':^40}')
        print(f'{f'O jogador escolheu {itens[jogador]}':^40}')
        print('\033[35m~\033[m' * 40)

        # Regras de vitória, derrota ou empate.
        match computador:
            case 0:
                match jogador:
                    case 0:
                        print('\033[1;033m\nEMPATOU!!!\033[m')
                    case 1:
                        print('\033[1;032m\nVOCÊ GANHOU!!!\033[m')
                    case 2:
                        print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')
            case 1:
                match jogador:
                    case 0:
                        print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')
                    case 1:
                        print('\033[1;033m\nEMPATOU!!!\033[m')
                    case 2:
                        print('\033[1;032m\nVOCÊ GANHOU!!!\033[m')
            case 2:
                match jogador:
                    case 0:
                        print('\033[1;032m\nVOCÊ GANHOU!!!\033[m')
                    case 1:
                        print('\033[1;31m\nVOCÊ PERDEU!!!\033[m')
                    case 2:
                        print('\033[1;033m\nEMPATOU!!!\033[m')
        sleep(0.5)

        if sair() == 'N':
            limpar_terminal()
            print('Obrigado por jogar, volte sempre.')
            sleep(1)
            break