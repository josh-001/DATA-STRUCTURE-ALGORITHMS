class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r=1
        while r<len(nums):
            if nums[r]==nums[r-1]:
                nums.pop(r)
            else:
                r=r+1
        print(nums)






class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                j=j+1
                nums[j]=nums[i]
        return j+1


      