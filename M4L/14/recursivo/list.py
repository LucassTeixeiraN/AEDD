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
            newNode.prev = self.tail
            self.tail = newNode

    @staticmethod
    def verifyPosition(curPos, pos):
        return curPos < pos - 1

    @staticmethod
    def firstPosition(pos):
        return pos == 0


    def listChanger(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node     
        self.head = prev              

    def showList(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ")
                temp = temp.next