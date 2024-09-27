'''1. Implemente um programa estruturado e recursivo para pesquisa linear. Faça uma
função de busca chamada pesquisaLR que receba como parâmetro o valor a ser
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1,
caso não encontre o item, ou retornará o índice, caso o encontre.'''

def pesquisaLR(target, vetor, position = 0):
    if position == len(vetor):
        return -1
    if target == vetor[position]:
        return position
    
    return pesquisaLR(target, vetor, position + 1)

def main():
    target = 5
    vetor = [1,2,3,4]
    print(pesquisaLR(target, vetor))

main()