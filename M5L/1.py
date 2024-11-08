# Escreva um programa que use uma pilha para testar strings de entrada e determinar
# se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma
# forma de frente para trás e de trás para a frente; por exemplo, arara.

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo = self.topo  
        self.topo = novo_no 

    def desempilhar(self):
        if not self.esta_vazia():
            item = self.topo.dado 
            self.topo = self.topo.proximo  
            return item
        return None

    def esta_vazia(self):
        return self.topo is None

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
        entrada = input("Digite uma palavra ou digite 'stop' para encerrar o programa: ").lower()
        if entrada == "stop":
            print("Programa encerrado!")
            break
        if not entrada.isalpha():  
            print("Insira uma palavra válida (apenas letras)!")
            continue
        if eh_palindromo(entrada):
            print(f'"{entrada}" é um palíndromo.')
        else:
            print(f'"{entrada}" não é um palíndromo.')

main()
