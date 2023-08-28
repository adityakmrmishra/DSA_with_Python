def InsertionSort(array,n,index):
    if index == n:
        return array
    j = index
    while j >  0 and array[j-1] > array[j] :
        array[j-1], array[j] = array[j], array[j-1]
        print(array)
        j-=1
    return InsertionSort(array, n , index+1)

# array = []
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]

print("The sorted array is: ", InsertionSort(array,len(array),0))
