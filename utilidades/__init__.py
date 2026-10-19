"""
Módulo de Inicialização do Pacote de Utilitários (__init__.py)
Responsável por agrupar e expor funções essenciais de utilidade para os outros módulos do projeto.
"""

from .limpar import limpar_terminal
from .sair import sair
from .titulo import titulo
from .mapas import baralho_map, funcoes_map

# Define os símbolos públicos exportados quando o pacote é importado via 'from utilidades import *'
__all__ = [
    'limpar_terminal',
    'sair',
    'titulo',
    'baralho_map',
    'funcoes_map'
]