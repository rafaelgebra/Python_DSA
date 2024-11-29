#Pacote Python - MAIS USADO
#Introdução a NumPy (Numerial Python) numpy.org

# Importação de pacote
import numpy as dsa
print(dsa.__version__)

# criando um Array numpy a partir de ua lista python
arrl = dsa.array([10,21,32,43,48,15,76,57,89,5])
print("Imprimindo a variável arrl, que é a array.")
print(arrl)
# Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho.
print(type(arrl))
# Com o shape consegue veriaficar o formado do array.
print(f"Veridicando o formato da array com shape.\nO resultado é {arrl.shape}. Esse resultado acontece porque tem {arrl.shape[-1]} elementos em uma unica dimenção.\nTambém conhecido como vetor, 'Uma lista de elementos'.")

print("Um array, NumPy é uma estrutura de dados multidimensional usada em computação científica e análise de dados. O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grande homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros. Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem vários otimizações de dessempenho. Além disso, NumPy permite a fácil leitura e escrita e arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.\n")

