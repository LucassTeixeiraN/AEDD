# 5. Dada a função abaixo, determine a complexidade:

def tem_duplicacao(array, n): #1
    for i in range(n): #n + 1
        val = array[i] #n
        j = i + 1 #n
        while j < n: #n(n + 1)
            if array[j] == val: #n*n
                return True#1
            j += 1#n*n
    return False #1
#3n² + 4n + 4
#O(n²)
        
def main():
    array = [1,2,3,4]
    print(tem_duplicacao(array, len(array)))

main()
