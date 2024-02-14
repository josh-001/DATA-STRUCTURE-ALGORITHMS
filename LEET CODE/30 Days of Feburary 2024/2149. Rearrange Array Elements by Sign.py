class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        ###   BRUTE FORCE  ##
        # a=[]
        # b=[]
        # for i in nums:
        #     if i <0:
        #         a.append(i)
        #     else:
        #         b.append(i)
        # x=[]
        # f=0
        # g=0
        # for i in range(len(nums)):
        #     if i%2==0:
        #         x.append(b[f])
        #         f=f+1
        #     else:
        #         x.append(a[g])
        #         g=g+1
        # return x

        a=[0]*len(nums)
        p=0
        n=1
        for i in nums:
            if i>0:
                a[p]=i
                p+=2
            else:
                a[n]=i
                n+=2
        return a