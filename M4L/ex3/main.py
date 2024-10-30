'''Defina uma função chamada pop que remove o item em determinada posição de uma
estrutura unicamente ligada. Essa função espera uma posição como primeiro
argumento, com a precondição 0 <= posição < comprimento da estrutura. Seu
segundo argumento é a estrutura ligada, que, é claro, não pode estar vazia. A função
retorna uma tupla contendo a estrutura ligada modificada e o item que foi removido.
Um exemplo de chamada é (head, item) = pop(1, head).'''
from linked_list import LinkedList, pop

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
            item = input("Enter item to append: ")
            linked_list.append(item)
            print("Item appended.")
        
        elif choice == '2':
            index = int(input("Enter index to pop: "))
            
            if 0 <= index and index < linked_list.length:
                linked_list, item = pop(index, linked_list)
                
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

if __name__ == "__main__":
    main()
