'''11. Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados:
nome, nota1 e nota2. Primeiro, liste todos os alunos cadastrados, ordenando-os pela
média ponderada das notas, tendo a primeira nota peso 2 e a segunda, peso 3. Em
seguida, ordene os alunos, de forma crescente, pela nota1, e liste-os. Finalmente,
considerando que, para ser aprovado, o aluno deve ter no mínimo média 7, liste, em
ordem alfabética, os alunos reprovados. Em cada ordenação use um algoritmo
diferente.'''

def cadastrarAlunos(n):
    nomes = []
    notas1 = []
    medias = []
    for i in range(n):
        nome = input("Nome do aluno {}: ".format(i+1))
        nota1 = float(input("Nota 1 do aluno {}: ".format(i+1)))
        nota2 = float(input("Nota 2 do aluno {}: ".format(i+1)))
        media = (nota1*2 + nota2*3)/5
        nomes.append(nome)
        notas1.append(nota1)
        medias.append(media)
        
    return (nomes,notas1,medias)

def swap(lista1, lista2, i, j):
    lista1[i], lista1[j] = lista1[j], lista1[i]
    lista2[i], lista2[j] = lista2[j], lista2[i]

def selectionSort(nomes, medias):
    i = 0
    while i<len(medias) - 1:
        minIndex = i
        j = i+1
        while j < len(medias):
            if medias[j] < medias[minIndex]:
                minIndex = j
            j += 1

        if minIndex != i:
            swap(medias, nomes, minIndex, i)
        i += 1
        
def bubbleSort(nomes, nota):
    n=len(nota)
    while n>1:
        swapped = False
        i = 1
        while i< n:
            if nota[i] < nota[i-1]:
                swap(nota, nomes, i, i-1)
                swapped = True
            i+=1
        if not swapped: break
        n-=1
        
def insertionSort(nomes, medias):
    i = 1
    while i< len(nomes):
        nomeParaInserir = nomes[i]
        mediaParaInserir = medias[i]
        j = i-1
        while j>=0:
            if nomeParaInserir < nomes[j]:
                nomes[j+1] = nomes[j]
                medias[j+1] = medias[j]
                j -= 1
            else:
                break
        nomes[j+1] = nomeParaInserir
        medias[j+1] = mediaParaInserir
        i+=1
        
def abaixoMedia(nomes, media):
    i = 0
    nomesRep = []
    mediasRep = []
    while i < len(media):
        if media[i] < 7:
            nomesRep.append(nomes[i])
            mediasRep.append(media[i])
        i += 1
    return [nomesRep, mediasRep]
    
def main():
    numeroAlunos = int(input("Insira o número de alunos"))
    nomes,notas1,media = cadastrarAlunos(numeroAlunos)
    
    # ordenar pela media
    nomesSelctionSort = nomes.copy()
    selectionSort(nomesSelctionSort, media)
    print("Ordenados pela média:")
    print(nomesSelctionSort,media)
    
    # ordenar pela primeira nota
    nomesBubbleSort = nomes.copy()
    bubbleSort(nomesBubbleSort, notas1)
    print("Ordenados pela primeira nota:")
    print(nomesBubbleSort,notas1)
    
    # alunos reprovados
    print("Alunos reprovados:")
    nomesRep, mediasRep =  abaixoMedia(nomesSelctionSort, media)
    insertionSort(nomesRep, mediasRep)
    print(nomesRep,mediasRep)
    
main()
