
# 13. Crie uma aplicação que implemente uma matriz quadrada com n números inteiros, os
# quais devem ser fornecidos aleatoriamente pelo usuário. Implemente um menu com
# duas opções:
# a. Colocar os elementos em ordem crescente (use o insertionSort).
# b. Colocar os elementos em ordem decrescente (use o selectionSort).


def matrizquad():
    import math
   
    def is_perfect_square(n):
        return math.isqrt(n) ** 2 == n
    
    def insertion_sort(lista):
        for i in range(1, len(lista)):
            chave = lista[i]
            k = i
            while k > 0 and chave < lista[k - 1]:
                lista[k] = lista[k - 1]
                k -= 1
            lista[k] = chave

   
    def selection_sort(lista):
        n = len(lista)
        for i in range(n):
            menor = i
            for j in range(i + 1, n):
                if lista[j] < lista[menor]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]
        return lista

    
    while True:
        n = int(input("Informe a quantidade de elementos (deve ser um quadrado perfeito): "))
        if is_perfect_square(n):
            break
        else:
            print("Por favor, insira um número que seja um quadrado perfeito.")

  
    matriz = []
    for i in range(n):
        num = int(input(f"Digite o elemento {i + 1}: "))
        matriz.append(num)

    while True:
        print("\nMenu:")
        print("1. Ordenar elementos em ordem crescente (Insertion Sort)")
        print("2. Ordenar elementos em ordem decrescente (Selection Sort)")
        print("3. Sair")

        escolha = input("Escolha uma opção (1/2/3): ")

        if escolha == '1':
            insertion_sort(matriz)
            print("Matriz em ordem crescente:", matriz)
        elif escolha == '2':
            selection_sort(matriz)
            matriz.sort(reverse=True) 
            print("Matriz em ordem decrescente:", matriz)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

matrizquad()
