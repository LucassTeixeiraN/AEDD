'''A função pow retorna o resultado de elevar um número a determinada potência.
Defina uma função expo que execute essa tarefa e indique a complexidade
computacional usando a notação big-O. O primeiro argumento dessa função é o
número e o segundo argumento é o expoente (apenas números não negativos). Você
pode usar um laço em sua implementação, mas não use o operador ** do Python ou a
função pow do Python.'''
numero = 5
exp = 2
def expo(numero , exp):
    result = 1  #iram rodar 1 vez
    
   
    for i in range(exp):# ira rodar exp + 1 vezes
        result *= numero # ira rodar exp vezes
    
    return result

def pow():
    X = expo(numero, exp)
    print(numero,"elevado a" , exp,"é igual a:",X) # ira rodar 1 vez
pow()

# 2exp + 3 = equação de complexidade
#O(exp)
