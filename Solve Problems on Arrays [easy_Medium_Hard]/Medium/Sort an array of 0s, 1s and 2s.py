# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# method 1
def sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array


def Sort_0_1_2(arr):
    low=0
    mid=0
    high=len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            mid +=1
            low +=1

        elif arr[mid] == 1:
            mid+=1

        elif arr[mid] == 2 :
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1
        else:
            print("arr not valid ") 
    return arr         

arr = [2,0,2,1,1,0]
print(sort(arr))
print(Sort_0_1_2(arr))