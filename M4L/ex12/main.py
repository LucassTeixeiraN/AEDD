'''Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que faça
uma cópia da lista e outra função que concatene duas listas encadeadas (isto é,
engate a segunda no fim da primeira). Faça duas versões da função: uma iterativa e
uma recursiva.'''

from linked_list import LinkedList, iterativeCopy, recursiveConcatenate, recursiveCopy, iterativeConcatenate

def menu():
    print()
    print("1. Append item")
    print("2. Pop item")
    print("3. Print list")
    print("4. Exit")
    return input("Choose an option (1-4): ")

def main():
    linked_list = LinkedList()
    
    while True:
        choice = menu()
        if choice == '1':
            item = int(input("Enter integer to append: "))
            linked_list.append(item)
            print("Item appended.")
        
        elif choice == '2':
            index = int(input("Enter index to pop: "))
            
            if 0 <= index and index < linked_list.length:
                linked_list, item = linked_list.pop(index)
                
                print("New linked list:")
                linked_list.printList()
                print(f"Removed Item: {item.data}")
            else:
                print('Index out of range!')
        
        elif choice == '3':
            linked_list.printList()
        
        elif choice == '4':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
    print('\nIterative copy:')
    linked_list_copy = iterativeCopy(linked_list)
    linked_list_copy.printList()
    
    print('\nRecursive copy:')
    linked_list_copy = recursiveCopy(linked_list)
    linked_list_copy.printList()
    
    linked_list2 = LinkedList()
    linked_list2.append(1)
    linked_list2.append(2)
    
    print('\nIterative concatenate:')
    linked_list = iterativeConcatenate(linked_list, linked_list2)
    linked_list.printList()
    
    print('\nRecursive concatenate:')
    linked_list = recursiveConcatenate(linked_list2, linked_list)
    linked_list.printList()
    

if __name__ == "__main__":
    main()