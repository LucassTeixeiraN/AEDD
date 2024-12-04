from nodeTree import NodeTree

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
    def printTree(self, node: NodeTree, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + '->', node.data)
            self.printTree(node.left, level + 1)

    def insert(self, node: NodeTree, data):
        new_node = NodeTree(data)
        if self.isEmpty():
            self.root = new_node
        else:
            if data < node.data:
                if node.left is None:
                    node.left = new_node
                else:
                    self.insert(node.left, data)
            if data > node.data:
                if node.right is None:
                    node.right = new_node
                else:
                    self.insert(node.right, data)
                    
    def search(self, node: NodeTree, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def showLeaves(self, node: NodeTree):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(f'{node.data} ', end='')
        self.showLeaves(node.left)
        self.showLeaves(node.right)
    
    def findAncestors(self, node: NodeTree, data, ancestors=[]):
        if node is None:
            return None
        if node.data == data:
            return ancestors
        ancestors.append(node.data)
        if data < node.data:
            return self.findAncestors(node.left, data, ancestors)
        else:
            return self.findAncestors(node.right, data, ancestors)
    
    def findDescendants(self, node: NodeTree, data):
        target_node = self.search(node, data)
        if target_node:
            self._printDescendants(target_node)
    
    def _printDescendants(self, node: NodeTree):
        if node is None:
            return
        print(f'{node.data} ', end='')
        self._printDescendants(node.left)
        self._printDescendants(node.right)
    
    def showParentAndChildren(self, node: NodeTree, data):
        target_node = self.search(node, data)
        if target_node is None:
            print("Node not found")
            return
        
        parent = self.searchParent(self.root, target_node)
        print(f"Nó pai: {parent.data if parent else 'None'}")
        print("Filhos do nó:")
        if target_node.left: 
            print(f"Esquerda: {target_node.left.data}", end=" ")
        if target_node.right: 
            print(f"Direita: {target_node.right.data}", end=" ")
        print()
            

    def searchParent(self, node: NodeTree, target_node: NodeTree):
        if node is None or (node.left == target_node or node.right == target_node):
            return node
        elif target_node.data < node.data:
            return self.searchParent(node.left, target_node)
        else:
            return self.searchParent(node.right, target_node)