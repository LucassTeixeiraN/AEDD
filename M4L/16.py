# 16. Faça um programa que implemente uma lista duplamente encadeada de números
# inteiros com inserção de dados pelo usuário através de um menu. Escreva uma
# função que remova da lista a célula apontada por p e outra função que insira uma
# nova célula com conteúdo x nesta lista duplamente encadeada logo após a célula
# apontada por p. Dê duas soluções: uma iterativa e uma recursiva.

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, node, new_value):
        new_node = Node(new_value)
        if node is None:
            return  

        new_node.next = node.next
        new_node.prev = node

        if node.next:
            node.next.prev = new_node
        node.next = new_node

    def remove(self, node):
        if node is None:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head: 
            self.head = node.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' <=> ')
            current = current.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

def main():
    doubly_linked_list = DoublyLinkedList()
    while True:
        print("\nMenu:")
        print("1. Adicionar número")
        print("2. Remover número")
        print("3. Inserir após um número")
        print("4. Exibir lista")
        print("5. Sair")
        option = int(input("Escolha uma opção: "))

        if option == 1:
            value = int(input("Digite um número para adicionar: "))
            doubly_linked_list.append(value)

        elif option == 2:
            value = int(input("Digite um número para remover: "))
            current = doubly_linked_list.head
            while current:
                if current.value == value:
                    doubly_linked_list.remove(current)
                    break
                current = current.next

        elif option == 3:
            existing_value = int(input("Digite um número existente para inserir após: "))
            new_value = int(input("Digite o número a ser inserido: "))
            current = doubly_linked_list.head
            while current:
                if current.value == existing_value:
                    doubly_linked_list.insert_after(current, new_value)
                    break
                current = current.next

        elif option == 4:
            doubly_linked_list.display()

        elif option == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
