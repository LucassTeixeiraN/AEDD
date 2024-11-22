'''Faça um programa para executar as operações abaixo em uma árvore binária.
1 – Inserir número
2 – Mostrar se a arvore é estritamente binária
3 – Mostrar se a arvore é completa
4 – Mostrar se a arvore é cheia
5 – Sair

Árvore estritamente binária: Cada nó possui exatamente 0 ou 2 filhos. 
Árvore binária completa: Nós com menos de 2 filhos ficam no úlimo ou no penúltimo nível da árvore. 
Árvore binária cheia: Nós com menos de 2 filhos ficam no último nível da árvore.'''

from binaryTree import BinaryTree

def menu():
    option = -1
    
    while option < 0 or option > 7:
        print("\nBinary Search Tree")
        print("1. Insert")
        print("2. Search")
        print("3. Verificar se árvore é estritamente binária")
        print("4. Verificar se árvore é completa")
        print("5. Verificar se árvore é cheia")
        print("6. Print Tree")
        print("7. Exit")
        option = int(input("Enter an option: "))
        if option < 0 or option > 7:
            print("Invalid option")
    
    return option

def main():
    tree = BinaryTree()
    
    while True:
        option = menu()
        
        if option == 1:
            data = int(input("Enter data: "))
            tree.insert(tree.root, data)
        elif option == 2:
            data = int(input("Enter data to search: "))
            if tree.search(tree.root, data):
                print("Data found")
            else:
                print("Data not found")
        elif option == 3:
            if tree.isStrict(tree.root):
                print('A árvore é estritamente binária!')
            else:
                print('A árvore não é estritamente binária!')
        elif option == 4:
            if tree.isComplete(tree.root):
                print('A árvore é completa!')
            else:
                print('A árvore não é completa!')
        elif option == 5:
            if tree.isPerfect(tree.root, tree.heightTree(tree.root)):
                print('A árvore é cheia!')
            else:
                print('A árvore não é cheia!')
        elif option == 6:
            tree.printTree(tree.root)
        elif option == 7:
            break
        
if __name__ == '__main__':
    main()