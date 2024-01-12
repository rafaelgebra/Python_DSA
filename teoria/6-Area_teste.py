from difflib import restore
from platform import python_version
from time import sleep
from urllib import response
import pandas as pd
import os
import csv
import json
from urllib.request import urlopen
import numpy
import random
import statistics
import urllib.request
from functools import reduce


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

#Função zip()
titulo('Usando função zip()')
lento('A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como lista, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.')

x = [1, 2, 3]
y = [4, 5, 6]
lento(f'Exemplo de como usar a função zip()\nx = [1, 2, 3]\ny = [4, 5, 6] o resultado normalmente é um objeto iterável: {zip(x, y)}')
lento(f'Mas convertendo para uma lista, podemos ter o resultado: {list(zip(x, y))}')
print()
titulo('Para unir as estruturas podemos usar a função zip() mas tem suas limitações.\n os valores/"conteúdo" tem que ter a mesma quantidade.')
print('Ex:')
print(list(zip('ABCD', 'YX')))
lento('A lista original código original é list(zip("ABCD","YX")), como uma das listas é menor a função zip() só consegui ir até aonde tem informação.')
lento('Isso também acontece com números ou qualquer outros "dados/valores/conteúdo".\n Ex')
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
lento('As listas originais são:\na = [1, 2, 3]\nb = [4, 5, 6, 7, 8]')
print(list(zip(a, b)))
lento('Os valores da nova lista não estão completos porque falta dados')
titulo('O mesmo acontece com qualquer objeto iterável feito pela função zip(), por exemplo dicionarios em Python')
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
print(list(zip(d1, d2)))
lento('Por padrão a função zip "combina" as chaves dos valores.\nPara alterar isso para os valores tem que chamar o método values de pelos menos de um dos funcionarios.\n Ex:\nprint(list(zip(d1, d2.values())))')
print(list(zip(d1, d2.values())))
titulo('Também da para fazer a mesma coisa usando um loop')
def trova_valores(d1, d2):
    dict_temporario = {}
    for d1key, d2values in zip(d1, d2.values()):
        dict_temporario[d1key] = d2values
    return dict_temporario
print(trova_valores(d1, d2))