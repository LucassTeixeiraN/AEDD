'''Faça um programa que cadastre o nome e o salário de n funcionários em uma lista
duplamente encadeada e ordenada pelo salário de forma crescente. A seguir, o
programa deve mostrar o nome, o valor do imposto e o valor a receber, ou seja, o
salário menos o imposto de todos os funcionários cadastrados. Posteriormente, o
programa deve mostrar os nomes e os salários dos funcionários cujos nomes
comecem por uma letra digitada pelo usuário (considera a possibilidade de letras
maiúsculas e minúsculas). Se nenhum funcionário tem o nome começado com a letra
digitada pelo usuário, mostrar mensagem. Finalmente, o programa deve apresentar
duas listagens:

a. Dos nomes e salários dos funcionários por ordem crescente de salário;
b. Dos nomes e salários dos funcionários por ordem decrescente de salário.
Observação: os percentuais de imposto seguem a tabela abaixo:

Valor do salário    | Percentual do imposto
Até 850             | Isento
Entre 850 e 1200    | 10% do salário
De 1200 para cima   | 20% do salário'''
from doublyCircularLinkedOrdered import DoublyCircularLinkedOrderedList

def main():
    ordered_list = DoublyCircularLinkedOrderedList()

    print("Inserting elements:")
    while True:
        try:
            name = input("Enter name: ")
            salary = float(input("Enter salary: "))
            ordered_list.insert({"name": name, "salary": salary})
            
            if input("Do you want to add another employee? (y/n): ").lower() != "y":
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    ordered_list.display()

    # Test searching for an element
    print("\nSearching for 20:")
    node = ordered_list.searchNode(20)
    if node:
        print(f"Found: {node.data}")
    else:
        print("Not found.")

    # Test deleting an element
    print("\nDeleting 20:")
    ordered_list.delete(20)
    ordered_list.display()  # Should display: 10 30 40

    # Test deleting an element that does not exist
    print("\nTrying to delete 50 (not in list):")
    ordered_list.delete(50)  # Should print "Element not found in the list!"

    # Test deleting the head element
    print("\nDeleting 10 (head):")
    ordered_list.delete(10)
    ordered_list.display()  # Should display: 30 40

    # Test deleting the last remaining element
    print("\nDeleting 40 (last element):")
    ordered_list.delete(40)
    ordered_list.display()  # Should display: 30

    # Final check to see if the list is empty
    print("\nDeleting last element (30):")
    ordered_list.delete(30)
    ordered_list.display()  # Should print "List is empty!!"

    # Final check
    print("Is the list empty?", ordered_list.isEmpty())

if __name__ == "__main__":
    main()
