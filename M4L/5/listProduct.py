from node import Node
class ListProduct:
    def __init__(self):
        self.head = None

    def cadastrar_produto(self, codigo, preco, quantidade):
        novo_produto = Node(codigo, preco, quantidade)
        if self.head is None:
            self.head = novo_produto
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_produto

    def aplicar_desconto(self, taxa):
        atual = self.head
        while atual:
            # Aplica o desconto no preço do produto
            atual.preco = atual.preco * (1 - taxa / 100)
            atual = atual.proximo

    def relatorio_produtos(self):
        atual = self.head
        contador_estoque_maior_500 = 0
        print("Relatório de Produtos:")
        while atual:
            print(f"Código: {atual.codigo}, Novo Preço: R${atual.preco:.2f}")
            if atual.quantidade > 500:
                contador_estoque_maior_500 += 1
            atual = atual.proximo
        print(f"\nQuantidade de produtos com estoque superior a 500: {contador_estoque_maior_500}")
