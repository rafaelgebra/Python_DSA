# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print('Selecione o número da operação desejada:\n')
print('1 - Soma')
print('2 - Subtação')
print('3 - Multiplocação')
print('4 - Divisão\n')
opcao = int(input('Digite sua opção [1, 2, 3, 4]: '))


if opcao not in (1, 2, 3, 4):
    print(('Opção inválida.... '))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if opcao == 1:
    total = n1 + n2
    print(f'{n1} + {n2} = {total}')

elif opcao == 2:
    total = n1 -n2
    print(f'{n1} + {n2} = {total}')

elif opcao == 3:
    total = n1 * n2
    print(f'{n1} * {n2} = {total}')

elif opcao == 4:
    total = n1 / n2
    print(f'{n1} / {n2} = {total}')