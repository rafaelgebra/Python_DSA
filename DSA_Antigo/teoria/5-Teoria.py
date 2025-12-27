
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
import numpy as dsa

def titulo(msg):
    print()
    print(f'--- {msg.upper()} ---')
    print()

def lento(msg, t=0.003):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(t)
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
potencia(5)
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

titulo('Manipulação de arquivos CSV - (Comma-Separated Values "VALORES SEPARADOS POR VIRGULA")')

lento('CSV (Comma-Separated Values "VALORES SEPARADOS POR VIRGULA") é um formato de arquivo que armazena dados tabulares em formato de testo plano. Cada linha do arquivo CSV representa uma linha da tabela e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e importar dados em diferentes aplicações, como planilhas e banco de dados. CSV é uma opção simples e universal para compartilhar dados, pois pode ser aberto e editado com muitos aplicativos diferentes, incluindo programas de planilhas e editor de texto.')

with open('Cap06/arquivos/numeros.cvs', 'w') as arquivo8: # Aqui esta fazendo a abertura do arquivo8 e mostrando o caminha com  open('Cap06/arquivos/numeros.cvs', 'w')
    write = csv.writer(arquivo8) #Com o write = csv.write(arquivo*) é criado o objeto de gravação
    write.writerow(('nota1', 'nota2', 'nota3')) #Gravar arquivo linha a linha
    write.writerow((63, 87, 92))
    write.writerow((61, 79, 76))
    write.writerow((72, 64, 91))
with open('Cap06/arquivos/numeros.cvs', 'r', encoding='utf8', newline='\r\n') as arquivo8:
    leitor = csv.reader(arquivo8) #Objeto de leitura # com o método reader() é lido cada linha e gera uma lista 
    for x in leitor: #Loop - vai percorrem o objeto = cada linha do objeto
        print(x)
with open('Cap06/arquivos/numeros.cvs', 'r') as arquivo8:
    leitor = csv.reader(arquivo8)
    dados = list(leitor)
print(dados)
for linha in dados[1]:
    print(linha)


titulo('Manipulando arquivo JSON(Java Script Object Notation)')
lento('JSON (JavaScript Object Notation) é um  formato de dados de text simples e leve que é utilizado para transmitir informações em aplicações WEB. É baseado em uma estrutura de objetos JavaScript e usa pares de chave-valor para representar dados. JSON é facilmente lidos e escritos por máquinas e é amplamente ultilzado com formatos de intercâmbio de dados em aplicações web modernas\n')
dict_guido = {'nome': 'Guido van Rossum',
              'liguagem': 'Python',
              'similar': ['c', 'Modula-3', 'lisp'],
              'users': 1000000}
for k, v in dict_guido.items():
    print(k, v)
print()

print(f'Aqui é feito a impressão usando o pacote de importação "JSON" com o método função json.dumps(dict_guido), onde json.dumps é a função onde converte o dicionario Python em formato "JSON" e (dict_guido) é o parametro "dicionario Python".{json.dumps(dict_guido)}\n')

with open('Cap06/arquivos/dados.json', 'w') as arquivo9: # aqui é feita a "gravação/criação".
    arquivo9.write(json.dumps(dict_guido)) #Novamente (json.dumps(disct_guido)) é a converção do dicionario python para o formato "JSON". O método write é para gravar/criar na variável arquivo9.
with open('Cap06/arquivos/dados.json', 'r') as arquivo10:# Aqui é aberto novamente o arquivo, só que para leitura agora.
    texto = arquivo10.read() #Com o método read(), é usado para gravar o conteúdo do arquivo10 em uma variável para impressão
    dados = json.loads(texto)# usando o método "loads = carregar". Aqui esta "carregando\convertendo" o conteúdo da variável texto na variável dados.
print(f'Se tentar imprimir o conteúdo da variável arquivo10 sem converte para variável python da o sequinte erro: {arquivo10}')
print()
print(dados)
print(dados['nome'])

titulo('Estraçã de arquivo da WEB')# imprimindo dados diretamente da WEB

response = urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
dados = json.loads(response)[0]
print(dados)
print()
print('titulo: ', dados['title'] )
print('URL: ', dados['url'])
print('Duração: ', dados['duration'],'min')
print('Número de Visualizações: ', dados['stats_number_of_plays'])
print('\n')
lento('Segundo exemplo de extração de dados da WEB')

respons = urlopen('https://compras.dados.gov.br/licitacoes/doc/licitacao/02000105001802012.json').read().decode('utf8')
dados = json.loads(respons)
print(dados)
print('modalidade: ', dados['modalidade'])
print('situacao_aviso: ', dados['situacao_aviso'])
sleep(5)# É o tempo para verificar se o código/resultado deu certo

#Exemplo de extração de dados

arquivo_fonte = 'Cap06/arquivos/pro.json'
arquivo_destino = 'Cap06/arquivos/dados1.txt'
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfiles:
        outfiles.write(text)
with open('Cap06/arquivos/dados1.txt', 'r') as arquivo1:
    texto = arquivo1.read()
    dados = json.loads(texto)
print('\nDados impresso da planilha dados1.txt')
print('modalidade: ', dados['modalidade'])
print('situacao_aviso: ', dados['situacao_aviso'])

titulo('Copiando conteúdo de um arquivo para outro.')

arquivo_fonte = 'Cap06/arquivos/dados.json'
arquivo_destino = 'Cap06/arquivos/dados.txt'
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)
with open('Cap06/arquivos/dados.txt', 'r') as arquivo11:#Essas linhas de código é para a leitura e impressão dos dados
    texto = arquivo11.read()
    dados = json.loads(texto)
print(f'Esses dados é impresso com a estrutura dos código convencional.\n{dados}\n')

open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())
with open('Cap06/arquivos/dados.txt', 'r') as arquivo12:#Essas linhas de código é para a leitura e impressão dos dados
    texto = arquivo12.read()
    dados = json.loads(texto)
print(f'Esses dados são impresso com os código simplificado . O resultado é:\n{dados}\n')

titulo('Pacotes e Módulos em Puthon')

lento('Em Python, um módulo é um arquivo (script) que contém códico Python e pode ser importado em outros arquivos Python. Ele é usado para compartilhar funções, classes e variáveis entre arquivos.\nJá um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. Ele permite a divisão de um aplicativo em múltiplos modulos, o que facilita a manutenção e o desenvolvimento.\nVisite o PyPi, repositório de pacotes da linguagem Python: https://pypi.org/')

dados = (dir(numpy))
lento('Agora será impresso todos os métodos e atributos do pacote numpy.\nAlguns são modulos outros não, depende da organização do pacote')
#for valor in dados:
    #print(valor)
    
print()
print(f'O resultado da raiz quadrade de 25 é: {numpy.sqrt(25)}')
print()
print(dir(numpy))# Esse comando imprime na tela todo o conteudo do pacote, todos os métodos e atributos.


