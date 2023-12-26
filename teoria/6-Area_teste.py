from time import sleep
import pandas as pd

def titulo(msg):
    print()
    print(f'--- {msg.upper()} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.009)
    print('\n')

titulo('Manipulação de arquivos - Parte 2. Formados TXT, CSV, JSON')
lento('TXT é a externsão de arquivos para arquivos de texto puro. Um arquivo TXT é uma arquivo de texto simples sem formação, com negrito, itálico ou fontes diferentes. Eles pode ser aberto e editado com muitos aplicativos diferentes, incluindo editores de texto, processandores de texto e IDEs. Arquivos TXT são amplamentes utilizados para armazenar dados de texto simples, como listas, notas e documentos de texto. Eles são universais e podem ser lidos em praticamente qualquer dispositivo ou sistemas operacional.')

