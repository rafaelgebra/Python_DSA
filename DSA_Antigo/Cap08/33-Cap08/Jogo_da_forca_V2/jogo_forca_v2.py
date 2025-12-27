# Projeto 2- Desenvolver a segunda versão do Game Forca em Python.
# Iniciar importando a biblíoteca 'random' para escolher de forma aleatória as palavras e a biblíoteca 'os' de systema

import random
from os import system, name

def limpa_tela():
    # Limpar tela se o sistema operacional dor Windows.
    if name == "nt": # "nt" é o nome interno dado para o sistema operacional Windows.
        _ = system("cls") # se o sistema operacional for Windons, com o comando "cls" é realizado a limpeza da tela.
    # o underline esta sendo usado como variável de retorno, mas como não será usado fica sem uso
    else:
        _ = system("clear") # Para outros sistemas operacionais como Mac ou linux o comando "clear" faz a limpeza da tela.

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []


# Método para adivinhar a letra
    def guess(self,letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
    
        else:
            return False
        
        return True
    
	# Método para verificar se o jogo terminou
    def hangman_over(self):
        
        return self.hangman_won() or (len(self.letras_erradas) == 6)

	# Método para verificar se o jogador venceu
    def hangman_won(self):
        if "_" not in self.hide_palavra():
            return True
        return False

    
	# Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ""
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += "_"
            else:
                rtn += letra
        return rtn

	# Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.letras_erradas)])
        print(f"\nPalavra: {self.hide_palavra()}")
        print(f"\nLetras erradas: \n",) 
        for letra in self.letras_erradas:
            print(f"{letra}", end=",")
        print()
        print("Letras corretas: ",)
        for letra in self.letras_escolhidas:
            print(f"{letra}", end=",")
        print()

# Método para ler uma palavra de forma aleatória do banco de palavras.
def rand_palavra():

    # Lista de palavras para o jogo
    palavras = ["banana", "abacaxi", "uva", "morango", "laranja",]
    # Escolha randimicamente uma palavra.
    palavra = random.choice(palavras)
    
    return palavra

# Método Main - Execução do programa
def main():
    limpa_tela()

    # Cria objeto e seleciona uma palavra randomicamente
    game = Hangman(rand_palavra())

    # Enquanto o jogo não tiver terminado, print do statu, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        # Status do game
        game.print_game_status()

        # Recebe input do terminal
        user_input = input("\nDigite uma letra: ")

        # Verifica se a letra digitada fas parte da palavra
        game.guess(user_input)
    # Veridifa o status do jogo
    game.print_game_status()
    
    # De acordo com o status, imprime mensagem na tela para o usuário.
    if game.hangman_won():
        print("\nParabéns!  Você venceu!!")

    else:
        print(f"\nGame over! Você perdeu.\nA palavra correta era {game.palavra}")

    print("\nFoi bom jogar com você! Agora vá estudar!!\n")

# Executa o game
if __name__ == "__main__":
    main()