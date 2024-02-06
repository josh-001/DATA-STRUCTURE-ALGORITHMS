class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i=0
        j=0
        while len(s)<(len(word1)+len(word2)):
            if i<len(word1):
                s=s+word1[i]
                i=i+1
            if j<len(word2):
                s=s+word2[j]
                j=j+1
        return s