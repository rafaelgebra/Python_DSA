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
