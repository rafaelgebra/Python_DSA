dic3 = {'chave1':1230, 'chave2':[22, 453, 73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}
print(dic3)
print(dic3['chave2'])
print(dic3['chave3'][0].upper())
var1 = dic3['chave2'][0]-2 # Nessa opção é feita uma conta matemática e adicionada a uma variável a resposta.  
print(var1)
dic3['chave2'][0] -= 2 #Dessa maneiro pode ser feita a subtração e a atribuição na mesna linha, mas não da para imprimim direto, tem que imprimir depois como o exemplo abaixo.
print(dic3)

