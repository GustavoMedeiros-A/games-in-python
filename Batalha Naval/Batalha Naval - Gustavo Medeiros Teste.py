# Gustavo Andrade Medeiros

import random

print("=-"*10)
print("   Batalha Naval")
print("=-"*10)

def matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append("- |")
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    print(" "*4, end="")
    for i in range(dimensao):
        print(f"{i} ", end="  ")
    print()
    for i in range(dimensao):
        print(f"{i} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()

def alocar_jogador():
    print("Digite a posição que você quer colocar o navio!")
    cont = 0
    while cont < 1:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            print("Esse numero não existe!")
        else:
            cont += 1
            matriz_jogador[linha][coluna] = "O |"
    exibir_matriz(matriz_jogador)

def alocar_cpu():
    quantidade_linhas = 5
    quantidade_colunas = 5
    cont_cpu = 0
    while cont_cpu < 1:
        linhas = random.randint(0, quantidade_linhas - 1)
        colunas = random.randint(0, quantidade_colunas - 1)
        matriz_cpu[linhas][colunas] = "O |"
        cont_cpu += 1
    exibir_matriz(matriz_cpu)

def jogo():
    ganhou_jogador = False
    while ganhou_jogador == False:
        print("Faça sua Tentativa, jogador!")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            print("Esse número não existe!")
        else:
            matriz_cpu_verificacao[linha][coluna] = "O |"
            if matriz_cpu_verificacao[linha][coluna] == matriz_cpu[linha][coluna]:
                print("Você acertou um navio!")
                matriz_cpu_verificacao[linha][coluna] = matriz_cpu[linha][coluna] = "X |"
                exibir_matriz(matriz_cpu_verificacao)
                if matriz_cpu_verificacao == matriz_cpu:
                    print(f"Parabéns jogador, você ganhou!")
                    ganhou_jogador = True
                    quit()
            else:
                if ganhou_jogador == False:
                    print("Acertou a água!")
                    matriz_cpu_verificacao[linha][coluna] = matriz_cpu[linha][coluna] = "# |"
                    exibir_matriz(matriz_cpu_verificacao)
                    jogo_cpu()

def jogo_cpu():
    ganhou = False
    while ganhou == False:
        quantidade_linhas = 5
        quantidade_colunas = 5
        linha = random.randint(0, quantidade_linhas - 1)
        coluna = random.randint(0, quantidade_colunas - 1)
        matriz_jogador_verificacao[linha][coluna] = "O |"
        if matriz_jogador_verificacao[linha][coluna] == matriz_jogador[linha][coluna]:
            print("A CPU acertou um navio seu!")
            matriz_jogador_verificacao[linha][coluna] = matriz_jogador[linha][coluna] = "X |"
            exibir_matriz(matriz_jogador_verificacao)
            if matriz_jogador_verificacao == matriz_jogador:
                print(f"A CPU ganhou!")
                ganhou = True
        else:
            if ganhou == False:
                print("A CPU errou!")
                matriz_jogador_verificacao[linha][coluna] = matriz_jogador[linha][coluna] = "# |"
                exibir_matriz(matriz_jogador_verificacao)
                jogo()

#def verificar_vitoria():
    #if matriz_cpu_verificacao == matriz_cpu:
        #print(f"Parabéns jogador, você ganhou!")
        #exibir_matriz(matriz_cpu)
        #ganhou = True

#def verificar_vitoria_cpu():
    #if matriz_jogador_verificacao == matriz_jogador:
        #print(f"A CPU ganhou!")
        #ganhou = True


dimensao = 5
ganhou = False
matriz_jogador = matriz(dimensao)
matriz_jogador_verificacao = matriz(dimensao)
matriz_cpu = matriz(dimensao)
matriz_cpu_verificacao = matriz(dimensao)
alocar_jogador()
alocar_cpu()
jogo()
