#Tipos Primitivos em Python.

# Integer (inteiro)
numero_inteiro = 100
print(f"Valor{numero_inteiro}, tipo {type(numero_inteiro)}")

# Floa (Ponto Flutuante)
numero_decimal = 19.99
print(f"Valor {numero_decimal}, Tipo {type(numero_decimal)}")

#String (Texto)
texto = "Python é incrivel!!!"
print(f"Valor {texto}, tipo: {type(texto)}")

#Boolean (Booleano)
verdadeiro = True
falso = False
print(f"valor: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"valor: {falso}, Tipo: {type(falso)}")

# operadores aritméticos.
print("\nOperações com tipos aritméticos:\n")

a = 10
b = 3

# usando os operadores aritméticos.
soma = a + b                    #Adição
subtracao = a - b               #Subtração
multiplicacao = a * b           #Multiplicação
divisao = a / b                 #Divisão (reultado e sempre float/ decimal)
divisao_inteira = a // b        #Divisão Inteira (descarta a parte decimal/ sempre será inteiro)
mudulo = a % b                  #Modulo Resto da divisão
potencia = a ** b               #Potência

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao:.4f}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {mudulo}")
print(f"{a} ** {b} = {potencia}\n")


#Operadores de Comparação
print("Operadores de Comparação:\n")

x = 5
y = 10

#Operador "maior que"
print(f"O simbolo '>' sifgnifica 'maior que' o resultado é Boolean: {x} > {y} = {x > y}")
print(f"O Simbolo '<' siginifica 'menor que' o resultado é Boolean: {x} < {y} = {x < y}")
print(f"O simbolo '==' significa 'igual a' o resultado é Bollean: {x} == {y} = {x == y}")
print(f"O simbolo '!=' significa 'diferente de' o resultado é boolean: {x} != {y} = {x != y}")
print(f"O simbolo '>=' significa 'maior ou igual a' o resultado é Boolean: {x} >= {y} = {x >= y}")
print(f"O simbolo '<=' significa 'menor ou igual a' o resultado é Boolean: {x} <= {y} = {x <= y}")

#Operadores Lógicos
print("\n Operadores Lógicos:\n")
tem_dinheiro = True
tem_tempo = False

print("Operador AND (e): Ambos precisam ser verdadeiros.")
print(f"O cliente pode viajar? {'Pode viajar tem dinheiro ou tempo'if tem_dinheiro and tem_tempo else 'Não pode viajar, não tem dinheiro ou tempo'}")
print("\nO operador OR (ou): Pelo menos um precisa ser verdadeiro")
print(f"O cliente pode viajar? {'Pode viajar tem dinheiro'if tem_dinheiro or tem_tempo else 'Não pode viajar, não tem tempo'}\n")

print("Operador NOT (não): Inverte o valore Bolleano.")
print(f"O cliente pode viajar? {'Pode viajar tem dinheiro'if tem_dinheiro or tem_tempo else 'Não pode viajar, não tem tempo'}")

print(f"O cliente pode viajar? {'Pode viajar tem dinheiro'if tem_dinheiro or not tem_tempo else 'Não pode viajar, não tem tempo'}")

print(f"O cliente pode viajar? {'Pode viajar tem dinheiro'if tem_dinheiro and tem_tempo else 'Não pode viajar, não tem tempo'}")
print(f"O cliente pode viajar? {'Pode viajar tem dinheiro'if tem_dinheiro and not tem_tempo else 'Não pode viajar, não tem tempo'}\n")


# Strings em Python
print("Trabalhando com manupulação de strings em Python:")
frase = " Aprender Python é muito divertido! "
#Concatenando.
nome = "Maria"
saudacao = "olá, " + nome + "! "+"Usando o simbolo aritmético de adição + para concatenar strings"
print(saudacao)
print(f"Olá, {nome}!" + "Usando f-strings para concatenar\n")