lento('Um outro pacote muito usado é o pacote RANDOM.\nCom ele consegue fazer a randomização de números e string.\n Segue exemplos abaixo.')
random_str = random.choice(['Abacaxi','Banana', 'Laranja'])# Choice, é escolher em Ingles.
print(f'Usando o pacote random com a função choice, consegui de forma "aleatória" o resuldato de uma lista {random_str}')
print()
random_num = random.sample(range(100),10)# Sample, é amostra em Ingles.
print(f'Usando o pacote random com a função sample, consegui de forma "aleatória" o resultado de uma lista{random_num}')
print()
lento('Um outro exmplo de pacote é: statistics')
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados)) #É um método de calcula a média
print(statistics.median(dados)) # É um método que calcula a mediana

lento('Com o pacote os(sistema operacional) pode trazer o local aonde o programa ta sendo executado.\nExemplo a baixo.')
local_os = os.getcwd()
print(local_os)
print()

lento('Podemos trabalhar com módulos dos pacotes(quando disponível).\nSegue exemplo:')
lento('Com o pacote import urllib.resquet. Onde urllib é o pacote e request é o módulo (import urllib.request).\nEntão junto com o pacote e o modulo pode ser chamado depois a função urlopen()')
resposta = urllib.request.urlopen('http://python.org')
print(f'{resposta}\nEssas informações é um objeto do tipo http, expecificamente http da parte do cliente. Com essa informação podemos fazer a  extração do código HTML.\nPara fazer isso é só ler com read() a variável e imprimir com print().html = resposta.read()\nprint(html)')
html = resposta.read()
#print(html)

#Capitulo 6 funções Built-in em Python

titulo('Exemplo de função = função built-in python')
print('Função MAP')
lento('A função map() em Python é uma função que aplica uma determinada função a cada elemento de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável). A função map() retorna um objeto que pode ser convertido em outra estrutura de dados, como uma lista, se necessário.')

numeros = [1, 2, 3, 4, 5]
def potencia1(x):
    return x ** 2

numeros_ao_quadrado = list(map(potencia1, numeros))
print(numeros_ao_quadrado)

titulo('Exemplo 2 - Como usar a função map()')

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit.
# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius.

# Função 1.
def fahrenheit(t):
    return ((float(9)/5) * t + 32)

def celsius(t):
    return (float(5)/9) * (t-32)

temperaturas = [0, 22.5, 40, 100]

lento(f'Quando se manda imprimir o conteúdo da função map() sem converter para uma lista, tupla e assim por diante ela traz ({(map(fahrenheit, temperaturas))}) esse tipo de informação')
lento(f'Para que sejá possivel manipular esse objeto bastra converte-lo.\n{list((map(fahrenheit, temperaturas)))} ')


lento(f'Quando se manda imprimir o conteúdo da função map() sem converter para uma lista, tupla e assim por diante ela traz ({(map(celsius, temperaturas))}) esse tipo de informação')
lento(f'Para que sejá possivel manipular esse objeto bastra converte-lo.\n{list((map(celsius, temperaturas)))} ')

lento('Importante:\nEm Python 3, a função map() retorna um interator (retornaum objeto pelo qual podemos navegar)')

lento('Para deixar "bonito" ou criar uma iteração pode ser feito pelo loop for. Conforme o exemplo abaixo')
print('Usando o for para ter iteração. temperatura em fahrenheit')
for temp in map(fahrenheit, temperaturas):
    print(temp)
print('Usando o for para ter iteração. temperatura em celsius')
for temp in map(celsius, temperaturas):
    print(f'{temp:.2f}') # Foi usado formatação para reduzir a quantidade de casa decimais

lento('Agora sejá usado a função lambda para fazer a mesma coisa.')
titulo('Temperatura em CeLsius: ')
map(lambda t: (5.0/9)* (t - 32), temperaturas)
print(list(map(lambda t: ((float(9)/5) * t + 32), temperaturas)))
titulo('Temperatura em fahrenheit: ')
map(lambda t: (float(5)/9) * (t-32), temperaturas)
#print(list(map(lambda t: (float(5)/9) * (t-32), temperaturas))) # Primeira opção, sem formatação de casas decimais.
lista =list(map(lambda t: (float(5)/9) * (t-32), temperaturas)) # Só para mostrar com formatação de duas casas decimais
for temp in lista:
    print(f'{temp:.2f}')
print()

titulo('Exemplo de soma de listas')
lento('Aqui esta fazendo uma soma entre os valores da lista a e lista b.')
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(list(map(lambda x, y: x + y, a, b)))
print(list(map(lambda x, y: x + y, a, b)))

titulo('Função reduce()')

lento('A função reduce() em Python é uma função da biblioteca que aplica uma determinada função binária a pares consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tula ou outro objeto iterável), reduzindo-a um único valor.')

lista = [47, 11, 42, 13]
def soma3(a, b):
    x = a + b
    return x
lento('Com a função reducce () consegui facilmente reduzir o tamanho do código.\nNa vez de fazer um código que tenha que "somar" cada número de uma lista, pode ser usado a função reduce() e diminuir o tamanho do código')
print(reduce(soma3, lista))
print()
lento('Também da para fazer o mesmo dentro da expressão lambda.\nNão é nescessario criar uma função para cada tarefa, se esse for o caso pode se usar a expressão lambda onte')
print(reduce(lambda x, y: x + y, lista))
lento('Com essa proxima expressão conseguimos encontrar o maior valor e o menor valor')
max_find2 = lambda a,b: a if (a > b) else b
min_find2 = lambda a,b: a if (a < b) else b

print(f'Aqui temos o maior valor usando a expressão lambda: {reduce(max_find2, lista)} da seguinte lista {lista}')
print(f'Aqui temos o menor valor usando a expressão lambda: {reduce(min_find2, lista)} da seguinte lista {lista}')

# Usando a Função filter()
titulo('Usando a Função built-in - filter()')
lento('A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável (como listas, tuplas ou outro objeto iterável) com base em uma determinada condição. a função filter() retorna um objeto filtro que pode ser convertido em outra estrutura de dados, como lista, se necessário.')

