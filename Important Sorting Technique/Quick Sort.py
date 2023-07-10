def partition(array,lb,ub):
    pivot = array[ub]
    i=lb-1
    for j in range(lb,ub):
        if array[j] <= pivot:
            i=i+1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[ub]=array[ub],array[i+1]        
    return i+1    


def quickSort(array ,lb,ub):
    if lb<ub:
        m=partition(array,lb,ub)  
        quickSort(array ,lb,m-1) 
        quickSort(array ,m+1,ub) 


# n=int(input("enter the size of array: "))
# print("Enter the elements of the array: ")
# array=[]
# for i in range(0,n):
#     item = int(input())
#     array.append(item)
# print(array)
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
quickSort(array,0,len(array)-1 )
print("Sorted array is : ")
print(array)
