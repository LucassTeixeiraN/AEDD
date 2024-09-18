'''
9. Do fragmento de código abaixo, determine a complexidade:
for i=0 to n-1: 
    for j=0 to n-1:
        mat[i][j] = 0
        for k=0 to n-1:
            mat[i][j] += A[i][k] * B[k][j]'''

# os loops iteram n vezes (de 0 a n-1)
# n * n * n = n³
# o primeiro laço executa n vezes, o segundo executa n vezes para cada iteração do primeiro(n*n = n²)
# O terceiro executa n vezes para cada iteração do segundo loop (n*n*n = n³)
# Complexidade = O(n³)