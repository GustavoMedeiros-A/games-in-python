import random

linhas = 6
colunas = 6
vetor = [0] * 6
vetor_mapa = [ "0" ] * colunas
matriz = []
mapa = []
contador = 0

navio = 1
submarino = 2
porta_aviao = 3
onu = 5
contador_navio = 0
contador_submarino = 0
contador_porta = 0
contador_onu = 0

def imprime(mat, l):
    cont = 0
    while cont < l:
        print(mat[cont])
        cont += 1

while contador < linhas:
    matriz.append(vetor.copy())
    mapa.append(vetor_mapa.copy())
    contador += 1

while contador_navio < navio:
    linhas = random.randint(0, linhas-1)
    colunas = random.randint(0, colunas-1)
    matriz[linhas][colunas] = 1
    contador_navio += 1

while contador_submarino < submarino:
    linhas = random.randint(0, linhas-1)
    colunas = random.randint(0, colunas-1)
    while (matriz[linhas][colunas] == 1):
        linhas = random.randint(0, linhas-1)
        colunas = random.randint(0, colunas-1)
    matriz[linhas][colunas] = 2
    contador_submarino += 1

while contador_porta < porta_aviao:
    linhas = random.randint(0, linhas-1)
    colunas = random.randint(0, colunas-1)
    while (matriz[linhas][colunas] == 1) or (matriz[linhas][colunas] == 2):
        linhas = random.randint(0, linhas-1)
        colunas = random.randint(0, colunas-1)
    matriz[linhas][colunas] = 3
    contador_porta += 1

while contador_onu < onu:
    linhas = random.randint(0, linhas-1)
    colunas = random.randint(0, colunas-1)
    while (matriz[linhas][colunas] == 1) or (matriz[linhas][colunas] == 2) or (matriz[linhas][colunas] == 3):
        linhas = random.randint(0, linhas - 1)
        colunas = random.randint(0, colunas - 1)
    matriz[linhas][colunas] = 4
    contador_onu += 1

def jogo(linha, coluna):
    jogador_1 = 0
    if matriz[linha-1][coluna-1] == 0:
        print("Você mirou na água!")
        matriz[linha_jog-1]