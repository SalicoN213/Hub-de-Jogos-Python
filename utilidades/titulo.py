"""
Módulo de Títulos (titulo.py)
Utiliza a biblioteca pyfiglet para estilizar os títulos exibidos no terminal.
"""

from pyfiglet import figlet_format

def titulo(texto):
    """
    Recebe um texto ou número identificador e imprime uma arte em ASCII
    correspondente ao título do jogo ou seção.
    """
    mapa = {1: 'Adivinhacao', 2:  'Jokenpo', 3: 'Par ou Impar', 4: 'Caca Niquel', 5: 'Blackjack'}

    if texto.isdigit():
        if int(texto) == 5:
            print(figlet_format('Blackjack', 'cards'))
        else:
            print(figlet_format(mapa[int(texto)], 'big'))

    else:
        print(figlet_format(texto, 'big'))