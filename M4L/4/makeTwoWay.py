from node import DoubleNode  

class MakeTwoWay:
    
    def makeTwoWay(self, lista_simples):
        """Converte uma lista simplesmente ligada em uma lista duplamente ligada."""
        if lista_simples is None:
            return None

        inicio_duplo = DoubleNode(lista_simples.valor)
        atual_duplo = inicio_duplo
        atual_simples = lista_simples.proximo

        while atual_simples is not None:
            novo_no = DoubleNode(atual_simples.valor)
            atual_duplo.proximo = novo_no
            novo_no.anterior = atual_duplo
            atual_duplo = novo_no
            atual_simples = atual_simples.proximo

        return inicio_duplo

    def print_list(self, inicio, detalhado=False):
  
        atual = inicio
        while atual is not None:
            if detalhado:
                anterior = atual.anterior.valor if atual.anterior else None
                proximo = atual.proximo.valor if atual.proximo else None
                print(f"Valor: {atual.valor} (Anterior: {anterior}, Próximo: {proximo})")
            else:
                print(atual.valor, end=" -> " if atual.proximo else "")
            atual = atual.proximo
        if not detalhado:
            print() 
