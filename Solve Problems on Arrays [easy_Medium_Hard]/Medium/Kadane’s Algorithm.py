def maxSubarraySum(arr):
    maxi = 0
    sum = 0
    for i in range(len(arr)):
        sum=max(arr[i],sum+arr[i])
        maxi = max(maxi,sum)

    return maxi    

arr = [1, 2, 7, -4, 3, 2, -10, 9 ,1]

print("The maximum subarray sum is:", maxSubarraySum(arr))