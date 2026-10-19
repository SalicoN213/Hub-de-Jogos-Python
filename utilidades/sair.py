"""
Módulo de Saída (sair.py)
Controla a lógica de repetição ou encerramento ao final de cada partida.
"""

from utilidades import limpar_terminal
from time import sleep

def sair():
    """
    Pergunta ao usuário se deseja jogar novamente.
    Retorna 'S' para sim ou 'N' para não, validando erros de digitação.
    """
    while True:
        try:
            reposta = input("\nDeseja jogar novamente? [S/N] ").upper().strip()[0]
            if reposta in ('S', 'N'):
                limpar_terminal()
                return reposta

            limpar_terminal()
            print("OPÇÃO INVALIDA!")
            sleep(1)
            limpar_terminal()

        except IndexError:
            limpar_terminal()
            print("DIGITE ALGO!")
            sleep(1)
            limpar_terminal()