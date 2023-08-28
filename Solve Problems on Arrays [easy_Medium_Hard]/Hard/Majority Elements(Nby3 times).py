# Majority Elements(>N/3 times) | Find the elements that appears more than N/3 times in the array
# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. If no such element exists, return an empty vector.


from collections import Counter

def majorityElement(arr):
    n=len(arr)
    maj=[]
    mp = Counter(arr)
    # print(Counter(arr))
    for x in mp:
        # print(x, mp[x])
        if mp[x] > n//3:
            maj.append(x)
    return maj        



arr = [11, 11, 33, 11]
ans = majorityElement(arr)

print("The majority elements are: ", ans)