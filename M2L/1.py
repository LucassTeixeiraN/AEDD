'''Uma pesquisa sequencial de uma lista ordenada pode ser interrompida quando o alvo
é menor que determinado elemento na lista. Defina uma versão modificada desse
algoritmo e indique a complexidade computacional, usando a notação big-O, do
desempenho nos casos melhor, pior e médio.'''
array = [1, 5, 2, 7, 3]
x = 3
array.sort()
for item in array:
     if x < item:
          
          break
     elif x == item:
          print("Element found")
          break
else:
     print("Element not found")
    
# Melhor caso: ocorre quando o valor de x é menor que o menor elemento da lista, nesse caso a complexidade de tempo é O(1) pois só precisa comparar x com o primeiro elemento
# Pior caso:  ocorre quando o valor de x é maior que o maior elemento da lista, nesse caso a complexidade de tempo é O(n) pois precisa comparar x com todos os elementos da lista
# Caso médio: ocorre quando o vlaor de x é igual a algum elemento da lista cujo index esteja pro meio da lista O(n/2)
