# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input

# ABCDCDC
# CDC
# Sample Output

# 2
# Concept

# Some string processing examples, such as these, might be useful.
# There are a couple of new concepts:
# In Python, the length of a string is found by the function len(s), where  is the string.
# To traverse through the length of a string, use a for loop:

# for i in range(0, len(s)):
#     print (s[i])
# A range function is used to loop over some length:

# range (0, 5)



def count_substring(string, sub_string):
    n=len(sub_string)
    c=0
    for i in range(len(string)-n+1):
        if string[i:i+n]==sub_string:
            c=c+1
    return c
        # if string[i:i+n]==sub_string:
        #     c=c+1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)