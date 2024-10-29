import random


def binary_search(array, target):
    """Realiza uma busca binária e retorna uma lista com os índices onde o elemento foi encontrado."""
    left, right = 0, len(array) - 1
    positions = []
    
    
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
        
            positions.append(mid)
           
            i = mid - 1
            while i >= 0 and array[i] == target:
                positions.append(i)
                i -= 1
       
            i = mid + 1
            while i < len(array) and array[i] == target:
                positions.append(i)
                i += 1
            break
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return sorted(positions)

def find_in_matrix(matrix, target):
    
    flat_matrix = []
    index_map = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            index = i * len(matrix[0]) + j
            flat_matrix.append(matrix[i][j])
            index_map[index] = (i, j)
    
    sorted_flat_matrix = sorted(flat_matrix)
    
    positions_in_flat = binary_search(sorted_flat_matrix, target)
    
    # Converte os índices da lista achatada para posições na matriz original
    matrix_positions = [index_map[pos] for pos in positions_in_flat]
    
    return matrix_positions



linhas, colunas = 500, 50
matriz = [[random.randint(1, 10000) for _ in range(colunas)] for _ in range(linhas)]

print(matriz)


target = random.choice([elem for row in matriz for elem in row])
print("\nNúmero sorteado:", target)

positions = find_in_matrix(matriz, target)

if positions:
    print("\nNúmero de ocorrências:", len(positions))
    print("Posições na matriz:", positions)
else:
    print("\nO número não foi encontrado na matriz.")
