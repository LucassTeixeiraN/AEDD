class NodeTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'\nLeft: {self.left} | {self.data} | Right: {self.right}'