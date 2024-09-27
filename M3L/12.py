import random

def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    esquerda = mergesort(lista[:mid])
    direita = mergesort(lista[mid:])

    return merge(esquerda, direita)

def merge(lista1, lista2):
    resultado = []
    i = j = 0
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    
    return resultado
def main():
    lista1 = [random.randint(1, 100) for _ in range(20)]
    lista2 = [random.randint(1, 100) for _ in range(20)]

    lista_combinada = lista1 + lista2

    lista_ordenada = mergesort(lista_combinada)

    print(lista_ordenada)
main()
