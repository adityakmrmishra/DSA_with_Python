def Max_conse_one(a):
    c =0
    max_c = 0
    for i in range(len(array)) :
        if a[i] == 1 :
            c+=1
        else :
            c =0     
        max_c= max(c,max_c)
    return max_c           


array = [1,1,1,0,1,1]
print(Max_conse_one(array))
