# 15. Faça um programa que implemente uma lista encadeada de números inteiros com
# inserção de dados pelo usuário através de um menu. Escreva uma função que copie
# o conteúdo de um vetor para uma lista encadeada preservando a ordem dos
# elementos e outra função que copie o conteúdo de uma lista encadeada para um
# vetor preservando a ordem dos elementos. Faça duas versões: uma iterativa e uma
# # recursiva.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data}. Current list:", self.to_list_iterative())

    def to_list_iterative(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_recursive(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.head
        if node:
            result.append(node.data)
            self.to_list_recursive(node.next, result)
        return result

    def from_list_iterative(self, lst):
        self.head = None  
        for item in reversed(lst):
            self.insert(item)
        print("Created list from input (iterative):", self.to_list_iterative())

    def from_list_recursive(self, lst, index=0):
        self.head = None 
        self._from_list_recursive_helper(lst, index)
        print("Created list from input (recursive):", self.to_list_iterative())

    def _from_list_recursive_helper(self, lst, index):
        if index < len(lst):
            self.insert(lst[index])
            self._from_list_recursive_helper(lst, index + 1)

def menu():
    ll = LinkedList()
    while True:
        print("\n1. Insert")
        print("2. Convert to list (iterative)")
        print("3. Convert to list (recursive)")
        print("4. Create from list (iterative)")
        print("5. Create from list (recursive)")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert: "))
            ll.insert(data)
        elif choice == 2:
            print("List (iterative):", ll.to_list_iterative())
        elif choice == 3:
            print("List (recursive):", ll.to_list_recursive())
        elif choice == 4:
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            ll.from_list_iterative(lst)
        elif choice == 5:
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            ll.from_list_recursive(lst)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
