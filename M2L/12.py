# Calcule a complexidade, no pior e no melhor caso, dos fragmentos de código abaixo:
n=5
for i in range (n-1): #rodará n-1 vezes
    print(i)
for i in range(0,n,2): #rodará até n variando de 2 em 2
    print(i)
for i in range(0,n,2):#rodará até n variando de 2 em 2
    print(i)
    i -= 1
"""no melhor onde n é impár rodará até 1 numero antes do final"""
"""pior caso onde n é par rodará até o proprio n"""
# 0(n)
