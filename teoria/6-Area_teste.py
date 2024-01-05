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


lento('Um outro pacote muito usado é o pacote RANDOM.\nCom ele consegue fazer a randomização de números e string.\n Segue exemplos abaixo.')
random_str = random.choice(['Abacaxi','Banana', 'Laranja'])# Choice, é escolher em Ingles.
print(f'Usando o pacote random com a função choice, consegui de forma "aleatória" o resuldato de uma lista {random_str}')
print()
random_num = random.sample(range(100),10)# Sample, é amostra em Ingles.
print(f'Usando o pacote random com a função sample, consegui de forma "aleatória" o resultado de uma lista{random_num}')
print()
lento('Um outro exmplo de pacote é: statistics')
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados)) #É um método de calcula a média
print(statistics.median(dados)) # É um método que calcula a mediana

lento('Com o pacote os(sistema operacional) pode trazer o local aonde o programa ta sendo executado.\nExemplo a baixo.')
local_os = os.getcwd()
print(local_os)
print()

lento('Podemos trabalhar com módulos dos pacotes(quando disponível).\nSegue exemplo:')
lento('Com o pacote import urllib.resquet. Onde urllib é o pacote e request é o módulo (import urllib.request).\nEntão junto com o pacote e o modulo pode ser chamado depois a função urlopen()')
resposta = urllib.request.urlopen('http://python.org')
print(f'{resposta}\nEssas informações é um objeto do tipo http, expecificamente http da parte do cliente. Com essa informação podemos fazer a  extração do código HTML.\nPara fazer isso é só ler com read() a variável e imprimir com print().html = resposta.read()\nprint(html)')
html = resposta.read()
#print(html)
