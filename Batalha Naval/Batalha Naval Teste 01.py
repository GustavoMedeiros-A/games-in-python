import random
import numpy as np

letras = ["A", "B", "C", "D", "E", "F"]
navio = 0
contador_navio = 0
linhas = 0
colunas = 0


def criar_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append("- |")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz, jogador):
    print(f"Matriz {jogador}")
    print(" "*4, end="")
    for i in (letras):
        print(f"{i}  ", end=" ")
    print()
    for i in range(dimensao):
        print(f"{i} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()


dimensao = 6
matriz1 = criar_matriz(dimensao)
#jogador1 = input("Digite o nome do jogador 1: ")
exibir_matriz(matriz1, 1)



while contador_navio < navio:
    linhas = random.randint(0, linhas-1)
    colunas = random.randint(0, colunas-1)
    matriz1[linhas][colunas] = 1
    contador_navio += 1

def game():
    print("Batalha Naval")
    print()




#jogador2 = input("Digite o nome do jogador 2: ")
matriz2 = criar_matriz(dimensao)
exibir_matriz(matriz2, 2)