"""
Módulo do Caça-Níquel (caca_niquel.py)
Simula um jogo de caça-níquel com animação visual no terminal e verificação de combinações.
"""

from utilidades import limpar_terminal, sair
from random import choice
from time import sleep

simbolos = ['#', '@', '$', '%', '&', '*']

def mostrar_animacao():
    """Exibe uma animação rápida simulando o giro dos rolos da máquina."""
    for _ in range(10):
        limpar_terminal()
        print('=' * 20)
        print(f'| {choice(simbolos)}  | | {choice(simbolos)}  | | {choice(simbolos)}  |')
        print('=' * 20)
        sleep(0.15)
    limpar_terminal()

def girar_rolo():
    """Retorna um símbolo aleatório para compor o resultado do giro."""
    return choice(simbolos)

def caca_niquel():
    """Função principal que executa o jogo de Caça-Níquel."""
    while True:
        resultado = [girar_rolo(), girar_rolo(), girar_rolo()]

        mostrar_animacao()

        print('=' * 20)
        print(f'| {resultado[0]}  | | {resultado[1]}  | | {resultado[2]}  |')
        print('=' * 20)

        # Verifica se houve vitória, quase-acerto ou derrota
        if resultado[0] == resultado[1] == resultado[2]:
            print('\n\033[1;32mVOCÊ GANHOU!!!\033[m')
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            print('\n\033[1;33mQUASE!!!\033[m')
        else:
            print('\n\033[1;31mVOCÊ PERDEU!!!\033[m')

        if sair() == 'N':
            limpar_terminal()
            print('Obrigado por jogar, volte sempre.')
            sleep(1)
            break