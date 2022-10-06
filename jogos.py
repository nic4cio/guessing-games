import adivinhacao
import forca

def escolhe_jogo():
    print("****************")
    print("Selecione o jogo")
    print("****************")


    print("(1) Forca (2) Adivinhação")
    jogo_selecionado = int(input(": "))

    if(jogo_selecionado == 1):
        print("Jogo da Forca")
        forca.jogar()

    elif(jogo_selecionado == 2):
        print("Jogo da Adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()