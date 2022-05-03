def menu():
    continuar = 1
    while continuar == 1:
        continuar = int(input("Digite 0 para sair: \n"
                              "Digite 1 para continuar: \n"))
        if continuar:
            game()
        else:
            print("Até mais")



def game():
    jogadas = 0
    while ganhou() == 0:
        print("\n Jogador ", jogadas % 2 + 1)
        mostrar_tabulheiro()
        linha = int(input("\nDigite qual linha você quer jogar: "))
        coluna = int(input("Digite qual coluna você quer jogar: "))
        if tabulheiro[linha][coluna] != 10 or tabulheiro[linha][coluna] != -10:
            if (jogadas % 2 + 1) == 1:
                tabulheiro[linha][coluna] = 10
            else:
                tabulheiro[linha][coluna] = -10
        else:
            print("Alguem já jogou nessa posição!")

        if ganhou():
            print(f"Jogador {jogadas%2-1} ganhou após {jogadas+1} rodadas")
        jogadas = jogadas + 1

def ganhou():
    #Analisando se ganhou por linha
    for i in range(3):
        soma = tabulheiro[i][0] + tabulheiro[i][1] + tabulheiro[i][2]
        if soma == 30 or soma == -30:
            return 1

    for i in range(3):
        soma = tabulheiro[0][i] + tabulheiro[1][i] + tabulheiro[2][i]
        if soma == 30 or soma == -30:
            return 1

    diagonal1 = tabulheiro[0][0] + tabulheiro[1][1] + tabulheiro[2][2]
    diagonal2 = tabulheiro[0][2] + tabulheiro[1][1] + tabulheiro[2][0]
    if diagonal1 == 30 or diagonal1 == -30 or diagonal2 == 30 or diagonal2 == -30:
        return 1

    return 0

def mostrar_tabulheiro():
    for i in range(3):
        for j in range(3):
            if tabulheiro[i][j] == 10:
                print(" | X", end="")
                desenha_tabuleiro(i,j)
            else:
                if tabulheiro[i][j] == -10:
                    print(" | O", end="")
                    desenha_tabuleiro(i,j)
                else:
                    desenha_tabuleiro(i, j)




def desenha_tabuleiro(i,j):
    if tabulheiro[i][j] == 1 or tabulheiro[i][j] == 4 or tabulheiro[i][j] == 7:
        print(f" | {tabulheiro[i][j]}", end="")
    else:
        if tabulheiro[i][j] == 2 or tabulheiro[i][j] == 5 or tabulheiro[i][j] == 8:
            print(" |", end="")
            print(f" {tabulheiro[i][j]}", end="")
        else:
            if tabulheiro[i][j] == 3 or tabulheiro[i][j] == 6:
                print(f" | {tabulheiro[i][j]}", end="")
                print("\n -----------")
            else:
                if tabulheiro[i][j] == 9:
                    print(f" | {tabulheiro[i][j]}")




tabulheiro = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
]

menu()