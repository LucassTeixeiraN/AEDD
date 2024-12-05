'''12. Adicione um método rangeFind a uma Árvore Binária de Busca. Esse método espera
dois itens como argumentos que especificam os limites de um intervalo dos itens a
serem encontrados na árvore. O método percorre a árvore e constrói e retorna uma
lista ordenada dos itens encontrados dentro do intervalo especificado.'''

class NodeTree:
    def __init__(self, data, ):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def insert(self, node: NodeTree, data):
        if self.isEmpty():
            self.root = NodeTree(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            if data > node.data:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)
                    
    def _minValueRight(self, node: NodeTree):
        current = node
        while current.left is not None:
            current = current.left
            return current

    def delete(self, node: NodeTree, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            # Case 1: The node to be deleted has no children (leaf node)
            if node.left is None and node.right is None:
                return None
            # Case 2: The node to be deleted has only one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: The node to be deleted has two children
            else:
                # Find the node with the minimum value in the right subtree
                successor = self._minValueRight(node.right)
                node.data = successor.data
                # Delete successor
                node.right = self.delete(node.right, successor.data)
        return None  
    
    def printTree(self, node: NodeTree, level):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level + 1)

    def rangeFind(self, low, high):

        result = []
        self.rangeFindAux(self.root, low, high, result)
        return result

    def rangeFindAux(self, node, low, high, result):
        if node is None:
            return

        if low <= node.data <= high:
            result.append(node.data)

        if low < node.data:
            self.rangeFindAux(node.left, low, high, result)

        if high > node.data:
            self.rangeFindAux(node.right, low, high, result)
    
def menu():
    print("1 – Inserir nó")
    print("2 – Remover nó")
    print("3 – Imprimir árvore")
    print("4 – Imprimir os números de um intervalo")
    print("0 – Sair")

    return input("Escolha uma opção: ")


def main():
    tree = BinarySearchTree()

    while True:
        option = menu()

        if option == "1":
            data = int(input("Número: "))
            tree.insert(tree.root, data)
        elif option == "2":
            data = int(input("Número: "))
            tree.delete(tree.root, data)
        elif option == "3":
            tree.printTree(tree.root, 0)
        elif option == "4":
            low = int(input("Insira o menor valor do intervalo: "))
            high = int(input("Insira o maior valor do intervalo: "))
            print(tree.rangeFind(low, high))
        elif option == "0":
            break

main()