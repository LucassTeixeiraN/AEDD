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

    def index(self, item: Node):
        index = 0
        temp = self.head
        while temp:
            if temp.data == item.data:
                return index
            temp = temp.next
            index += 1
    
    def clear(self):
        if self.isEmpty():
            print("Empty list.")
        else:
            self.head = None
            
    @property    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count



def pop(key, linked_list):
    temp = linked_list.head
    prev = None
    
    while temp is not None:
        if linked_list.index(temp) == key:
            if prev is None:
                linked_list.head = temp.next
            else:
                prev.next = temp.next
            return (linked_list, temp)
        prev = temp
        temp = temp.next