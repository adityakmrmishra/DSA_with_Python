def is_Sorted(array):
    a = array.copy()
    array.sort()
    if a == array:
        return True
    return False

def isSorted(array):
    for i in range(len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

# array=[] 
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]

# [-202, -97, -9, -2, 0, 11, 45, 88, 747]

# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))

print("not better approch")
print(is_Sorted(array))

print("Optimal approch")
print(isSorted(array))