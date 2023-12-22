from time import sleep


def titulo(msg):
    print()
    print(f'--- {msg} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.009)
    print('\n')


print()
lento('Agora vamos abrir o arquivo para gravação')
lento('Lembrando que o modulo open() é usado para abrir o arquivo')
arq2 = open('Cap06/arquivos/arquivo2.txt', 'w')
print('O w = write. Significa escrita')
len('Quando se utiliza o modo "w" tem que ter muita atenção, porque se não encontrar o arquivo solicitado vai ser criado o arquivo se o arquivo já existir o modo "w" vai sobrescrever')
print(arq2.read())
print()
lento('Lembrando')
