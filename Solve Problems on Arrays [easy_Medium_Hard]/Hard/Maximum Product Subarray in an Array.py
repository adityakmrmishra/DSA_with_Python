# Maximum Product Subarray in an Array
# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.


def maxProductSubArray(nums):
    result = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            result = max(result, prod)
    return result


def maxProductSubArr(nums):
    prod1 = nums[0]
    prod2 = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        prod1  = max(nums[i], prod1 * nums[i], prod2 * nums[i])
        prod2 = min(nums[i], prod1 * nums[i], prod2 * nums[i])

        result = max(result, prod1)

    return result



if __name__ == "__main__":
    nums = [1, 2, -3, 0, -4, -5]
    print("The maximum product subarray:", maxProductSubArray(nums))
    print("The maximum product subarray:", maxProductSubArr(nums))