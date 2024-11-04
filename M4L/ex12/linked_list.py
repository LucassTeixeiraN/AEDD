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
            
    def pop(self, key):
        temp = self.head
        prev = None
        
        while temp is not None:
            if self.index(temp) == key:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return (self, temp)
            prev = temp
            temp = temp.next
            
    @property    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count
    
def iterativeCopy(linked_list: LinkedList):
    new_linked_list = LinkedList()
    temp = linked_list.head
    while temp:
        new_linked_list.append(temp.data)
        temp = temp.next
    return new_linked_list

def copy(node):
    if node is None:
        return None
    new_node = Node(node.data)
    new_node.next = copy(node.next)
    return new_node

def recursiveCopy(linked_list: LinkedList):
    new_linked_list = LinkedList()
    new_linked_list.head = copy(linked_list.head)
    return new_linked_list

def iterativeConcatenate(linked_list1: LinkedList, linked_list2: LinkedList):
    new_linked_list = LinkedList()
    temp = linked_list1.head
    while temp:
        new_linked_list.append(temp.data)
        temp = temp.next
    temp = linked_list2.head
    while temp:
        new_linked_list.append(temp.data)
        temp = temp.next
    return new_linked_list

def get_tail(node):
    if node.next is None:
        return node
    return get_tail(node.next)

def recursiveConcatenate(linked_list1: LinkedList, linked_list2: LinkedList):
    new_linked_list = LinkedList()
    new_linked_list.head = copy(linked_list1.head)
    
    tail = get_tail(new_linked_list.head)
    tail.next = copy(linked_list2.head)
    
    return new_linked_list
    