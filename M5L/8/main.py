'''Faça um programa que cadastre n números em uma fila dinâmica e mais n em uma
pilha dinâmica. Em seguida, o programa deve mostrar 3 relatórios. O primeiro terá os
números que estão nas duas estruturas. O segundo terá os que estão apenas na fila e
o terceiro terá os que estão apenas na pilha.'''

from filaLigada import FilaLigada
from pilhaLigada import PilhaLigada

def gerar_relatorios(fila, pilha):
    conjunto_fila = set(fila)
    conjunto_pilha = set(pilha)

    em_ambas = sorted(list(conjunto_fila & conjunto_pilha))
    apenas_na_fila = sorted(list(conjunto_fila - conjunto_pilha))
    apenas_na_pilha = sorted(list(conjunto_pilha - conjunto_fila))

    print("\nRelatório 1 - Números presentes em ambas as estruturas:")
    print(em_ambas if em_ambas else "Nenhum número em comum")

    print("\nRelatório 2 - Números presentes apenas na fila:")
    print(apenas_na_fila if apenas_na_fila else "Nenhum número presente apenas na fila")

    print("\nRelatório 3 - Números presentes apenas na pilha:")
    print(apenas_na_pilha if apenas_na_pilha else "Nenhum número presente apenas na pilha")

def cadastrar_numeros_na_fila(fila, numeros):
    for num in numeros:
        fila.enqueue(num)

def cadastrar_numeros_na_pilha(pilha, numeros):
    # Para garantir que a pilha exiba 8, 7, 6, devemos empilhar na ordem inversa
    for num in reversed(numeros):
        pilha.push(num)

def main():
    # Definindo números para a fila e a pilha
    numeros_fila = [1, 2, 3, 4, 5]  
    numeros_pilha = [4, 5, 6, 7, 8]  # Mudamos para uma lista que já está na ordem correta

    # Criando as estruturas de dados
    fila = FilaLigada()
    pilha = PilhaLigada()

    # Cadastrando os números nas estruturas
    cadastrar_numeros_na_fila(fila, numeros_fila)
    cadastrar_numeros_na_pilha(pilha, numeros_pilha)

    # Convertendo as estruturas para listas
    lista_fila = fila.to_list()
    lista_pilha = pilha.to_list()

    # Gerando os relatórios
    gerar_relatorios(lista_fila, lista_pilha)

if __name__ == "__main__":
    main()
