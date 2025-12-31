#CAP02
print("Ola, Mundo!")

#criando lista
numeros = list(range(1, 21))
print(numeros)
print(type(numeros))

#Percorer a lista e imprimir números pares e divísiveis por 4
for n in numeros:
    if n % 2 == 0 and n % 4 == 0:
        print(n)

