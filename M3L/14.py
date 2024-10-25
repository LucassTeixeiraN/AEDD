# 14. Elabore um programa que armazene os seguintes dados de n pessoas: nome, idade e
# sexo. O programa deve apresentar os dados em:
# a. Ordem crescente alfabética de nome (use o quickSort).
# # b. Ordem decrescente de idade (use o bubbleSort).

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]
    left = [x for x in arr if x[key] > pivot] 
    middle = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] < pivot]  
    return quick_sort(left, key) + middle + quick_sort(right, key)


def main():
    n = int(input("Quantas pessoas deseja cadastrar? "))
    pessoas = []

    for i in range(n):
        print(f"\nCadastro da pessoa {i + 1}:")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo: ")
        
        pessoa = {
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
        }
        
        pessoas.append(pessoa)

    print("\nPessoas cadastradas:", pessoas)

    print("\nOrdenando por idade usando Bubble Sort:")
    bubble_sort(pessoas, "idade")
    print(pessoas)

    print("\nOrdenando por nome (ordem alfabética) usando Quick Sort:")
    pessoas = quick_sort(pessoas, "nome")
    print(pessoas)

main()
