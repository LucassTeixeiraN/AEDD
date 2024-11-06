from linkedList import LinkedList

def menu():
    print("\nLinked List Operations Menu:")
    print("1. Add element to the list")
    print("2. Print the current list")
    print("3. Reorder letters and digits")
    print("4. Exit")

def main():
    linked_list = LinkedList()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            linked_list.add(value)
            print(f"Added '{value}' to the list.")

        elif choice == "2":
            print("\nCurrent list:")
            linked_list.print_list()

        elif choice == "3":
            reordered_list = linked_list.reorder_letters_digits()
            print("\nReordered list:")
            reordered_list.print_list()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()