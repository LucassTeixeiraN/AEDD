'''Adicione o método rebalance a uma Árvore Binária de Busca. O método copia os itens
da árvore para uma lista durante um percurso em in-ordem e, em seguida, limpa a
árvore. O método então copia os itens da lista de volta para a árvore de tal maneira
que a forma da árvore permaneça balanceada. Dica: Use uma função auxiliar
recursiva que visite repetidamente os itens nos pontos médios das partes da lista.'''
from binaryTree import BinaryTree

def menu():
    option = -1
    
    while option < 0 or option > 14:
        print("\nBinary Search Tree")
        print("1. Insert")
        print("2. Search")
        print("3. Print In Order")
        print("4. Print Pre Order")
        print("5. Print Post Order")
        print("6. Min Node")
        print("7. Max Node")
        print("8. Height Tree")
        print("9. Count Nodes")
        print("10. Delete a Node")
        print("11. Clear Tree")
        print("12. Print Tree")
        print("13. Rebalance")
        print("14. Exit")
        option = int(input("Enter an option: "))
        if option < 0 or option > 14:
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
            tree.printInOrder(tree.root)
        elif option == 4:
            tree.printPreOrder(tree.root)
        elif option == 5:
            tree.printPostOrder(tree.root)
        elif option == 6:
            print(f'Min Node: {tree.minNode(tree.root)}')
        elif option == 7:
            print(f'Max Node: {tree.maxNode(tree.root)}')
        elif option == 8:
            print(f'Height Tree: {tree.heightTree(tree.root)}')
        elif option == 9:
            print(f'Count Nodes: {tree.countNodes(tree.root)}')
        elif option == 10:
            data = int(input("Enter data to delete: "))
            if tree.delete(tree.root, data):
                print("Data deleted")
            else:
                print("Data not found")
        elif option == 11:
            tree.deleteTree()
        elif option == 12:
            tree.printTree(tree.root)
        elif option == 13:
            tree.rebalance()
        elif option == 14:
            break
        
if __name__ == '__main__':
    main()