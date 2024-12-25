# Capítulo 9. 

#Pacote Python - MAIS USADO
#Introdução a NumPy (Numerial Python) numpy.org

# Importação de pacote
import numpy as dsa
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
print(f"Usando a mesma indexação, trazer as infirmações de uma determinada coluna. arr_4d[0,2,1,4]. O resultado é 50. Comprovando com o código: {arr_4d[0,2,1,4]}")