'''9. Crie uma árvore binária ordenada para implementar um dicionário da língua inglesa.
Cada nó precisa ter a palavra e o seu significado. Implemente as funções básicas
para inserção, remoção, pesquisa e impressão do dicionário.'''

class NodeTree:
    def __init__(self, eng, pt):
        self.eng = eng
        self.pt = pt
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def insert(self, node: NodeTree, eng, pt):
        if self.isEmpty():
            self.root = NodeTree(eng, pt)
        else:
            if eng < node.eng:
                if node.left is None:
                    node.left = NodeTree(eng, pt)
                else:
                    self.insert(node.left, eng, pt)
            if eng > node.eng:
                if node.right is None:
                    node.right = NodeTree(eng, pt)
                else:
                    self.insert(node.right, eng, pt)
                    
    def search(self, node: NodeTree, data):
        if node is None or node.eng == data:
            return node
        if data < node.eng:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
    
    def _minValueRight(self, node: NodeTree):
        current = node
        while current.left is not None:
            current = current.left
            return current

    def delete(self, node: NodeTree, data):
        if node is None:
            return None
        
        if data < node.eng:
            node.left = self.delete(node.left, data)
        elif data > node.eng:
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
                node.eng = successor.eng
                # Delete successor
                node.right = self.delete(node.right, successor.eng)
        return None  
    
    def printTree(self, node: NodeTree, level, space):
        if node is not None:
            self.printTree(node.right, level + 1, len(node.eng) + len(node.pt))
            print(' ' * space * level + '->', node.eng, ":", node.pt)
            self.printTree(node.left, level + 1, len(node.eng) + len(node.pt))
    
def menu():
    print("1 – Inserir palavra")
    print("2 – Remover palavra")
    print("3 – Pesquisar palavra")
    print("4 – Imprimir dicionário")
    print("0 – Sair")

    return input("Escolha uma opção: ")


def main():
    tree = BinarySearchTree()

    while True:
        option = menu()

        if option == "1":
            english = input("Inglês: ")
            portuguese = input("Português: ")
            tree.insert(tree.root, english, portuguese)
        elif option == "2":
            word = input("Insira a palavra: ")
            tree.delete(tree.root, word)
        elif option == "3":
            word = input("Insira a palavra: ")
            node = tree.search(tree.root, word)
            if node:
                print(f"{node.eng}: {node.pt}")
            else:
                print("Essa palavra não existe no dicionário")
        elif option == "4":
            tree.printTree(tree.root, 0, 0)
        elif option == "0":
            break

main()