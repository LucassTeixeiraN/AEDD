from node import Node

class DoublyCircularLinkedOrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            current = self.head
            while True:
                if new_data['salary'] < current.data['salary']:
                    new_node.previous = current.previous
                    new_node.next = current
                    current.previous.next = new_node
                    current.previous = new_node

                    if current == self.head:
                        self.head = new_node
                    break

                elif current.next == self.head:
                    current.next = new_node
                    new_node.previous = current
                    new_node.next = self.head
                    self.head.previous = new_node
                    break
                current = current.next

    def delete(self, data):
        if self.isEmpty():
            print("List is empty!!")
            return
        
        current = self.head
        while True:
            if current.data == data:
                if current == self.head and current.next == self.head:
                    self.head = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break
        
        print("Element not found in the list!")

    def searchNode(self, data):
        if self.isEmpty():
            print("Empty list.")
            return None
        
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def display(self):
        if self.isEmpty():
            print("List is empty!!")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()
