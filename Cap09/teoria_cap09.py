# Capítulo 9. 

#Pacote Python - MAIS USADO
#Introdução a NumPy (Numerial Python) numpy.org

# Importação de pacote
import numpy as dsa
import os
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
print("Operações Matemáticas com Arrays NumPy.")
print("Criando array com a Bíblioteca Numpy, usando o arange. Será o seguinte código.")
arr15 = dsa.arange(1, 10)
print(f"O resultado do arange de 1, 10 é: {arr15} *Lembrete, 0 número 10 não aparece porque ele é absoluto.")
print(f"Um exemplo do que podemos fazer com a matématica na bíbliotera NumPy é somar os valores com o método .sum(), obviamente esse é um exemplo simple mas, seve de exemplo.\nO resultado da soma de todos os valores do array arr15 é: {dsa.sum(arr15)}\n")
print(f"Outro exemplo é que pode ser calculado o produto com o método .prod(), o resultado é: {dsa.prod(arr15)}. Produto é a multiplicação de todos os valores dentro da arry.")
print(f"A soma acumulada é outo exemplo, {dsa.cumsum(arr15)}. É só somar o primeiro elemento com o segundo, depois somar o segundo com o terceito. Essa seguençia vai até o fim dos elementos.")
print("Exemplo com 2 arrays. Um chamado arr16 e o outro chamado arr17.")
arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])
arr18 = dsa.add(arr16, arr17)
print(f"O valor dos arrays são:\nArr16 é: {arr16}.\nArr17 é: {arr17}.\n")
print(f"Pode ser usado o método .add(), da bíblioteca NumPy para somar os elementos das arrays.\nO resultado da soma entre os elementos é: {arr18}. # Lembrando, os valores somados não é o total de todos o conteúdo, foi somado os valores referênte a cada elemento de cada indice de cada array.\n")
print("Para multiplicar duas matrizes NumPy, podemos usar a função dot() ou o operador @. Ambos os métodos executam a multiplicação matricial. É importante lembrar que, para a multipicação de matrizes possa ser executada, o número de colunas da primeira matriz deve ser igual ao número de linhas do segunda matriz.\n\nHá varias forma de multiplicar elementos de matrizes NumPy. A função dot() é uma método bastante utilizado\n")
print("Exemplificando com duas novas matrizes.")
print("A primeira matriz é a arr19 e a segunda é arr20. #Lembre é uma matriz de 2 dimenções.")
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])
arr21 = dsa.dot(arr19, arr20)
print(f"O valor da matriz arr19 é:\n{arr19}.\nO valor da segunda matriz é:\n{arr20}.\n")
print(f"Como dito o arra19 é uma matriz de {arr19.shape}. Podemos ter a certeza disso porque foi usado o atributo '.shape'.")
print(f"Como dito o arra20 é uma matriz de {arr20.shape}. Podemos ter a certeza disso porque foi usado o atributo '.shape'.\n")
print(f"Agora será feito a multiplicação das matrizes, esse exemplo será usado a matrix arr19 e arr20.\nE para fazer essa Multiplicação é só usar o método .dot(), pondo as arrys como elementos do método.\nfica assim: arr21 = dsa.dot(arr19, arr20).\nO resutado é:\n{arr21}")
print(f"O processo de multiplicão de uma matriz pelo método .dot().\nO exemplo que será usado é dos arrays arr19 e arr20.\nOnde os valores do arr19 é:\n{arr19}.\nE os valores do arr20 é:\n{arr20}.\nA multiplicação é feita da seguinte forma.\nA primeira linha da primeira matrix é multiplicado com a primeira coluna da primeira matriz. E depois são somadas. Após isso, é feita a multiplicação da primeira linha com a segunda coluna...\nSegue abaixo exemplo gráfico.")
print("""
        1 2  X  5 6   =   1*5 + 2*0   1*6 + 2*7   =   5  20
        3 4  x  0 7   =   3*5 + 4*0   3*6 + 4*7   =   15 46
      """)
print(f"LEMBRETE.\nPara utilizar o método .dot() as matrizes tem que ter as especificações correta... O número de colunas da primeira matriz tem que ser mesmo número de linhas da segunda matriz. Senão da ERRO.")
arr21 = arr19 @ arr20
print(f"Além do metodo .dot() para fazer a multiplicação pode ser usado o simbulo @.\nVejá o resultado trucando o método .dot() por @: 'arr21 = arr19 @ arr20':\n{arr21}\nO @ foi lançado na versão 3.5 do Python")
arr21A = arr19 @ arr20
print(f"Outra opção para multiplicar matrizes é o método .tensordot() faz a mesma coisa que @ e .dot().\nVejá o resultado usando o .tensordot(): 'arr22 = arr19 @ arr20'.\n{arr21A}\n")
print(f"ConceitoSlicing (FATIAMENTO) de Arrays NumPy\n")
print(f"Será criado uma array de 3 dimenções usando o método função .diag(), o comando completo é arr22 = dsa.diag(dsa.arange(3)).")
arr22 = dsa.diag(dsa.arange(3))
print(f"O resultado é:\n{arr22}\n")
print(f"Comprovando a quantidade de dimenção usando o método .share(): {arr22.shape}.\n")
print(f"Fariando com anotação de índixe resultado do arr22[1,1], o resultado é o conteúdo da linha 1 com a coluna 1: {arr22[1,1]}")
print(f"Solicitando o conteúdo da linha 1, arr22[1].\nResultado:\n{arr22[1]}\n")
print(f"Solicitando o conteúdo de todas as linhas mas a coluna 2, arr22[:,2].\nResultado:\n{arr22[:,2]}")