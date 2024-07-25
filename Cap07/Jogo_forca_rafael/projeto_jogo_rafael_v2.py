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

    # Lista comprehension.
    letras_descobertas = ["_" for letra in palavra] # Com esse for consegue deixar um underline para cada letra da palavra que precisa ser descoberta

    # Número de chances
    chances = 6 # Essa variável limita a quantidade de chances.

    # Lista para as letras erradas. 
    letras_erradas = [] # Essa lista vai acrescentar a letra erradas, com ela pode ir somando usando o atributo len(), para contar e mostrar para o usuario a quantidade de letra que errou.

    # Loop (while), enquanto o número de chances dor maior do que zero vai continuar.
    while chances > 0:
        #print
        print(" ".join(letras_descobertas)) # O join() faz aqui uma junção entre o espaço em banco e a lista letras_decobertas.
        print(f"\n\033[;30;42mChance restante:\033[m {chances}")
        print(f"\033[;30;41mLetras erradas: {" ".join(letras_erradas)}\033[m") # Aqui o join() também faz a função de junção mas nessa caso é a junção do espaço com a variável letra_erradas 

        # Tentativa
        tentativa = input("\nDigite um letra: ").lower()

        # Bloco condicional.
        if tentativa in palavra: # Se a letra estiver dentro da palavra escolhida, a variável index é criada e recebe 0.
            index = 0
            for letra in palavra: # O loop for nesse caso é para checar cada letra dentro da palavra. 
                if tentativa == letra: # Se a letra digitada em tentativa for igual (==) a letra que foi verificado pelo Loop, entra na proxím
                    letras_descobertas[index] = letra # se a condição de cima for verdadeira, a lista letras_descobertas recebi no local "index" de aonde foi "encontrada"
                index += 1 # Esse incremento é dado quando a confição de cima dor verdade
        else:
            chances -= 1 # Se a condição estiver errada, é reduzido o número de chances
            letras_erradas.append(tentativa) # Por letras_erradas ser uma lista é feito um append da letra. podendo mais para frente usar a função len() para contar a quantidade de letras erradas.
        
        # Segunda condição.
        if "_" not in letras_descobertas: # Se os underline não tiver mais na lista de letras_descobertas. o usúario venceu.
            print(f"\n\033[;30;42mVocê venceu, a palavra era:\033[m {palavra}")
            break # É dado um break porque o usúario venceu e sai do loop while dando fim ao jogo.
    
    # Terceira condição. Analizar se ainda tem underlaine na palavra escolhida.
    if "_" in letras_descobertas:
        print(f"\n\033[;30;41mVocê perdeu, a palavra era:\033[m \033[;30;42m{palavra.capitalize()}\033[m")

# Bloco main. É usado para dizer que esse script é um móduçp Python um programa Python

if __name__ == "__main__":
    game() # Como parametro é usado a função game() de já chama a função limpar_tela
    print("\n\033[;30;42mParabéns. Você esta aprendendo a progrmar em Python com a DSA. :\033[m\n")