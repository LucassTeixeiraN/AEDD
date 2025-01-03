from node import Node

class DoublyCircularLinkedUnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_front(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.previous = self.head.previous
            self.head.previous.next = new_node
            self.head.previous = new_node
            self.head = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            new_node.next = current.next
            new_node.previous = current
            current.next.previous = new_node
            current.next = new_node

    def insert_after(self, previous, new_data):
        if previous is None:
            print("The given previous node must be in the list.")
            return

        new_node = Node(new_data)
        new_node.next = previous.next
        previous.next = new_node
        new_node.next.previous = new_node
        new_node.previous = previous

    def delete_front(self):
        if self.isEmpty():
            print("List is empty!!")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head.next
            current.previous = self.head.previous
            self.head.previous.next = current
            self.head = None
            self.head = current

    def delete_end(self):
        if self.isEmpty():
            print("List is empty!!")
        elif self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.previous.next = current.next
            current.next.previous = current.previous
            current = None

    def delete_mid(self, data):
        if self.isEmpty():
            print("List is empty!!!")
        else:
            if self.head.data == data:
                self.delete_front()
            else:
                current = self.head.next
                while current.data != data:
                    if current == self.head:
                        print("Entered element not found in the list!!")
                        return
                    current = current.next

                current.previous.next = current.next
                current.next.previous = current.previous
                current = None

    def searchNode(self, data):
        if self.isEmpty():
            print("Empty list.")
        else:
            temp = self.head

            while temp:
                if temp.data == data:
                    return temp
                temp = temp.next
                if temp == self.head:
                    return None
            return None

    def display(self):
        if self.isEmpty():
            print("List is empty!!")
            return

        current = self.head.next
        if current is None:
            print("List is empty!!")
        else:
            print(self.head.data, end=" ")
            while current != self.head:
                print(current.data, end=" ")
                current = current.next
        print()
