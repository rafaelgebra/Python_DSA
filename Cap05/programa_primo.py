#Vamos encontrar números primos de uma coleçãp de números usando loop WHILE e FOR juntos.
from time import sleep


def titulo(msg):
    print()
    print(f'--- {msg} ---')
    print()


def lento(msg):
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.001)


titulo('ESSA É UMA EXPLICAÇÃO DO QUE É NÚMEROS PRIMOS')

explicacao = 'Um número primo é um número natural maior do que 1 que pe divisível apenas por 1 e por ele mesmo.\nIsso significa que não há nenhum outro número inteiro que possa dividir o número primo sem deixar resto.\nPor exemplo, o número 2 é primo, pois é divisivel por 1 e 2. O número 4 não é primo, pois é divisível por 2.'
print(lento(explicacao))


titulo('SEGUE O PSEUDOCÓDIGO')

pseudocodigo = 'Iniciar uma lista para armazenar os números primos. \nPara cada número N entre 2 e 30: \n    Inicialize uma variável eh_primo comm verdade.\n    Para cada número i entre 2 e N/2:\n      Se N é divisível por i, então: \n        Altere a variável eh_primo para falso \n        Pare de verificar os outros números \n    Se a variável eh_primo ainda é verdadeira, adicione N à lista de números primos \nImprima a lista de números primos.'
print(lento(pseudocodigo))

# Variável para armazenar números primos
primos = []
# Loop for para percorrer números de 2 a 30
for num in range(2, 31):
    # Variável de controle
    eh_primo = True
    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1
    # Adicionando o número primo na lista
    if eh_primo:
        primos.append(num)
print()
# Imprimindo a lista de números primos
print(lento(f'Esse são os números primos entre 2 à 30 {primos}.'))
