from difflib import restore
from operator import length_hint
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
    print(f'--- {msg.upper()} ---')
    print()

def lento(msg, t=0.003):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(t)
    print('\n')

