'''Considere uma coleção de nomes de sites da web e seus respectivos links na Internet
armazenados através de uma lista simplesmente encadeada. Escreva a respectiva
estrutura e um método que, dado o nome de um site, busque o seu link
correspondente na lista e ao mesmo tempo mova o nó que contém o nome buscado
para o início da lista, de forma que ele possa ser encontrado mais rapidamente na
próxima vez que for buscado.'''

from linkedList import LinkedList

def main():
    linked_list = LinkedList()
    linked_list.insert('google', 'https://www.google.com')
    linked_list.insert('facebook', 'https://www.facebook.com')
    linked_list.insert('X', 'https://www.x.com')

    print("Lista antes da busca:")
    linked_list.display()

    link = linked_list.searchAndMove('facebook')
    print(f'\nlink encontrado: {link}')

    print("\nLista após a busca:")
    linked_list.display()

    link = linked_list.searchAndMove('google')
    print(f'\nLink encontrado: {link}')

    print("\nLista após a busca:")
    linked_list.display()
main()