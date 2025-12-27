"""
Pseudicódigo3 - Algoritmo Bublle Sort
Bublle Sorte é um algoritimo de ordenação simples que funcio a comparando cada elemento com o próximo, e trocando-os de lugar se eles estiverem em ordem incorreta. O algoritimo repete esse processe várias vezes, até que todos os elementos estejam ordenados. A cada passagem, o maior elemento "FLUTUA" para o final da array "VETOR/LISTA de elementos", como uma bolha dando origem ao nome do algoritimo. (Bublle-bolha, Sort-ordenar)

INICIO
    Programando com pseudocódigo

    Para da cada elemento I no array de elemento N
        Para cada elemento J na array do tamanho N - 1
            Se elemento I for maior de elemento J
                Troca os elementos I e J
    Exibir o array ordenado
        
FIM
"""
lista = [17,3,2,5,6,4,7]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(lista))