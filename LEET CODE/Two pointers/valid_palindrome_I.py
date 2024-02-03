class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        n=len(prices)
        # x=prices[:n-1]
        # #get the minimum value
        # a=min(x)
        # ##get the index of a
        # b=prices.index(a)
        # # print(b)
        # s=0
        # for i in range(n-1,b-1,-1):
        #     c=prices[i]-a
        #     if c>s:
        #         s=c

        # s=0
        # for i in range(0,n):
        #     a=prices[i]-s
        #     if a>s:
        #         s=a
        l,r=0,1
        s=0
        while r<len(prices):
            if prices[l]<prices[r]:
                x=prices[r]-prices[l]
                s=max(s,x)
            else:
                l=r
            r=r+1
        return s