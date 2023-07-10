
def Merge_Sort(array,beg,end):
    if beg >= end:
        return
    mid = (beg + end)//2
    Merge_Sort(array,beg,mid)
    Merge_Sort(array,mid+1,end)
    Merge(array,beg,mid,end)

def Merge(array,beg,mid,end):
    n1=mid-beg+1
    n2=end-mid
    l=[]
    r=[]
    # copy data to temporary arrays

    l = array[beg:mid+1]
    r = array[mid+1:end+1]

# another method for above process

    # for i in range(n1):
    #     l.append(array[beg+i])
    # # print(l)    
    # for j in range(n2):
    #     r.append(array[mid+1+j])
    # # print(r)        

    # Initial values for variables that we use to keep  
    # track of where we are in each array

    i= 0 
    j = 0 
    k = beg

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            array[k]= l[i]
            i=i+1
        else:
            array[k] = r[j] 
            j=j+1
        k=k+1
    while i < len(l):
        array[k] = l[i]
        i=i+1
        k=k+1
    while j < len(r):
        array[k] = r[j]
        j=j+1
        k=k+1




# array = []
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array =  [-2, 45, 0, 11, -9,88,-97,-202,747]
print("The sorted array is: ")
Merge_Sort(array, 0, len(array) -1)  
print(array)  