# Approach:

# Take a variable i as 0;
# Use a for loop by using a variable ‘j’ from 1 to length of the array.
# If arr[j] != arr[i], increase ‘i’ and update arr[i] == arr[j].
#  After completion of the loop return i+1, i.e size of the array of unique elements.

def remove_Duplicates(array):
    i = 0
    for j in range(1,len(array)):
            if array[j] != array[i]:
                i+=1
                array[i] = array[j]
    arr = array[:i+1]        
    return arr        


# array=[] 

# [-202, -97, -9, -2, 0, 11, 45, 88, 747]

# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array =  [1,2,2,2,4,5,6,6]
print(remove_Duplicates(array))