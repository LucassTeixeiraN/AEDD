'''Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar todos
3 – Mostrar a sub-árvore direita de um nó
4 – Mostrar a sub-árvore esquerda de um nó
5 – Sair'''
from arvoreBinaria import ArvoreBinaria
def menu():
    print("\nMenu:")
    print("1 – Inserir número")
    print("2 – Mostrar todos")
    print("3 – Mostrar a sub-árvore direita de um nó")
    print("4 – Mostrar a sub-árvore esquerda de um nó")
    print("5 – Sair")

def main():
    arvore = ArvoreBinaria()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        try:
            if opcao == "1":
                valor = int(input("Digite o número para inserir: "))
                arvore.inserir(valor)
            elif opcao == "2":
                print("Todos os números na árvore:")
                arvore.mostrar_todos()
            elif opcao == "3":
                valor = int(input("Digite o valor do nó para exibir a sub-árvore direita: "))
                arvore.mostrar_subarvore_direita(valor)
            elif opcao == "4":
                valor = int(input("Digite o valor do nó para exibir a sub-árvore esquerda: "))
                arvore.mostrar_subarvore_esquerda(valor)
            elif opcao == "5":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Valores inválidos.")
if __name__ == "__main__":
    main()
