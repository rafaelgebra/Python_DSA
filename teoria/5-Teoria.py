from time import sleep 

def titulo(msg):
    print()
    print(f'--- {msg} ---')
    print()


def lento(msg):
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.001)


titulo('EXPLICAÇÃO DE CONDICIONAL IF, ELIF, ELSE')
titulo('PRIMEIRA CONDIÇÃO')
# Condição if(se) e else(senão)
if 5 > 2:
    print('Verdade\n')
else:
    print('Falso\n')

titulo('SEGUNDA CONDIÇÃO')
# Codição if e else com variável
dia = 'Terça'
if dia == 'Segunda':
    print(f'Correto hoje é {dia}\n')
else:
    print(f'Incorreto hoje é {dia} não Segunda\n')

titulo('TERCEIRA CONDIÇÃO retorna valor Booleano True(verdade) ou False(falso)')
if dia == 'Segunda':
    print('Correto hojé Segunda \n')
elif dia == 'Terça':
    print(f'Incorreto hoje é {dia} não Segunda \n')
else:
    print('Tente novamente')

titulo('OPERADORES RELACIONAIS')

print('<, >, <=, >=, ==, !=')
print('6 > 3?   ',6 > 3)
print('3 > 7?   ',3 > 7)
print('4 >= 4?  ',4 >= 4)
print('4 <= 4?  ',4 <= 4)
print('4 == 4?  ',4 == 4)
print('4 != 4?  ',4 != 4,'\n')

titulo('OPERADORES LOGICOS')
print('and  (e)')
print('or   (ou)')
print('not  (não)\n')

titulo('TRABALHANDO COM LOOP FOR (PARA)')

tupla = (2, 3 ,4)
for i in tupla: # i representa o valor dentro do array
    print(i, end=', ')
print('\n')
titulo('TRABALHANDO COM LOOP FOR (PARA) com range()')
for contador in range(0, 5):
    print(contador, end=', ')
print('\n')
for caracter in 'Python é uma linguagem de programação divertida!':
    print(caracter, end='')
print('\n')

titulo('LOOP FOR ANINHADO')
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

titulo('PROCURANDO NUMERO 47 DENTRO DE DUAS LISTAS')
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


titulo('EXEMPLO DE LOOP FOR "procurando Maior e Menor número"')
matriz = [[42, 23, 34], [100, 215, 114, 1], [10.1, 98.7, 12.3]]
maior_Numero = menor_numero = c = 0
for linha in matriz:
    for numero in linha:
        if c == 0:
            menor_numero = numero
            c += 1
        else:
            if numero > maior_Numero:
                maior_Numero = numero
            elif numero < menor_numero:
                menor_numero = numero
print()
print('Essa são os elementos da matriz', matriz,'\n')
print(f'O maior número encontrado é {maior_Numero}')
print(f'O menor número encontrado é {menor_numero}\n')

titulo('USANDO LOOP FOR EM DICIONARIO')
print('')

dic = {'k1':'Python', 'k2':'R', 'k3':'Scala'}

titulo('essa opção só mostra as chaves (keys) do dicionario')
for item in dic:
    print(item)
print()
titulo('Essa opção (items), mostra as chaves (keys), e valor (values)') 
for k, v in dic.items():
    print(f'O valor "{v}" pentence a chave "{k}"')
print()

print()
titulo('USANDO O LOOP WHILE')
titulo('EX1 - Como ponto de "chegado pré-definido"')
valor = 0
fim = valor + 10
while valor <= fim:
    print(valor, end=', ')
    valor += 1
print()

print()
titulo('MAIS UM EXEMPLO DE LOOP WHILE, AGORA USANDO O ELSE NO FINAL.')
x = 0
while x < 10:
    print(f'O valor de x nesta inteação é: {x}')
    print('x ainda é menor que o limite, por isso será somando mais 1')
    x += 1
else:
    print()
    print(f'LOOP WHILE foi conclúido. O número {x} é o limite, por isso ele não foi somado')
print()

titulo('Manupular WHILE com as cláusulas PASS (passar), BREAK (quebrar, "sair"), CONTINUE (continuar)')
valor = 0
while valor < 10:
    if valor == 4:
        break
    else:
        pass
        if valor == 3:
            print(valor, end=' ')
        else:
            print(valor, end=', ')
    valor += 1
print()


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
