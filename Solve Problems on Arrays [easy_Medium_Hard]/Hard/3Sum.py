# 3 Sum : Find triplets that add up to a zero
# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.


def triplet( nums, target):
        num_list = list(range(len(nums)))
        trip=[]
        for indx, i in enumerate(num_list):
            for j in num_list[indx+1:]:
                for k in num_list[indx+2:]:
                    if nums[i] + nums[j]+ nums[k] == target:
                        trip.append([nums[i], nums[j], nums[k]])
                    else:
                        continue;
        return trip



arr = [-1, 0, 1, 2, -1, -4]

ans = triplet(arr,0)
print(ans)