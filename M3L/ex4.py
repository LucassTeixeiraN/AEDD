'''Faça um programa que cadastre n produtos. Para cada produto devem ser
cadastrados os seguintes dados: código, descrição e preço. Use um método de
ordenação e em seguida calcule e mostre quantas comparações devem ser feitas
para encontrar um funcionário pelo código:
a. Usando busca sequencial.
b. Usando busca binária.'''
from faker import Faker
faker = Faker()

def registerFakeProduct():
    return [
        {
            'code': i + 1, 
            'description': faker.word(), 
            'price': faker.random_number(digits=2)
        } for i in range(50)
    ]

def registerProduct():
    products = []
    while True:
        try:
            code = int(input('Entre o código do produto: '))
            description = input('Entre a descrição do produto: ')
            price = float(input('Entre o preço do produto: '))
            products.append({'code': code, 'description': description, 'price': price})
            
            if input('Deseja continuar inserindo? (s/n)').lower().strip() == 'n':
                break
        except:
            print('Valor inválido. Tente novamente.')
            
    return products

def sequentialSearch(value, array):
    comparisons = 0
    for i in range(len(array)):
        comparisons += 1
        if array[i]['code'] == value:
            break
    return comparisons

def binarySearch(value, sorted_array):
    comparisons = 0
    left = 0
    right = len(sorted_array) - 1
    
    while left <= right:
        comparisons += 1
        mid_point = (left + right) // 2
        
        if sorted_array[mid_point]['code'] == value:
            break
        elif sorted_array[mid_point]['code'] < value:
            left = mid_point + 1
        else:
            right = mid_point - 1
            
    return comparisons

def main():
    if input('Deseja inserir os produtos manualmente? (s/n)').lower().strip() == 's':
        products = registerProduct()
        products.sort(key=lambda x: x['code'])
    else:
        products = registerFakeProduct()
    
    print(products, end='\n\n')
    
    value = int(input('Entre o código do produto a ser pesquisado: '))
    
    print('-' * 50)
    print('Número de comparações de uma busca sequencial: ', sequentialSearch(value, products))
    print('Número de comparações de uma busca binária: ', binarySearch(value, products))
    print('-' * 50)
    
main()