from node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def push(self, new_data):
        new_node = Node(new_data)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        if self.is_empty():
            print('Empty stack.')
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
            
    def pop(self):
        if not self.is_empty():
            self.head = self.head.next
            
    def clear(self):
        self.head = None


def show_even_numbers(stack: Stack):
    if stack.is_empty():
        print('Empty stack.')
    else:
        current = stack.head
        while current:
            if current.data % 2 == 0:
                print(current.data, end=" ")
            current = current.next
        print()

    

def delete_number(stack: Stack):
    if stack.is_empty():
        print("A pilha está vazia. Nenhum número para excluir.")
    else:
        removed = stack.pop()
        print(f"Número {removed} excluído da pilha.")