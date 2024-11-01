'''Uma estrutura de dados mantém informações sobre rodovias do estado de SC e as
cidades pelas quais uma rodovia passa. Um exemplo desta estrutura é mostrado
abaixo:

a. defina as estruturas que julgar necessárias para implementar este modelo;
b. implemente uma função insereCidade(nomeRodovia string, nomeCidade string)
que insere uma cidade na lista de cidades de uma rodovia, mantendo sempre
ordenada a lista de cidades;
c. implemente uma função rodoviasCidade(nomeCidade string) que retorna uma
lista encadeada com os nomes de todas as rodovias que passam pela cidade
nomeCidade;
d. implemente uma função Cruzamento(nomeRodovia1 string, nomeRodovia2
string) que retorna verdadeiro se as duas rodovias se cruzam em alguma cidade,
ou falso, caso contrário. Considere que as listas de cidades estão ordenadas!
Obs.: ^ representa NULL'''

from highwayQueue import HighwayQueue
from highway import Highway

highwayQueue:HighwayQueue = None

def menu():
    print("1 - Inserir cidade")
    print("2 - Rodovias que passam por uma cidade")
    print("3 - Cruzamento de rodovias")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def findHighway(highway):
    return highwayQueue.searchHighway(highway)


def insereCidade(nomeRodovia: str, nomeCidade: str):
    #Caso a rodovia ainda não exista
    if not findHighway(nomeRodovia):
        highwayQueue.push(nomeRodovia)
    
    highway:Highway = findHighway(nomeRodovia)
    highway.append(nomeCidade)
        


def main():
    global highwayQueue
    highwayQueue = HighwayQueue()
    
    while True:
        option = menu()
        
        if option == "1":
            cityName =  input("Nome da cidade: ")
            highwayName =  input("Nome da rodovia: ")
            insereCidade(highwayName, cityName)
        elif option == "2":
            highwayQueue.print()
        # elif option == "3":
            
        else:
            print("Saindo do programa...")
            break
        
main()