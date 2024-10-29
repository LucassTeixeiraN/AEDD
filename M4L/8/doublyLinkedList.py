from doublyNode import DoublyNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = DoublyNode(data)
        if not self.head:  # Lista vazia
            self.head = new_node
            self.tail = new_node
            return

        if data < self.head.data:  # Inserir no início
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        current.next = new_node
        if new_node.next:  # Atualiza o ponteiro prev do próximo nó
            new_node.next.prev = new_node
        else:  # Atualiza o tail se for o último elemento
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()