def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(f'O número 35 é par? {verifica_par(35)}')
print(f'O número 10 é par? {verifica_par(10)}')
print()
lista4 = [0, 1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
print(f'retornou um objeto iterável{filter(verifica_par, lista4)}')# retornou um objeto iterável
print(list(filter(verifica_par, lista4)))# converterdo para uma lista conseguimos visualizar o resultado.
print()
lento('Agora podemos fazer de forma mais "simples" usando a função lambda, dessa forma não precisa criar uma função.')
print(f'Esso é o retorno de um objeto iterável. {filter(lambda x: x % 2 == 0, lista4)}')
print(f'Converterdo para uma lista, conseguimos visualizar o resultado.{list(filter(lambda x : x % 2 == 0, lista4))}')
print()
lento('Também podemos imprimeir de determinado valor, desde que o código esteja correto.')
print(f'Novamente objeto iterával: {filter(lambda x : x % 2 == 0 and x > 8, lista4)}')
print(f'Novamente valor do objeto: {list(filter(lambda x : x % 2 == 0 and x > 8, lista4))}')
print()


#Função zip()
titulo('Usando função zip()')
lento('A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como lista, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.')

x = [1, 2, 3]
y = [4, 5, 6]
lento(f'Exemplo de como usar a função zip()\nx = [1, 2, 3]\ny = [4, 5, 6] o resultado normalmente é um objeto iterável: {zip(x, y)}')
lento(f'Mas convertendo para uma lista, podemos ter o resultado: {list(zip(x, y))}')
print()
titulo('Para unir as estruturas podemos usar a função zip() mas tem suas limitações.\n os valores/"conteúdo" tem que ter a mesma quantidade.')
print('Ex:')
print(list(zip('ABCD', 'YX')))
lento('A lista original código original é list(zip("ABCD","YX")), como uma das listas é menor a função zip() só consegui ir até aonde tem informação.')
lento('Isso também acontece com números ou qualquer outros "dados/valores/conteúdo".\n Ex')
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]
lento('As listas originais são:\na = [1, 2, 3]\nb = [4, 5, 6, 7, 8]')
print(list(zip(a, b)))
lento('Os valores da nova lista não estão completos porque falta dados')
titulo('O mesmo acontece com qualquer objeto iterável feito pela função zip(), por exemplo dicionarios em Python')
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
print(list(zip(d1, d2)))
lento('Por padrão a função zip "combina" as chaves dos valores.\nPara alterar isso para os valores tem que chamar o método values de pelos menos de um dos funcionarios.\n Ex:\nprint(list(zip(d1, d2.values())))')
print(list(zip(d1, d2.values())))
titulo('Também da para fazer a mesma coisa usando um loop')
def trova_valores(d1, d2):
    dict_temporario = {}
    for d1key, d2values in zip(d1, d2.values()):
        dict_temporario[d1key] = d2values
    return dict_temporario
print(trova_valores(d1, d2))

#Enumerete
titulo('Capítulo 6 - Funão enumerete()')
lento('A função enumerete() em Python é uma função que permite iterar sobre uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de cada elemento.')
lento('Abaixo está a "sequencia" lista de caracter desse exemplo.')
seq = ['a', 'b', 'c']
lento('Como é um objeto itereitor (O Iteraror é um padrão de projeto comportamental que permite a passagem sequencial através de uma estrutura de dados complexa sem expor seus detalhes internos.)')
print(enumerate(seq))
lento('Para conseguir visualidar o conteúdo do iterator é só converter para uma lista.')
print(list(enumerate(seq)))
lento('Nesse exemplo a cima, foi realisada a numeração com indice e valor')
titulo('Exemplo 2')
for indice, valor in enumerate(seq):
    print(indice, valor)
print('Nesse exenplo mostra o indice com o seu valor.\nEm python toda lista tem o indice e o seu valor, com a função enumerete() consegui visualizar os dois.')
seq2 = ['a', 'b', 'c', 'd', 'e']
for indice, valor in enumerate(seq2):
    if indice > 3 :
        break
    else:
        print(valor, end=' ')
print()
print(f'A lista completa é {seq2}')
titulo('Exemplo 3')
lista = ['Marketing', 'Tecnologia', 'Business']
for i, item in enumerate(lista):
    print(f'No indice {i}, esse é o item/valor do indice {item}')
titulo('Exemplo 4 (str)')
lento('No próximo exemple sera usado uma string, separando cada letra em um indice.')
lento('Primeiro exemplo é atribuido uma lista uma frase que (conjunto de caracter).\n Nesse exemplo não é separado por letra porquê a frase esta em uma lista')
teste = ['Data Science Academy']
for i, item in enumerate(teste):
    print(i, item)
lento('Nesse exemplo já podemos vamor usar uma array invez de uma lista')
teste1 = 'Data Science Academy'
for i, item in enumerate(teste1):
    print(i, item)
lento('Nesse exemplo vamos ver a frase direto/dentro na função enumerate() sem a variável.')
for i, item in enumerate('Data Science Academy'):
    print(i, item)
print()
titulo('exemplo 4')
lento('Também da para usar o enumerete() um range()')
for i, valor in enumerate(range(5, 10)):
    print(f'indice {i}, valor {valor}')
print()
lento('Também pode fazer passando sómente o valor final do range()')
for i, valor in enumerate(range(5)):
    print(f'indice {i}, valor{valor}')

titulo('Erros fazem partes do dia-dia!!!!')

titulo('Erros e Exceções')
lento('Sempre leia as mensagens de erro. Erros fazem parte do processo de aprendizagem e vão na sua jornada em programação, em qualquer linguagem.')

lento('Para usar o tratamento de erro em Python, usamos as palavras reservadas = Try, Except, Finally')

titulo('Exemplo 1')
try:
    total = 8 + '2'
except TypeError:
    print('Operação não permitida. ERRO DE TYPO')

titulo('Exemplo 2: gravando conteúdo em arquivo')
try:
    f = open('Cap06/arquivos/testandoerros.txt', 'w')# Caso o o caminho esteja errado, vai ser acionado o "except".
    f.write('Gravando no arquivo')
except IOError:
    print('Erro: arquivo não encontrado ou não pode ser salvo.')
else:
    print('Conteúdo gravado com sucesso')
    f.close()


titulo('Exemplo 3: Tentando abrir arquivo, porém o "endereço/extenção" esta errado')
try:
    f = open('Cap06/arquivos/testandoerros', 'r')
except IOError:
    print('Erro: arquivo não encontrado ou não pode ser lido.')
else:
    print('Leitura feita com sucesso!')
    f.close()

titulo('Exemplo 4: usando o operador finally')

lento('Exemplo COM erro', 0.2)
try:
    f = open('Cap06/arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo. Teste 2')
except IOError:
    print('ERRO: arquivo não encontrado ou não pode ser salvo')
else:
    print('Conteúdo gravado com sucesso')
    f.close()
finally:
    print('Comando no bloco finally são sempre executados, independente do resultado.')

