# 7. Faça um programa para executar as operações abaixo em uma árvore binária não
# ordenada.
# Menu
# 1 – Inserir número aleatório com geração e inserção aleatórias
# 2 – Mostrar os números da árvore usando o imprimeRelacoes da questão 4
# 3 – Imprimir emOrdem, preOrdem e posOrdem
# 4 – Mostrar o maior número na árvore
# 5 – Sair


import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir_aleatorio(self):
        valor = random.randint(1, 100)  
        print(f"Inserindo o valor {valor} na árvore.")
        self.raiz = self.inserir(self.raiz, valor)
    
    def inserir(self, raiz, valor):
        if raiz is None:
            return No(valor)
        else:
            if random.choice([True, False]):
                raiz.esquerda = self.inserir(raiz.esquerda, valor)
            else:
                raiz.direita = self.inserir(raiz.direita, valor)
        return raiz
    
# espaço para a opção 2 que é necessario uma parte do exercicio 4
######################################################################################
######################################################################################
######################################################################################
          
    
    def em_ordem(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.valor, end=" ")
            self.em_ordem(raiz.direita)
    
    def pre_ordem(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz:
            print(raiz.valor, end=" ")
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)
    
    def pos_ordem(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz:
            self.pos_ordem(raiz.esquerda)
            self.pos_ordem(raiz.direita)
            print(raiz.valor, end=" ")
    
    def maior_numero(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        while raiz and raiz.direita:
            raiz = raiz.direita
        return raiz.valor if raiz else None


def main():
    arvore = ArvoreBinaria()
    
    while True:
        print("\nMenu:")
        print("1 – Inserir número aleatório com geração e inserção aleatórias")
        print("2 – Mostrar os números da árvore usando o imprimeRelacoes")
        print("3 – Imprimir emOrdem, preOrdem e posOrdem")
        print("4 – Mostrar o maior número na árvore")
        print("5 – Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            arvore.inserir_aleatorio()
        elif opcao == "2":
            print("Relacionamentos na árvore:")
           ##############################################################
        elif opcao == "3":
            print("Em Ordem: ", end="")
            arvore.em_ordem()
            print("\nPré Ordem: ", end="")
            arvore.pre_ordem()
            print("\nPós Ordem: ", end="")
            arvore.pos_ordem()
            print()
        elif opcao == "4":
            maior = arvore.maior_numero()
            if maior is not None:
                print(f"O maior número na árvore é: {maior}")
            else:
                print("A árvore está vazia.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
