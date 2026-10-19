"""
Módulo de Mapeamentos (mapas.py)
Contém funções que retornam dicionários de mapeamento para cartas do baralho
e para a execução das funções dos jogos.
"""

import jogos as j

def baralho_map():
    """
    Retorna um dicionário representando um baralho padrão de Blackjack,
    onde cada carta (chave) possui o seu respectivo valor numérico (valor).
    """
    return {
        '2♠': 2, '2♥': 2, '2♣': 2, '2♦': 2, '3♠': 3, '3♥': 3, '3♣': 3, '3♦': 3,
        '4♠': 4, '4♥': 4, '4♣': 4, '4♦': 4, '5♠': 5, '5♥': 5, '5♣': 5, '5♦': 5,
        '6♠': 6, '6♥': 6, '6♣': 6, '6♦': 6, '7♠': 7, '7♥': 7, '7♣': 7, '7♦': 7,
        '8♠': 8, '8♥': 8, '8♣': 8, '8♦': 8, '9♠': 9, '9♥': 9, '9♣': 9, '9♦': 9,
        '10♠': 10, '10♥': 10, '10♣': 10, '10♦': 10, 'J♠': 10, 'J♥': 10, 'J♣': 10, 'J♦': 10,
        'Q♠': 10, 'Q♥': 10, 'Q♣': 10, 'Q♦': 10, 'K♠': 10, 'K♥': 10, 'K♣': 10, 'K♦': 10,
        'A♠': 11, 'A♥': 11, 'A♣': 11, 'A♦': 11,
    }

def funcoes_map():
    """
    Mapeia os códigos em string do menu principal para as respectivas
    funções de jogos importadas.
    """
    return {
        '1': j.adivinhacao, '2': j.jokenpo, '3': j.par_ou_impar,
        '4': j.caca_niquel, '5': j.blackjack
    }