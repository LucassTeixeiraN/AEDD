from node import No
class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Insere um valor na árvore binária de busca"""
        self.raiz = self._inserir(self.raiz, valor, None)

    def _inserir(self, no, valor, pai):
        """Método auxiliar recursivo para inserir um nó"""
        if no is None:
            return No(valor, pai)  # Passando o pai para o novo nó
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor, no)
        else:
            no.direita = self._inserir(no.direita, valor, no)
        return no

    def sucessor(self, valor):
        """Encontra o sucessor do valor na árvore"""
        no = self._buscar(self.raiz, valor)
        if no:
            return self._sucessor(no)
        return None

    def _sucessor(self, no):
        """Encontra o sucessor de um nó"""
        # Se o nó tem um filho à direita, o sucessor é o menor valor na subárvore à direita
        if no.direita:
            return self._minimo(no.direita)
        
        # Caso contrário, percorre os ancestrais até encontrar um nó cujo valor seja maior
        p = no
        while p.pai and p.pai.direita == p:  # Subir na árvore até encontrar um ancestral maior
            p = p.pai
        return p.pai.valor if p.pai else None

    def antecessor(self, valor):
        """Encontra o antecessor do valor na árvore"""
        no = self._buscar(self.raiz, valor)
        if no:
            return self._antecessor(no)
        return None

    def _antecessor(self, no):
        """Encontra o antecessor de um nó"""
        # Se o nó tem um filho à esquerda, o antecessor é o maior valor na subárvore à esquerda
        if no.esquerda:
            return self._maximo(no.esquerda)

        # Caso contrário, percorre os ancestrais até encontrar um nó cujo valor seja menor
        p = no
        while p.pai and p.pai.esquerda == p:  # Subir na árvore até encontrar um ancestral menor
            p = p.pai
        return p.pai.valor if p.pai else None

    def _minimo(self, no):
        """Encontra o nó com o valor mínimo em uma subárvore"""
        while no.esquerda:
            no = no.esquerda
        return no.valor

    def _maximo(self, no):
        """Encontra o nó com o valor máximo em uma subárvore"""
        while no.direita:
            no = no.direita
        return no.valor

    def _buscar(self, no, valor):
        """Busca um valor na árvore binária de busca"""
        if no is None or no.valor == valor:
            return no
        elif valor < no.valor:
            return self._buscar(no.esquerda, valor)
        else:
            return self._buscar(no.direita, valor)