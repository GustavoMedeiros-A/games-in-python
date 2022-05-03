from random import *
red = "\033[1;31m"
n = "\033[m"
def criar_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append("-")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    print(" "*4, end="")
    for i in range(dimensao):
        print(f"{red}{i}{n} ", end="")
    print()
    for i in range(dimensao):
        print(f"{red}{i}{n} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()

def sortear_minas(matriz):
    dimensao = len(matriz)
    cont_minas = 0
    while cont_minas < dimensao:
        linha = randint(0, dimensao - 1)
        coluna = randint(0, dimensao - 1)
        if matriz[linha][coluna] != "@":
            matriz[linha][coluna] = "@"
            cont_minas = cont_minas + 1
    return matriz

def verificar_quadrados(matriz):
    dimensao = len(matriz)
    for i in range(dimensao):
        for j in range(dimensao):
            if matriz[i][j] != "@":
                linha_inicial = i - 1
                if linha_inicial < 0:
                    linha_inicial = 0
                linha_final = i + 1
                if linha_final > dimensao - 1:
                    linha_final = dimensao - 1
                coluna_inicial = j - 1
                if coluna_inicial < 0:
                    coluna_inicial = 0
                coluna_final = j + 1
                if coluna_final > dimensao - 1:
                    coluna_final = dimensao - 1

                valor = 0
                for l in range(linha_inicial, linha_final + 1):
                    for c in range(coluna_inicial, coluna_final + 1):
                        if matriz[l][c] == "@":
                            valor = valor + 1
                if valor != 0:
                    matriz[i][j] = valor

    return matriz

#def verificar_quadrados_secretos(matriz_secreta):


 #   return matriz_secreta




def abrir_matriz(matriz, i, j):
    dimensao = len(matriz)

    if matriz[i][j] == "-":
        matriz[i][j] = " "

        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_matriz(matriz, l, c)

def abrir_matriz_secreta(matriz_secreta, i, j):
    dimensao = len(matriz_secreta)

    if matriz[i][j] == " " and matriz_secreta[i][j] == "-":
        matriz_secreta[i][j] = " "

        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_matriz_secreta(matriz_secreta, l, c)


def menu():
    print("-="*15)
    print("""Escolha o que quer fazer
1 - Marcar um casa
2 - Colocar uma bandeira
3 - Retirar uma bandeira
4 - Finalizar o jogo""")
    print("-="*15)

def jogo():
    minas_marcadas = 0
    menu()
    escolha = int(input("Escolha o que quer fazer: "))
    while minas_marcadas < len(matriz):
        if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
            print("Escolha Inválida!")
            menu()
            escolha = int(input("Escolha o que quer fazer: "))
        else:
            if escolha == 1:
                while escolha == 1:
                    print("=-"*15)
                    print("Escolha uma casa")
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                        print("Esse número não existe: ")
                    else:
                        if matriz[linha][coluna] == " ":
                            print("Área já aberta!")
                        else:
                            if matriz[linha][coluna] == "@":
                                print("Você acertou uma mina! Perdeu!")
                                escolha = 4
                            else:
                                if matriz[linha][coluna] == "-":
                                    abrir_matriz(matriz, linha, coluna)
                                    abrir_matriz_secreta(matriz_secreta, linha, coluna)

                                    exibir_matriz(matriz)
                                    exibir_matriz(matriz_secreta)
                                    menu()
                                    escolha = int(input("Escolha o que quer fazer: "))
                                else:
                                    matriz[linha][coluna] = " "
                                    exibir_matriz(matriz)
                                    menu()
                                    escolha = int(input("Escolha o que quer fazer: "))

            if escolha == 2:
                while escolha == 2:
                    print("=-"*15)
                    print("Escolha uma casa para colocar uma bandeira: ")
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                        print("Esse número não existe: ")
                    else:
                        if matriz[linha][coluna] == "@":
                            minas_marcadas = minas_marcadas + 1
                            matriz[linha][coluna] = "⚐"
                            exibir_matriz(matriz)
                            print("Você marcou uma mina!")
                            if minas_marcadas == len(matriz):
                                print("Parabéns, você ganhou!")
                                escolha = 4
                            else:
                                menu()
                                escolha = int(input("Escolha o que quer fazer: "))
                        else:
                            matriz[linha][coluna] = "⚐"
                            exibir_matriz(matriz)
                            menu()
                            escolha = int(input("Escolha o que quer fazer: "))



            if escolha == 3:
                while escolha == 3:
                    print("=-" * 15)
                    print("Escolha uma casa para retirar uma bandeira: ")
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                        print("Esse número não existe: ")
                    else:
                        if matriz[linha][coluna] != "⚐":
                            print("Não existe bandeira nesse lugar!")
                        else:
                            minas_marcadas = minas_marcadas - 1
                            matriz[linha][coluna] = "@"
                            exibir_matriz(matriz)
                            print("Você desmarcou uma casa!")
                            menu()
                            escolha = int(input("Escolha o que quer fazer: "))

            if escolha == 4:
                print("Jogo Acabou!")
                minas_marcadas = len(matriz)


dimensao = 10

matriz = criar_matriz(dimensao)
matriz = sortear_minas(matriz)
matriz = verificar_quadrados(matriz)

matriz_secreta = criar_matriz(dimensao)



exibir_matriz(matriz)
jogo()
