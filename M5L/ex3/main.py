from circularDoublyLinkedList import CircularDoublyLinkedList

def main():
    list1 = CircularDoublyLinkedList()
    list1.insert(1, "Alice")
    list1.insert(3, "Bob")
    list1.insert(2, "Charlie")

    print("List 1:")
    list1.print_list()

    print("\nSearch name with key 2:")
    print(list1.search_name(2))

    list1.remove(3)
    print("\nList 1 after removing key 3:")
    list1.print_list()

    list2 = list1.copy_list()
    print("\nList 2 (copy of List 1):")
    list2.print_list()

    list3 = CircularDoublyLinkedList()
    list3.insert(4, "David")
    list3.insert(5, "Eve")

    print("\nConcatenate List 1 and List 3:")
    list1.concatenate(list3)
    list1.print_list()

    print("\nInterleave List 1 and List 2:")
    interleaved_list = list1.interleave(list2)
    interleaved_list.print_list()

main()