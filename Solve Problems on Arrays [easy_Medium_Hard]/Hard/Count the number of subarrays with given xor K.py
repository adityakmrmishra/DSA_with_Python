# Count the number of subarrays with given xor K
# Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.


from collections import defaultdict

def subarraysWithXorK(a,s):
    xr = 0
    mpp = defaultdict(int) # declaring the dictionary.
    mpp[xr] = 1 # setting the value of 0.
    cnt = 0
    
    for i in range(len(a)):
        # prefix XOR till index i:
        xr = xr ^ a[i]

        # By formula: x = xr^k:
        x = xr ^ s
        # print("'",x,"'")

        # add the occurrence of xr^k
        # to the count:
        cnt += mpp[x]
        # print(xr)

        # Insert the prefix xor till index i
        # into the dictionary:
        mpp[xr] += 1

    return cnt



k= 6
array =[4,2,2,6,4]
ans = subarraysWithXorK(array, k)
print("The number of subarrays with XOR k is:", ans)