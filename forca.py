def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "koenigsegg"
    letras_certas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        
        chute = input("Qual é a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_certas[index] = letra
            index = index + 1

        print(letras_certas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
