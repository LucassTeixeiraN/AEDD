# s = 0
# for i=0 to n-2:
# for j=1 to 2*N:
# s = s+1
n=10
s = 0 
for i in range(n-2 ):# rodará  n-1 vezes
    
    for j in range(1, 2*n): #rodará  n-2(2*n + 1) vezes
        s += 1  #rodará  n-2(2*n) vezes
        
# equação de grandeza = 2(n-2(2*n+1)) 
#                     = 2(n-2n-2)
#                     = 2(-n-2)
#                     = 2n-4

# O(n**2)