print("Para saber o tamanho da frase usar a função len():")
print(f"A frase tem {len(frase)} de caracteres\n")
print(f"Frase original: {frase}\n")
print("Deixar tudo em maiúscolo é usado o método upper():")
print(f"Deixando tudo em maiúsculo: {frase.upper()}\n")
print("Deixar todo em minúsculo é usado o método lower():")
print(f"Deixando tudo em minúscolo: {frase.lower()}")
print("Removendo espaços em branco do início e fim da string é usado o método strip():")
print(f"Removendo espaços em branco: {frase.strip()}, antes com {len(frase)}, agora com {len(frase.strip())} caracteres")
print(f"Usando dois metodos juntos strip() e len: {len(frase.strip())}\n")
nova_frase = ({frase.strip().upper()})
print(nova_frase)
frase_sem_espaco = frase.strip()
print("substituir um pedaço do texto")
print(f"\nSubstituindo uma palavra na string é usado o método replace(): {frase.replace('divertido', 'legal')}")
print(f"Uma informação adicional a string salva na memória não é trocada, a menos que seja atribuída a uma nova variável, como não foi feito isso a string continua original. \n Original - {frase}.\n Trocada - {frase.replace ('divertido', 'legal')}.\nIsso só acontece em tempo de execução.\n")
print("Fatiando a String (Slicing):")
print(frase_sem_espaco)
print(f"O primeiro caracter é: {frase_sem_espaco[0]}")
print(f"O ultimo caracter é {frase_sem_espaco[-1]}")
print(f"A palavra 'python', {frase_sem_espaco[9:15]}\n")

print("Estrutura de dados em Python - Listas")
print("Listas são coleções ordenadas e mutáveis de itens. Que podem conter diferentes tipos de dados")
#Criando uma lista
lista_frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Lista de frutas: {lista_frutas}")
print(type(lista_frutas))
#acessando elementos da lista
print(f"Localizando a primeira fruta da lista: {lista_frutas[0]}")
print(f"Localizando a última fruta da lista: {lista_frutas[-1]}\n")
print(f"Adicionando uma fruta a lista de frutas: Isso é feito com o método append()")
lista_frutas.append("tomate")
print(f"Lista a dualizada: {lista_frutas}\n")
print("Remover uma fruta da lista: Isso é feito com o método remove()")
lista_frutas.remove('laranja')
print(f"Lista atualizada: {lista_frutas}\n")
#Modificando um item da lista
print(f"Para modificar um item da lista, basta acessar o índice e atribuir um novo valor")
lista_frutas[0] = 'Morango'
print(f"lista atualiada depois da troca do primeiro item: {lista_frutas}\n")
print(f"E para deletar uma lista, só usar o método del()")
del lista_frutas
#print(lista_frutas)
print()
print("estrutura de dados em Python - Tuplas")
print("Estrutura de dados em Python - Dicionários")
print("Estrutura de dados em Python - Conjuntos (Sets)")

#TUPLAS
print("\nEstrutura de dados - TUPLAS")
print("Tuplas são coleções ordenadas e imutáveis de itens. Uma vez criada, não podem ser alteradas.")
#Criando uma tupla.
print("Criando uma tupla")
coordenadas = (10.0, 20.5)
print(f"Com o método type() consigo saver qual o tipo do elemento: {type(coordenadas)}")
print(f"Tupla de coordenadas: {coordenadas}\n")
print("Para acessar elementos da tupla, é usado o índice '[]' para acessar esses elementos")
print(f"Coordenada X: {coordenadas [0]}")
print(f"Coordenada Y: {coordenadas [1]}\n")
print("não é possível modificar uma tupla depois de criada, \nSegue exemplo:\n print(coordenadas [0] = 14) : isso gerará um erro.\n")
#print(coordenadas [0] = 14)
print("As tuplas são úteis para dados que não devem ser alterados.")
dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
print(f"O primeiro dia da semana é: {dias_semana[0]}\n")
#DICIONÁRIOS
print("Estrutura de dados - DICIONÁRIOS")
print("Criando uma dicionárop de informações de um aluno:")
aluno = {
    "nome" : "Bob",
    "idade" : 22,
    "curso" : "Data Science Para análise Multivariada",
    "aluno_ativo" : True
}
print(type(aluno))
print(f"Dicionario do aluno: {aluno}")
print(f"Acessando os valores dela chave")
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}\n") # get é uma forma segura de acessar o valor da chave.
print("Agora vamos ver como é feita a adição de um novo par de chave-valore no dicionário:")
aluno["Cidade"] = "São paulo"
print(f"Dicionário com o valor adicionado: {aluno}\n")
print("Agora vamos modificar um valor já existente no dicionário:")
aluno["idade"] = 24
print(f"Dicionário com o valor alterado: {[aluno["idade"]]}\n")
print("Agora vamos remover/deletar um par de chave-valor de um dicionário:")
del aluno["aluno_ativo"]
print(f"Resultado do dicionário após a remoção da chave 'aluno_ativo': {aluno}\n")
print(f"Mostrando a quantidade de itens em um dicionário com a função len(): Tem {len(aluno)} itens nesse dicionário\n")

