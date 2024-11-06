from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        atual = self.head
        if not atual:
            print("Lista vazia.")
            return
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    def verificar_ordem_crescente(self):
        return self._verificar_ordem_crescente_iterativa()

    def _verificar_ordem_crescente_iterativa(self):
        atual = self.head
        while atual and atual.proximo:
            if atual.valor > atual.proximo.valor:
                return False
            atual = atual.proximo
        return True

    def buscar(self, valor):
        return self._buscar_iterativo(valor)

    def _buscar_iterativo(self, valor):
        atual = self.head
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def buscar_recursivo(self, valor):
        return self._buscar_recursivo(self.head, valor)

    def _buscar_recursivo(self, node, valor):
        if node is None:
            return False
        if node.valor == valor:
            return True
        return self._buscar_recursivo(node.proximo, valor)
