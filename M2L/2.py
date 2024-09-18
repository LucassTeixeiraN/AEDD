elem=10
array=[9,8,7,6,5,4,3,10]

def find_element(array , n, elem):
    for i in range (n): # rodará até n
        if array[i]==elem:# rodará até array i = elem 
            return True
        return False
    
# equação = 2n
# O(n)
