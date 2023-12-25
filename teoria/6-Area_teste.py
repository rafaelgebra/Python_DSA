from time import sleep


def titulo(msg):
    print()
    print(f'--- {msg.upper()} ---', flush=True)
    #sleep(0.3)
    print()


def lento(msg):# Lento para frase em str
    for letra in msg:
        print(letra, end='', flush=True)
        sleep(0.001)
    print('\n')


titulo('Abrindo Dataset em linha Única')

f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows)

titulo('Dividindo Um Arquivo em colunas')

f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
#print(full_data)

titulo('Contando as linha de um arquivo')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1
print(f'O arquivo "salarios.csv" tem {count} linhas')

titulo('Contando o número de colunas de um arquivo')
f = open('Cap06/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count1 = 0
for calumn in first_row:
    count1 += 1
print(count1)