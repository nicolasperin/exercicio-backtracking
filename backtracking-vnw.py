def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " | ".join(linha) + " |")

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    if (chegou_ao_fim(linha_atual, coluna_atual)):
        return linha_atual, coluna_atual, profundidade
    
    melhor_profundidade = float("inf")
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    direcoes = [(0,1), (0,-1), (1,0), (-1, 0)]
    
    for d_linha, d_coluna in direcoes:
        nova_linha, nova_coluna = linha_atual + d_linha, coluna_atual + d_coluna
        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '*'
            resultado = proximo_movimento(tabuleiro, nova_linha, nova_coluna, profundidade + 1)
            tabuleiro[nova_linha][nova_coluna] = ' '
            if resultado[2] < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = nova_linha, nova_coluna, resultado[2]

    return melhor_linha, melhor_coluna, melhor_profundidade             

def movimento_valido(tabuleiro, linha, coluna):
    if linha < 0 or linha >= len(tabuleiro):
        return False
    if coluna < 0 or coluna >= len(tabuleiro[0]):
        return False
    return tabuleiro[linha][coluna] == ' '

def chegou_ao_fim(linha, coluna):
    return linha == 3 and coluna == 4
    
def main():
    tabuleiro = [
            [' ',' ',' ',' ', 'X'],
            ['X','X',' ','X', ' '],
            [' ',' ',' ','X', ' '],
            ['*','X',' ',' ', ' ']
        ]
    
    linha_atual, coluna_atual = 3, 0

    while True:
        if (chegou_ao_fim(linha_atual, coluna_atual)):
            print("Chegou ao fim")
            break

        nova_linha, nova_coluna, profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0)

        if (profundidade == float("inf")):
            print("Não foi possível encontrar um caminho")
            break
        
        linha_atual, coluna_atual = nova_linha, nova_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'
        mostrar_tabuleiro(tabuleiro)

        continuar = input("Pressione enter para mostrar o próximo passo ou digite 'q' para sair: ")
        if continuar.lower() == "q":
            break

main()