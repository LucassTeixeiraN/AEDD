from node import Node

class NumberQueue:
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
            print("A fila está vazia")
            
        else:
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult
    
    def showqueue(self, type):
        if self.isEmpty():
            print(f"A fila de {type} está vazia")
        else:
            
            temp = self.head
            queueStr = ""
            while temp:
                queueStr += f"{temp.data} "
                temp = temp.next
            
            print(f"Fila de {type}:")
            print(queueStr)