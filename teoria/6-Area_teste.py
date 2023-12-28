from encodings import utf_8
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

titulo('Manipulação de arquivos CSV - (Comma-Separated Values "VALORES SEPARADOS POR VIRGULA")')

lento('CSV (Comma-Separated Values "VALORES SEPARADOS POR VIRGULA") é um formato de arquivo que armazena dados tabulares em formato de testo plano. Cada linha do arquivo CSV representa uma linha da tabela e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e importar dados em diferentes aplicações, como planilhas e banco de dados. CSV é uma opção simples e universal para compartilhar dados, pois pode ser aberto e editado com muitos aplicativos diferentes, incluindo programas de planilhas e editor de texto.')

with open('Cap06/arquivos/numeros.cvs', 'w') as arquivo8: # Aqui esta fazendo a abertura do arquivo8 e mostrando o caminha com  open('Cap06/arquivos/numeros.cvs', 'w')
    write = csv.writer(arquivo8) #Com o write = csv.write(arquivo*) é criado o objeto de gravação
    write.writerow(('nota1', 'nota2', 'nota3')) #Gravar arquivo linha a linha
    write.writerow((63, 87, 92))
    write.writerow((61, 79, 76))
    write.writerow((72, 64, 91))
with open('Cap06/arquivos/numeros.cvs', 'r', encoding='utf8', newline='\r\n') as arquivo8:
    leitor = csv.reader(arquivo8) #Objeto de leitura # com o método reader() é lido cada linha e gera uma lista 
    for x in leitor: #Loop - vai percorrem o objeto = cada linha do objeto
        print(x)
with open('Cap06/arquivos/numeros.cvs', 'r') as arquivo8:
    leitor = csv.reader(arquivo8)
    dados = list(leitor)
print(dados)
for linha in dados[1]:
    print(linha)

titulo('Manipulando arquivo JSON(Java Script Object Notation)')
lento('JSON (JavaScript Object Notation) é um  formato de dados de text simples e leve que é utilizado para transmitir informações em aplicações WEB. É baseado em uma estrutura de objetos JavaScript e usa pares de chave-valor para representar dados. JSON é facilmente lidos e escritos por máquinas e é amplamente ultilzado com formatos de intercâmbio de dados em aplicações web modernas')
dict = {}