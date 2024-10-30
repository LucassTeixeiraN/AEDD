'''13. Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que insira
uma nova célula com conteúdo x imediatamente depois da k-ésima célula da lista
encadeada e outra função que troque de posição duas células de uma mesma lista.
Faça duas versões: uma iterativa e uma recursiva.'''

from list import List 

def menu():
    print("1. Criar lista")
    print("2. Ver lista")
    print("3. Adicionar um elemento a lista")
    print("4. Trocar dois elementos da lista lista")
    print("0. Sair")
    option = input()
    return option

def criarLista(list: List):
    length = int(input("Insira quantos elementos a lista terá: "))
    for i in range(length):
        list.appendElement(int(input(f"Insira o {i+1}° elemento: ")))

def main():
    newList = List()

    while True:
        option = menu()

        if option == "1":
            criarLista(newList)
        elif option == "2":
            print("-"*60)
            newList.showList()
            print("-"*60)
        elif option == "3":
            k = int(input("Insira a posição do novo elemento: "))
            num = int(input("Insira o elemento: "))
            newList.insertElement(num, k)
        elif option == '4':
            pos1 = int(input("Insira a posição do primeiro elemento a ser trocado: "))
            pos2 = int(input("Insira a posição do segundo elemento a ser trocado: "))
            newList.changeElements(pos1, pos2)
        elif option == "0":
            break

        else:
            print("Valor inválido")


main()