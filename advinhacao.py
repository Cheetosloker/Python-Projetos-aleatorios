def jogar():

    print("jogo")

    import random

    numero_secreto = random.randrange(101)
    total_tentavas = 0
    pontos = 1000

    print ("qual nivel de dificuldade")
    print ("(1) facil (2) medio (3) dificil")

    nivel = int(input("defina nivel: "))

    if(nivel == 1):
        total_tentavas =20
    elif(nivel == 2):
        total_tentavas = 10
    else:
        total_tentavas= 5

    for rodada  in range(1, total_tentavas + 1):
        print ("tentativa {} de {}". format(rodada, total_tentavas))
        chute_str  = input("digite o numero")
        print("voce digitou", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("voce acerto e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("voce erro seu chute foi maior")
            elif (menor):
                print("voce erro seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("fim de jogo")
if(__name__ == "main"):
    jogar()