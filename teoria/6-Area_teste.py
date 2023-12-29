from platform import python_version
from time import sleep
from urllib import response 
import pandas as pd
import os
import csv
import json
from urllib.request import urlopen

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

response = urlopen('https://compras.dados.gov.br/licitacoes/doc/licitacao/02000105001802012.json').read().decode('utf8')
dados = json.loads(response)

arquivo_fonte = 'Cap06/arquivos/pro.json'
arquivo_destino = 'Cap06/arquivos/dados1.json'
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfiles:
        outfiles.write(text)
with open('Cap06/arquivos/dados1.json') as arquivo1:
    texto = arquivo1.read()
    dados = json.loads(texto)
print('modalidade: ', dados['modalidade'])
print('situacao_aviso: ', dados['situacao_aviso'])

