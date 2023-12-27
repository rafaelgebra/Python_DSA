from operator import length_hint
from time import sleep
import pandas as pd
import os

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


titulo('Segundo Exemplo')
titulo('Manipulando Arquivos TXT em Python com a Expressão with - Nessa expressão o método close() é fechado automaticamente')


