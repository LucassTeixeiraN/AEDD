'''11. Calcule a complexidade, no pior caso, do fragmento de código abaixo:
s = 0
for i=0 to n-2:
    for j=1 to 2*N:
        s = s+1'''

s = 0
n = 5
N = 10
for i in range(n-2):
    for j in range(1, 2*N+1):
        s += 1
        
# O primeiro laço executa n - 1 vezes (pois vai de 0 a n-2)
# O segundo laço executa 2N vezes para cada iteração do primeiro laço

# O número total de iterações é (n-1) * 2N,  então a complexidade é O(n * 2N) = O(n*N) ignorando constantes e termos menores
