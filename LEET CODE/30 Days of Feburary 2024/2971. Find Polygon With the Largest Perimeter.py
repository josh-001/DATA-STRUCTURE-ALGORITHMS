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
        