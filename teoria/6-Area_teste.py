from platform import python_version
from time import sleep
from urllib import response
import pandas as pd
import os
import csv
import json
from urllib.request import urlopen
import numpy

def titulo(msg):
    print()
    print(f'--- {msg.upper()} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.003)
    print('\n')



lento('Em Python, um módulo é um arquivo (script) que contém códico Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções, classes e variáveis entre arquivos.\nJá um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos modulos, o que facilita a manutenção e o desenvolvimento.\nVisite o PyPi, repositório de pacotes da linguagem Python: https://pypi.org/')

dados = (dir(numpy))
lento('Agora será impresso todos os métodos e atributos do pacote numpy.\nAlguns são modulos outros não, depende da organização do pacote')
for valor in dados:
    print(valor)
print()
print(f'O resultado da raiz quadrade de 25 é: {numpy.sqrt(25)}')
print()