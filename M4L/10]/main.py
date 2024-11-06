'''Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que
verifique se esta lista está em ordem crescente e outra função que faça uma busca na
lista, dado um elemento passado pelo usuário. Faça versões recursiva e iterativa.'''
from linkedList import LinkedList
def menu():
        print("\nMenu:")
        print("1. Inserir número")
        print("2. Imprimir lista")
        print("3. Verificar se está em ordem crescente")
        print("4. Buscar número (Iterativo)")
        print("5. Buscar número (Recursivo)")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")
        return opcao
    
def main():
    lista = LinkedList()
    while True:
        if input("Aperte ENTER para ir ao menu.") == '':
            opcao = menu()
            try:
                if opcao == '1':
                    valor = int(input("Digite um número inteiro: "))
                    lista.inserir(valor)
                elif opcao == '2':
                    lista.imprimir()
                elif opcao == '3':
                    if lista.verificar_ordem_crescente():
                        print("A lista está em ordem crescente.")
                    else:
                        print("A lista não está em ordem crescente.")
                elif opcao == '4':
                    valor = int(input("Digite o número a ser buscado: "))
                    if lista.buscar(valor):
                        print(f"O número {valor} foi encontrado na lista.")
                    else:
                        print(f"O número {valor} não foi encontrado na lista.")
                elif opcao == '5':
                    valor = int(input("Digite o número a ser buscado: "))
                    if lista.buscar_recursivo(valor):
                        print(f"O número {valor} foi encontrado na lista.")
                    else:
                        print(f"O número {valor} não foi encontrado na lista.")
                elif opcao == '6':
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Valor inválido.")
main()
                     

