import random

def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def criar_palavra_secreta():
    arquivo = open("jogos/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    aleatoria = random.randrange(0, len(palavras))
    palavra_secreta = palavras[aleatoria].upper()
    return palavra_secreta

def define_letras_certas(palavra_secreta):
    letras_certas = ["_" for letra in palavra_secreta]

def escreva_letra_letra():
    chute = input("Qual é a letra?")
        chute = chute.strip().upper()

def jogar():

    mensagem_inicial()
    palavra_secreta = criar_palavra_secreta()

    letras_certas = define_letras_certas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        
        chute = escreva_letra()

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

    