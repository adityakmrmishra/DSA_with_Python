def Longest_Subarray_Sum(a,s):
    dict={}
    curr_sum = 0
    maxLen = 0
    for i in range(len(a)):
        # calculate the sum till index i:
        curr_sum += a[i]
        # if the sum = k, update the maxLen:
        if curr_sum == s:
            maxLen = max(maxLen, i + 1)
            print("Subarray with sum ",s ,"starts from 0 to ",i,"and maxLen is ",maxLen)
        # Calculate the length and update maxLen:
        if curr_sum -s in dict:
            length = i - dict[curr_sum -s]
            maxLen = max(maxLen, length)
            print("Subarray with sum",s ,"starts from ",dict[curr_sum - s]+1," to ",i,"and Len is ",length)
        # Finally, update the dict checking the conditions:
        if curr_sum not in dict: 
            dict[curr_sum] = i
    print()
    print("The length of the longest subarray with sum '", s ,"' is :-",maxLen)
s= 10
array =[2, 3, 5, 1, 9]
Longest_Subarray_Sum(array,s)
