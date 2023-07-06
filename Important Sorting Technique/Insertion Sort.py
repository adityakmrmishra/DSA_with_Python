def InsertionSort(array):
    for i in range(1, len(array)):

        temp = array[i]
        j = i-1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array

# array = []
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]

print("The sorted array is: ", InsertionSort(array))
