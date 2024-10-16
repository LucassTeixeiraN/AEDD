'''Implemente um programa estruturado e recursivo para pesquisa binária. Faça uma
função de busca chamada pesquisaBR que receba como parâmetro o valor a ser
encontrado e a referência do vetor onde a busca será efetuada. A função retornará -1,
caso não encontre o item, ou retornará o índice, caso o encontre.'''

def pesquisaBR(value, sorted_array, start, end):
    if start > end:
        return -1
    
    mid_point = (start + end) // 2
    if sorted_array[mid_point] == value:
        return mid_point
    elif sorted_array[mid_point] < value:
        return pesquisaBR(value, sorted_array, mid_point + 1, end)
    else:
        return pesquisaBR(value, sorted_array, start, mid_point - 1)
    
def main():
    value = 11
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(pesquisaBR(value, array, 0, len(array) - 1))
    
main()