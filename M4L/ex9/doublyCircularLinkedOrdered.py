from node import Node

class DoublyCircularLinkedOrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            new_node.next = new_node
            new_node.previous = new_node
            self.head = new_node
        else:
            current = self.head
            while True:
                if new_data['salary'] < current.data['salary']:
                    new_node.previous = current.previous
                    new_node.next = current
                    current.previous.next = new_node
                    current.previous = new_node

                    if current == self.head:
                        self.head = new_node
                    break

                elif current.next == self.head:
                    current.next = new_node
                    new_node.previous = current
                    new_node.next = self.head
                    self.head.previous = new_node
                    break
                current = current.next

    def delete(self, data):
        if self.isEmpty():
            print("List is empty!!")
            return
        
        current = self.head
        while True:
            if current.data == data:
                if current == self.head and current.next == self.head:
                    self.head = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break
        
        print("Element not found in the list!")

    def searchNode(self, letter: str):
        if self.isEmpty():
            print("Empty list.")
            return None
        
        hasFound = False
        current = self.head
        while True:
            if current.data['name'][0].lower() == letter.lower():
                print(f'Nome: {current.data["name"]} | Salário: {current.data["salary"]:.2f}', end='\n')
                hasFound = True
            current = current.next
            if current == self.head:
                break
        
        if not hasFound:
            print("Nenhum nome encontrado com a letra digitada.")

    def calculateTax(self, salary):
        if salary <= 850:
            return 0
        elif salary <= 1200:
            return salary * 0.1
        else:
            return salary * 0.2
        
    def showNodeData(self, data: dict, show_tax):
        if show_tax:
            tax = self.calculateTax(data['salary'])
            print(f"Nome: {data['name']} | Imposto: {tax:.2f} | Valor a receber: {(data['salary'] - tax):.2f}", end='\n')
        else:
            print(f"Nome: {data['name']} | Salário: {data['salary']:.2f}", end='\n')

    def display(self, show_tax=True):
        if self.isEmpty():
            print("List is empty!!")
            return

        current = self.head
        while True:
            self.showNodeData(current.data, show_tax)
            current = current.next
            if current == self.head:
                break
        print()

    def displayReverse(self, show_tax=True):
        if self.isEmpty():
            print("List is empty!!")
            return

        current = self.head.previous
        while True:
            self.showNodeData(current.data, show_tax)
            current = current.previous
            if current == self.head.previous:
                break
        print()