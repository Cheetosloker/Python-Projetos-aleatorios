import forca
import advinhacao
def escolha_jogo():
    print("escolha o jogo")

    print("(1) adivinhas (2)forca")

    jogo = int(input("qual jogos"))

    if(jogo == 1):
        print("jogando adivinhacao")
        advinhacao.jogar()
    elif(jogo == 2):
        print("jogando forca")
        forca.jogar()
if(__name__ == "__main__"):
    escolha_jogo()