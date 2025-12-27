"""from math import sqrt

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rochet(self):
        print(self.x, self.y)


roc1 = Rocket(2, 5)
roc1.move_rocket(4, 6)
roc1.print_rochet()
print(roc1.x)
print(roc1.y)"""
"""

# Exercicio 2
class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("teste de inicialização do construtor")

    def retorno(self):
        return self.nome, self.cidade, self.telefone, self.email
        


pessoa1 = Pessoa("Rafael", "Guarulhos", "(11)958525535", "rafael@gmail.com")
nome_antes = pessoa1.nome
print(f"Objeto do type {pessoa1} impresso")
print(f"Esse não os atributos do método {[item for item in pessoa1.retorno()]}")
print("-- Usando métodos especiais --")
print(f"Usando o hasattr para verificar o se o nome existe, {hasattr(pessoa1, "nome")} ")
setattr(pessoa1, "nome", "troxa")
print(f"Usando o método especial setattr o nome foi alterado de {nome_antes} para, {getattr(pessoa1, "nome")}")
print(f"Posso chamar o atributo dessa forma, 'pessoa.nome' como também dessa forma, 'getattr(pessoa1, 'nome')'. Ambas traz o mesmo resultado")"""

# Exercicio 3

class Smartphone(object):
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho = "Pequeno", interface = "Led"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
    
    def print_mp3player(self):
        print(f"Valores para do objeto criado {self.tamanho}, {self.interface}, {self.capacidade}")

device1 = MP3Player("64","GB")
device1.print_mp3player()