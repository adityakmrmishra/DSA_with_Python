#  OPTIMAL APPROCH
def findLargestElement(arr):
    max=arr[0]
    for i in range(len(array)):
        if max < arr[i]:
            max = arr[i]
    return max
        
#BRUTE FORCE 
def findLargestElement2(array):
    array.sort()
    return array[-1]


# array=[] 
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
max = findLargestElement(array)
print("The largest element in the array is:", max)
print("The largest element in the array is by Brutforce :", findLargestElement2(array))
