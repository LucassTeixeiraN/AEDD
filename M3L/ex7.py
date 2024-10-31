'''Implemente uma versão generalizada para busca binária numa matriz m x n.'''
def buscar(matriz, alvo):
    if not matriz or not matriz[0]:
        return False
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    linha = 0
    coluna = colunas - 1
    
    while linha < linhas and coluna >= 0:
        valor_atual = matriz[linha][coluna]
        
        if valor_atual == alvo:
            return True
        elif valor_atual > alvo:
            # Se o valor atual é maior que o alvo, mova para a esquerda
            coluna -= 1
        else:
            # Se o valor atual é menor que o alvo, mova para baixo
            linha += 1
            
    return False

def main():
    
    matriz = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60],
    ]

    alvo = 3
    resultado = buscar(matriz, alvo)
    print(f"O valor {alvo} foi encontrado na matriz? {resultado}")

    alvo = 13
    resultado = buscar(matriz, alvo)
    print(f"O valor {alvo} foi encontrado na matriz? {resultado}")
main()