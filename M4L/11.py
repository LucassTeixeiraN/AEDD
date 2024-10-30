# Faça um programa que implemente uma lista encadeada de números inteiros com
# inserção de dados pelo usuário através de um menu. Escreva uma função que
# encontre o nó que contenha o menor valor e outra função que verifique se duas listas
# encadeadas são iguais, ou melhor, se têm o mesmo conteúdo. Faça duas versões:
# uma iterativa e uma recursiva.

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

    def find_min_iterative(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def find_min_recursive(self, node):
        if not node:
            return None  
        next_min = self.find_min_recursive(node.next)
        if next_min is None:
            return node.data  
        return min(node.data, next_min)

    def are_equal_iterative(self, other):
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

    def are_equal_recursive(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.data != node2.data:
            return False
        return self.are_equal_recursive(node1.next, node2.next)

def menu():
    list1 = LinkedList()
    list2 = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Inserir na lista 1")
        print("2. Inserir na lista 2")
        print("3. Encontrar o menor valor na lista 1 (Iterativo)")
        print("4. Encontrar o menor valor na lista 1 (Recursivo)")
        print("5. Encontrar o menor valor na lista 2 (Iterativo)")
        print("6. Encontrar o menor valor na lista 2 (Recursivo)")
        print("7. Verificar se as listas são iguais (Iterativo)")
        print("8. Verificar se as listas são iguais (Recursivo)")
        print("9. Sair")
        
        choice = int(input("Escolha uma opção: "))
        
        if choice == 1:
            data = int(input("Digite um número para inserir na lista 1: "))
            list1.insert(data)
        elif choice == 2:
            data = int(input("Digite um número para inserir na lista 2: "))
            list2.insert(data)
        elif choice == 3:
            min_value = list1.find_min_iterative()
            if min_value is not None:
                print("Menor valor na lista 1 (Iterativo):", min_value)
            else:
                print("A lista 1 está vazia.")
        elif choice == 4:
            min_value = list1.find_min_recursive(list1.head)
            if min_value is not None:
                print("Menor valor na lista 1 (Recursivo):", min_value)
            else:
                print("A lista 1 está vazia.")
        elif choice == 5:
            min_value = list2.find_min_iterative()
            if min_value is not None:
                print("Menor valor na lista 2 (Iterativo):", min_value)
            else:
                print("A lista 2 está vazia.")
        elif choice == 6:
            min_value = list2.find_min_recursive(list2.head)
            if min_value is not None:
                print("Menor valor na lista 2 (Recursivo):", min_value)
            else:
                print("A lista 2 está vazia.")
        elif choice == 7:
            are_equal = list1.are_equal_iterative(list2)
            print("As listas são iguais (Iterativo):", are_equal)
        elif choice == 8:
            are_equal = list1.are_equal_recursive(list1.head, list2.head)
            print("As listas são iguais (Recursivo):", are_equal)
        elif choice == 9:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
