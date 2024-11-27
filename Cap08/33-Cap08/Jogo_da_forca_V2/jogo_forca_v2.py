# Projeto 2- Desenvolver a segunda versão do Game Forca em Python.
# Iniciar importando a biblíoteca 'random' para escolher de forma aleatória as palavras e a biblíoteca 'os' de systema

import random
from os import system, name

def limpa_tela():
    # Limpar tela se o sistema operacional dor Windows.
    if name == "nt": # "nt" é o nome interno dado para o sistema operacional Windows.
        _ = system("cls") # se o sistema operacional for Windons, com o comando "cls" é realizado a limpeza da tela.
    # o underline esta sendo usado como variável de retorno, mas como não será usado fica sem uso
    else:
        _ = system("clear") # Para outros sistemas operacionais como Mac ou linux o comando "clear" faz a limpeza da tela.

