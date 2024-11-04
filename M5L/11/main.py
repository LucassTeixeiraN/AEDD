'''11. Faça um programa que cadastre em uma pilha vários números. A entrada deles será
finalizada com a digitação de um número menor ou igual a zero. Posteriormente, o
programa deve gerar duas filas: a primeira com os números pares e a segunda, com
os números ímpares. A saída do programa deve apresentar a pilha digitada e as filas
geradas. Caso alguma das filas seja vazia, deve-se mostrar a mensagem.'''

from numberQueue import NumberQueue
from numberStack import NumberStack

def menu():
    print("1. Criar pilha")
    print("2. Remover número da pilha")
    print("3. Remover número da fila de pares")
    print("4. Remover número da fila de impares")
    print("5. Ver listas")
    print("0. Sair")
    
    option = input("Escolha uma opção: ")
    return option
    
    
def createStack():
    stack = NumberStack()
    evenQueue = NumberQueue()
    oddQueue = NumberQueue()
    while True:
        try:
            number = int(input("Digite um número para adicionar à pilha: "))
            if number > 0:
                stack.push(number)
                if number % 2 == 0:
                    evenQueue.push(number)
                else:
                    oddQueue.push(number)
            else:
                return stack, evenQueue, oddQueue                
        except ValueError:
            print("Valor inválido")            
            
            

def main():

    
    while True:
        option = menu()
        
        if option == "1":
            stack, evenQueue, oddQueue = createStack()
        elif option == "2":
            stack.pop()
        elif option == "3":
            evenQueue.pop()
        elif option == "4":
            oddQueue.pop()
        elif option == "5":
            stack.showStack()
            evenQueue.showqueue("pares")
            oddQueue.showqueue("impares")
        elif option == "0":
            print("Fechando programa...")
            break
        else:
            print("Opção inválida")
        

main()