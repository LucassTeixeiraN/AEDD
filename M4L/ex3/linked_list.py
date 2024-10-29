from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the LinkedList.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printList(self):
        if self.isEmpty():
            print("Empty list.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def searchNode(self, data):
        if self.isEmpty():
            print("Empty list.")
            return None
        
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def pop(self, key):
        if self.isEmpty():
            print("Empty list.")
            return

        temp = self.head
        prev = None
        
        while temp is not None:
            if temp.data == key:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return (self.head, temp)
            prev = temp
            temp = temp.next

    def clear(self):
        if self.isEmpty():
            print("Empty list.")
        else:
            self.head = None