#Estrutura de dados  - Conjustos (Sets)
print("Estrutura de dados - Conjuntos (Sets)")
print("Conjuntos são coleções não ordenadas de itens únicos. Eles são úteis para remover duplicatas e realixar perações matemáticas de conjutos (união e interseção).")
#Criando um conjunto
print("Vamos criar um conjunto de números:")
numeros = {1,2,3,4,2,3,5}
print(f"Esse é um exemplo de Conjunto/Sets: {numeros}\n")
print(type(numeros))
print(f"Conjunto de números (sem duplicatas): {numeros}\n")
print("agora vamos adicionar um item")
numeros.add(6)
print(f"Após adicionar o valor 6 ao conjunto/sets: {numeros}\n")
print("Agora vamos remover um item")
numeros.remove(2)
print(f"Resultado após remover o valor 2: {numeros}\n")
print("Vamos ver agora operações de conjuntos:")
print("Criando dois conjuntos: conjunto_a = {1,2,3,4} e conjunto_b = {3, 4, 5, 6}")
conjunto_a = {1, 2, 3, 4} 
conjunto_b = {3, 4, 5, 6}
print("Unindo os dois conjuntos (todos os elementos) (uniao = conjunto_a.union(conjunto_b)")
uniao = conjunto_a.union(conjunto_b)
print(f"O resultado da união dos dois conjuntos: {uniao}\n")
print("Vamos agora fazer uma interseção (elementos que estão em ambos os conjustos):")
intersecao = conjunto_a.intersection(conjunto_b)
print(f"O resultado da interseção dos dois conjuntos A e B: {intersecao}\n")
#conversão entre tipos de dados (Type Casting)
print("Vamos ver como funciona a conversão entre tipos de dados (type Casting):\nA conversão de tipos de dados é converter de um tipo de dado para outro.")
#converter de String para número integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(F"O texto em String '{numero_em_texto}'que é do tipo {type(numero_em_texto)}, foi convertido para número inteiro: {numero_inteiro}, e agora é do type: {type(numero_inteiro)}\n")
#convertendo String para número float
numero_decimal_em_texto = "45.67"
numero_float = float(numero_decimal_em_texto)
print(f"O texto em String '{numero_decimal_em_texto}' que é do tupo {type(numero_decimal_em_texto)}, foi convertido para número float: {numero_float}, e agora é do tipo: {type(numero_float)}")
#Convertendo de número para String
idade = 25
idade_texto = str(idade)
print(f"O número: {idade} é do tipo {type(idade)}, foi convertido para String:'{idade_texto}', e agora é do tipo {type(idade_texto)}")
#Conversão entre estruturas de dados.
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 4, 5]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)
print(f"\nLista original: {lista_com_duplicatas}")
print(f"\nConvertido para Conjunto/Sets (remove duplicatas) {conjunto_unico}")
print(f"\nConvertida de valta para lista {lista_sem_duplicatas}")