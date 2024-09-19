'''Uma estratégia alternativa para a função expo usa a seguinte definição recursiva:
expo(número, expoente)
= 1, quando expoente = 0.
= número * expo(número, expoente – 1), quando o expoente é ímpar.
= (expo(número, expoente / 2))2

, quando o expoente é par.

Defina uma função recursiva expo que usa essa estratégia e indique sua
complexidade computacional usando a notação big-O.'''

def expo(numero, expoente):
    print(f'{numero} ^ {expoente}', end=' - ')
    if expoente == 0:
        return 1
    elif expoente % 2:
        return numero * expo(numero, expoente - 1)
    else:
        return expo(numero, expoente / 2) ** 2

'''
Melhor caso em que o expoente é igual a 0: O(1)
Pior caso: log(n) em que n é o expoente
'''

for i in range(1,11):
    print('base: ',i)
    for i2 in range(1, 11):
        expo(i, i2)
        print()