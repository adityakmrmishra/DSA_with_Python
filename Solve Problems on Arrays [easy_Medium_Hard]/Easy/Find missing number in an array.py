def missing_numbers(a):
    m = []
    for ele in range(1, a[-1]+1):
        if ele not in a:
            m.append(ele)

    return m 


array= [ 2,3,5,7,13]
print("the missing numbers are:", missing_numbers(array))