import random

linhas, colunas = 500, 50
matriz = [[random.randint(1, 10000) for _ in range(colunas)] for _ in range(linhas)]

print(matriz)
