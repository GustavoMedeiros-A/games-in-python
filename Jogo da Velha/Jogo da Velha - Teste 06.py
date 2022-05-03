white = "\033[1;30m "
blue = "\033[1;34m "
red = "\033[1;31m"
n = "\033[m"
x = "\033[1;30m X \033[m"
o = "\033[1;34m O \033[m"

tabuleiro = [
         [" 1 ", " 2 ", " 3 "],
         [" 4 ", " 5 ", " 6 "],
         [" 7 ", " 8 ", " 9 "]
]

matriz = [[0, 0], [0, 1], [0, 2],
          [1, 0], [1, 1], [1, 2],
          [2, 0], [2, 1], [2, 2]]

def game():
    jogadas = 0

    jogador1 = input("Digite o nome do jogador 1: ")
    jogador2 = input("Digite o nome do jogador 2: ")
    while vitoria() == 0:
        if (jogadas % 2 + 1) == 1:
            print(f"Sua vez,{white}{jogador1}{n}!")
        else:
            print(f"Sua vez,{blue}{jogador2}{n}!")
        desenhar_tabuleiro()
        pegador = input("Digite o lugar que você quer jogar: ")
        if pegador.isdigit() == False:
            print("Isso não é um número!")
        else:
            escolha = int(pegador)
            if escolha > 9 or escolha < 1:
                print("Esse número não existe!")
            else:
                for i in range(9):
                    escolha[i] == matriz[i]

                if tabuleiro[matriz[i]] == f"{x}" or tabuleiro[matriz[i]] == f"{o}":
                    if (jogadas % 2 + 1) == 1:
                        print(f"{red}Não tá vendo que o {jogador2} já jogou nessa posição! Tente de novo {jogador1}!{n}")
                    else:
                        print(f"{red}Não tá vendo que o {jogador1} já jogou nessa posição! Tente de novo {jogador2}!{n}")
                else:
                    if (jogadas % 2 + 1) == 1:
                        tabuleiro[matriz[i]] = f"{x}"
                        jogadas = jogadas + 1
                    else:
                        tabuleiro[matriz[i]] = f"{o}"
                        jogadas = jogadas + 1


                if vitoria():
                    if jogadas % 2 + 1 == 1:
                       print(f"{blue}{jogador2} ganhou! Boa!{n}")
                       desenhar_tabuleiro()
                    else:
                        print(f"{white}{jogador1} ganhou! Boa!{n}")
                        desenhar_tabuleiro()

                if jogadas == 9 and vitoria() == False:
                    print(f"{red}Empate!{n}")
                    return 1


def vitoria():
    for i in range(3):
        soma = tabuleiro[i][0] + tabuleiro[i][1] + tabuleiro[i][2]
        if soma == f"{x}{x}{x}" or soma == f"{o}{o}{o}":
            return 1

    for i in range(3):
        soma = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if soma ==f"{x}{x}{x}" or soma == f"{o}{o}{o}":
            return 1

    diagonal1 = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 ==f"{x}{x}{x}"or diagonal1 ==f"{o}{o}{o}" or diagonal2 ==f"{x}{x}{x}"or diagonal2 == f"{o}{o}{o}":
        return 1
    return 0

def desenhar_tabuleiro():
    print(f" {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("----------------")
    print(f" {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("----------------")
    print(f" {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")


game()