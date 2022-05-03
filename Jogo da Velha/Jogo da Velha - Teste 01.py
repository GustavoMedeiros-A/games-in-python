import os
import random

jogar_novamente = "s"
jogadas = 0
atual_jogador = 2 # 1 = CPU / 2 = Jogador
maximo_jogadas = 9
vitoria = "N"
tabulheiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global tabulheiro
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print(f"0:  {tabulheiro[0][0]} | {tabulheiro[0][1]} | {tabulheiro[0][2]}")
    print("   ---|---|---")
    print(f"1:  {tabulheiro[1][0]} | {tabulheiro[1][1]} | {tabulheiro[1][2]}")
    print("   ---|---|---")
    print(f"2:  {tabulheiro[2][0]} | {tabulheiro[2][1]} | {tabulheiro[2][2]}")
    print(f"Jogadas: {str(jogadas)}")

def jogadas_jogador():
    global jogadas
    global atual_jogador
    global maximo_jogadas
    if atual_jogador == 2 and jogadas < maximo_jogadas:
        try:
            linha = int(input("Linha..: "))
            coluna = int(input("Coluna.: "))
            while tabulheiro[linha][coluna] != " ":
                linha = int(input("Linha..: "))
                coluna = int(input("Coluna.: "))
            tabulheiro[linha][coluna] = "X"
            atual_jogador = 1
            jogadas = jogadas + 1
        except:
            print("Jogada Inválida")
            os.system("pause")


def jogadas_cpu():
    global jogadas
    global atual_jogador
    global maximo_jogadas
    if atual_jogador == 1 and jogadas < maximo_jogadas:
        linha = random.randrange(0, 3)
        coluna = random.randrange(0, 3)
        while tabulheiro[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        tabulheiro[linha][coluna] = "O"
        jogadas = jogadas + 1
        atual_jogador = 2

def verificar_vitoria():
    global tabulheiro
    vitoria = "n"
    simbolos = ["X", "O"]
    for i in simbolos:
        vitoria = "n"
        # Verificar vitoria em linhas
        indice_linha = indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna < 3:
                if(tabulheiro[indice_linha][indice_coluna] == i):
                    soma = soma + 1
                indice_coluna = indice_coluna + 1
            if soma == 3:
                vitoria = i
                break
            indice_linha = indice_linha + 1
        if vitoria != "n":
            break
        # Verificar colunas
        indice_linha = indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_linha = 0
            while indice_linha < 3:
                if(tabulheiro[indice_linha][indice_coluna] == i):
                    soma = soma + 1
                indice_linha = indice_linha + 1
            if soma == 3:
                vitoria = i
                break
            indice_coluna = indice_coluna + 1
        if vitoria != "n":
            break

        #Verifica diagonal 1
        soma = 0
        indice_diagonal = 0
        while indice_diagonal < 3:
            if (tabulheiro[indice_diagonal][indice_diagonal] == i):
                soma = soma + 1
            indice_diagonal = indice_diagonal + 1
        if soma == 3:
            vitoria = i
            break

        #Verifica diagonal 2
        soma = 0
        indice_diagonal_linha = 0
        indice_diagonal_coluna = 2
        while indice_diagonal_coluna >= 3:
            if (tabulheiro[indice_diagonal_linha][indice_diagonal_coluna] == i):
                soma = soma + 1
            indice_diagonal_linha = indice_diagonal_linha + 1
            indice_diagonal_coluna = indice_diagonal_coluna - 1
        if soma == 3:
            vitoria = i
            break
    return vitoria

def redefinir():
    global tabulheiro
    global jogadas
    global atual_jogador
    global maximo_jogadas
    global vitoria
    jogadas = 0
    atual_jogador = 2  # 1 = CPU / 2 = Jogador
    maximo_jogadas = 9
    vitoria = "N"
    tabulheiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


while jogar_novamente == "s":
    while True:
        tela()
        jogadas_jogador()
        jogadas_cpu()
        tela()
        vitoria = verificar_vitoria()
        if vitoria != "n" or jogadas >= maximo_jogadas:
            break

        print("Fim do Jogo")
        if vitoria == "X" or vitoria == "O":
            print(f"Resultado: Jogador {vitoria} venceu!")
        else:
            print("Empate!")
        jogar_novamente = input("Jogar novamente? [S/N]: ")
        redefinir()