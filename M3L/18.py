'''18. Crie uma aplicação que permita inserir cerca de 8 mil números inteiros aleatórios de 1
a 8 mil num vetor de inteiros. Faça um comparativo considerando o número de trocas
realizadas entre os algoritmos selectionSort, mergeSort e quickSort. Comente as
diferenças e considere testar com números diferentes de elementos. Dica: quando
tiver rodando os algoritmos, evite executar outros programas na máquina.'''

import random

def generate_random_numbers(size, lower=1, upper=8000):
    return [random.randint(lower, upper) for _ in range(size)]

def selection_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return swaps

def merge_sort(arr):
    swaps = 0
    
    def merge(left_half, right_half):
        nonlocal swaps
        result = []
        i = j = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
                swaps += len(left_half) - i  # Count swaps for each element moved from the right
        result.extend(left_half[i:])
        result.extend(right_half[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = sort(arr[:mid])
        right_half = sort(arr[mid:])
        return merge(left_half, right_half)

    sorted_array = sort(arr)
    arr[:] = sorted_array  # Update original array
    return swaps

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    swaps = 0
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    if i + 1 != high:
        swaps += 1  # Count the swap of the pivot
    return i + 1, swaps

def quick_sort(arr, low, high):
    swaps = 0
    if low < high:
        pi, swap_count = partition(arr, low, high)
        swaps += swap_count
        swaps += quick_sort(arr, low, pi - 1)
        swaps += quick_sort(arr, pi + 1, high)
    return swaps

def test_sorting_algorithms(size):
    original_array = generate_random_numbers(size)

    # Test Selection Sort
    array_selection = original_array.copy()
    selection_swaps = selection_sort(array_selection)

    # Test Merge Sort
    array_merge = original_array.copy()
    merge_swaps = merge_sort(array_merge)

    # Test Quick Sort
    array_quick = original_array.copy()
    quick_swaps = quick_sort(array_quick, 0, len(array_quick) - 1)

    print(f"Tamanho do vetor: {size}")
    print(f"Selection Sort: Trocas: {selection_swaps}")
    print(f"Merge Sort: Trocas: {merge_swaps}")
    print(f"Quick Sort: Trocas: {quick_swaps}")
    print("-" * 50)

# Testando com diferentes tamanhos de vetor
for size in [1000, 2000, 4000, 8000]:
    test_sorting_algorithms(size)
