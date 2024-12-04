'''Adicione os métodos sucessor e antecessor a uma Árvore Binária de Busca. Cada
método espera um item como argumento e retorna um item ou None. Um sucessor é
o menor item na árvore que é maior do que o determinado item. Um predecessor é o
maior item na árvore que é menor do que o determinado item. Observe que o
sucessor pode existir mesmo se o item fornecido não estiver presente na árvore.'''
# main.py

from arvoreBinaria import ArvoreBinariaDeBusca

def main():
    # Criação da árvore binária de busca
    arvore = ArvoreBinariaDeBusca()

    # Inserção de alguns valores
    arvore.inserir(20)
    arvore.inserir(10)
    arvore.inserir(30)
    arvore.inserir(25)
    arvore.inserir(40)
    arvore.inserir(5)
    arvore.inserir(15)

    # Testando o sucessor
    valor = 20
    print(f"Sucessor de {valor}: {arvore.sucessor(valor)}")

    valor = 10
    print(f"Sucessor de {valor}: {arvore.sucessor(valor)}")

    # Testando o antecessor
    valor = 30
    print(f"Antecessor de {valor}: {arvore.antecessor(valor)}")

    valor = 25
    print(f"Antecessor de {valor}: {arvore.antecessor(valor)}")

if __name__ == "__main__":
    main()

