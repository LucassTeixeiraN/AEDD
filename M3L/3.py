"""3. Um vetor de tamanho n, pode conter elementos do alfabeto e numerais 0 a 9. Escreva
um algoritmo que seja capaz de localizar, pelo método binário, um caractere
fornecido pelo usuário. Se esse caractere for uma letra, o usuário poderá fornecê-la
para a busca no formato maiúsculo ou minúsculo."""

def binarySearch(target, sortedList):
    left = 0
    right = len(sortedList) - 1
    while left <= right:
        midpoint = (left + right)//2
        if target == sortedList[midpoint]:
            return midpoint
        elif target < sortedList[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

def listInput():
    try:
        len = int(input("Insira quantos elementos a lista terá: "))
        print("Insira os elementos da lista (apenas o primeiro caractere de cada elementos será considerado):")
        sortedList = [input()[0] for _ in range(len)]
        return sortedList
    except ValueError:
        print("Valor inválido")
        listInput()

def main():
    target = input("Insira uma letra do alfabeto ou um numeral de 0 a 9 (apenas o primeiro caractere será considerado): ")[0]
    sortedList = listInput()
    sortedList.sort()
    print(sortedList)
    print(binarySearch(target, sortedList))
main()
