def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array


array=[] 
# array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
n = int(input("Entser the size of array :"))
print("Enter the array you want to sort:")
for i in range(n):
    array.append(int(input()))


print("The sorted array is: ", bubble_sort(array))  


