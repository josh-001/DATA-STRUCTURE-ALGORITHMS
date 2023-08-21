# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
##ERROR##
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        x=""
        for i in s:
            if i not in x:
                x=x+i
        n=len(s)
        y=len(x)
        a=n//y
        b=""
        if a==1:
            return False
        for i in range(a):
            b=b+x
        if s==b:
            return True
        else:
            return False
  
  a=(s+s)[1:-1]
        return s in a