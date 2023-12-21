# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print('Selecione o número da operação desejada:\n')
print('1 - Soma')
print('2 - Subtação')
print('3 - Multiplocação')
print('4 - Divisão\n')
while True:
    opcao = int(input('Digite sua opção [1, 2, 3, 4]: '))
    if opcao not in (1, 2, 3, 4):
        print(('\nOpção inválida.... \n'))
    else:
        n1 = int(input('\nDigite o primeiro número: '))
        n2 = int(input('\nDigite o segundo número: '))
        if opcao == 1:
            total = n1 + n2
            print(f'\n{n1} + {n2} = {total}')
            break
        elif opcao == 2:
            total = n1 -n2
            print(f'\n{n1} + {n2} = {total}')
            break
        elif opcao == 3:
            total = n1 * n2
            print(f'\n{n1} * {n2} = {total}')
            break
        elif opcao == 4:
            if n1 == 0:
                print('\nNão é posivel fazer divição por 0')
            else:
                total = n1 / n2
                print(f'\n{n1} / {n2} = {total}')
                break