# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

def print_leader(a):
    l=[]
    for i in range(len(a)):
        leader = True
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                leader = False
                break
        if leader:
            l.append(a[i])    
    return l

def get_leader(a):
    l=[]
    leader = a[-1]
    l.append(leader)
    for i in range(len(a)-2,-1,-1):
        if a[i] > leader:
            leader = a[i]
            l.append(a[i])
    return l        

arr = [4, 7, 1, 0]
print(print_leader(arr))
print(get_leader(arr))
