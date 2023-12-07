from time import sleep


def titulo(msg):
    print(f'--- {msg} ---')

mensangem = 'Um número primo é um número natural maior do que 1 que pe divisível apenas por 1 e por ele mesmo. Isso significa que não há nenhum outro número inteiro que possa dividir o número primo sem deixar resto. Por exemplo, o número 2 é primo, pois é divisivel por 1 e 2. O número 4 não é primo, pois é divisível por 2.'
for letra in mensangem:
    print(letra, end='', flush=True)
    sleep(0.1)

#Vamos encontrar números primos de uma coleçãp de números usando loop WHILE e FOR juntos.
