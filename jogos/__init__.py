"""
Módulo de Inicialização do Pacote de Jogos (__init__.py)
Responsável por agrupar e expor todas as funções dos jogos disponíveis no projeto.
"""

from .advinhacao import adivinhacao
from .caca_niquel import caca_niquel
from .jokenpo import jokenpo
from .par_ou_impar import par_ou_impar
from .blackjack import blackjack

# Define os símbolos públicos exportados quando o pacote é importado via 'from jogos import *'
__all__ = [
    'advinhacao',
    'caca_niquel',
    'jokenpo',
    'par_ou_impar',
    'blackjack'
]