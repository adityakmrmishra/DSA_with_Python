def selection_sort(array):  
    for i in range(len(array)):
        min = i 
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min =j
        array[i] , array[min] = array[min], array[i]

    return array        


array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
# array=[] 
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))


print("The sorted array is: ", selection_sort(array))  