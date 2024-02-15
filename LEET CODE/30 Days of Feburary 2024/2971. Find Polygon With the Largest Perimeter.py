class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res=-1
        sumt=0
        for i in nums:
            if sumt>i:
                res=max(res,sumt+i)
            sumt=sumt+i
        return res
        ### BACK TRACKING ##
        nums.sort()
        x=sum(nums)
        for i in range(len(nums)-1,-1,-1):
            x=x-nums[i]
            if nums[i]<x:
                return x+nums[i]
        return -1