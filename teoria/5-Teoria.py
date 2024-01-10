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

def titulo(msg):
    print()
    print(f'--- {msg} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.001)
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
def potencia(x):
    return x ** 2

numeros_ao_quadrado = list(map(potencia, numeros))
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