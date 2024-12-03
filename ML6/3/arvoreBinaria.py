from node import No

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(atual.esquerda, valor)
        else:
            if atual.direita is None:
                atual.direita = No(valor)
            else:
                self._inserir_recursivo(atual.direita, valor)

    def mostrar_todos(self):
        self._percorrer_em_ordem(self.raiz)
        print()

    def _percorrer_em_ordem(self, no):
        if no is not None:
            self._percorrer_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self._percorrer_em_ordem(no.direita)

    def mostrar_subarvore_direita(self, valor):
        no = self._buscar(self.raiz, valor)
        if no and no.direita:
            print(f"Subárvore direita do nó {valor}:")
            self._percorrer_em_ordem(no.direita)
        else:
            print(f"O nó {valor} não tem subárvore direita.")
        print()

    def mostrar_subarvore_esquerda(self, valor):
        no = self._buscar(self.raiz, valor)
        if no and no.esquerda:
            print(f"Subárvore esquerda do nó {valor}:")
            self._percorrer_em_ordem(no.esquerda)
        else:
            print(f"O nó {valor} não tem subárvore esquerda.")
        print()

    def _buscar(self, atual, valor):
        if atual is None or atual.valor == valor:
            return atual
        if valor < atual.valor:
            return self._buscar(atual.esquerda, valor)
        else:
            return self._buscar(atual.direita, valor)
