def menu():
    continuar = 1
    while continuar == 1:
        continuar = int(input("Digite 0 para sair: \n"
                              "Digite 1 para continuar: \n"))
        if continuar:
            game()
        else:
            print("Até mais")


contador = 0
def game():
    global contador
    jogadas = 0
    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do jogador 2: ")
    while ganhou() == 0:
        if (jogadas % 2 + 1) == 1:
            print(f"Vez do Jogador {jogador1}!")
        else:
            print(f"Vez do Jogador {jogador2}!")
        mostrar_tabuleiro()
        escolha = int(input("Digite o lugar que você quer jogar: "))
        contador = escolha
        if escolha == 1:
            linha = 0
            coluna = 0
        else:
            if escolha == 2:
                linha = 0
                coluna = 1
            else:
                if escolha == 3:
                    linha = 0
                    coluna = 2
                else:
                    if escolha == 4:
                        linha = 1
                        coluna = 0
                    else:
                        if escolha == 5:
                            linha = 1
                            coluna = 1
                        else:
                            if escolha == 6:
                                linha = 1
                                coluna = 2
                            else:
                                if escolha == 7:
                                    linha = 2
                                    coluna = 0
                                else:
                                    if escolha == 8:
                                        linha = 2
                                        coluna = 1
                                    else:
                                        if escolha == 9:
                                            linha = 2
                                            coluna = 2
        # Falta arrumar
        if tabuleiro[linha][coluna] != 10 or tabuleiro[linha][coluna] != -10:
            if (jogadas % 2 + 1) == 1:
                tabuleiro[linha][coluna] = 10
            else:
                tabuleiro[linha][coluna] = -10
        else:
            print("Alguem já jogou nessa posição!")

        if ganhou():
            if jogadas%2 + 1 == 1:
                print(f"O jogador {jogador1} ganhou depois de {jogadas+1} rodadas!")
            else:
                print(f"O jogador {jogador2} ganhou depois de {jogadas+1} rodadas!")
        jogadas = jogadas + 1

def ganhou():
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == 30 or soma == -30:
            return 1

    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma == 30 or soma == -30:
            return 1

    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 == 30 or diagonal1 == -30 or diagonal2 == 30 or diagonal2 == -30:
        return 1

    return 0
# Falta arrumar
def mostrar_tabuleiro():
    global contador
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 10 and (contador == 3 or contador == 6 or contador == 9):
                print(" | X")
                print("-----------")

            else:
                if tabuleiro[i][j] == -10 and (contador == 3 or contador == 6 or contador == 9):
                    print(" | O")
                    print("-----------")
                else:
                    if tabuleiro[i][j] == 10:
                        print(" | X", end="")
                    else:
                        if tabuleiro[i][j] == -10:
                            print(" | O", end="")
                        else:
                            desenha_tabuleiro(i, j)



# Falta arrumar
def desenha_tabuleiro(i,j):
    if tabuleiro[i][j] == 1 or tabuleiro[i][j] == 4 or tabuleiro[i][j] == 7:
        print(f" | {tabuleiro[i][j]}", end="")
    else:
        if tabuleiro[i][j] == 2 or tabuleiro[i][j] == 5 or tabuleiro[i][j] == 8:
            print(" |", end="")
            print(f" {tabuleiro[i][j]}", end="")
        else:
            if tabuleiro[i][j] == 3 or tabuleiro[i][j] == 6:
                print(f" | {tabuleiro[i][j]}", end="")
                print("\n -----------")
            else:
                if tabuleiro[i][j] == 9:
                    print(f" | {tabuleiro[i][j]}")




tabuleiro = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
]

menu()