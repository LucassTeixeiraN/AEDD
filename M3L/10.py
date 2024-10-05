'''10. Faça um programa que cadastre n números, ordene-os pelo bubbleSort e em seguida
encontre e mostre:
a. O menor número e quantas vezes ele aparece no vetor.
b. O maior número e quantas vezes ele aparece no vetor.'''

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubbleSort(list):
    n=len(list)
    while n>1:
        swapped = False
        i = 1
        while i< n:
            if list[i] < list[i-1]:
                swap(list, i, i-1)
                swapped = True
            i+=1
        if not swapped: break
        n-=1

def cadastrarNumeros(n):
    lista = []
    for _ in range(n):
        lista.append(input())
    return lista

def menorNumero(lista, min, n):
    if not lista:
        return n
    elif lista[0] == min:
        return menorNumero(lista[1:], min, n + 1)
    else:
        return menorNumero(lista[1:], min, n)
    
def maiorNumero(lista, max, n):
    if not lista:
        return n
    elif lista[-1] == max:
        return menorNumero(lista[:len(lista)-1], min, n + 1)
    else:
        return menorNumero(lista[:len(lista)-1], min, n)

def main():
    lista = cadastrarNumeros(int(input("Insira quantos números a lista terá: ")))
    bubbleSort(lista)
    print(f"O menor número é {lista[0]} e ele aparece {menorNumero(lista, lista[0], 0)} vezes")
    print(f"O maior número é {lista[-1]} e ele aparece {menorNumero(lista, lista[-1], 0)} vezes")

main()
