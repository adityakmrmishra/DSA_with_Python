def Left_Rotate_By_D_Place(array,n):
    for i in range(0,n):
        first = array[0]
        for j in range(0,len(array)-1):
            array[j] = array[j+1]
        array[len(array)-1] = first
    return array    

def Left_Rotate_One_Place(array):
    first = array[0]
    for j in range(0,len(array)-1):
        array[j] = array[j+1]
    array[len(array)-1] = first
    return array 
#uncomment the below code for user input

# array=[] 
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]

print(Left_Rotate_One_Place(array))

# n tells the no. of times an array will be rotated
n=1
#we get the remainder by dividing the n by size of array as if the n is equal to size of input array than the array will we same as orignal array after rotation so we only do the rotation of the remaing n after dividing ex. n= 10 therefore: n = 10 % 9 => 1 so we will rote array by one place 
n=n % len(array)
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
print(Left_Rotate_By_D_Place(array,n)) 