print()
lento('Exemplo SEM erro', 0.2)
try:
    f = open('Cap06/arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print('ERRO: arquivo não encontrado ou não pode ser salvo')
else:
    print('Conteúdo gravado com sucesso')
    f.close()
finally:
    print('Comandos no bloco finally são sempre executados!')
print()

titulo('Exemplo 6:')
lento('Tentando resolver com tratamento de erro tentativo 1', 0.03)
def askint():
    try:
        val = int(input('Digite um número: '))
    except:
        print('Você não digitou um número')
    finally:
        print('Obrigado')
askint()

titulo('Exemplo 7:')
lento('Tentando resolver com tratamento de erro tentativo 2', 0.03)
def askint2():
    try:
        val = float(input('Digite um número: '))
    except:
        print('Você não digitou um número!')
        val = float(input('Tente novamente. Digite um número: '))
    finally:
        print('Obrigado')
askint2()

titulo('Exemplo 8:')
lento('Tentando resolver com tratamento de erro tentativo 3', 0.03)
def askint3():
    while True:
        try:
            val = float(input('Digite um número: '))
        except:
            print('Você não digitou um número!')
            continue
        else:
            print('Obrigado por digitar um número.')
            break
        finally:
                print(f'O valor digitado foi {val}')
                print('Fim da execução')
askint3()        


# Cap08 - Classes

"""Em Programanção Orientada a Objetos (POO), uma classe é uma estrutura que descreve um objeto, especificando os atributos e compostamentos que os objetos deve ter. Uma classe é uma espécie de modelo que define as características e ações que uma objetos deve possuir.

As classes são usadas para criar objetos, que são instâncias da classes. Cada objeto criado a partir da mesma classe terá os mesmos atributos e comportamentos.

Para criar uma classe em Python, utiliza-se a palabra revervada 'class'.


O nome da classe segue a mesma convenção de nomes para criação de funções e variáveis em Python, mas normalmente se usa a primeira letra maiúscula em cada paralavra no nome de classe

"""

# Criando um classe chamada Livro
class Livro():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__ # metodo construtor
    # (self) é uma referência a cada atrituto da própria classe (e não de uma classe mãi, por exempço)
    def __init__(self):

        #Atributo dão propriedades
        self.titulo = "Sapiens - Uma breve História da Humanidade"
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe")

    # Métodos dão funções que executam ações nos objetos da classe
    def imprime(self):
        print(f"Foi criado o livro {self.titulo} com ISBN {self.isbn}\n")

"""'Em python, a palavra reservada self é uma referência ao objeto atual da classe. quando um objeto é incrivel a partir de uma classe, self é ultilizado para se referir a esse objeto específico.'"""

Livro1 = Livro()
print(Livro1,"\n")
print(type(Livro1),"\n")
print((Livro1.titulo),"\n")
print(Livro1.isbn, "\n")
Livro1.imprime()



# Criando a classe Livro com parâmetros no método construtor.
class Livro():
    def __init__ (self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")

    def imprimr(self, titulo, isbn):
        print(f"Este é o livro { titulo} é o ISBN {isbn}\n")

Livro2 = Livro("O poder do Hábito", 77886611)
print(Livro2.titulo, "\n")
Livro2.imprimr("O poder do Hábito", 77886611)


class Algotirmo():
    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe\n")
print()
algo1 = Algotirmo(tipo_algo="Random Forest")
print(algo1.tipo,"\n")
algo2 = Algotirmo(tipo_algo="Deep Learning")
print(algo2.tipo,"\n")

"""
OBJETOS:
Em Python TUDO é Objeto.
"""
# Criando uma lista.
lst_num = ["Data", "Science", "Academy", "Nota", 10, 10]
# A lista lst_num é um objeto, uma instância da classe lista em Python
print(f"O tipo é: {type(lst_num)}")
print(f"Quantas vezes aparece o elemento 10 na lista, lst_num?\nResponta: {lst_num.count(10)}")

# Usamos o função type, para verificar o tipo de um objeto.
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type("a"))


class Carro(object):
    pass

ferrari = Carro()
print(type(ferrari), "\n")


class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

#Criando um OBJETO chamado Estudante a partir da classe Estudantes.
Estudantes1 = Estudantes("Bob", 12, 9.5)
# Atributo da classe Estudante, ultilizado por cada objeto criado a partir desta classe.
print(f"O nome do estudante é: {Estudantes1.nome}\n")
# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta class.
print(f"A idade do estudante é: {Estudantes1.idade}\n")
# Atributo da ckasse estudante, utiliza por cada objeto criado a partir desta class.
print(f"A nota do estudante é: {Estudantes1.nota}\n")


# Criando uma classe.
class Funcioanarios:
    def __init__ (self, nome, salario, cargo): # O __init__ é chamado Metodo construtor
        self.nome = nome # Isso é Atributo.
        self.salario = salario # Isso é um Atributo.
        self.cargo = cargo # Isso é um Atributo.

    def listFunc(self):
        print(f"Funcionario(a) {self.nome} tem saláro de R$ {self.salario} e o cargo é {self.cargo}.\n")

# Criando um objeto chamado Func1 a partir da classe Funcionario.
Func1 = Funcioanarios("Mary", 2000, "Cientista de dados") # Instancia da classe
# Usando o método e atributos da classe
Func1.listFunc()
print("**** Usanado Atributos ****")
print(f"No objeto Func1 tem o 'atributo haattr' nome?\nResponta: ", end="")
print(hasattr(Func1, 'nome'))
print(f"No objeto Func1 tem o 'atributo haattr' salario?\nResponta: ", end="")
print(hasattr(Func1, 'salario'))
print(f"Mude o sálario de {Func1.salario}, para R$4.500,00")
setattr(Func1,"salario", 4500)# troca realizada com setattr()
print(f"Qual o valor do sálario R$", end="")
print(getattr(Func1, "salario"))# Retornar "mostrar" com getattr
delattr(Func1, "salario")
print(f"Existe o atributo sálario do metodo Funcionarios? ", end="") # Com delattr, foi deletado o atributo salario.
print(hasattr(Func1, "salario")) # mostra de se o atributo existe/tem.
Func1.listFunc() # Da erro porque foi Deletado o atributo "salario"



"""
Os atributos de uma classe são as caracteristicas/propriedades da classe
O que faz a diferençã na programação são os métodos
"""

"""
TRABALANDO COM MÉTODOS DE CLASSES EM PYTHON
Em Python, os métodos de classes funções dentro de uma ckasse, que realizam operaçoes especificas em objetos criados a partir dessa classe. Os médodos de classes são usados para implementar o comportamento dos objetos que pertencem a essa classe.

Assim como as funções em Python, os métodos de classes podem rceber argumentos e retornar valores, No entando, diferente das funções normais, os métodos de classes sempre incluem o parâmetro self com o primeiro argumento, que é usado para se referir ao objeto atual de classe.

O método __init__ é um método especial que é chamado quando um objeto é xriado a partir da classe. Este método é usado para inicializar os atributos dos objetos. Outros métodos podem ser definidos para exercutar tarefas específicas em um objeto,como calcular valores, realizar operações de entrada e saída, ou alterar o estado do objeto.

"""

# Criando uma classe chamada Circulo.
class Circulo():
    # O valor de pi é contante.
    pi = 3.14
    
    # Qunado um objto desta classe for criado, este método será executado e o valor default do raio se 5.
    def __init__(self, raio=5):
        self.raio = raio

    # Esse método calcula a área.
    def area(self):
        return(self.raio * self.raio) * Circulo.pi
    
    # Método para gerar um novo raio.
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo.
    def getRaio(self):
        return self.raio
    
# Criando o objeto circ, uma instância da classe Circulo()
circ = Circulo() # Aqui foi criado o OBJETO circ, sem a inclução de parametros.
# Executando um método da classe Circulo.
print(f"O valor do raio é {circ.getRaio()}, então o valor da área é {circ.area()}\n") # O método getRaio é usado para retormar/imprimir o resultado. 
circ1 = Circulo(7) # Criado um novo OBJETO sendo da classe Circulo, só que dessa vez inviando o parametro.
# Executando um método da classe Círculo.
print(f"O novo valor passado como parametro é {circ1.raio}, então o valor da área é {circ1.area()}\n")
# Passar um novo valor para o atributo raio da classe Circulo.
circ.setRaio(3)
# Imprimir um novo valor para o raio.
print(f"O novo valor passado como parametro para o raio é de {circ.getRaio()}, então o novo valor da área é {circ.area()} \n")


""" Herança de classes em Python"""

"""
TRABALANDO COM HERANÇA DE CLASSES EM PYTHON

Em Programação Orientada a Objetos (POO), a herança é um coneito que permite criar novas classes a partir de outra classes existentes, aproveitando os atributos e métodos da classe original e adicionando novos atributos e médosos específicos.

A classe original é chamada de classes mão ou superclasse e a nova classe criada é chamada de classe filha ou subclasse.

A herança é uma técnica importante e POO porque permite reutilizar o código de maneira eficiente. Em vez de criar uma nova classe do zero, a subclasse pode herdar todos os atributos e métodos da superclasse e adicionar apenas o que é necessário. Dessa forma, a subclasse pode ser concentrar em fornecer funcionalidades adicionais sem precisar se preocupar com as características básicas da classe.

Ha nerança, uma subclasse pode herdar os artributos e métodos de superclasse e substituí-los os estendê-los conforme necessário. Por exemplo, uma subclasse pode ter um método com o mesmo nome de uma método da super classe, mas com um comportamemto diferente.

"""

# Criando a classe Animal - Super-Classe.
class Animal: # NÃO É OBRIGATORIO O USO DE PARENTESES EM CLASSES se não tem parametro.
    # Iniciando com o Método construtor.
    def __init__(self):
        print("Animal Criado.", end=" ")
    
    # Criando o método de impressão.
    def imprimir(self):
        print("Este é um animal.\n")
    
    # Criando o método para informar o hora de comer.
    def comer(self):
        print("Hora de comer.\n")

    # Criando método para emitir som, mas ainda não esta configurado. Por isso será passado o pass como parámetro.
    def emitir_son(self):
        pass

# Criando duas sub-classes.
    # A Primeira sub-classe é Cachorro.
class Cachorro(Animal):
    # Inicia com o método construtor __init__.
    def __init__(self): # A sub-classe também necessita do método construtor.
        Animal.__init__(self) # Além do método construtor da sub-classe atual, também tem que inicializar o método construtor da classe mãe. Isso é feito assim Animal.__init__(self). "Animal" o nome da super classe, chama o método construtor "__init__(self)"
        print("Objeto Cachorro criado.\n")
    # O método emitir som, com o print("Au au!") esta na sub-classe de proprosito, porque o som é para cada tipo de animal especifico.
    def emitir_som(self):
        print("Au au!\n")

    # A Segunda sub-classe é Cato.

class Gato(Animal):
    # Iniciando o método construtor com __init__.
    def __init__(self): # A sub-classe também necessita do método construtor.
        Animal.__init__(self) # Além do método construtor da sub-classe atual, também tem que inicializar o método construtor da classe mãe. Isso é feito assim Animal.__init__(self). "Animal" o nome da super classe, chama o método construtor "__init__(self)"
        print("Objeto Gato Criado\n")
    # O método emitir som, com o print("Miau!") esta na sub-classe de proprosito, porque o som é para cada tipo de animal especifico.
    def emitir_son(self):
        print("Miau!\n")

# Criando o OBJETO rex, para trazer as caracteristicas/atributos da sub-classe Cachorro.
rex = Cachorro() # Criando a Instância da classe
# Criando o OBJETO zeze, para trazer as caracteristicas/atributos da sub-classe Gato.
zeze = Gato() # Criando a Instância da classe.

# Chamar o método emitir som, apartir do objeto rex.
print("O cachorro faz.", end=" ")
rex.emitir_som() # Se tiver métodos com os mesmos nomes nos métodos mãe e filha. A que fica valendo é a da filha sempre. Porque ele sub-escreve o da super-classe. Isso ajuda muito na forma que quer manipular/estuturar o programa.

# Chamar o método emitir som, apartir do objeto zeze.
print("O Gato faz.", end=" ")
zeze.emitir_son()
# Esse método é chamado para que os Animais comer
# Executando o método da classe Canhoro(sub-classe) do canhoro.
print(f"O resultado da impressão do médoto imprimir do médoto Cachorro é. ", end="" )
rex.comer()

# Executando o método da classe Gato(sub-classe) do canhoro.
print(f"O resultado da impressão do médoto imprimir do método Gato é. ", end="" )
zeze.comer()




"""TRABALHANDO COM POLIMORFISMO DE CLASSES EM PYTHON"""

"""
Polimorfismo é um dos conceitos fundamentais da Programação Orientada a Objeos(POO). O polimorfismo permite que objetos de diferentes classes possam ser tratados de forma uniforme. Isso significa que um objeto pode ser tratado como se fosse um objeto de uma superclasse, mesmo que ela seja de uma sub-classe.

Mais especificamente, o polimorfismo se refere à habilidade de um objeto responder de diferentes formas a uma mesma mensagem. Isso é possível porque as subclasses podem implementar métodos com o mesmo nome que os métodos da superclasse, mas com comportamentos deferentes.

"""
# Criando Super-classe.
class Veiculo:
    # Criando o método construtor com mais 2 parametros/argumentos.
    def __init__(self, marca, modelo):
        self.marca = marca # Criação do atributo, marca do veiculo
        self.modelo = modelo # Criação do atributo, modelo do veiculo.

    def acelerar(self):# Criação do método, sem atributo (podendo ser editado no futuro)
        pass

    def frear(self):# Criação do método, sem atributo (podendo ser editado no futuro)
        pass

# Criação das sub-classes
    # Criação da Primeira sup-classe. Carro
class Carro1(Veiculo): # sub-classe Carro endando as caracteristicas/atributos da super-classe Veiculo.
    def acelerar(self):
        print("O carro esta acelerando.")

    def frear(self):
        print("O carro esta freando")

    # Criação da segunda sup-classe. Moto
class Moto(Veiculo): # sub-classe Carro endando as caracteristicas/atributos da super-classe Veiculo.
    def acelerar(self):
        print("A moto esta acelerando.")

    def frear(self):
        print("A moto esta freando")


    # Criação da Terceira sup-classe. Avião
class Aviao(Veiculo): # sub-classe Carro endando as caracteristicas/atributos da super-classe Veiculo.
    def acelerar(self):
        print("O avião esta acelerando.")

    def frear(self):
        print("O avião esta freando.")

    def decolar(self):
        print("O avião esta decolando.")


# Criando os objetos, nesse exemplo é uma lista.
lista_veiculos = [Carro1("Porsche", "911 Turbo"), 
                  Moto("Honda", "CB 1000R Black Edition"), 
                  Aviao("Boeing", "757")] # Isso é uma lista de instâncias de classes, uma lista de objetos.
# Criando um loop, para percorrete a lista_veivulos.
for item in lista_veiculos:
    # O método acelerar tem comportamento diferente dependendo do tipo de objeto.
    item.acelerar()

    # O médodo frear tem comportamento diferente dependendo do tipo de objeto.
    item.frear()

    # Executamos o método decolar somente se o obleto for instância da classe Avião.
    if isinstance(item, Aviao):# Função interna Python, faz uma comparação para saber se o tipo é igual. A função interna é isinstance()
        item.decolar()

    print("---")
    print("\n")

    # Capítulo 9. 

#Pacote Python - MAIS USADO
#Introdução a NumPy (Numerial Python) numpy.org

filename = os.path.join('dataset.csv') # Não funciona no VScode, só no Jupyter notebook
print(f"Versão do software {dsa.__version__}")

# criando um Array numpy a partir de ua lista python
arrl = dsa.array([10,21,32,43,48,15,76,57,89,5])
print("Imprimindo a variável arrl, que é a array.")
print(arrl)
# Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho.
print(f"Mostrando o tipo: {type(arrl)}")
print(f"O resultado do tipo. significa: {type(arrl)}\nnumpy = é de numpy mesmo,\nndarray = número de dimenções do array")
# Com o shape consegue veriaficar o formado do array.
print(f"Veridicando o formato da array com shape.\nO resultado é {arrl.shape}. Esse resultado acontece porque tem {arrl.shape[-1]} elementos em uma unica dimenção.\nTambém conhecido como vetor, 'Uma lista de elementos'.")
print(f"Esse vetor/array {arrl.shape} significa que so tem uma dimenção, ou sejá uma linha.")
print(f"Também existe o array de uma ou mais linhas com uma ou mais colunas.\n(2,3) = 2 linha e 3 colunas.\n(4,3,2) = 4 linhas, 3 colunas, 2 profundidade.\n")

print("Um array, NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grande homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros. Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem vários otimizações de dessempenho. Além disso, NumPy permite a fácil leitura e escrita e arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.\n")

# Indezação em arrays Numpy
print(f"Imprimindo a array/vetor: {arrl} e a dimenção: {arrl.shape}")
print(f"Imprimindo um elemento especifico da array. É usado o sistema de indexação de lista")
print(f"Buscando por índice número 4, o resultado é: {arrl[4]}")
print(f"Buscando por indexação, ex: índice 1 até o 4. Resultado {arrl[1:4]}. #LEMBRANDO o ultimo número do índice significa que ele é exclusivo, não aparecera o resultado ele só do anterior. Para ter o ultimo valor é só escolher o índice a frente  ou mais {arrl[1:5]} ")
print(f"Buscando por indexação, ex: índice 1 até o 4. Resultado {arrl[1:4]}. #LEMBRANDO o ultimo número do índice significa que ele é exclusivo, não aparecera o resultado ele só do anterior. Para ter o ultimo valor é só escolher o índice a frente arrl[1:5] {arrl[1:5]} ou mais arrl[1:4+1] {arrl[1:4+1]}\n")
print(f"Usando lista python como índices númericos do Numpy")
indices = [1, 2, 5, 6]
print(f"Print da lista de índices {indices}")
print(f"Valores impressos usando a lista indices como índices da array, o resultado: {arrl[indices]}")
# Criando máscaras booleanas para os elementos pares. Nome bunito para criar a especie de padrão.
print(f"Criando uma máscara booleana")
mask = (arrl % 2 == 0)
print(f"Imprimindo a máscara (mask) ")
print(f"{mask}\nO resultado é um valor Booleano, com esse 'valor' posso usar para imprimir os valores pares da máscara.")
print(f"Resultado = {arrl[mask]}")
mask=(arrl % 2 == 1)
print(f"Também da para usar o exemplo para o impares e para muitas outras aplicações.\n{mask}\nResultado = {arrl[mask]}")
# Também é possivel alterar o valor de uma array/vetor
print("Alterando um elemento do array")
print(f"Pode ser feito simplesmente como é feito em uma lista. 'arrl[0] = 100', o valor do índice 0 altera para 100")
print(f"Veja o resultado antes e depois\n{arrl}")
arrl[0] = 100
print(arrl)
print()
#Não é permitido incluir elementos de outro tipo.
print(f"No mesmo array Numpy não é permitido usar mais de um tipo de elemento.")
print(f"O array que estamos usando 'arrl' é do tipo númerico isso significa que não da para usar string ou qualquer outro tipo nele")
print(
    """
        Se entar fazer a seguinte operação, da erro

                try:
                arrl[0] = "Novo elemento"
            except:
                print("Operação não permitida!")
""")
try:
    arrl[0] = "Novo elemento"
except:
    print("Operação não permitida!")

#Trabalhando com Funções NumPy - Parte 1 de 2.
print("FUNÇÕES NUMPY")
print(f"A função array() no Numpy.")
arr2 = dsa.array([1, 2, 3, 4, 5])
print(f"A array foi definida o nome da variável é arr2.")
print(f"Confirmando o valor da arr2.\n{arr2}")
print(f"Para saber os métoros e etributos disponíveis em objetos NumPy, é só por um . depois da variável/arry/objeto NumPy.\n   Ex:\n       arr2.AQUI VAI APARECER OS MÉTODOS DISPONIVEIS\n")
print(f"Mostrando qual o tipo de objeto é a variável arr2: {type(arr2)}")
print(f"Os detalhes mostra que é da biblíoteca NumPy, ND numeras dimenções, ARRAY é um vetor")
print(f"Outros métodos do objeto não, cumsun() cumprod()")
print(f"Com o cumpun() 'soma acumulada'{arr2.cumsum()}, soma o primeiro valor com o segundo, com o resultado soma com o proximo valor, assim até o fim.\n")
print(f"Com o comprod() 'produto acumulado' {arr2.cumprod()}, multiplica o primeiro valor com o segundo, com o resultado multiplica com o próximo valor, assim até o fim.")
print(f"Para saber quais o métodos e atributos para o NumPy basta por o . depois do 'apelido' que foi dado ao NumPy lá no começo.")
print("dsa'.'")#tirar as aspas
print(f"Esse é o objeto numpy que esta nessa maquina:\n{dsa}")
print("\n")
#Função arange
print(f"A função arange cria um array NymPy cintendo uma pregressão aritmética a partir de um intervalo - star, stop, step. Vamos para o teste...")
arr3 = dsa.arange(0,50,5)
print(arr3)
print(f"Em Python puro tem o range tem como objetivo criar uma lista de valores, mas no caso o arange é para criar essa lista de valores para o NumPy.")
print(f"Qual o tipo de objeto é a arr3?\nVamos ver: {type(arr3)}.\nIsso mostra que pode ser criado array mais de uma forma, da forma tradicional pondo depois do dsa.array os valores ou usando uma arange para criar o valores, 'dsa.range(0,50,5)'.")
print(f"Imprimindo o formato/shape arr3: {dsa.shape(arr3)}. Mostra número de elementos e quantidade de dimenção. ATENÇÃO. O shape() é uma função do NumPy")
print(f"Mostrando o tipo de dado na array arr3: {arr3.dtype}. ATENÇÃO. dtype é um atribúto.")
#Trabalhando com Funções NumPy - Parte 2 de 2.
#Usando a função zeros()
print(f"Vamos criar um array preenchido com zeros. Fazermos isso usando o método zeros().")
arr4 = dsa.zeros(10)
print(f"Imprimindo o array arr4: {arr4}")
print(f"Criando uma matriz diagonal. Exemplo de aplicação da função zeros() e outras.")
print("Para criar uma matriz diagonal é usado uma array e o módulo olho'eye'. 'arr5 = dsaéye(3)")
arr5 = dsa.eye(3)
print(f"Fica assim a matriz.\n{arr5}")
print("A matriz diagonal é usada largamente na ciência de dados. Tem muitoas propriedades")
print(f"Vamos criar uma matriz diagonal passando os valores como parametros.")
arr6 = dsa.diag(dsa.array([1, 2, 3, 4,]))
print("O resultado da criação da seguinte array = arr6 = dsa.diag(dsa.array(1,2,3,4,))")
print(arr6)
print(f"Criando um array com valores booleanos,\n O nome da nova array é arr7, criada da seguinte forma: arr7 = dsa.array([True, False, True, False])")
arr7 = dsa.array([True, False, True, False])
print(f"Resultado da criação do array arr7: {arr7}\n")
print("Também da para criar um array de strings. Lembrando do o array só pode ser um unico tipo.")
arr8 = dsa.array(["Linguagem Python", "Linguagem R", "Linguagem Julia"])
print(f"O resuldado da criação da array arr8 é : {arr8}")
# Duas novas funções linspace() e logspace()
print("A função linspace() do NumPy é usada para criar sequência de números igualmente esaçados dentro de um intervalo especifico. Essa função é amplamente utilizada em programação científica e matemática para gerar array de números para diversos fins, como gráficos, cáculos e simulações.\n\nO método linspace(linearly spaced vector) retorna um número de valores igualmente distribuídos no intervalo especifico")
print("Imprimindo o resuldato da linspace(0,10):")
print(dsa.linspace(0,10))
print()
print("Imprimindo o resuldado da linspace(0, 10, 15): ")
print(dsa.linspace(0, 10, 15))
print()
print("Fução logspace() no NumPy é usda para criar uma sequência de números igualmente espacados em escala logarítmica dentro de um intervalo especifico. Essa função é amplamente ultilizada em programação científica e matemática para gerar arrays de números para diversos fins, como gráficos, cálculos e simulações.")
print(dsa.logspace(0, 5, 10))
# Manipulação de matrizes NumPy - Parte 1 de 2
print("Criando uma Matriz, Isso simplesmente é uma lista de listas (isso é conhecido como lista aninhada)")
arr9 = dsa.array([[1, 2, 3,],[4, 5, 6,]])
print(f"Mostar que é uma ndarray: um array da bíblioteca NumPy. {type(arr9)}")
print(f"Imprimindo a MATRIZ:\n{arr9}")
print(f"Com o .shape, mostra qual a dimenção dessa matriz: {arr9.shape}, Duas linhas e Três colunas.")
print(f"Criando uma matriz de ((2, 3)) apenas com número 1. è criada usando o método .ones().")
arr10 = dsa.ones((2,3,))
print(f"Fica assim:\n{arr10}")
lista = [[13, 18, 22,], [0, 34, 59,], [21, 48, 94,]]
arr11 = dsa.matrix(lista)
print(f"Agora vamos criar uma matriz tendo como párametro uma lista de listas.\nO comando é .matrix(). Então para fazer isso tem que usar o NumPy e o método tendo como párametro a lista.\narr11 = dsa.matrix(lista) o resultado é:\n {arr11}")
print(f"Como de costume verificar o tipo: {type(arr11)}, interessante notar que é uma matriz agora.")
print(f"Usando o método .shape(), podemos descobrir o formato dessa matriz.\nO formato é: {dsa.shape(arr11)}. O arr11 é uma matriz de duas dimenções, 3 linhas e 3 colunas.")
print(f"O tipo de dado {arr11.dtype}")
print(f"Usando um outro atribudo ddo abjeto aar11.\nEsse atributo é o .size.\nO resultado é: {arr11.size}. Size é tamanho em inglês, então isso significa que o tamanho dessa matriz é {arr11.size}")
print("INDEXAÇÃO COM DUAS DIMENÇÕES da Matriz.")
print(f"O que muda?\nÉ que agora consegue preencher o número do índice para cada dimenção:\nEx. {arr11[2,1]}. Esse valor significa que retornou o valor da linha 2, da coluna 1")
print(f"Fazendo o mesmo exemplo só que agora com um range de de linhas arr11[0:2,2].\nO resultado é:\n {arr11[0:2,2]}.\nÉ esse resultado porque limita as linhas do índice 0 e 1, e busca a coluna do índice 2 que é a coluna 2.")
print(f"Terceiro exemplo de indexação de matriz.\nCom esse tipo de fatiamento aee11[1,] é retornado todas as colunas do índice da linha 1.\nResultado: {arr11[1,]}")
print("Para fazer alteração de um elemento de uma matriz é só usar o mesmo sistema que faz com lista.")
print(f"Pode ser feito dessa forma arr11[1,0] = 100.\nAntes.\n{arr11} ")
arr11[1,0] = 100
print(f"Depois.\n{arr11}\n")
print(f"Tem como FORÇAR o tipo de dado que o arry.\nPor exemplo:\nx = dsa.array([1, 2]) # Dessa forma é deixar o proprio interpretador do numpy decidir qual é o tipo de dado.\nOutro exemplo:\ny = dsa.array([1.0, 2.0]) # Novamente o NumPy esta escolhendo o tipo de dado.\nAgora vamos ver como FORÇAR o tipo de dado, é só indicar qual o tipo de dado quer.\nExmplo:\nx = dsa.array([1, 2], dtype = dsa.float64) # Dessa forma esta forçando ser float mesmo que o tipo deja int.")
x = dsa.array([1, 2])
y = dsa.array([1.0, 2.0])
z = dsa.array([1, 2], dtype = dsa.float64)
print(f"Resultado de y: {x.dtype}\nResultado de y: {y.dtype}\nResultado de z: {z.dtype}")
print(f"Criando uma nova lista de lista = uma matriz. Com os seguintes dados e array: arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)")
arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)
print(f"O resuldado é uma matriz de dados do tipo float conforme FORÇADO pelo comando dtype.float.\n{arr12}")
print(f"O itemsize de um array numpy é um atributo que retorna o tamanho em bytes de cada elemento em bytes de cada elemento do array. Em outras palavras. o itemsize representa o número de bytes necessários para armazenar cada valor do array numpy.")
print(f"Vamos usar o atributo .itemsize: {arr12.itemsize}, esse número é o tamanho em bytes de cada elemneto arr12.\nPara somar todo os bytes é usado o attibuto .nbytes: {arr12.nbytes}, esse valor total é a quantidade de bytes que essa matriz esta gastando de memória do computador.")
print(f"Agora vamos ver a quantidade de dimenções usando o atributo de número de imenções .ndim. o arr12 tem: {arr12.ndim}\n")
print(f"Manipulando Objetos de 3 e 4 dimensões com NumPy.")

