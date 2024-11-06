from circularDoublyLinkedList import CircularDoublyLinkedList

def menu():
    print("\nCircular Doubly Linked List Operations Menu:")
    print("1. Insert element into the list")
    print("2. Search name by key")
    print("3. Remove element by key")
    print("4. Print the current list")
    print("5. Copy the current list")
    print("6. Concatenate two lists")
    print("7. Interleave two lists")
    print("8. Exit")

def main():
    list1 = CircularDoublyLinkedList()
    list2 = CircularDoublyLinkedList()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key (integer): "))
            name = input("Enter name (string): ")
            list1.insert(key, name)
            print(f"Inserted {name} with key {key} into List 1.")

        elif choice == "2":
            key = int(input("Enter key to search: "))
            result = list1.search_name(key)
            if result:
                print(f"Found: {result}")
            else:
                print(f"No entry found with key {key}.")

        elif choice == "3":
            key = int(input("Enter key to remove: "))
            list1.remove(key)
            print(f"Removed element with key {key} from List 1.")

        elif choice == "4":
            print("\nCurrent List 1:")
            list1.print_list()

        elif choice == "5":
            list2 = list1.copy_list()
            print("\nList 2 is a copy of List 1:")
            list2.print_list()

        elif choice == "6":
            print("\nConcatenating List 1 and List 2...")
            list1.concatenate(list2)
            list1.print_list()

        elif choice == "7":
            print("\nInterleaving List 1 and List 2...")
            interleaved_list = list1.interleave(list2)
            interleaved_list.print_list()

        elif choice == "8":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
