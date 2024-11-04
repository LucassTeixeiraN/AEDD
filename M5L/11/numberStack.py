from node import Node

class NumberStack:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if  self.head == None:
            return True
        return False
    
    def push(self, number):
        newNode = Node(number)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def pop(self):
        if self.isEmpty():
            print("A pilha está vazia")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
    
    def showStack(self):
        if self.isEmpty():
            print("A pilha está vazia")
        else:
            temp = self.head
            stackStr = ""
            while temp:
                stackStr += f"{temp.data} "
                temp = temp.next
            
            print("Pilha:")
            print(stackStr)