class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self._inserir_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self._inserir_recursivo(no.direita, chave)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, no):
        if no is None:
            return 0
        else:
            altura_esquerda = self._altura_recursiva(no.esquerda)
            altura_direita = self._altura_recursiva(no.direita)
            return max(altura_esquerda, altura_direita) + 1

    def nivel(self, chave):
        return self._nivel_recursivo(self.raiz, chave, 0)

    def _nivel_recursivo(self, no, chave, nivel):
        if no is None:
            return -1
        if no.chave == chave:
            return nivel
        elif chave < no.chave:
            return self._nivel_recursivo(no.esquerda, chave, nivel + 1)
        else:
            return self._nivel_recursivo(no.direita, chave, nivel + 1)


def menu():
    arvore = ArvoreBinaria()
    while True:
        print("\nMenu:")
        print("1 - Inserir número")
        print("2 - Mostrar a altura da árvore")
        print("3 - Mostrar o nível de um nó")
        print("4 - Sair")
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            try:
                numero = int(input("Digite o número a ser inserido: "))
                arvore.inserir(numero)
                print(f"Número {numero} inserido com sucesso.")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif opcao == "2":
            altura = arvore.altura()
            print(f"A altura da árvore é: {altura}")
        
        elif opcao == "3":
            try:
                numero = int(input("Digite o número do nó para verificar o nível: "))
                nivel = arvore.nivel(numero)
                if nivel == -1:
                    print(f"O nó {numero} não foi encontrado na árvore.")
                else:
                    print(f"O nível do nó {numero} é: {nivel}")
            except ValueError:
                print("Por favor, insira um número válido.")
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")


menu()
