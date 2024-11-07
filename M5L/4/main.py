'''Escreva um programa que recebe duas listas encadeadas de inteiros e efetue os
seguintes passos:
a. Verifique se as listas estão ordenadas;
b. Ordene as listas, caso não estejam ordenadas;
c. Mescle os elementos da segunda lista na primeira, mantendo a ordenação na lista
final.'''
from linkedList import LinkedList
def main():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(4)
    list2.append(2)
    list2.append(6)

    if not list1.is_sorted():
        print("A lista 1 não está ordenada. Ordenando...")
        list1.sort()
    else:
        print("A lista 1 está ordenada.")

    if not list2.is_sorted():
        print("A lista 2 não está ordenada. Ordenando...")
        list2.sort()
    else:
       print("A lista 2 está ordenada.")

    list1.merge(list2)

    print("Lista mesclada:")
    list1.print_list()

main()