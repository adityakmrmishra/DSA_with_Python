# Find Second Smallest and Second Largest Element in an array

# METHOD 1 BRUTEFORCE 

def findSecondLargestElement(array):
    array.sort()
    return array[-2]


def findSecondSmallestElement(array):
    array.sort()
    return array[1]


# METHOD 2 OPTIMAL APPROCH

def findSecondLargestElement2(array):
    if (len(array) < 2):
        return -1
    large = array[0]
    second_large = 0
    for i in range(len(array)):
        if array[i] > large:
            second_large = large
            large = array[i]
        elif (array[i] > second_large and array[i] != large):
            second_large = array[i]    
    return second_large


def findSecondSmallestElement2(array):
    if (len(array) < 2):
        return -1
    small = array[0]
    second_small = 0
    for i in range(len(array)):
        if array[i] < small:
            second_small = small
            small = array[i]
        elif (array[i] < second_small and array[i] != small):
            second_small = array[i]    
    return second_small




# array=[] 
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]

# [-202, -97, -9, -2, 0, 11, 45, 88, 747]

# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))

print("The largest element in the array is  by Brutforce:", findSecondLargestElement(array))
# print(array)
print("The largest element in the array is by Brutforce :", findSecondSmallestElement(array))

print("The Second largest element in the array is:", findSecondLargestElement2(array))
print("The Second Smallest element in the array is :", findSecondSmallestElement2(array))
