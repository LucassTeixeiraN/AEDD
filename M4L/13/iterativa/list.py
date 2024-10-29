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

    @staticmethod
    def verifyPosition(curPos, pos):
        return curPos < pos - 1

    @staticmethod
    def firstPosition(pos):
        return pos == 0

    def insertElement(self, newData, pos):
        newNode = Node(newData)
        
        if self.firstPosition(pos):
            newNode.next = self.head
            self.head = newNode
            return

        temp = self.head
        currentPosition = 0
        
        while temp and self.verifyPosition(currentPosition, pos):
            temp = temp.next
            currentPosition += 1

        if temp is not None:
            newNode.next = temp.next
            temp.next = newNode
        else:
            print("Posição fora do alcance da lista.")

    def findPosition(self, temp, pos, num):
        currentPosition = 0
        while temp and self.verifyPosition(currentPosition, pos):
            temp = temp.next
            currentPosition += 1

        if temp is not None:
            return temp.next
        else:
            print(f"Posição do {num} elemento está fora do alcance da lista.")
            return None
    
    def changeElements(self, pos1, pos2):
        if self.firstPosition(pos1):
            data1 = self.head.data
            next1 = self.head.next

        if self.firstPosition(pos2):
            data2 = self.head.data
            next2 = self.head.next
        
        temp1 = temp2 = self.head
        
        next1 = self.findPosition(self, temp1, pos1, "primeiro")
        next2 = self.findPosition(self, temp2, pos2, "segundo")

        if data1 and data2:
            aux = next1
            next1 = next2
            next2 = aux


    def showList(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ")
                temp = temp.next