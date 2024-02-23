class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=(Counter(nums))
        t=0
        a=[]
        b=dict(sorted(x.items(), key=lambda x:x[1], reverse=True))
        print(b)
        for i in b:
            if t<k:
                a.append(i)
                t=t+1
        return a

            
        