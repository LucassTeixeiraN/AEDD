# 14. Escreva um algoritmo que receba valores em um vetor e imprima “ORDENADO” se o
# vetor estiver em ordem crescente. Qual é a complexidade deste seu algoritmo?

def estaOrdenado(list, n): # 1
    for i in range(n-1): # n
        prox = list[i+1] #n-1
        if list[i] > prox: #no pior dos casos n-1 e 1 no melhor
           return False #1
    return True #1
# 3n + 1
# O(n)


def main():
    # lista = [1,2,3,4,5]
    lista = [1,2,4,3,5]

    if estaOrdenado(lista, len(lista)):
        print("ORDENADA")
    else:
        print("NÃO ORDENADA")

main()

     