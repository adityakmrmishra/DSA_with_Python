# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

#explanation of below code

# The code defines a function called nextPermutation that takes a list of numbers (nums) as an input and returns the next lexicographic permutation of the list as an output.
# The function starts by finding the length of the list (n) and then loops backwards from the end of the list to the second element (for i in range(len(nums)-1,0,-1)).
# In each iteration, it checks if the current element is greater than the previous one (if nums[i] > nums[i-1]). If so, it means that there is a possible permutation that is larger than the current one.
# Then, it finds the smallest element in the right part of the list that is larger than the previous element (while j < n and nums[j] > nums[i-1]). It stores the index of that element in a variable called idx.
# It swaps the previous element with the element at idx (nums[idx], nums[i-1] = nums[i-1], nums[idx]). This creates a new list that is slightly larger than the original one.
# It sorts the right part of the list in ascending order (nums[i:] = sorted(nums[i:])). This ensures that the new list is the smallest possible permutation that is larger than the original one.
# It returns the new list as the output (return  nums).
# If no such permutation exists, it means that the list is already in descending order and there is no larger permutation possible. In that case, it reverses the list and returns it as the output (return nums.reverse()).

def nextPermutation(nums):
        n = len(nums)
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                j = i
                while j < n and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                nums[i:] = sorted(nums[i:])
                return  nums
        return nums.reverse()


from itertools import permutations

def next_permutation(array):
    l=[i for i in range(1,len(array)+1)]
    perm = permutations(l)
    print(perm)
    p = list(perm)
    # Print the obtained permutations
    print(p)
    # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    for i in range(len(p)-1):
        if p[i] == tuple(array):
            return list(p[i+1])
        if  tuple(array) == p[-1]:
            return list(p[0])



arr = [2,1,3]
print(next_permutation(arr))    
print(nextPermutation(arr))    