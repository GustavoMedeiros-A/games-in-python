
def game():
    jogadas = 0

    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do jogador 2: ")
    while vitoria() == 0:
        if (jogadas % 2 + 1) == 1:
            print(f"Vez do Jogador {jogador1}!")
        else:
            print(f"Vez do Jogador {jogador2}!")
        desenhar_tabuleiro()
        escolha = int(input("Digite o lugar que você quer jogar: "))
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

        if tabuleiro[linha][coluna] == "\033[1;30m X \033[m" or tabuleiro[linha][coluna] == "\033[1;31m O \033[m":
            if (jogadas % 2 + 1) == 1:
                print(f"O jogador {jogador2} já jogou nessa posição! Tente de novo {jogador1}!")
            else:
                print(f"O jogador {jogador1} já jogou nessa posição! Tente de novo {jogador2}!")
        else:
            if (jogadas % 2 + 1) == 1:
                tabuleiro[linha][coluna] = "\033[1;30m X \033[m"
                jogadas = jogadas + 1
            else:
                tabuleiro[linha][coluna] = "\033[1;31m O \033[m"
                jogadas = jogadas + 1


        if jogadas >= 9:
            print("Empate!")
            break

        if vitoria():
            if jogadas % 2 + 1 == 1:
               print(f"O jogador {jogador2} ganhou depois de {jogadas + 1} rodadas!")
               desenhar_tabuleiro()
            else:
                print(f"O jogador {jogador1} ganhou depois de {jogadas + 1} rodadas!")
                desenhar_tabuleiro()




def vitoria():
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == " X  X  X " or soma == " O  O  O ":
            return 1

    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma ==" X  X  X " or soma == " O  O  O ":
            return 1

    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 ==" X  X  X "or diagonal1 ==" O  O  O " or diagonal2 ==" X  X  X "or diagonal2 == " O  O  O ":
        return 1

    return 0

def desenhar_tabuleiro():
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("----------------")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("----------------")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")



tabuleiro = [
         [" 1 ", " 2 ", " 3 "],
         [" 4 ", " 5 ", " 6 "],
         [" 7 ", " 8 ", " 9 "]
]

game()