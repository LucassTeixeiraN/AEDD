'''
Faça um programa para executar as operações abaixo em uma árvore binária.
1 - Inserir número
2 - Mostrar nós folha
3 - Mostrar os nós ancestrais de um nó
4 - Mostrar os descendentes de um nó
5 - Mostrar o nó pai e os nós filhos de um nó
6 - Sair'''
from binarySearchTree import BinarySearchTree

def menu():
    print("\nEscolha uma operação:")
    print("1 - Inserir número")
    print("2 - Mostrar nós folha")
    print("3 - Mostrar os nós ancestrais de um nó")
    print("4 - Mostrar os descendentes de um nó")
    print("5 - Mostrar o nó pai e os nós filhos de um nó")
    print("6 - Mostrar arvore")
    print("7 - Sair")
    return input("Escolha: ")

def main():
    tree = BinarySearchTree()
    while True:
        choice = menu()
        
        if choice == '1':
            num = int(input("Digite um número para inserir na árvore: "))
            tree.insert(tree.root, num)
        
        elif choice == '2':
            print("Nós folha: ", end="")
            tree.showLeaves(tree.root)
            print()
        
        elif choice == '3':
            num = int(input("Digite o número do nó para mostrar os ancestrais: "))
            ancestors = tree.findAncestors(tree.root, num)
            if ancestors:
                print("Ancestrais: ", ancestors)
            else:
                print("Nó não encontrado.")
        
        elif choice == '4':
            num = int(input("Digite o número do nó para mostrar os descendentes: "))
            print("Descendentes: ", end="")
            tree.findDescendants(tree.root, num)
            print()
        
        elif choice == '5':
            num = int(input("Digite o número do nó para mostrar pai e filhos: "))
            tree.showParentAndChildren(tree.root, num)

        elif choice == '6':
            tree.printTree(tree.root)
        
        elif choice == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()