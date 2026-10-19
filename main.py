"""
Arquivo principal (main.py)
Responsável por executar o Hub de Jogos, gerenciar o menu principal
e direcionar o usuário para o jogo selecionado.
"""

from utilidades import limpar_terminal, titulo, funcoes_map
from time import sleep

while True:
    # Loop de exibição e validação do menu principal
    while True:
        limpar_terminal()

        titulo('Hub')
        sleep(1)
        limpar_terminal()
        print('\033[35m=-=' * 10)
        print('''   Selecione sua Opção:
        [ 0 ]Sair
        [ 1 ]Advinhação
        [ 2 ]Jokenpô
        [ 3 ]Par ou Impar
        [ 4 ]Caça Niquel
        [ 5 ]Blackjack''')
        print('\033[35m=-=\033[m' * 10)
        escolha = input('Sua opção: ')

        # Valida se a entrada do usuário está entre as opções disponíveis.
        if not escolha or escolha not in ('0', '1', '2', '3', '4', '5'):
            limpar_terminal()
            print("\033[1;31mCOMANDO NÃO RECONHECIDO!\033[m")
            sleep(1)
            limpar_terminal()
        else: break

    # Opção '0' encerra o programa principal
    if escolha == '0':
        limpar_terminal()
        print('Volte sempre')
        sleep(1)
        limpar_terminal()
        break

    # Mapeia as funções dos jogos disponíveis
    funcoes = funcoes_map()

    # Tratamento para opções que ainda estão em desenvolvimento.
    if escolha not in funcoes:
        limpar_terminal()
        print('\33[1;33mEm Desenvolvimento!\33[m')
        sleep(1)

    # Executa a função correspondente ao jogo escolhido
    if escolha in funcoes:
        limpar_terminal()
        titulo(escolha)
        sleep(1)
        funcoes[escolha]()