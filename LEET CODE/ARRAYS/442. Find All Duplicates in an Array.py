# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=Counter(nums)
        b=[]
        for i,j in a.items():
            if j==2:
                b.append(i)
        return b
        # a=[]
        # for i in nums:
        #     if nums.count(i)==2:
        #         a.append(i)
        #         nums.remove(i)
        # a.sort()
        # return a
            # if nums[i] not in a:
            #     a.append(nums[i])
        # b=[]
        # for i in a:
        #     if nums.count(i)==2:
        #         b.append(i)
        # b.sort()
        # return b