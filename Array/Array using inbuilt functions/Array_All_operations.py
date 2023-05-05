#ARRAY

# Basic Operations

# The basic operations supported by an array are as stated below −
# Traverse − print all the array elements one by one.
# Insertion − Adds an element at the given index.
# Deletion − Deletes an element at the given index.
# Search − Searches an element using the given index or by the value.
# Update − Updates an element at the given index.

#Array is created in Python by importing array module to the python program. Then, the array is declared as shown below −

# from array import *

# arrayName = array(typecode, [Initializers])

# Typecode	                Value
#      b	        Represents signed integer of size 1 byte
#      B	        Represents unsigned integer of size 1 byte
#      c	        Represents character of size 1 byte
#      i	        Represents signed integer of size 2 bytes
#      I	        Represents unsigned integer of size 2 bytes
#      f	        Represents floating point of size 4 bytes
#      d	        Represents floating point of size 8 bytes


from array import *

print("The Array is :") 
arr = array('i', [10,20,30,40,50])
for x in arr:
    print(x, end=' ')
print('\n')

# Accessing Array Element

# We can access each element of an array using the index of the element.  
print("First and fourth elment of the arr are :")  
print(arr[0])
print(arr[3])
print('\n')


# Insertion Operation

# Insert operation is to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array.

# Here, we add a data element using the python in-built insert() method
# insert(i,element)
# i= position 

# insert new item at the beginning of the array
arr.insert(0,2)
for x in arr:
    print(x, end=' ')
print('\n')    
# insert new item at the middle of the array
arr.insert(3,4)
for x in arr:
    print(x, end=' ')
print('\n')    
# insert new item at the last of the array
arr.insert(7,5)
for x in arr:
    print(x, end=' ')
print('\n')    


# Deletion Operation


# Deletion refers to removing an existing element from the array and re-organizing all elements of an array.

# Here, we remove a data element using the python in-built remove() method.
# remove(item)

print("Deleting 5 from the given array")
arr.remove(5)
for x in arr:
    print(x, end=' ')
print('\n')  


# Search Operation

# You can perform a search for an array element based on its value or its index.

# Here, we search a data element using the python in-built index() method.

pos = arr.index(30)
print("Element is present at position:", pos)

print('\n') 

# Update Operation

# Update operation refers to updating an existing element from the array at a given index.

# Here, we simply reassign a new value to the desired index we want to update.

arr[2] =100

for x in arr:
    print(x, end=' ')
print('\n') 