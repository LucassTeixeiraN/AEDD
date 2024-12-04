def matriz_potencia(matriz, k):
    n = len(matriz)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        resultado[i][i] = 1

    while k:
        if k % 2 == 1:
            resultado = multiplica_matrizes(resultado, matriz)
        matriz = multiplica_matrizes(matriz, matriz)
        k //= 2

    return resultado

def multiplica_matrizes(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][l] * B[l][j] for l in range(n))
    return C

def num_caminhos_comprimento_k(matriz_adj, u, v, k):
    matriz_k = matriz_potencia(matriz_adj, k)
    return matriz_k[u][v]

def total_caminhos(matriz_adj, u, v):
    n = len(matriz_adj)
    total = 0
    for k in range(1, n + 1):
        total += num_caminhos_comprimento_k(matriz_adj, u, v, k)
    return total


matriz_adj = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]

u, v = 0, 3
k = 2

print(f"Número de caminhos de comprimento {k} entre os nós {u} e {v}: {num_caminhos_comprimento_k(matriz_adj, u, v, k)}")
print(f"Número total de caminhos entre os nós {u} e {v}: {total_caminhos(matriz_adj, u, v)}")
