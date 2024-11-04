# Escreva um programa que use uma pilha para testar strings de entrada e determinar
# se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma
# forma de frente para trás e de trás para a frente; por exemplo, arara.

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

def eh_palindromo(string):
    pilha = Pilha()
    
    for caractere in string:
        pilha.empilhar(caractere)

    for caractere in string:
        if caractere != pilha.desempilhar():
            return False
    return True

def main():
    while True:
        entrada = input("Digite uma palavra ou digite stop para encerrar o programa: ").lower()
        if entrada == "stop":
            print("programa encerrado!")
            break
        if not entrada.isalpha():  
            print("Insira uma palavra válida (apenas letras)!")
            continue
        if eh_palindromo(entrada):
            print(f'"{entrada}" é um palíndromo.')
        else:
            print(f'"{entrada}" não é um palíndromo.')

main()
