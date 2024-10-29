'''8. Faça um programa que receba n números e armazene os pares em uma lista
simplesmente encadeada e não ordenada e os ímpares em uma segunda lista
simplesmente encadeada e não ordenada. Posteriormente, o programa deve montar
uma terceira lista, duplamente encadeada e ordenada de forma crescente, com os
números das duas listas anteriores. Para finalizar, o programa deve mostrar todos os
números da terceira lista das seguintes formas:
a. Crescente.
b. Decrescente.'''

from simpleLinkedList import SimpleLinkedList 
from doublyLinkedList import DoublyLinkedList 

def main():
    even_list = SimpleLinkedList()
    odd_list = SimpleLinkedList()
    sorted_list = DoublyLinkedList()

    n = int(input("Quantos números você deseja inserir? "))
    for _ in range(n):
        num = int(input("Insira um número: "))
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    # Adicionando elementos das listas simples à lista duplamente encadeada
    current = even_list.head
    while current:
        sorted_list.insert(current.data)
        current = current.next

    current = odd_list.head
    while current:
        sorted_list.insert(current.data)
        current = current.next

    # Exibindo resultados
    print("Lista em ordem crescente:")
    sorted_list.display()

    print("Lista em ordem decrescente:")
    sorted_list.display_reverse()

main()
