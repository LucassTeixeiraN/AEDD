# 15. Escreva um algoritmo que receba um vetor ordenado e um número extra e insira esse
# número na sua posição correta no vetor ordenado, deslocando os outros números, se
# necessário. Qual é a complexidade no melhor e no pior caso deste algoritmo?

def inserirNumero(vetor, n, numero):
    for i in range(n):
        if numero < vetor[i]: 
            vetor.insert(i, numero)
            break
    else:
        vetor.append(numero)
    return vetor
# Melhor caso O(1)
# Pior caso O(n)
# O melhor caso ocorre quando o número inserido é o menor que todos os números da lista, então ele é inserido no primeiro termo

def main():
    vetor = [1,5,7,9,10,12]
    numero = 8

    print(inserirNumero(vetor, len(vetor), numero))
main()