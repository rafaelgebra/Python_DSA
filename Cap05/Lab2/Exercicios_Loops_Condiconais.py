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
# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista
lista2 = []
numero = 4

while numero <= 20:
    if numero % 2 == 0:
        lista2.append(numero)
    numero += 1
print(lista2)

titulo('Ex:8')
# Exercício 8 - Transforme o resultado desta função range em uma lista: range(5, 45, 2)
nums = [x for x in range(5, 45, 2)]
print(nums)

titulo('Ex:9')
# Exercício 9 - Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
    print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

titulo('Ex:10')
# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 
frase = "A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão." 
print(f'Tem {frase.count("r")} vezes a letra "r" nessa frase. ')
