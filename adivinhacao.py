import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input(": "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa: {rodada} de {total_de_tentativas} rodadas")
        chute_str = input("digite um numero entre um 1 e 100: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)


        if(chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print(" ")
            print("você acertou")
            break
        else: 
            if(chute_maior):
                print(" ")
                print("você errou! o seu chute foi maior do que o número secreto")

            elif(chute_menor):
                print(" ")
                print("você errou! o seu chute foi menor do que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
    print("Fim de jogo!")
    print("")
    print(f"Pontuação: {pontos}")


if(__name__== "__main__"):
    jogar()