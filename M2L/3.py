n=6
exp=5
def expo(exp , n):
    result = 1  #iram rodar 1 vez
    
   
    for _ in range(exp):# ira rodar exp + 1 vezes
        result *= n # ira rodar exp vezes
    
    return result

def pow():
    X=expo(n,exp)
    print(n,"elevado a" , exp,"é igual a:",X) # ira rodar 1 vez
pow()

# 2exp + 10 = equação de complexidade
#O(exp)
