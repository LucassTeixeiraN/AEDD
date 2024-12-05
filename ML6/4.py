'''4. Apenas imprimindo linearmente os elementos da árvore não é possível reproduzir
sua estrutura. Faça um método imprimeRelacoes que percorra a árvore imprimindo
as relações entre os nós, de forma que se possa através dessa descrição reproduzir a
estrutura de uma árvore. Exemplos de descrições impressas são:
- o nó de valor XXX é filho esquerdo de YYY
- o nó de valor ZZZ é filho direito de YYY
- o nó de valor XXX não tem filho esquerdo
- o nó de valor ZZZ não tem filho direito'''

class NodeTree:
    def __init__(self, data):
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
                    
    def search(self, node: NodeTree, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)
        
    
    def printTree(self, node: NodeTree, level):
        if node is not None:
            self.printTree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.data)
            self.printTree(node.left, level + 1)

    def imprimeRelacoes(self, node: NodeTree):
        if node is None:
            return

        if node.left:
            print(f"o nó de valor {node.left.data} é filho esquerdo de {node.data}")
        else:
            print(f"o nó de valor {node.data} não tem filho esquerdo")
        
        self.imprimeRelacoes(node.left)

        if node.right:
            print(f"o nó de valor {node.right.data} é filho direito de {node.data}")
        else:
            print(f"o nó de valor {node.data} não tem filho direito")
        
        self.imprimeRelacoes(node.right)



def menu():
    print("1 – Inserir número")
    print("2 – Mostrar as relações dos nós")
    print("0 – Sair")

    return input("Escolha uma opção: ")


def main():
    tree = BinarySearchTree()

    while True:
        option = menu()

        if option == "1":
            number = int(input("Número: "))
            tree.insert(tree.root, number)
        elif option == "2":
            tree.imprimeRelacoes(tree.root)
        elif option == "0":
            break

main()