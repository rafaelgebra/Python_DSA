from operator import length_hint
from time import sleep
import pandas as pd
import os
import csv

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

lento('CSV (Comma-Separated Values "VALORES SEPARADOS POR VIRGULA") é um formato de arquivo que armazena dados tabulares em formato de testo plano. Cada linha do arquivo CSV representa uma linha da tabela e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e importar dados em diferentes aplicações, como planilhas e banco de dados. CSV é uma opção simples e universal para compartilhar dados, pois pode ser aberto e editado com muitos aplicativos diferentes, incluindo programas de planilhas e editor de texto.')

with open('Cap06/arquivos/numeros.cvs', 'w') as arquivo8: # Aqui esta fazendo a abertura do arquivo8 e mostrando o caminha com  open('Cap06/arquivos/numeros.cvs', 'w')
    write = csv.write(arquivo8) #Com o write = csv.write(arquivo*) é criado o objeto de gravação
    write.writerow(('nota1', 'nota2', 'nota3'))
    write.writerow((63, 87, 92))
    wri