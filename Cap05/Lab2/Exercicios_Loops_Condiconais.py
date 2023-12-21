from platform import python_version
print(f'A versão que estamos trabalhando de Python é: {python_version()}')


def titulo(msg):
    print()
    print(f'-- {msg.capitalize()} --')


def mult(*tup):
    for v in tup:
        for valor in v:
            resultado = valor * 2
            lista.append(resultado)
        print(lista)


# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
titulo('Ex:1')
dia = str(input('Que dia é hoje: ')).capitalize()
print(dia)
if dia in ['Sabado','Domingo']:
    print('Hoje é dia de descando')
else:
    print('Você precisa trabalhar!!')


titulo('Ex:2')
# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista
frutas = ['Morango', 'Abacaxi', 'Maça', 'Melão', 'Pera']
fruta = str(input('Qual fruta você esta procurando? ')).capitalize()
if fruta in frutas:
    print(f'{fruta}, faz parte da lista.')
else:
    print(f'{fruta}, NÃO faz parte da lista. ')


titulo('Ex:3')
# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista
tupla = (1, 2, 3, 4)
lista = []
print('O resultado é: ',end='')
(mult(tupla))


titulo('Ex:4')
# Exercício 4 - Crie uma sequência de números pares entre 100 e 150 e imprima na tela
for i in range(100, 150):
    if i % 2 == 0:
        print(i, end=' ')
print('\n')

titulo('Ex:5')
# Exercício 5 - Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, 
# imprima as temperaturas na tela
temperatura = 40
while temperatura > 35:
    print(temperatura, end=' ')
    temperatura -= 1
print('\n')

titulo('Ex:6')
# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa
contador = 0
while contador < 100:
    print(contador, end=' ')
    contador += 1
    if contador == 23:
        print('\n')
        break

titulo('Ex:7')