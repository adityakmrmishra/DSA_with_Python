import ctypes

# ctypes is a library which is used to create the c language data types in python
#so we will use c lang. array here not list of python

class Array:

    def __init__(self):
        self.size = 1
        # size is the size of the array
        self.n = 0
        # n is the number of elements in the array
        # create a new array of c type with size = self.size
        self.A = self.create_array(self.size)

    # MAGIC METHOD TO GET THE LENGTH OF ARRAY
    def __len__(self):
        return self.n
    

    # MAGIC METHOD TO PRINT THE ARRAY
    def __str__(self):
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'  

    # MAGIC METHOD TO GET OR SEARCH THE ITEM WITH THE HELP OF INDEX NO (arr[0])
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'
    
    def append(self,item):
        if self.size == self.n:
            #resize
            self.resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n + 1 
        
    # to delete the last item from array
    def pop(self):
        if self.n == 0:
            return 'Empty list'
        
        print('Deleting', self.A[self.n-1])   
        self.n = self.n - 1

    # to clear all the elements of the array
    def clear(self):
        self.n = 0
        self.size = 1    

    def resize(self,new_size):
        # create a new  array with new_size
        B= self.create_array(new_size)
        self.size = new_size

        #copy the content of the array A to the new array B
        for i in range(self.n):
            B[i] = self.A[i]

        # reassign A
        self.A = B    


    def create_array(self, size):
        # creates a C type array (static and refrential array) with the given size 
        return (size*ctypes.py_object)()
    


arr = Array()
#appending the items to the array 
arr.append(1)
arr.append(2)
arr.append(3)

print("Array is: ",  arr)
arr.pop()
print("Array is: ",  arr)
arr.clear()
print("Array is: ",  arr)

print("item present at the given index is :", arr[0])
print("Length of the array is : ",len(arr))   