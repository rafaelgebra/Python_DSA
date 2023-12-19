from platform import python_version


def titulo(msg):
    print()
    print(f'-- {msg} --')


def par():
    for i in range(1, 20):
        if i % 2 == 0:
            print(i)  


def string(msg):
    return msg.upper()


def lista(*num):
    for i in range(1,3):
        lis.append(int(input(f'Digite {i}º numero: ')))
    print(lis)


def num(arg1, *lis):
    print(arg1)
    for i in lis:
        print(i)



def soma1(arg1, arg2):
    total = arg1 + arg2 
    print ("Dentro da função o total é: ", total)
    return total


titulo(f'A versão que estamos trabalhando é {python_version()}')

titulo('Exercícios - Métodos e Funções (Solução)')

print('Ex:1')
# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números
par()
print()


titulo('Ex:2')
# Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string
msg = str(input('Digite uma mensagem. '))
print(string(msg))
print()

titulo('Ex:3')
# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
lis = [1, 2, 3, 4]
lista(lis)

titulo('Ex:4')
# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos
num('teste')
num(1, 3, 2, 5)

titulo('Ex:5 (LAMBDA)')
# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles
soma = lambda arg, arg2: arg + arg2
print(f'A soma entre as valores {soma(3, 7)}')

titulo('Ex:6')
# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
soma1(10, 20)
print (f'Fora da função o total é: { total}')

titulo('Ex:7')
# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
Celsius = [39.2, 36.5, 37.3, 37.8]

def Cel(*num):
    for i in(num):
        for v in i:
            n = (v * 9/5) + 32
            print(f'Para a temperatura em {v}Cº a converção fica {n:.2f}Fº')
Cel(Celsius)