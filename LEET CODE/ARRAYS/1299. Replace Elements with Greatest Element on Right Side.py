class Solution:
    
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        n=len(arr)
        x=0
        for i in range(n-1):
            if x<=arr[i]:
                x=self.Maxnum(arr[i+1:])
            arr[i]=x
        arr[i+1]=-1
        return arr
    def Maxnum(self,arr):
        maxi=0
        for i in range(len(arr)):
            if maxi<arr[i]:
                maxi=arr[i]
        return maxi