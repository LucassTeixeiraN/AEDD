'''O método de lista reverse inverte os elementos da lista. Defina uma função chamada
reverse que inverte os elementos no argumento de lista (sem usar o método reverse).
Tente tornar essa função a mais eficiente possível e indique sua complexidade
computacional usando a notação big-O.'''


array = [9, 8, 7, 6, 5, 4, 3, 10]
n = len(array)
def reverse(array, n):
    start = 0               # COMPLEXIDADE não tem pior ou melhor caso: executa igual
    end = n - 1
    while start < end:       # Quantas trocas aconteceram?
        aux = array[start]        # a função itera sobre a metade da lista, invertendo o inicio e o fim, ou seja, a cada iteração o inicio e fim são trocados, portanto n/2
        array[start] = array[end]       # Logo, O(n)
        array[end] = aux
        start += 1
        end -= 1
    print(array)

reverse(array, n)  
