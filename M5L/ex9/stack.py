class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def bottom(self):
        if not self.is_empty():
            return self.items[0]
        return None


def show_even_numbers(stack):
    if stack.is_empty() or stack.bottom() == stack.top():
        print("Intervalo inválido para mostrar números pares.")
        return

    start = min(stack.bottom(), stack.top())
    end = max(stack.bottom(), stack.top())

    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    if even_numbers:
        print("Números pares entre o primeiro e o último número cadastrado:", even_numbers)
    else:
        print("Não há números pares no intervalo.")


def delete_number(stack):
    if stack.is_empty():
        print("A pilha está vazia. Nenhum número para excluir.")
    else:
        removed = stack.pop()
        print(f"Número {removed} excluído da pilha.")


def main():
    stack = Stack()
    while True:
        print("\nMENU")
        print("1- Cadastrar número")
        print("2- Mostrar números pares entre o primeiro e o último número cadastrado")
        print("3- Excluir número")
        print("4- Sair")
        
        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, digite um número entre 1 e 4.")
            continue

        if option == 1:
            try:
                num = int(input("Digite o número para cadastrar: "))
                stack.push(num)
                print(f"Número {num} cadastrado.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
        
        elif option == 2:
            show_even_numbers(stack)
        
        elif option == 3:
            delete_number(stack)
        
        elif option == 4:
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")


if __name__ == "__main__":
    main()
