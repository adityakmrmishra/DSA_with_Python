def rev_array(arr,i):
    if i >= len(arr)//2:
        return 
    arr[i] , arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    
    return rev_array(arr, i+1)

arr =[1,2,3,4,5,6,7,8,9,10]
rev_array(arr,0)
print(arr)
