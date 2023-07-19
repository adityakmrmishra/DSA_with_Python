def find_union(a,b):
    i= j = k = 0
    union = []
    while(i <len(a) and j <len(b)):
        if (a[i] <= b[j]):
            if (len(union) == 0  or union[-1] != a[i]):
                union.append(a[i])
            # print(union)
            i+=1
            k+=1
        else:
            if (len(union) == 0  or union[-1] != b[j]):
                union.append(b[j])
            j+=1
            # print(union)
            k+=1   
    # print(union)
    
    while (i < len(a)):
        if (len(union)== 0  or union[-1] != a[i]):
                union.append(a[i])
        i+=1
        k+=1
        # print(union)
        
    while (j < len(b)): 
        if(len(union)== 0  or union[-1] != b[j]):
                union.append(b[j])
        j+=1 
        k+=1
        # print(union)  

    return union


# another method 
def find_union_m2(arr1, arr2):
    res = []
    for i in arr1:
        if i not in res:
            res.append(i)
    for i in arr2:
        if i not in res:
            res.append(i)
    return res



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]


print("Union of arr1 and arr2 is:")
print(find_union(arr1, arr2))
print(find_union_m2(arr1, arr2))


