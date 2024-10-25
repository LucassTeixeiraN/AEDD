'''1. Defina uma função length (não len) que espera uma estrutura unicamente ligada
como argumento. A função retorna o número de itens na estrutura.'''

from list import List 

def menu():
    print("1. Adicionar um elemento à lista")
    print("2. Ver quantos elementos a lista possui")
    print("0. Sair")
    option = input()
    return option

def length(list:List):
    count = 0
    if not list.isEmpty():
        temp = list.head

        while temp:
            count += 1
            temp = temp.next

    return count

def main():
    newList = List()

    while True:
        option = menu()

        if option == "1":
            newList.appendElement(input("Insira um dado: "))
        elif option == "2":
            print(f"A lista tem {length(newList)} elementos")
        elif option == "0":
            break

        else:
            print("Valor inválido")


main()