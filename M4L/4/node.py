class SimpleNode:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class DoubleNode:
    def __init__(self, valor, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior