# Problem Statement:

# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Note: Start the array with positive elements.

# method 1

def Rearrange(a):
    p = []
    n=[]
    for i in range(len(a)):
        if a[i] > 0:
            p.append(a[i])
        else:
            n.append(a[i])    
    
    for i in range(len(a)//2):
        a[2*i] = p[i]
        a[2*i+1] = n[i]
    return a

# method 2
def RearrangebySign(a):
    p , n = 0 , 1
    result = [0]*len(a)
    for i in range(len(a)):
        if a[i] > 0 :
            result[p] = a[i]
            p+=2
        else:
            result[n] =a[i]
            n+=2
    return result            



arr=[1,2,-4,-5]
print(Rearrange(arr))
print(RearrangebySign(arr))