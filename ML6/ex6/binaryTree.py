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
    
    def isStrict(self, node: NodeTree) -> bool:
        if node is None:
            return True
        if (node.left is not None) ^ (node.right is not None):
            return False
        return self.isStrict(node.left) and self.isStrict(node.right)
    
    def isComplete(self, node: NodeTree) -> bool:
        if node is None:
            return True
        
        left_height = self.heightTree(node.left)
        right_height = self.heightTree(node.right)
        return (left_height == right_height) and self.isComplete(node.left) and self.isComplete(node.right)
        
    def isPerfect(self, node: NodeTree, level) -> bool:
        if node is None:
            return True
        if (node.left is None) and (node.right is None):
            return level == 1 # É folha
        if (node.left is None) or (node.right is None):
            return False
        
        return self.isPerfect(node.left, level - 1) and self.isPerfect(node.right, level - 1)
        
    def heightTree(self, node: NodeTree):
        if node is None:
            return 0
        else:
            left_height = self.heightTree(node.left)
            right_height = self.heightTree(node.right)
            return max(left_height, right_height) + 1
    
    def printTree(self, node: NodeTree, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + '->', node.data)
            self.printTree(node.left, level + 1)