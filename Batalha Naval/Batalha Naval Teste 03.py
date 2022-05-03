import random

print("=-"*10)
print("   Batalha Naval")
print("=-"*10)

def criar_matriz(dimensao):
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
    while cont < 5:
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        cont +=1
        matriz_jogador[linha][coluna] = "O |"
    exibir_matriz(matriz_jogador)

def alocar_cpu():
    quantidade_linhas = 10
    quantidade_colunas = 10
    cont_cpu = 0
    while cont_cpu < 5:
        linhas = random.randint(0, quantidade_linhas - 1)
        colunas = random.randint(0, quantidade_colunas - 1)
        matriz_cpu[linhas][colunas] = "G |"
        cont_cpu += 1
    exibir_matriz(matriz_cpu)

def jogo():
    ganhou = False
    while ganhou == False:
        print("Faça sua Tentativa, jogador!")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        matriz_cpu_verificacao[linha][coluna] = "G |"
        if matriz_cpu_verificacao[linha][coluna] == matriz_cpu[linha][coluna]:
            print("Você acertou um navio!")
            matriz_cpu_verificacao[linha][coluna] = matriz_cpu[linha][coluna] = "X |"
            exibir_matriz(matriz_cpu_verificacao)
            if matriz_cpu_verificacao == matriz_cpu:
                print(f"Parabéns jogador, você ganhou!")
                break
        else:
            print("Acertou a água!")
            matriz_cpu_verificacao[linha][coluna] = matriz_cpu[linha][coluna] = "# |"
            exibir_matriz(matriz_cpu_verificacao)
            jogo_cpu()

def jogo_cpu():
    ganhou = False
    while ganhou == False:
        quantidade_linhas = 10
        quantidade_colunas = 10
        linha = random.randint(0, quantidade_linhas - 1)
        coluna = random.randint(0, quantidade_colunas - 1)
        matriz_jogador_verificacao[linha][coluna] = "G |"
        if matriz_jogador_verificacao[linha][coluna] == matriz_jogador[linha][coluna]:
            print("A cpu acertou um navio seu!")
            matriz_jogador_verificacao[linha][coluna] = matriz_jogador[linha][coluna] = "X |"
            exibir_matriz(matriz_jogador_verificacao)
            if matriz_jogador_verificacao == matriz_jogador:
                print(f"A CPU ganhou!")
                break
        else:
            print("A CPU errou!")
            matriz_jogador_verificacao[linha][coluna] = matriz_jogador[linha][coluna] = "# |"
            exibir_matriz(matriz_jogador_verificacao)
            jogo()

dimensao = 10
matriz_jogador = criar_matriz(dimensao)
matriz_jogador_verificacao = criar_matriz(dimensao)
matriz_cpu = criar_matriz(dimensao)
matriz_cpu_verificacao = criar_matriz(dimensao)
alocar_jogador()
alocar_cpu()
jogo()
