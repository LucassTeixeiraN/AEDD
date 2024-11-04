'''Faça um programa que cadastre o nome e o salário de n funcionários em uma lista
duplamente encadeada e ordenada pelo salário de forma crescente. A seguir, o
programa deve mostrar o nome, o valor do imposto e o valor a receber, ou seja, o
salário menos o imposto de todos os funcionários cadastrados. Posteriormente, o
programa deve mostrar os nomes e os salários dos funcionários cujos nomes
comecem por uma letra digitada pelo usuário (considera a possibilidade de letras
maiúsculas e minúsculas). Se nenhum funcionário tem o nome começado com a letra
digitada pelo usuário, mostrar mensagem. Finalmente, o programa deve apresentar
duas listagens:

a. Dos nomes e salários dos funcionários por ordem crescente de salário;
b. Dos nomes e salários dos funcionários por ordem decrescente de salário.
Observação: os percentuais de imposto seguem a tabela abaixo:

Valor do salário    | Percentual do imposto
Até 850             | Isento
Entre 850 e 1200    | 10% do salário
De 1200 para cima   | 20% do salário'''
from doublyCircularLinkedOrdered import DoublyCircularLinkedOrderedList

def main():
    ordered_list = DoublyCircularLinkedOrderedList()

    while True:
        try:
            name = input("Digite o nome: ")
            salary = float(input("Digite o salário: "))
            ordered_list.insert({"name": name, "salary": salary})
            
            if input("Deseja continuar? (s/n): ").lower().strip() == "n":
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    print('Salários e impostos:')
    ordered_list.display()
    
    print('Pesquisa pela letra inicial do nome')
    ordered_list.searchNode(input("Digite a letra inicial do nome: "))
    
    print('\nFuncionarios ordenados pelo salário (crescente):')
    ordered_list.display(False)
    
    print('\nFuncionarios ordenados pelo salário (decrescente):')
    ordered_list.displayReverse(False)

if __name__ == "__main__":
    main()
