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


    def listChanger(self, length):
        currentPosition = 1
        temp = self.head
        reverseTemp = self.tail
        while currentPosition < length // 2 and temp and reverseTemp:

            if temp.next == reverseTemp:
                temp.next = None
                reverseTemp.prev = None
                reverseTemp.next = temp
                temp.prev = reverseTemp
                self.head = reverseTemp  
                self.tail = temp 
                break
            else:
               
                temp.next.prev = reverseTemp 
                reverseTemp.prev.next = temp  

              
                temp.prev, reverseTemp.prev = reverseTemp.prev, temp.prev
                temp.next, reverseTemp.next = reverseTemp.next, temp.next
                
                if temp.next:
                    temp.next.prev = temp  
                if reverseTemp.next:
                    reverseTemp.next.prev = reverseTemp  

            
            temp = temp.next
            reverseTemp = reverseTemp.prev
            currentPosition += 1

    def showList(self):
        if self.isEmpty():
            print("Lista vazia")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ")
                temp = temp.next