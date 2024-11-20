# Projeto 1 - Desenvolvimento de Gome em Linguagem Python - Versão 1

# Import

import random
from os import system, name


# Função para limpar a tela a cada exercução.
def limpa_tela():

    # Windows
    if name == "nt": # nt é o nome interno dado para Windows.
        _= system("cls") 

    # Mac ou linux
    else:
        _= system("clear")
        

def game ():
    limpa_tela()
    print("\nBem-Vindo(a) ao incrivel jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo.
    palavras = [ "uva", "morango", "laranja","banana","abacaxi",]
    stages = [ # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """]
    

    # Escolha de palavras de forma randomica.
    palavra = random.choice(palavras)
    
    # List comprehension
    letras_descobertas = ["_" for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas.
    letras_erradas = []

    # Loop enquanto número de chaces for maior do que zero
    while chances > 0:

        # Print na tela:
        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print(f"Letras erradas: {" ".join(letras_erradas)}")
        if chances:
            print(f"{stages[chances]}")
        

        # Tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0

            # Fazer uma checagem para saber se a tentativa esta dentro da palavra.
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Segunda condição.
        if "_" not in letras_descobertas:
            print(f"\nVocê venceu, a palavra era: {palavra.capitalize()}")
            break
    if "_" in letras_descobertas:    
        print(f"\nInfelizmente você perdeu, a palavra é {palavra.capitalize()}")

# bloco main. Indica de um programa python
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está apendendo programação em Python com a DAS. : \n")