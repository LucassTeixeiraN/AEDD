from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reorder_letters_digits(self):
        letters = []
        digits = []

        current = self.head
        while current:
            if current.value.isdigit():
                digits.append(current.value)
            else:
                letters.append(current.value)
            current = current.next

        result = letters + digits[::-1]
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()