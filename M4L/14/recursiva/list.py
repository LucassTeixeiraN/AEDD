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

    def findPosition(self, temp, pos, currentPosition = 0):
        
        if temp and self.verifyPosition(currentPosition, pos):
          return self.findPosition(temp.next, pos, currentPosition + 1)
      
        if temp is not None:
            return temp
        else:
            print(f"Posição {pos} está fora do alcance da lista.")
            return None
    
    def changeElements(self, pos1, pos2):
        if pos1 < 0 or pos2 < 0:
            print("Posições devem ser não negativas.")
            return

        node1 = self.findPosition(self.head, pos1)
        node2 = self.findPosition(self.head, pos2)

        if node1 and node2:
            node1.data, node2.data = node2.data, node1.data
        else:
            print("Não foi possível trocar os elementos.")


    def showList(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ")
                temp = temp.next