# 13. Crie uma aplicação que implemente uma matriz quadrada com n números inteiros, os
# quais devem ser fornecidos aleatoriamente pelo usuário. Implemente um menu com
# duas opções:
# a. Colocar os elementos em ordem crescente (use o insertionSort).
# b. Colocar os elementos em ordem decrescente (use o selectionSort).



def matrizquad():
    matriz=[]
    while True:
        pass



def is_perfect_square(n):
    n = n ** 0.5
    if type(n) == int:
        return True 
    return False

is_perfect_square(len(matriz))
  

def insertion_sort( lista ):
  for i in range( 1, len( lista ) ):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave


def selection_sort(lista):
 
  n = len(lista) 

  if n == 1: 
    return lista[0] 


  for i in range(n-1):
    
    menor = i  


    for j in range(i + 1, n):
      if lista[j] < lista[menor]:
        menor = j

  
    if lista[i] != lista[menor]:
      aux = lista[i]
      lista[i] = lista[menor]
      lista[menor] = aux

  return 
