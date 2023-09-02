# Implement Upper Bound
# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.

def upperBound(a, target,low , high):

    if low > high:
        return -1

    mid= (low + high) // 2

    if a[mid] > target:
        return mid
    elif a[mid] >= target:
        return upperBound(a, target,low , mid-1)
    else:
        return upperBound(a, target,mid+1, high)
    


def upperbound(arr, n, t):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > t:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans    




a = [3, 5, 8, 15, 19]
target = 9
ind = upperBound(a, target,0 , len(a)-1)
if ind == -1:
    print("The target is not present.")
else:
    print("The target is at index:", ind)



arr = [3, 5, 8, 15, 19]
n = 5
x = 9
ind = upperbound(arr, n, x)
print("The lower bound is the index:", ind)    
