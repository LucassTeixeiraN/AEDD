'''Crie um vetor que armazene dados de n funcionários de uma empresa. Deverão ser
considerados os dados: código funcional, nome, salário e data de admissão. Elabore
um programa que: preencha o vetor com os dados fornecidos pelo usuário e ordene
de forma crescente os elementos pelo campo de código funcional, usando o
quickSort.'''
class Funcionario:
    def __init__(self, codigo, nome, salario, dataADM):
        self.codigo = codigo
        self.nome = nome
        self.salario = salario
        self.dataADM = dataADM

    def __str__(self):
        return f"Funcionario (codigo={self.codigo}, nome = {self.nome}, salario = {self.salario}, dataADM = {self.dataADM})"

def quicksort(funcionarios, low, high):
    if low < high:
        pi = partition(funcionarios, low, high)
        quicksort(funcionarios, low, pi - 1)
        quicksort(funcionarios, pi + 1, high)

def partition(funcionarios, low, high):
    pivot = funcionarios[high].codigo
    i = low - 1
    for j in range(low, high):
        if funcionarios[j].codigo <= pivot:
            i += 1
            funcionarios[i], funcionarios[j] = funcionarios[j], funcionarios[i]
    funcionarios[i + 1], funcionarios[high] = funcionarios[high], funcionarios[i + 1]
    return i + 1

def coletarDados(n):
    funcionarios = []
    while n > 0:
        try:
            codigo = int(input("Informe o código funcional: "))
            nome = input("Informe o nome: ")
            salario = float(input("Informe o salário: "))
            dataADM = input("Informe a data de admissão (DD/MM/AAAA): ")
            funcionario = Funcionario(codigo, nome, salario, dataADM)
            funcionarios.append(funcionario)
            n -= 1
        except ValueError:
            print("Dados invalidos.")
            continue
    return funcionarios

def main():
    n = int(input("Informe o número de funcionários: "))
    
    funcionarios = coletarDados(n)

    print("\nFuncionários antes da ordenação:")
    for f in funcionarios:
        print(f)

    quicksort(funcionarios, 0, len(funcionarios) - 1)

    print("\nFuncionários após a ordenação por código funcional:")
    for f in funcionarios:
        print(f)

main()