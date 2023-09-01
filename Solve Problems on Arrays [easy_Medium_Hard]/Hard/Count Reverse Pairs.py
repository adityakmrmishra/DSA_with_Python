# Count Reverse Pairs
# Problem Statement: Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i<j and arr[i]>2*arr[j].


#easy method brute force

def countPair(a, n):
    # Count the number of pairs:
    l=[]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > 2 * a[j]:
                cnt += 1
                l.append((a[i] ,a[j]))
    return cnt ,l


#optiized method

def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt

def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt



a = [4, 1, 2, 3, 1]
n = 5
cnt = countPair(a, n)
print("The number of reverse pair is:",mergeSort(a,0,n-1))
print("The number of reverse pair is:", cnt[0] ,"and pairs are",cnt[1])


