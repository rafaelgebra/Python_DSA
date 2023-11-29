numeros = list(range(1, 101))

for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        if numero == 20:
            print('O numero 20 foi selecionado')
        else:
            print(numero)
