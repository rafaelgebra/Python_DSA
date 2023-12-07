from time import sleep 

print('\n')
print('EXPLICAÇÃO DE CONDICIONAL IF, ELIF, ELSE')
print('PRIMEIRA CONDIÇÃO')
# Condição if(se) e else(senão)
if 5 > 2:
    print('Verdade\n')
else:
    print('Falso\n')

print('SEGUNDA CONDIÇÃO')
# Codição if e else com variável
dia = 'Terça'
if dia == 'Segunda':
    print(f'Correto hoje é {dia}\n')
else:
    print(f'Incorreto hoje é {dia} não Segunda\n')

print('TERCEIRA CONDIÇÃO retorna valor Booleano True(verdade) ou False(falso)')
if dia == 'Segunda':
    print('Correto hojé Segunda \n')
elif dia == 'Terça':
    print(f'Incorreto hoje é {dia} não Segunda \n')
else:
    print('Tente novamente \n')

print('OPERADORES RELACIONAIS')

print('<, >, <=, >=, ==, !=')
print('6 > 3?   ',6 > 3)
print('3 > 7?   ',3 > 7)
print('4 >= 4?  ',4 >= 4)
print('4 <= 4?  ',4 <= 4)
print('4 == 4?  ',4 == 4)
print('4 != 4?  ',4 != 4)

print('\nOPERADORES LOGICOS')
print('and  (e)')
print('or   (ou)')
print('not  (não)\n')

print('TRABALHANDO COM LOOP FOR (PARA)')

tupla = (2, 3 ,4)
for i in tupla: # i representa o valor dentro do array
    print(i, end=', ')
print('\n')
print('TRABALHANDO COM LOOP FOR (PARA) com range()')
for contador in range(0, 5):
    print(contador, end=', ')
print('\n')
for caracter in 'Python é uma linguagem de programação divertida!':
    print(caracter, end='')
print('\n')

print('LOOP FOR ANINHADO')
lista1 = [0, 1, 2, 3, 4]
lista2 = [1, 2, 3]

total = 0
print(f'Esse é o conteúdo da lista1 {lista1}')
print(f'Esse é o conteúdo da lista2 {lista2}')
for elementos_lista1 in lista1:
    for elementos_lista2 in lista2:
        total = elementos_lista1 * elementos_lista2
        print(f' {elementos_lista1} * {elementos_lista2:} = {total:>2}' )
        sleep(0.1)
print('\n')

print('PROCURANDO NUMERO 47 DENTRO DE DUAS LISTAS')
lista3 = [10, 16, 24, 39, 47, 2, 3, 4, 5]
lista4 = [32, 2 , 3, 4, 89, 47, 76, 12]
c1 = 0
for elementos_lista3 in lista3:
    c1 += 1
    c2 = 0
    for elementos_lista4 in lista4:
        c2 += 1
        if elementos_lista3 == 47 and elementos_lista4 == 47:
            print(f'Foi encontrado o elemento (47) na posição ({c1}) da lista3 e na posição ({c2}) da lista4')
print('\n')

