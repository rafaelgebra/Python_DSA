"""
INICIO
    Programando com pseudocódigo
    Exibir "Bem vindo à Calculadora"
    Peça para o usuário inserir o primeiro número
    Armazene o primeiro número em uma variável
    Peça para o usuário inserir o segundo número
    Armasene o segundo número em uma variável
    Peça para o usuário selecionar uma operação (+, -, *, /)
    Armazene a operação em uma variável
    Ultilize a operação selecionada e os números armazenados para realizar o cálculo
    Exiba o resultado
FIM
"""

print('Bem vindo à Calculadora')
n1 = float(input('Digite o primeiro números: '))
n2 = float(input('Digite o segundo número: '))
ope = str(input('Qual a operação? +, -, *, /'))
if ope == '+' :
    total = n1 + n2
    print(total)
elif ope == '-' :
    total = n1 - n2
    print(total)
elif ope == '*':
    total = n1 * n2
    print(total)
elif ope == '/':
    total = n1 / n2
    print(total)
