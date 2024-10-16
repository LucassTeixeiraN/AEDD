'''Faça um programa que cadastre o nome e o salário de n funcionários. Usando um
método de ordenação diferente para cada item a seguir, liste todos os dados dos
funcionários das seguintes formas:
a. Em ordem crescente de salário;
b. Em ordem decrescente de salário;
c. Em ordem alfabética.'''
from faker import Faker
faker = Faker()

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, start, end):
    middle = (start + end) // 2
    pivot = array[middle]
    array[middle] = array[end]
    array[end] = pivot
    boundary = start
    
    for index in range(start, end):
        if array[index]['name'] < pivot['name']:
            swap(array, boundary, index)
            boundary += 1
    swap(array, boundary, end)
    return boundary

def selectionSort(array):
    i = 0
    while i < len(array):
        minIndex = i
        j = i + 1
        while j < len(array):
            if array[j]['salary'] < array[minIndex]['salary']:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(array, i, minIndex)
        i += 1
    
def bubbleSort(array):
    n = len(array)
    while n > 1:
        i = 1
        swapped = False
        while i < n:
            if array[i]['salary'] > array[i - 1]['salary']:
                swap(array, i, i - 1)
                swapped = True
            i += 1
        if not swapped:
            return
        n -= 1
        
def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)
        
def main():
    employees = []
    for i in range(20):
        employees.append({'name': faker.name(), 'salary': faker.random_number(digits=4)})
    
    print('Em ordem crescente de salário:')
    selectionSort(employees)
    for employee in employees:
        print(employee)
    
    print('\nEm ordem decrescente de salário:')
    bubbleSort(employees)
    for employee in employees:
        print(employee)
    
    print('\nEm ordem alfabética:')
    quickSort(employees, 0, len(employees) - 1)
    for employee in employees:
        print(employee)
        
main()