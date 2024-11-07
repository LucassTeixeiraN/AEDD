from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if not self.head or not self.head.next:
            return
        
        sorted_list = LinkedList()
        current = self.head
        
        while current:
            sorted_list.sorted_insert(current.data)
            current = current.next
        
        self.head = sorted_list.head

    def sorted_insert(self, new_data):
        new_node = Node(new_data)
        
        if not self.head or self.head.data >= new_data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        if not other.head:
            return
        
        merged_list = LinkedList()
        current1 = self.head
        current2 = other.head
        
        while current1 and current2:
            if current1.data < current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next
        
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next
        
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next
        
        self.head = merged_list.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")