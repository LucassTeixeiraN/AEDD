from nodeTree import NodeTree

class BinaryTree():
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.root is None
    
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
    
    def copyIntoArray(self, node: NodeTree, items: list):
        if node is not None:
            items = self.copyIntoArray(node.left, items)
            items.append(node.data)
            items = self.copyIntoArray(node.right, items)
        return items
    
    def insertBalanced(self, items: list):
        middle = len(items) // 2
        start_array = items[:middle]
        end_array = items[middle + 1:]
        
        self.insert(self.root, items[middle])
        if len(start_array) > 0:
            self.insertBalanced(start_array)
        if len(end_array) > 0:
            self.insertBalanced(end_array)
        
        
    def rebalance(self):
        items = self.copyIntoArray(self.root, [])
        self.deleteTree()
        self.insertBalanced(items)
        
        
    def printInOrder(self, node: NodeTree):
        if self.isEmpty():
            print("Tree is empty")
        else:
            if node is not None:
                self.printInOrder(node.left)
                print(f'{node.data} ', end='')
                self.printInOrder(node.right)    
                
    def printPreOrder(self, node: NodeTree):
        if self.isEmpty():
            print("Tree is empty")
        else:
            if node is not None:
                print(f'{node.data} ', end='')
                self.printPreOrder(node.left)
                self.printPreOrder(node.right)
                
    def printPostOrder(self, node: NodeTree):
        if self.isEmpty():
            print("Tree is empty")
        else:
            if node is not None:
                self.printPostOrder(node.left)
                self.printPostOrder(node.right)
                print(f'{node.data} ', end='')
    
    def minNode(self, node: NodeTree):
        if not self.isEmpty():
            while node.left:
                node = node.left
            return node.data
        
    def maxNode(self, node: NodeTree):
        if not self.isEmpty():
            while node.right:
                node = node.right
            return node.data
        
    def heightTree(self, node: NodeTree):
        if node is None:
            return 0
        else:
            left_height = self.heightTree(node.left)
            right_height = self.heightTree(node.right)
            return max(left_height, right_height) + 1
        
    def countNodes(self, node: NodeTree):
        if node is None:
            return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)
    
    def _minValueRight(self, node: NodeTree):
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, node: NodeTree, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._minValueRight(node.right)
                node.data = successor.data
                node.right = self.delete(node.right, successor.data)
        return node
    
    def printTree(self, node: NodeTree, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + '->', node.data)
            self.printTree(node.left, level + 1)
    
    def deleteTree(self):
        self.root = None