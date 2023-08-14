# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        for i in range(len(nums)):
            if nums[i]!=0:
                mul=mul*nums[i]
        if 0 in nums:
            if nums.count(0)>1:
                return [0]*len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i]!=0:
                        nums[i]=0
                    else:
                        nums[i]=mul
        else:
            for i in range(len(nums)):
                nums[i]=mul//nums[i]
        return nums

        
