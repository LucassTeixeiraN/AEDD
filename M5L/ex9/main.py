from stack import Stack, show_even_numbers, delete_number

def menu():
    print("\nMENU")
    print("1- Cadastrar número")
    print("2- Mostrar números")
    print("3- Mostrar números pares entre o primeiro e o último número cadastrado")
    print("4- Excluir número")
    print("5- Sair")
    
    return int(input("Escolha uma opção: "))

def main():
    stack = Stack()
    while True:
        option = menu()
        
        if option == 1:
            try:
                num = int(input("Digite o número para cadastrar: "))
                stack.push(num)
                print(f"Número {num} cadastrado.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        
        elif option == 2:
            stack.print_list()
        
        elif option == 3:
            show_even_numbers(stack)
        
        elif option == 4:
            delete_number(stack)
        
        elif option == 5:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")


if __name__ == "__main__":
    main()
