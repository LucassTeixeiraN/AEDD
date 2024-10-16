'''Faça um programa que cadastre n números, não permitindo números repetidos.
Ordene-os e, em seguida, verifique se o número digitado pelo usuário está no vetor.
Caso encontre, verifique se está numa posição par ou ímpar do vetor:
a. Usando busca sequencial.
b. Usando busca binária.'''

def registerNumbers():
    numbers = []
    while True:
        try:
            number = int(input('Entre com um número: '))
            if number not in numbers:
                numbers.append(number)
            else:
                print('Número repetido. Tente novamente.')
                
            if input('Deseja continuar inserindo? (s/n)').lower().strip() == 'n':
                break
        except:
            print('Valor inválido. Tente novamente.')
        
    numbers.sort()
    return numbers

def sequentialSearch(value, array):
    comparisons = 0
    for i in range(len(array)):
        comparisons += 1
        if array[i] == value:
            return 'Par' if i % 2 == 0 else 'Ímpar'
    return 'Item não encontrado.'

def binarySearch(value, sorted_array):
    comparisons = 0
    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        comparisons += 1
        mid_point = (left + right) // 2
        
        if sorted_array[mid_point] == value:
            return 'Par' if mid_point % 2 == 0 else 'Ímpar'
        elif sorted_array[mid_point] < value:
            left = mid_point + 1
        else:
            right = mid_point - 1
            
    return 'Item não encontrado.'

def main():
    numbers = registerNumbers()
    print(numbers)
    
    value = int(input('Entre com um número para buscar: '))
    print('Resultado da busca sequencial: ',sequentialSearch(value, numbers))
    print('Resultado da busca binária: ', binarySearch(value, numbers))
    
main()