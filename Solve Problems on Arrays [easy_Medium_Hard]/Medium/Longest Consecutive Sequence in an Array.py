# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.


def linearSearch(a, num):
    n = len(a)  # size of array
    for i in range(n):
        if a[i] == num:
            return True
    return False


def longestSuccessiveElements(a):
    if len(a) == 0:
        return 0
    longest = 1
    # pick an element and search for its consecutive numbers
    for i in range(len(a)):
        x = a[i]
        count = 1
        # search for consecutive numbers using linear search
        while linearSearch(a, x + 1):
            x += 1
            count += 1

        longest = max(longest, count)
    return longest


def lse(a):
    if len(a) == 0:
        return 0
    
    longest = 0
    sat = set(i for i in a)

    for i in sat:
        if i-1 not in sat:
            count =1 
            j = i
            while j+1 in sat:
                count+=1
                j+=1
            longest = max(longest,count)    
    return longest

a = [100, 200, 1, 3, 2, 4]
print("The longest consecutive sequence is", longestSuccessiveElements(a))
print("The longest consecutive sequence is",lse(a) )