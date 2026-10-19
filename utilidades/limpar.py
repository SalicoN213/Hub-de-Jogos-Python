"""
Módulo de Limpeza de Tela (limpar.py)
Responsável por limpar o terminal independentemente do sistema operacional.
"""

import os

def limpar_terminal():
    """
    Executa o comando de limpeza de tela compatível com Windows ('cls')
    ou sistemas Unix/Linux/Mac ('clear').
    """
    os.system('cls' if os.name == 'nt' else 'clear')