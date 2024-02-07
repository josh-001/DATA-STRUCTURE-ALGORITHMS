class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j=j+1
        print(nums1)
        nums1.sort()
        # i=0
        # j=0
        # while i<len(nums1)-1:
        #     if nums1[i]<nums2[j]:
        #         i+=1
        #         # print(i)
        #         continue
        #     else:
        #         # nums1[i+2]=nums1[i+1]
        #         nums1.insert(nums1[i+1],nums2[j])
        #         print(nums1)
        #         j+=1
        #         # print(j)
        # return nums1


        # i,j=0,0
        # a=[]
        # while len(a)<(m+n):
        #     if nums1[i] <nums2[j]:
        #         i+=1
        #         a.append(nums1[i])
        #         continue
        #     else:
        #         a.append(nums2[j])
        #         j+=1
        # return a