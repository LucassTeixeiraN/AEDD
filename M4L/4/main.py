'''Defina uma função makeTwoWay que espera uma estrutura unicamente ligada como
o argumento. A função cria e retorna uma estrutura duplamente ligada que contém os
itens na estrutura unicamente ligada. (Nota: A função não deve alterar a estrutura do
argumento.)'''
# main.py

from node import SimpleNode
from makeTwoWay import MakeTwoWay

def main():
    lista_simples = SimpleNode(1, SimpleNode(2, SimpleNode(3)))

    conversor = MakeTwoWay()

    lista_dupla = conversor.makeTwoWay(lista_simples)

    print("Lista duplamente ligada (detalhada):")
    conversor.print_list(lista_dupla, detalhado=True)

    print("\nFormato final da lista duplamente ligada:")
    conversor.print_list(lista_dupla, detalhado=False)

main()

