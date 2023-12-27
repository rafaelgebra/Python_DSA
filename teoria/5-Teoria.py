from platform import python_version
from time import sleep 
import pandas as pd
import os
import csv

def titulo(msg):
    print()
    print(f'--- {msg} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.004)
    print('\n')

versao = python_version()
titulo(f'A versão do python que estamos usado é: {versao}')


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
        sleep(0.03)
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

titulo('COMO FUNCIONA A FUNÇÃO RANGE')
for i in range(1, 11):
    print(i, end='')

titulo('Exemplo de RANGE, com lista')

lista5 = ['Abacaxi', 'Banana', 'Morango', 'Uva']
lista_Tamanho = len(lista5)
print(f'Esse é os "valores" conteúdo da lista5: {lista5}')
print(f'Esse é o tamanha da lista5 com a função len(lista5): {lista_Tamanho}')
print()
for i in range(0, lista_Tamanho):
    print(lista5[i])

print(lento('Posição é com colchete []. Ex: lista5[i]'))
print()

titulo('METODOS')
metodos = 'Tudo em Python é o objeto. cada objeto tem métodos e atributos.\n      -Atributos são propriedades, características do objetivos. \n      -Métodos são funções com ações que podem ser executadas nos objetos.'
lento(metodos)
titulo('A função help() explica com ultizar cada método de um objeto')
print('Ex: help(print)')
#help(print)# Para sair da função help() usar shift + q

titulo('Para listar/mostrar todos os métodos e atributos de um objeto usar: dir(lista5)')
print('Ex: ')
listar = dir(lista5)
for i in listar:
    print(f"'{i}'")

titulo('Tipo especifico de função - LAMBDA (função anônima)')
print('Exemplo de Função "COMUM" em python')
def potencia(num):
    resultado = num ** 2
    return resultado
print('Esse é o resultado da função ', potencia(5),'\n')

print('Essa proxima função é feita de forma resulmida')
def potencia2(num):
    return num ** 2
print('Esse é o resultado da função resulmida', potencia2(5),'\n')

print('Agora é mais resulmido ainda, tudo na mesmoa linha de codigo')
def potencia3(num): return num ** 2
print('Esse resultado é com o código tudo na mesma linha ', potencia3(5),'\n')

lambda_Texto = 'Normalmente não é atribuido uma variável a uma expressão em Python.\nA expressão LAMBDA cria uma função em tempo de execução (Não precisa nominar a função), EX:'
print(lento(lambda_Texto))

potencia4 = lambda num: num ** 2
print(f'Esse resuldato é usado a função LAMBDA \n(potencia4 = lambda num: num ** 2) =  {potencia4(5)}\n')

print('Segundo EX:\nOperadores de comaparação retornam boolean: TRUE or FALSE \n')
par = lambda x: x % 2 == 0
print(f'Esse é um exemplo usando a função LAMBDA.\npar = lambda x: x % 2 == 0: {par(3)}\n')
print(f'Esse é um exemplo usando a função LAMBDA.\npar = lambda x: x % 2 == 0: {par(4)}\n')

print('Terceiro EX:\n Usando A função LAMBDA em sting (str)\n')
frist = lambda s: s[0]
print(f'Com essa opção consegue fazer a separação de caracter por indice, nessa caso frist = lambda s: s[0] "{frist("Python")}"\n')
reverso = lambda s : s[::-1]
print(f'Também da para fazer a reverção com por analise de string. reverso = lambda s : s[::-1] "{reverso("Python")}"\n')

titulo('List Comprehension e Dict Comprehension "é uma forma de resulmir o função em lista e dicionario"')
print('Ex 1:\n')

print('Uma expressão em list comprehension segue a seguinte ideia: [x for x in range(10)].\nIsso significa o seguinte.\nO primeiro x é o retorno da função, for(para) valor(x) in(dentro/em) range(0, 10)')
lista_Numeros = [x for x in range(10)]
print(lista_Numeros,'\n')

print('Ex 2: Usando operadores condicionais')
lista_Numeros2 = [x for x in range(10) if x <= 5]
print(f'Essa resposta foi filtrada com operadores condicionais (if, elif, else) e relacionais (<, <=, ==, !=, >=, > )  e só vai aparecer os números 0 à 5:\nA expressão é lista_Numeros2 = [x for x in range(10) if x <= 5] = {lista_Numeros2}\n')

lista_Frutas = ['banana', 'abacaxi', 'melancia', 'cereja', 'manga']
nova_Lista = []
for x in lista_Frutas:
    if 'm'.lower() in x:
        nova_Lista.append(x)
print('O código é o seguinte.\nfor x in lista_Frutas:\n    if "m".lower() in x:z\n        nova_Lista.append(x)\nprint(nova_Lista)')        
print(f'Esse é o resultado de um loop FOR sem usar a list comprehension: {nova_Lista}.\n')
print('A proxima expressão é usando o metodo de list comprehension.\n ')
nova_Lista = [x for x in lista_Frutas if 'm'.lower() in x]
print(f'Essa é a lista usando a list comprehension. {nova_Lista}.\nPode notar que não tem alteração, a diferença é no linha de comando.')

titulo('Dict Comprehension --- Dicionario, é um conjunto de pares contendo chave e valor. Ex: dic_Aluno = {"Bob":25, "Thati": 20}')
dict_Aluno = {'Bob':68, 'Michel':84, 'Zico':57, 'Ana':93 }
print(f'Esse é o dicionario dict_Aluno com os seus pares de chave:valor: {dict_Aluno} \n. Essa linha de código é a original')
dict_Alunos_Status = {k:('Aprovado' if v > 70 else 'Reprovado') for (k, v) in dict_Aluno.items()}

print(f'Com a modificação no código acrescentando ("Aprovado" if v > 70 else "Reprovado") no lugar do resultado de v, conseguimos fazer a manipulação de status.\nAntes era {dict_Aluno}\nAgora é {dict_Alunos_Status}\n')

titulo('Manipulação de Arquivos em Python')

print('Informação: "open" é abrir em inglês')
print('Informação: "r" = "read" é ler em inglês\n')

arq1 = open('Cap06/arquivos/arquivo1.txt', 'r')
print('Para ver o tipo do objeto usar o metodo - type()')
print(type(arq1),'\n')

print('Para LER o arquivo usar o metodo - read() = r')
print(arq1.read(),'\n')

print('Contar o números de caracteres. Para fazer isso só usar o metodo - tell()')
print(arq1.tell(),'\n')

print('Imprimento o arquivo novamente sem resetar o locar do "cursor"')
print(f'O arquivo foi "impresso" porém não tem o que imprimir, porque o cursor esta no fim da frase.{arq1.read()}\n')

print('Agora vamos retornar para o cursor no início do arquivo, usar o metodo - seek(0,0) = seek é metodo, 0,0 é o posição do "cursor" nesse caso esta trazendo para o inicio da frase.')
arq1.seek(0,0)
print(arq1.read(),'\n')

print('Com o metodo read() da para escoler até que letra quer que "imprima":')
arq1.seek(0,0)
print(arq1.read(23))
print('Se chamar novamente a leitura ele continua da onde parou a leitura:')
print(arq1.read())
print('Para voltar do inicio é do usar novamente o metodo seek(0,0) que o "cursor volta para o inicio da frase"')
arq1.seek(0,0)
print(arq1.read(),'\n')

print()
lento('Agora vamos abrir o arquivo para gravação')
lento('Lembrando que o modulo open() é usado para abrir o arquivo')
arq2 = open('Cap06/arquivos/arquivo2.txt', 'w')
print('O w = write. Significa escrita')
lento('Quando se utiliza o modo "w" tem que ter muita atenção, porque se não encontrar o arquivo solicitado vai ser criado o arquivo se o arquivo já existir o modo "w" vai sobrescrever')
#print(arq2.read())# se o arquivo foi aberto apenas para escrita 'w = write' o não tem como ler 'r = read'
print()
lento('Para gravar no arquivo usar o metodo write()')
arq2.write('Aprendendo a programar em Python. E a metodologia de ensino da Data Science Academy facilita o aprendizado.')
arq2.close()
arq2 = open('Cap06/arquivos/arquivo2.txt', 'r')
print(arq2.read())
print()

lento('Agora vamos abrir o arquivo no metodo "a = append" acrescentar')
arq2 = open('Cap06/arquivos/arquivo2.txt', 'a')
arq2.write('\nE a metodologia de ensino da Data Science Academy facilita o aprendizado')
arq2.close()
arq2 = open('Cap06/arquivos/arquivo2.txt', 'r')
print(arq2.read())
arq2.seek(0,0)
print(arq2.read())


titulo('Abrindo Dataset em linha Única')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows)