print(f"Criando um array de 3 dimensões.")
arr_3d = dsa.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
facil_visu = """
    arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10 , 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]    
])
"""
print(f"Isso é uma array de 3 dimensões,\narr_3d = dsa.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]).\nPara facilitar a visualisação fica assim.\n{facil_visu}")
print(f"A quantidade de dimenções é novamente chamada com o atributo .ndim.\nEntão o número de dimensões da arr_3d é: {arr_3d.ndim}\n")
print(f"Com o atributo .shape podemos conprovar: {arr_3d.shape}.\n EXPLICAÇÃO: O primeiro eixo tem 2 elementos Dentro de um elemento tem 3 linhas por isso o numero 3 no shape. E para cada linha tem 4 colunas.\n")
print(f"Para filtras as dimenções segue o mesmo principio.\nEx: arr_3d[0, 2, 1] o resultado será 10.\nComprovando usando o código {arr_3d[0, 2, 1]}\n# busca é feita como é em lista por índice.\n")
print(f"Criando um array de 4 dimensões.")
arr_4d = dsa.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],[[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35],[36,37,38,39,40]],[[41,42,43,44,45],[46,47,48,49,50],[51,52,53,54,55],[56,57,58,59,60]]],[[[61,62,63,64,65],[66,67,68,69,70],[71,72,73,74,75],[76,77,78,79,80]],[[81,82,83,84,85],[86,87,88,89,90],[91,92,93,94,95],[96,97,98,99,100]],[[101,102,103,104,105],[106,107,108,109,110],[111,112,113,114,115],[116,117,118,119,120]]]])
facil_visu2 = """arr_4d = dsa.array([
    [
        [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20]
        ],
        [
            [21,22,23,24,25],
            [26,27,28,29,30],
            [31,32,33,34,35],
            [36,37,38,39,40]
        ],
        [
            [41,42,43,44,45],
            [46,47,48,49,50],
            [51,52,53,54,55],
            [56,57,58,59,60]
        ]
    ],
    [
        [
            [61,62,63,64,65],
            [66,67,68,69,70],
            [71,72,73,74,75],
            [76,77,78,79,80]
        ],
        [
            [81,82,83,84,85],
            [86,87,88,89,90],
            [91,92,93,94,95],
            [96,97,98,99,100]
        ],
        [
            [101,102,103,104,105],
            [106,107,108,109,110],
            [111,112,113,114,115],
            [116,117,118,119,120]
        ]
    ]
])
"""
print(f"A visualização de uma matriz de 4 dimensões é assim arr_4d = dsa.array([[[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]],[[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35],[36,37,38,39,40]],[[41,42,43,44,45],[46,47,48,49,50],[51,52,53,54,55],[56,57,58,59,60]]],[[[61,62,63,64,65],[66,67,68,69,70],[71,72,73,74,75],[76,77,78,79,80]],[[81,82,83,84,85],[86,87,88,89,90],[91,92,93,94,95],[96,97,98,99,100]],[[101,102,103,104,105],[106,107,108,109,110],[111,112,113,114,115],[116,117,118,119,120]]]]).\nPara facilitar a visualização:\n{facil_visu2}")
print(f"Novamente com atributo .ndim, para visualizar a quantidade de dimesões: {arr_4d.ndim}")
print(f"Visualizando o shape. {arr_4d.shape}.\nO número 2 é o primeiro eixo da dimensão, isso significa que tem 2 grupos.\nDentro de qualquer um desses grupos tem mais 3 grupos de elementros dentro do shape.\nDentro de qualquer um desses 4 grupos tem a linhas no caso tem 4 linhas e é composta de 5 colunas.")
print("Aplicando uma filtragem do array (arr_4d), usando o fatiamento - arr_4d[0,2,1]")
print(f"O resultado é a linha com os seguintes dados:[46,47,48,49,50]\nComprovando com o código:{arr_4d[0,2,1]}")
print(f"Usando a mesma indexação, trazer as infirmações de uma determinada coluna. arr_4d[0,2,1,4]. O resultado é 50. Comprovando com o código: {arr_4d[0,2,1,4]}.\n")
print("Manipulando arquivos com NumPy.")
print("1º importar a bíblioteca 'os'.\n2º Criar uma variável recebendo os dados da tabela 'dataset.csv', fica assim = filename - os.path.join('dataset.csv').\nPara carregar esse arquivo tem que levar para uma array do NumPy. Assim: arr13 = ")
print()
# Análise Estatistica Básica cm NumPy.
print(f"Explicando análise estatística básica com NumPy")
print(f"Criando uma array.\nPrimeira coisa tem que criar um array NumPy: arr14 = dsa.array([15, 23, 63, 94, 74])")
arr14 = dsa.array([15, 23, 63, 94, 75])
print(f"Em Estatístoca, a média é uma medida de tendência central que representa o valor central de um conjunto de dados. É calculado somente-se todos os valores do conjuto de dados e dividindo-se pelo número de observações")
print("Com a bíblioteca NumPy, é só chamar a função '.maen()' e passar como parametro a variável que contém o vetor arr14 nesse exemplo.\nEntão fica assim: dsa.maen(arr14)")
print(f"Resultado: {dsa.mean(arr14)}\n")
print("O desvio padrão é uma medida estatística de dispensão que indica o quanto os valores de um conjunto de dados se afastam da média. Ele é calculado como a raiz quadrada da variável, que é a média dos quadrados das diferencas entre cada valore e a média.\n\nO desvio padrão é uma medida útil porque permite avaliar a variabilidade dos dados em torno da média. Se os valores estiverem próximos da média, o desvio padrão será baixo, indicando que os dados têm pouco variabilidade. Por outro lado, se os valores estiverem muito distante da média, desvio padrão será alto, indicando que os dados têm alta variabilidade.\n\nO desvio padrão é amplamente ultilizado em Análise e Ciência de Dados, oara avaliar a consistência dos dados e comparar conjuntos de dados diferentes. É importante notar que o desvio padrão pode ser influienciado por valores extremos (outliers) e pode ser afetados por diferentes distribuições de dados.\n")
print(f"Uma forma de usar o desvio padrão de uma média é usar a Bíblioteca NumPy, o metodo .std().\nEx:dsa.std(aar14).\nO resultado é {dsa.std(arr14)}.\nComo o valor decimal ficou grande, da para simplificar usando a formatação, dsa.std(arr14):.2f.\nEntão, fica assim: {dsa.std(arr14):.2f}")
print("O valor mostrado com o método .std(). Mostra que o valor esta bem desperço, não significa que os valores estão errado ou que os dados estão errados, mas mostra que estão distante os valores.\n")
print("VARIÂNCIA... Também é posivel e nescessario fazer outras estatísticas além di desvio padrão, por isso também é usada a variância.")
print("A variância é uma medida estatística que quantifica a dispersão dos valores em um conjunto de dados em relação à média. Ela é calculada com a média dos quadrados das diferenças entre cada valor e a média.\n\nA fórmula para o cálculo da variância é:")
print("""
    var = 1/n*Ʃ(xi - ẍ)^2
      
    Onde:
      . var é a variância.
      . n é o número de observações.
      . Ʃ é o somatório.
      . xi é o i-ésimo valor no conjunto de dados.
      . ẍ é a média dos valores.
    
    A variância é uma medida útil para avaliar a variabilidade dos dados em torno da média. Se a variância for baixa, isso indica que os valores estão próximos da média e têm pouca variabilidade. Por outro lado, se a variância for alta, isso indica que os valores estão distrantes da média e têm alta variabilidade.
""")
print(f"Para aplicar a variância é só usar o método .vat() da Bíblioteca NumPy.\nUm exemplo que podemos ver é dsa.var(arr14), o resultado é: {dsa.var(arr14)}.\nDa mesmo forma, para simplificar o valor basta formatar as casas decimais, então fica assim: {dsa.var(arr14):.2f}.\n")
print("LER O MANUAL EM PDF NO CAPÍTULO 9 SOBRE QUANDO USAR A VARIÂNCIA E DESVIO PADRÃO PARA ANÁLISE DE DADOS.\n")
