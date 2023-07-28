# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array

def Longest_Subarray_Sum(a,s):
    ma=[]
    dict={}
    curr_sum = 0
    maxLen = 0
    for i in range(len(a)):
        # calculate the sum till index i:
        curr_sum += a[i]
        # if the sum = k, update the maxLen:
        if curr_sum == s:
            maxLen = max(maxLen, i + 1)
            sa=[a[i] for i in range(0,i+1)]
            ma.append(sa)
            print("Subarray with sum ",s ,"starts from 0 to ",i," i.e",sa," and Len is ",maxLen)

        # Calculate the length and update maxLen:
        if curr_sum -s in dict:
            length = i - dict[curr_sum -s]
            maxLen = max(maxLen, length)
            sa = [a[i] for i in range(dict[curr_sum - s]+1,i+1)]
            ma.append(sa)
            print("Subarray with sum",s ,"starts from ",dict[curr_sum - s]+1," to ",i,"i.e",sa," and Len is ",length)
        # Finally, update the dict checking the conditions:
        if curr_sum not in dict: 
            dict[curr_sum] = i
    print()
    return ma
s= 10
array =[2, 3, 5, 1, 9,6,4]
print(Longest_Subarray_Sum(array,s))
