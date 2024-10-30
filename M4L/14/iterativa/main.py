'''14. Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que inverta
a ordem das células de uma lista encadeada (a primeira passa a ser a última, a
segunda passa a ser a penúltima etc.). Faça isso sem usar espaço auxiliar, apenas
alterando ponteiros. Dê duas soluções: uma iterativa e uma recursiva.'''

from list import List 

def menu():
    print("1. Criar lista")
    print("2. Inverter e ver lista")
    print("0. Sair")
    option = input()
    return option

def criarLista(list: List , length):
    for i in range(length):
        list.appendElement(int(input(f"Insira o {i+1}° elemento: ")))

def main():
    newList = List()

    while True:
        option = menu()

        if option == "1":
            len = int(input("Insira quantos elementos a lista terá: "))
            criarLista(newList, len)
        elif option == "2":
            print("-"*60)
            newList.listChanger(len)
            newList.showList()
            print("-"*60)
        elif option == "0":
            break

        else:
            print("Valor inválido")


main()