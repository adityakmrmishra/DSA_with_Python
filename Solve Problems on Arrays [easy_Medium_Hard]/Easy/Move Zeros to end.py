def Move_Zero(array):
    j = -1
    # Place the pointer j
    for i in range(len(array)):
        if array[i] == 0:
            j = i
            break
    # No non-zero elements
    if j == -1:
        return array    
    
    # Move the pointers i and j and swap accordingly
    for i in range(j+1,len(array)):
            if array[i] != 0:
                array[i] , array[j] = array[j], array[i]
                j+=1    
    return array            


# array=[] 
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
print(Move_Zero(array))