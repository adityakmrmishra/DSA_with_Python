#Two Sum : Check if a pair with given sum exists in Array
# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

# Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

def Two_Sum( nums, target):
        num_list = list(range(len(nums)))
        for indx, i in enumerate(num_list):
            for j in num_list[indx+1:]:
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    continue;
        return None 


def TwoSum(arr, t):
    result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == t:
                result.append(i)
                result.append(j)
                print("Yes")
                return result 
    print("No")              
    return [-1, -1]

arr = [2,6,5,8,11]
target = 14
print(TwoSum(arr,target))
print(Two_Sum(arr,target))