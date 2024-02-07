# class Solution:
#     def frequencySort(self, s: str) -> str:                                                                                                                                                                                                                                                                                          
#         res=defaultdict(list)
#         # char=[0]*52
        
#         for i in s:
#             if i not in res.keys():
#                 res[i]=s.count(i)
#         res=sorted(res.items(),reverse=True)
#         print(res)
#         x=list(res)
#         a=""
#         for i in range(len(x)):
#             j=0
#             while j<x[i][1]:
#                 a=a+x[i][0]
#                 j=j+1
#         return a

                

#             # char[ord(i)-ord("a")]+=1
#             # print(char)
#             # res[tuple(count)].append(i)
#         # print(res)

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        char_count = Counter(s)
        
        # Step 2: Sort characters based on their frequency in descending order
        sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

        # Step 3: Build the result string by repeating characters according to their frequency
        result = ''
        for char in sorted_chars:
            result += char * char_count[char]
        
        # Step 4: Return the final sorted string
        return result