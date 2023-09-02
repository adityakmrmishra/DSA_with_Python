# Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.


# Note:

# Binary search is only applicable in a sorted search space. The sorted search space does not necessarily have to be a sorted array. It can be anything but the search space must be sorted.
# In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.



def binarySearch(a, target,low , high):
    if low > high:
        return -1

    mid= (low + high) // 2

    if a[mid] == target:
        return mid
    elif a[mid] > target:
        return binarySearch(a, target,low , mid-1)
    else:
        return binarySearch(a, target,mid+1, high)
    
    



a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
ind = binarySearch(a, target,0 , len(a)-1)
if ind == -1:
    print("The target is not present.")
else:
    print("The target is at index:", ind)






# Let’s derive the number of divisions mathematically,

# If a number n can be divided by 2 for x times:
# 	2^x = n
# Therefore, x = logn (base is 2)
# So the overall time complexity is O(logN), where N = size of the given array.