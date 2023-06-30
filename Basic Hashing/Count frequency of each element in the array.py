# Make a visited array of type boolean.
# Use the first loop to point to an element of the array.
# Initialize the variable count to 1.
# Make that index true in the visited array.
# Run second loop, if we find the element then mark the visited index true and increase the count.
# If the visited index is already true then skip the other steps.

#  Use of two loops 
# def countFreq(arr, n):
#     visited = [False] * n
#     for i in range(n):
#         if (visited[i] == True):
#             continue
#         count = 1
#         for j in range(i + 1, n):
#             if (arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
#         print(arr[i], count)


# Using dict

# def countFreq(arr, n):
#     mp = {}
#     for i in range(n):
#         if arr[i] in mp:
#             mp[arr[i]] += 1
#         else:
#             mp[arr[i]] = 1
#     for x in mp:
#         print(x, mp[x])


# Using counter mwthod from collection

from collections import Counter

def countFreq(arr, n):
    mp = Counter(arr)
    for x in mp:
        print(x, mp[x])

# In this code, we create a Counter object called mp by passing the arr list as an argument to the Counter constructor. The Counter object automatically counts the frequency of each element in the list and stores it as a key-value pair, where the key is the element and the value is its frequency. Then we iterate over the keys of the mp dictionary and print the element and its frequency.     

arr = [10,5,10,15,10,5]
n = len(arr)
# print(Counter(arr))
countFreq(arr, n)