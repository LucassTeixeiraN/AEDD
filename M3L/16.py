# 16. Crie um vetor que armazene dados de n casas numa imobiliária. Deverão ser
# considerados os dados: código, bairro, tamanho em m2

# , valor de venda e valor de
# aluguel. Elabore um programa que: preencha o vetor com os dados fornecidos pelo
# usuário e ordene de forma decrescente os elementos pelo campo de venda, usando o
# bubbleSort.

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    n = int(input("Quantas casas deseja cadastrar? "))
    casas = []

    for i in range(n):
        print(f"\nCadastro da casa {i + 1}:")
        codigo = input("Código: ")
        bairro = input("Bairro: ")
        tamanho_m2 = float(input("Tamanho (m²): "))
        valor_venda = float(input("Valor de venda: "))
        valor_aluguel = float(input("Valor de aluguel: "))
        
        
        casa = {
            "codigo": codigo,
            "bairro": bairro,
            "tamanho_m2": tamanho_m2,
            "valor_venda": valor_venda,
            "valor_aluguel": valor_aluguel
        }
        
        casas.append(casa)

    bubble_sort(casas, "valor_venda")

    print("\nCasas ordenadas pelo valor de venda (decrescente):")
    for casa in casas:
        print(casa)

main()
