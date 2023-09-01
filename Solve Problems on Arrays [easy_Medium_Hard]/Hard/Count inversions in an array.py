# Count inversions in an array
# Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).

# What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].


def merge(arr, low, mid, high):
    temp=[]
    l=low
    r=mid+1

    
    cnt = 0     # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while (l <= mid and r <= high):
        if (arr[l] <= arr[r]):
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            cnt += (mid - l + 1)  # Modification 2
            r += 1

    # if elements on the left half are still left
    while (l <= mid):
        temp.append(arr[l])
        l += 1

    # if elements on the right half are still left
    while (r <= high):
        temp.append(arr[r])
        r += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt   # Modification 3




def numberOfInversions(a, low, high):
    cnt= 0
    if low >=high:
        return cnt
    mid = (low + high) // 2
    cnt += numberOfInversions(a, low, mid)    # left half
    cnt += numberOfInversions(a, mid + 1, high)  # right half
    cnt += merge(a, low, mid, high)  # merging sorted halves
    return cnt


n = 5
a = [5, 4, 3, 2, 1]
cnt = numberOfInversions(a,0, n-1)
print("The number of inversions are:", cnt)