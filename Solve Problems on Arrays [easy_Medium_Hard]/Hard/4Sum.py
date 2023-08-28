def Quads( nums, target):
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i] + nums[j]+ nums[k]+nums[l] == target:
                                temp = [nums[i], nums[j], nums[k], nums[l]]
                                temp.sort()
                                ans.add(tuple(temp))   
        return [list(x) for x in ans]



def fourSum(nums ,target):
    n = len(nums) # size of the 
    ans = []

    # sort the given array:
    nums.sort()

    # calculating the quadruplets:
    for i in range(n):
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1

                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1

    return ans




arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]

ans = Quads(arr,9)
print(ans)

print(fourSum(arr, 9))