titulo('Dividindo Um Arquivo em colunas')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
#print(full_data)

titulo('Contando as linha de um arquivo')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1
print(f'O arquivo "salarios.csv" tem {count} linhas')

titulo('Contando o número de colunas de um arquivo')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
first_row = full_data[0]
count1 = 0
for calumn in first_row:
    count1 += 1
print(f'O total de colunas é {count1}.')

titulo('Introdução ao PANDAS = Modulo adicional')

print(f'Essa é a versão do PANDAS que estamos usando {pd.__version__}')
arquivo3 = 'Cap06/arquivos/salarios.csv'
df = pd.read_csv(arquivo3) #df = dataframe
print(df.head())
print(df['Position Title'].value_counts())

titulo('Manipulação de arquivos - Parte 2. Formados TXT, CSV, JSON')
lento('TXT é a externsão de arquivos para arquivos de texto puro. Um arquivo TXT é uma arquivo de texto simples sem formação, com negrito, itálico ou fontes diferentes. Eles pode ser aberto e editado com muitos aplicativos diferentes, incluindo editores de texto, processandores de texto e IDEs. Arquivos TXT são amplamentes utilizados para armazenar dados de texto simples, como listas, notas e documentos de texto. Eles são universais e podem ser lidos em praticamente qualquer dispositivo ou sistemas operacional.')

