from node import Node

class List:

    def __init__(self):
        self.tail = None
        self.head= None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def appendElement(self, newData):
        newNode = Node(newData) 

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def showList(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            temp = self.head
            while temp:
                print(temp.data+ " ")
                temp = temp.next