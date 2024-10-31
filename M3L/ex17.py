'''Crie uma aplicação que permita inserir cerca de 10 mil números inteiros aleatórios de
1 a 10 mil num vetor de inteiros. Registre o tempo de início e término da operação de
ordenação e compare essas diferenças entre os algoritmos bubbleSort, insertionSort
e quickSort. Comente as diferenças e considere testar com números diferentes de
elementos. Dica: quando tiver rodando os algoritmos, evite executar outros
programas na máquina.'''
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Função para medir o tempo de execução
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

def main():
    n = 10000
    random_numbers = [random.randint(1, 10000) for _ in range(n)]
    
    bubble_time = measure_time(bubble_sort, random_numbers)
    print(f"Tempo de execução do Bubble Sort: {bubble_time:.6f} segundos")
    
    insertion_time = measure_time(insertion_sort, random_numbers)
    print(f"Tempo de execução do Insertion Sort: {insertion_time:.6f} segundos")
    
    quick_time = measure_time(quick_sort, random_numbers)
    print(f"Tempo de execução do Quick Sort: {quick_time:.6f} segundos")

main()