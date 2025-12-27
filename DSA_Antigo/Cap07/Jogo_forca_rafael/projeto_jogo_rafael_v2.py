# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

# Import
import random
from os import system, name 

# Função para limpar a tela a cada execução
def limpar_tela():
#Aqui em baixo tem um bloco condicional para saber qual o sistem operacional que o jogo vai "rodar".

    # A primeira coisa que vai fazer é limpar a tela.
    # Windows.
    if name == 'nt': # "nt" é o nome interno dado para o sistema "Windows". 
        _ = system("cls") # Se o sistema operacional for windows, com o comando "cls" é feito a limpesa da tela.
        
        # O underline é a variavél de retorno da função system, porém não "quero" que tenha algum retorno, então é jogado para essa variavél sem uso.

    # Mac ou Linux.
    else: # Se o sistema operacional for Mac ou Linux o comando para limpar a tela é "clear".
        _ = system ("clear") # Se o sistema operacional dor Mac ou Linux, com o comando "clear" é feito a limpesa da tela.
        # O underline é a variavél de retorno da função system, porém não "quero" que tenha algum retorno, então é jogado para essa variavél sem uso.

# Função que desenha a forca na tela.
def display_hangman(chances):
    # Lista de estágios da farca, é feito literalmente dentro de uma lista com caracteres.
    stages = [ # Estágio 6 (final)
                """
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    |
                    |_________
                    
                """,
                # Estágio 5
                """
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    |
                    |_________
                    
                """,
                # Estágio 4
                """
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |
                    |
                    |_________
                    
                """,
                # Estágio 3
                """
                    ---------
                    |       |
                    |       O
                    |      \\|
                    |       |
                    |
                    |
                    |_________
                    
                """,
                # Estágio 2
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |       |
                    |
                    |
                    |_________
                    
                """,
                # Estágio 1
                """
                    ---------
                    |       |
                    |       O
                    |
                    |
                    |
                    |
                    |_________
                    
                """,
                # Estágio 0
                """
                    ---------
                    |       |
                    |
                    |
                    |
                    |
                    |
                    |_________
                    
                """
    ]
    return stages[chances]

#função
def game():
    # Bloco inicial do game
    limpar_tela() # Função para limpar a tela
    print("\n\033[;30;42mBem_vindo(a) ao jogo da forca!\033[m\n")
    print("\033[;30;42mAdivinha a palavra abaixo:\033[m")

    # Lista de Paravras para o jogo
    palavras = ["banana", "abacaxi", "uva", "morango", "laranja",]

    # Usando a bíblioteca (pacote) python Random consegue usar de forma aleatória a escolha de palavas.
    palavra = random.choice(palavras) # com a função choice (escolher em ingles) do pacote Random faz essa "escolha". 

    #Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra] # Retorna a letra separada da palavra

    # Cria o tabuleiro com caracter "_" Multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6 # Essa variável limita a quantidade de chances.

    # Lista para as letras digitadas
    letras_tentativas = []

    # Loop (while), enquanto o número de chances dor maior do que zero vai continuar.
    while chances > 0:
        #print
        print(display_hangman(chances))
        print("\033[;30;42mPalavra:\033[m", tabuleiro)
        print("\n") # Um espaço no fim

        # Tentativa
        tentativa = input("\nDigite um letra: ").lower()

        if tentativa in letras_tentativas:
            print("\033[;30;42mVocê já tentou essa letra. escolha outra!\033[m")
            continue

        # Adiciona as letras/ tentativas na lista de letras_tentaticas.
        letras_tentativas.append(tentativa)
    
        # Condicional
        if tentativa in lista_letras_palavras:
            print("\033[;30;42mVocê acertou a letra!\033[m")
            
            # Um loop For
            for indice in range(len(lista_letras_palavras)):
                # Uma condição.
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
        
            # Se todos os espaças foram preenchidis, o jogo acabou.
            if "_" not in tabuleiro:
                print(f"\033[;30;42mVocê venceu! A palavra é:\033[m {palavra}")
                break
        else:    
            print(f"\n\033[;30;41mOps. Essa letra não está na palavra\033[m")
            chances -= 1

        #Condicional
    if "_" in tabuleiro:
        print(f"\n\033[;30;41mVocê perdeu! A palavra era:\033[m {palavra}")


# Bloco main. É usado para dizer que esse script é um móduçp Python um programa Python

if __name__ == "__main__":
    game() # Como parametro é usado a função game() de já chama a função limpar_tela
    print("\n\033[;30;42mParabéns. Você esta aprendendo a progrmar em Python com a DSA. :\033[m\n")