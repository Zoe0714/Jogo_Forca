def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "koenigsegg".upper()
    letras_certas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        
        chute = input("Qual é a letraj?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas[index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 7
        acertou = "_" not in letras_certas
        print(letras_certas)

        if(acertou):
            print("Você acertou!")
        else:
            print("Você perdeu!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
