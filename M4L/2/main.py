'''Defina uma função chamada Insert que insere um item em uma estrutura unicamente
ligada em determinada posição. A função espera três argumentos: o item, a posição e
a estrutura ligada. (A última pode estar vazia.) A função retorna a estrutura ligada
modificada. Se a posição é maior ou igual ao comprimento da estrutura, a função
insere o item no final. Um exemplo de chamada da função, onde head é uma variável
que é uma ligação vazia ou se refere ao primeiro nó de uma estrutura, é head =
Insert(1, data, head).'''
from node import Node
from linkedList import LinkedList

def main():
# Criando uma lista ligada
    # Criando uma lista ligada
    linked_list = LinkedList()

    # Inserindo elementos
    linked_list.insert(0, 10)  # Inserir no início
    linked_list.insert(1, 20)  # Inserir após o primeiro elemento
    linked_list.insert(0, 5)   # Inserir no início novamente
    linked_list.insert(2, 15)  # Inserir em uma posição intermediária

    # Imprimindo a lista
    linked_list.print_list()
    # Saída: 5 -> 10 -> 15 -> 20 -> None

main()
