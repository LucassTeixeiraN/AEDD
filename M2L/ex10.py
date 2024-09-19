'''
for i=0 to n-2:
    for j=i+1 to n-1:
        for k=1 to j-1:
            s=1 
            
Melhor caso é O(1) quando n = 1 ou n = 2
Pior caso é O(n^3)
'''

def f(n):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(1, j - 1):
                s = 1
