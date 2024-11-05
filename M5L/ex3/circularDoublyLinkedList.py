from node import Node

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def search_name(self, key):
        if self.head is None:
            return None
        current = self.head
        while True:
            if current.key == key:
                return current.name
            current = current.next
            if current == self.head:
                break
        return None

    def insert(self, key, name):
        new_node = Node(key, name)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head and current.next.key < key:
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            if current == self.head and key < self.head.key:
                self.head = new_node

    def remove(self, key):
        if self.head is None:
            return
        current = self.head
        while True:
            if current.key == key:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break

    def print_list(self):
        if self.head is None:
            print("Empty list.")
            return
        current = self.head
        while True:
            print(f"Key: {current.key}, Name: {current.name}")
            current = current.next
            if current == self.head:
                break

    def copy_list(self):
        new_list = CircularDoublyLinkedList()
        if self.head is None:
            return new_list
        current = self.head
        while True:
            new_list.insert(current.key, current.name)
            current = current.next
            if current == self.head:
                break
        return new_list

    def concatenate(self, other_list):
        if self.head is None:
            self.head = other_list.head
            return
        if other_list.head is None:
            return
        last_self = self.head.prev
        last_other = other_list.head.prev

        last_self.next = other_list.head
        other_list.head.prev = last_self

        last_other.next = self.head
        self.head.prev = last_other

    def interleave(self, other_list):
        new_list = CircularDoublyLinkedList()
        current1 = self.head
        current2 = other_list.head

        while current1 != self.head or current2 != other_list.head:
            if current1 != self.head:
                new_list.insert(current1.key, current1.name)
                current1 = current1.next
            if current2 != other_list.head:
                new_list.insert(current2.key, current2.name)
                current2 = current2.next

        return new_list