texto = 'Ciêntista de Dados pode ser uma excelente alternativa de carreira. \n'
texto += 'Esses profissionais precisam saber como programar em Python. \n'
texto += 'E, Claro, devem ser proficientes sem Data Science'
print(lento(texto))

lento('O módulo "os" permite interagir com o sistema operacioal de forma mais façil')
arquivo5 = open(os.path.join('Cap06/arquivos/cientista.txt'), 'w')
print(lento('Lembrete. "open" é abrir do pacote python.\nDo pacote "os" vai chamado o pacote "path" que é caminho e "join" que pe juntar.\nIsso tudo é para abrir o arquivo para gravação "Cap06/arquivos/cientista.txt"'))
for palavra in texto.split():#Esta sendo criado um loop para percorrer o a variável, o split() sem nada dentro dos parenteses, significa que é para fazer a divição no espaço entre as palavras
    arquivo5.write(palavra + ' ')#Posso usar a escrever em cima da mesma variável de antes usando metodo write() colocando como parametro o resulta do for + ' ' para separar as letras. No for retirou todos os espeços "limpando". Agora dentro da arquitetura do for estamos separando as palavras por espaço e deixando tudo na mesma linha.   
arquivo5.close() # o metodo close() é usado para feixar a edisão do arquivo.
arquivo5 = open('Cap06/arquivos/cientista.txt', 'r')# Agora novamente é feita a abertura do arquivo agora no modo read que é a leitura.
conteudo = arquivo5.read()# Para para uma variável o 'conteúdo desse arquivo' com o metudo read()
arquivo5.close()# Novamente é usando o metodo close() para fechar o arquivo para não ocorrer erros/bugs/corromper os dados
print(conteudo)

titulo('Manipulando Arquivos TXT em Python com a Expressão with')
lento('Nessa expressão o método close() é fechado automaticamente, então com esse metodo pode abrir tanto read(), write(), e outras')
with open('Cap06/arquivos/cientista.txt', 'r') as arquivo6:#Nessa sintaxe é colocado o "with = com" é colocado no começo da expressão, após isso é colocado o método open('o local, o nome do arquivo e o tipo'), após isso é colocado "as = como" que é para por o nome/apelido"carinhoso" do arquivo para ser usado em python - nesse exemplo o nome do arquido é arquivo6.
    conteudo = arquivo6.read()# Essa linha de comando é execurada após o execusão de cima (aqui pode ser feita qualquer coisa)
print(len(conteudo))#com o método len() consegui ter a informação do comprimento do conteúdo
print(conteudo)

titulo('Segundo Exemplo')

with open('Cap06/arquivos/cientista.txt', 'w') as arquivo7:
    arquivo7.write(texto[:19])#Isso é analize se dados, vai ser pego os 19 caracters iniciais
    arquivo7.write('\n')#Vai dar um Enter
    arquivo7.write(texto[28:66])#Agora pega os caracters do 28 até o 65 - o 66 fica de fora.

arquivo7 = open('Cap06/arquivos/cientista.txt', 'r')#Faz novamente a apertura do arquivo mas como leitura do  'r'
conteudo1 = arquivo7.read()#Grava em uma variável usando o método leitura read()
arquivo7.close()#fecha o arquivo com cloase()
print(conteudo1)# imprime o conteúdo da variável 