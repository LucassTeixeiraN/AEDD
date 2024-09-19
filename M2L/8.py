# 8. Dada a função abaixo, determine a complexidade:

def ache_min(array, n): #1
    min = array[0] #1
    for i in range(n): # n+1
        if array[i] < min: #n
            min = array[i] # no melhor dos casos 1 e no pior n
    return min # 1
# 3n + 4
# O(n)

def main():
    array = [5,2,6,7,1,7,10]
    print(ache_min(array, len(array)))

main()
