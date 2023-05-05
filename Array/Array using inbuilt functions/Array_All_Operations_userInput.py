# CREATING ARRAY

from array import *

print("CHOOSE THE OPTION")
print("1. CREATE THE ARRAY")
print("2. ACCESS ANY ELMENT WITH ITS INDEX NO.")
print("3. INSERTION OPERATION")
print("4. DELETE ITEM OF ARRAY")
print("5. SEARCH AN ITEM OF ARRAY")
print("6. UPDATE AN ITEM OF ARRAY")
print("7. EXIT")

while True:

    c=int(input("enter your choice: "))

    if c == 1:
        a=[]
        n=int(input("Enter the number of elements in array:"))
        print("Enter the elements of array")
        for i in range(0,n):
            item=int(input())
            a.append(item)
        print("The Array is :") 
        arr = array('i', a)
        for x in arr:
            print(x, end=' ')
        print('\n')

    elif c==2:
        #  Accessing Array Element

        # We can access each element of an array using the index of the element.  
        a =int(input("Enter the position of the element you want to access:"))
        print(arr[a])

        print('\n')

    elif c == 3:
        # Insertion Operation

        # Insert operation is to insert one or more data elements into an array. Based on the requirement, a new element can be added at the beginning, end, or any given index of array.

        # Here, we add a data element using the python in-built insert() method
        # insert(P,element)
        # P= position 

        P=int(input("Enter the position of the element you want to insert in array: "))
        item=int(input("Enter the item you want to insert: "))
        arr.insert(P,item)
        print("The New Array after insertion is :") 
        for x in arr:
            print(x, end=' ')
        print('\n')  

    elif c == 4:
        # Deletion Operation


        # Deletion refers to removing an existing element from the array and re-organizing all elements of an array.

        # Here, we remove a data element using the python in-built remove() method.
        # remove(item)

        item=int(input("Enter the item you want to delete: "))    
        arr.remove(item)
        print("The New Array after deletion is :")
        for x in arr:
            print(x, end=' ')
        print('\n')

    elif c == 5:
        # Search Operation

        # You can perform a search for an array element based on its value or its index.

        # Here, we search a data element using the python in-built index() method.
        item=int(input("Enter the item you want to search: "))   
        pos = arr.index(item)
        print("Element is present at position:", pos)

        print('\n') 

    elif c == 6:
        # Update Operation

        # Update operation refers to updating an existing element from the array at a given index.

        # Here, we simply reassign a new value to the desired index we want to update.
        item=int(input("Enter the item position you want to update: ")) 
        new_value=int(input("Enter the new value: "))
        arr[item] = new_value

        for x in arr:
            print(x, end=' ')
        print('\n')     

    elif c == 7:
        print(exit())

    else:
        print("Invalid choice!")